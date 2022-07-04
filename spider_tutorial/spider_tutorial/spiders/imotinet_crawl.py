import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ImotinetCrawlSpider(CrawlSpider):
    name = 'imotinet_crawl'
    allowed_domains = ['imoti.net']
    start_urls = ['https://imoti.net/bg/obiavi/r/prodava/plovdiv/?sid=hRTfWw/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='list-view real-estates']/li/a")),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//a[@class='next-page-btn']"))),
    )

    def parse_item(self, response):
        article = response.xpath("//div[@class='page-content']")
        yield {
            'type_m2': article.xpath("./section/header/h2/text()").get(),
            'location': article.xpath("./section/header/span[@class='location']/text()").get(),
            'description': article.xpath("./section/div[@class='text']/p/text()").get(),
            'flore': article.xpath("./aside/section/div[@class='simple-table']/table/tbody/tr[3]/td[2]/text()").get(),
            'construction': article.xpath("./aside/section/div[@class='simple-table']/table/tbody/tr[4]/td[2]/text()").get(),
            'year': article.xpath("./aside/section/div[@class='simple-table']/table/tbody/tr[5]/td[2]/text()").get(),
            'akt16': article.xpath("./aside/section/div[@class='simple-table']/table/tbody/tr[6]/td[2]/text()").get(),
            'extras': article.xpath("./aside/section/ul[@class='extras']/li/text()").getall(),
            'price': article.xpath("./aside[@class='info-sidebar']/section/header/div[@class='big-price']/strong/text()").get(),
            'url': response.url,
        }

