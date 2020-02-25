from django.shortcuts import render
from django.views import View
from goods.models import HotSell, NurseGoods


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
        # 热销排行榜
        hot_sells = HotSell.objects.all().order_by('goods_nun')

        # 主体商品
        nurse_goods = NurseGoods.objects.all()

        arg_dir = {
            'nav_at': 'nurse',  # 标签页的使能
            'hot_sells':hot_sells,
            'nurse_goods':nurse_goods
        }

        return render(request, 'nurse-goods.html', arg_dir)


