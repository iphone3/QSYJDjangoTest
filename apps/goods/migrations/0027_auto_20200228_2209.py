# Generated by Django 2.2.7 on 2020-02-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0026_auto_20200228_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactlensbanner',
            name='goods_id',
            field=models.IntegerField(unique=True, verbose_name='商品详情ID'),
        ),
        migrations.AlterField(
            model_name='nursegoods',
            name='goods_id',
            field=models.IntegerField(unique=True, verbose_name='商品详情ID'),
        ),
    ]
