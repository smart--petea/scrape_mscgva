from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy import log
from ms_shedule.items import MsSheduleItem

import re
import json, base64

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


DATA = '2013-02-15'
WEEKS = '6'
reStroka = re.compile(r'<span class="tooltip" title=".*?">(.*?)<.*?>(\w+)<.*?>(\w+)<.*?>([\w ]+?)<.*?>([\w ]+?)<.*?>(\w+?)<.*?>([\w ]+?)<')

class SpiderIno(BaseSpider):
	name = 'MySpider'

	def start_requests(self):
		JsonFile = self._crawler.settings.get("MY_PORTS_FILE", None)
		if not JsonFile:
			log.msg(message="SpiderIno, start_request, MY_PORTS_FILE is not defined")
		try:
			ffile = open(JsonFile, 'r')
		except IOError as e:
			log.msg(message="SpiderIno, start_request, failed to open MY_PORTS_FILE with error %s" % str(e))
			return

		stroka = ffile.read()
		ffile.close()
		del ffile, JsonFile
				
		OriginList  = json.loads(stroka)
		DestinationList = OriginList[:]
		for origin in OriginList:
			DestinationList.remove(origin)
			for destination in DestinationList:

				meta = {}
				meta['origin'] = origin
				meta['destination'] = destination
				meta['category'] = 'D'
				forB64 = '*'.join([origin['label'], origin['name']+', '+origin['country'], origin['msccode'], destination['label'], destination['name']+', '+ destination['country'], destination['msccode'], DATA, WEEKS, 'D'])
				forB64en = base64.b64encode(forB64)
				yield Request('http://www.mscgva.ch/php/schedules/OSData.php?e='+forB64en, meta = meta)

				meta['category'] = 'A'
				forB64 = '*'.join([origin['label'], origin['name']+', '+origin['country'], origin['msccode'], destination['label'], destination['name']+', '+ destination['country'], destination['msccode'], DATA, WEEKS, 'A'])
				forB64en = base64.b64encode(forB64)
				yield Request('http://www.mscgva.ch/php/schedules/OSData.php?e='+forB64en, meta = meta)

	def parse(self, response):

		MyList = reStroka.findall(response.body)
		if MyList == []:
			return
		print(response.url)
		meta = response.meta
		item = MsSheduleItem()
		item['origin'] = meta['origin']
		item['destination'] = meta['destination']
		item['category'] = meta['category']
		item['table'] = []
		for x in MyList:
			item['table'].append(
								{
									'vessel': x[0],
									'voyage': x[1],
									'departure day':x[2],
									'departure date': x[3],
									'transit':x[4],
									'arrival day':x[5],
									'arrival date': x[6],
								}			
								)
		return item
