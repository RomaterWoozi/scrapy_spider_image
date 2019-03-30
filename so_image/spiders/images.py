# -*- coding: utf-8 -*-
import scrapy
import json
from so_image.items import SoImageItem

"""
带有 yield 的函数在 Python 中被称之为 generator（生成器）
"""


class ImagesSpider(scrapy.Spider):
    BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
    name = 'images'
    start_index = 0
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/zj?ch=art&sn=0&listtype=new&temp=1']
    MAX_DOWNLOAD_NUM = 600

    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        # images = SoImagesItem()
        image_lists = []

        # iter_temp=iter(infos);
        if infos['list'] is not None:
            for info in infos['list']:
                image_lists.append(info['qhimg_url'])
        else:
            self.start_index += 1

        image_urls = {'image_urls': image_lists}
        # yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}
        if self.start_index == 600:
            print("")
        yield image_urls
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield scrapy.Request(self.BASE_URL % self.start_index)
        pass
