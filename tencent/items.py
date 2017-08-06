# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    #职位名
    positionname = scrapy.Field()
    #职位链接
    positionlink = scrapy.Field()
    #职位类型
    positiontype = scrapy.Field()
    #招聘人数
    peoplenumber = scrapy.Field()
    #工作地点
    worklocatiom = scrapy.Field()
    #发布时间
    publishtime = scrapy.Field()
