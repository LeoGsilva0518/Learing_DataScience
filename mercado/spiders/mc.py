import scrapy


class McSpider(scrapy.Spider):
    name = 'mc'
    #allowed_domains = ['atacadao.com']
    start_urls = ['https://www.atacadao.com.br/bebidas/']

    def parse(self, response, **kwargs):
        for i in response.xpath('//div[@class="product-box"]'):
            price = i.xpath('.//span[@class="product-box__price--number"]//text()').getall()
            title = i.xpath('.//h2[@class="product-box__name"]/text()').get()
            link = i.xpath('./a/@href=').get()

            yield {
                'price': price,
                'title': title,
                'link': link
            }