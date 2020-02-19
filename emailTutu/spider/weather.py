import requests
from urllib.parse import quote
from lxml import etree
from config import city
from mytools.UserAgent import makeAgent

url = "https://www.tianqi.com/tianqi/search?keyword=" + quote(city)

# 定义xpath规则
date_xpath = '//dd[@class="week"]/text()'
temperature_xpath = '//p[@class="now"]//text()'
weather_xpath = '//dd[@class="weather"]/span/b/text()'
weather_temp_xpath = '//dd[@class="weather"]/span/text()'  # 天气温度
humidity_xpath = '//dd[@class="shidu"]/b[1]/text()'  # 湿度
wind_xpath = '//dd[@class="shidu"]/b[2]/text()'
sun_xpath = '//dd[@class="shidu"]/b[3]/text()'  # 紫外线
air_xpath = '//dd[@class="kongqi"]/h5/text()'  # 空气质量
pm_xpath = '//dd[@class="kongqi"]/h6/text()'  # PM
sun_rise_xpath = '//dd[@class="kongqi"]/span/text()'  # 日出日落

html = ""
date = ""
temperature = ""
weather = ""
weather_temp = ""
humidity = ""
wind = ""
sun = ""
air = ""
pm = ""
sun_rise = ""


#
# print(" ".join(date))
# print(" ".join(temperature))
# print(" ".join(weather))
# print(" ".join(weather_temp))
# print(" ".join(humidity))
# print(" ".join(wind))
# print(" ".join(sun))
# print(" ".join(air))
# print(" ".join(pm))
# print(" ".join(sun_rise))

def _init():
    global date, temperature, weather, weather_temp, humidity, wind, sun, air, pm, sun_rise

    r = requests.get(url, headers=makeAgent())
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    date = html.xpath(date_xpath)
    temperature = html.xpath(temperature_xpath)
    weather = html.xpath(weather_xpath)
    weather_temp = html.xpath(weather_temp_xpath)
    humidity = html.xpath(humidity_xpath)
    wind = html.xpath(wind_xpath)
    sun = html.xpath(sun_xpath)
    air = html.xpath(air_xpath)
    pm = html.xpath(pm_xpath)
    sun_rise = html.xpath(sun_rise_xpath)
    if not len(date):
        _init()
    else:
        return

_init()

def get_date():
    global date
    return " ".join(date)


def get_temperature():
    global temperature
    return "".join(temperature)


def get_weather():
    global weather
    return " ".join(weather)


def get_weather_temp():
    global weather_temp
    return " ".join(weather_temp)


def get_humidity():
    global humidity
    return " ".join(humidity)


def get_wind():
    global wind
    return " ".join(wind)


def get_sun():
    global sun
    return " ".join(sun)


def get_air():
    global air
    return " ".join(air)


def get_pm():
    global pm
    return " ".join(pm)


def get_sun_rise():
    global sun_rise
    return " ".join(sun_rise)
