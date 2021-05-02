#coding:utf-8

'''
    An iterator
    filename:iterator.py
'''



class Myrange:
    def __init__(self,n):
        self.n = n
        self.i = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<=self.n:
            i = self.i
            self.i+=1
            return i
        else:
            raise StopIteration()

print('range(7):',list(range(7)))
print('Myrange(7):',list(Myrange(7)))



