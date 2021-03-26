#coding:utf-8

'''
    filename:sort_str_case_insensitive.py
        chap:5
    subject:19
    conditions:origin string
    solution:sorted string with case insensitive
'''





origin = 'LifeisShortYouNeedPython'

def sort_str_case_i(origin:str):
    return ''.join(sorted(origin,key=str.lower))


print(sort_str_case_i(origin))






