import scrapy

class DianyinSpider(scrapy.Spider):
    name = "dianyin"
    allowed_domains = ["dytt8.net"]
    start_urls = [
        "https://www.dytt8.net/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        #/html/head/title
        title=response.xpath('/html/head/title/text()').extract_first("")
        print title;

