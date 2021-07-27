#coding:utf-8

'''
    filename:exit_program.py
    sys.exit() exit from the program.
'''


print('file start pos')
import sys

n = 10

while n >0:
    n-=1
    if n==5:
        #sys.exit()
        break
    else:
        print(n)

print('file end pos')


"""
#        sys.exit()
root@kali-book:~/python-laoqi/docs/chap7/code# python3 exit_program.py
file start pos
9
8
7
6
root@kali-book:~/python-laoqi/docs/chap7/code# vim exit_program.py

#        break
root@kali-book:~/python-laoqi/docs/chap7/code# python3 exit_program.py
file start pos
9
8
7
6
file end pos
"""
