#coding:utf-8

'''
    filename:peach.py
        chap:4
    subject:16
    conditions:f(n)=n/2-1 ,f(n)=1
    solution:n
'''


times = 9
peaches = 1

for i in range(times):
    peaches = (peaches+1)*2

print(f'The sum of peaches is {peaches}')


#for i in range(times):
#    peaches = peaches/2 -1
#
#print(peaches)
