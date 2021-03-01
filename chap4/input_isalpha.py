#coding:utf-8

'''
    filename:input_isalpha.py
        chap:4
    subject:6
    conditions:input_string
    solution:input is ALPHA char or string
'''

input_string = input('Enter an alpha sting : ')

if input_string.isalpha():
    if (input_len:=len(input_string)) == 1:
        print('your input is an ALPHA char')
    elif input_len > 1:
        print('your input is an ALPHA string')
else:
    print('your input is not all ALPHA')


