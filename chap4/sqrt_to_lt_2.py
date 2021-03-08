#coding:utf-8

'''
    filename:sqrt_to_lt_2.py
        chap:4
    subject:11
    conditions:input a int number > 2
    solution:sqrt the number  until < 2 ,times, .2f
'''

import math

integer = input('Enter an integer > 2 : ')

if integer.isdigit() and (rst:=int(integer)) > 2:
    count = 0
    while rst >= 2:
        count += 1
        rst = math.sqrt(rst)
    print(f'sqort_times: {count},result:{rst:.2f}')

else:
    print('Input is not integer or not gt 2.')
