#coding:utf-8

'''
    filename:roundfloat.py
        chap:6
    subject:16
    conditions:对6.8.1节的类RoundFloat改写，增加 +，* 方法
    solution:__add__ __mul__
'''

import numbers

class RoundFloat:
    def __init__(self,value):
        self.value = round(value,2)
    def __str__(self):
        return "{:.2f}".format(self.value)
    __repr__ = __str__
    #新增 加法  和乘法
    def __add__(self,other):
        if isinstance(other,numbers.Real):
            return type(self)(self.value + other)
        if isinstance(other,type(self)):
            return self.__class__(self.value + other.value)
        raise TypeError("""unsupported operand type(s) for *: '{}' and '{}'""".format(type(self).__name__,type(other).__name__))
    def __radd__(self,other):
        return self.__add__(other)
    #乘法
    def __mul__(self,other):
        if isinstance(other,numbers.Real):
            return type(self)(self.value * other)
        if isinstance(other,type(self)):
            return self.__class__(self.value*other.value)
        raise TypeError("""unsupported operand type(s) for *: '{}' and '{}'""".format(type(self).__name__,type(other).__name__))
    def __rmul__(self,other):
        return self.__mul__(other)


print('in roundfloat.py')
if __name__ == '__main__':
    a = RoundFloat(3.145)
    print(dir(a))
    print(a+a,44+a,a+45.33)
    print(a*a,23.9*a,124*a)

