## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------


# 第7章 模块和包

+ 重要的物理规律: 熵增加原理
+ Python 的生态环境是开放的，所以它不会热寂，能够保持发展的活力。
+ Python 中的模块和包就是其开放的重要体现之一，任何人都可以“造轮子”和“用轮子”


## 7.1 模块

+ Python 中的模块(module):就是拓展名为`.py`的文件
+ module -- 模块: 此对象是 Python 代码的一种组织单位。各模块具有独立的命名空间，可包含任意 Python 对象。模块可通过 importing 操作被加载到 Python 中。
+ `sys.path`:  
	- 一个 **由字符串组成的列表，用于指定模块的搜索路径** 。初始化自环境变量 PYTHONPATH，再加上一条与安装有关的默认路径。
	- 程序启动时将初始化本列表，列表的第一项 path[0] 目录含有调用 Python 解释器的脚本。如果脚本目录不可用（比如以交互方式调用了解释器，或脚本是从标准输入中读取的），则 path[0] 为空字符串，这将导致 Python 优先搜索当前目录中的模块。注意，脚本目录将插入在 PYTHONPATH 的条目*之前*。
	- 程序可以随意修改本列表用于自己的目的。只能向 sys.path 中添加 string 和 bytes 类型，其他数据类型将在导入期间被忽略。
+ 特别注意: **导入模块时，不要写拓展名`.py`**



```doctest
root@kali-book:~/python-laoqi/docs/chap7/code# vim moduleexample.py 
root@kali-book:~/python-laoqi/docs/chap7/code# pwd
/root/python-laoqi/docs/chap7/code
root@kali-book:~/python-laoqi/docs/chap7/code# cd
root@kali-book:~# python3
Python 3.9.1 (default, Dec  8 2020, 07:51:42) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> import moduleexample
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'moduleexample'
>>> print(sys.path)
['', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/usr/local/lib/python3.9/dist-packages', '/usr/local/lib/python3.9/dist-packages/wikitables-0.5.4-py3.9.egg', '/usr/local/lib/python3.9/dist-packages/mwparserfromhell-0.6-py3.9-linux-x86_64.egg', '/usr/lib/python3/dist-packages']
>>> sys.path.append('/root/python-laoqi/docs/chap7/code')
>>> print(sys.path)
['', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/usr/local/lib/python3.9/dist-packages', '/usr/local/lib/python3.9/dist-packages/wikitables-0.5.4-py3.9.egg', '/usr/local/lib/python3.9/dist-packages/mwparserfromhell-0.6-py3.9-linux-x86_64.egg', '/usr/lib/python3/dist-packages', '/root/python-laoqi/docs/chap7/code']
>>> import moduleexample
>>> dir(moduleexample)
['Book', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'foo', 'mul_result', 'python_name', 'python_var']
>>> book = moduleexample.Book('laoqiiii')
>>> boo
book   bool(  
>>> book.get_name()
'laoqiiii'
>>> moduleexample.mul_result
4
>>> moduleexample.python_var
<moduleexample.Book object at 0x7f4628e6ce50>
>>> moduleexample.python_name
'laoqi'
```


+ 观察`dir()`函数的返回结果，可以发现，在该文件中所定义的类，函数都已经作为模块的一部分显示出来
+ 仔细观察，还可以发现，文件moduleexample.py中调用函数和类的变量名称也呈现出来了，这些测试代码对模块的使用者没有意义，但开发测试模块时又是必须的
+ 解决办法: `if __name__ == "__main__":`
+ `__name__`:  属性必须被设为模块的完整限定名称。 此名称被用来在导入系统中唯一地标识模块
+ `__main__` --- 顶层脚本环境


```
'__main__' 是顶层代码执行的作用域的名称。模块的 __name__ 在通过标准输入、脚本文件或是交互式命令读入的时候会等于 '__main__'。
模块可以通过检查自己的 __name__ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 python -m 运行时条件性地执行一些代码，而在被 import 时不会执行。
if __name__ == "__main__":
    # execute only if run as a script
    main()
对软件包来说，通过加入 __main__.py 模块可以达到同样的效果，当使用 -m 运行模块时，其中的代码会被执行。
```


+ `__file__`：当前module所在的文件的路径。
+ `__package__`：当前module所在的包名。如果没有，为None。



```
__file__: /root/python-laoqi/docs/chap7/code/moduleexample.py
__package__: None
```



+ `__all__` : 模块公开接口的一种约定
	- 可以在模块级别暴露接口
	- 以提供了 ***白名单*** 的形式暴露接口
	- 其他文件中使用 `from <module> import *` 导入文件时，只会导入 `__all__`列出的成员，其他成员都被排除在外
	- `__all__` 的形式都是list类型
	- 不能动态生成(列表解析)；作用是定义公开接口，需要以字面量的形式显示写出来
	- 不应该在非临时代码(console)中使用`from <modue> import *` 语法
	- 按照PEP8建议的风格，`__all__`应该写在所有import 语句的下面;函数，类，常量等成员定义的上面
	- 如果一个模块需要暴露的接口改动频繁，`__all__`可以这样定义:
	- 这样修改一个暴露的接口只修改1行，方便版本控制的时候看 diff;最后多出的逗号在Python中是允许的，符合PEP8风格


```
__all__ = [
        'Book',
        'GLOBALVAR',
        ]
```


-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap7.md
[pre_chap]: ../2021-01-21-chap7.md
[next_chap]: chap7_2_package.md
