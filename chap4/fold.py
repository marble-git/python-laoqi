#coding:utf-8

'''
    filename:fold.py
        chap:4
    subject:13
    conditions:fold paper
    solution:thickness
'''


fold_times = 30
paper_thickness = 2e-4
rst_thickness = 1

for i in range(fold_times):
    rst_thickness *=2
rst_thickness *= paper_thickness
print(f'After {fold_times} folded,the thickness is {rst_thickness:e}m')


rst_thickness = paper_thickness * pow(2,fold_times)
print(f'After {fold_times} folded,the thickness is {rst_thickness:e}m')

