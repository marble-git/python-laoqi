#coding:utf-8

'''
    filename:get.py
        chap:5
    subject:17
    conditions:list,index
    solution:return list[idex] or default value
'''





lst = list('abc')

def list_get(lst,index,default=None):
    d=dict(enumerate(lst))
    return d.get(index,default)


print(list_get(lst,2))
print(list_get(lst,3))
print(list_get(lst,3,3333))





