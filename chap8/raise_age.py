#coding:utf-8

'''
    filename:raise_age.py
    judge the number of age is even or odd.
'''


def enterAge(age):
    if age <0:
        raise ValueError('Only *POSITIVE* integers are allowed')
    if age%2 == 0:
        print('age is even')
    else:
        print('age is odd')


try:
    num = int(input('Enter your age: '))
    enterAge(num)
except ValueError as e:
    print(e)
    print('Only *INTEGERS* are allowed')
except :
    print('Something is wrong')


