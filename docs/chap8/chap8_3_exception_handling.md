## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------


## 8.3 异常处理

+ `try` 语句可为一组语句指定异常处理器和/或清理代码:


```pybnf
try_stmt  ::=  try1_stmt | try2_stmt
try1_stmt ::=  "try" ":" suite
               ("except" [expression ["as" identifier]] ":" suite)+
               ["else" ":" suite]
               ["finally" ":" suite]
try2_stmt ::=  "try" ":" suite
               "finally" ":" suite
```



+ 稳健性(robust):如果在程序运行过程中抛出异常，程序就会终止运行，这样的程序是不稳健的
+ 稳健性强的程序应该是不为各种异常所击倒，所以要在程序中对异常进行处理


+ `try...except...` 是常用的异常处理语句

```
>>> while True:
...     try:
...             n = int(input('Enter an integer: '))
...             print(n)
...             break
...     except :
...             print('Try again!')
... 
Enter an integer: w
Try again!
Enter an integer: af
Try again!
Enter an integer: 0xa
Try again!
Enter an integer: 3e
Try again!
Enter an integer: 8
8
```

+ 应该明确：对于`try...except...`语句，try分支下是要执行的语句，except则是异常处理语句，上例没有规定要捕获的异常类型(BaseException)

+ 函数`eval()`:能实现对字符串形式的表达式进行计算
+ 在编程实践中，不提倡except后面不声明异常类型的做法;不要在一个处理异常的分支中包含太多异常处理
+ 在except分支明确了要处理的异常类型，其他异常类型在该except分支就不做处理了

```
#!/bin/python3
#coding:utf-8

'''
    filename:test.py
        chap:8
'''

import sys


class Calculator:
    is_raise = False
    def clac(self,expression):
        try:
            return eval(expression)
        except ZeroDivisionError:
            if self.is_raise:
                raise 
            else:
                return 'zero cannot be divided.'

if __name__ == '__main__':
    c = Calculator()
    print(c.clac('3+5'))
    print(c.clac('8/0'))
    print('-'*60)

    c.is_raise = True
    print(c.clac('2/0.0'))

root@kali-book:~/python-laoqi/chap8# ./test.py 
8
zero cannot be divided.
------------------------------------------------------------
Traceback (most recent call last):
  File "/root/python-laoqi/chap8/./test.py", line 61, in <module>
    print(c.clac('2/0.0'))
  File "/root/python-laoqi/chap8/./test.py", line 47, in clac
    return eval(expression)
  File "<string>", line 1, in <module>
ZeroDivisionError: float division by zero
```

+ [`raise` 语句](https://docs.python.org/zh-cn/3.9/reference/simple_stmts.html#the-raise-statement)

```pybnf
raise_stmt ::=  "raise" [expression ["from" expression]]
```

+ 如果不带表达式，raise 会重新引发当前作用域内最后一个激活的异常。 如果当前作用域内没有激活的异常，将会引发 RuntimeError 来提示错误。

```
>>> raise 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: No active exception to reraise
```

+ 否则的话，raise 会将第一个表达式求值为异常对象。 它必须为 BaseException 的子类或实例。 如果它是一个类，当需要时会通过不带参数地实例化该类来获得异常的实例。

```
>>> class MyException(BaseException):
...     def __init__(self,*args,**kwargs):
...             print('args : ',args)
...             print('kwargs : ',kwargs)
...             super().__init__(*args,**kwargs)
... 
>>> raise MyException(123,'abc',a=1,b=2)
args :  (123, 'abc')
kwargs :  {'a': 1, 'b': 2}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in __init__
TypeError: MyException() takes no keyword arguments
>>> raise MyException
args :  ()
kwargs :  {}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyException
>>> help(MyException)

>>> raise BaseException(123,'abc',a=1,b=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: BaseException() takes no keyword arguments
```


+ `异常`的 `类型` 为 **异常实例的类** ，`值` 为 **实例本身**

+ `from` 子句用于 **异常串连** ：如果有该子句，则 ***第二个 表达式 必须为另一个异常或实例*** ，它将作为可写的 `__cause__` 属性被关联到所引发的异常。 如果引发的异常未被处理，两个异常都将被打印出来:

+ 如果一个异常在`异常处理器`或 `finally clause`: 中被引发，类似的机制会隐式地发挥作用，之前的异常将被关联到新异常的 `__context__` 属性

+ 异常串连可通过在 from 子句中指定 None 来显式地加以抑制



+ `try...except...`是处理异常的基本方式，在此基础上还可有扩展，能够处理多个异常
	- 处理多个异常不是因为同时报出多个异常
	- 程序运行中，只要遇到一个异常就会有反应，所以每次捕获到的异常一定是一个
	- 所谓处理多个异常，即捕获不同的异常，由不同的`except`子句处理


```python
#coding:utf-8

'''
    filename:mul_exceptions.py
    handling multiple exceptions.
'''

while True:
    try:
        a = float(input('First number : '))
        b = float(input('Second number : '))
        r = a/b
        print('{} / {} = {}'.format(a,b,r))
        break
    except ZeroDivisionError:
        print('The second number cannot be zero. Try again')
    except ValueError:
        print('Please enter number.Try again')
#    except (ValueError,ZeroDivisionError)
#        print('Try again!')
    except :
        break

[out:]
root@kali-book:~/python-laoqi/chap8# python3 mul_exceptions.py 
First number : 4 
Second number : 0
The second number cannot be zero. Try again
First number : e
Please enter number.Try again
First number : 2
Second number : 3
2.0 / 3.0 = 0.6666666666666666
```


+ except 后面不仅 **可以放1个异常类型的名称** ，还可以放 **多个**
	- **注意** : except 后面的多个参数，一定要用`圆括号()`包裹起来
+ `except...as...`:可以将所捕获的异常命名，方便提取有用的异常信息


```python


#coding:utf-8

'''
    filename:mul_exceptions.py
    handling multiple exceptions.
'''

while True:
    try:
        a = float(input('First number : '))
        b = float(input('Second number : '))
        r = a/b
        print('{} / {} = {}'.format(a,b,r))
        break
#    except ZeroDivisionError:
#        print('The second number cannot be zero. Try again')
#    except ValueError:
#        print('Please enter number.Try again')
    except (ValueError,ZeroDivisionError) as e:
        print(e)
        print('Try again')
    except :
        break


root@kali-book:~/python-laoqi/chap8# python3 mul_exceptions.py 
First number : 3
Second number : 0
float division by zero
Try again
First number : e
could not convert string to float: 'e'
Try again
First number : 2
Second number : 4
2.0 / 4.0 = 0.5
```


+ `try...except...else...`: 可选的`else分支`，放在所有`except`的后面，当没有异常的时候执行else分支下的语句块
	- 如果控制流离开 try 子句体时没有引发异常，
	- 并且没有执行 return, continue 或 break 语句，
	- 可选的 else 子句将被执行。 
	- else 语句中的异常不会由之前的 except 子句处理。
+ `try...except...else...finally...`: 不管前面执行了哪个分支，最后都要执行`finally分支`
	- 如果存在 finally，它将指定一个‘清理’处理程序。
	- try 子句会被执行，包括任何 except 和 else 子句。 
	- 如果在这些子句中发生任何未处理的异常，该异常会被临时保存。 
	- finally 子句将被执行。 
	- 如果存在被保存的异常，它会在 finally 子句的末尾被重新引发。 
	- 如果 finally 子句引发了另一个异常，被保存的异常会被设为新异常的上下文。 
	- 如果 finally 子句执行了 return, break 或 continue 语句，
	- 则被保存的异常会被丢弃
	- 在 finally 子句执行期间，程序不能获取异常信息。

+ 当 return, break 或 continue 语句在一个 try...finally 语句的 try 子语句体中被执行时，finally 子语句也会‘在离开时’被执行。
	- 函数的返回值是由最后被执行的 return 语句所决定的。 
	- 由于 finally 子句总是被执行，
	- 因此在 finally 子句中被执行的 return 语句总是最后被执行的

```
>>> def foo():
...     try:
...             print('try')
...             int(input())
...     except ValueError:
...             print('except')
...     else:
...             print('else')
...     finally:
...             print('finally')
... 
>>> foo()
try
23
else
finally
>>> foo()
try
e
except
finally
>>> def bar():
...     try:
...             1/0
...     finally:
...             return 234
... 
>>> bar()
234
>>> try:
...     1/0
... finally:
...     print('passp')
... 
passp
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero
>>> try:
...     1/0
... finally:
...     int('abc')
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
>>> def baz():
...     try:
...             return 'try'
...     finally:
...             return 'finally'
... 
>>> baz()
'finally'
```

+ `raise`: 在程序中，除了使用`try...except...`处理异常，有时需要主动抛出异常
+ `raise`可以抛出指定类型的异常，以及相应的提示语句
+ `raise X from Y`: from 子句用于异常串连

```
如果有该子句，则第二个 表达式 必须为另一个异常或实例，它将作为可写的 __cause__ 属性被关联到所引发的异常。 如果引发的异常未被处理，两个异常都将被打印出来
如果一个异常在异常处理器或 finally clause: 中被引发，类似的机制会隐式地发挥作用，之前的异常将被关联到新异常的 __context__ 属性
异常串连可通过在 from 子句中指定 None 来显式地加以抑制
```


```
#coding:utf-8

'''
    filename:raise_age.py
    judge the number of age is even or odd.
'''


def enterAge(age):
    if age <0:
        raise ValueError('Only *POSITIVE* integers are allowed')
    if age%2 == 0:
        print('age is even')
    else:
        print('age is odd')


try:
    num = int(input('Enter your age: '))
    enterAge(num)
except ValueError as e:
    print(e)
    print('Only *INTEGERS* are allowed')
except :
    print('Something is wrong')




[out]
root@kali-book:~/python-laoqi/chap8# python3 raise_age.py 
Enter your age: php
invalid literal for int() with base 10: 'php'
Only *INTEGERS* are allowed
root@kali-book:~/python-laoqi/chap8# python3 raise_age.py 
Enter your age: 11
age is odd
root@kali-book:~/python-laoqi/chap8# python3 raise_age.py 
Enter your age: 12
age is even
root@kali-book:~/python-laoqi/chap8# python3 raise_age.py 
Enter your age: -22
Only *POSITIVE* integers are allowed
Only *INTEGERS* are allowed
root@kali-book:~/python-laoqi/
```


+ `assert`: Python中以条件判断为基础的异常抛出，的另一种处理方式

+ assert 语句是在程序中插入调试性断言的简便方式:

```pybnf
assert_stmt ::=  "assert" expression ["," expression]
```

+ 简单形式 `assert expression` 等价于

```python
if __debug__:
    if not expression: raise AssertionError
```

+ 扩展形式 `assert expression1, expression2` 等价于

```python
if __debug__:
    if not expression1: raise AssertionError(expression2)
```

+ 以上等价形式假定 `__debug__` 和 `AssertionError` 指向具有指定名称的内置变量。
+ 在当前实现中，内置变量 `__debug__` 在正常情况下为 True，
+ 在请求优化时为 False (对应命令行选项为 -O)。
+ 如果在编译时请求优化，当前代码生成器不会为 assert 语句发出任何代码。
+ 请注意不必在错误信息中包含失败表达式的源代码；它会被作为栈追踪的一部分被显示。

+ 赋值给 `__debug__` 是非法的。 该内置变量的值会在解释器启动时确定。


```
>>> raise AssertionError('df')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: df
>>> assert 'df'
>>> assert False,'df'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: df
>>> __debug__
True
>>> __debug__ = False
  File "<stdin>", line 1
SyntaxError: cannot assign to __debug__
>>> def year(y):
...     assert y>0,'year must *GE* 0 .'
...     return str(y)+'year'
... 
>>> year(2021)
'2021year'
>>> year(-2021)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in year
AssertionError: year must *GE* 0 .
```





-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
