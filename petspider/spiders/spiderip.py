from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class SpiderIps(BaseSpider):
    name = "SpiderIps.org"
    allowed_domains = ["SpiderIps.org"]
    start_urls = [
       # "http://www.nianshao.me/"
       "http://www.whatismyip.com.tw/"
    ]

    def parse(self, response):
        # print (response.body)
        hxs = HtmlXPathSelector(response)
        #  '//'不管多少层次找到底
        for ip in hxs.select('//script[@id="ip-json"]/text()').extract():
        	print (ip)