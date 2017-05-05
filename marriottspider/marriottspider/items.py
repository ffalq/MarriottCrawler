# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MarriottspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field
    score = scrapy.Field
    url = scrapy.Field
    address = scrapy.Field
    phone = scrapy.Field
    numberratings = scrapy.Field()
