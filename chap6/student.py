#coding:utf-8

'''
    filename:student.py
        chap:6
    subject:2
    conditions:student's attributes[id,name,age,score,grade,school]
            method [do_homework,do_exam,]
    solution:class Student
'''



class Student:
    def __init__(self,idn,name,age,grade,school):
        self.idn = idn
        self.name = name
        self.age = age
        self.grade = grade
        self.school = school
    def do_homework(self,time:'minutes'):
        self.worktime = time
        return '{} used {} minutes to do homework.'.format(self.name,self.worktime)
    def do_exam(self,time:'0<=minutes',score:'0<=score<=100'):
        self.examtime = time
        if 0<=time<=90:
            self.score = score
        else:
            self.score = 0
        return f'{self.name} used {self.examtime} minutes to do exam,score is {score},final score is {self.score}'
    def introduction(self):
        print('My id is :',self.idn)
        print('my name is :',self.name)
        print("I'm {} years old".format(self.age))
        print("I'm in grade {} of {}".format(self.grade,self.school))


xiaoming = Student('A123456','Xiaoming',10,4,'No.3 Middle School')
xiaoming.introduction()
print(xiaoming.do_homework(25))
print(xiaoming.do_exam(78,90))


