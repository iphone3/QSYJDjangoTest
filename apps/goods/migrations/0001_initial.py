# Generated by Django 2.2.7 on 2020-03-16 22:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(default='', max_length=100, verbose_name='商品分类')),
            ],
            options={
                'verbose_name': '分类管理',
                'verbose_name_plural': '分类管理',
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_val', models.CharField(default='', max_length=100, verbose_name='规格属性值')),
            ],
            options={
                'verbose_name': '属性值管理',
                'verbose_name_plural': '属性值管理',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_name', models.CharField(default='', max_length=32, verbose_name='品牌名称')),
                ('key_num', models.IntegerField(default=1, verbose_name='显示序号')),
            ],
            options={
                'verbose_name': '品牌管理',
                'verbose_name_plural': '品牌管理',
            },
        ),
        migrations.CreateModel(
            name='ContactLensBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(unique=True, verbose_name='商品详情ID')),
                ('goods_name', models.CharField(default='', max_length=255, verbose_name='商品名称')),
                ('goods_img', models.ImageField(blank=True, default='', null=True, upload_to='image/%Y/%m', verbose_name='商品图片')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '彩瞳 - 轮播图',
                'verbose_name_plural': '彩瞳 - 轮播图',
            },
        ),
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
                'verbose_name': '彩瞳-商品',
                'verbose_name_plural': '彩瞳-商品',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_content', models.CharField(default='', max_length=255, verbose_name='促销内容')),
            ],
            options={
                'verbose_name': '促销管理',
                'verbose_name_plural': '促销管理',
            },
        ),
        migrations.CreateModel(
            name='GoodsDetailBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_big_img', models.ImageField(blank=True, default='', null=True, upload_to='image/%Y/%m', verbose_name='大图片')),
                ('g_small_img', models.ImageField(blank=True, default='', null=True, upload_to='image/%Y/%m', verbose_name='小图片')),
            ],
            options={
                'verbose_name': '商品详情-轮播图',
                'verbose_name_plural': '商品详情-轮播图',
            },
        ),
        migrations.CreateModel(
            name='HotSell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_nun', models.IntegerField(default=1, verbose_name='排行榜')),
                ('goods_id', models.IntegerField(verbose_name='商品ID')),
                ('goods_name', models.CharField(default='', max_length=200, verbose_name='商品名称')),
                ('goods_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='商品价格')),
                ('goods_img', models.ImageField(blank=True, default='image/atom.png', null=True, upload_to='image/%Y/%m', verbose_name='商品图片')),
            ],
            options={
                'verbose_name': '护理用品-热销榜',
                'verbose_name_plural': '护理用品-热销榜',
            },
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('s_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='商品详情ID')),
                ('s_name', models.CharField(default='', max_length=255, verbose_name='商品名')),
                ('s_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='商品价格')),
                ('s_stock', models.IntegerField(default=0, verbose_name='库存')),
            ],
            options={
                'verbose_name': 'SKU管理',
                'verbose_name_plural': 'SKU管理',
            },
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(default='', max_length=100, verbose_name='商品规格')),
                ('a_assort', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.Assort', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '规格管理',
                'verbose_name_plural': '规格管理',
            },
        ),
        migrations.CreateModel(
            name='SPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(default='', max_length=255, verbose_name='产品名称')),
                ('p_assort', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.Assort', verbose_name='所属分类')),
                ('p_brand', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.Brand', verbose_name='品牌')),
                ('p_discount', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.Discount', verbose_name='促销信息')),
            ],
            options={
                'verbose_name': 'SPU管理',
                'verbose_name_plural': 'SPU管理',
            },
        ),
        migrations.CreateModel(
            name='SkuBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_goods_detail', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsDetailBanner', verbose_name='商品详情轮播图ID')),
                ('s_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.SKU', verbose_name='SKU ID')),
            ],
            options={
                'verbose_name': 'SKU轮播图',
                'verbose_name_plural': 'SKU轮播图',
            },
        ),
        migrations.CreateModel(
            name='SKUAttrVal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_attr_val', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.AttributeValue', verbose_name='规格属性值ID')),
                ('s_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.SKU', verbose_name='SKU ID')),
                ('s_standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Standard', verbose_name='规格ID')),
            ],
            options={
                'verbose_name': 'SKU规格属性值',
                'verbose_name_plural': 'SKU规格属性值',
            },
        ),
        migrations.AddField(
            model_name='sku',
            name='s_spu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.SPU', verbose_name='所属产品'),
        ),
        migrations.CreateModel(
            name='NurseGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(unique=True, verbose_name='商品详情ID')),
                ('goods_name', models.CharField(default='', max_length=255, verbose_name='商品名称')),
                ('goods_price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='商品价格')),
                ('goods_img', models.ImageField(blank=True, default='image/atom.png', null=True, upload_to='image/%Y/%m', verbose_name='商品图片')),
                ('goods_tip', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='商品评分')),
                ('goods_sales', models.IntegerField(default=0, verbose_name='商品销量')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods_brand', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.Brand', verbose_name='商品品牌')),
            ],
            options={
                'verbose_name': '护理用品-商品',
                'verbose_name_plural': '护理用品-商品',
            },
        ),
        migrations.AddField(
            model_name='goodsdetailbanner',
            name='s_spu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.SPU', verbose_name='SPU ID'),
        ),
        migrations.CreateModel(
            name='GoodsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_img', models.ImageField(blank=True, default='', null=True, upload_to='image/%Y/%m', verbose_name='大图片')),
                ('g_spu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.SPU', verbose_name='SPU ID')),
            ],
            options={
                'verbose_name': '商品详情图片',
                'verbose_name_plural': '商品详情图片',
            },
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='o_standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Standard', verbose_name='所属规格'),
        ),
    ]
