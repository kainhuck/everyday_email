import datetime
from config import lesson_table

# 获取当前星期
now = datetime.datetime.now().strftime("%A")

# 获取今天课表
lessons = lesson_table.get(now, None)

def get_lesson():
    if not lessons: # 周末
        return '''
        <h3 style="color: darkviolet;">今天是周末好好休息吧 <^_^></h3>
        '''

    lesson_li = ''
    for each in lessons:
        temp_li = """
        <li>
        课名：%s<br>
        任课老师：<span>%s</span><br>
        上课地点：%s<br>
        上课时间：%s<br>
        </li>
        """ % (each["name"], each["teacher"], each["address"], each["long"])
        lesson_li += temp_li

    return '''
    <h3>康康给图图播报<i style="color: darkviolet;">今日课表</i></h3>
    <ul>
       %s
    </ul>
    ''' % lesson_li