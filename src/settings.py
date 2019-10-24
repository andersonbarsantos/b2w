# -*- coding: utf-8 -*-

BOT_NAME = 'src'

SPIDER_MODULES = ['src.spiders']
NEWSPIDER_MODULE = 'src.spiders'

ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 4
DOWNLOAD_TIMEOUT = 5

ITEM_PIPELINES = {
    'src.pipelines.B2WJsonWriterPipeline': 800
}