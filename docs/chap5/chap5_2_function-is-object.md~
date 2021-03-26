## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 5.2 函数是对象

+ `pass` `pass_stmt ::=  "pass"`
+ pass 是一个空操作 --- 当它被执行时，什么都不发生。 它适合当语法上需要一条语句但并不需要执行任何代码时用来临时占位
+ 在python中对于任何对象，都可以这样理解:
	- 单独写对象名称(引用对象的变量),得到的是该对象
	- 在对象后面增加圆括号 `()`,就是执行或调用这个对象;只不过有些对象不允许执行或调用
+ `callable()` 判断对象是否可调用
+ `hex`返回一个数字的16进制形式

```python
>>> def bar():pass
... 
>>> bar
<function bar at 0x7f6d04a81af0>
>>> bar()
>>> id(bar())
9467616
>>> 3()
<stdin>:1: SyntaxWarning: 'int' object is not callable; perhaps you missed a comma?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> callable(bar)
True
>>> callable(3)
False
>>>help(hex)
hex(number, /)
    Return the hexadecimal representation of an integer.
    >>> hex(12648430)
    '0xc0ffee'
>>> help(callable)
callable(obj, /)
    Return whether the object is callable (i.e., some kind of function).
    Note that classes are callable, as are instances of classes with a
    __call__() method.
(END)
```




### 5.2.1 属性


+ `dir(foo)` 查看函数的属性
+ `foo.lang='python'` 增加函数的属性

```python
def foo():
    foo.lang = 'php'	#定义函数的属性
```

+ `del foo.lang` 删除函数的属性
+ `eval(source, globals=None, locals=None, /)` 返回表达式source的执行结果
+ 查看函数的属性及其值
```python
def get_attrs(f:'function name'):
    attrs=dir(f)
    for item in attrs:
        f_attr=f.__name__+'.'+item
        print(f_attr,' : ',eval(f_attr))
```


### 5.2.2 嵌套函数


+ partial 函数的功能就是：把一个函数的某些参数给固定住，返回一个新的函数
```python
class partial(builtins.object)
 |  partial(func, *args, **keywords) - new function with partial application
 |  of the given arguments and keywords.
from functools import partial
pt = partial(print,sep='*')
#等价于:
def pt(*args,**kwargs):
    if 'sep' not in kwargs:
        return print(*args,sep='*',**kwargs)
    else:
        return print(*args,**kwargs)
```

+ 嵌套函数: 在函数内部定义函数
+ 诞生理由: 一个函数想使用另一个函数内部的变量，可以定义在其内部

### 闭包 closure 与 自由变量 free variable

+ 闭包: 如果一个函数定义在另一个函数的作用域内，并且引用了外层函数的变量，则该函数称为闭包。

+ 自由变量: 自由变量指未在本地作用域绑定的变量。这是一个相对的概念
+ nonlocal 语句会使得所列出的名称指向之前在最近的包含作用域中绑定的除全局变量以外的变量。 这种功能很重要，因为绑定的默认行为是先搜索局部命名空间。 这个语句允许被封装的代码重新绑定局部作用域以外且非全局（模块）作用域当中的变量。

+ 闭包是Python所支持的一种特性，它让在非global scope定义的函数可以引用其外围空间中的变量，这些外围空间中被引用的变量叫做这个函数的环境变量。环境变量和这个非全局函数一起构成了闭包。
+ `closure.__closure__` 包含了外层函数的变量(环境) free variable
+ 闭包特点：
 - 一个函数返回的函数对象，这个函数对象执行的话依赖非函数内部的变量值，这个时候，函数返回的实际内容如下：
 - 1 函数对象
 - 2 函数对象需要使用的外部变量和变量值
*** 闭包必须嵌套在一个函数里，必须返回一个调用外部变量的函数对象，才是闭包***

***通俗理解就是：里面函数执行  ，需要用到外面函数的一个变量 ，所以，就把外面变量和里面这个函数合到一块，合到一块的这两个东西就是闭包***

```python
def outer():
    x = 1
    def closure():
    print(x)
    return closure
```
+ 命名空间Name space: Local->Nested->Global->Builtin
+ `global name` 声明或引用global变量,name可以在全局命名空间中存在或不存在
+ `nonlocal name` 引用 `非local,非global` 即`Nested命名空间`中的变量,必须在外层嵌套函数中已定义




### 5.2.3 装饰器


+ `内层函数`是在外层函数执行时被定义的
+ `@` 是装饰器语法糖
+ `装饰器`是在被装饰的函数定义时执行的

```python
@g
def f():pass
<==>
def f():pass
f = g(f)
```

+ 多个装饰器装饰一个函数时，装饰器的执行顺序为:从下至上

```python
@g
@f
def m():pass
<==>
def m():pass
m = g(f(m))
```

+ 带参数的装饰器为3层嵌套

```python
@log('INFO')
def foo():pass
<==>
def foo():pass
foo = log('INFO')(foo)
```

+ `functools.wraps` 保留原始被装饰函数的属性
+ `functools.wraps 是 functools.update_wrapper 的 functools.partial()方便形式`


***装饰器内使用 functools.wraps()***
```python
def dec1(f):
    print('exec dec1')
    def inner1(*a,**k):
        print('exec inner1')
        rst = f(*a,**k)
        print('ending inner1')
        return rst
    print('ending dec1')
    return inner1

def dec(func):
    @functools.wraps(func) #@functools.wraps(func)
    @dec1
    def indec(*a,**k):
        rst = func(*a,**k)
        return rst
    print('indec name:',indec.__name__)
    return indec

@dec
def foo():pass

print('-'*20,'start foo','-'*20)


输出:
exec dec1
ending dec1
indec name: foo #indec name: inner1
-------------------- start foo --------------------
exec inner1
ending inner1
```






***多个装饰器***
```python
def dec1(f):
    print('exec dec1')
    def inner1(*a,**k):
        print('exec inner1')
        rst = f(*a,**k)
        print('ending inner1')
        return rst
    print('ending dec1')
    return inner1



def dec2(f):
    print('exec dec2')
    def inner2(*a,**k):
        print('exec inner2')
        rst = f(*a,**k)
        print('ending inner2')
        return rst
    print('ending dec2')
    return inner2


@dec1
@dec2
def foo():
    print('exec foo')

print('-'*20,'start foo','-'*20)
foo()




输出:
exec dec2
ending dec2
exec dec1
ending dec1
-------------------- start foo --------------------
exec inner1
exec inner2
exec foo
ending inner2
ending inner1
```



***带参数的装饰器***
```python
def log(log_level='INFO',/):
    def outer(func):
        @functools.wraps(func)
        def wrapper(*arg,**kwargs):
            print(log_level,':',func.__name__,'is running.')
            return func(*arg,**kwargs)
        return wrapper
    return outer

@log('WARRING')
def foo():pass
foo()

@log()
def bar():pass
bar()
print(foo.__name__,bar.__name__)



输出:
WARRING : foo is running.
INFO : bar is running.
foo bar
```






***functools.wraps & functools.update_wrapper***
```python
>>> help(functools.wraps)
Help on function wraps in module functools:
wraps(wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))
    Decorator factory to apply update_wrapper() to a wrapper function
    Returns a decorator that invokes update_wrapper() with the decorated
    function as the wrapper argument and the arguments to wraps() as the
    remaining arguments. Default arguments are as for update_wrapper().
    This is a convenience function to simplify applying partial() to
    update_wrapper().
(END)
>>> help(functools.update_wrapper)
Help on function update_wrapper in module functools:
update_wrapper(wrapper, wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))
    Update a wrapper function to look like the wrapped function
    wrapper is the function to be updated
    wrapped is the original function
    assigned is a tuple naming the attributes assigned directly
    from the wrapped function to the wrapper function (defaults to
    functools.WRAPPER_ASSIGNMENTS)
    updated is a tuple naming the attributes of the wrapper that
    are updated with the corresponding attribute from the wrapped
    function (defaults to functools.WRAPPER_UPDATES)
(END)
```






-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap5.md
[pre_chap]: chap5_1_function-basis.md
[next_chap]: chap5_3_lambda_map_filter.md
