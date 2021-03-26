#coding:utf-8

'''
    filename:mass_energy_equation.py
        chap:5
    subject:4
    conditions:E = m * c**2
    solution:input mass,get energy
'''


def mass_energy(mass:'kg'):
    ''' calculate the energy of mass
    returm mass * c**2
    mass : kg
    c : m/s
    energy : j
    '''

    c=299792458
    return mass * c**2



mass = int(input('enter the mass (kg):'))

print(f'the energy of mass is {mass_energy(mass):22.23e}j.')
