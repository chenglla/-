# Generated by Django 2.2.3 on 2019-08-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190819_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(verbose_name='爬取链接')),
            ],
        ),
    ]
