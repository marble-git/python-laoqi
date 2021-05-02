#coding:utf-8

'''
    filename:merit_student.py
        chap:6
    subject:5
    conditions:inherit class Student,
            attrs [studyhard,helpothers]
            method []
    solution:
'''


from  student import Student

class MeritStudent(Student):
    studyhard = True
    helpothers = True
    def ismeritstudent(self):
        return '{} is studyhard:{} and helpothers:{}.'.format(self.name,self.studyhard,self.helpothers)


xiaohong = MeritStudent('A903242','xiaohong',11,7,'NO.2 Middle School')
xiaohong.introduction()
print(xiaohong.ismeritstudent())


