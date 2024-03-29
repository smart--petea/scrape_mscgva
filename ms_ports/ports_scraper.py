#!/usr/bin/python2

from scrapy.settings import CrawlerSettings
from ms_ports import settings
from scrapy import log
from scrapy.crawler import CrawlerProcess


MySettings = CrawlerSettings(settings_module = settings)
MyCrawler = CrawlerProcess(MySettings)
log.start_from_crawler(MyCrawler)
MyCrawler.configure()

for spider_object in MyCrawler.spiders._spiders.itervalues():
	MyCrawler.crawl(spider_object())

MyCrawler.start()
