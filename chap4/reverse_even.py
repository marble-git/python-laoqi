#coding:utf-8

'''
    filename:reverse_even.py
        chap:4
    subject:8
    conditions:input int number
    solution:if the end number is even ,then reverse the int number [234->432,120->21]
'''


input_number = input('Enter a integer: ')

if input_number.isdigit() and int(input_number[-1])%2 == 0:
    print(f'''Reversed number : {int(''.join(reversed(input_number)))}''')
else:
    print("Inputed string isn't pure digit or not even.")
