#coding:utf-8

'''
    filename:speech.py
        chap:5
    subject:7
    conditions:speech_text
    solution:non_repeat_words,sorted by counts
'''

import re
import operator


speech_text='''Four score and seven years ago our fathers brought forth upon this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate—we can not consecrate—we can not hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom—and that government of the people, by the people, for the people, shall not perish from the earth.
—Abraham Lincoln'''


def non_repeat(text:str)->'set of non repeat words':
    word_list = re.split(r'\W+',text)
    non_repeat_word = set(word_list)
    return non_repeat_word



def non_repeat_sorted_reverse(text:str)->'dict of word:counts sorted by counts in reverse':
    word_list = re.split(r'\W+',text)
    non_repeat_word = set(word_list)
    word_dict = {key:word_list.count(key) for key in non_repeat_word}
    word_dict = dict(sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True))
    return word_dict



non_repeat_set = non_repeat(speech_text)
non_repeat_dict_sorted = non_repeat_sorted_reverse(speech_text)
print('non_repeat words:',non_repeat_set)
print('dict of non_repeat_words sorted by count in reverse',non_repeat_dict_sorted)


