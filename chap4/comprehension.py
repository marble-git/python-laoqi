#coding:utf-8

'''
    filename:comprehension.py
        chap:4
    subject:18
    conditions:
    solution:
'''

#找出[2,4,-7,19,-2,-1,45]中小于0的数
lst = [2,4,-7,19,-2,-1,45]
print([i for i in lst if i<0])


#找出{'python':89,'java':58,'physics':65,'math':87,'chinese':74,'english':60}大于平均分的学科
scores = {'python':89,'java':58,'physics':65,'math':87,'chinese':74,'english':60}
print([k for k,v in scores.items() if v>sum(scores.values())/len(scores)])

#计算1到100的整数平方的和

print(sum([i**2 for i in range(1,101)]))

s=0
i = 1
while i<=100:
    s+=i**2
    i+=1

print(s)
