# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# from spider import settings
#
# p_user = 'root'
# p_password = 'rabbitmq@jszbtb'
# p_host = '192.168.3.17'
# p_port = 5376
# p_v_host = '/'
# p_exchange = 'product'
# p_queue = 'js_queue'
#
# #测试环境
# t_user = 'root'
# t_password = 'rabbitmq@jszbtb'
# t_host = '192.168.1.21'
# t_port = 5376
# t_v_host = '/'
# t_exchange = 'test'
# t_queue = 'hua1'
#
# produce_ = {
#     'user':settings.p_user,
#     'password':settings.p_password,
#     'host':settings.p_host,
#     'port':5672,
#     'v_host':'/',
#     'exchange':settings.p_exchange,
#     'queue':settings.p_queue,
#
# }
#
#
# test_ = {
#     'user':settings.t_user,
#     'password':settings.t_password,
#     'host':settings.t_host,
#     'port':5672,
#     'v_host':'/',
#     'exchange':settings.t_exchange,
#     'queue':settings.t_queue,
#
# }


from spider import settings
import pymysql
import pika

import random
import json
# import MySQLdb
import time


SAVE_PATH = 'D:/statics/Web/Assert/'
RE_PATH = 'D:/statics/'
SER_NAME = 'https://v3f.imacco111.com'
import requests
import os
import requests
import html as Hua
from bs4 import BeautifulSoup
from functools import reduce
import bs4
class SpiderPipeline(object):


        # KeyNO = 'Info00000001'
        # newlist = item['video_image_url']
        # img_list = []
        # img_list1 = []
        # for i in range(len(newlist)):
        #     print("转储图片url： ", i)
        #     img = ''
        #     if (newlist[i].encode("UTF-8") != ''):
        #         ##1 下载图片
        #         print(newlist[i])
        #         # 用当前时间戳＋一个随机数 保证图片名称唯一性
        #         imgpath = str(time.time()) + str(int(random.uniform(10, 20)))
        #         if not os.path.exists(SAVE_PATH + 'InfoWebUrl/' + KeyNO):
        #             print('创建图片文件夹...')
        #             os.makedirs(SAVE_PATH+ 'InfoWebUrl/' + KeyNO)
        #             os.system("chmod -R 777 " + SAVE_PATH + 'InfoWebUrl/' + KeyNO)
        #         newImgPath = SAVE_PATH + 'InfoWebUrl/' + KeyNO + '/' + imgpath + '.jpg'
        #         'Gecko) Chrome/67.0.3396.87 Safari/537.36'
        #
        #     try:
        #         headers = {
        #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like'
        #                           ' Gecko) Chrome/67.0.3396.87 Safari/537.36'
        #         }
        #
        #         response = requests.get(newlist[i], headers=headers, timeout=120)
        #         # 获取的文本实际上是图片的二进制文本
        #         resp = response.content
        #         with open(newImgPath, 'wb') as fp:
        #             fp.write(resp)
        #     except:
        #         print('抓这个路径出错了' + newlist[i], ' : ', 'wrongImg')
        #
        #     saveimgpath = newImgPath.replace(RE_PATH, '')
        #     #  加一个insert uploadImg
        #     ImageUrl = imgpath + '.jpg'  # 图片入库信息
        #     img = img + SER_NAME  + "/" + saveimgpath
        #
        #     # 存单个图片链接
        #     imgurl = '<img src="{}" style="width: 100%; top: 0; left: 0; "/>'.format(img)
        #     img_list.append(imgurl)
        #     img_list1.append(img)
        # # print(img_list1,'imgggggggggggggggggggggggggggggggggggggggggggg')
        # ImageUrls = ''
        # for i in img_list1:
        #     ImageUrls = ImageUrls + i + ','
        #
        # ImageUrls = ImageUrls.rstrip(',')
        # # ImageUrls = html.escape(ImageUrls)
        #
        #
        #
        # Content1 = []
        # for i in item['Description'].split('<br />'):
        #     ele = {"Type": "Text",
        #            "content": Hua.escape(i)}
        #     Content1.append(ele)
        #
        # print('===========')
        # print(ImageUrls)
        #
        #
        # sql = 'update info set Content = "%s"  where KeyNo = "%s"' % (Content1,KeyNO)
        # print('----'*30)
        # print(sql,'+++++++++')
        # print('----'*30)
        # self.cur.execute(sql)
        # self.conn.commit()
        #
        # return item


    def open_spider(self, spider):
        print('start~~~~~~~~~')
        self.f = open('macco.json','w+',encoding='ascii')
        self.conn = pymysql.connect('192.168.1.11','root','Kitche931743','zzh_info')
        self.cur = self.conn.cursor()


    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
        print('ok')


    def process_item(self, item, spider):
        txt = dict(item)
        print(item['type'],'++++++++++++')
        print(item['url'],'-------------------')
        if item['type']:

            a = json.dumps({
            "Tags": "",
            "Title": "",
            "UID":"",
            "Type": 1,
            "Json": {
                "ConverImage": "",
                "Content":list(item['Content']),
                "ImageUrls":item['Imgs']
            },
                "Products": ""
            })
            self.f.write(a)
            keyno = item['url']
            key = keyno.split('WebUrl/')[1].split('/')[0]
            print(key, '--------------')

            sql = 'update info set Content = "%s",Type = "%s",ImageUrls="%s" where KeyNo = "%s"' % (item['Content']
                                                                                     , item['type'],item['Imgs'],key)


            # sql = "update info set Content =
            # '%s' ,Type = '%s' where KeyNo = '%s'" % (item['Content'],item['Type'],keyno)
            print('---' * 30)
            print()
            print('++++', sql, '+++++++++++++++++++++++')
            self.cur.execute(sql)
            self.conn.commit()
        else:
            b =json.dumps({

                "Tags": "",
                "Title": "",
                "UID": "",
                "Type": 0,
                "Json": {
                        "ConverImage":"",
            "Content": item['Content'],
            "Products": ""
            }
            })
            self.f.write(b)
            keyno = item['url']
            key = keyno.split('WebUrl/')[1].split('/')[0]
            print(key,'--------------')

            sql = 'update info set Content = "%s",Type = "%s" where KeyNo = "%s"' % (item['Content']
,item['type'],key)
            print('---'*30)
            print()
            print('++++',sql,'+++++++++++++++++++++++')
            self.cur.execute(sql)
            self.conn.commit()

        return item








    # def open_spider(self, spider):
    #     if not spider.env:
    #         self.env = produce_
    #     else:
    #         self.env = test_
    #     print(self.env)
    #     usr = pika.PlainCredentials(self.env['user'], self.env['password'])
    #     parms = pika.ConnectionParameters(self.env['host'], 5672, virtual_host='/', credentials=usr)
    #     self.connection = pika.BlockingConnection(parms)
    # #
    #
    #
    # def close_spider(self, spider):
    #     print('ok')
    #
    #
    # def process_item(self, item, spider):
    #     print(self.env,'~~~~~~~~~~~~')
    #     item = dict(item)
    #     lines = json.dumps(item, ensure_ascii=False)
    #     exchange = self.env['exchange']
    #     #建立通道
    #     channel = self.connection.channel()
    #     channel.queue_declare(queue=self.env['queue'])
    #     channel.exchange_declare(
    #
    #         exchange,  # 交换机名称
    #         'topic'
    #     )
    #     channel.basic_publish(exchange=exchange,
    #                     routing_key=item['type'],  # 广播模式 这个无所谓了
    #                     body=lines)
    #     print('++++++++++++++++')
    #     channel.close()
    #     return item








