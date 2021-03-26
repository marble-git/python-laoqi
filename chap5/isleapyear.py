#coding:utf-8

'''
    filename:isleapyear.py
        chap:5
    subject:3
    conditions:leap year is a year = (year%4 == 0 and year%100 != 0) or (year%400 == 0)
    solution:all leap years in  20th century
'''


def isleapyear(year):
    if (
            (year%4 ==0 and year%100 !=0) 
            or (year%400 ==0)):
        return True
    else:
        return False

leap_years = list(filter(isleapyear,range(1900,2000)))
print('all leap years in  20th century:',leap_years)


