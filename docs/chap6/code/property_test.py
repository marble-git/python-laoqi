#coding:utf-8

'''
    filename:property_test.py
'''


class Book:
    def __init__(self):
        self.__book = 'None book'
    @property
    def book(self):
        print('getting book name')
        return self.__book
    @book.setter
    def book(self,book):
        print('setting book name')
        self.__book=book
    @book.deleter
    def book(self):
        print('deleting book')
        del self.__book


b = Book()
print(dir(b))
print(b.__dict__)

print(b.book)
b.book = 'python'
print(b.book)
del b.book
print(b.book)

