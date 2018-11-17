import scrapy

class DianyinSpider(scrapy.Spider):
    name = "dianyin"
    allowed_domains = ["dytt8.net"]
    start_urls = [
        "https://www.dytt8.net/",
        "https://www.dytt8.net/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)