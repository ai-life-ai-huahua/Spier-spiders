# -*- coding: utf-8 -*-
import scrapy


class Xhs11Spider(scrapy.Spider):
    name = 'xhs11'
    allowed_domains = ['douyin.com']
    start_urls = ['http://douyin.com/']

    def parse(self, response):
        pass
