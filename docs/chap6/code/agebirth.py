#coding:utf-8

'''
    filename:agebirth.py
    The example of class method
'''


import datetime


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def by_birth(cls,name,birth_year):
        thisyear = datetime.date.today().year
        age = thisyear - birth_year
        return cls(name,age)
    def get_info(self):
        return '''{}'s age is {}'''.format(self.name,str(self.age))

newton = Person('Newton',26)
print(newton.get_info())

hertz = Person.by_birth('Hertz',1857)
print(hertz.get_info())

laoqi = newton.by_birth('Qiwei',1986)
print(laoqi.get_info())



