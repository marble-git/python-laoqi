
#coding=utf-8

'''
    filename:triradian_radian.py
    chap:3
    subject:9 10.4
    user input a,b,c
    conditions:side1,a,b,c of sides =3,7,9
    solution:radian A,B,C
COS_C = (a^2+b^2-c^2 )/(2*a*b)
'''

import math

#sides = (3,7,9)
sides = tuple(eval(input("""
Please enter the 3 sides of triangle 
with the format of 'a,b,c': """)))

#print(sides)

results = []
for i in range(3):
    a = sides[(i+0)%3] 
    b = sides[(i+1)%3]
    c = sides[(i+2)%3]
    cos_a = float(c**2 + b**2 - a**2)/float(2*c*b)
    C = math.acos(cos_a)
    #print(a,b,c,cos_a,C)
    results.append(C)

message = '''The sides of triradian are a,b,c={0},{1},{2}
then It's radians are A,B,C={3},{4},{5}
'''.format(*(list(sides)+results) )

print(message)


