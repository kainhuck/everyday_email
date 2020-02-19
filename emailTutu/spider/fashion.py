import time

import requests
from lxml import etree
from mytools.UserAgent import makeAgent
from utils.getTime import get_today

url = "http://www.ladymax.cn/"

news = []
today = get_today()
news_flag = True
ret_list = []


def _init():
    global news
    r = requests.get(url, headers=makeAgent())
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    news = html.xpath('//div[@id="list"]/div[@class="i"]')
    if not len(news):
        _init()
        time.sleep(1)
    else:
        return


_init()

if today != news[0].xpath('./a[2]/i/span/text()')[0].split(" ")[0]:
    news_flag = False
    today = news[0].xpath('./a[2]/i/span/text()')[0].split(" ")[0]

for each in news:
    date = each.xpath('./a[2]/i/span/text()')[0].split(" ")[0]
    if date == today:
        content = '''
            <li>
              <div class="img"><img src="%s"></div>
              <div class="info">
                <i>%s</i>
                <a href="%s" style="color: brown;">%s</a>
              </div>
            </li>
        ''' % (each.xpath('./a[1]/img/@src')[0], each.xpath('./a[2]/i/span/text()')[0], each.xpath('./a[2]/@href')[0],
               each.xpath('./a[2]/text()')[0])
        ret_list.append(content)
    else:
        break

def get_fashion_news():
    if news_flag:
        ret = '''
        <b>早间消息</b><br>
        <ul>
        %s
        </ul>
        ''' % "".join(ret_list)
        return ret

    return '''
        <b>今早无消息，为你呈上昨日消息</b><br>
        <ul>
        %s
        </ul>
        ''' % "".join(ret_list)


# print(get_fashion_news())