
#coding=utf-8

'''
    filename:caesar_cipher.py
    chap:3
    subject:30
    conditions:plainText,offset
    solution:cipherText
'''


offset  = int(input("\nPlease enter the offset : ") )
plainText = input("\nPlease enter the plainText : \n") 
cipherlist = []

lower = [chr(i) for i in range(ord('a'),ord('z')+1)]
upper = [chr(i) for i in range(ord('A'),ord('Z')+1)]
number = [str(i) for i in range(10)]
chars = lower + upper + number
nums = [i for i in range(len(chars))]
c2n = dict(zip(chars,nums))
n2c = dict(zip(nums,chars))

for i in plainText:
    if i not in chars:continue
    plainval = c2n.setdefault(i)
    cipherval = (plainval + offset) % len(chars)
    cipherchar= n2c.setdefault(cipherval)
    cipherlist.append(cipherchar)
#print(cipherlist)
cipherText = ''.join(cipherlist)

message ="""The cipherText is : 
{0}""".format(cipherText)

print(message)
