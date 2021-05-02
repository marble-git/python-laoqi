#coding:utf-8

'''
    filename:point.py
        chap:6
    subject:15
    conditions:(x,y) 实现 + 运算
    solution:class Point
'''


import math


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        x=self.x + other.x
        y=self.y + other.y
        return self.__class__(x,y)
    def __sub__(self,other):
        x=self.x - other.x
        y=self.y - other.y
        return self.__class__(x,y)
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    def __repr__(self):
        return '{}({},{})'.format(type(self).__name__,self.x,self.y)
    __str__ = __repr__
    def __iter__(self):
        # 支持*Point(x,y) 拆包
        return iter((self.x,self.y))

if __name__ == '__main__':
    a=Point(2,3)
    b=Point(5,5)
    c=a+b
    print(a,b,c)



