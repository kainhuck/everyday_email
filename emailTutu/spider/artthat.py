import requests
import random

from mytools.UserAgent import makeAgent
from lxml import etree

url = "http://www.artthat.net/category/newcollectors/arts/page/" + str(random.randint(1, 44)) + "/"

article_xpath = '//div[@class="grids masonry-layout entries"]/article'
article_xpath_2 = '//div[@class="grids masonry-layout entries masonry"]/article'

r = requests.get(url, headers=makeAgent())
r.encoding = r.apparent_encoding

html = etree.HTML(r.text)
num = "[" + str(random.randint(1, 10)) + "]"
xpath = article_xpath + num

article = html.xpath(xpath)
if len(article) == 0:
    article = html.xpath(article_xpath_2 + num)

pic = article[0].xpath("./figure/a/img/@src")
link = article[0].xpath("./figure/a/@href")
title = article[0].xpath("./header/h2/a/text()")
summary = article[0].xpath("./div/p/text()")


# print(pic[0])
# print(link[0])
# print(title[0])


def get_art_pic():
    return '''
        <b>%s</b><br>
        <img alt="艺术图片" src="%s"><br>
        <i>简介</i><br>
        <p>%s</p>
        <a href="%s">链接</a>
    ''' % (title[0], pic[0], summary[0], link[0])
