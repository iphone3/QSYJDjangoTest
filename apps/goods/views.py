from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from goods.models import HotSell, NurseGoods, Brand, ContactLensBanner, ContactLensGoods, Stock
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import UserFavorite
from users.models import UserProfile


class IndexView(View):  # 首页
    def get(self, request):
        return render(request, 'index.html', {'nav_at':'index'})


class ContactView(View):  # 彩瞳
    def get(self, request):
        # 轮播图
        banners = ContactLensBanner.objects.all()

        # 商品
        contact_lens_goods = ContactLensGoods.objects.all()

        arg_dir = {
            'nav_at': 'contact',    # 标签页的使能
            'banners': banners,   # 轮播图
            'contact_lens_goods': contact_lens_goods, # 主体商品
        }

        return render(request, 'contact-lens.html', arg_dir)


class NurseView(View):  # 护理用品
    def get(self, request):
        # 商品品牌
        brands = Brand.objects.all().order_by('key_num')

        # 热销排行榜
        hot_sells = HotSell.objects.all().order_by('goods_nun')

        # 取出筛选品牌
        brand_num = int(request.GET.get('brand_num', '0'))
        if brand_num == 0:  # 全部主体商品
            nurse_goods = NurseGoods.objects.all()
        else:   # 根据品牌获取级联数据
            brand = Brand.objects.get(key_num=brand_num)
            nurse_goods = brand.nursegoods_set.all()

        # 用户是否登录，已登录时，需要将对应收藏信息显示
        user_favorites = None
        if request.user.is_authenticated:
            # 获取用户级联的收藏数据
            user_favorites = request.user.userfavorite_set.all()

        # 排序
        sort = request.GET.get('sort', 'syn')
        if sort == 'sales': # 销售量
            nurse_goods = nurse_goods.order_by('-goods_sales')
        elif sort == 'price':   # 价格
            nurse_goods = nurse_goods.order_by('goods_price')

        # 主体商品
        # nurse_goods = NurseGoods.objects.all()

        # 分页处理
        try:    # 获取页码
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Paginator(总数据，每页显示数据)
        paginator = Paginator(nurse_goods, 8, request=request)
        nurse_part = paginator.page(page)

        arg_dir = {
            'nav_at': 'nurse',  # 标签页的使能
            'brands':brands,    # 商品品牌
            'brand_num': brand_num, # 商品品牌使能
            'hot_sells':hot_sells,  # 热销排行榜
            'nurse_goods':nurse_part,    # 主体商品，此时就不是全部数据
            'sort':sort,  # 排序
            'user_favorites':user_favorites,    # 用户收藏数据
        }

        return render(request, 'nurse-goods.html', arg_dir)


class FavoriteView(View):   # 收藏
    def post(self, request):    # 此处是Ajax操作
        # 获取数据
        goods_id = int(request.POST.get('goods_id', 0))

        # 用户是否登录
        # is_authenticated是属性，不是方法，不能添加括号
        if not request.user.is_authenticated: # 未登录
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        # 获取收藏信息
        user_favorite = UserFavorite.objects.filter(user=request.user,goods_id=goods_id)
        if user_favorite:   # 已收藏，取消收藏(删除)
            user_favorite.delete()
            return HttpResponse('{"status":"succeed", "msg":"取消收藏成功", "is_fav":"0"}', content_type='application/json')
        else:   # 未收藏，收藏(添加新数据)
            user_favorite = UserFavorite()
            user_favorite.user = request.user
            user_favorite.goods_id = goods_id
            user_favorite.save()
            return HttpResponse('{"status":"succeed", "msg":"收藏成功", "is_fav":"1"}', content_type='application/json')


class GoodsDetailView(View):    # 商品详情页
    def get(self, request, sku_id):
        # 获取到具体商品的SKU  【具体的商品】
        sku = Stock.objects.get(s_id=sku_id)

        # 根据SKU获取到SPU 【产品】
        spu = sku.s_product

        # 获取对应SPU 下的所有 SKU 【该产品下订单所有商品，要获取其属性】
        skus = spu.stock_set.all()
        attrs = {}
        for sku_item in skus:
            # 根据SKU获取到对应的属性
            stock_attr_ops = sku_item.stockattrop_set.all()
            for stock_attr_op in stock_attr_ops:    # 遍历获取属性和属性选项
                attr_name = stock_attr_op.s_attr.a_name
                attr_val = stock_attr_op.s_attr_op.o_name
                print(stock_attr_op.s_sku)
                if attr_name in attrs:  # 是否存在这个key
                    temp_arr = attrs[attr_name]     # 取出key对应的值，后续追加新的属性值
                    if not attr_val in temp_arr:    # 判断value是否已存在数组中
                        temp_arr.append(attr_val)
                        attrs[attr_name] = temp_arr
                else:
                    attrs[attr_name] = [attr_val]


        # 获取当前商品的属性选项
        current_attrs = []
        current_stock_attr_ops = sku.stockattrop_set.all()
        for stock_attr_op in current_stock_attr_ops:
            # attr_name = stock_attr_op.s_attr.a_name
            attr_val = stock_attr_op.s_attr_op.o_name
            current_attrs.append(attr_val)

        # 轮播图
        banners = spu.goodsdetailbanner_set.all()

        # 当前商品轮播图
        sku_banner = sku.skubanner_set.first().s_goods_detail

        # 获取产品详情图片
        goods_details = spu.goodsdetail_set.all()

        # 促销信息
        discount = spu.p_discount.d_content

        arg_dir = {
            'sku':sku,
            'attrs':attrs,  # 产品所有属性
            'current_attrs':current_attrs, # 当前商品属性
            'banners':banners,  # 轮播图
            'sku_banner':sku_banner,    # 当前商品轮播图
            'goods_details':goods_details,   # 产品详情
            'discount':discount,    # 促销信息
        }

        return render(request, 'goods-detail.html', arg_dir)
