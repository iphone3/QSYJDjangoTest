# Generated by Django 2.2.7 on 2020-02-25 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_auto_20200225_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotsell',
            old_name='goods_file',
            new_name='goods_img',
        ),
    ]
