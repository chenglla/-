# Generated by Django 2.2.3 on 2019-08-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190820_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu',
            name='label',
            field=models.TextField(default=''),
        ),
    ]
