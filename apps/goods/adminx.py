import xadmin
from goods.models import HotSell, Brand, NurseGoods, ContactLensBanner, ContactLensGoods, Assort, Product, Stock, \
    Attribute, AttributeOption, StockAttrOp, GoodsDetailBanner, SkuBanner, GoodsDetail


class BrandAdmin(object):   # 护理用品 - 品牌
    list_display = ['key_name','key_num']
    search_fields = ['key_name']
xadmin.site.register(Brand, BrandAdmin)


class HotSellAdmin(object): # 护理用户 - 热销排行榜
    list_display = ['goods_name', 'goods_nun','goods_price']
    search_fields = ['goods_name', 'goods_id']
xadmin.site.register(HotSell, HotSellAdmin)


class NurseGoodsAdmin(object):  # 护理用户 - 商品
    list_display = ['goods_name', 'goods_price', 'goods_tip', 'goods_sales', 'goods_id']
    list_filter = ['goods_name', 'goods_brand', 'goods_sales', 'goods_tip']
xadmin.site.register(NurseGoods, NurseGoodsAdmin)



class ContactLensBannerAdmin(object):   # 彩瞳 - 轮播图
    list_display = ['goods_name', 'add_time', 'goods_id']
    list_filter = ['goods_name']
xadmin.site.register(ContactLensBanner, ContactLensBannerAdmin)


class ContactLensGoodsAdmin(object):    # 彩瞳 - 商品
    list_display = ['goods_name', 'goods_price', 'goods_discount', 'goods_id']
    list_filter = ['goods_name', 'goods_discount']
xadmin.site.register(ContactLensGoods, ContactLensGoodsAdmin)


class AssortAdmin(object): # 商品分类
    list_display = ['a_name']
    list_filter = ['a_name']
    search_fields = ['a_name']
xadmin.site.register(Assort, AssortAdmin)


class ProductAdmin(object): # SPU 标准产品单位
    list_display = ['p_name', 'p_assort']
    list_filter = ['p_name', 'p_assort']
    search_fields = ['p_name', 'p_assort']
xadmin.site.register(Product, ProductAdmin)


class StockAdmin(object):   # SKU 库存量单位
    list_display = ['s_name', 's_product', 's_id']
    list_filter = ['s_name', 's_product']
    search_fields = ['s_name', 's_product']
xadmin.site.register(Stock, StockAdmin)


class AttributeAdmin(object):   # 商品属性
    list_display = ['a_name', 'a_assort']
    list_filter = ['a_name', 'a_assort']
    search_fields = ['a_name', 'a_assort']
xadmin.site.register(Attribute, AttributeAdmin)


class AttributeOptionAdmin(object):   # 商品属性选项
    list_display = ['o_name', 'o_attr']
    list_filter = ['o_name', 'o_attr']
    search_fields = ['o_name', 'o_attr']
xadmin.site.register(AttributeOption, AttributeOptionAdmin)


class StockAttrOpAdmin(object):   # SKU属性选项
    list_display = ['s_sku', 's_attr_op', 's_attr']
    list_filter = ['s_sku', 's_attr_op', 's_attr']
    search_fields = ['s_sku', 's_attr_op', 's_attr']
xadmin.site.register(StockAttrOp, StockAttrOpAdmin)


class GoodsDetailBannerAdmin(object):   # 商品详情轮播图
    list_display = ['g_small_img', 's_spu']
    list_filter = ['g_small_img', 's_spu']
    search_fields = ['g_small_img', 's_spu']
xadmin.site.register(GoodsDetailBanner, GoodsDetailBannerAdmin)


class SkuBannerAdmin(object):   # SKU轮播图
    list_display = ['s_sku', 's_goods_detail']
    list_filter = ['s_sku', 's_goods_detail']
    search_fields = ['s_sku', 's_goods_detail']
xadmin.site.register(SkuBanner, SkuBannerAdmin)


class GoodsDetailAdmin(object):   # 商品详情图片
    list_display = ['g_img', 'g_spu']
    list_filter = ['g_img', 'g_spu']
    search_fields = ['g_img', 'g_spu']
xadmin.site.register(GoodsDetail, GoodsDetailAdmin)

