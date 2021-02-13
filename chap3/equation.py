
#coding=utf-8

'''
    filename:equation.py
    chap:3
    subject:8 ---10.3
    conditions:a=2,b=5,c=-8
    solution:roots of a * x^2 + b * x + c = 0
'''

import math
'''
a = 2
b = 5
c = -8
'''
a,b,c=eval(input("""
Please enter a,b,c of 'a * x^2 + b * x + c = 0' 
with format of 'a,b,c': """)) 

#print(a,b,c)
deta = math.sqrt(b**2 - 4*a*c)
root1 = (-b + deta) /(2 * a)
root2 = (-b - deta) /(2 * a)

message = '''with the condition "a = {a},b = {b},c = {c}"
of equation "a*x^2 + b*x + c = 0"
It's roots are 
root1 = {root1} and 
root2 = {root2}
'''.format(a=a,b=b,c=c,root1=root1,root2=root2)

print(message)


