#coding:utf-8

'''
    filename:heap_sort_key.py
        chap:7
    subject:6-1
    conditions:books_price,heapq,operator.itemgetter
    solution:fun heapsort
'''


import heapq
import operator
from pprint import pprint


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

def heapsort(iterable,/,*,key=None,reverse=False):
    sortfunc = heapq.nlargest if reverse else heapq.nsmallest
    return sortfunc(len(iterable),iterable,key = key)


if __name__ == '__main__':
    by_book = heapsort(books_price,key=operator.itemgetter('book'))
    print('print:',by_book)
    pprint(by_book,indent=4,depth=2)
