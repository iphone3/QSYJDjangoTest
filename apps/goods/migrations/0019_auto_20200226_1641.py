# Generated by Django 2.2.7 on 2020-02-26 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0018_auto_20200226_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nursegoods',
            name='goods_brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.Brand'),
        ),
    ]