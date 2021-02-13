#coding:utf-8
'''
cylinder.py
10.2 onput r and h
chap3 7. 计算圆柱体的体积并打印结果
'''
import math

#radius = 11
#height = 98

radius,height=eval(input("Please enter r and h of cylinder with the format of 'r,h'"))

volume = height * 2 * math.pi * radius ** 2

message = '''With a cylinder's radius is {R}, and height is {H}
It's volume is {V}'''.format(R=radius,H=height,V=volume)

print(message)
