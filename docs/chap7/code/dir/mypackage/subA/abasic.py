#coding=utf-8
'''
    path = ./mypackage/subA/abasic.py
    filename = abasic.py
'''

from . import apython
from ..subB import brust




print('in mypackage/subA/abasic.py')
basic = "BASIC-"+apython.python()+"-"+brust.rust
print(basic)
