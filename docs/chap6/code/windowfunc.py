#coding:utf-8

'''
    filename:windowfunc.py
    window moving function
'''


import itertools

def spliter(iterable,n):
    result = [[] for i in range(n)]
    resiter = itertools.cycle(result)
    for item,sublist in zip(iterable,resiter):
        sublist.append(item)
    return result


s = 'abcde'

d = dict(zip('abcdefgh','12345678'))

print("string:",s)
print(spliter(s,3))
print('dict:',d)
print(spliter(d,3))




