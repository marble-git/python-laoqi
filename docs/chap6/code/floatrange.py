#coding:utf-8

'''
    filename:floatrange.py
    generate a sequence of parmeters with floating-point numbers.
'''


import itertools


def frange(start,end=None,step=1.0):
    if end is None:
        end = float(start)
        start = 0.0
    assert step
    for i in itertools.count():
        next = start+ i*step
        if (step > 0.0 and next >= end)or (step < 0.0 and next <= end):
            break
        yield next

f = frange(1.2,9)
print(list(f))


f = frange(1.2)
print(list(f))


f = frange(1.2,9,-1)
print(list(f))

f = frange(1.2,None,-1)
print(list(f))


f = frange(1.2,None,0)
print(list(f))










