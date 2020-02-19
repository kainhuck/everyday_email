import requests
from utils.getTime import get_today
from lxml import etree
from mytools.UserAgent import makeAgent

url = "http://news.zstu.edu.cn/tzgg.htm"

def _init():
    today = get_today()

    r = requests.get(url, headers=makeAgent())
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)

    # 要发送的信息列表，今天或者上次通知
    notice_list = []
    notice_flag = True  # 今日有无消息

    notice = html.xpath('//ul[@class="right_vter"]/div')

    if today != notice[0].xpath("./span/text()")[0]:
        notice_flag = False  # 今日无消息，标志设置为False
        # 爬取上一次消息
        today = notice[0].xpath("./span/text()")[0]

    for each in notice:
        date = each.xpath("./span/text()")[0]
        if date == today:

            msg = """
                <li>
                    <i>%s</i>
                    <a href="%s"><b style="color: brown;">%s</b></a>
                </li>
            """ % (date, "http://news.zstu.edu.cn/" + each.xpath("./a/@href")[0], each.xpath("./a/text()")[0])

            notice_list.append(msg)
        else:
            break
    return notice_list, notice_flag


def get_ZSTU_notice():
    notice_list, notice_flag = _init()
    if notice_flag:  # 今日有消息
        return """
        <b>早间通知公告</b><br>
        <ul>
            %s
        </ul>
        """ % "".join(notice_list)

    return """
    <b>今早无通知公告，为图图呈上最近一次内容</b><br>
    <ul>
            %s
        </ul>
        """ % "".join(notice_list)


# print(get_ZSTU_notice())