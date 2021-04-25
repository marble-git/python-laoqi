#coding:utf-8

'''
    filename:single_inheritance.py
'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

class Student(Person):
    def grade(self,n):
        print("{}'s grade is {}".format(self.name,str(n)))





stu1 = Student("Galileo",27)
stu1.grade(99)
print(stu1.get_name())
print(stu1.get_age())



#base class name
class StudentOverrideName(Person):
    def __init__(self,school,name,age):
        self.school = school
        Person.__init__(self,name,age)
    def grade(self,n):
        print("{}'s grade is {}".format(self.name,str(n)))
stu2 = StudentOverrideName("Soochow University",'Name',23)
stu2.grade(99)
print(stu2.get_name())
print(stu2.get_age())


#super
class StudentOverrideSuper(Person):
    def __init__(self,school,name,age):
        self.school = school
        super().__init__(name,age)
    def grade(self,n):
        print("{}'s grade is {}".format(self.name,str(n)))
stu3 = StudentOverrideSuper("Soochow University",'Super',24)
stu3.grade(99)
print(stu3.get_name())
print(stu3.get_age())


#error
class StudentOverrideError(Person):
    def __init__(self,school):
        self.school = school
    def grade(self,n):
        print("{}'s grade is {}".format(self.name,str(n)))
stu4 = StudentOverrideError("Soochow University")
stu4.grade(99)
print(stu4.get_name())
print(stu4.get_age())







