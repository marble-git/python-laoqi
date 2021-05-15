#coding:utf-8

'''
    filename:heap_sort_key2.py
        chap:7
    subject:6-2
    conditions:class User,heapsort,operator
    solution:operator.attrgetter
'''


import heapq
import operator
from pprint import pprint


class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return "User({0})".format(self.user_id)


def heapsort(iterable,/,*,key=None,reverse=False):
    sortfunc = heapq.nlargest if reverse else heapq.nsmallest
    return sortfunc(len(iterable),iterable,key = key)

if __name__ == '__main__':
    users = [User(2), User(11),User(3),User(9)]
    sorted_users = heapsort(users,key= operator.attrgetter('user_id'))
    print(sorted_users)
    pprint(sorted_users)

