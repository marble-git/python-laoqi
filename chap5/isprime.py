#coding:utf-8

'''
    filename:isprime.py
        chap:5
    subject:1
    conditions:isprime range # 1 既不是素数prime也不是合数composite
    solution:find all numbers are prime in range
'''


import math


def isprime(number) -> 'bool val':
    if number < 2:
        return False
    elif number in (2,3):
        return True
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0 :
            return False
    return True

primes = list(filter(isprime,range(100)))
print('all numbers are prime in range(100) are : ',primes)
