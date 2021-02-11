#coding:utf-8

'''
4. 直角三角形 hypotenuse=50 side1 = 30 求 side2 ?

计算直角三角形的一条直角边长度
'''

hypotenuse = 50
side1 = 30

import math 
side2 = math.sqrt(hypotenuse ** 2 - math.pow(side1,2))

result_msg = "With a triangle's hypotenuse = {0:<4} and side1 = {1:^4},It's \nside2 = {2:>4}".format(hypotenuse,side1,side2)
print(result_msg)




