# Generated by Django 2.2.7 on 2020-02-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_hotsell'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotsell',
            name='goods_file',
            field=models.ImageField(default='image/atom.png', upload_to='image/%Y/%m', verbose_name='商品图片'),
        ),
    ]