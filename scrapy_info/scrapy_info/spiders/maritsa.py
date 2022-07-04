import scrapy


class MaritsaSpider(scrapy.Spider):
    name = 'maritsa'
    allowed_domains = ['www.marica.bg']
    start_urls = ['https://www.marica.bg/imoti']

    def parse(self, response):
        container = response.xpath('//div[contains(@class,"col-lg-8")]/article')

        for element in container:
            lks = element.xpath('.//a/@href').get()
            title = element.xpath('.//a/div/div[2]/div[1]/h3/text()').get()
            text = element.xpath(".//a/div/div/div/div[@class='article-text']/text()").get()
            date = element.xpath(".//a/div/div[2]/div/div[2]/div[1]/div/span[2]/text()").get()

            yield {
                'title': title,
                'date': date,
                'link': lks,
                'text': text
            }
