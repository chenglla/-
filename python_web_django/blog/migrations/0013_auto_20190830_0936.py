# Generated by Django 2.2.3 on 2019-08-30 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190822_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configinfo',
            name='config_status',
            field=models.IntegerField(default=0, verbose_name='网页类型（动态或静态）'),
        ),
    ]
