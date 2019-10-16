# -*- coding: utf-8 -*-
import scrapy
import json
import requests
import lxml.html
import re
etree = lxml.html.etree
from spider.items import SpiderItem

class XinyongSpider(scrapy.Spider):
    name = 'xinyong'
    # allowed_domains = ['http://jsggzy.jszwfw.gov.cn']
    # start_urls = ['http://http://jsggzy.jszwfw.gov.cn/']
    allowed_domains = ['xiaohongshu.com']



    def start_requests(self):
        url = 'http://jsggzy.jszwfw.gov.cn/xyxx/creditInfo.html'
        # for i in range(1,23):
        #     if i == 1:
        #         url = 'http://jsggzy.jszwfw.gov.cn/xyxx/creditInfo.html'
        #     elif i <=10:
        #         url = 'http://jsggzy.jszwfw.gov.cn/xyxx/{}.html'.format(
        #         i)
        #     else:
        #         url = 'http://jsggzy.jszwfw.gov.cn/xyxx/creditInfo.html?categoryNum=005&pageIndex={}'.format(i)

        yield scrapy.Request(url=url, callback=self.parse)

    def tdTostr(self,str1):
        txt = str1.split('\n')
        print(txt)
        lst = (list(filter(lambda x: x and x.strip(), txt)))
        for i in lst:
            print(i.lstrip(' ').strip(' '))

    def parse(self, response):
        text = response.text
        dom = etree.HTML(text)
        print(type(dom))
        articles = dom.xpath('//*[@id="main"]/table/tbody/tr')
        print(len(articles))
        item =  SpiderItem()
        for i in articles:
            title = i.xpath('td[2]/a/text()')[0].lstrip()
            # print(title)

            url = i.xpath('td[2]/a/@href')[0]
            if url.startswith('http'):
                res = requests.get(url)
                text = res.content.decode('utf-8')
                print(url)
                # print(text)
                dom = etree.HTML(text)
                title = dom.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/h1/text()')[0]

                a  =title.encode('utf-8').decode('utf-8')
                print(a.lstrip('\n').rstrip('\n').strip(' '))
                pulishtime = dom.xpath('/html/body/div[2]/div[2]/div[2]/div[2]/span/text()')[0]
                a1 = pulishtime.encode('utf-8').decode('utf-8')
                print(a.lstrip('\n').rstrip('\n').strip(' '),'!!')
                txt = dom.xpath("string(/html/body/div[2]/div[2]/div[2]/div[3]/div/div)")
                node = txt.encode('utf-8').decode('utf-8')
                print(node.split(' A{line-height:1;font-family:宋体;font-size:12pt;}')[1])
                item['publishTime'] = a1
                item['title'] = a
                item['article'] = node.split(' A{line-height:1;font-family:宋体;font-size:12pt;}')[1]
                item['type'] = 'other url'
            else:
                url = 'http://jsggzy.jszwfw.gov.cn/' +url
                res = requests.get(url)
                text = res.text
                dom = etree.HTML(text)
                title  =dom.xpath('/html/body/div[2]/div/div[2]/div/div[1]/h1/text()')[0]

                print(title.encode('utf-8').decode('utf-8'))
                print('----------------------------------------------------------------')
                plishtime = dom.xpath('/html/body/div[2]/div/div[2]/div/div[1]/p/span[1]/text()')[0]
                str1 = plishtime.encode('utf-8').decode('utf-8')
                date = re.search('信息发布时间.*-..-.. ..:..:..', str1)
                print(date.group(), 'date')
                date = date.group().split('信息发布时间：')[1]
                print('----------------------------------------------------------')
                # desc = dom.xpath('string(/html/body/div[2]/div/div[2]/div/div[1]/div[1])')


                td  = dom.xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[1]/table/tbody')
                if td:
                    print('解析表格','------------------')
                    # tr = dom.xpath('string(/html/body/div[2]/div/div[2]/div/div[1]/div[1])')
                    trs = dom.xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[1]/table/tbody/tr')
                    print(len(trs))
                    lst = []
                    for n in trs:
                        if n.xpath('td[2]//text()'):
                            a = (n.xpath('td[2]//text()')[0])
                        else:
                            a = ('')
                        lst.append(a)
                    print(lst)
                    item['articledministrativePenaltyDecisionNo'] = lst[0]
                    item['nameOfPenalty'] = lst[1]
                    item['theCauseOfThePunishment'] = lst[2]
                    item['typesOfPenalties'] = lst[3]
                    item['theBasisOfThePenalty'] = lst[4]
                    item['nameOfAdministrativeCounterpart'] = lst[5]
                    item['unifiedSocialCreditCode'] = lst[6]
                    item['organizationCode'] = lst[7]
                    item['businessRegistrationCode'] = lst[8]
                    item['taxRegistrationNumber'] = lst[9]
                    item['residentIDNumber'] = lst[10]
                    item['nameOfLegalRepresentative'] = lst[11]
                    item['resultsOfPenalties'] = lst[12]
                    item['penaltyDecisionDate'] = lst[13]
                    item['publicityDeadline'] = lst[14]
                    item['penaltyOrgans'] = lst[15]
                    item['currentState'] = lst[16]
                    item['localCoding'] = lst[17]
                    item['dataUpdateTimestamp'] = lst[18]
                    item['type'] = 'td'

                    # print(url)
                    # str1 = tr.encode('utf-8').decode('utf-8')

                else:
                    if dom.xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[1]/p'):
                        txt = dom.xpath('string(/html/body/div[2]/div/div[2]/div/div[1]/div[1])')
                        print(url)
                        print('解析文本')
                        print(type(txt.encode('utf-8').decode('utf-8')))
                        item['article'] =txt.encode('utf-8').decode('utf-8')
                        item['publishTime'] = date
                        item['title'] = title
                        item['type'] = 'txt'

                    else:
                        print(url)
                        print('空白页面')
            yield item





