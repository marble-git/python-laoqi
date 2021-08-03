## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------


# 第9章 读写文件

+ 文件:在日常社会生活和计算机系统中都占有重要位置
	- 一般文件的读写方法
	- 特定文件格式的专门读写工具




## 9.1 简单文件操作


### 9.1.1 新建文件

+ 要操作文件，必须有文件，如果没有，就创建一个

```
>>> import os
>>> os.getcwd()
'/root'
>>> f = open('raise.txt','w')
>>> f
<_io.TextIOWrapper name='raise.txt' mode='w' encoding='UTF-8'>
>>> type(f)
<class '_io.TextIOWrapper'>
>>> f.write('You raise me up.')
16
>>> f.close()
```

+ 创建，写入，关闭，文件的3个步骤如下
	- 使用`open()`打开(新建)文件
	- `open()` 返回的是一个对象，使用文件对象的`write()`方法实现向文件中写入字符串功能
	- 写入之后，一定要进行`close()`操作，否则对文件的修改没有保存到硬盘中

```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)¶
打开 file 并返回对应的 file object。 如果该文件不能被打开，则引发 OSError。 请参阅 读写文件 获取此函数的更多用法示例。

file 是一个 path-like object，表示将要打开的文件的路径（绝对路径或者当前工作目录的相对路径），也可以是要被封装的整数类型文件描述符。（如果是文件描述符，它会随着返回的 I/O 对象关闭而关闭，除非 closefd 被设为 False 。）

mode 是一个可选字符串，用于指定打开文件的模式。默认值是 'r' ，这意味着它以文本模式打开并读取。其他常见模式有：写入 'w' （截断已经存在的文件）；排它性创建 'x' ；追加写 'a' （在 一些 Unix 系统上，无论当前的文件指针在什么位置，所有 写入都会追加到文件末尾）。在文本模式，如果 encoding 没有指定，则根据平台来决定使用的编码：使用 locale.getpreferredencoding(False) 来获取本地编码。（要读取和写入原始字节，请使用二进制模式并不要指定 encoding。）可用的模式有
```

+ 常用文件打开方式

字符|意义				|文件未存在		|文件已存在
----|-----------------------------------|-----------------------|---------
'r'|读取（默认）			|`FileNotFoundError`	|`<_io.TextIOWrapper name='rt' mode='rt' encoding='UTF-8'>`
'w'|写入，并先截断文件			|`<_io.TextIOWrapper name='wt' mode='wt' encoding='UTF-8'>`|`same`
'x'|排它性创建，如果文件已存在则失败	|`<_io.TextIOWrapper name='xt' mode='xt' encoding='UTF-8'>`|`FileExistsError`
'a'|写入，如果文件存在则在末尾追加	|`<_io.TextIOWrapper name='at' mode='at' encoding='UTF-8'>`|`same`
'b'|二进制模式				|''|''
't'|文本模式（默认）			|''|''
'+'|打开用于更新(读取与写入i)		|''|''


+ `[rwxa]+` mode

mode	|readable|writable|override已存在文件
--------|:-----:|:------:|:------:
'r+'	|True	|True	|False;文件不存在失败
'w+'	|True	|True	|True
'x+'	|True	|True	|文件已存在则失败
'a+'	|True	|True	|False


### 9.1.2 读文件

+ `<class '_io.TextIOWrapper'>` : open函数返回的对象类型
+ `I/O`: 就是Input/Output
	- `print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)`函数也属于`I/O`,只不过是输出在控制台界面
	- 文件是另一种形式的`I/O`
+ Python的标准库中有针对I/O的模块，即 [**io**](https://docs.python.org/zh-cn/3.9/library/io.html)
+ io的基本作用:[io — Core tools for working with streams(处理流的核心工具)](https://docs.python.org/zh-cn/3.9/library/io.html)
+ 对于I/O而言，所有的输入，输出内容都可以看作数据流(stream,“流”)
+ 打开文件所用的内置函数open也是io模块来定义的

```
>>> import io
>>> help(io)
DESCRIPTION
    The io module provides the Python interfaces to stream handling. The builtin open function is defined in this module.
```

+ `_io`是`io`的C语言表达，在Python中会对某些模块用C语言重写,以进一步提高其运行速度，相应的模块名称就由`modulename`变为了`_modulename`形式

```
>>> import io
>>> import _io
>>> io
<module 'io' from '/usr/lib/python3.9/io.py'>
>>> _io
<module 'io' (built-in)>
```

+ `open('raise.txt')`得到的对象，是io模块的`TextIOWrapper`类的实例对象，称之为 **文件对象(file object)**

+ 文件对象的属性和方法

```
>>> f
<_io.TextIOWrapper name='a+' mode='a+' encoding='UTF-8'>
>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
>>> hasattr(f,'__next__')
True
>>> hasattr(f,'__iter__')
True
```

+ 文件对象包含了`__iter__,__next__`方法，是迭代器对象
	- 可以对`file object` 使用for循环

```
>>> f = open('raise.txt')
>>> for line in f:
...     print(line,end='')
... 
You raise me up.
so I can stand on mountains.
You raise me up to walk on stormy seas.
I am on your shoulders.
You raise me up to more than I can be.
>>> f.read()
''
>>> f.tell()
149
>>> f.seek(0)
0
>>> f.read()
'You raise me up.\nso I can stand on mountains.\nYou raise me up to walk on stormy seas.\nI am on your shoulders.\nYou raise me up to more than I can be.\n'
```

+  文件对象是迭代器，在for循环过程中，"指针"也随之移动，当循环结束时，指针就移动到了文件的最后
+ 如果试图再次读取内容，返回的就是 **空** 了
+ 文件对象的方法中提供了 **移动文件指针的方法`seek()`**

```
>>> help(f.seek)

Help on built-in function seek:

seek(cookie, whence=0, /) method of _io.TextIOWrapper instance
    Change stream position.
    
    Change the stream position to the given byte offset. The offset is
    interpreted relative to the position indicated by whence.  Values
    for whence are:
    
    * 0 -- start of stream (the default); offset should be zero or positive
    * 1 -- current stream position; offset may be negative
    * 2 -- end of stream; offset is usually negative
    
    Return the new absolute position.
(END)
>>> f.seek(0)
0
>>> f.read(3)
'You'
>>> f.readline()
' raise me up.\n'
>>> f.readlines()
['so I can stand on mountains.\n', 'You raise me up to walk on stormy seas.\n', 'I am on your shoulders.\n', 'You raise me up to more than I can be.\n']
```

+ 在使用seek（）函数时，有时候会报错为  “io.UnsupportedOperation: can't do nonzero cur-relative seeks”
+ 照理说，按照seek()方法的格式file.seek(offset,whence)，后面的1代表从当前位置开始算起进行偏移，那又为什么报错呢？
+ 这是因为，在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始计算相对位置，从文件尾计算时就会引发异常。 ***将打开模式改为`b`二进制，即可使用seek的相对(当前指针位置，文件尾)进行移动***

f = open("aaa.txt","rb")   就可以了

```
>>> f = open('raise.txt','r+b')
>>> f.read()
b'You raise me up.\nso I can stand on mountains.\nYou raise me up to walk on stormy seas.\nI am on your shoulders.\nYou raise me up to more than I can be.\n'
>>> f.seek(-10,2)
139
>>> f.tell()
139
>>> f.read()
b'I can be.\n'
>>> f.seek(-20,1)
129
>>> f.seek(-20,1)
109
>>> f.readlines()
[b'\n', b'You raise me up to more than I can be.\n']
```

+ 用print函数将要打印的内容输出到一个文件中

```
>>> with open('printfile.txt','wt') as pf:
...     print('you need python',file=pf)
... 
>>> open('printfile.txt').read()
'you need python\n'
```


+ `readable,read,readline,readlines`
	- **readable()** :如果可以读取流，则返回 True 。否则为 False ，且 read() 将引发 OSError 错误。
	- **read(size=-1)**:从流中读取至多 size 个字符并以单个 str 的形式返回。 如果 size 为负值或 None，则读取至 EOF。
	- **readline(size=-1)**:从流中读取并返回一行。如果指定了 size，将至多读取 size 个字节。对于二进制文件行结束符总是 b'\n'；对于文本文件，可以用将 newline 参数传给 open() 的方式来选择要识别的行结束符。
	- **readlines(hint=-1)**:从流中读取并返回包含多行的列表。可以指定 hint 来控制要读取的行数：如果（以字节/字符数表示的）所有行的总大小超出了 hint 则将不会读取更多的行。

+ 请注意使用 for line in file: ... 就足够对文件对象进行迭代了，可以不必调用 file.readlines()。
	- readable: 查看文件对象是否 可读
	- read: size参数指定最多读取的字符数
	- readline: size参数指定读取的一行中的字符最大数目
	- readlines: hint参数 如果 **hint大于等于前n行的总字数** 但小于前n+1行的总字数，则执行函数会读取文件的前n+1行


```
>>> f = open('lines')
>>> f.read(23)
'line0\nline1\nline2\nline3'
>>> f.readline()
'\n'
>>> f.readline()
'line4\n'
>>> f.readline(2)
'li'
>>> f.readline(20)
'ne5\n'
>>> f.readline(20)
'line6\n'
>>> f.readlines(2)
['line7\n']
>>> f.readlines(2)
['line8\n']
>>> f.readlines(5)
['line9\n']
>>> f.readlines(20)
['line10\n', 'line11\n', 'line12\n']
>>> f.readlines(15)
['line13\n', 'line14\n', 'line15\n']
>>> f.readlines(22)
['line16\n', 'line17\n', 'line18\n', 'line19\n']
```




+ writable,write,writelines,write_through
	- **writable()**:如果流支持写入则返回 True。 如为 False，则 write() 和 truncate() 将引发 OSError。
	- **write(s)**:将字符串 s 写入到流并返回写入的字符数。
	- **writelines(lines)**:将行列表写入到流。 不会添加行分隔符，因此通常所提供的每一行都带有末尾行分隔符。
+ writable: 判断文件对象是否可写
+ write: s 参数，要写入的字符串，返回写入的字符数
+ writelines: lines参数，要写入到流的行的列表，不自动添加行分割符号

```
>>> f = open('writefile','wt')
>>> f.writable()
True
>>> f.write('this is the write file.\n')
24
>>> lines = ['writeline'+str(i)+'\n' for i in range(10)]
>>> lines
['writeline0\n', 'writeline1\n', 'writeline2\n', 'writeline3\n', 'writeline4\n', 'writeline5\n', 'writeline6\n', 'writeline7\n', 'writeline8\n', 'writeline9\n']
>>> f.writelines(lines)
>>> f.close()
root@kali-book:~/file_opens# cat writefile 
this is the write file.
writeline0
writeline1
writeline2
writeline3
writeline4
writeline5
writeline6
writeline7
writeline8
writeline9
```




+ ***上下文管理器和 with块*** : <<Fluent Python>> 15.2 p370

+ [with 语句](https://docs.python.org/zh-cn/3.9/reference/compound_stmts.html#the-with-statement)

```
with 语句用于包装带有使用上下文管理器 (参见 with 语句上下文管理器 一节) 定义的方法的代码块的执行。 这允许对普通的 try...except...finally 使用模式进行封装以方便地重用。
with_stmt ::=  "with" with_item ("," with_item)* ":" suite
with_item ::=  expression ["as" target]
带有一个“with_item”的 with 语句的执行过程如下:
1. 对上下文表达式 (在 with_item 中给出的表达式) 求值以获得一个上下文管理器。
2. 载入上下文管理器的 __enter__() 以便后续使用。
3. 载入上下文管理器的 __exit__() 以便后续使用。
4. 发起调用上下文管理器的 __enter__() 方法。
5. 如果 with 语句中包含一个目标，来自 __enter__() 的返回值将被赋值给它。
注解 with 语句会保证如果 __enter__() 方法返回时未发生错误，则 __exit__() 将总是被调用。 因此，如果在对目标列表赋值期间发生错误，则会将其视为在语句体内部发生的错误。 参见下面的第 6 步。
6. 执行语句体。
7. 发起调用上下文管理器的 __exit__() 方法。 如果语句体的退出是由异常导致的，则其类型、值和回溯信息将被作为参数传递给 __exit__()。 否则的话，将提供三个 None 参数。
如果语句体的退出是由异常导致的，并且来自 __exit__() 方法的返回值为假，则该异常会被重新引发。 如果返回值为真，则该异常会被抑制，并会继续执行 with 语句之后的语句。
如果语句体由于异常以外的任何原因退出，则来自 __exit__() 的返回值会被忽略，并会在该类退出正常的发生位置继续执行。
```

+ 上下文管理器对象存在的目的是管理with语句
+ 就像迭代器的存在是为了管理for语句一样
+ `with` 语句的目的是简化 `try/finally` 模式:
	- 用于保证一段代码运行完毕后执行某项操作
	- 即使那段代码由于 *异常,return,sys.exit()* 而中止，也会执行指定的操作
	- finally 子句中的代码通常用于 *释放重要资源,或还原临时变更的状态*

+ 上下文管理器协议：
	- `__enter__`方法: with语句开始运行时，会在 *上下文管理器对象(with_item 的求值结果)* 上调用该方法
	- `__exit__`方法: with语句运行结束后，会在上下文管理器对象上调用该方法，以此扮演finally子句的角色

+ ***执行with后面的表达式得到的结果是上下文管理器对象*** 
+ 把 *值* 绑定到目标变量(as 子句) **是** ***在上下文管理器上调用`__enter__` 方法的返回结果***


+ 如果语句体的退出是由异常导致的，
	- 并且来自 __exit__() 方法的返回值为假，
	- 则该异常会被重新引发。 
	- 如果返回值为真，
	- 则该异常会被抑制，并会继续执行 with 语句之后的语句。

+ 如果语句体由于异常以外的任何原因退出，
	- 则来自 __exit__() 的返回值会被忽略，
	- 并会在该类退出正常的发生位置继续执行


```python
#测试LookingGlass上下文管理器类
>>> from mirror import *
>>> with LookingGlass() as what:
...     print('Alice, Kitty and Snowdrop')
...     print(what)
... 
Enter
pordwonS dna yttiK ,ecilA
4321DCBA
tixE
>>> what
'ABCD1234'
>>> print('back to normal')
back to normal
>>> 

#mirror.py LookingGlass上下文管理器类的代码
#coding:utf-8

'''
    filename:mirror.py
    <fluent python,p372>
    with,contextmanager
'''


class LookingGlass:
    def __enter__(self):
        print('Enter')
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'ABCD1234'
    def reverse_write(self,text):
        self.original_write(text[::-1])
    def __exit__(self,exc_type,exc_value,traceback):
        print('Exit')
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('please DO NOT divide by zero')
            return True

#在with块之外使用LookingGlass类
>>> from mirror import *
>>> manager = LookingGlass()
>>> manager
<mirror.LookingGlass object at 0x7efe104b9be0>
>>> monster = manager.__enter__()
Enter
>>> manager
>0eb9b401efe7x0 ta tcejbo ssalGgnikooL.rorrim<
>>> monster
'4321DCBA'
>>> True
eurT
>>> import sys
>>> manager.__exit__(*sys.exc_info())
tixE
>>> monster
'ABCD1234'
#测试异常处理
>>> with LookingGlass() as lg:
...     1/0
... 
Enter
tixE
please DO NOT divide by zero
>>> with LookingGlass() as lg:
...     raise ValueError('wrong value!')
... 
Enter
tixE
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: wrong value!
```

+ [***contextlib 模块中的实用工具***](https://docs.python.org/zh-cn/3.9/library/contextlib.html)




+ `closing(thing)`: 如果对象提供了close()方法，但没有实现`__enter__/__exit__`协议，那么可以使用这个函数构建上下文管理器
+ 返回一个在语句块执行完成时关闭things的上下文管理器

```python
#基本上等价于：
from contextlib import contextmanager

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
#使用样例
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)
```

+ `suppress(*exceptions)`:构建临时忽略指定异常的上下文管理器
+ 返回一个上下文管理器，如果任何一个指定的异常发生在使用该上下文管理器的 with 语句中，该异常将被它抑制，然后程序将从 with 语句结束后的第一个语句开始恢复执行。
+ 与完全抑制异常的任何其他机制一样，该上下文管理器应当只用来抑制非常具体的错误，并确保该场景下静默地继续执行程序是通用的正确做法。

```python
#使用实例
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('somefile.tmp')

#这段代码等价于：
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass
```

+ `redirect_stdout(new_target)`:用于将sys.stdout临时重定向到 **一个文件，或类文件对象** 的上下文管理器
+ 该工具给已有的将输出硬编码写到stdout的函数或者类提供了额外的灵活性

```python
#使用实例
#1 捕获标准输出到一个字符串中
f = io.StringIO()
with redirect_stdout(f):
    help(pow)
s=f.getvalue()
print(s)

#2 把标准输出写到磁盘文件中，重定向输出到一个常规文件
with open('help.txt','wt') as f:
    with redirect_stdout(f):
        help(pow)
#3 把标准输出重定向到标准错误
with redirect_stdout(sys.stderr):
    print(something)
```

+ **注意** : sys.stdout的全局副作用意味着此上下文管理器
	- 不适合在库代码和大多数多线程应用程序中使用
	- 它对子线程的输出没有影响
	- 不过对于许多工具脚本而言，它仍然是一个有用的方法

+ [3.4版contextlib.py源码](https://hg.python.org/cpython/file/3.4/Lib/contextlib.py#134)

+ `@contextmanager`: 这个装饰器把简单的生成器函数变成上下文管理器，这样就不用创建类去实现管理器协议了

+ `@comtextmanager` 装饰器能减少创建上下文管理器的样板代码量
	- 因为不用编写一个完整的类
	- 定义`__enter__/__exit__`方法
	- 只需实现有一个yield语句的生成器
	- 生成想让`__enter__`方法返回的值
+ 在使用`@contextmanager`装饰的生成器中，
	- yield语句的作用是把函数的定义体分为2部分
	- yield语句前面的所有代码在with块开始时执行(`__enter__`)
	- yield语句后面的代码在with块结束时(`__exit__`)执行

+ 使用定义类的方式定义上下文管理器时
	- `__exit__`方法返回True时
	- 解释器会supress异常
	- 如果没有显示返回一个真值，with语句结束后解释器会重新引发异常
+ 使用`@contextmanager`装饰器定义上下文管理器时
	- 默认行为是相反的
	- 装饰器提供的`__exit__`方法假定发给生成器的所有异常都得到处理了，因此应该压制异常(把异常发给生成器的方式是使用throw方法)
	- 如果不想让`@contextmanager`压制异常，必须在被装饰的函数中 **显式重新抛出异常(raise exception)或返回值(return value,导致抛出异常`StopIteration value`)**


+ **注意** : 使用`@contextmanager`装饰器时，要把yield语句放在 ***try/finally*** 语句中(或者with语句中)，这是无法避免的，因为我们永远不知道上下文管理器的用户会在with块中做什么

```python
#测试
>>> from mirror_gen import *
>>> with looking_glass() as f:
...     raise ValueError('asd')
... 
Enter gen
Leaving gen
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: asd

#基于生成器的上下文管理器，抛出未处理异常
#coding:utf-8
'''
    filename:mirror_gen.py
    <fluent python,p376>
    with,contextmanager
'''

from contextlib import contextmanager

@contextmanager
def looking_glass():
    print('Enter gen')
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ""
    try:
        yield 'ContextManager_gen'
    except ZeroDivisionError:
        msg = "Do Not divide by zero"
    except :
        raise 
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
        print('Leaving gen')
```







-----------------------------------------------------------------------------------
# [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap9.md
[pre_chap]: ../2021-01-21-chap9.md
[next_chap]: chap9_2_specific_files.md
