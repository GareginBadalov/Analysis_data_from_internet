# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstParserItem(scrapy.Item):
    name = scrapy.Field()
    salary = scrapy.Field()
    _id = scrapy.Field()
    link = scrapy.Field()
    suite = scrapy.Field()
