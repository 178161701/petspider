from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class UrlUserAgent(BaseSpider):
    name = "UrlUserAgent.org"
    allowed_domains = ["UrlUserAgent.org"]
    start_urls = [
       "http://movie.douban.com/top250?start=0&filter="
    ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #  '//'不管多少层次找到底
                # hxs.xpath
        for moviename in hxs.select('//ol/li/div/div[@class="info"]/div[@class="hd"]/a/span[@class="title"][1]/text()').extract():
        	print (moviename)