# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class RO321Item(scrapy.Item):
    name = scrapy.Field()
    id = scrapy.Field()
    type = scrapy.Field()
    series = scrapy.Field()
    buy_price = scrapy.Field()
    sell_price = scrapy.Field()
    weight = scrapy.Field()
    description = scrapy.Field()
    script = scrapy.Field()
    loot = scrapy.Field()
    other_loot = scrapy.Field()
