import requests
from utils.getTime import get_today
from lxml import etree
from mytools.UserAgent import makeAgent

url = "http://news.ladymax.cn/"

news_xpath = '//div[@id="list"]/div[@class="i"]'


def _init():
    today = get_today()

    r = requests.get(url, headers=makeAgent())
    r.encoding = r.apparent_encoding
    # print(r.text)
    # print(r.status_code)

    html = etree.HTML(r.text)
    news = html.xpath(news_xpath)

    # 要发送的消息列表
    news_list = []
    news_flag = True  # 今日是否有消息

    if today != news[0].xpath("./a[2]/i/text()")[0].split("/")[1].strip():
        news_flag = False  # 今日无新闻
        today = news[0].xpath("./a[2]/i/text()")[0].split("/")[1].strip()  # 获取最近一次新闻

    for each in news:
        date = each.xpath("./a[2]/i/text()")[0].split("/")[1].strip()
        if date == today:
            msg = each.xpath("./a[2]/i/text()")[0] + ' <b style="color: brown;">' + each.xpath("./a[2]/text()")[
                0] + '</b> || <a href="' + each.xpath("./a[2]/@href")[0] + '">详情链接</a>'
            news_list.append(msg)
    return news_flag, news_list


def get_fashion_news():
    news_flag, news_list = _init()
    content = ""
    if news_flag:
        head = "<b>今日消息<b/><br>"
    else:
        head = "<b>今日无消息，为图图呈上最近一次消息</b><br>"
    content += head

    for each in news_list:
        content += "<p>" + each + "</p>"
    return content
