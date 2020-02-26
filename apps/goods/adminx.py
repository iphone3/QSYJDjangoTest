import xadmin
from goods.models import HotSell, Brand, NurseGoods

class BrandAdmin(object):   # 护理用品 - 品牌
    list_display = ['key_name','key_num']
    search_fields = ['key_name']
xadmin.site.register(Brand, BrandAdmin)


class HotSellAdmin(object): # 护理用户 - 热销排行榜
    list_display = ['goods_name', 'goods_nun','goods_price']
    search_fields = ['goods_name', 'goods_id']
xadmin.site.register(HotSell, HotSellAdmin)


class NurseGoodsAdmin(object):  # 护理用户 - 商品
    list_display = ['goods_name', 'goods_price', 'goods_tip', 'goods_sales']
    list_filter = ['goods_name', 'goods_brand', 'goods_sales', 'goods_tip']
xadmin.site.register(NurseGoods, NurseGoodsAdmin)