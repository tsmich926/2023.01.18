# import calendar
# import datetime

# year=int(input('연도입력: '))
# while (year%4==0 and year%100 !=0) or (year%400 ==0):
#     year=int(input('윤년입니다. 다시 입력: '))
# print(calendar.Calendar(year))
# month= int(input('월 입력: '))
# day =int(input('일 입력: '))
# #요일반환
# weekday= calendar.weekday(year,month,day)
# days=['월','화','수','목','금','토','일']
# d= days[datetime.date(year,month,day).weekday()]
# if d == '월':
#     print('경고:월요일입니다.')

# print(f'년:{year},월:{month},일:{day} 요일:{d}')


# 달력사용
# c =calendar.TextCalendar()
# print(c.formatyear(2016))


def getSortedStr(strValue):
    t=sorted(strValue)
    print(t)



