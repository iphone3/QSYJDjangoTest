# Generated by Django 2.2.7 on 2020-02-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='image/atom.png', null=True, upload_to='image/%Y/%m', verbose_name='头像'),
        ),
    ]