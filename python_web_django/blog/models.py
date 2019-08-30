from django.db import models


# Create your models here.
class Stu(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    url = models.TextField(default="", verbose_name="爬取链接")
    label = models.TextField(default="")

    # class Meta:
    #     app_label = 'blog'
    #     db_table = 'test_table'


class ConfigInfo(models.Model):
    url = models.TextField(verbose_name="爬取链接", null=True)
    config_data = models.TextField(verbose_name="爬取全文", null=True)
    config_css1 = models.CharField(max_length=255, verbose_name="爬取css1", null=True)
    config_css2 = models.CharField(max_length=255, verbose_name="爬取css2", null=True)
    config_type = models.CharField(max_length=100, verbose_name="爬取类型", null=True)
    config_people = models.CharField(max_length=100, verbose_name="操作人", null=True)
    config_table = models.CharField(max_length=100, verbose_name="存入表名", null=True)
    config_status = models.IntegerField(verbose_name="网页类型（动态或静态）", default=0)
    config_createTime = models.DateTimeField(u'create time', auto_now_add=True)
    config_updateTime = models.DateTimeField(u'update time', auto_now=True)
