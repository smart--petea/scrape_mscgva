# Scrapy settings for ms_ports project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ms_ports'

SPIDER_MODULES = ['ms_ports.spiders.ports']
NEWSPIDER_MODULE = 'ms_ports.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537/17 (KHTML, like Gecko) Chrome/24.0.1312.57"
LOG_FILE = "crawl.log"
MY_JSON_FILE = "ports.json"
EXTENSIONS = {
				'ms_ports.MyJsonExporter.MyJsonExporter': 500,
				}
