#coding:utf-8

'''
    filename:books.py
    The total price of books and delivery.
'''




class Books:
    prices = {'A':45.7,'B':56.7,'C':67.8,'D':78.9,'E':90.1}
    shipping = 5    #delivery price
    def __init__(self,book_name,book_number,free_ship:"min book cost of free ship"):
        self.book_name = book_name
        self.book_number = book_number
        self.free_ship = free_ship

    def totals(self):
        price = Books.prices.get(self.book_name)
        if price:
            t = price * self.book_number
            return (t + Books.shipping) if t<self.free_ship else t
        return "No this book"


book_a = Books('A',2,100)
book_b = Books('B',4,200)
book_n = Books('N',5,1)

a_total = book_a.totals()
b_total = book_b.totals()
n_total = book_n.totals()

print(f'book {book_a.book_name} : {a_total}')
print(f'book {book_b.book_name} : {b_total}')
print(f'book {book_n.book_name} : {n_total}')





