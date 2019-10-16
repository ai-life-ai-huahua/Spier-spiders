# -*- coding: utf-8 -*-
import scrapy
import json
import re
import requests
from spider.items import SpiderItem
import datetime
class JigouSpider(scrapy.Spider):
    name = 'jigou'
    allowed_domains = ['jsggzy.jszwfw.gov.cn']
    def __init__(self,i=0,env=None,*args,**kwargs):
        super(JigouSpider,self).__init__(*args,**kwargs)
        self.i = i
        self.env = env

    def start_requests(self):
            #板块每一页的url
            url = 'http://jsggzy.jszwfw.gov.cn/EpointWebBuilder_jsggzy/dataWebAction.action?cmd=getDataList&categoryNum=004001002&projectName=&projectCode=&pageSize=15&pageIndex={}'.format(self.i)
            print(url,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if json.loads(json.loads(response.body.decode('utf-8'))['custom'])['Table']:
            print('++++++++++')
            for d in json.loads(json.loads(response.body.decode('utf-8'))['custom'])['Table']:
                url1 = 'http://jsggzy.jszwfw.gov.cn/EpointWebBuilder_jsggzy/dataWebAction.action?cmd=getDetail&rowguid={}&categorynum=4001002'.format(d['rowguid'])
                print(url1,'~~~~~~~~~~~~~',self.i)
                res = requests.get(url=url1)
                #从res里解析需要的字段
                str = (json.loads(res.content.decode('utf-8'))['custom'])
                item = SpiderItem()
                res = re.search('"LEGAL_CODE":".*?"', str)
                item['legalCode'] = res.group().split(':')[1].replace('"', '')


                res = re.search('"LEGAL_REPRESENT":".*?"', str)
                item['legalRepresent'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"REGISTER_PROVINCE":".*?"', str)
                item['registerProvince'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"REGISTER_CITY":".*?"', str)
                item['registerCity'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_TYPE":".*?"', str)
                item['legalType'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_UNIT_ADDRESS":".*?"', str)
                item['legalUnitAddress'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"REG_CAPITAL":".*?"', str)
                item['regCapital'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"REG_UNIT":".*?"', str)
                item['regUnit'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"REG_CAP_CURRENCY":".*?"', str)
                item['regCapCurrency'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_CONTACT_PHONE":".*?"', str)
                item['legalContactPhone'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_EMAIL":".*?"', str)
                item['legalEmail'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"ATTACHMENT_SET_CODE":".*?"', str)
                item['attachmentSetCode'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"BASIC_ACCOUNT_NAME":".*?"', str)
                item['basicAccountName'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"BASIC_ACCOUNT_NO":".*?"', str)
                item['basicAccountNo'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"BASIC_BANK":".*?"', str)
                item['basicBank'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"BASIC_BRANCH_BANK":".*?"', str)
                item['basicBranchBank'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"BIDDER_CODE_TYPE":".*?"', str)
                item['bidderCodeType'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"CREDIT_RATE":".*?"', str)
                item['creditRate'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_CONTACT_ADDRESS":".*?"', str)
                item['legalContactAddress'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_INDUSTRY":".*?"', str)
                item['legalIndustry'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_NAME":".*?"', str)
                item['legalName'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_ROLE":".*?"', str)
                item['legalRole'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_STATUS":".*?"', str)
                item['legalStatus'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_WEB":".*?"', str)
                item['legalWeb'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LEGAL_ZIP_CODE":".*?"', str)
                item['legalZipCode'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"LICENSE_NO":".*?"', str)
                item['licenseNo'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"DATA_TIMESTAMP":{.*?}', str)
                if res == None:
                    item['licenseEndDate'] = 'null'
                else:
                    try:
                        date = json.loads(res.group().split(':', 1)[1])
                        if (date['time']) > 9999999999999:
                            timeStamp = int(date['time']) // 10000
                        elif date['time'] < 0:
                            raise ImportError
                        else:
                            timeStamp = int(date['time']) // 1000
                        dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                        item['dataTimestamp'] = otherStyleTime
                    except:
                        otherStyleTime = 'null'
                        item['dataTimestamp'] = otherStyleTime


                res = re.search('"LICENSE_END_DATE":{.*?}', str)
                if res == None:
                    item['licenseEndDate'] = 'null'
                else:
                    try:
                        date = json.loads(res.group().split(':', 1)[1])
                        if (date['time']) > 9999999999999:
                            timeStamp = int(date['time']) // 10000
                        elif date['time'] < 0:
                            raise ImportError
                        else:
                            timeStamp = int(date['time']) // 1000
                        dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                        item['licenseEndDate'] = otherStyleTime
                    except:
                        otherStyleTime = 'null'
                        item['licenseEndDate'] = otherStyleTime

                res = re.search('"LOCAL_TAX_CERT_END_DATE":{.*?}', str)
                if res:
                    date = json.loads(res.group().split(':', 1)[1])
                    try:
                        if (date['time']) > 9999999999999:
                            timeStamp = int(date['time']) // 10000
                        elif date['time'] < 0:
                            raise ImportError
                        else:
                            timeStamp = int(date['time']) // 1000

                        dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                        item['localTaxCertEndDate'] = otherStyleTime
                    except:
                        otherStyleTime = 'null'
                        item['licenseEndDate'] = otherStyleTime
                else:
                    item['licenseEndDate'] = 'null'

                res = re.search('"LOCAL_TAX_CERT_NO":".*?"', str)
                item['localTaxCertNo'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"ORGAN_CERT_END_DATE":.*?,', str)
                if res:
                    try:
                        if res.group().split(':', 1)[1] == 'null':
                            date = json.loads(res.group().split(':', 1)[1])
                            if (date['time']) > 9999999999999:
                                timeStamp = int(date['time']) // 10000
                            elif date['time'] < 0:
                                raise ImportError
                            else:
                                timeStamp = int(date['time']) // 1000
                            dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                            otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                            item['organCertEndDate'] = otherStyleTime
                        else:
                            item['organCertEndDate'] = 'null'
                    except:
                        item['organCertEndDate'] = 'null'
                else:
                    item['organCertEndDate'] = 'null'

                res = re.search('"TAX_CERT_END_DATE":{.*?}', str)
                if res:
                    try:
                        date = json.loads(res.group().split(':', 1)[1])
                        if (date['time']) > 9999999999999:
                            timeStamp = int(date['time']) // 10000
                        elif date['time'] < 0:
                            raise ImportError
                        else:
                            timeStamp = int(date['time']) // 1000
                        dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                        item['taxCertEndDate'] = otherStyleTime
                    except:
                        item['taxCertEndDate'] = 'null'
                else:
                    item['taxCertEndDate'] = 'null'

                res = re.search('"ORGAN_NO":".*?"', str)
                item['organNo'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"PLATFORM_CODE":".*?"', str)
                item['platfromCode'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"PUB_SERVICE_PLAT_CODE":".*?"', str)
                item['pubServicePlatCode'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"REGION_CODE":".*?"', str)
                item['regionCode'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"rowguid":".*?"', str)
                item['rowguid'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"REPRESENT_PHONE":".*?"', str)
                item['representPhone'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"TAX_CERT_NO":".*?"', str)
                item['taxCertNo'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"danWeiGuid":".*?"', str)
                item['danWeiGuid'] = res.group().split(':')[1].replace('"', '')

                res = re.search('"danWeiType":".*?"', str)
                item['danWeiType'] = res.group().split(':')[1].replace('"', '')
                item['type'] = 'tenderagency'

                yield item
            self.i += 1
            url = 'http://jsggzy.jszwfw.gov.cn/EpointWebBuilder_jsggzy/dataWebAction.action?cmd=getDataList&categoryNum=004001002&projectName=&projectCode=&pageSize=15&pageIndex={}'.format(self.i)
            yield scrapy.Request(url=url, callback=self.parse)
        else:
            self.crawler.engine.close_spider(self, '没有新的文章，关闭爬虫')