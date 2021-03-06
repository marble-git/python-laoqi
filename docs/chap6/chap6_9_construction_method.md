## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------


## 6.9 构造方法



+ `__init__`:初始化方法
+ [`__new__`:构造方法,调用以创建一个 cls 类的新实例,用于自定义类型的特殊方法](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__new__)

+ 如果 `__new__()` 在构造对象期间被发起调用并且它返回了一个实例或 cls 的子类，则新实例的 `__init__()` 方法将以 `__init__(self[, ...])` 的形式被发起调用，其中 self 为新实例而其余的参数与被传给对象构造器的参数相同。


```doctest
>>> class A:pass
... 
>>> def new(cls,*a,**k):
...     print(cls,a,k)
...     return super().__new__(cls)
... 
>>> def init(self,*a,**k):
...     print(self,a,k)
>>> A.__new__ = new
>>> A.__init__ = init
>>> a = A()
<class '__main__.A'> () {}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in new
RuntimeError: super(): __class__ cell not found
>>> def new(cls,*a,**k):
...     print(cls,a,k)
...     return object.__new__(cls)
... 
>>> A.__new__ = new
>>> a = A()
<class '__main__.A'> () {}
<__main__.A object at 0x7fedea414b80> () {}
>>> a = A(1,2,3,k=5,n=9)
<class '__main__.A'> (1, 2, 3) {'k': 5, 'n': 9}
<__main__.A object at 0x7fedea4148e0> (1, 2, 3) {'k': 5, 'n': 9}
```



### 6.9.1 基本应用

+ 类中的`__new__`方法的定义格式与其他特殊方法无异, ***第一参数cls引用当前类***
+ 构造方法`__new__`的返回值必须是所创建的实例
+ ***在自定义的`__new__()`中得到实例(调用`super()/object.__new__(cls)`)时，不要再传入其他参数***







### 6.9.2 单例模式


+ [`单例模式`:目的，某个类只有一个实例存在](https://www.runoob.com/design-pattern/singleton-pattern.html)
+ 实现:重写`__new__()`




+ 装饰器

```doctest
>>> from functools import wraps
>>> def singleton(cls): 
...     ins = {}
#...     @wraps(cls)
...     def inner():
...             if cls not in ins:
...                     obj = cls()
...                     ins[cls]=obj
...                     print('create :',obj)
...             else:
...                     print('already exist')
...             return ins[cls]
...     return inner
... 
>>> @singleton
... class A:
...     def __init__(self):
...             print('A init calles')
... 
>>> 
>>> A()
A init calles
create : <__main__.A object at 0x7f96fb604f70>
<__main__.A object at 0x7f96fb604f70>
>>> A.__name__
'inner'
>>> A()
already exist
<__main__.A object at 0x7f96fb604f70>
>>> A()
already exist
<__main__.A object at 0x7f96fb604f70>
```



-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap6.md
[pre_chap]: chap6_8_custom_object_types.md
[next_chap]: chap6_10_iterator.md
