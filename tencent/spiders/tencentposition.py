# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencentposition'
    allowed_domains = ['tencent.com']
    url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url+str(offset)]


    def parse(self, response):
        for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            #初始化模型对象
            item = TencentItem()

            # 职位名
            item['positionname'] = each.xpath('./td[1]/a/text()').extract()[0]
            # 职位链接
            item['positionlink'] = each.xpath('./td[1]/a/@href').extract()[0]
            # 职位类型
            positiontype = each.xpath('./td[2]/text()').extract()
            if positiontype:
                item['positiontype'] = positiontype[0]
            else:
                item['positiontype'] = '职位类别'

            # 招聘人数
            item['peoplenumber'] = each.xpath('./td[3]/text()').extract()[0]
            # 工作地点
            item['worklocatiom'] = each.xpath('./td[4]/text()').extract()[0]
            # 发布时间
            item['publishtime'] = each.xpath('./td[5]/text()').extract()[0]

            yield item

        if self.offset < 2140:
            self.offset += 10

        #每次处理完一页后，重新发送下一页页面请求
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
