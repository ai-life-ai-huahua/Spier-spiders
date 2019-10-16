# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import bs4

class GuideSpider(scrapy.Spider):
    name = 'guide'
    allowed_domains = ['china.guidechem.com']

    def  start_requests(self):
        url = 'https://china.guidechem.com/datacenter/hzp-a-p1.html'
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        print(response.text[100:500])
        print('____________')
        dom = BeautifulSoup(response.text, 'html.parser')
        div = dom.select('div[class="e_tics_bot"]')[0]
        print(div.name)
        for node in div.descendants:
            if isinstance(node,bs4.element.Tag) and node.name == 'a' :
                print(node.get('href'),node.string)
                url1 = 'https://china.guidechem.com/datacenter/{}'.format(node.get('href'))
                yield scrapy.Request(url=url1,callback=self.parse1)


    def parse1(self,response):
        print('+++++++++++++++++++',response.url)



