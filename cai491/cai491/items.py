# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cai491Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()

class Cai491(scrapy.Item):
    content = scrapy.Field()