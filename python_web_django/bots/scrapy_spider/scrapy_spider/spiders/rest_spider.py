# import scrapy, json
# from scrapy.http import Request
# from urllib import parse
# from bots.scrapy_spider.scrapy_spider.items import ToutiaoSpiderItem
#
#
# class ToutiaoSpider(scrapy.Spider):
#     name = 'toutiao'
#
#     def start_requests(self):
#         query_string = {
#             "offset": "0",
#             "format": "json",
#             "keyword": "甘肃",
#             "autoload": "true",
#             "count": "20",
#             "cur_tab": "1",
#             "from": "search_tab",
#             "pd": "synthesis"
#         }
#         qs = parse.urlencode(query_string)
#         url = 'https://www.toutiao.com/search_content/?' + qs
#         # url = "https://lf.snssdk.com/api/search/content/?" + qs
#         yield Request(url=url, callback=self.parse_init_data)
#
#     def parse_init_data(self, response):
#         res = json.loads(response.text)['data']
#         item = ToutiaoSpiderItem()
#         for i in res:
#             item['name'] = i['display']['lemmaTitle']
#             # item['description'] = i['display']['picAbs']
#             yield item
# -*- coding: utf-8 -*-
import scrapy
from bots.scrapy_spider.scrapy_spider.items import ToutiaoSpiderItem


class ToutiaoSpider(scrapy.Spider):
    name = "toutiao"

    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'SDCArticle.pipelines.SDCArticlesPipeline': 300,
    #     },
    # }
    # 这里初始化这个类,可以动态传值并开始爬虫,这里传的是keyword
    def __init__(self, keyword=None, *args, **kwargs):
        super(ToutiaoSpider, self).__init__(*args, **kwargs)
        # self.start_urls = ['https://s.taobao.com/search?q={}'.format(keyword)]
        self.url = keyword
        self.django_css = kwargs.get('django_css')
        self.django_url = kwargs.get('django_url')
        self.django_type = kwargs.get('django_type')
        self.static_date1 = kwargs.get('static_date1')

    def start_requests(self):
        headers = {
            # 'Referer': 'http://www.moe.gov.cn',
        }
        print(self.url)
        yield scrapy.Request(url=self.url, dont_filter=False, headers=headers, callback=self.parse)

    def parse(self, response):
        links = response.css(str(self.django_css))
        # print(response.body)
        # links = response.css('#list > li ')
        for link in links:
            title = link.css('::text').extract_first()
            # url_content = link.css('a::attr(href)').extract_first()
            url_content = link.css(str(self.django_url)).extract_first()
            # title = link.css('a::text').extract_first()
            url_content = response.urljoin(url_content)
            # url_content = response.urljoin(url_content)
            item = ToutiaoSpiderItem()
            item['name'] = title
            item['url'] = url_content
            item['label'] = self.django_type
            item['createTime'] = self.static_date1
            print(title)
            yield item
