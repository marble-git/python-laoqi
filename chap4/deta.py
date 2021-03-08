#coding:utf-8

'''
    filename:deta.py
        chap:4
    subject:7
    conditions:a,b,c of equation
    solution:print roots | tips messages
'''

import math

a,b,c = eval(input('Enter a,b,c of equation "a*x^2 + b*x + c = 0" : '))
if (deta:= b**2 - 4*a*c) < 0:
    print('deta < 0 ,there is no roots')
else:
    root1 = (-b - math.sqrt(deta)) / (2 * a)
    root2 = (-b + math.sqrt(deta)) / (2 * a)
    print('the roots of equation "{}x^2 + {}x + {} = 0" are {},{}'.format(
        a,b,c,root1,root2)
        )
