from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.core import serializers
import requests
from selenium import webdriver
# 引入Keys类包 发起键盘操作
from selenium.webdriver.common.keys import Keys
import time
from django.utils import timezone
from django.http import HttpResponse
import json
import base64
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def addConfig(request):
    list = []
    print(request.GET.get('status_select'))
    if int(request.GET.get('status_select')) == 1:
        link = request.GET.get('link')
        django_css = request.GET.get('static_css')
        django_url = request.GET.get('static_url')
        django_type = request.GET.get('static_type')
        django_t = request.GET.get('static_t')
        django_people = request.GET.get('static_people')
        # 查询某个字段
        print(link)
        for i in ConfigInfo.objects.values('url'):
            list.append(i['url'])
        if link not in list:
            # # 表中添加数据
            ConfigInfo.objects.create(url=link, config_people=django_people, config_table=django_t,
                                      config_type=django_type, config_css1=django_css, config_css2=django_url,
                                      config_status=1)
        # url = 'http://localhost:6800/schedule.json'
        # data = {'project': 'scrapy_spider', 'spider': 'toutiao', 'keyword': link, 'django_css': django_css,
        #         'django_type': django_type}
        # # data = {'project': 'scrapy_spider', 'spider': 'toutiao', 'keyword': link, 'django_css': django_css, 'django_a_css': django_a_css}
        # print(requests.post(url=url, data=data))
        # 等待爬虫完成
        # time.sleep(10)
        # json_filter = getDB(link)
        return JsonResponse({"status": 0, "message": "模板存库爬取完成"})
        # return JsonResponse({"status": 0, "message": "this is lulu 0", "data": json_filter})
    else:
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
        if dynamic_link not in list:
            # # 表中添加数据
            ConfigInfo.objects.create(url=dynamic_link, config_people=dynamic_people, config_table=dynamic_t,
                                      config_type=dynamic_type,
                                      config_css1=dynamic_css1, config_css2=dynamic_css2, config_status=2,
                                      config_data=dynamic_data
                                      )
        # url = 'http://localhost:6800/schedule.json'
        # data = {'project': 'scrapy_spider', 'spider': 'qq', 'keyword': dynamic_link, 'dynamic_css1': dynamic_css1,
        #         'dynamic_css2': dynamic_css2, 'dynamic_data': dynamic_data, 'dynamic_type': dynamic_type}
        # # data = {'project': 'scrapy_spider', 'spider': 'toutiao', 'keyword': link, 'django_css': django_css, 'django_a_css': django_a_css}
        # print(requests.post(url=url, data=data))
        return JsonResponse({"status": 0, "message": "模板存库爬取完成"})


def getId(request):
    info = Stu.objects.all().last()
    data = model_to_dict(info)
    id = data['id']
    return JsonResponse({"status": 0, "message": "获取id成功", "id": id})


def crawl(request):
    # info = Stu.objects.all().last()
    # data = model_to_dict(info)
    # id = data['id']
    # print(id)
    # s = HttpResponse(json.dumps(data), content_type="application/json")
    # print(s)
    if int(request.GET.get('status_select')) == 2:
        dynamic_link = request.GET.get('dynamic_link')
        dynamic_data = request.GET.get('dynamic_data')
        dynamic_css1 = request.GET.get('dynamic_css1')
        dynamic_css2 = request.GET.get('dynamic_css2')
        # dynamic_type = request.GET.get('dynamic_type')
        dynamic_date = request.GET.get('dynamic_date')
        dynamic_type = request.GET.get('dynamic_name')
        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'scrapy_spider', 'spider': 'qq', 'keyword': dynamic_link, 'dynamic_css1': dynamic_css1,
                'dynamic_css2': dynamic_css2, 'dynamic_data': dynamic_data, 'dynamic_type': dynamic_type,
                'dynamic_date': dynamic_date}
        print(requests.post(url=url, data=data))
        return JsonResponse({"status": 0, "message": "动态网址爬取完成"})
    else:
        link = request.GET.get('link')
        django_css = request.GET.get('static_css')
        django_url = request.GET.get('static_url')
        # django_type = request.GET.get('static_type')
        django_name = request.GET.get('static_name')
        static_date1 = request.GET.get('static_date1')

        url = 'http://localhost:6800/schedule.json'
        data = {'project': 'scrapy_spider', 'spider': 'toutiao', 'keyword': link, 'django_css': django_css,
                'django_type': django_name, 'django_url': django_url, 'static_date1': static_date1}
        print(requests.post(url=url, data=data))
        return JsonResponse({"status": 0, "message": "静态网址爬取完成"})
    #     return JsonResponse({"status": 0, "message": "静态网址爬取完成", "id": id})


def getCrawlData(request):
    id = request.GET.get('id')
    # list = Stu.objects.filter(id__gt=6670)
    list = Stu.objects.filter(id__gt=int(id))
    data = serializers.serialize('json', list)
    print(data)
    return JsonResponse({"status": 0, "message": "静态网址爬取完成", "data": data})


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
    print(request.GET.get('page'))
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


def saveEdit(request):
    name = request.GET.get('name')
    name = str(''.join(name))
    url = request.GET.get('url')
    url = str(''.join(url))
    label = request.GET.get('label')
    label = str(''.join(label))
    id = request.GET.get('id')
    print(id)
    info = Stu.objects.get(id=int(id))
    info.url = url
    info.label = label
    info.name = name
    info.save()
    return JsonResponse({"status": 'ok', "message": "Edit succeed"})


def updatePass(request):
    oldPass = request.GET.get('oldPass')
    newPass = request.GET.get('newPass')
    return JsonResponse({"status": 'ok', "message": "修改成功"})


def saveEditMoudle(request):
    config_type = request.GET['config_type'],
    config_type = str(''.join(config_type))
    print(config_type)
    print(type(config_type))
    url = request.GET.get('url'),
    url = str(''.join(url))
    config_css1 = request.GET['config_css1'],
    config_css1 = str(''.join(config_css1))
    # print('cs:',a)
    config_css2 = request.GET.get('config_css2'),
    config_css2 = str(''.join(config_css2))
    config_people = str(''.join(request.GET.get('config_people'))),
    config_people = str(''.join(config_people))
    config_status = request.GET.get('config_status'),
    config_createTime = timezone.now().strftime("%Y-%m-%d"),
    print(config_createTime)
    # url = request.GET.get('url'),
    # config_css1 = request.GET.get('config_css1'),
    # config_css2 = request.GET.get('config_css2'),
    # config_people = request.GET.get('config_people'),
    # config_status = request.GET.get('config_status'),
    # config_createTime = timezone.now().strftime("%Y-%m-%d"),
    # print(config_createTime)
    id = request.GET.get('id')

    info = ConfigInfo.objects.get(id=id)
    # print(type(info))
    # info = json.loads(info)
    # print('a:', info)
    info.url = url
    info.config_type = config_type
    info.config_css1 = config_css1
    info.config_css2 = config_css2
    info.config_people = config_people
    info.config_status = int(config_status[0])
    info.config_updateTime = config_createTime
    info.save()
    print('b:', info)
    # info = json.loads(str(info))
    # info = serializers.serialize("json", info)
    return JsonResponse({"status": 'ok', "message": "EditMoudle succeed"})


def delConfig(request):
    id = request.GET.get('id')
    ConfigInfo.objects.get(id=int(id)).delete()
    return JsonResponse({"status": 'ok', "message": "delete config succeed"})


def delData(request):
    id = request.GET.get('id')
    Stu.objects.get(id=int(id)).delete()
    return JsonResponse({"status": 'ok', "message": "delete succeed"})


def selectLine(request):
    list = []
    data = []
    lists = Stu.objects.values('createTime').distinct().order_by('createTime')
    for i in lists:
        print(i)
        list.append(i['createTime'])
        num = Stu.objects.filter(createTime=i['createTime']).count()
        data.append(num)
        print(num)
    print(list)
    print(data)
    return JsonResponse({"status": 'ok', "message": "delete succeed", "data": data, "list": list})


def selectPie(request):
    list = []
    option = []
    # 去重
    lists = Stu.objects.values('label').distinct()
    for i in lists:
        each = {}
        print(i['label'])
        num = Stu.objects.filter(label=i['label']).count()
        print(num)
        each = {'name': i['label'], 'value': num}
        option.append(i['label'])
        list.append(each)
    print(list)
    print(option)
    return JsonResponse({"status": 'ok', "message": "delete succeed", "data": list, "list": option})
    # Stu.objects.get()


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


# 加载静态界面index首页
def index(request):
    # request.META["CSRF_COOKIE_USED"] = True
    return render(request, 'index.html', {"zidian": 324})
