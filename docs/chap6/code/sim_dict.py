#coding:utf-8

'''
    filename:sim_dict.py
    define a type that is similar to dictionary.
'''


class SimDict:
    def __init__(self,k,v):
        self.dct = dict([(k,v)])

    def __getitem__(self,k):
        return self.dct[k]

    def __setitem__(self,k,v):
        self.dct[k] = v

    def __delitem__(self,k):
        del self.dct[k]

    def __len__(self):
        return len(self.dct)


d = SimDict('name','laoqi')
d['lang'] = 'python'
d['city'] = 'shanghai'
print(d['city'],d,d.dct)
print(len(d))
del d['city']
print(d.dct)




