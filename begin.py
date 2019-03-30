# -*- coding: utf-8 -*-
from scrapy import cmdline

cmdline.execute("scrapy crawl images -o images.json".split())

