# -*- coding: utf-8 -*-
import scrapy
import requests
import re
import json
import datetime
from spider.items import SpiderItem


class GongyingshangSpider(scrapy.Spider):
    name = 'gongyingshang'
    allowed_domains = ['jsggzy.jszwfw.gov.cn']
    # start_urls = ['http://http://jsggzy.jszwfw.gov.cn/']

    def start_requests(self):
        for i in range(710):

            url = 'http://jsggzy.jszwfw.gov.cn/EpointWebBuilder_jsggzy/dataWebAction.action?cmd=getDataList&categoryNum=004001006&projectName=&projectCode=&pageSize=15&pageIndex={}'.format(
                i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for d in json.loads(json.loads(response.body.decode('utf-8'))['custom'])['Table']:
            url1 = 'http://jsggzy.jszwfw.gov.cn/EpointWebBuilder_jsggzy/dataWebAction.action?cmd=getDetail&rowguid={}&categorynum=4001006'.format(
                d['rowguid'])
            res = requests.get(url=url1)

            str = (json.loads(res.content.decode('utf-8'))['custom'])

            item = SpiderItem()
            res = re.search('"LEGAL_CODE":".*?"', str)
            # print(res.group().split(':')[1].replace('"',''))
            item['legalCode'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"LEGAL_REPRESENT":".*?"', str)
            # print(res.group().split(':')[1].replace('"',''))
            item['legalRepresent'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"REGISTER_PROVINCE":".*?"', str)
            # print(res.group().split(':')[1].replace('"',''))
            item['registerProvince'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"REGISTER_CITY":".*?"', str)
            # print(res.group().split(':')[1].replace('"',''))
            item['registerCity'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"LEGAL_TYPE":".*?"', str)
            # print(res.group().split(':')[1].replace('"',''))
            item['legalType'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"LEGAL_UNIT_ADDRESS":".*?"', str)
            # print(res.group().split(':')[1].replace('"',''))
            item['legalUnitAddress'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"REG_CAPITAL":".*?"', str)
            # print(res.group().split(':')[1].replace('"',''))
            item['regCapital'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"REG_UNIT":".*?"', str)
            # print(res.group().split(':')[1].replace('"',''))
            item['regUnit'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"REG_CAP_CURRENCY":".*?"', str)
            # print(res.group().split(':')[1].replace('"',''))
            item['regCapCurrency'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"LEGAL_CONTACT_PHONE":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['legalContactPhone'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"LEGAL_EMAIL":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['legalEmail'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"ATTACHMENT_SET_CODE":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['attachmentSetCode'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"BASIC_ACCOUNT_NAME":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['basicAccountName'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"BASIC_ACCOUNT_NO":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['basicAccountNo'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"BASIC_BANK":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['basicBank'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"BASIC_BRANCH_BANK":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['basicBranchBank'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"BIDDER_CODE_TYPE":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['bidderCodeType'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"CREDIT_RATE":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['creditRate'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"LEGAL_CONTACT_ADDRESS":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['legalContactAddress'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"LEGAL_INDUSTRY":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['legalIndustry'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"LEGAL_NAME":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['legalName'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"LEGAL_ROLE":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
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
            date = json.loads(res.group().split(':', 1)[1])

            timeStamp = int(date['time']) // 1000


            dateArray = datetime.datetime.utcfromtimestamp(timeStamp)

            otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")

            item['dataTimestamp'] = otherStyleTime

            res = re.search('"LICENSE_END_DATE":{.*?}', str)
            if res == None:
                item['licenseEndDate'] = 'null'

            else:
                try:
                    date = json.loads(res.group().split(':', 1)[1])
                    if len(str(date['time'])) > 13:
                        timeStamp = int(date['time']) // 10000
                    else:
                        timeStamp = int(date['time']) // 1000

                    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                    item['licenseEndDate'] = otherStyleTime
                except:
                    otherStyleTime = 'null'
                    item['licenseEndDate'] = otherStyleTime
            print(str,'+++++++++++++')
            res = re.search('"LOCAL_TAX_CERT_END_DATE":{.*?}', str)
            print(res,'---------------------')
            if res:
                date = json.loads(res.group().split(':', 1)[1])
                try:
                    if len(str(date['time'])) > 13:
                        timeStamp = int(date['time']) // 10000
                    else:
                        timeStamp = int(date['time']) // 1000

                    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                    item['localTaxCertEndDate'] = otherStyleTime
                except:
                    otherStyleTime = 'null'
                    item['licenseEndDate'] = otherStyleTime
            else:
                print('~~~~~~~~~~~~~~~')
                item['licenseEndDate'] = 'null'




            res = re.search('"LOCAL_TAX_CERT_NO":".*?"', str)

            item['localTaxCertNo'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"ORGAN_CERT_END_DATE":.*?,', str)
            print(res, '~~~~~~~~~~~~')
            if res:

                if res.group().split(':', 1)[1] == 'null':
                    date = json.loads(res.group().split(':', 1)[1])

                    # print(date['time'])
                    if (date['time']) > 9999999999999:
                        timeStamp = int(date['time']) // 10000
                    else:
                        timeStamp = int(date['time']) // 1000
                    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
                    # print(otherStyleTime, '~~~~~~')
                    item['organCertEndDate'] = otherStyleTime
                else:
                    item['organCertEndDate'] ='null'

            else:
                item['organCertEndDate'] = 'null'
            # print(res.group().split(':')[1].split(',')[0])



            res = re.search('"TAX_CERT_END_DATE":{.*?}', str)
            print(res,'~~~~~~~~~~~~')
            if res:

                date = json.loads(res.group().split(':', 1)[1])




            # print(date['time'])
                if (date['time']) > 9999999999999:
                    timeStamp = int(date['time']) // 10000
                else:
                    timeStamp = int(date['time']) // 1000
                dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
                otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
            # print(otherStyleTime, '~~~~~~')
                item['taxCertEndDate'] = otherStyleTime
            else:
                item['taxCertEndDate'] = 'null'

            res = re.search('"ORGAN_NO":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['organNo'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"PLATFORM_CODE":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['platfromCode'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"PUB_SERVICE_PLAT_CODE":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['pubServicePlatCode'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"REGION_CODE":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['regionCode'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"rowguid":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['rowguid'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"REPRESENT_PHONE":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['representPhone'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"TAX_CERT_NO":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['taxCertNo'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"danWeiGuid":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['danWeiGuid'] = res.group().split(':')[1].replace('"', '')

            res = re.search('"danWeiType":".*?"', str)
            # print(res.group().split(':')[1].replace('"', ''))
            item['danWeiType'] = res.group().split(':')[1].replace('"', '')
            item['type'] = 'suplier'

            print('--------------------')
            yield item


