#coding:utf-8

'''
    filename:mysequence.py
        chap:6
    subject:20
    conditions:inherit collections.abc.Sequence
            新容器内的对象必须按照一定顺序排列
    solution:class MySequence
'''

import collections
import numbers

class MySequence(collections.abc.Sequence):
    '''必要方法 __getitem__,__len__'''
    def __init__(self,seq):
        self.seq = type(self).order(seq)

    def __getitem__(self,index):
        return self.seq[index]
    def __len__(self):
        return len(self.seq)
    def __repr__(self):
        return '{}:{}'.format(type(self).__name__,self.seq)


    @staticmethod
    def order(seq):
        '''返回 按类别排序的序列'''
#        print('seq:',seq)
        source = list(seq)
#        print('source:',source)
        number_list = []
        str_list = []
        tuple_list = []
        list_list = []
        dict_list = []
        set_list = []
        other_list = []
        d = {'numbers.Real':number_list,
                'str':str_list,
                'tuple':tuple_list,
                'list':list_list,
                'dict':dict_list,
                'set':set_list}
        for item in source:
            for cls_string in d.keys():
                if isinstance(item,eval(cls_string)):
                    d[cls_string].append(item)
                    break
            else:
                other_list.append(item)
#        print('other_list :',other_list)
        rst = []
        lists = list(d.values())
        for lst in lists:
#            print('before sort:',lst)
            lst.sort()
#            print('after sort:',lst)
            rst += lst
        return rst+other_list

if __name__ == '__main__':
    l = [1,2,(3,4,55),{'a','b'},{(11,11):111,'name':'laoqi'},(33,5),62,'python',9,'age']
    a = MySequence(l)
    print(l)
    print(a)
    print(len(a))
    print(list(a))
