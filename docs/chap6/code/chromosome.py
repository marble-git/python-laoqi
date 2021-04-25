#coding:utf-8

'''
    filename:chromosome.py
    Judge having a boy or girl by sex chromosome.
'''


import random

class Father:
    def __init__(self):
        super().__init__()
        print('Father initing.')
        self.father_chromosome = "XY"
        return
    def father_do(self):
        print("Make money.")

class Mother:
    def __init__(self):
        super().__init__()
        print('Mother initing.')
        self.mother_chromosome = 'XX'
        return
    def mother_do(self):
        print('Manage money.')

class Child(Father,Mother):
    def __init__(self):
        super().__init__()
        print('Child initing.')
        #Father.__init__(self)
        #Mother.__init__(self)



    def child_gender(self):
        #fat = random.choice(self.father_chromosome)
        fat = ''.join(random.choices(self.father_chromosome,weights=[1,10],k=1))
        mot = random.choice(self.mother_chromosome)
        chi = fat+mot
        if "Y" in chi:
            return 'boy'
        else:
            return 'girl'



print(Child.mro())
p = Child()
for i in range(10):
    print(p.child_gender())



print('='*60)
f= Father()
f.father_do()







