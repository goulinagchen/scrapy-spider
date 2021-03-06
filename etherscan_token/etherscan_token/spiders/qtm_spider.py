#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2018/1/29 11:59
"""
from scrapy import Request
from scrapy.spider import Spider

from etherscan_token.items import EtherscanTokenItem


class QTMSpider(Spider):
    name = "qtm"  # 0x9a642d6b3368ddc662CA244bAdf32cDA716005BC
    url = "https://etherscan.io/token/generic-tokenholders2?a=0x9a642d6b3368ddc662CA244bAdf32cDA716005BC&s=1E%2b27&p="
    page = 100  # start page
    start_urls = [url + str(page)]

    def parse(self, response):
        for ele in response.xpath("//tr"):
            results = ele.xpath("./td/span/a/text()").extract()
            if len(results) > 0:
                token = results[0]
                item = EtherscanTokenItem()
                item['token'] = token
                yield item

        self.page += 1
        print("request url: %s" % (self.url + str(self.page)))
        yield Request(self.url + str(self.page))
