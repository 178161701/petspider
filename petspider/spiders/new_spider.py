from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class NewSpider(BaseSpider):
    name = "new.org"
    allowed_domains = ["new.org"]
    start_urls = [
       "http://geek.csdn.net/forum/AI"
    ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        for url in hxs.select('//a/@href').extract():
        	print (url)