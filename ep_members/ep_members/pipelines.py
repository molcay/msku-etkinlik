# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EpMembersPipeline(object):
    def process_item(self, item, spider):
        email = item["email"]
        to_replace = [("mailto:", ""), ("[dot]", "."), ("[at]", "@")]
        for word1, word2 in to_replace:
            email = email.replace(word1, word2)
        # email = email.replace("mailto:", "")
        # email = email.replace("[dot]", ".")
        # email = email.replace("[at]", "@")
        email = email[::-1]  
        item["email"] = email      
        return item

import json
import codecs

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open('items.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()