# import calendar
#import datetime

# while year%4==0 and year%100 !=0) or (year%400 ==0)
# year=int(input('연도입력: '))
# if (year%4==0 and year%100 !=0) or (year%400 ==0):
#     year=input('윤년입니다. 다시 입력: ')
# else:
#     print(calendar.calendar(year))
#     month= input('월 입력: ')
#     day =input('일 입력: ')

# weekday1= calendar.weekday(year,month,day)
# print(weekday1)

# print(f'년:{year},월:{month},일:{day} 요일:{weekday}')

#? 윤년 판별함수
#input 연도받고 output으로 True,False 반환

# def isleap(year):
#     if (year%4 ==0 and year%100 !=0) or (year%400 ==0):
#         return True

#     return False
    
# year= input()
# while year != exit:
#     print(isleap(int(year)))
    # year= input()

# ! 문자열을 입력받아 정렬된 문자열을 return
# a=input().split())

def getSortedStr(strValue):
    t=sorted(strValue)
    # print(sorted(strValue))
    t = ''.join(t)     #join으로 문자열 합치기  
    return t

inputL= input().split()
res={}
for strV in inputL:
    sortedV = getSortedStr(strV)
    if sortedV in res.keys():
        res[sortedV].append(strV)
    else:
        res[sortedV] = [strV]

print(list(res.values()))

# getSortedStr('eat')

# res: {'aet':['eat','tea','ate'],'ant':[],}
# 입력된 모든 문자열에 대하여

# if 문자열의 대표값이 res에 있으면 
#     res[대표값].append(문자열)
# else:
#     res[대표값]=[문자열]



#? 2차원 리스트의 전체합 구하기

def all_list_sum(values):
    sumV=0
    for value in values: 
        print(value)
        for v in value:
            # print(v)
            sumV += v
    return sumV

res = all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
print(res)

#######################################
def all_list_sum(values):
    sumV=0
    for value in values: 
        # print(value)
        sumV=0
        for v in value:
            # print(v)
            sumV += v
        print(sumV)
    return sumV

res = all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
print(res)


####################
#max함수없이 최댓값 구하기
#! 함수만들때 return 넣기