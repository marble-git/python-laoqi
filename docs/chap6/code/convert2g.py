#coding:utf-8

'''
    filename:convert2g.py
    convert from jin to gram.
'''


class ToGram(float):
    def __new__(cls,jin=0.0):
        gram = jin/2 * 1000
        obj = super()
        print("super obj :",obj)
        return obj.__new__(cls,gram)

jin = 2.3 

gram = ToGram(jin)

print('{}jin = {}g'.format(jin,gram))
