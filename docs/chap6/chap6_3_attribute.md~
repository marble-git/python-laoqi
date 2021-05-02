## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

# 6.3 属性

+ Python中的对象属性(variable)可以划分为 **实例属性(instance var)** 与 **类属性(class var)**
+ 类变量不是在实例化时创建的, **而是随着类的创建而存在的**

### 6.3.1 类属性

+ 类属性(类变量:class variable)，又称 **静态属性**
+ 只有通过类才能修改
+ 实例也拥有类属性，但不能修改类属性(可以访问)







### 6.3.2 实例属性

+ 实例属性(实例变量:instance variable)，又称 **动态属性**
+ 通过实例创建
+ 不同实例的实例属性可以不同
+ 实例的`__dict__`显示当前 **实例的** 所有属性
+ 使用`del inst.var` 删除属性:本质上是 解除变量与对象的引用关系
+ 实例变量与类变量同名，实例变量会"遮盖"类变量


### 6.3.3 self 的作用


+ self 就是实例对象,创建实例的时候，实例作为第1个参数被解释器传给了self
+ 实例调用，隐式传递实例对象给self
+ 通过类调用，必须向self提供实例
+ 定义类的时候，参数self就是预备用来实例化后引用实例的变量



```doctest
>>> class P:
...     def __init__(self,name):
...             self.name=name
...     def get_name(self):
...             return self.name
... 
>>> a=P('xiaohuang')
>>> a.get_name()
'xiaohuang'
>>> P.get_name(a)
'xiaohuang'
>>> P.get_name()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: get_name() missing 1 required positional argument: 'self'
>>> P.get_name(self=a)
'xiaohuang'
```










-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap6.md
[pre_chap]: chap6_2_simple_class.md
[next_chap]: chap6_4_method.md
