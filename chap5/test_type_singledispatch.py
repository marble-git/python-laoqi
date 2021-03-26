#coding:utf-8

'''
    filename:test_type_singledispatch.py
        chap:5
    subject:21
    conditions:obj
    solution:obj's type
'''



from functools import singledispatch



@singledispatch
def determine_type(obj):
    '''Determine which built-in type the object belongs to
    '''
    print(obj,type(obj),' is not a built-in type.')
    return False

@determine_type.register(int)
def d_int(obj):
    print(obj,'is <int> type.')
    return True
@determine_type.register(float)
def d_float(obj):
    print(obj,'is <float> type.')
    return True
@determine_type.register(str)
def d_str(obj):
    print(obj,'is <str> type.')
    return True
@determine_type.register(list)
def d_list(obj):
    print(obj,'is <list> type.')
    return True
@determine_type.register(tuple)
def d_tuple(obj):
    print(obj,'is <tuple> type.')
    return True
@determine_type.register(dict)
def d_dict(obj):
    print(obj,'is <dict> type.')
    return True
@determine_type.register(set)
def d_set(obj):
    print(obj,'is <set> type.')
    return True



print('registry:',determine_type.registry)


ins = [11,'string',[],(),{},{1,2,3},zip('abc','123')]

for i in ins:
    print(i,determine_type(i))
