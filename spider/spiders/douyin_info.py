
# -*- coding: utf-8 -*-
import json
import re
import time
import scrapy
from bs4 import BeautifulSoup
from lxml import html

etree = html.etree
a = etree.HTMLParser()
with open('weburl.json', 'r') as f:
    a = (f.read())
    url_list = a.split('\n')
# print(url_list)
from spider.items import SpiderItem
class DouyinInfoSpider(scrapy.Spider):
    name = 'douyin_info'
    allowed_domains = ['file.imacco.com']
    # start_urls = ['http://douyin.com/']
    def start_requests(self):
        for url in url_list:
            print(url,'++++++++++')
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        '''  "Tags": "1,2,3,4 ",
            "Title": "a new test",
            "UID": 2381,
            "Type": 1
            "Json": {
                "ConverImage": {
                    "ImageUrl": "http://imgv4f.5imakeup.com/Web/Assert/InfoWebUrl/Info000017150/1563283868.846175210.jpg",
                    "Width": 50,
                    "Height": 100
                },
            "Content": "skjowjnksjdjkasnmbgf",  +
            "ImageUrls": "url1,url2",  +
            "Products": 223, 135
        }'''
        print(response.url)
        print('~~~~~~~~~')
        dom = etree.HTML(response.text)
        print(dom)

        # section = dom.xpath('//body/section[@id="maccoEditSection"]')
        # print(section)
        # if section:
        #     images = dom.xpath('//div[@id="images"]/img/@src')
        #     print(images)
        # else:
        #     print(response.url,'++++++++++++++++')
























 # html_doc = response.text
        # pattern_desc = re.compile(r'''<p class="desc">(.*?)</p>''')
        # pattern_url = re.compile(r'''playAddr: "(.*?)",''')
        # Description = pattern_desc.search(html_doc).group(1)
        # video_image_url = pattern_url.search(html_doc).group(1)
        # # print(video_image_url)
        # # 去标题表情
        # try:
        #     # python UCS-4 build的处理方式
        #     highpoints = re.compile(u'[\U00010000-\U0010ffff]')
        # except re.error:
        #     # python UCS-2 build的处理方式
        #     highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        # biaoqing = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        # item = SpiderItem()
        # item['type'] = 'DouYin_video'
        # item['uid'] = self.uid
        # if len(Description) > 30:
        #     title = highpoints.sub(u'', Description[:30])
        # elif not Description:
        #     title = '该抖音视频无标题'
        # else:
        #     title = highpoints.sub(u'', Description)
        # item['Title'] = title
        # item['Description'] = Description
        #
        # item['video_image_url'] = run.other_remove_watermark(self.start_urls)
        # # item['video_image_url'] = video_image_url
        # item['PyInfoType'] = 3
        # if self.CatchType == 'url':
        #     item['CatchType'] = 0
        # elif self.CatchType == 'auto':
        #     item['CatchType'] = 1
        # else:
        #     item['CatchType'] = 2
        # item['release_time'] = ''
        # item['CatchUrl'] = self.start_urls[0]
        #
        # # print(item)
        # yield item