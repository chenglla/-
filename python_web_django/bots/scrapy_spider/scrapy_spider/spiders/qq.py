# -*- coding: utf-8 -*-
import scrapy
from bots.scrapy_spider.scrapy_spider.items import ToutiaoSpiderItem
import json


class QQSpider(scrapy.Spider):
    name = "qq"

    # 这里初始化这个类,可以动态传值并开始爬虫,这里传的是keyword
    def __init__(self, keyword=None, *args, **kwargs):
        super(QQSpider, self).__init__(*args, **kwargs)
        # self.start_urls = ['https://s.taobao.com/search?q={}'.format(keyword)]
        self.url = keyword
        self.dynamic_css1 = kwargs.get('dynamic_css1')
        self.dynamic_css2 = kwargs.get('dynamic_css2')
        self.dynamic_data = kwargs.get('dynamic_data')
        self.dynamic_type = kwargs.get('dynamic_type')

    def start_requests(self):
        # urls = [
        #     'https://pacaio.match.qq.com/irs/rcd?cid=137&token=d0f13d594edfc180f5bf6b845456f3ea&ext=top&page=1'
        # ]
        #
        # for url in urls:
        print(self.url)
        yield scrapy.Request(url=self.url, dont_filter=False, callback=self.parse)

    # 解析首页的数据
    def parse(self, response):
        doc = json.loads(response.body_as_unicode())
        # for element in doc['data']:
        #     title = element['title']
        #     url = element['vurl']
        #     print(title, url)
        for element in doc[str(self.dynamic_data)]:
            item = ToutiaoSpiderItem()
            item['name'] = element[str(self.dynamic_css1)]
            item['label'] = self.dynamic_type
            item['url'] = element[str(self.dynamic_css2)]
            yield item
            # title = element[str(self.dynamic_css1)]
            # url = element[str(self.dynamic_css2)]
            # print(title, url)

        # 请求下一页的链接
        url = response.url
        print(url)
        # 先以&分开，得到page变量，再用=分开得到page的值
        list = url.split('&')
        page = int(list[3].split('=')[1])
        # if page < 95:
        if page < 15:
            page += 1
            newUrl = list[0] + '&' + list[1] + '&' + list[2] + '&page=' + str(page)
            # print(newUrl)
            yield scrapy.Request(url=newUrl, callback=self.parse)


