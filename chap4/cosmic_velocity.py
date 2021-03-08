#coding:utf-8

'''
    filename:cosmic_velocity.py
        chap:4
    subject:3
    conditions:input velocity
    solution:print the status of the subject with the velocity of input_velocity
'''



first_cosmic_velocity = 7.9 
second_cosmic_velocity =  11.2
third_cosmic_velocity =  42.2


def isnumber(string):
    try:
        float(string)
        return True
    except:
        return False

def get_status(velocity):
    if velocity < first_cosmic_velocity:return 'fall back to the ground'
    elif velocity < second_cosmic_velocity:return 'move around the earth'
    elif velocity < third_cosmic_velocity:return 'move around the sun'
    else:return 'fly out of the solar system'


input_velocity = input('Enter the velocity of subject [km/s]: ')

if isnumber(input_velocity):
    print(f'The subject will {get_status(float(input_velocity))}')
else:
    print('illegal input')




