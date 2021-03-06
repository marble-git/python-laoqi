## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 6.12 元类

+ 实例对象由类实例化而来

+ 作为对象的类 由`type`类 实例化而来
+ 所有类都是type的实例， ***但元类还是type的子类***
+ type 是 根元类
+ 大多数内置类都是由type实例化来的
+ 元类(metaclass) [PEP 3115 -- Metaclasses in Python 3000](https://www.python.org/dev/peps/pep-3115/)
+ `__qualname__`: A dotted name showing the “path” from a module’s global scope to a class, function or method defined in that module, as defined in PEP 3155. For top-level functions and classes, the qualified name is the same as the object’s name:
	-  一个显示从从定义该对象的模块到到达该对象(类，函数，方法)所经路径的带.号的名字？对于top-level的类和方法，该名字就是该对象的名字

```
>>> class Foo:
...     class Bar:
...             pass
... 
>>> Foo.Bar.__name__
'Bar'
>>> Foo.Bar.__qualname__
'Foo.Bar'
```

+ 使用type定义类

```
>>> Foo = type('Foo',(),{})
>>> f = Foo()
>>> f.__class__
<class '__main__.Foo'>
>>> type(f)
<class '__main__.Foo'>
```

+ 由继承的知识可知，如果一个类继承自type,那么这个类就有了type的特征
+ 具有type特征的类也叫元类，类是元类的实例，根据元类可以创建类

```
>>> class Meta(type):
...     pass
... 
>>> class Spam(metaclass=Meta):
...     pass
... 
>>> s = Spam()
>>> type(s)
<class '__main__.Spam'>
>>> type(Spam)
<class '__main__.Meta'>
```

+ 类定义中 使用 关键字参数 metaclass 指明元类

+ 元类也是类，可以自定义元类的属性和方法来使所定义的元类具有某种特殊功能

+ [元类中的`__prepare__`方法 PEP 3115 -- Metaclasses in Python 3000](https://www.python.org/dev/peps/pep-3115/)

```python
root@kali-book:~/python-laoqi/chap6# cat-filter test.py 
'''
    filename:test.py
'''
import collections
print('-'*60)
class M(type):
    @classmethod
    def __prepare__(metacls,name,base):
        print('Meta __prepare__ called')
        print('metacls :',metacls)
        return collections.OrderedDict()
    def __new__(metacls,name,base,attr):
        print('Meta __new__ called')
        print('metacls :',metacls)
        return type.__new__(metacls,name,base,attr)
    def __init__(self,name,base,attr):
        print('Meta __init__ called')
        print('self :',self)
        return type.__init__(self,name,base,attr)
    def __call__(self):
        print('Meta __call__ called')
        print('self :',self)
        ins = type.__call__(self)
        print('ins :',ins)
        print('Meta __call__ ending')
        return ins
class D(metaclass = M):
    def __init__(self):
        print('D __init__ called')
        print('self :',self)
        print('D __init__ ending')
    def __new__(self):
        print('D __new__ called')
        print('self :',self)
        print('D __new__ ending')
        return super().__new__(self)
print('-'*40)
d=D()
print('d :',d)
root@kali-book:~/python-laoqi/chap6# python3 test.py 
------------------------------------------------------------
Meta __prepare__ called
metacls : <class '__main__.M'>
Meta __new__ called
metacls : <class '__main__.M'>
Meta __init__ called
self : <class '__main__.D'>
----------------------------------------
Meta __call__ called
self : <class '__main__.D'>
D __new__ called
self : <class '__main__.D'>
D __new__ ending
D __init__ called
self : <__main__.D object at 0x7f11381d9d60>
D __init__ ending
ins : <__main__.D object at 0x7f11381d9d60>
Meta __call__ ending
d : <__main__.D object at 0x7f11381d9d60>
```

+ `__prepare__(metacls,name,bases,**kwds)->attr_dict`只在元类中有用，且必须声明为 类方法(@classmethod)
+ [准备类命名空间](https://docs.python.org/zh-cn/3/reference/datamodel.html#preparing-the-class-namespace)一旦确定了适当的元类，则将准备好类命名空间。 如果元类具有 `__prepare__` 属性，它会以 `namespace = metaclass.__prepare__(name, bases, **kwds)` 的形式被调用（其中如果有任何额外的关键字参数，则应当来自类定义）。 `__prepare__` 方法应该被实现为 classmethod()。 `__prepare__` 所返回的命名空间会被传入 `__new__`，但是当最终的类对象被创建时，该命名空间会被拷贝到一个新的 dict 中；如果元类没有 `__prepare__` 属性，则类命名空间将初始化为一个空的有序映射。


+ type的 `__new__(metacls,name,bases,attr_dict)`方法 是类方法
+ 元类的 `__init__(inscls,name,bases,attr_dict)`方法接收由 `__new__`创建的 ***实例类***
+ 元类的 `__call__(inscls,*args,**kwargs)->obj`方法  ***在每次 实例类 进行实例化时调用，*** `type.__call__()` 会调用 `inscls.__new__` ; `metacls.__call__`的返回值 通常是inscls的实例


+ 使用元类实现单例模式


```
class Singleton(type):
    instance = {}
    def __call__(inscls,*args,**kwargs):
        if inscls not in inscls.instance:
            inscls.instance[inscls] = type.__call__(inscls,*args,**kwargs)
        return inscls.instance[inscls]
class Spam(metaclass = Singleton):pass
x = Spam()
y = Spam()
print(x)
print(x is y)
print(Singleton.__dict__)
print(Spam.__dict__)
print(x.__dict__)
root@kali-book:~/python-laoqi/chap6# python3 singleton_metaclass.py 
<__main__.Spam object at 0x7fa29693e3a0>
True
{'__module__': '__main__', 'instance': {<class '__main__.Spam'>: <__main__.Spam object at 0x7fa29693e3a0>}, '__call__': <function Singleton.__call__ at 0x7fa296841670>, '__doc__': None}
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Spam' objects>, '__weakref__': <attribute '__weakref__' of 'Spam' objects>, '__doc__': None}
{}
```




-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap6.md
[pre_chap]: chap6_11_generator.md
[next_chap]: ../2021-01-21-chap6.md
