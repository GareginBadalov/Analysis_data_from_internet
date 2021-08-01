from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from lesson_6.lerua.lerua.spiders.leruamerlin import LeruamerlinSpider
from lesson_6.lerua.lerua import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeruamerlinSpider)
    process.start()
