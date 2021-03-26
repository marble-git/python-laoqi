#coding:utf-8

'''
    filename:factorial.py
        chap:5
    subject:10
    conditions:positive n
    solution:factorial n
'''


import operator
import functools

def factorial(n:'n > 0')->"n!":
    '''return n!'''
    if n > 0:
        return functools.reduce(operator.mul,range(1,n+1))



n = int(input('enter a positive number:'))
print(f'{n}! :',factorial(n))
