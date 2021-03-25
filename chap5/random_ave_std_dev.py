#coding:utf-8

'''
    filename:random_ave_std_dev.py
        chap:5
    subject:9
    conditions:random.randint(0,100) range(10000)
    solution:average standard_deviation
'''






import random
import average_std_deviation as ad




numbers = [random.randint(0,100) for i in range(10000)]

print('numbers average:',ad.average(numbers))
print('numbers std_deviation:',ad.std_deviation(numbers))





