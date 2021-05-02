#coding:utf-8

'''
    filename:replace.py
        chap:6
    subject:18
    conditions:replace pattern with repl in string
    solution:class Replace
'''

import re

class Replace:
    def __init__(self,string):
        self.string = string
    def replace(self,pattern,repl):
        return re.sub(pattern,repl,self.string)



if __name__ == '__main__':
    a = Replace('This is a book')
    print(a.replace('a','one'))

