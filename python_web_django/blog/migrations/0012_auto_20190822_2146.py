# Generated by Django 2.2.3 on 2019-08-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190822_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='configinfo',
            name='config_data',
            field=models.TextField(null=True, verbose_name='爬取全文'),
        ),
        migrations.AlterField(
            model_name='configinfo',
            name='url',
            field=models.TextField(null=True, verbose_name='爬取链接'),
        ),
    ]
