import datetime
a = int(input())
b = int(input())
def get_day(a,b):
    d = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    return d[datetime.date(2020, a, b).weekday()]
print(get_day(a, b))