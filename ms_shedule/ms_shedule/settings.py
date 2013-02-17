# Scrapy settings for ms_shedule project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ms_shedule'

SPIDER_MODULES = ['ms_shedule.spiders.spiderino']
NEWSPIDER_MODULE = 'ms_shedule.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17" 
LOG_FILE = "crawl.log"
MY_PORTS_FILE = "../ms_ports/ports.json"
FEED_FORMAT = 'json'
FEED_URI = 'file:///schedule.json'
CLOSESPIDER_ITEMCOUNT = 100
DOWNLOAD_DELAY = 0.5
