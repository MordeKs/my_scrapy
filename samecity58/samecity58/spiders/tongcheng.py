import scrapy
import time


class TongchengSpider(scrapy.Spider):
    name = 'tongcheng'
    allowed_domains = ['qz.58.com']
    start_urls = ['https://qz.58.com/shouji/pn2/']

    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        'LOG_FILE': '5688_log_%s.txt' % time.time(),  # 配置的日志
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
    }

    def parse(self, response):
        page = 100
        detail_page = response.css('.tdiv')
        for i in detail_page:
            print(i)