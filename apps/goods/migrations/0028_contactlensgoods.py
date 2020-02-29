# Generated by Django 2.2.7 on 2020-02-28 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0027_auto_20200228_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactLensGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(unique=True, verbose_name='商品详情ID')),
                ('goods_name', models.CharField(default='', max_length=255, verbose_name='商品名称')),
                ('goods_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='商品价格')),
                ('goods_img', models.ImageField(blank=True, default='image/atom.png', null=True, upload_to='image/%Y/%m', verbose_name='商品图片')),
                ('goods_discount', models.CharField(default='', max_length=255, verbose_name='商品优惠')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '彩瞳-商品',
                'verbose_name': '彩瞳-商品',
            },
        ),
    ]