import scrapy


class ImotinetSpider(scrapy.Spider):
    name = 'imotinet'
    allowed_domains = ['www.imoti.net']
    start_urls = ['https://www.imoti.net/bg/obiavi/r/prodava/plovdiv/?sid=hRTfWw/']

    def parse(self, response):
        product_container = response.xpath("//div[@class='wrapper sidebar-layout padded-bottom']/div/ul/li")

        for product in product_container:
            ap_type = product.xpath('.//div[@class="real-estate-text"]/header/div[@class="inline-group"]/h3/text()').get()
            sq_meters = product.xpath('.//div[@class="real-estate-text"]/header/div[@class ="inline-group"]/h3/span[2]/text()').get()
            address = product.xpath('.//div[@class="real-estate-text"]/header/div[@class ="inline-group"]/span/text()').get()
            price = product.xpath('.//div[@class="real-estate-text"]/header/strong/text()').get()
            flore = product.xpath('.//div[@class="real-estate-text"]/ul/li[1]/strong/text()').get()
            price_m2 = product.xpath('.//div[@class="real-estate-text"]/ul/li[2]/strong/text()').get()
            description = product.xpath('.//div[@class="real-estate-text"]/p[2]/text()').get()
            # link = product.xpath()



            yield {
                'ap_type':ap_type,
                'sq_meters': sq_meters,
                'address': address,
                'price': price,
                'flore': flore,
                'price_m2': price_m2,
                'description': description,
            }

