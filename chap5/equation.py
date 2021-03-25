#coding:utf-8

'''
    filename:equation.py
        chap:5
    subject:15
    conditions:a,b,c
    solution:Quadratic equation of one variable
'''




x = eval(input('Enter the value of x:'))


a,b,c = 2,7,5

def equation(a,b,c):
    def inner(x):
        y = a*x**2 + b*x + c
        #print(locals())
        return 'result of y = {a}*x^2 + {b}*x + {c} ,x={x},y={y}'.format(**locals())
    return inner


f = equation(a,b,c)
print(f(x))



