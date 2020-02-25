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
BRAND_CHOICES = (
    ('AEK','爱尔康'),
    ('KB','库博'),
    ('HC','海昌'),
    ('SK','视康'),
    ('CS','蔡司'),
    ('MNK','美尼康'),
    ('QT','其他'),
)
SPEC_CHOICES =(
    ('CX','促销装'),
    ('DP','大瓶装'),
    ('ZP','中瓶装'),
    ('XP','小瓶装'),
)
FUNC_CHOICES =(
    ('HLY','护理液'),
    ('BLH','伴侣盒'),
    ('RYY','润眼液'),
    ('QXQ','清洗器'),
    ('QDQ','取戴器'),
    ('SLH','双联盒'),
)
TEXTURE_CHOICES =(
    ('GJ','硅胶'),
    ('NL','尼龙'),
    ('QT','其他'),
)
class NurseGoods(models.Model):
    goods_id = models.IntegerField(verbose_name='商品详情ID')
    goods_name = models.CharField(max_length=200, verbose_name='商品名称', default='')
    goods_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='商品价格', default=0)
    goods_img = models.ImageField(max_length=100, verbose_name='商品图片', upload_to='image/%Y/%m',default='image/atom.png', null=True, blank=True)
    goods_tip = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='商品评分', default=0)
    goods_sales = models.IntegerField(verbose_name='商品销量', default=0)
    goods_brand = models.CharField(verbose_name='商品品牌', max_length=32, choices=BRAND_CHOICES, default='QT')
    goods_spec = models.CharField(verbose_name='商品规格', max_length=32, choices=SPEC_CHOICES, default='CX')
    goods_func = models.CharField(verbose_name='商品功能', max_length=32, choices=FUNC_CHOICES, default='HLY')
    goods_texture = models.CharField(verbose_name='商品材质', max_length=32, choices=TEXTURE_CHOICES, default='QT')

    class Meta:
        verbose_name = '护理用品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name

