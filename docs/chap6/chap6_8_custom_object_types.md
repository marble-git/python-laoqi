## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 6.8 自定义对象类型

+ **定义类** ，就是定义 **新的对象类型**
+ 目标: 尽量缩小自定义类 与 内置对象类型的差距

### 6.8.1 简单的对象类型

+ `__bytes`,`bytes()`:获取对象的字节序列表示形式
+ `__format__`,`format()`:使用特殊的格式代码显示对象的字符串表示形式
	- [格式字符串语法](https://docs.python.org/zh-cn/3/library/string.html#format-string-syntax)
	- [格式规格迷你语言](https://docs.python.org/zh-cn/3/library/string.html#formatspec)
+ `__str__`:以 **便于用户理解** 的方式返回 **对象的字符串表示形式**;
+ `str()`:将对象转换为字符串，返回用户易读的表达形式
+ `__repr__`:以 **便于开发者理解** 的方式返回 **对象的字符串表示形式**
+ `repr()`:产生一个解释器易读的表达形式

```doctest
Help on built-in function repr in module builtins:
repr(obj, /)
    Return the canonical string representation of the object.
    For many object types, including most builtins, eval(repr(obj)) == obj.
(END)
>>> class RoundFloat:
...     def __init__(self,value):
...             self.value=value
...     def __str__(self):
...             print('in __str__')
...             return '{0:.2f}'.format(self.value)
...     def __repr__(self):
...             print('in __repr__')
...             return '{0}({1})'.format(type(self).__name__,self.value)
>>> rf = RoundFloat(3.1415)
>>> rf
in __repr__
RoundFloat(3.1415)
>>> print(rf)
in __str__
3.14
```

+ 运算符重载: `a + b` <==> `a.__add__(b)`
	- 以`+`运算符为例,2个对象能否进行加法运算首先要看是否有`__add__()`方法
	- 即使对象在数学上不能做“加法”运算，也可以用“+”来表达`obj.__add__()`方法所定义的操作
	- 运算符有简化书写的功能，但要依靠特殊方法实现




+ ***运算符和方法名称***



运算符	|特殊方法
:------:|:--------
`+`	|`__add__`,`__radd__`
`-`	|`__sub__`,`__rsub__`
`*`	|`__mul__`,`__rmul__`
`/`	|`__div__`,`__rdiv__`,`__truediv__`,`__rtruediv__`
`//`	|`__floordiv__`,`__rfloordiv__`
`%`	|`__mod__`,`__rmod__`
`**`	|`__pow__`,`__rpow__`
`<<`	|`__lshift__`,`__rlshift__`
`>>`	|`__rshift__`,`__rrshift__`
`&`	|`__and__`,`__rand__`
`==`	|`__eq__`
`!=`	|`__ne__`
`>`	|`__gt__`
`<`	|`__lt__`
`>=`	|`__ge__`
`<=`	|`__le__`





```doctest
>>> rf2=RoundFloat(2)
>>> rf3=RoundFloat(3)
>>> rf2
in __repr__
RoundFloat(2)
>>> rf3
in __repr__
RoundFloat(3)
>>> rf2 + rf3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'RoundFloat' and 'RoundFloat'
>>> def fadd(self,other):
...     print('in __add__')
...     return type(self)(self.value + other.value)
... 
>>> RoundFloat.__add__ = fadd
>>> rf2 + rf3
in __add__
in __repr__
RoundFloat(5)
>>> rfs = rf2 + rf3
in __add__
>>> rfs
in __repr__
RoundFloat(5)
>>> print(rfs)
in __str__
5.00
```



+ 对于多数内置对象，有:`obj == eval(repr(obj))`
+ 如果类中没有 `__str__()`方法，会调用`__repr__()`

```doctest
>>> class Trepr:
...     def __init__(self,value):
...             self.value=value
...     def __repr__(self):
...             print('in repr')
...             return 'Trepr({v})'.format(v=self.value)
... 
>>> r = Trepr(3.1415)
>>> r
in repr
Trepr(3.1415)
>>> print(r)
in repr
Trepr(3.1415)
>>> repr(r)
in repr
'Trepr(3.1415)'
>>> eval(repr(r)) == r
in repr
False
>>> rr = eval(repr(r))
in repr
>>> rr
in repr
Trepr(3.1415)
>>> type(rr)
<class '__main__.Trepr'>
>>> type(r)
<class '__main__.Trepr'>
>>> rr.value
3.1415
>>> r.value
3.1415
>>> rr == r
False
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> a == eval(repr(a))
True
```


### 6.8.2 控制属性访问



+ [`__slots__` 特殊属性:](https://docs.python.org/zh-cn/3/reference/datamodel.html#slots)
+ *流畅的Python P221*
+ `__slots__` 属性的设计目的是用于优化的，不是为了约束程序员
+ 不要使用 `__slots__` 属性来禁止类的用户新增实例属性
+ 在类中定义`__slots__`属性后,实例不能再有`__slots__`中所列名称之外的其他属性。 ***这只是一个副作用*** 



+ `.` 属性访问 [自定义模块属性访问](https://docs.python.org/zh-cn/3/reference/datamodel.html#customizing-attribute-access)
+ `__getattr__(self,name)`:访问对象不存在的属性时调用
+ `__setattr__(self,name,value)`:为对象创建新属性或为属性赋值时调用
+ `__getattribute__(self,name)`:每当访问对象的属性时调用
+ `__delattr__(self,name)`:删除对象的属性时调用


```doctest
>>> class Bar:
...     def __getattribute__(self,name):
...             print('in getattribute')
...             return object.__getattribute__(self,name)
...     def __getattr__(self,name):
...             print('in getattr')
...             return object.__getattr__(self,name)
... 
>>> b=Bar()
>>> b.x=1
>>> b.x
in getattribute
1
>>> b.y
in getattribute
in getattr
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in __getattr__
AttributeError: type object 'object' has no attribute '__getattr__'
>>> 
```





```doctest
>>> class NewRectangle:
...     def __init__(self):
...             self.width=0
...             self.length=0
...     def __getattr__(self,name):
...             print('in getattr')
...             if name == 'size':
...                     return self.width,self.length
...             else:
...                     raise AttributeError
...     def __setattr__(self,name,value):
...             print('in setattr')
...             if name == 'size':
...                     self.width,self.length=value
...             else:
...                     self.__dict__[name] = value
... 
>>> 
>>> r = NewRectangle()
in setattr
in setattr
>>> dir(r)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'length', 'width']
>>> r.length
0
>>> r.width
0
>>> r.size
in getattr
(0, 0)
>>> r.size = [11,22]
in setattr
in setattr
in setattr
>>> r.size
in getattr
(11, 22)
>>> r.aa=123
in setattr
>>> def nset(s,n,v):
...     print('in nset')
...     if n == 'size':
...             print('will set size(width,length)')
...             s.width,s.length = v
...     else:
...             print('in else br')
...             print(f'will set {n} = {v}')
...             s.__dict__[n]=v
... 
>>> NewRectangle.__setattr__ = nset
>>> r.size = [999,111]
in nset
will set size(width,length)
in nset
in else br
will set width = 999
in nset
in else br
will set length = 111
>>> r.size 
in getattr
(999, 111)
>>> 
```




+ **相应的函数**
+ `getattr(object, name[, default]) -> value` getattr(x, 'y') is equivalent to x.y
+ `setattr(obj, name, value, /)`  setattr(x, 'y', v) is equivalent to ``x.y = v''
+ `delattr(obj, name, /)` delattr(x, 'y') is equivalent to ``del x.y''








### 6.8.3 可调用对象


+ `()` 函数调用
+ 任何对象，如果只写名称，表示的是该名称所引用的对象本身
+ 只有在对象名称后增加`()`才是执行/调用这个对象
+ `__call__` 特殊方法: 使类的实例可调用;拥有该方法的对象才可调用(callable)
+ `callable()`函数检查一个对象是否可调用


```doctest
Help on built-in function callable in module builtins:
callable(obj, /)
    Return whether the object is callable (i.e., some kind of function). 
    Note that classes are callable, as are instances of classes with a
    __call__() method.
(END)
```



```doctest
>>> def foo():pass
... 
>>> dir(foo)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> 'abc'()
<stdin>:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
>>> class Bar:...     def __call__(self,x):...             print('<{}>, called, input value is :{}'.format(self,x))
... 
>>> b = Bar()>>> b()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __call__() missing 1 required positional argument: 'x'
>>> b(589)
<<__main__.Bar object at 0x7f0381999d90>>, called, input value is :589
>>> b
<__main__.Bar object at 0x7f0381999d90>
>>> callable('sfsaf')
False
>>> callable(foo)
True
>>> callable(Bar)
True
>>> callable(b)
True
>>> dir(Bar)
['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```






### 6.8.4 对象的类索引操作


+ `[]` 元素访问/切片
+ [模拟容器类型](https://docs.python.org/zh-cn/3/reference/datamodel.html#emulating-container-types)
+ `__len__(self)`:调用此方法以实现内置函数 len()。应该返回对象的长度，以一个 >= 0 的整数表示。此外，如果一个对象未定义 __bool__() 方法而其 __len__() 方法返回值为零，则在布尔运算中会被视为假值。
+ `len()`

```
len(obj, /)
    Return the number of items in a container.
(END)
```

+ 切片:`a[1:2]` 会被转写为`a[slice(1,2,None)]`;略去的切片项总是以None补全
+ `slice()`:

```
>>> dir(slice)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'indices', 'start', 'step', 'stop']
class slice(object)
 |  slice(stop)
 |  slice(start, stop[, step])
 |  
 |  Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).
```

+ [`slice.indices(self, length)`](https://docs.python.org/zh-cn/3/reference/datamodel.html#slice.indices)

```
indices(...) method of builtins.slice instance
    S.indices(len) -> (start, stop, stride)
    
    Assuming a sequence of length len, calculate the start and stop
    indices, and the stride length of the extended slice described by
    S. Out of bounds indices are clipped in a manner consistent with the
    handling of normal slices.
slice.indices(self, length)¶
此方法接受一个整型参数 length 并计算在切片对象被应用到 length 指定长度的条目序列时切片的相关信息应如何描述。 其返回值为三个整型数组成的元组；这些数分别为切片的 start 和 stop 索引号以及 step 步长值。索引号缺失或越界则按照与正规切片相一致的方式处理。
>>> b = slice(1,7,3)
>>> b.indices(4)
(1, 4, 3)
>>> b = slice(1,-7,3)
>>> b
slice(1, -7, 3)
>>> b.indices(20)
(1, 13, 3)
```



+ `__getitem__(self,key)`
+ `__setitem__(self,key,value)`
+ `__delitem__(self,key)`

```doctest
>>> class S:
...     def __getitem__(self,k):print(k)
...     def __setitem__(self,k,v):print(k,'|',v)
...     def __delitem__(self,k):print(k)
... 
>>> 
>>> s = S()
>>> i = 1
>>> s[i]; s[i]='a'; del s[i]
1
1 | a
1
>>> s[1:] ; s[1:] = 11; del s[1:]
slice(1, None, None)
slice(1, None, None) | 11
slice(1, None, None)
>>> s[1:,2] ; s[1:,2] = 11; del s[1:,2]
(slice(1, None, None), 2)
(slice(1, None, None), 2) | 11
(slice(1, None, None), 2)
>>> s[1:,::2] ; s[1:,::2] = 11; del s[1:,::2]
(slice(1, None, None), slice(None, None, 2))
(slice(1, None, None), slice(None, None, 2)) | 11
(slice(1, None, None), slice(None, None, 2))
```



+ `__missing__(self,key)`:此方法由 `dict.__getitem__()` 在找不到字典中的键时调用以实现 **dict 子类** 的 self[key]。


+ 成员检测运算符 (in 和 not in) 通常以对容器进行逐个迭代的方式来实现。 不过，容器对象可以提供以下特殊方法并采用更有效率的实现，这样也不要求对象必须为可迭代对象
+ `__contains__(self,item)`:调用此方法以实现成员检测运算符。如果 item 是 self 的成员则应返回真，否则返回假。对于映射类型，此检测应基于映射的键而不是值或者键值对。

- 对于未定义 `__contains__()` 的对象，成员检测将首先尝试通过 `__iter__()` 进行迭代，然后再使用 `__getitem__()` 的旧式序列迭代协议，参看 语言参考中的相应部分。




+ `__reversed__(self)`:此方法（如果存在）会被 reversed() 内置函数调用以实现逆向迭代。它应当返回一个新的以逆序逐个迭代容器内所有对象的迭代器对象。

+ 如果未提供 `__reversed__()` 方法，则 reversed() 内置函数将回退到使用序列协议 (`__len__()` 和 `__getitem__()`)。支持序列协议的对象应当仅在能够提供比 reversed() 所提供的实现更高效的实现时才提供 `__reversed__()` 方法。

```doctest
>>> class A:
...     def __len__(self):
...             print('in len')
...             return 5
...     def __getitem__(self,key):
...             print('in geti :',key)
... 
>>> 
>>> a=A()
>>> len(a)
in len
5
>>> reversed(a)
in len
<reversed object at 0x7f03815f8f40>
>>> list(reversed(a))
in len
in len
in geti : 4
in geti : 3
in geti : 2
in geti : 1
in geti : 0
[None, None, None, None, None]
```


+ `reversed()`

```
class reversed(object)
 |  reversed(sequence, /)
 |  
 |  Return a reverse iterator over the values of the given sequence.
```



```doctest
>>> class Bar:
...     def __init__(self,t):
...             self.num = [None] * t
...     def __setitem__(self,p,v):
...             print('in setitem')
...             self.num[p] = v
...     def __getitem__(self,p):
...             print('in geti')
...             return self.num[p]
... 
>>> 
>>> b = Bar(3)
>>> b
<__main__.Bar object at 0x7f03815f8100>
>>> b.num
[None, None, None]
>>> b[1]
in geti
>>> b[1] = 'python'
in setitem
>>> b.num
[None, 'python', None]
>>> b[1]
in geti
'python'
>>> b.__setitem__(2,'php')
in setitem
>>> b.num
[None, 'python', 'php']
>>> b[2]
in geti
'php'
>>> b[0]='c'
in setitem
>>> b[3]='rust'
in setitem
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in __setitem__
IndexError: list assignment index out of range
>>> b.num
['c', 'python', 'php']
>>> len(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'Bar' has no len()
>>> for i in b:
...     print(i)
... 
in geti
c
in geti
python
in geti
php
in geti
```





-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap6.md
[pre_chap]: chap6_7_encapsulation.md
[next_chap]: chap6_9_construction_method.md
