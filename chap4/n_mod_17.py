#coding:utf-8

'''
    filename:n_mod_17.py
        chap:4
    subject:5
    conditions: mod_number
    solution:numbers mod mod_number == 0;100 <= numbers <=999
'''

mod_number = 17
mod_range = [100,999]

# for...in 
result = []
for i in range(min(mod_range),max(mod_range)+1):
    if not i%mod_number:
        result.append(i)
print('numbers in range [{},{}],which is multiple of {} ,are {}'.format(
        min(mod_range),
        max(mod_range),
        mod_number,
        result)
        )

# list comprehension
result = [i for i in range(min(mod_range),max(mod_range)+1) if not i%mod_number]
print('numbers in range [{},{}],which is multiple of {} ,are {}'.format(
        min(mod_range),
        max(mod_range),
        mod_number,
        result)
        )
