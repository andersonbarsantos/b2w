# -*- coding: utf-8 -*-
import json

class B2WJsonWriterPipeline(object):   
    def open_spider(self, spider):
        self.file = open('produto.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) 
        self.file.write(line)
        return item