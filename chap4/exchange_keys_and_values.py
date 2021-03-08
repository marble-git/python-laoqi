#coding:utf-8

'''
    filename:exchange_keys_and_values.py
        chap:4
    subject:10
    conditions:a dict
    solution:exchanged keys and values
'''


origin_dict = {'book':['python','djang','data'],'author':'laoqi','publisher':'phei'}


def ishashable(obj):
    try:
        hash(obj)
        return True
    except:
        return False

xchange_dict = {}
for key,value in origin_dict.items():
    if ishashable(value):
        xchange_dict.update({value:key})
    else:
        for v in value:
            xchange_dict.update({v:key})





print(f'''origin_dict : {origin_dict}
xchange_dict{xchange_dict}''')
