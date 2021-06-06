import scrapy
from scrapy.http import HtmlResponse
from lesson_6.lerua.lerua.items import LeruaItem
from scrapy.loader import ItemLoader


class LeruamerlinSpider(scrapy.Spider):
    name = 'leruamerlin'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['http://leroymerlin.ru/']

    def __init__(self):
        self.start_urls = ["https://leroymerlin.ru/catalogue/okna-i-podokonniki/"]

    def parse(self, response):
        ads_links = response.xpath("//div[@class='phytpj4_plp largeCard']/a[@class='bex6mjh_plp b1f5t594_plp iypgduq_plp nf842wf_plp']/@href").extract()
        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='header-2']/text()").extract_first()
        photos = response.xpath('//uc-pdp-media-carousel/img[1]/@src').extract_first()
        price = response.xpath("//uc-pdp-price-view/span[@slot='price']/text()").extract()
        yield LeruaItem(name=name, photos=photos, price=price)
        print(name, photos, price)


