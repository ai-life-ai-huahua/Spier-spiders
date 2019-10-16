# -*- coding: utf-8 -*-
import scrapy
import re
import json
from spider.items import SpiderItem

# class XhsSpider(scrapy.Spider):
#     name = 'xhs'
#     allowed_domains = ['xiaohongshu.com']
#     # start_urls = ['http://xiaohongshu.com/']
#
#     def start_requests(self):
#         self.url  ='https://www.xiaohongshu.com/discovery/item/5cf239c6000000000702a3da'
#         # url = 'http://httpbin.org/ip'
#         yield scrapy.Request(url=self.url,
#
#                              callback=self.parse)
#
#     def parse(self, response):
#         html_doc = response.text
#         print(html_doc)
#         pattern = re.compile(r"<script>window.__INITIAL_SSR_STATE__=(.|\n)*?</script>")

#         indo = pattern.search(html_doc)
#
#         indo = indo.group()
#         print(indo,'-------')
#         data_info = str(indo).split("__INITIAL_SSR_STATE__=")[1].split("</script>")[0]
#         data = json.loads(data_info)
#         print(data)
#         need_infos = data['NoteView']['noteInfo']
#         print(need_infos)




class XhsSpider(scrapy.Spider):
    name = 'xhs'
    allowed_domains = ['xiaohongshu.com']
    # start_urls = ['http://xiaohongshu.com/']
    uid = 2013
    start_urls = 'https://www.xiaohongshu.com/discovery/item/5da1dd650000000001002e5f'

    CatchType = None
    def start_requests(self):
        self.url  ='https://api.cuntubao.com/ctbm/Content/getMaterial'
        # url = 'http://httpbin.org/ip'
        data = {
            # "userId": 0,
            "url": self.start_urls,
            # "appid": "wx6399fcc7164e4844",
            # "version": "1.2.1",
            "token": "bec63b8e508eaa12702a5b38c09c6058"
        }
        yield scrapy.FormRequest(url=self.url,
                            formdata=data,
                             callback=self.parse)

    def parse(self, response):
            item  = SpiderItem()
            datas = json.loads(response.body)
            try:
                # python UCS-4 build的处理方式
                highpoints = re.compile(u'[\U00010000-\U0010ffff]')
            except re.error:
                # python UCS-2 build的处理方式
                highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
            biaoqing = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
            # 去除小红书表情
            remove_xhs_emoji = re.compile(r'\[.*?R]')

            if 'data' in str(response.text):
                data = datas['data']['content']
                img_urls = []
                flag = False
                if data:
                    for u in datas['data']['content']:
                        if u['type'] == 'image':
                            img_urls.append(u['src'])
                        elif u['type'] == 'text':
                            # print('desc', u['content'])
                            titles = u['content'].lstrip('\n').split('\n',1)[0]
                            title_ = highpoints.sub(u'', titles)
                            Description = remove_xhs_emoji.sub(u'', u['content'].split('\n',1)[1])
                            if len(title_) < 10:
                                title = title_ + ",标题太短,爬取时添加,编辑可自行删除"
                            else:
                                title = title_

                            item['uid'] = self.uid
                            # item['Title'] = highpoints.sub(u'', title)

                            item['Description'] = str(Description).replace('\n', '<br />')


                        elif u['type'] == 'video':
                            print('=================')

                            item['type'] = 'video'
                            item['video_image_url'] = u['src']
                            flag = True

                        else:
                            print(response.text)
                    if not flag:
                        item['video_image_url'] = img_urls
                        item['type'] = 'normal'

                    item['PyInfoType'] = 0
                    if self.CatchType == 'url':
                        item['CatchType'] = 0
                    elif self.CatchType == 'auto':
                        item['CatchType'] = 1
                    else:
                        item['CatchType'] = 2

            print('sucess')
            item['Title'] = title
            item['CatchUrl'] = self.start_urls
            print(item['video_image_url'],'~~~~~~~~~~~~~~~~~~~~~~')
            yield item





