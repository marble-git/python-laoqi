#coding:utf-8

'''
    filename:vowel_counts.py
        chap:4
    subject:9
    conditions:chap3_35 string
    solution:count a,e,i,o,u 
'''


text = '''You raise me up,so I can stand on mountains
You raise me up to walk on stromy seas
I am strong when I am on your shoulders
You raise me up to more than I can be'''

vowels = ('a','e','i','o','u')
result = dict.fromkeys(vowels,0)
for char in text:
    if char in result.keys():
        result[char] +=1
print(f'Vowel_counts :{result}')


rst = {char:text.count(char) for char in vowels} 
print(f'Vowel_counts :{rst}')
