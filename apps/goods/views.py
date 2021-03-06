from collections import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from goods.models import HotSell, NurseGoods, Brand, ContactLensBanner, ContactLensGoods, SKUAttrVal, SKU
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import UserFavorite


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
        sku = SKU.objects.get(s_id=sku_id)

        # 根据SKU获取到SPU 【产品】
        spu = sku.s_spu

        """ 该产品SPU 规格和属性值
        [
            {
                'standard_name': '颜色',
                'standard_id': 1,
                'standard_value': [
                    {'id': 2, 'name': '黑色'}, 
                    {'id': 1, 'name': '棕色'}, 
                    {'id': 4, 'name': '梦境紫'}
                ]
            },
            {
                'standard_name': '度数',
                'standard_id': 2,
                'standard_value': [
                    {'id': 12, 'name': '0度'}, 
                    {'id': 13, 'name': '100'}, 
                    {'id': 17, 'name': '200'}
                ]
            }
        ]
        """
        """
        [
            {'standard_id': 1, 'standard_name': '颜色', 'attr_id': 2, 'attr_val': '黑色'}, 
            {'standard_id': 2, 'standard_name': '度数', 'attr_id': 12, 'attr_val': '0度'}, 
            {'standard_id': 1, 'standard_name': '颜色', 'attr_id': 1, 'attr_val': '棕色'}, 
            {'standard_id': 2, 'standard_name': '度数', 'attr_id': 13, 'attr_val': '100'}, 
            {'standard_id': 1, 'standard_name': '颜色', 'attr_id': 4, 'attr_val': '梦境紫'},
            {'standard_id': 2, 'standard_name': '度数', 'attr_id': 12, 'attr_val': '0度'}, 
            {'standard_id': 1, 'standard_name': '颜色', 'attr_id': 4, 'attr_val': '梦境紫'}, 
            {'standard_id': 2, 'standard_name': '度数', 'attr_id': 13, 'attr_val': '100'}, 
            {'standard_id': 1, 'standard_name': '颜色', 'attr_id': 4, 'attr_val': '梦境紫'}, 
            {'standard_id': 2, 'standard_name': '度数', 'attr_id': 17, 'attr_val': '200'}
        ]
        
        [
            {'standard_id': 1, 'sku_id': 1000001, 'attr_id': 2}, 
            {'standard_id': 2, 'sku_id': 1000001, 'attr_id': 12}, 
            {'standard_id': 1, 'sku_id': 1000002, 'attr_id': 1}, 
            {'standard_id': 2, 'sku_id': 1000002, 'attr_id': 13}, 
            {'standard_id': 1, 'sku_id': 1000003, 'attr_id': 4}, 
            {'standard_id': 2, 'sku_id': 1000003, 'attr_id': 12}, 
            {'standard_id': 1, 'sku_id': 1000004, 'attr_id': 4}, 
            {'standard_id': 2, 'sku_id': 1000004, 'attr_id': 13}, 
            {'standard_id': 1, 'sku_id': 1000005, 'attr_id': 4},    
            {'standard_id': 2, 'sku_id': 1000005, 'attr_id': 17}
        ]
        """
        skus = spu.sku_set.all()
        spu_attrs = []  # 所有规格和属性值
        skuids =[]  # 所有规格、属性值对应的sku_id
        for sku_item in skus:
            # 根据SKU获取到对应的属性
            sku_attr_vals = sku_item.skuattrval_set.all()
            for sku_attr_val in sku_attr_vals:  # 遍历获取 属性和属性选项
                # standard_id 规格ID  3
                standard_id = sku_attr_val.s_standard.id
                # standard_name 颜色
                standard_name = sku_attr_val.s_standard.a_name
                # attr_val 黑色
                attr_val = sku_attr_val.s_attr_val.o_val
                # attr_id  3
                attr_id = sku_attr_val.s_attr_val.id
                # sku_id
                sku_id = sku_attr_val.s_sku.s_id

                spu_attrs.append({
                    'standard_id':standard_id,
                    'standard_name': standard_name,
                    'attr_val':attr_val,
                    'attr_id':attr_id,
                    'sku_id':sku_id
                })

                skuids.append({
                    'sku_id': sku_id,
                    'standard_id': standard_id,
                    'attr_id':attr_id,
                })

        # 数据处理 -- 去重
        b = OrderedDict()
        for item in spu_attrs:
            b.setdefault(item['attr_id'], {**item, })
        spu_attrs = list(b.values())

        # 数据处理 -- 序列化
        wrapper_dir = []
        for item in spu_attrs:  # 遍历初始化好基本结构
            dir = {
                'standard_name': item['standard_name'],
                'standard_id': item['standard_id'],
                'standard_value': []
            }
            if dir not in wrapper_dir:
                wrapper_dir.append(dir)

        for item in wrapper_dir:    # 填充standard_value数值
            for spu_attr in spu_attrs:
                if spu_attr['standard_name'] == item['standard_name']:
                    dir = {'id': spu_attr['attr_id'], 'name': spu_attr['attr_val']}
                    item['standard_value'].append(dir)

        # 数据处理完成，重新赋值
        spu_attrs = wrapper_dir


        """ 
        当前选中属性
        [
            {
                'standard_name': '颜色', 
                'attr_id': 4, 
                'attr_val': '梦境紫'
            }, 
            {
                'standard_name': '度数', 
                'attr_id': 12, 
                'attr_val': '0度'
            }
        ]
        """
        current_attrs = []
        current_sku_attr_ops = sku.skuattrval_set.all()

        for current_sku_attr_op in current_sku_attr_ops:
            # standard_id 规格ID  3
            standard_id = current_sku_attr_op.s_standard.id
            # standard_id 规格名  颜色
            standard_name = current_sku_attr_op.s_standard.a_name
            # attr_val 黑色
            attr_val = current_sku_attr_op.s_attr_val.o_val
            # attr_id  3
            attr_id = current_sku_attr_op.s_attr_val.id
            dir = {
                'standard_name': standard_name,
                'attr_id':attr_id,
                'attr_val':attr_val
            }
            current_attrs.append(dir)

        # 轮播图
        banners = spu.goodsdetailbanner_set.all()

        # 当前商品轮播图
        sku_banners = sku.skubanner_set.all()
        if sku_banners.count(): # 存在
            sku_banner = sku_banners.first().s_goods_detail
        else:   # 不存在
            sku_banner = spu.goodsdetailbanner_set.first()

        # 获取产品详情图片
        goods_details = spu.goodsdetail_set.all()

        # 促销信息
        discount = spu.p_discount.d_content

        # 请求地址    先拆分，后取值，最后拼装  /goods/detail/
        path = '/' + '/'.join(request.path.split('/')[1:3]) + '/'

        arg_dir = {
            'sku':sku,  # 产品
            'spu_attrs':spu_attrs,  # 产品所有属性
            'spu_name': spu.p_name, # 产品名称
            'current_attrs':current_attrs, # 当前商品属性
            'skuids':skuids,    # 所有规格、属性值对应的sku_id
            'banners':banners,  # 轮播图
            'sku_banner':sku_banner,    # 当前商品轮播图
            'goods_details':goods_details,   # 产品详情
            'discount':discount,    # 促销信息
            'path': path,   # 请求的完整路径
        }

        return render(request, 'goods-detail.html', arg_dir)
