## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

# 第6章 类

+ 类 即 ***class***

## 6.1 面向对象

+ 对象的概念


### 6.1.1 对象和面向对象

+ **对象(object)** : 是 **面向对象** 中的术语,既表示客观世界 [问题空间(namespace?problem_space)](https://chi.jinzhao.wiki/wiki/%E9%97%AE%E9%A2%98%E7%A9%BA%E9%97%B4) 中的某个具体的事物,又表示软件系统解空间中的基本元素
+ Grandy Booch 对`对象`的定义:
	- **对象(Object)** :一个对象有自己的 **状态** , **行为** 和 **唯一的标识** ;所有相同类型的对象所具有的结构和行为在他们共同的类中被定义
	- **状态(State)** :包括这个 **对象已有的属性(类属性,通常是类里面已经定义好的)** ,再加上对象具有的 **当前属性值(实例属性,这些属性往往是动态的)**
	- **行为(Behavior)** :指一个 **对象如何影响外界及被外界影响(方法)** ,表现为对象自身状态的改变和信息的传递
	- **标识(Identity)** :指一个对象所具有的区别于所有其他对象的属性(本质上指内存中所创建的对象的地址)
+ [**面向对象程序设计(OOP)**](https://chi.jinzhao.wiki/wiki/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1) :是种具有对象概念的编程典范，同时也是一种程序开发的抽象方针。它可能包含数据、属性、代码与方法。对象则指的是类（class）的实例。它将对象作为程序的基本单元，将程序和数据封装其中，以提高软件的重用性、灵活性和扩展性，对象里的程序可以访问及经常修改对象相关连的数据。在面向对象程序编程里，计算机程序会被设计成彼此相关的对象



### 6.1.2 类的概述

+ [**类(Class)**](https://chi.jinzhao.wiki/wiki/%E7%B1%BB_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6)) :是一种面向对象计算机编程语言的构造,是创建对象的蓝图,描述了 **所创建的对象的共同的属性和方法**

+ **实例** :由`类`创建的对象,也称为实例(instance)。
+ **实例化** :根据"类"得到"实例"的过程叫做"实例化"或者"创建实例"



+ `isinstance()` 判断一个对象是否为某个或某些对象的实例
+ `issubclass()` 判断一个类是否为某个或某些对象的子类
```python
>>> help(isinstance)
Help on built-in function isinstance in module builtins:
isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.
    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
(END)
>>> help(issubclass)
Help on built-in function issubclass in module builtins:
issubclass(cls, class_or_tuple, /)
    Return whether 'cls' is a derived from another class or is the same class.
    A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
    or ...`` etc.
(END)
```

-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
