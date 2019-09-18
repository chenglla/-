import requests
import time
import threading
import bots.scrapy_spider.scrapy_spider.goubanjia
import requests.packages


# 获取代理IP的线程类
class GetIpThread(threading.Thread):
    def __init__(self, apiUrl, fetchSecond):
        super(GetIpThread, self).__init__()
        self.fetchSecond = fetchSecond
        self.apiUrl = apiUrl

    def run(self):
        # while True:
        # 获取IP列表
            print('线程开始')
            res = requests.get(self.apiUrl).content.decode()
            # 按照,分割获取到的IP
            bots.scrapy_spider.scrapy_spider.goubanjia.IPPOOL = res.split(',')[0]
            print('获取到的ip：', bots.scrapy_spider.scrapy_spider.goubanjia.IPPOOL)
            # 休眠
            time.sleep(self.fetchSecond)



