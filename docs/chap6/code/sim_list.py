#coding:utf-8

'''
    filename:sim_list.py
    an object type simlilar to list type.
'''


class SimList:
    def __init__(self,total):
        self.__num = [None]*total
    def __getitem__(self,n):
        return self.__num[n]
    def __setitem__(self,n,data):
        self.__num[n]=data
    def __len__(self):
        return len(self.__num)


slst = SimList(3)
print(len(slst))
print(dir(slst))


