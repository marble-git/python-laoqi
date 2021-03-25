#coding:utf-8

'''
    filename:get_dict.py
        chap:5
    subject:23
    conditions:list
    solution:dict
'''


lst = [1,'a',2,'b',3,'c',4,'d']

def get_dict(lst):
    '''convert lst to a dict
    with keys are lst[::2],values are lst[1::2]
    example:  [1,'a',2,'b',3,'c',4,'d']->{1:'a',2:'b',3:'c',4:'d'}
    '''
    return dict(zip(lst[::2],lst[1::2]))


print('list:',lst)
print('dict:',get_dict(lst))


