## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 6.4 类的方法
+ 方法(method): 根据定义，一个类中所有是函数对象的属性都是定义了其实例的相应方法。
+ [***实例的方法(p.f) 与 类的函数(P.f) 不是一回事***](https://docs.python.org/zh-cn/3/utorial/classes.html#method-objects)


```doctest
>>> class P:
...     def f(self):
...             print('x :',self.x)
... 
>>> p = P()
>>> id(p.f)
139776728062528
>>> id(P.f)
139776726219648
>>> p.f
<bound method P.f of <__main__.P object at 0x7f204e1e2520>>
>>> P.f
<function P.f at 0x7f204e1d3b80>
>>> type(p.f)
<class 'method'>
>>> type(P.f)
<class 'function'>
```

### 6.4.1 方法和函数的异同

+ 相同点:名称的命名;代码块的编写方式都一样;
+ 不同点:(实例)方法不能单独调用，只能通过实例或类 调用
	- 方法的第1个参数必须是self





### 6.4.2 类方法

+ [`@classmethod` 类方法的装饰器，可以解决“硬编码(hard code)”的问题](https://docs.python.org/zh-cn/3.9/library/functions.html#classmethod)
+ 类方法第一个参数：cls(cls<==>type(self)),表示类本身
+ 调用类方法时，隐式将类对象传给了第1个参数cls;不必再显示的传入类对象
+ 因为classmethod函数可以使用第1个参数，cls，来访问类变量，因此继承之后，cls自动就指向了继承后的类。注意，这是@classmethod与@staticmethod不一样的地方。也因为这个特性，决定了classmethod的应用会比staticmethod要广。
+ **类方法与当前类绑定**

类方法与当前类绑定

```doctest
>>> class A:
...     @classmethod
...     def f(cls):print(cls)
... 
>>> class B(A):
...     pass
... 
>>> a=A()
>>> b=B()
>>> a.f
<bound method A.f of <class '__main__.A'>>
>>> a.f()
<class '__main__.A'>
>>> b.f
<bound method A.f of <class '__main__.B'>>
>>> b.f()
<class '__main__.B'>
>>> A.f
<bound method A.f of <class '__main__.A'>>
>>> A.f()
<class '__main__.A'>
>>> B.f
<bound method A.f of <class '__main__.B'>>
>>> B.f()
<class '__main__.B'>
>>> a=A();aa=A();b=B();bb=B()
>>> id(a.f);id(aa.f);id(A.f)
139776723283648
139776723283648
139776723283648
>>> a.f  is  aa.f
False
>>> a.f  is  A.f
False
>>> id(b.f);id(bb.f);id(B.f)
139776723283648
139776723283648
139776723283648
>>> b.f is bb.f
False
>>> b.f is B.f
False
>>> a.f is b.f
False
>>> id(a.f) == id(b.f)
True
>>> A.f is B.f
False
>>> A.f == B.f
False
>>> id(A.f) == id(B.f)
True
```




### 6.4.3 静态方法

+ `@staticmethod`:将方法转换为静态方法
+ 静态方法不与实例绑定
+ 对于静态方法，不论通过实例或者类，都可以调用;且都是同一个对象

```doctest
>>> class D:
...     @staticmethod
...     def f():
...             print('staticmethod of D')
... 
>>> d=D()
>>> dd=D()
>>> d.f;dd.f;D.f
<function D.f at 0x7f204df0aca0>
<function D.f at 0x7f204df0aca0>
<function D.f at 0x7f204df0aca0>
>>> id(d.f);id(dd.f);id(D.f)
139776723299488
139776723299488
139776723299488
>>> d.f is dd.f
True
>>> d.f is D.f
True
>>> d.f();dd.f();D.f()
staticmethod of D
staticmethod of D
staticmethod of D
```






-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap6.md
[pre_chap]: chap6_3_attribute.md
[next_chap]: chap6_5_inheritance.md
