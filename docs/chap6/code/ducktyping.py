#coding:utf-8

'''
    filename:ducktyping.py
'''


class Cat:
    def speak(self):
        print('cat speak:meow')

class Dog:
    def speak(self):
        print('Dog speak:woof!')

class Bob:
    def speak(self):
        print('Bob speak:welcome')
    def bow(self):
        print('thank you')
    def drive(self):
        print('beep,beep')


def cmd(pet):
    pet.speak()


pets = [Cat(),Dog(),Bob()]

for pet in pets:
    cmd(pet)






