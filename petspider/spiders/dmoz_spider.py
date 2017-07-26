'''import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz" #运行时的name
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.w3cschool.cn/html/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
'''
# scrapy crawl dmoz


from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
    name = "dmoz.org"
    allowed_domains = ["dmoz.org"]
    start_urls = [
       "http://www.w3cschool.cn/html/",
       "http://blog.csdn.net/olanlanxiari/article/details/48196255"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)


# scrapy crawl dmoz.org