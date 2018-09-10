# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class RankTxtline(object):
    def open_spider(self, spider):
        self.file = codecs.open(spider.name + '.txt', 'w', 'utf-8')

    def close_file(self, spider):
        self.file.close()

    def process_item(self, dict, spider):
        type = dict['type']
        items = dict['items']
        line = type
        line += '\r\n'
        self.file.write(line)
        for item in items:
            line = item['rank'] + " " + item['title'] + " " + item['average_big'] + item['average_small'] + " " + \
                   item['link']
            line += '\r\n'
            self.file.write(line)

        return dict


class RankJsonLine(object):
    def open_spider(self, spider):
        self.file = codecs.open(spider.name + '.json', 'w', 'utf-8')

    def close_file(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        items = item["items"]
        line = json.dumps(list(items))
        self.file.write(line + "\n")
        return item
