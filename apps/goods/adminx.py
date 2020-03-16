import xadmin
from goods.models import HotSell, Brand, NurseGoods, ContactLensBanner, ContactLensGoods, Assort,  \
    Standard, AttributeValue, SKUAttrVal, GoodsDetailBanner, SkuBanner, GoodsDetail, Discount, SPU, SKU


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


class DiscountAdmin(object):    # 促销
    list_display = ['d_content']
    list_filter = ['d_content']
    search_fields = ['d_content']
xadmin.site.register(Discount, DiscountAdmin)


class SPUAdmin(object): # SPU 标准产品单位
    list_display = ['p_name', 'p_assort', 'p_brand']
    list_filter = ['p_name', 'p_assort', 'p_brand']
    search_fields = ['p_name', 'p_assort']
xadmin.site.register(SPU, SPUAdmin)


class SKUAdmin(object):   # SKU 库存量单位
    list_display = ['s_name', 's_spu', 's_price','s_id', 's_stock']
    list_filter = ['s_name', 's_spu', 's_stock', 's_price']
    search_fields = ['s_name', 's_spu']
xadmin.site.register(SKU, SKUAdmin)


class StandardAdmin(object):   # 规格 【颜色】
    list_display = ['a_name', 'a_assort']
    list_filter = ['a_name', 'a_assort']
    search_fields = ['a_name', 'a_assort']
xadmin.site.register(Standard, StandardAdmin)


class AttributeValueAdmin(object):   # 规格属性值 【红色】
    list_display = ['o_val', 'o_standard']
    list_filter = ['o_val', 'o_standard']
    search_fields = ['o_val', 'o_standard']
xadmin.site.register(AttributeValue, AttributeValueAdmin)


class SKUAttrValAdmin(object):   # SKU规格属性值
    list_display = ['s_sku', 's_attr_val', 's_standard']
    list_filter = ['s_sku', 's_attr_val', 's_standard']
    search_fields = ['s_sku', 's_attr_val', 's_standard']
xadmin.site.register(SKUAttrVal, SKUAttrValAdmin)


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

