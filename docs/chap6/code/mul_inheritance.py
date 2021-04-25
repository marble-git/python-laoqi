#coding:utf-8

'''
    filename:mul_inheritance.py
    the order of multiple inheritance in Python.
'''


class K1:
    def foo(self):
        print('K1-foo')
class K2:
    def foo(self):
        print('K2-foo')

class J1(K1):
    pass

class J2(K2):
    def bar(self):
        print("J2-bar")

class C(J1,J2):
    pass


c = C()
c.foo()
c.bar()
print(C.mro())
print(C.__mro__)
#print(c.mro())
#print(c.__mro__)
