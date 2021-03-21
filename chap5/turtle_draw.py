#coding:utf-8

'''
    filename:turtle_draw.py
        chap:5
    subject:6
    conditions:library turtle
    solution:draw a pentagon
'''


import turtle as tu



edge = 200

tu.pencolor('red')
tu.width(3)
tu.speed(2)

tu.up()
tu.bk(edge/2)
tu.down()



for i in range(5):
    tu.fd(edge)
    tu.right(180 - 180/5)


