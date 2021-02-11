
#coding=utf-8

'''
circle.py
chap3 6. 已知圆的半径 R = 23 计算:
    1. 周长 和面积
    2. 打印结果，保留2位小数
    3. 调试无误
'''

import math


radius = 23

circumference = 2 * radius * math.pi
area = math.pow(radius,2) * math.pi

message = '''With radius of a circle is {R}.
It\'s circumference is {L:.2f}
and area is {S:.2f}'''.format(R=radius,L=circumference,S=area)

print(message)
