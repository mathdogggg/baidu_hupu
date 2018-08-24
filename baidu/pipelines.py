# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class BaiduPipeline(object):
    def process_item(self, item, spider):
        line = '{}\n'.format(json.dumps(dict(item)))
        self.file.write(line)
        return item
    def open_spider(self,spider):
        self.file = open('buleng_seed.txt','w',encoding='utf-8')
        print('open file')

    def close_spider(self,spider):
        self.file.close()
        print('close file')
