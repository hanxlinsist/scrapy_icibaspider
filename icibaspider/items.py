# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IcibaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    en = scrapy.Field()
    cn = scrapy.Field()
    url = scrapy.Field()

    pass
