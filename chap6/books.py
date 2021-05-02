#coding:utf-8

'''
    filename:books.py
        chap:6
    subject:4
    conditions:在6.3.1基础上，快递费按距离远近划分为
    [包邮区，一类地区，二类地区，特远地区]
    据此修改 totals方法
    solution:class Books
'''




class Books:
    prices = {'A':45.7,'B':56.7,'C':67.8,'D':78.9,'E':90.1}
    shipping_dict = {'free':0,'near':5,'far':10,'realyfar':20}
    def __init__(self,book_name,book_number,distance):
        self.book_name = book_name
        self.book_number = book_number
        self.shipping = self.get_shipping(distance)

    @classmethod
    def get_shipping(cls,distance):
        if 0< distance <=100:
            area = 'free'
        elif 100<distance<=500:
            area = 'near'
        elif 500<distance<=1000:
            area = 'far'
        elif distance > 1000:
            area = 'realyfar'
        else:
            raise ValueError('distance {} must > 0'.format(distance))
        return cls.shipping_dict[area]

    def totals(self):
        price = Books.prices.get(self.book_name)
        if price:
            t = price * self.book_number
            return t+self.shipping
        return "No this book"


books = [Books('A',2,100),Books('B',4,600),Books('N',5,1)]

print(r'bookname |booknum |price |shipping |total')
for book in books:
    print('{:9}|{:8}|{:6}|{:9}|{}'.format(book.book_name,book.book_number,book.totals()-book.shipping,book.shipping,book.totals()))









