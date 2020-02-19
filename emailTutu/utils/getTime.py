import datetime




# 获取当天时间
def get_today():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")


# 获取和图图相恋时间差/天
def get_total_day():
    then = datetime.datetime(2019, 12, 1, 20, 0, 0)
    now = datetime.datetime.now()
    delta = now - then
    return delta.days


# 获取和图图相恋时间差/秒
def get_total_seconds():
    then = datetime.datetime(2019, 12, 1, 20, 0, 0)
    now = datetime.datetime.now()
    delta = now - then
    return delta.total_seconds()


if __name__ == '__main__':
    print(get_today())
    print(get_total_day())
    print(get_total_seconds())
