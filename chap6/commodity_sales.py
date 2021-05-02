#coding:utf-8

'''
    filename:commodity_sales.py
        chap:6
    subject:11
    conditions:sold_num,retail_price,wholesale_discount,wholesale_min,
                method [total_sales,gross_sales]
    solution:class CommoditySales
'''

class CommoditySales:
    def __init__(self,retail_price,wholesale_discount,wholesale_min):
        self._retail_price = retail_price
        self._wholesale_min = wholesale_min
        self._wholesale_discount = wholesale_discount
        self._wholesale_price = self._retail_price * (1-self._wholesale_discount)
        # price:sold_number
        self._sold_dict = {self._retail_price:0,self._wholesale_price:0}
    def gross_sales(self):
        '''Get gross sales of *THIS* commodity'''
        return sum(price*number for price,number in self._sold_dict.items())
    def total_sales(self):
        '''Get total sales number of *THIS* commdity'''
        return sum(self._sold_dict.values())
    def sale(self,number):
        '''Number muse GT 0.
        if number GE wholesale_min,sale with price wholesale_price ,
        otherwise,retail_price
        '''
        if 0< number < self._wholesale_min:
            self._sold_dict[self._retail_price]+=number
            return self._retail_price
        elif number >= self._wholesale_min:
            self._sold_dict[self._wholesale_price]+=number
            return self._wholesale_price
        else:
            return f'sale number {number} must > 0 !'
#        return f'sale {number} more.'




if __name__ == '__main__':
    apple = CommoditySales(3,.2,10)
    apple.sale(7)
    apple.sale(15)
    print(apple.total_sales())
    print(apple.gross_sales())
    print(apple._sold_dict)

