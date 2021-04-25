## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------


## 6.2 简单的类

+ 类定义
```pybnf
classdef    ::=  [decorators] "class" classname [inheritance] ":" suite
inheritance ::=  "(" [argument_list] ")"
classname   ::=  identifier
```

### 6.2.1 创建类


+ 类的常规结构分解
+ `class`: 关键字，用来声明此处要创建一个类
+ `SuperMan`: 类名，由每个单词的首字母大写拼接组成 驼峰式
+ `:` 类名称后紧跟 英文状态下的冒号，类名后没有 `()` 
+ 后面为类的代码块，相对类定义缩进一级
+ 3引号内的为 "类的文档"
+ `def` 定义类的方法，必须有第一个参数代指由类创建的具体实例，`self`是惯例命名
+ `__init__`: 初始化方法 **没有返回值(return None)** 实例化的时候由解析器自动调用
+ 由双下划线开始和结尾的方法，统称"特殊方法"

```python
class SuperMan:
    '''
    A class of superman
    '''
    def __init__(self,name):
        self.name = name
        self.gender = 1 #1,male
        self.single = False
        self.illness = False
    def nine_negative_kungfu(self):
        return 'Ya! You have to die.'
```



### 6.2.2 实例

+ 名称表示对象，`()`才是执行
+ `Foo()` 表示执行类，即进行实例化，得到类的一个实例
+ Foo 和 int 地位一样
+ 解释器  **隐式传递** 实例对象给方法中的`self` 参数

```
>>> SuperMan.nine_negative_kungfu(z3)
'Ya! You have to die.'
>>> z3.nine_negative_kungfu()
'Ya! You have to die.'
```



```doctest
>>> class Foo:
...     pass
... 
>>> Foo
<class '__main__.Foo'>
>>> Foo()
<__main__.Foo object at 0x7fc1e0726700>
>>> type(Foo)
<class 'type'>
>>> id(Foo)
43898912
>>> type(Foo())
<class '__main__.Foo'>
>>> int
<class 'int'>
>>> type(int)
<class 'type'>
>>> id(int)
9461536
```















-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
