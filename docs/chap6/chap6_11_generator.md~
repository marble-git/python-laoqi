## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------


## 6.11 生成器



+ generator -- 生成器
	- 返回一个 generator iterator 的函数。它看起来很像普通函数，不同点在于其包含 yield 表达式以便产生一系列值供给 for-循环使用或是通过 next() 函数逐一获取。
	- 通常是指生成器函数，但在某些情况下也可能是指 生成器迭代器。如果需要清楚表达具体含义，请使用全称以避免歧义。

+ generator iterator -- 生成器迭代器:generator 函数所创建的对象。
	-  每个 yield 会临时暂停处理，记住当前位置执行状态（包括局部变量和挂起的 try 语句）。当该 生成器迭代器 恢复时，它会从离开位置继续执行（这与每次调用都从新开始的普通函数差别很大）。

+ generator expression -- 生成器表达式
	- 返回一个迭代器的表达式。 它看起来很像普通表达式后面带有定义了一个循环变量、范围的 for 子句，以及一个可选的 if 子句。 以下复合表达式会为外层函数生成一系列值:

```doctest
>>> sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81
285
```

+ 生成器(generator):包含yield关键字的函数，或使用圆括号`()`的推导式comprehension
+ 生成器对象是迭代器

```doctest
>>> def  g():
...     yield 0
...     yield 1
...     yield 2
... 
>>> ge = g()
>>> g
<function g at 0x7f06dd3a1a60>
>>> ge
<generator object g at 0x7f06dd40c5f0>
>>> type(ge)
<class 'generator'>
>>> import collections.abc as ca
>>> isinstance(ge,ca.Iterator)
True
>>> dir(ge)
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
```



+ 生成器函数的执行过程

```doctest
>>> def y(n):
...     print('init y generator obj')
...     while n>0:
...             print('before yield ')
...             yield n
...             n-=1
...             print('after yield ')
... 
>>> yy = y(3)	#调用生成器函数获得生成器时,函数体内的语句没有执行
>>> next(yy)
init y generator obj	#第一次调用next()函数时才开始执行生成器函数内的语句
before yield 
3
>>> next(yy)
after yield 		#生成器函数被挂起然后恢复执行，并不是和return一样直接退出
before yield 
2
>>> next(yy)
after yield 
before yield 
1
>>> next(yy)
after yield 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

+ 生成器解析:

```doctest
>>> gt = (x**2 for x in range(7))
>>> gt
<generator object <genexpr> at 0x7f06dd40c6d0>
>>> type(gt)
<class 'generator'>
>>> next(gt)
0
>>> next(gt)
1
>>> next(gt)
4
>>> next(gt)
9
>>> next(gt)
16
>>> for i in gt:
...     print(i)
... 
25
36
>>> 
```

+ `yield from`: 生成器函数需要产出另一个生成器的值
+ [PEP 380-委托给子生成器的语法/PEP 380 -- Syntax for Delegating to a Subgenerator](https://www.python.org/dev/peps/pep-0380/)

```
#传统解决方案，使用for循环
>>> def chain(*iterables):
...     for it in iterables:
...             for i in it:
...                     yield i
... 
>>> s
'abc'
>>> lst
['A', 1, (2, 'Z')]
>>> t
(11, 22)
>>> c = chain(s,lst,t)
>>> c
<generator object chain at 0x7f06dd146c80>
>>> list(c)
['a', 'b', 'c', 'A', 1, (2, 'Z'), 11, 22]
#使用`yield from`完全代替内层的for循环
>>> def y_chain(*iterables):
...             for i in iterables:
...                     yield from i
>>> y_c = y_chain(s,lst,t)
>>> y_c
<generator object y_chain at 0x7f06dd146cf0>
>>> list(y_c)
['a', 'b', 'c', 'A', 1, (2, 'Z'), 11, 22]
>>> 
```



-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap6.md
[pre_chap]: chap6_10_iterator.md
[next_chap]: chap6_12_metaclass.md
