import re
import time

import schedule

from sendEmail import sendEmail
from utils.getTime import *
from utils.getWords import get_words
from utils.lesson import get_lesson
from spider.weather import *
from spider.zstu import get_ZSTU_notice
from spider.fashion import get_fashion_news
from spider.artthat import get_art_pic
from config import city, sendTime


def main():
    # 1. 主题
    subject = "%s-图图早上好～" % get_today()

    # 2. 内容
    with open("./template.html", "r") as f:
        html = "".join(f.readlines())

    # 2.1 在一起的天数
    msgContent = re.sub(r"{{total_days}}", str(get_total_day()), html)

    # 2.2 爱图图的话
    msgContent = re.sub(r"{{love_words}}", get_words(), msgContent)

    # 2.3 每日天气信息
    msgContent = re.sub(r"{{date}}", get_date(), msgContent)
    msgContent = re.sub(r"{{temperature}}", get_temperature(), msgContent)
    msgContent = re.sub(r"{{weather}}", get_weather(), msgContent)
    msgContent = re.sub(r"{{weather_temp}}", get_weather_temp(), msgContent)
    msgContent = re.sub(r"{{humidity}}", get_humidity(), msgContent)
    msgContent = re.sub(r"{{wind}}", get_wind(), msgContent)
    msgContent = re.sub(r"{{sun}}", get_sun(), msgContent)
    msgContent = re.sub(r"{{air}}", get_air(), msgContent)
    msgContent = re.sub(r"{{pm}}", get_pm(), msgContent)
    msgContent = re.sub(r"{{sun_rise}}", get_sun_rise(), msgContent)
    msgContent = re.sub(r"{{city}}", city, msgContent)

    # 2.4 浙江理工大学当日通知
    msgContent = re.sub(r"{{zstu_notice}}", get_ZSTU_notice(), msgContent)

    # 2.5 时尚头条网最新新闻
    msgContent = re.sub(r"{{fashion_news}}", get_fashion_news(), msgContent)

    # 2.6 艺廊网一张艺术图片
    msgContent = re.sub(r"{{art_pic}}", get_art_pic(), msgContent)

    # 2.7 图图课表
    msgContent = re.sub(r"{{lesson}}", get_lesson(), msgContent)

    # attachment = '/home/kain/Pictures/bg01.jpg'
    sendEmail(subject, msgContent)


# 每天7:00执行一次
# schedule.every().day.at(sendTime).do(main)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)d

main()
