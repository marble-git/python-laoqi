#coding:utf-8

'''
    filename:custom_exception.py
    judge the number of age is even or odd
'''



class NegativeAgeException(RuntimeError):
    def __init__(self,age):
        super().__init__()
        self.age = age


def enterage(age):
    if age<0:
        raise NegativeAgeException('Only *POSITIVE* integers are allowed')
    if age%2==0:
        print('age is even')
    else:
        print("age is odd")


try:
    age = int(input('Enter your age : '))
    enterage(age)
except NegativeAgeException as error:
    print('error: ',error)
    print('error.age: ',error.age)
    print('Only *INTEGERS* are allowed')
except :
    print('something is wrong')

