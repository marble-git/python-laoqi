#coding:utf-8

'''
    filename:pandas_excel.py
        chap:4
    subject:14
    conditions:'分省月度数据.xls'
    solution:dict,average,above average
'''



import pandas as pd


fname = '分省月度数据.xls'
df = pd.read_excel(fname)
data = dict(df.iloc[3:34,[0,2]].values)

print(data)

average = sum(data.values())/len(data)

print(f'全国价格指数 2021年1月 的平均值为 {average}')

above_average = {key:value for key,value in data.items() if value > average}

print(f'高于平均值的省市和其价格指数分别为{above_average}')
