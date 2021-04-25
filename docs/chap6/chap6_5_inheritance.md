## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 6.5 继承

+ 继承(inheritance),是OOP中的中的重要概念，也是类的3大特性之一(另外2个分别是 多态和封装)
+ 子类继承父类后，不需要再次编写相同的代码，实现了代码的重用
+ 子类继承父类的同时，也可以重新定义某些属性或方法来覆盖父类原有的对应部分，使子类获得与父类不同的功能
+ 从继承方式来看，python中的继承分为“单继承”和“多继承”
+ `class.__base__`  获得该类的第1个直接基类
+ [`class.__bases__` 获得该类的所有直接基类组成的元组](https://blog.csdn.net/LaoYuanPython/article/details/93785166?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161771857716780264024311%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161771857716780264024311&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~sobaiduend~default-3-93785166.pc_v2_rank_blog_default&utm_term=python+__bases__) [官方文档](https://docs.python.org/zh-cn/3.9/library/stdtypes.html?highlight=__bases__#special-attributes)
+ [`super()` ](https://docs.python.org/zh-cn/3.9/library/functions.html#super)
```doctest
class super(object)
 |  super() -> same as super(__class__, <first argument>)
 |  super(type) -> unbound super object
 |  super(type, obj) -> bound super object; requires isinstance(obj, type)
 |  super(type, type2) -> bound super object; requires issubclass(type2, type)
 |  Typical use to call a cooperative superclass method:
 |  class C(B):
 |      def meth(self, arg):
 |          super().meth(arg)
 |  This works for class methods too:
 |  class C(B):
 |      @classmethod
 |      def cmeth(cls, arg):
 |          super().cmeth(arg)
 |  Data descriptors defined here:
 |  
 |  __self__
 |      the instance invoking super(); may be None
 |  
 |  __self_class__
 |      the type of the instance invoking super(); may be None
 |  
 |  __thisclass__
 |      the class invoking super()
>>> class A:
...     pass
... 
>>> 
>>> class B(A):
...     def foo(self):
...             print(super().__self__,super().__self_class__,super().__thisclass__)
... 
>>> class D(B):pass
... 
>>> b = B()
>>> d=D()
>>> b.foo()
<__main__.B object at 0x7fb9dfce8490> <class '__main__.B'> <class '__main__.B'>
>>> d.foo()
<__main__.D object at 0x7fb9dfce83a0> <class '__main__.D'> <class '__main__.B'>
>>> D.mro()
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
```


+ `isinstance`
```doctest
Help on built-in function isinstance in module builtins:
isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.
    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
```


+ `issubclass`
```doctest
Help on built-in function issubclass in module builtins:
issubclass(cls, class_or_tuple, /)
    Return whether 'cls' is a derived from another class or is the same class. 
    A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
    or ...`` etc.
(END)
```





+ 'type': `__base__,__bases__,__mro__,mro()`
```doctest
>>> dir(type)
['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__', '__weakrefoffset__', 'mro']
>>> type.mro(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor 'mro' for 'type' objects doesn't apply to a 'C' object
>>> type.mro(C)
[<class 'mul_inheritance.C'>, <class 'mul_inheritance.J1'>, <class 'mul_inheritance.K1'>, <class 'mul_inheritance.J2'>, <class 'mul_inheritance.K2'>, <class 'object'>]
```

### 6.5.1 单继承

+ 单继承:就是只从一个父类那里继承
+ `__base__` 属性可以得到当前类的第一个直接父类
+ python3中，所有类都是object的子类;所以不用定义类的时候写这个“公共的父类”了
+ 继承:把父类的属性和方法都拿到子类中
+ 重写(override):子类中对父类的属性或方法的覆盖，重写
+ 在子类中继续使用被覆盖的父类方法或属性
	- `父类名.方法名(self,arg1,arg2,...)`
	- `super().方法名(arg1,arg2,...)`
```python
#coding:utf-8
'''
    filename:single_inheritance.py
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
class Student(Person):
    def grade(self,n):
        print("{}'s grade is {}".format(self.name,str(n)))
stu1 = Student("Galileo",27)
stu1.grade(99)
print(stu1.get_name())
print(stu1.get_age())
#base class name
class StudentOverrideName(Person):
    def __init__(self,school,name,age):
        self.school = school
        Person.__init__(self,name,age)
    def grade(self,n):
        print("{}'s grade is {}".format(self.name,str(n)))
stu2 = StudentOverrideName("Soochow University",'Name',23)
stu2.grade(99)
print(stu2.get_name())
print(stu2.get_age())
#super
class StudentOverrideSuper(Person):
    def __init__(self,school,name,age):
        self.school = school
        super().__init__(name,age)
    def grade(self,n):
        print("{}'s grade is {}".format(self.name,str(n)))
stu3 = StudentOverrideSuper("Soochow University",'Super',24)
stu3.grade(99)
print(stu3.get_name())
print(stu3.get_age())
#error
class StudentOverrideError(Person):
    def __init__(self,school):
        self.school = school
    def grade(self,n):
        print("{}'s grade is {}".format(self.name,str(n)))
stu4 = StudentOverrideError("Soochow University")
stu4.grade(99)
print(stu4.get_name())
print(stu4.get_age())
```
out:
```
root@kali-book:~/python-laoqi/chap6# python3 single_inheritance.py 
Galileo's grade is 99
Galileo
27
Name's grade is 99
Name
23
Super's grade is 99
Super
24
Traceback (most recent call last):
  File "/root/python-laoqi/chap6/single_inheritance.py", line 64, in <module>
    stu4.grade(99)
  File "/root/python-laoqi/chap6/single_inheritance.py", line 62, in grade
    print("{}'s grade is {}".format(self.name,str(n)))
AttributeError: 'StudentOverrideError' object has no attribute 'name'
```










### 6.5.2 多继承

+ 多继承:指某个子类的父类不止一个，而是多个
+ `__mro__`属性显示的是类的继承顺序，python3中采用了[“C3方法”来确定顺序](https://chi.jinzhao.wiki/wiki/C3%E7%BA%BF%E6%80%A7%E5%8C%96)
+ `__bases__`属性显示当前类的所有直接父类组成的元组
+ [`Mixin`](https://chi.jinzhao.wiki/wiki/Mixin)

+ [多继承中的`super`用法](https://blog.csdn.net/qq_26442553/article/details/81775449)
```doctest
>>> class A:
...     def __init__(self):
...             super().__init__()
...             print('initing A')
... 
>>> 
>>> class B:
...     def __init__(self):
...             super().__init__()
...             print('initing B')
... 
>>> 
>>> class C(A,B):
...     def __init__(self):
...             super().__init__()
...             print('initing C')
... 
>>> a=A()
initing A
>>> b=B()
initing B
>>> c=C();
initing B
initing A
initing C
>>> C.mro()
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```




```python
#coding:utf-8
'''
    filename:mul_inheritance.py
    the order of multiple inheritance in Python.
'''
class K1:
    def foo(self):
        print('K1-foo')
class K2:
    def foo(self):
        print('K2-foo')
class J1(K1):
    pass
class J2(K2):
    def bar(self):
        print("J2-bar")
class C(J1,J2):
    pass
c = C()
c.foo()
c.bar()
print(C.mro())
print(C.__mro__)
#print(c.mro())
#print(c.__mro__)
```


```doctest
>>> from mul_inheritance import *
K1-foo
J2-bar
[<class 'mul_inheritance.C'>, <class 'mul_inheritance.J1'>, <class 'mul_inheritance.K1'>, <class 'mul_inheritance.J2'>, <class 'mul_inheritance.K2'>, <class 'object'>]
(<class 'mul_inheritance.C'>, <class 'mul_inheritance.J1'>, <class 'mul_inheritance.K1'>, <class 'mul_inheritance.J2'>, <class 'mul_inheritance.K2'>, <class 'object'>)
>>> dir()
['C', 'J1', 'J2', 'K1', 'K2', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'c']
>>> dir(C)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bar', 'foo']
>>> C.__base__
<class 'mul_inheritance.J1'>
>>> C.__bases__
(<class 'mul_inheritance.J1'>, <class 'mul_inheritance.J2'>)
>>> C.__mro__
(<class 'mul_inheritance.C'>, <class 'mul_inheritance.J1'>, <class 'mul_inheritance.K1'>, <class 'mul_inheritance.J2'>, <class 'mul_inheritance.K2'>, <class 'object'>)
>>> C.mro()
[<class 'mul_inheritance.C'>, <class 'mul_inheritance.J1'>, <class 'mul_inheritance.K1'>, <class 'mul_inheritance.J2'>, <class 'mul_inheritance.K2'>, <class 'object'>]
>>> isinstance(c,C)
True
>>> isinstance(c,J1)
True
>>> isinstance(c,J2)
True
>>> isinstance(c,K1)
True
>>> isinstance(c,K2)
True
>>> isinstance(c,object)
True
>>> isinstance(c,type)
False
>>> isinstance(C,type)
True
oo==================ooooooo
>>> issubclass(C,J1)
True
>>> issubclass(C,J2)
True
>>> issubclass(C,K1)
True
>>> issubclass(C,K2)
True
>>> issubclass(C,object)
True
>>> issubclass(C,type)
False
>>> isinstance(object,type)
True
>>> isinstance(type,object)
True
>>> issubclass(object,type)
False
>>> issubclass(type,object)
True
```


-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
