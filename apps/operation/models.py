from datetime import datetime

from django.db import models
from users.models import UserProfile


# 用户评论
# GoodsComments

# 用户收藏
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    # 这里没有级联，是因为有多种商品表，所以只保存商品ID即可
    goods_id = models.IntegerField(default=0, verbose_name='商品ID')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = '用户收藏'

# 用户购物车


# 用户订单
