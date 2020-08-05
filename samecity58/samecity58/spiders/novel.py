import scrapy
import time
from items import Samecity58Item, Samecity58ItemLoader


class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['qu.la']
    start_urls = ['https://www.qu.la/book/109018/']
    custom_settings = {
        # 'LOG_LEVEL': 'DEBUG',
        # 'LOG_FILE': '5688_log_%s.txt' % time.time(),  # 配置的日志
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
    }

    def parse(self, response):
        item_nodes = response.css('.section-list.fix ul')
        for item_node in item_nodes:
            print(item_node)
            item_loader = Samecity58ItemLoader(item=Samecity58Item(),selector=item_node)
            item_loader.add_css("chapter_name", "li a::text")
