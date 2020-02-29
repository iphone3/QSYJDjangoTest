from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# auth_user使用系统提供的用户类 【有验证、权限等功能】
# 扩展Django默认的user表，添加额外属性
# 通过UserProfile覆盖默认user表
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='');
    birthday = models.DateField(max_length=8, verbose_name='生日', null=True, blank=True);
    gender = models.CharField(max_length=10,verbose_name='性别', choices=(('man', '男'),('women', '女')), default='man');
    address = models.CharField(max_length=100, verbose_name='地址', default='');
    image = models.ImageField(max_length=100, verbose_name='头像', default='image/atom.png', upload_to='image/%Y/%m', null=True, blank=True);

    class Meta:
        verbose_name = '用户信息';
        verbose_name_plural = verbose_name;

    def __str__(self):
        return self.username;
