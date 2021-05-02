#coding:utf-8

'''
    filename:physicist.py
    single inheritance Physicist
'''


class Physicist:
    def __init__(self,name,iq=120,looks='handsom',subject='physics'):
        self.name=name
        self.iq=iq
        self.looks=looks
        self.subject=subject
    def research(self,field):
        print('{0} research {1}'.format(self.name,field))
    def speak(self):
        print(
f'''My name is {self.name}
I am {self.looks}
Intelligence is {self.iq}
I like {self.subject}''')

class ExperimentalPhysicist(Physicist):
    def __init__(self,main_study,name,iq=120,looks='handsom',subject='physics'):
        self.main_study=main_study
        super().__init__(name,iq,looks,subject)
    def experiment(self):
        print('{0} is in Physics Lab.'.format(self.name))

class TheoreticalPhysicist(Physicist):
    def __init__(self,theory,name,iq=120,looks='handsom',subject='physics'):
        self.theory=theory
        super().__init__(name,iq,looks,subject)
    def research(self,field,base):
        super().research(field)
        print(f'My theory is {field}, it is based on {base}.')


einstein = TheoreticalPhysicist('Relativity','Albert Einstein',160,'Hair is messy but handsom')
einstein.research('Black Hole','General relativity')
einstein.speak()
print('*'*50)


wu = ExperimentalPhysicist('Nuclear Physics','Chien-Shiung Wu',160,'beautiful and wisdom')
wu.experiment()
wu.speak()





