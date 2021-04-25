#coding:utf-8

'''
    filename:fibsgenerator.py
    the generator of Fibonacci sequence.
'''

import itertools


def fibs():
    prev, curr = 0,1
    while True:
        yield prev
        prev,curr=curr,prev+curr


print(list(itertools.islice(fibs(),10)))



