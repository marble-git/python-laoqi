#coding:utf-8

'''
    filename:arithmetic_sequence.py
        chap:5
    subject:12
    conditions:a1,d,n
    solution:sum arithmetic seq
'''


def sum_arithmetic_seq(a,d,n):
    return n*a + n*(n-1)*d/2

print(sum_arithmetic_seq(1,1,100))
