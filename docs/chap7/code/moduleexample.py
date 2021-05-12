#coding:utf-8

'''
    filename:moduleexample.py
    The module of Python.
'''

__all__ = [
        'Book',
        'GLOBALVAR',
        ]

GLOBALVAR = 'test string'
class Book:
    lang = 'python'
    def __init__(self,auther):
        self.auther = auther
    def get_name(self):
        return self.auther


def foo(x):
    return x*2

python_var = Book("laoqi")
python_name = python_var.get_name()

mul_result = foo(2)




#print("__path__:",__path__) #error
print("__file__:",__file__)
print("__package__:",__package__)


