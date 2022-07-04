import scrapy


class ImotbgSpider(scrapy.Spider):
    name = 'imotbg'
    allowed_domains = ['www.imot.bg']
    start_urls = ['https://www.imot.bg/pcgi/imot.cgi?act=3&slink=7acern&f1=1/']

    def parse(self, response):
        product_container = response.xpath('/html/body/div[1]/table[1]/tbody/tr[1]/td[1]/table')

        for product in product_container:
            price = product.xpath('.//tbody/tr[2]/td[2]/div/text()').get()

            yield {
                'price': price,
            }

