# -*- coding: utf-8 -*-

# Scrapy settings for english_crawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'english_crawl_2.0'

SPIDER_MODULES = ['english_crawl.spiders']
NEWSPIDER_MODULE = 'english_crawl.spiders'
Max_Line = '你好啊'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'english_crawl (+http://www.jukuu.com)'
FEED_EXPORT_ENCODING = 'utf-8'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True





# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'english_crawl.middlewares.EnglishCrawlSpiderMiddleware': 543,
# }

# USER_AGENT_LIST = [
#     'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
#     'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
#     'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
#     'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
#     'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
#     'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
#     'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
#     'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
# ]
# # 随机生成user agent
# USER_AGENT = random.choice(USER_AGENT_LIST)



# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     'english_crawl.randomAgentMiddleware.MyUserAgentMiddleware': 400,
# }


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'english_crawl.middlewares.EnglishCrawlDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 配置管道优先级，目前只有一个管道,数字越小优先级越高
ITEM_PIPELINES = {
    'english_crawl.pipelines.EnglishCrawlPipeline': 300,
}
# DOWNLOADER_MIDDLEWARES = {
#     'english_crawl.middlewares.UserAgentMiddleware': 300
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
