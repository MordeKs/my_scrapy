# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class Samecity58ItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class Samecity58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prices = scrapy.Field()
    goods = scrapy.Field()
    url = scrapy.Field()
    chapter_name = scrapy.Field()
