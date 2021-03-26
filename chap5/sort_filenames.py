#coding:utf-8

'''
    filename:sort_filenames.py
        chap:5
    subject:20
    conditions:list of filenames
    solution:sorted list of filenames
'''




import re


filenames = ['py1.py','py14.py','py10.py','py2.py',]

fl = filenames.copy()
fl.sort()
print('filenames:',filenames)
print('fl:',fl)


def sort_filenames(filenames):
    #fl = [re.findall(r'\d+|\D+',i) for i in filenames]
    return sorted(filenames,key=lambda s:int(re.findall(r'(\d+)',s)[0]))


filenames = sort_filenames(filenames)
print('filenames:',filenames)
