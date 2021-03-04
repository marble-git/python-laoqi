#coding:utf-8

'''
    filename:palindrome.py
        chap:4
    subject:17
    conditions:输入一个5位数
    solution:判断是否为回文数
'''


number = input('Enter a 5 digits number : ')
if number.isdigit() and len(number) == 5:
    if number == number[::-1]:
        print(f'{number} is palindrome.')
    else:
        print(f'{number} is not palindrome.')
else:
    print('Your input is not pure digits or not 5 digits.')
