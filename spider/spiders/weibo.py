# -*- coding: utf-8 -*-
import json
import re
import time

import scrapy
# from scrapy_spiders.items import ScrapySpidersItem


class WeiboInfoSpider(scrapy.Spider):
    name = 'weibo_info'
    allowed_domains = ['weibo.cn']

    # start_urls = ['http://weibo.cn/']

    def __init__(self, url=None, uid=None, CatchType=None, *args, **kwargs):
        super(WeiboInfoSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]
        self.uid = uid
        self.CatchType = CatchType

    def parse(self, response):
        html = str(response.text)
        pattern = re.compile(r'render_data =(.*)\[0\] \|\| {};', re.DOTALL)
        info = pattern.search(html).group(1)
        # print(info)
        datas = json.loads(info)
        # 去标题表情
        try:
            # python UCS-4 build的处理方式
            highpoints = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            # python UCS-2 build的处理方式
            highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        biaoqing = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        item = ScrapySpidersItem()
        for data in datas:
            status = data['status']
            # Title = status['status_title']
            Description = ''.join(status['text'])
            if status['pic_ids']:
                pattern2 = re.compile(r'"pid": "(.*?)",', re.DOTALL)
                # video_image_url = pattern2.search(str(info)).group(1)
                image_url = pattern2.findall(str(info))
                item['type'] = 'WeiBo_image'
                # video_image_url = ['https://wx3.sinaimg.cn/large/' + image + '.jpg' for image in status['pic_ids']]
                video_image_url = ['https://wx3.sinaimg.cn/large/' + image + '.jpg' for image in image_url]
            # elif 'media_info' in status['page_info']:
            elif 'page_info' in status and 'media_info' in status['page_info'] and 'stream_url' in status['page_info'][
                'media_info']:
                pattern3 = re.compile(r'"stream_url": "(.*?)",')
                video_image_url = pattern3.search(str(info)).group(1)
                item['type'] = 'WeiBo_video'
                # video_image_url = data['status']['page_info']['media_info']['stream_url']
            else:
                item['type'] = 'WeiBo_image'
                video_image_url = ''

            titles = re.sub('<[^<]+?>', '', Description).replace('\n', '').strip()
            item['uid'] = self.uid
            if len(titles) > 30:
                title = highpoints.sub(u'', titles[:30])
            else:
                title = highpoints.sub(u'', titles)
            item['Title'] = title
            item['Description'] = re.sub('<[^<]+?>', '', Description).replace('\n', '<br />').strip()
            item['video_image_url'] = video_image_url
            item['PyInfoType'] = 2
            if self.CatchType == 'url':
                item['CatchType'] = 0
            elif self.CatchType == 'auto':
                item['CatchType'] = 1
            else:
                item['CatchType'] = 2

            # 转换时间戳函数
            def trans_format(time_string, from_format, to_format='%Y.%m.%d %H:%M:%S'):
                time_struct = time.strptime(time_string, from_format)
                times = time.strftime(to_format, time_struct)
                return times

            # time_string = 'Fri Jun 14 18:03:56 +0800 2019'
            pattern = re.compile(r'''"created_at": "(.*?)",''')
            time_string = pattern.search(response.text).group(1)
            item['release_time'] = trans_format(time_string, '%a %b %d %H:%M:%S %z %Y', '%Y-%m-%d %H:%M:%S')
            item['CatchUrl'] = self.start_urls[0]
            # print(item)
            yield item
