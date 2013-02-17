from scrapy import log
from scrapy import signals


class MyJsonExporter(object):
	def __init__(self, JsonFile):
		self.file = open(JsonFile, 'w')
		self.firstItem = True


	@classmethod
	def from_crawler(cls, crawler):
		JsonName= crawler.settings.get("MY_JSON_FILE", 'my.json')
		cls = cls(JsonName)
		crawler.signals.connect(cls.item_scraped, signal=signals.item_scraped)
		crawler.signals.connect(cls.spider_closed, signal = signals.spider_closed)

		return cls


	def item_scraped(self, item, spider):
		forWriting = item['mm'][1:-1]
		if self.firstItem:
			self.file.write("["+forWriting)
			self.firstItem = False
		else:
			self.file.write(","+forWriting)

		return item

	def spider_closed(self, spider):
		self.file.write("]")
		self.file.close()
		del self.file
