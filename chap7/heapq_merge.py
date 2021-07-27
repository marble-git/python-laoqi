#coding:utf-8

'''
    filename:heapq_merge.py
        chap:7
    subject:4-2
    conditions:heapq.merge,sorted_list:lst1,lst2
            lst3=merged_list(lst1,lst2) is sorted
    solution:heapq.merge
'''

import heapq


lst1 = [1,3,5,7,9]
lst2 = [2,4,6,8]




if __name__ == '__main__':
    lst3 = heapq.merge(lst1,lst2)
    print('lst3',lst3)
    print(list(lst3))
