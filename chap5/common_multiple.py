#coding:utf-8

'''
    filename:common_multiple.py
        chap:5
    subject:5
    conditions:a,b,range(n)
    solution:get common multiples of a,b in range(n)
'''


from functools import partial


def iscommon_multiple(a,b,c):
    '''test if c is common multiple of a,b'''
    if c%a or c%b:
        return False
    else:
        return True


a,b,n = eval(input('enter a,b and range n:'))

isc_m = partial(iscommon_multiple,a,b)

common_multiples = list(filter(isc_m,range(1,100)))
print(f'common_multiples of {a,b} in range({n}) is {common_multiples}.')

