#coding:utf-8

'''
    filename:schoolkid.py
        chap:6
    subject:9
    conditions:name ,age,get,set
    solution:class SchoolKid,ExaggeratingKid
'''


class SchoolKid:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age

class ExaggeratingKid(SchoolKid):
    def get_age(self):
        return self.age+2

if __name__ == '__main__':
    xiaoming = SchoolKid('xiaming',12)
    print(xiaoming.get_name())
    print(xiaoming.get_age())
    print(xiaoming.__dict__)
    print(dir(xiaoming))

    print('-'*60)
    hong = ExaggeratingKid('xiaohong',12)
    print(hong.get_name())
    print(hong.get_age())
    print(hong.__dict__)
    print(dir(hong))

