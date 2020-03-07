# Generated by Django 2.2.7 on 2020-03-02 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0031_auto_20200301_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='s_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='商品价格'),
        ),
    ]