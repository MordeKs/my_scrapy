import scrapy


class TongchengSpider(scrapy.Spider):
    name = 'tongcheng'
    allowed_domains = ['qz.58.com']
    start_urls = ['https://qz.58.com/shouji/pn1/']

    def parse(self, response):
        page = 100
        detail_page = response.xpath('//*[@id="jingzhun"]/tbody/tr[1]/td[2]/div/a/text()')
        print(detail_page)