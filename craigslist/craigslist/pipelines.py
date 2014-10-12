# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from psycopg2._psycopg import IntegrityError


class CraigslistPipeline(object):
    def process_item(self, item, spider):
        try:
            item.save()
            return item
        except IntegrityError, e:
            spider.log(str(e))
            return None
