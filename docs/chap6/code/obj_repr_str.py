#coding:utf-8

'''
    filename:obj_repr_str.py
'''


class RoundFloat:
    def __init__(self,value):
            self.value=value
    def __str__(self):
            print('in __str__')
            return '{0:.2f}'.format(self.value)
    def __repr__(self):
            print('in __repr__')
            return '{0}({1})'.format(type(self).__name__,self.value)


