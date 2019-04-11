# -*- coding: utf-8 -*-
import pymongo

from scrapy import cmdline

if __name__ == '__main__':
    # cmdline.execute("scrapy crawl subspider -o data.json".split())
    cmdline.execute("scrapy crawl meizitu -o meizitu.json -s FEED_EXPORT_ENCODING=UTF-8".split())
