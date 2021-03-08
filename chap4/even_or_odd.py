#coding:utf-8

'''
    filename:even_or_odd.py
        chap:4
    subject:4
    conditions:input a number
    solution:print even | odd
'''


input_number = input('Enter a number : ')
if input_number.isdigit():
    if int(input_number) % 2:
        print('your number is odd.')
    else:
        print('your number is even.')
else:
    print('illegal input')


