#coding:utf-8

'''
    filename:booksale.py
        chap:6
    subject:12
    conditions:class value:bookname:fixedprice,init with bookname
            instance method:totalpay
    solution:class BookSale
'''


class BookSale:
    book_dict = {}
    def __init__(self,book_name,book_price):
        self.book_name = book_name
        self.book_price = book_price
        self.__class__.book_dict[self.book_name] = self.book_price
    def sale(self,number):
        if number <=0 :
            return 'number MUST GT 0'
        return type(self).book_dict[self.book_name]*number



if __name__ == '__main__':
    a=BookSale('A',12)
    print(a.sale(10))
    print(a.sale(-10))


