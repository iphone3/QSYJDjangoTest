from django.shortcuts import render
from django.views import View
from goods.models import HotSell, NurseGoods, Brand
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# 首页
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {'nav_at':'index'})

# 彩瞳
class ContactView(View):
    def get(self, request):
        return render(request, 'contact-lens.html', {'nav_at':'contact'})

# 护理用品
class NurseView(View):
    def get(self, request):
        # 商品品牌
        brands = Brand.objects.all().order_by('key_num')

        # 热销排行榜
        hot_sells = HotSell.objects.all().order_by('goods_nun')

        # 取出筛选品牌
        brand_num = int(request.GET.get('brand_num', '0'))
        if brand_num == 0:  # 全部主体商品
            print(brand_num)
            nurse_goods = NurseGoods.objects.all()
        else:   # 根据品牌获取级联数据
            brand = Brand.objects.get(key_num=brand_num)
            nurse_goods = brand.nursegoods_set.all()


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
        }

        return render(request, 'nurse-goods.html', arg_dir)


