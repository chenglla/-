# -*- coding: utf-8 -*-

# Scrapy settings for bots project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath('.')))
# os.environ['DJANGO_SETTINGS_MODULE'] = 'python_web_django.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_web_django.settings")# project_name 项目名称
django.setup()

ITEM_PIPELINES = {
    'scrapy_spider.pipelines.TestbotPipeline': 1
}

BOT_NAME = 'scrapy_spider'

SPIDER_MODULES = ['scrapy_spider.spiders']
NEWSPIDER_MODULE = 'scrapy_spider.spiders'
# from bots import setup_django_env
#
# setup_django_env()
#
# BOT_NAME = 'bots'
#
# SPIDER_MODULES = ['bots.spiders']
# NEWSPIDER_MODULE = 'bots.spiders'
#
# DOWNLOAD_HANDLERS = {'s3': None}
# DOWNLOAD_DELAY = 0.5
# DOWNLOAD_TIMEOUT = 100
#
# CONCURRENT_REQUESTS_PER_IP = 1
#
# ITEM_PIPELINES = {
#     'scrapy_spider.pipelines.TestbotPipeline': 1,
# }
#


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'bots (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'bots.middlewares.ScrapySpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'bots.middlewares.ScrapySpiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'bots.pipelines.ScrapySpiderPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# UAPOOL = ["Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
#           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
#           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"]
# # 间隔时间，单位秒。指明scrapy每两个请求之间的间隔。
# DOWNLOAD_DELAY = 5
#
# # 当访问异常时是否进行重试
# RETRY_ENABLED = True
# # 当遇到以下http状态码时进行重试
# RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]
# # 重试次数
# RETRY_TIMES = 5
#
# # Pipeline的并发数。同时最多可以有多少个Pipeline来处理item
# CONCURRENT_ITEMS = 200
# # 并发请求的最大数
# CONCURRENT_REQUESTS = 100
# # 对一个网站的最大并发数
# CONCURRENT_REQUESTS_PER_DOMAIN = 50
# # 对一个IP的最大并发数
# CONCURRENT_REQUESTS_PER_IP = 50