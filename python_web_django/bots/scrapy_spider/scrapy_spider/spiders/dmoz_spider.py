import scrapy
from bots.scrapy_spider.scrapy_spider.items import ToutiaoSpiderItem
import json
from bots.scrapy_spider.scrapy_spider.getIp import GetIpThread


# 导入settings文件中的UPPOOL
# 导入官方文档对应的HttpProxyMiddleware


# 导入settings文件中的UPPOOL
# 导入官方文档对应的HttpProxyMiddleware


# 获取代理IP的线程类
# class GetIpThread(threading.Thread):
#     def __init__(self, apiUrl, fetchSecond):
#         super(GetIpThread, self).__init__()
#         self.fetchSecond = fetchSecond
#         self.apiUrl = apiUrl
#
#     def run(self):
#         while True:
#             # 获取IP列表
#             res = requests.get(self.apiUrl).content.decode()
#             # 按照,分割获取到的IP
#             bots.scrapy_spider.scrapy_spider.settings.IPPOOL = res.split(',')[0]
#             print('获取到的ip：', bots.scrapy_spider.scrapy_spider.settings.IPPOOL)
#             #
#             time.sleep(self.fetchSecond)


class DmozSpider(scrapy.Spider):
    name = 'pubCrawl'
    print('gagagagaga')
    # # 这里填写无忧代理IP提供的API订单号（请到用户中心获取）
    order = "bcc89bef63ab6dd976d9a80191f7e7be"
    # 获取IP的API接口
    # apiUrl = "http://api.ip.goubanjia.com/dynamic/get.html?order=" + order
    apiUrl = "http://dynamic.goubanjia.com/dynamic/get/" + order + ".html?ttl"
    # 获取IP时间间隔，建议为5秒
    fetchSecond = 5
    # 开始自动获取IP
    GetIpThread(apiUrl, fetchSecond).start()

    # host = "api.ip.goubanjia.com"

    # 这里初始化这个类,可以动态传值并开始爬虫,这里传的是keyword
    def __init__(self, keyword=None, *args, **kwargs):
        super(DmozSpider, self).__init__(*args, **kwargs)
        # self.start_urls = ['https://s.taobao.com/search?q={}'.format(keyword)]
        self.url = str(keyword)
        self.dynamic_css = kwargs.get('dynamic_css1')
        self.dynamic_type = kwargs.get('dynamic_type')

    def start_requests(self):
        # start_urls = [
        #     # https://mp.weixin.qq.com/cgi-bin/appmsg?token=1508146730&lang=zh_CN&f=json&ajax=1&random=0.3073565099822291&action=list_ex&begin=5&count=5&query=&fakeid=MzA4MTA0NTAyNw%3D%3D&type=9
        #     "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA4MTA0NTAyNw==&f=json&offset=20&count=10&is_ok=1&scene=124&uin=MTc1MjY3ODMzMA%3D%3D&key=af995e53853344b59636160bd21dea21ece84943f3034f2566881a7632ffdf314d46f715d00c5db34b271d935c65e910cb75a0cce963e64b9641d38b75def56f5c9d2e9839aeda1141e89986586f6ad9&pass_ticket=yup14NX4g6ZludqTUnulKTf%2F7foKpQS2HTTli35R92%2FD79Up9s4DumgwWHfaXcyj&wxtoken=&appmsg_token=1018_M8GpP5Ml6XpXMC6R6hFrTEkpgs-gIEaynxJD8g~~&x5=0&f=json"]
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        print('当前连接：', response.url)
        doc = json.loads(response.body_as_unicode())
        print(doc)
        lists = doc['general_msg_list']
        content = json.loads(lists)
        # print(content[0])
        for list in content['list']:
            # info = list['app_msg_ext_info']
            print(list)
            # tutorialItem = ToutiaoSpiderItem()
            # tutorialItem['name'] = info['title']
            # tutorialItem['label'] = self.dynamic_type
            # tutorialItem['url'] = self.url
            # yield tutorialItem
            # # tutorialItem['inputtime'] = info['title']
            # # tutorialItem['is_delete'] = info['title']
            # print(list['app_msg_ext_info'])

        # countList = response.url.split('count')
        # lists = countList[0].split('&')
        # list = lists[3].split('=')
        # page = int(list[1])
        # if page < 100:
        #     page = page + 11
        #     url = lists[0] + '&' + lists[1] + '&' + lists[2] + '&' + list[0] + '=' + str(page) + '&' + 'count' + \
        #       countList[1]
        # # url = countList[0] + 'count' + countList[1]
        #     print('新url：', url)
        #     yield scrapy.Request(url=url, callback=self.parse)


# class Uamid(UserAgentMiddleware):
#     # 初始化 注意一定要user_agent，不然容易报错
#     def __init__(self, user_agent=''):
#         self.user_agent = user_agent
#
#     # 请求处理
#     def process_request(self, request, spider):
#         # 先随机选择一个用户代理
#         thisua = random.choice(UAPOOL)
#         print("当前使用User-Agent是：" + thisua)
#         request.headers.setdefault('User-Agent', thisua)
