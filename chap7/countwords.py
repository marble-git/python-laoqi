#coding:utf-8

'''
    filename:countwords.py
        chap:7
    subject:5
    conditions:chap3-36,dict of word_counts
    solution:统计出现频率最高的3个单词
'''


import re
import heapq
import operator




text = '''You raise me up,so I can stand on mountains
You raise me up to walk on stromy seas
I am strong when I am on your shoulders
You raise me up to more than I can be'''





def countwords(text):
    words = re.split(r'\W+',text)
#    print('length',len(words))
    word_counts = {}
#    print('words',words)
#    for i in words:
#        if i in word_counts:
#            word_counts[i] += 1
#        else:
#            word_counts[i] = 1
    for word in set(words):
        word_counts[word]=words.count(word)
    return word_counts

if __name__ == '__main__':
    d = countwords(text)
#    print(d)
#    print('sum_len',sum(d.values()))
    hfreq3 = heapq.nlargest(3,d.items(),key=operator.itemgetter(1))
    print('most 3 frequent words are:',hfreq3)





