#coding:utf-8

'''
    filename:find_words_2.py
        chap:5
    subject:14
    conditions:text
    solution:words contain a,e,i,o,u
    函数：判断string1是否含有string2中的字母
'''


text = '''
Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see http://www.opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit: 
releases have also been GPL-compatible; the table below summarizes
the various releases.
'''

import re

#word_list = text.split()
word_list = re.split(r'\W+',text)
word_list = list(filter(None,word_list))
#print(word_list)




def isvowel_word(word):
    '''使用set判断'''

    #vowels = 'aeiou'
    #for i in vowels:
    #    if i in word:
    #        return True
    #return False

    vowels = set('aeiou')
    if vowels.intersection(set(word)):
        return True
    else:
        return False







vowel_words = list(filter(isvowel_word,word_list))
print(f'word_counts: {len(word_list)} word_list:',word_list)
print(f'vowel_word_counts: {len(vowel_words)} vowel_word_list:',vowel_words)











