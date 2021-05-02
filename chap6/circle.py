#coding:utf-8

'''
    filename:circle.py
        chap:6
    subject:7
    conditions:radius,x,y self.circumference self.area
    solution:class Circle
'''

from point import Point
import math

class Circle:
    def __init__(self,r,center:Point=Point(0,0)):
        self.center = Point(*center)
        self.r=r

    def circumference(self):
        c = 2* math.pi * self.r 
        return c
    def area(self):
        s = math.pi * math.pow(self.r,2)
        return s
    def __repr__(self):
        # */** 拆包 需要对象 可迭代 Iterable
        return "{}({},{})".format(type(self).__name__,self.r,self.center)
    def __str__(self):
        fmt = '{:15}:{}'
        r = fmt.format('Radius',self.r)
        o = fmt.format('Center',self.center)
        c = fmt.format('Circumferance',self.circumference())
        s = fmt.format('Area',self.area())

        return '\n'.join([r,o,c,s])

if __name__ == '__main__':
    c1 = Circle(1)
    print(c1)
    c2 = Circle(23)
    print(c2)


