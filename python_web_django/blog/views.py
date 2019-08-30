from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.core import serializers
import requests
from selenium import webdriver
# 引入Keys类包 发起键盘操作
from selenium.webdriver.common.keys import Keys
import time


# Create your views here.

def addConfig(request):
    list = []
    print(request.GET.get('status_select'))
    if int(request.GET.get('status_select')) == 1:
        link = request.GET.get('link')
        django_css = request.GET.get('django_css')
        django_type = request.GET.get('django_type')
        django_t = request.GET.get('django_t')
        django_people = request.GET.get('django_people')
        # 查询某个字段
        print(link)
        for i in ConfigInfo.objects.values('url'):
            list.append(i['url'])
        if link not in list:
            # # 表中添加数据
            ConfigInfo.objects.create(url=link, config_people=django_people, config_table=django_t,
                                      config_type=django_type, config_css1=django_css,
                                      config_status=1)
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'scrapy_spider', 'spider': 'toutiao', 'keyword': link, 'django_css': django_css,
                'django_type': django_type}
        # data = {'project': 'scrapy_spider', 'spider': 'toutiao', 'keyword': link, 'django_css': django_css, 'django_a_css': django_a_css}
        print(requests.post(url=url, data=data))
        # 等待爬虫完成
        # time.sleep(10)
        # json_filter = getDB(link)
        return JsonResponse({"status": 0, "message": "爬取完成"})
        # return JsonResponse({"status": 0, "message": "this is lulu 0", "data": json_filter})
    else:
        print('aaaaaaaaaaaaaaaaa')
        dynamic_link = request.GET.get('dynamic_link')
        dynamic_data = request.GET.get('dynamic_data')
        dynamic_css1 = request.GET.get('dynamic_css1')
        dynamic_css2 = request.GET.get('dynamic_css2')
        dynamic_type = request.GET.get('dynamic_type')
        dynamic_t = request.GET.get('dynamic_t')
        dynamic_people = request.GET.get('dynamic_people')
        print(dynamic_link)
        # 查询某个字段
        for i in ConfigInfo.objects.values('url'):
            list.append(i['url'])
        if dynamic_link in list:
            # # 表中添加数据
            ConfigInfo.objects.create(url=dynamic_link, config_people=dynamic_people, config_table=dynamic_t,
                                      config_type=dynamic_type,
                                      config_css1=dynamic_css1, config_css2=dynamic_css2, config_status=2,
                                      config_data=dynamic_data
                                      )
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'scrapy_spider', 'spider': 'qq', 'keyword': dynamic_link, 'dynamic_css1': dynamic_css1,
                'dynamic_css2': dynamic_css2, 'dynamic_data': dynamic_data, 'dynamic_type': dynamic_type}
        # data = {'project': 'scrapy_spider', 'spider': 'toutiao', 'keyword': link, 'django_css': django_css, 'django_a_css': django_a_css}
        print(requests.post(url=url, data=data))
        return JsonResponse({"status": 0, "message": "配置爬取完成"})


def getDB(link):
    json = serializers.serialize("json", Stu.objects.all())
    print(json)
    # 条件查询label=“”
    json_filter = serializers.serialize("json", Stu.objects.filter(label=link))
    if json_filter is not None:
        return json_filter


def selectConfig(request):
    content = serializers.serialize("json", ConfigInfo.objects.all())
    # content = ConfigInfo.objects.values()
    print(content)
    return JsonResponse({"status": 0, "message": "这是模板配置信息", "data": content})


def selectData(request):
    content = serializers.serialize("json", Stu.objects.all())
    # content = ConfigInfo.objects.values()
    print(content)
    return JsonResponse({"status": 0, "message": "这是模板配置信息", "data": content})


def ret_user(request):
    if request.method == "GET":
        # db = Stu.objects.all()
        # db = [i.name for i in db]
        # return JsonResponse({"status": 0, "data": db})
        json = serializers.serialize("json", Stu.objects.all())
        return JsonResponse({"status": 0, "data": json})
    else:
        return JsonResponse({"status": 1, "message": "you need GET method"})


def autoSelect(request):
    keyw = request.GET.get('keyw')
    chrome_driver = r"D:\anaconda\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver)
    # driver = webdriver.Chrome()
    # 访问百度
    driver.get('http://www.baidu.com')

    # 输入框输入内容
    driver.find_element_by_id('kw').send_keys(keyw)
    # 3s
    time.sleep(3)

    # # 模拟回车操作 ,开始搜索
    driver.find_element_by_id('su').send_keys(Keys.ENTER)
    time.sleep(3)


def pubCrawl(request):
    pubName = request.GET.get('pubName')
    pubLink = request.GET.get('pubLink')
    pub_peo = request.GET.get('pub_peo')
    pub_tab = request.GET.get('pub_tab')
    pub_Field = request.GET.get('pub_Field')
    if pubLink not in list:
        # # 表中添加数据
        ConfigInfo.objects.create(url=pubLink, config_people=pub_peo, config_table=pub_tab,
                                  config_type=pubName, config_css1=pub_Field,
                                  config_status=1)
    url = 'http://localhost:6800/schedule.json'
    data = {'project': 'scrapy_spider', 'spider': 'pubCrawl', 'keyword': pubLink, 'django_css': pub_Field,
            'django_type': pubName + '公众号'}
    # data = {'project': 'scrapy_spider', 'spider': 'toutiao', 'keyword': link, 'django_css': django_css, 'django_a_css': django_a_css}
    print(requests.post(url=url, data=data))
