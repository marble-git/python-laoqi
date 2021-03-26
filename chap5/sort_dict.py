#coding:utf-8

'''
    filename:sort_dict.py
        chap:5
    subject:18
    conditions:dictionary d
    solution:sorted d by key
'''




import random
import operator


keys = list('abcdef')
random.shuffle(keys)
values = [random.randint(0,100) for i in range(len(keys))]
d=dict(zip(keys,values))
print('dictionary:',d)

def sort_dict(d):
    _=dict(sorted(d.items(),key=operator.itemgetter(0)))
    d.clear()
    d.update(_)

sort_dict(d)
print('sorted dict:',d)
