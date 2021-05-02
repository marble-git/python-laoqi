#coding:utf-8

'''
    filename:flatnesting.py
        chap:6
    subject:19
    conditions:flat nested_list
    solution:function flat_nesting
'''

import collections


def flat_nesting(nested):
#    print('Enter','-'*40)
    for item in nested:
        if isinstance(item,(list,tuple,dict,set)):
#        if isinstance(item,collections.abc.Container):
#            print('yield from :',item)
            yield from flat_nesting(item)
        else:
#            print('yield :',item,'*'*30)
            yield item
#    print('Leave','='*40)




if __name__ == '__main__':
    a = [1,2,(3,4,{'a','b'},{(11,22):111,'name':'laoqi'}),5,6,'python',9]
    print('nested list :',a)
    print(list(flat_nesting(a)))

