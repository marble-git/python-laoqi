#coding:utf-8

'''
    filename:force.py
        chap:5
    subject:13
    conditions:f1,f2,alpha
    solution:force(f1,f2,alpha)
'''

import math


f1 = 10
f2 = 10 
alpha = math.pi / 2

def force(f1,f2,alpha):
    '''正交分解法求合力
    以f1为x轴'''
    fx=f1 + f2*math.cos(alpha)
    fy=f2*math.sin(alpha)
    return math.sqrt(fx**2 + fy**2)




print(force(f1,f2,alpha))

