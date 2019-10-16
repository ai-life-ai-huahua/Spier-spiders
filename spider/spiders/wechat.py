
# -*- coding: utf-8 -*-
import datetime
import re
import pytz
import scrapy
from spider.items import SpiderItem
from bs4 import BeautifulSoup
import bs4
import html
from functools import reduce

class WechatSpider(scrapy.Spider):
    name = 'wechat'
    allowed_domains = ['mp.weixin.qq.com']
    # start_urls = ['http://mp.weixin.qq.com/']

    # start_urls = ['http://mp.weixin.qq.com/']



        # super(WechatInfoSpider, self).__init__(*args, **kwargs)
    start_urls = ['https://mp.weixin.qq.com/s/ZdpRg0ORt_H5iEuVcqCnmw']
    uid = 231
    CatchType = None


    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        item = SpiderItem()
        item['html'] = response

        # Content = self.list_dict_duplicate_removal(Content)
        item['keyno'] = 'Info000025952'


        # item['uid'] = self.uid
        # title = response.xpath('//h2/text()').extract()
        # print(title)
        # item['type'] = 'WeChat'
        # item['Title'] = (''.join(title)).replace('\n', '').replace('"', '').lstrip(' ').rstrip(' ').replace("'",
        #                                                                                                     '').replace(
        #     '"', '')
        # # item['Title'] = remove_emoji.format_str(str(title))
        # div_list = response.xpath('//div[@id="js_content"]')
        #





        # item['PyInfoType'] = 1
        # if self.CatchType == 'url':
        #     item['CatchType'] = 0
        # elif self.CatchType == 'auto':
        #     item['CatchType'] = 1
        # else:
        #     item['CatchType'] = 2
        # for div in div_list:
        #
        #     item['video_image_url'] = div.xpath('.//img/@data-src').extract()

        # # 指定时区为上海的时间格式转换
        # dateArray = datetime.datetime.fromtimestamp(int(timeStamp)).astimezone(pytz.timezone("Asia/Shanghai"))
        # item['release_time'] = dateArray.strftime("%Y--%m--%d %H:%M:%S")
        # item['CatchUrl'] = self.start_urls[0]


        # Content = []
        # print(soup)
        # for i in soup:
        #     if isinstance(i, bs4.element.Tag):
        #         if i.get('id') == 'js_article':  # 不需要去除title
        #             nodes = i.descendants
        #             print('---------------')
        #             for node in nodes:
        #                 # print(node.name,node,type(node))
        #                 if isinstance(node, bs4.element.Tag) and node.get('id') == 'js_pc_qr_code':
        #                     print('+++++++++')
        #                     break
        #                 if isinstance(node, bs4.element.Tag) and node.get('id') == 'js_preview_reward_author':
        #                     print('!!!!!!!!!!!!!!')
        #                     break
        #                 if isinstance(node, bs4.element.Tag) and node.get('id') == 'js_toobar3':
        #                     print('!!!!!!!!!!!!!!')
        #                     break
        #                 if node.name == 'img':
        #                     img = {"Type": "Image",
        #                            "content": node.get('src')}
        #                     Content.append(img)
        #                 elif node.string:
        #                     if node.string == '\n' or node.string == '\xa0':
        #                         continue
        #                     str = node.string
        #                     text = {"Type": "Text",
        #                             "content": html.escape(str)}
        #                     Content.append(text)
        #                 elif isinstance(node, bs4.element.Tag) and node.get('id') == 'js_sponsor_ad_area':
        #                     print(node.name, '~~~~~~~~~~~~~~~~~~~~')
        #                     break
        #             break
        # item['Content'] = Content

        yield item
