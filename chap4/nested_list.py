#coding:utf-8

'''
    filename:nested_list.py
        chap:4
    subject:19
    conditions:nested list
    solution:remove the second column
'''

import copy

nested_list = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]


print(nested_list)

rst1 = copy.deepcopy(nested_list)
for index,sub_list in enumerate(rst1):
    sub_list.pop(1)

print('deepcopy for: ',nested_list,rst1,sep='\n')










