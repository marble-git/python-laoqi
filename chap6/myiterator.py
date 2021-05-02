#coding:utf-8

'''
    filename:myiterator.py
        chap:6
    subject:13
    conditions:for, integer N,decrease 1 to 0
    solution:class MyIterator
'''


class MyIterator:
    def __init__(self,n:'start integer to decrease'):
        self.n=n
    def __next__(self):
        self.n-=1
        if self.n <0:
            raise StopIteration
        return self.n
    def __iter__(self):
        return self




if __name__ == '__main__':
    a=MyIterator(10)
    print(a,iter(a))
    for i in a:
        print(i)


