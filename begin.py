# -*- coding: utf-8 -*-

from scrapy import cmdline

cmdline.execute("scrapy crawl subspider -o data.json".split())
