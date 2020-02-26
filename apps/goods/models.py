from django.db import models


# 护理用品 - 关键字
# class KeyWords(models.Model):
#     key_name = models.CharField(max_length=32, verbose_name='关键字', default='')
#     key_type = models.CharField(max_length=32, verbose_name='类型', choices=(('brand', '品牌'), ('specifications', '规格'), ('function', '功能'), ('texture', '材质'), ('price', '价格')), default='brand')
#
#     class Meta:
#         verbose_name = '商品关键字'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.key_name

# 护理用品 - 品牌
class Brand(models.Model):
    key_name = models.CharField(max_length=32, verbose_name='品牌名称', default='')
    key_num = models.IntegerField(verbose_name='显示序号', default=1)

    class Meta:
        verbose_name = '商品品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.key_name

# 护理用户 - 热销排行榜
class HotSell(models.Model):
    goods_nun = models.IntegerField(verbose_name='排行榜', default=1)
    goods_id = models.IntegerField(verbose_name='商品详情ID')
    goods_name = models.CharField(max_length=200, verbose_name='商品名称', default='')
    goods_price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='商品价格', default=0)
    goods_img = models.ImageField(max_length=100, verbose_name='商品图片', upload_to='image/%Y/%m', default='image/atom.png', null=True, blank=True)

    class Meta:
        verbose_name = '热销排行榜'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name

# 护理用户 - 商品
class NurseGoods(models.Model):
    goods_id = models.IntegerField(verbose_name='商品详情ID')
    goods_name = models.CharField(max_length=200, verbose_name='商品名称', default='')
    goods_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='商品价格', default=0)
    goods_img = models.ImageField(max_length=100, verbose_name='商品图片', upload_to='image/%Y/%m',default='image/atom.png', null=True, blank=True)
    goods_tip = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='商品评分', default=0)
    goods_sales = models.IntegerField(verbose_name='商品销量', default=0)
    goods_brand = models.ForeignKey(Brand, default=1, on_delete=models.SET_DEFAULT, verbose_name='商品品牌')

    class Meta:
        verbose_name = '护理用品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name

