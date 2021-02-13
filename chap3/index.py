#coding=utf-8

'''
    filename:index.py
    chap:3
    subject:19
    conditions:target_string='Hello',char='l'
    solution:indexs of char in target_string
'''

target_string = 'Hello'
char = 'l'
result = []

start = 0
while True:
    start = target_string.find(char,start)
    if start == -1: break
    result.append(start)
    start += 1



message = """
The index(s) of char '{0}' in target_string '{1}' are : {2}
""".format(char,target_string,result)

print(message)

