# -*- coding: utf-8 -*-
import scrapy
import bs4
import html
from bs4 import BeautifulSoup
from functools import reduce
from spider.items import SpiderItem
class MaccoSpider(scrapy.Spider):
    name = 'macco'
    allowed_domains = ['file.imacco.com']
    # start_urls = ['http://file.imacco.com/']

    def list_dict_duplicate_removal(self,lst):
        data_list = lst
        run_function = lambda x, y: x if y in x else x + [y]
        return reduce(run_function, [[], ] + data_list)

    def start_requests(self):
        self.f = open('erro.txt','a+',encoding='utf-8')
        with open('weburl.json','r',encoding='utf-8') as f:
            a = f.read()
            url_list = a.split('\n')
            for url in url_list:
                # url = 'http://file.imacco.com/Web/Assert/WebUrl/Info000007756/11dd7c13d1d6fb1de9fbb89888c79ff4.html'

                yield scrapy.Request(url=url,callback=self.parse)

    def transferContent(self, content):
        if content is None:
            return None
        else:
            string = ""
            for c in content:
                if c == '"':
                    string += '\\\"'
                elif c == "'":
                    string += "\\\'"
                elif c == "\\":
                    string += "\\\\"
                else:
                    string += c
            return string

    def parse(self, response):
        # print(response.url)
        item = SpiderItem()
        item['url'] = response.url
        soup = BeautifulSoup(response.text, 'html.parser')
        Content = []
        if not soup.find_all('video') and soup.select('section[id="maccoEditSection"]'):
            try:
                for i in soup:
                    if isinstance(i, bs4.element.Tag):
                        if i.get('id') == 'maccoEditSection':
                            pass

                        elif i.get('id') == 'js_content':  # type=0  要去除title
                            nodes = i.descendants
                            for node in nodes:
                                if node.name == 'img':
                                    img = {"Type": "Image",
                                           "content": node.get('src')}
                                    Content.append(img)
                                elif node.string:
                                    if node.string == '\n' or node.string == '\xa0' or node.string == 'None' or node.string =='&nbsp;':
                                        continue
                                    str = html.escape(node.string)
                                    text = {"Type": "Text",
                                            "content": str}
                                    Content.append(text)

                            item['type'] = 0
                            break

                        elif i.get('id') == 'js_article':  # 不需要去除title
                            nodes = i.descendants
                            print('---------------')
                            for node in nodes:
                                # print(node.name,node,type(node))
                                if isinstance(node,bs4.element.Tag) and node.get('id') == 'js_pc_qr_code':
                                    print('+++++++++')
                                    break
                                if isinstance(node,bs4.element.Tag) and node.get('id') == 'js_preview_reward_author':
                                    print('!!!!!!!!!!!!!!')
                                    break
                                if isinstance(node,bs4.element.Tag) and node.get('id') == 'js_toobar3':
                                    print('!!!!!!!!!!!!!!')
                                    break
                                if node.name == 'img':
                                    img = {"Type": "Image",
                                         "content": node.get('src')}
                                    Content.append(img)
                                elif node.string:
                                    if node.string == '\n' or node.string == '\xa0':
                                        continue
                                    str =node.string
                                    text = {"Type": "Text",
                                            "content": html.escape(str)}
                                    Content.append(text)
                                elif isinstance(node, bs4.element.Tag) and node.get('id') == 'js_sponsor_ad_area':
                                    print(node.name, '~~~~~~~~~~~~~~~~~~~~')
                                    break
                            item['type'] = 0
                            break

                        elif i.get('id') == 'box':  # ppt
                            for node in i.children:
                                if isinstance(node, bs4.element.Tag) and node.get('id') == 'images':
                                    img= ''
                                    for i in node.children:
                                        if i.name == 'img':
                                            img += i.get('src') +','
                                            # Imgs.append(img + ',')
                                elif isinstance(node, bs4.element.Tag) and node.get('id') == 'article':
                                    a = node.strings
                                    for txt in a:
                                        if txt == '\n':
                                            continue
                                        text = {"Type": "Text",
                                                "content": txt}
                                        Content.append(text)
                            item['type'] = 1
                            break
                        else:
                            nodes = i.descendants
                            for node in nodes:
                                print(node.name,type(node),node)
                                if isinstance(node, bs4.element.Tag) and node.name == 'img':
                                    img = {"Type": "Image",
                                           "content": node.get('src')}
                                    Content.append(img)
                                elif isinstance(node, bs4.element.Tag) and node.string:
                                    if node.string == '\n' or node.string == '\xa0':
                                        continue
                                    str = node.string
                                    text = {"Type": "Text",
                                            "content": html.escape(str)}
                                    Content.append(text)
                                elif isinstance(node,bs4.element.NavigableString) and (node != '\n' and node != '\xa0'):
                                    text = {"Type": "Text",
                                            "content": html.escape(node)}
                                    Content.append(text)

                            item['type'] = 0

                Content1 = (self.list_dict_duplicate_removal(Content))
                # print(Content1[:10])
                item['Content'] = Content1
                if item['type']:
                    item['Imgs']  = img.rstrip(',')
                else:
                    pass

                yield item
            except Exception as e:
                print(e,'--')

                print(response.url)


        else:
            self.f.write(response.url + '\n')
            print('没有macco的url：'+response.url)


