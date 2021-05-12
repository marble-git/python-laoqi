## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 7.2 包

+ 包(package): 是有一定层次的目录结构，由“.py”文件(模块module),“子包”，“`__init__.py`”组成
+ Python不是纯粹的“解释”，“编译”型语言
+ 当目录中有了`__init__.py`后，就变成了一个包(package)
+ 如果一个包的目录下还有子目录，并且每个子目录都是“子包”，则必须在每个子目录中也增加`__init__.py`文件
+ 特别注意：如果让包中的模块作为执行程序，在该程序中不支持相对路径(`.`当前目录,`..`父级目录)的导入
	- 可以使用绝对路径 `import <module>` ;(path=mypackage/subA/abasic) `import apython`
	- 使用增加路径到`sys.path`,将包的路径加入Python解析器;`sys.path.append('/root/python-laoqi/docs/chap7/code')`


包 mypackage 的目录结构

```
root@kali-book:~/python-laoqi/docs/chap7/code# tree mypackage/
mypackage/
├── __init__.py
├── subA
│   ├── abasic.py
│   ├── apython.py
│   └── __init__.py
└── subB
    ├── brust.py
    └── __init__.py
```

相关文件中的代码

```
root@kali-book:~/python-laoqi/docs/chap7/code# cat mypackage/*/*
#coding=utf-8
'''
    path = ./mypackage/subA/abasic.py
    filename = abasic.py
'''
from . import apython
from ..subB import brust
print('in mypackage/subA/abasic.py')
basic = "BASIC-"+apython.python()+"-"+brust.rust
print(basic)
#coding=utf-8
'''
    path = ./mypackage/subA/apython.py
    filename = apython.py
'''
def python():
    print('in mypackage/subA/apython.py')
    return 'PYTHON'
print('in mypackage/subA/apython.py')
#coding=utf-8
'''
    path = ./mypackage/subB/brust.py
    filename = brust.py
'''
rust = 'RUST'
print('in mypackage/subB/brust.py :',rust)
```


在与包 mypackage 目录同级的位置创建 example_import.py 文件

```
root@kali-book:~/python-laoqi/docs/chap7/code# cat example_import.py 
#coding:utf-8
'''
    filename:example_import.py
    path : /root/python-laoqi/docs/chap7/code
'''
from mypackage.subA import abasic
if __name__ = '__main__':
    r = abasic.basic
    print(r)
```

执行这个程序

***这里将mypackage 目录及其子目录都看作包***


```
root@kali-book:~/python-laoqi/docs/chap7/code# python3 example_import.py 
in mypackage/subA/apython.py
in mypackage/subB/brust.py : RUST
in mypackage/subA/abasic.py
in mypackage/subA/apython.py
BASIC-PYTHON-RUST
BASIC-PYTHON-RUST
```

***不能在包内的模块中相对路径导入***
```
root@kali-book:~/python-laoqi/docs/chap7/code# cat mypackage/subA/abasic.py 
#coding=utf-8
'''
    path = ./mypackage/subA/abasic.py
    filename = abasic.py
'''
from . import apython
from ..subB import brust
print('in mypackage/subA/abasic.py')
basic = "BASIC-"+apython.python()+"-"+brust.rust
print(basic)
root@kali-book:~/python-laoqi/docs/chap7/code# python3  mypackage/subA/abasic.py 
Traceback (most recent call last):
  File "/root/python-laoqi/docs/chap7/code/mypackage/subA/abasic.py", line 7, in <module>
    from . import apython
ImportError: attempted relative import with no known parent package
```





+ 包是一种通过用“带点号的模块名”来构造 Python 模块命名空间的方法。 
	-例如，模块名 A.B 表示 A 包中名为 B 的子模块。
+ 正如 **模块的使用** 使得 **不同模块** 的作者 **不必担心彼此的全局变量名称一样** 
+ 使用 **加点的模块名** 可以使得 NumPy 或 Pillow 等 **多模块软件包** 的作者 **不必担心彼此的模块名称一样**


+ 当使用 `from package import item` 时，
	- **item可以是包的子模块（或子包）** ，
	- **也可以是包中定义的其他名称，如函数，类或变量。** 
	- import 语句首先测试是否在包中定义了item；如果没有，它假定它是一个模块并尝试加载它。如果找不到它，则引发 ImportError 异常。

+ 相反，当使用 `import item.subitem.subsubitem` 这样的语法时，
	- 除了 **最后一项之外** 的每一项 **都必须是一个包** ；
	- ***最后一项*** 可以 **是模块或包** ，但 ***不能是*** 前一项中定义的 ***类或函数或变量*** 。

+ 请注意， **相对导入** 是 **基于当前模块的名称** 进行导入的。
	- 由于  ***主模块的名称总是 "`__main__`"***
	- 因此用作Python应用程序 ***主模块*** 的模块 ***必须始终使用绝对导入***


+ 6.4.3. 多个目录中的包
	- 包支持另一个特殊属性， __path__ 。
	- 它被初始化为一个列表，
	- 其中包含在执行该文件中的代码之前保存包的文件 __init__.py 的目录的名称。
	- 这个变量可以修改；这样做会影响将来对包中包含的模块和子包的搜索。
	- 虽然通常不需要此功能，但它可用于扩展程序包中的模块集。



```
5.4.5. module.__path__
根据定义，如果一个模块具有 __path__ 属性，它就是包。
包的 __path__ 属性会在导入其子包期间被使用。 在导入机制内部，它的功能与 sys.path 基本相同，即在导入期间提供一个模块搜索位置列表。 但是，__path__ 通常会比 sys.path 受到更多限制。
__path__ 必须是由字符串组成的可迭代对象，但它也可以为空。 作用于 sys.path 的规则同样适用于包的 __path__，并且 sys.path_hooks (见下文) 会在遍历包的 __path__ 时被查询。
包的 __init__.py 文件可以设置或更改包的 __path__ 属性，而且这是在 PEP 420 之前实现命名空间包的典型方式。 随着 PEP 420 的引入，命名空间包不再需要提供仅包含 __path__ 操控代码的 __init__.py 文件；导入机制会自动为命名空间包正确地设置 __path__
```


```
root@kali-book:~/python-laoqi/docs/chap7/code# python3
Python 3.9.1 (default, Dec  8 2020, 07:51:42) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mypackage
>>> mypackage.__package__
'mypackage'
>>> mypackage.__path__
['/root/python-laoqi/docs/chap7/code/mypackage']
>>> mypackage.subA.__path__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'mypackage' has no attribute 'subA'
>>> import mypackage.subA
>>> mypackage.subA.__path__
['/root/python-laoqi/docs/chap7/code/mypackage/subA']
>>> mypackage.subA.__package__
'mypackage.subA'
>>> mypackage.subA.apython.__package__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'mypackage.subA' has no attribute 'apython'
>>> import mypackage.subA.apython
in mypackage/subA/apython.py
>>> mypackage.subA.apython.__package__
'mypackage.subA'
>>> mypackage.subA.apython.__path__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'mypackage.subA.apython' has no attribute '__path__'
```




-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap7.md
[pre_chap]: chap7_1_module.md
[next_chap]: chap7_3_standard_library.md
