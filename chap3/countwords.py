
#coding=utf-8

'''
    filename:countwords.py
    chap:3
    subject:36
    conditions:textstring
    solution:words's times
'''

import re
text = '''You raise me up,so I can stand on mountains
You raise me up to walk on stromy seas
I am strong when I am on your shoulders
You raise me up to more than I can be'''

#words = text.split(' ')
#word_counts = {word_counts[i] +=1 if i in word_counts else word_counts[i] = 1 for i in words }
# ??????

words = re.split(r'\W+',text)


word_counts = {}
for i in words:
    if i in word_counts:
        word_counts[i] += 1
    else:
        word_counts[i] = 1


message = '''The dict of everyword and it's count is
{0}'''.format(word_counts)

print(message)

