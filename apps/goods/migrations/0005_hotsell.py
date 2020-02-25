# Generated by Django 2.2.7 on 2020-02-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20200225_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotSell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(max_length=12, verbose_name='商品详情ID')),
                ('goods_name', models.CharField(default='', max_length=200, verbose_name='商品名称')),
                ('goods_price', models.CharField(max_length=12, verbose_name='商品价格')),
            ],
            options={
                'verbose_name': '热销排行榜',
                'verbose_name_plural': '热销排行榜',
            },
        ),
    ]
