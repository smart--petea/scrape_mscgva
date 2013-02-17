# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MsSheduleItem(Item):
	origin = Field()
	destination = Field()
	table = Field()
	category = Field()

