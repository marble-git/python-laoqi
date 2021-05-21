## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------


## 8.4 自定义异常类型

+ 异常处理: 是编程语言或计算机硬件里的一种机制，
+ 用于处理软件或者信息系统中出现的异常状况(即超出程序正常执行流程的某些特殊条件)
+ 通过异常处理，可以对用户在程序中的非法输入进行控制和提示，以防程序崩溃
+ 各种异常其实也是对象，所以可以使用 **类** 的知识自定义异常类型
+ `exception Exception`
	- 所有内置的非系统退出类异常都派生自此类。 所有用户自定义异常也应当派生自此类。

+ [Python官方教程8.6. 用户自定义异常¶](https://docs.python.org/zh-cn/3.9/tutorial/errors.html#user-defined-exceptions)
	- 程序可以通过创建新的异常类命名自己的异常（Python 类的内容详见 类）。不论是以直接还是间接的方式，异常都应从 Exception 类派生。
	- 异常类和其他类一样，可以执行任何操作。但通常会比较简单，只提供让处理异常的程序提取错误信息的一些属性。创建能触发多个不同错误的模块时，一般只为该模块定义异常基类，然后再根据不同的错误条件，创建指定异常类的子类
	- 大多数异常命名都以 “Error” 结尾，类似标准异常的命名。
	- 许多标准模块都需要自定义异常，以报告由其定义的函数中出现的错误。有关类的说明，详见 类。



```python
#coding:utf-8

'''
    filename:custom_exception.py
    judge the number of age is even or odd
'''

class NegativeAgeException(RuntimeError):
    def __init__(self,age):
        super().__init__()
        self.age = age

def enterage(age):
    if age<0:
        raise NegativeAgeException('Only *POSITIVE* integers are allowed')
    if age%2==0:
        print('age is even')
    else:
        print("age is odd")


try:
    age = int(input('Enter your age : '))
    enterage(age)
except NegativeAgeException as error:
    print('error: ',error)
    print('error.age: ',error.age)
    print('Only *INTEGERS* are allowed')
except :
    print('something is wrong')


[output]
root@kali-book:~/python-laoqi/chap8# python3 custom_exception.py 
Enter your age : 3
age is odd
root@kali-book:~/python-laoqi/chap8# python3 custom_exception.py 
Enter your age : 4
age is even
root@kali-book:~/python-laoqi/chap8# python3 custom_exception.py 
Enter your age : -34
error:  
error.age:  Only *POSITIVE* integers are allowed
Only *INTEGERS* are allowed
root@kali-book:~/python-laoqi/chap8# python3 custom_exception.py 
Enter your age : rf
something is wrong
```





-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
