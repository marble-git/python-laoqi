#coding:utf-8

'''
    filename:relationship_of_point_circle.py
        chap:6
    subject:8
    conditions:Point(),Circle()
    solution:relationship between circle and point
'''

from circle import Circle
from point import Point
import math


class Relationship:
    def __init__(self,circle:Circle,point:Point):
        self.c=circle
        self.p=point
    def get_relation(self):
        distance = abs(self.c.center - self.p)
        rst = ''
        if distance < self.c.r:
            rst = 'in'
        elif math.isclose(distance,self.c.r):
            rst = 'on'
        elif distance > self.c.r:
            rst = 'outside'
        return 'The {!r} is {} the {!r}.'.format(self.p,rst,self.c)
    def __str__(self):
        return self.get_relation()


if __name__ == '__main__':
    p1 = Point(0,0)
    p2 = Point(1,0)
    p3 = Point(1,1)
    c = Circle(1,p2)
    print(Relationship(c,p1))
    print(Relationship(c,p2))
    print(Relationship(c,p3))

