#coding:utf-8
'''
your name and age.
'''

name = input('your name: ')
age = input('your age: ')

after = int(age) + 10   #变量age引用字符串类型的对象，类型转换后才能参与运算

print('your name is: ',name)
#print('after ten years, you are ',after)

print('you are ' + age + ' years old.')

print('you will be ' +  str(after) + ' years old after ten years.') #整数 after 通过+ 号与字符串连接时，要转化为字符串类型.

