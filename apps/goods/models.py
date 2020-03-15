from datetime import datetime

from django.db import models

# 品牌
class Brand(models.Model):
    key_name = models.CharField(max_length=32, verbose_name='品牌名称', default='')
    key_num = models.IntegerField(verbose_name='显示序号', default=1)

    class Meta:
        verbose_name = '品牌管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.key_name


# 护理用户 - 热销排行榜
class HotSell(models.Model):
    goods_nun = models.IntegerField(verbose_name='排行榜', default=1)
    goods_id = models.IntegerField(verbose_name='商品ID')
    goods_name = models.CharField(max_length=200, verbose_name='商品名称', default='')
    goods_price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='商品价格', default=0)
    goods_img = models.ImageField(max_length=100, verbose_name='商品图片', upload_to='image/%Y/%m', default='image/atom.png', null=True, blank=True)

    class Meta:
        verbose_name = '护理用品-热销榜'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name


# 护理用户 - 商品
class NurseGoods(models.Model):
    goods_id = models.IntegerField(verbose_name='商品详情ID', unique=True)
    goods_name = models.CharField(max_length=255, verbose_name='商品名称', default='')
    goods_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='商品价格', default=0)
    goods_img = models.ImageField(max_length=100, verbose_name='商品图片', upload_to='image/%Y/%m',default='image/atom.png', null=True, blank=True)
    goods_tip = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='商品评分', default=0)
    goods_sales = models.IntegerField(verbose_name='商品销量', default=0)
    goods_brand = models.ForeignKey(Brand, default=1, on_delete=models.SET_DEFAULT, verbose_name='商品品牌')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '护理用品-商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name


# 彩瞳 - 轮播图
class ContactLensBanner(models.Model):
    goods_id = models.IntegerField(verbose_name='商品详情ID', unique=True)
    goods_name = models.CharField(max_length=255, verbose_name='商品名称', default='')
    goods_img = models.ImageField(max_length=100, verbose_name='商品图片', upload_to='image/%Y/%m',default='', null=True, blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '彩瞳 - 轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name

# 彩瞳 - 商品
class ContactLensGoods(models.Model):
    """
    后续此处需要关联到商品详情表
    此处商品是用于界面显示，而跳转后的是详情页
    数据添加时，先详情后商品展示

    【只需要goods_id，goods_name和goods_price不需要】
    """
    goods_id = models.IntegerField(verbose_name='商品详情ID', unique=True)
    goods_name = models.CharField(max_length=255, verbose_name='商品名称', default='')
    goods_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='商品价格', default=0)
    goods_img = models.ImageField(max_length=100, verbose_name='商品图片', upload_to='image/%Y/%m',default='image/atom.png', null=True, blank=True)
    goods_discount = models.CharField(max_length=255, verbose_name='商品优惠', default='')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '彩瞳-商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name




#####################
# 商品分类
class Assort(models.Model):
    a_name = models.CharField(max_length=100, default='', verbose_name='商品分类')

    class Meta:
        verbose_name = '分类管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.a_name


# 促销
class Discount(models.Model):
    d_content = models.CharField(max_length=255, default='', verbose_name='促销内容')


    class Meta:
        verbose_name = '促销管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.d_content

# SPU 标准产品单位
class Product(models.Model):
    p_name = models.CharField(max_length=255, default='', verbose_name='产品名称')
    p_brand = models.ForeignKey(Brand, on_delete=models.SET_DEFAULT,default='', null=True, blank=True, verbose_name='品牌')
    p_assort = models.ForeignKey(Assort, on_delete=models.SET_DEFAULT, default=1, verbose_name='所属分类')
    p_discount = models.ForeignKey(Discount, on_delete=models.SET_DEFAULT, default='', null=True, blank=True, verbose_name='促销信息')

    class Meta:
        verbose_name = 'SPU管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.p_name

# SKU 库存量单位
class Stock(models.Model):
    # 需要手动创建一个对象，1000001开始
    s_id = models.BigAutoField(primary_key=True,verbose_name='商品详情ID')
    s_name = models.CharField(max_length=255, default='', verbose_name='商品名')
    s_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='所属产品')   # 产品删除，即对应的商品一并删除
    s_price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='商品价格', default=0)

    # 库存  用库存在处理产品属性选择，如果没有库存即不显示假如购物车

    #

    class Meta:
        verbose_name = 'SKU管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.s_name


# 商品属性
class Attribute(models.Model):
    a_name = models.CharField(max_length=100, default='', verbose_name='商品属性名')
    a_assort = models.ForeignKey(Assort, on_delete=models.SET_DEFAULT, default=1, verbose_name='所属分类')
    a_index = models.IntegerField(default=1, verbose_name='规格下标')

    class Meta:
        verbose_name = '属性管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.a_name


# 商品属性选项
class AttributeOption(models.Model):
    o_name = models.CharField(max_length=100, default='', verbose_name='商品属性选项名')
    o_attr = models.ForeignKey(Attribute, on_delete=models.CASCADE, verbose_name='所属商品属性')

    class Meta:
        verbose_name = '属性选项管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.o_name

# SKU属性选项
class StockAttrOp(models.Model):
    s_sku = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name='SKU ID')
    s_attr_op = models.ForeignKey(AttributeOption, on_delete=models.CASCADE, verbose_name='AttributeOption ID')
    s_attr = models.ForeignKey(Attribute, on_delete=models.CASCADE, verbose_name='Attribute ID')

    class Meta:
        verbose_name = 'SKU属性选项'
        verbose_name_plural = verbose_name

# 商品详情轮播图
class GoodsDetailBanner(models.Model):
    g_big_img = models.ImageField(max_length=100, verbose_name='大图片', upload_to='image/%Y/%m',default='', null=True, blank=True)
    g_small_img = models.ImageField(max_length=100, verbose_name='小图片', upload_to='image/%Y/%m',default='', null=True, blank=True)
    s_spu = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='SPU ID')

    class Meta:
        verbose_name = '商品详情-轮播图'
        verbose_name_plural = verbose_name


# SKU轮播图
class SkuBanner(models.Model):
    s_sku = models.ForeignKey(Stock, on_delete=models.CASCADE, verbose_name='SKU ID')
    s_goods_detail = models.ForeignKey(GoodsDetailBanner, on_delete=models.CASCADE, verbose_name='商品详情轮播图ID', default=1, null=True, blank=True)

    class Meta:
        verbose_name = 'SKU轮播图'
        verbose_name_plural = verbose_name

# 商品详情图片
class GoodsDetail(models.Model):
    g_img = models.ImageField(max_length=100, verbose_name='大图片', upload_to='image/%Y/%m',default='', null=True, blank=True)
    g_spu = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='SPU ID')

    class Meta:
        verbose_name = '商品详情图片'
        verbose_name_plural = verbose_name
