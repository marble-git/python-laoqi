
#coding=utf-8

'''
    filename:number2english.py
    chap:3
    subject:34
    conditions:number
    solution:english
'''

number = input("Please enter the number : ")
number = number.lstrip('0')
english = ''
rstlist = []

num = [str(i) for i in range(10)]
eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
table = dict(zip(num,eng))

for i in number:
    rstlist.append(table[i])

english = ' '.join(rstlist)

message = '''The number in english is :
{0}'''.format(english)

print(message)


