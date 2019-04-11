# -*- coding: utf-8 -*-

from scrapy import cmdline

# cmdline.execute("scrapy crawl subspider -o data.json".split())
cmdline.execute("scrapy crawl ebookspider -o ebookspider.json -s FEED_EXPORT_ENCODING=UTF-8".split())
