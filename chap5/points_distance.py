#coding:utf-8

'''
    filename:points_distance.py
        chap:5
    subject:11
    conditions:pionts a,b
    solution:distance(a,b)
'''


import math

def distance(a:tuple,b:tuple)->float:
    c = sum([(a[i]-b[i])**2 for i in range(2)])
    return math.sqrt(c)




print(distance((0,2),(0,4)))





