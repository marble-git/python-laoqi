## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------


## 6.7 封装和私有化

+ Python中通过 **私有化** 的方式 ***实现封装***
+ 封装(Encapsulation):是指 对具体对象的一种抽象，即将某些部分隐藏起来，使外部程序无法访问，调用
+ Python中，封装就是对某些方法和属性的“私有化”，将其应用权限限制在某个区域内，外部无法调用
+ Python中，私有化通过在将要“私有化”的对象名字(`name`)前 添加双下划线(`__name`)
+ 名称改写(name mangling):`__name`-->`_clsname__name`，是一种安全措施，目的是避免意外访问，不能防止故意做错事

+ 私有化用于: 避免子类意外覆盖父类的“私有”属性
+ [单下划线与双下划线的区别](https://www.cnblogs.com/linwenbin/p/10370198.html)

```doctest
>>> class Foo:
...     me = 'me me'
...     _name = 'my name'
...     __book = 'python book'
...     def get_book(self):
...             print(self.__book)
...     def __code(self):
...             print('__code')
... 
>>> f = Foo()
>>> f.me;Foo.me
'me me'
'me me'
>>> f._name;Foo._name
'my name'
'my name'
>>> f.__book
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Foo' object has no attribute '__book'
>>> Foo.__book
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Foo' has no attribute '__book'
>>> f.get_book();Foo.get_book(f)
python book
python book
>>> f.__code()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Foo' object has no attribute '__code'
>>> Foo.__code()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Foo' has no attribute '__code'
>>> dir(f)
['_Foo__book', '_Foo__code', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_name', 'get_book', 'me']
>>> dir(Foo)
['_Foo__book', '_Foo__code', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_name', 'get_book', 'me']
>>> f.__dict__
{}
>>> Foo.__dict__
mappingproxy({'__module__': '__main__', 'me': 'me me', '_name': 'my name', '_Foo__book': 'python book', 'get_book': <function Foo.get_book at 0x7ff3c7fcea60>, '_Foo__code': <function Foo.__code at 0x7ff3c7fceaf0>, '__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None})
>>> f._Foo__book;Foo._Foo__book
'python book'
'python book'
>>> f._Foo__code();Foo._Foo__code(f)
__code
__code
```

+ 两个极端情况:外部不能访问(`__name`),外部可以调用和修改(`name`)
+ 中间情况:属性可以在外部访问，但是不能修改 ***property***

```doctest
>>> help(property)
Help on class property in module builtins:
class property(object)
 |  property(fget=None, fset=None, fdel=None, doc=None)
 |  
 |  Property attribute.
 |  
 |    fget
 |      function to be used for getting an attribute value
 |    fset
 |      function to be used for setting an attribute value
 |    fdel
 |      function to be used for del'ing an attribute
 |    doc
 |      docstring
 |  
 |  Typical use is to define a managed attribute x:
 |  
 |  class C(object):
 |      def getx(self): return self._x
 |      def setx(self, value): self._x = value
 |      def delx(self): del self._x
 |      x = property(getx, setx, delx, "I'm the 'x' property.")
 |  
 |  Decorators make defining new properties or modifying existing ones easy:
 |  
 |  class C(object):
 |      @property
 |      def x(self):
 |          "I am the 'x' property."
 |          return self._x
 |      @x.setter
 |      def x(self, value):
 |          self._x = value
 |      @x.deleter
 |      def x(self):
 |          del self._x
```

+ 测试property
```python
#coding:utf-8
'''
    filename:property_test.py
'''
class Book:
    def __init__(self):
        self.__book = 'None book'
    @property
    def book(self):
        print('getting book name')
        return self.__book
    @book.setter
    def book(self,book):
        print('setting book name')
        self.__book=book
    @book.deleter
    def book(self):
        print('deleting book')
        del self.__book
b = Book()
print(b.book)
b.book = 'python'
print(b.book)
del b.book
print(b.book)
[out:]
root@kali-book:~/python-laoqi/chap6# python3 property_test.py 
getting book name
None book
setting book name
getting book name
python
deleting book
getting book name
Traceback (most recent call last):
  File "/root/python-laoqi/chap6/property_test.py", line 30, in <module>
    print(b.book)
  File "/root/python-laoqi/chap6/property_test.py", line 14, in book
    return self.__book
AttributeError: 'Book' object has no attribute '_Book__book'
```







-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap6.md
[pre_chap]: chap6_6_polymorphism.md
[next_chap]: chap6_8_custom_object_types.md
