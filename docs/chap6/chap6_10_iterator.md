## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 6.10 迭代器

+ 可迭代的(Iterable):使用iter内置函数可以获取迭代器的对象; 如果对象实现了能返回迭代器的`__iter__`方法，那么对象就是可迭代的;序列都可以迭代;实现了`__getitem__`方法，而且其参数是从零开始的索引，这种对象也可以迭代
+ ***可迭代的对象一定不能是自身的迭代器:即，可迭代的对象必须实现`__iter__`方法，但不能实现`__next__`方法***

+ ***另一方面,迭代器应该一直可以迭代,迭代器的`__iter__`方法应该返回自身(self)***  `--<fluent python> p339`

+ 可迭代的对象与迭代器的关系:Python 从可迭代的对象中获取迭代器

+ 相关模块:dis,itertools
+ 标准的迭代器接口(collections.abc.Iterator(Iterable))有2个方法:`__next__`,`__iter__`
+ `__next__`:返回下一个可用的元素，如果元素耗尽，抛出StopIteration异常
+ next(iterator[, default]):通过调用 iterator 的 __next__() 方法获取下一个元素。如果迭代器耗尽，则返回给定的 default，如果没有默认值则触发 StopIteration。



```doctest
next(...)
    next(iterator[, default])
    
    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.
(END)
>>> class It:
...     def __iter__(self):
...             return self
...     def __next__(self):
...             print('next called :',self.i)
...             self.i +=1
...             return self.i
...     def __init__(self):
...             self.i = 0
... 
>>> 
>>> it = It()
>>> it
<__main__.It object at 0x7f13b26e6f70>
>>> import collections.abc as ca
>>> isinstance(it,ca.Iterable)
True
>>> isinstance(it,ca.Iterator)
True
>>> for i in it:
...     if i >10:break
...     print(i)
... 
next called : 0
1
next called : 1
2
next called : 2
3
next called : 3
4
next called : 4
5
next called : 5
6
next called : 6
7
next called : 7
8
next called : 8
9
next called : 9
10
next called : 10
```


+ `__iter__`:返回self,以便在应该使用可迭代对象的地方使用迭代器，例如在for循环中
+ [`iter()`:返回一个 iterator 对象。根据是否存在第二个实参，第一个实参的解释是非常不同的。如果没有第二个实参，object 必须是支持迭代协议（有 `__iter__()` 方法）的集合对象，或必须支持序列协议（有 `__getitem__()` 方法，且数字参数从 0 开始）。如果它不支持这些协议，会触发 TypeError。如果有第二个实参 sentinel，那么 object 必须是可调用的对象。这种情况下生成的迭代器，每次迭代调用它的 `__next__()` 方法时都会不带实参地调用 object；如果返回的结果是 sentinel 则触发 StopIteration，否则返回调用结果。](https://docs.python.org/zh-cn/3/library/functions.html#iter)

```doctest
iter(...)
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator 
    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.
(END)
>>> s = iter('python')
>>> s 
<str_iterator object at 0x7f13b292dd00>  
>>> for i in s:
...     print(i)
...
p 
y
t
h
o
n 
>>> import random
>>> def f():
...     return random.randint(0,9)
... 
>>> sf = iter(f,5)
>>> sf
<callable_iterator object at 0x7f13b26beb20>
>>> list(sf)
[9, 7, 8, 7, 4, 6, 7, 0]
```


```doctest
>>> import re
>>> import reprlib
>>> class Sentence:
...     def __init__(self,text):
...             self.text = text
...             self.words = re.findall(r'\w+',self.text)
...     def __repr__(self):
...             return f'Sentence({reprlib.repr(self.text)})'
...     def __iter__(self):
...             print('in iter')
...             for word in self.words:
...                     yield word
...             return 
... 
>>> 
>>> s = Sentence('you raise me up.')
>>> s
Sentence('you raise me up.')
>>> i = iter(s)
>>> i
<generator object Sentence.__iter__ at 0x7fe8e66435f0>
>>> next(i)
in iter
'you'
>>> next(i)
'raise'
>>> next(i)
'me'
>>> 
>>> next(i)
'up'
>>> next(i)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> for i in Sentence('you and me'):
...     print(i)
... 
in iter
you
and
me
>>> 
```


+ [dis 模块通过反汇编支持CPython的 bytecode 分析。该模块作为输入的 CPython 字节码在文件 Include/opcode.h 中定义，并由编译器和解释器使用。](https://docs.python.org/zh-cn/3/library/dis.html)

+ CPython implementation detail: 字节码是 CPython 解释器的实现细节。不保证不会在Python版本之间添加、删除或更改字节码。不应考虑将此模块的跨 Python VM 或 Python 版本的使用
+ 深入理解for循环

```doctest
>>> import dis
>>> lst = [1,2,3,4]
>>> dis.dis("for i in lst:pass")
  1           0 LOAD_NAME                0 (lst)
              2 GET_ITER
        >>    4 FOR_ITER                 4 (to 10)
              6 STORE_NAME               1 (i)
              8 JUMP_ABSOLUTE            4
        >>   10 LOAD_CONST               0 (None)
             12 RETURN_VALUE
>>> 
```
+ [itertools --- 为高效循环而创建迭代器的函数](https://docs.python.org/zh-cn/3/library/itertools.html)
+ `itertools.islice(iterable, stop)/itertools.islice(iterable, start, stop[, step])`
+ 创建一个迭代器，返回从 iterable 里选中的元素。
+ `itertools.count(start=0, step=1)':创建一个迭代器，它从 start 值开始，返回均匀间隔的值。

```doctest
>>> c = itertools.count(2,.5)
>>> list(itertools.islice(c,10))
[2, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]
```

+ `itertools.cycle(iterable)`:创建一个迭代器，返回 iterable 中所有元素并保存一个副本。当取完 iterable 中所有元素，返回副本中的所有元素。无限重复。


```doctest
>>> s = 'abc'
>>> x = itertools.cycle(s)
>>> x
<itertools.cycle object at 0x7f13b267f3c0>
>>> list(itertools.islice(x,10))
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a']
```



-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap6.md
[pre_chap]: chap6_9_construction_method.md
[next_chap]: chap6_11_generator.md
