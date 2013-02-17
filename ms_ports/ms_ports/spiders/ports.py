from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy import log
from ms_ports.items import MsPortsItem

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MsSpider(BaseSpider):
	name = 'MsSpider'
	allowed_domains = ['www.mscgva.ch']

	def start_requests(self):
		alph = "abcdefghijklmnopqrstuvwxyz"
		for x in alph:
			for y in alph:
				yield Request("http://www.mscgva.ch/php/schedules/OSLocations.php?term="+x + y, callback = self.parse)

	def parse(self, response):
		if not response.body: return
		print(response.url)
		item = MsPortsItem()
		item['mm'] = response.body
		yield item
