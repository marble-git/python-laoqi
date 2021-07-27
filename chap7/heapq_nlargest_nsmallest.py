#coding:utf-8

'''
    filename:heapq_nlargest_nsmallest.py
        chap:7
    subject:4-1
    conditions:heapq,a_list,nlargest(3,a_list),nsmallest(3,a_list)
    solution:heapq.n{largest,smallest}
'''

import heapq


lst = [38,45,19,9,-12,3,97,79,199,20,-49]




if __name__ == '__main__':
    largest3 = heapq.nlargest(3,lst)
    smallest3 = heapq.nsmallest(3,lst)
    print('largest3',largest3)
    print('smallest3',smallest3)
