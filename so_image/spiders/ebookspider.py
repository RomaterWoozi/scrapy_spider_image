# -*- coding: utf-8 -*-
import scrapy

from so_image.items import SoImageItem


class EbookspiderSpider(scrapy.Spider):
    name = 'ebookspider'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['http://www.mzitu.com/all']

    def parse(self, response):
        # self.log(response.body.decode("utf-8"))
        ebook_item = SoImageItem()
        item = {}
        data = []
        for earch in response.xpath("//ul[@class='archives']"):
            print((earch.xpath("./preceding::*[1]/text()").extract()[0]))
            item['year'] = " %s" % (earch.xpath("./preceding::*[1]/text()").extract()[0])
            alink_list = []
            for liitem in earch.xpath("./li"):
                pList = []
                for ptemp in liitem.xpath("./p[@class='url']/a"):
                    pdata = {'name': ptemp.xpath("./text()").extract()[0], 'alink': ptemp.xpath("./@href").extract()[0]}
                    pList.append(pdata)
                temp = {'month': liitem.xpath("./p[@class='month']/em/text()").extract()[0], 'columns': pList}
                alink_list.append(temp)
            item['alink_list'] = alink_list
            data.append(item)
        ebook_item['data_list'] = data
        yield ebook_item
        pass
