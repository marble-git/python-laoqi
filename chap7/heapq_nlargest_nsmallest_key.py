#coding:utf-8

'''
    filename:heapq_nlargest_nsmallest_key.py
        chap:7
    subject:4-3
    conditions:heapq.nlargest(n, iterable, key=None)
                heapq.nsmallest(n, iterable, key=None)
                books_price = [
                                {'book':bookname,'price':price} # entrys
                                ]
    solution:heapq
'''

import heapq
import operator


books_price = [
        {'book':'Python', 'price':69.99},
        {'book':'Java', 'price':59.99},
        {'book':'Rust', 'price':79.99},
        {'book':'JavaScript', 'price':49.99},
        {'book':'C++','price':89.99},
        {'book':'Ruby', 'price':39.99},
        {'book':'hadoop', 'price':99.99},
        {'book':'HTML5', 'price':29.99},
        ]



if __name__ == '__main__':
    hprice2 = heapq.nlargest(2,books_price,key=operator.itemgetter('price'))
    lprice2 = heapq.nsmallest(2,books_price,key=operator.itemgetter('price'))
    print('lprice2',lprice2)
    print('hprice2',hprice2)
