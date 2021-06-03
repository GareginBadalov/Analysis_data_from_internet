# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from lesson_5.first_parser.first_parser.items import FirstParserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://krasnodar.hh.ru/search/vacancy?area=&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//span[@class='bloko-form-spacer']/a[@class='bloko-button' and 1]")
        next_page = next_page[0].xpath('@href').extract()[0]
        yield response.follow(next_page, callback=self.parse)

        vacansy = response.css(
            'div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)'
        ).extract()

        for link in vacansy:
            yield response.follow(link, callback=self.vacansy_parse)

    def vacansy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='bloko-header-1']/text()").extract()
        salary = ''.join(response.xpath("//p[@class='vacancy-salary']/span[@class='bloko-header-2 bloko-header-2_lite']/text()").extract())
        link = response.url
        suite = self.allowed_domains[0]
        print(name, salary, link, suite)
        yield FirstParserItem(name=name, salary=salary, link=link, suite=suite)