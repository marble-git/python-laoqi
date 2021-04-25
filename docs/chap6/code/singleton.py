#coding:utf-8

'''
    filename:singleton.py
    singleton type by rewriting __new__
'''


class Singleton:
    __instance = None
    def __new__(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            print('create instance :',cls.__instance)
        return cls.__instance
    def __init__(self,*args,**kwargs):
        print('Singleton init called')

class MyClass(Singleton):
    a=1
    def __init__(self,*args,**kwargs):
        print('MyClass init called')

class A(Singleton):
    b=2
    def __init__(self,*args,**kwargs):
        print('A init called')

m1 = MyClass()
m2 = MyClass()
print(m1,m2)
print(dir(m1))

print('-'*60)

a1 = A()
a2 = A()

print(a1,a2)
print(dir(a1))
print('-'*60)

del a1,a2
print(A())




