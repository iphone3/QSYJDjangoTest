import xadmin
from goods.models import HotSell, NurseGoods


# class KeyWordsAdmin(object): # 护理用品 - 关键字
#     # 后台显示字段
#     list_display = ['key_name', 'key_type']
#     # 字段过滤
#     list_filter = ['key_type']
#     # 搜索字段
#     search_fields = ['key_name']
# xadmin.site.register(KeyWords, KeyWordsAdmin)


class HotSellAdmin(object): # 护理用户 - 热销排行榜
    list_display = ['goods_name', 'goods_nun','goods_price']
    search_fields = ['goods_name', 'goods_id']
xadmin.site.register(HotSell, HotSellAdmin)


class NurseGoodsAdmin(object):  # 护理用户 - 商品
    list_display = ['goods_name', 'goods_price', 'goods_tip', 'goods_sales']
    list_filter = ['goods_name', 'goods_brand', 'goods_spec', 'goods_func', 'goods_texture', 'goods_sales', 'goods_tip']
xadmin.site.register(NurseGoods, NurseGoodsAdmin)