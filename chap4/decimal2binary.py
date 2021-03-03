#coding:utf-8

'''
    filename:decimal2binary.py
        chap:4
    subject:12
    conditions:input a decimal integer
    solution:print the binary version
'''

def dec_2_bin(n):
    rst = []
    while n//2:
        rst.append(str(n%2))
        n//=2
    rst.append('1')
    return int(''.join(reversed(rst)))


integer = input('Enter an integer : ')
if integer.isdigit():
    integer = int(integer)
    print(f'decimal {integer} to binary : {dec_2_bin(integer)}')
