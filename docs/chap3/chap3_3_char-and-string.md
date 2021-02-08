## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------
## 3.3 字符和字符串

1. 键盘上的每个`键`对应一个`字符` `char` 
2. `字符`不仅包含字母，通常包括 `字母`，`数字`，`标点符号`，`控制字符`

### 3.3.1 字符编码

1. 计算机只能认识2进制数字，所有提交的东西都要`转化为2进制`
2. `字符` 与2进制的`位bit`之间建立的`对应关系`称为`字符编码`
3. 使用内置函数 `ord()` ordinal 获得`ASCII字符编码`的`10进制表示`
```python
>>> ord('A')
65
```
4. 乱码产生的原因:
	* 同一个2进制数字在不同编码方案中对应不同的字符
	* 各种语言都要让计算机识别，从而产生了各种编码
	* 每种语言可能有多种编码，如中文编码就有:`GB2312`,`BIG5`,`HKSCS`,`GBK`等
5. 解决方案 `统一的编码方案` `Unicode`
	* Unicode 的 `目的` 是实现`编码方案`的 `世界大同`
	* 翻译 `万国码`, `国际码`, `统一码`, `单一码`
	* Unicode 只是一个`字符集`，`没有制定编码规则`，需要`制定实现方式`
	* 具体实现有 `UTF-8`, `UTF-16`, `UTF-32`等
	* 目前使用最广泛的是 `UTF-8` (8-bit Unicode Transformation Format)
6. 查看vim 文件编码 `:set encoding fileencoding fileencodings termencoding`
7. 查看计算机的编码方式
```python
>>> import sys
>>> sys.getdefaultencoding()
'utf-8'
```
8. 使用内置函数 `chr()` 获得相应`数字`对应的`ASCII编码字符`
```python
>>> help(chr)
Help on built-in function chr in module builtins:
chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
>>> chr(65)
'A'
>>> chr(0b110111)
'7'
>>> chr(0x3f)
'?'
```

### 3.3.2 认识字符串

1. 字符串由`多个`被`单引号` `'`或`双引号` `"` 包裹的 `字符`组成 `a = "python"` 

a|=|"|python|"
----|----|------|----|----
变量|变量引用对象|字符串标志|字符串内容|字符串标志


2. `字符串`是`python内置对象`，用`type()查看，返回值为 `str`是`字符串的类型名称`

```python
>>> a= 'python'
>>> type(a)
<class 'str'>
```
3. `单引号`和`双引号`键盘输入时必须为`英文状态`，并且`成对出现`

```python
>>> "i love python'
  File "<stdin>", line 1
    "i love python'
                   ^
SyntaxError: EOL while scanning string literal
```
4. 引号中可以放 `字母`, `汉字`, `数字`等

```python
>>> type(22)
<class 'int'>
>>> type('22')
<class 'str'>
```
5. 注意，`表面看` ~~由数字组成的字符串可以通过`int()`和`str()`实现类型转化~~，实质上，***`int('250')`是以`字符串` `"250"`为参数创建的整数类型实例***,详见[第6章](../chap6)

```python
>>> int('250')
250
>>> str(250)
'250'
>>> int('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'a'
>>> int('a',base=36)
10
```
6. `嵌套错误` 与 `内置函数print()`

```python
>>> print('what's your  name')
  File "<stdin>", line 1
    print('what's your  name')
                ^
SyntaxError: invalid syntax
```
	* 注意`错误提示`
	* `print()`作用是`把参数中的内容打印出来`
	```python
	>>> help(print)
	Help on built-in function print in module builtins:
	print(...)
	    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
	    Prints the values to a stream, or to sys.stdout by default.
	    Optional keyword arguments:
	    file:  a file-like object (stream); defaults to the current sys.stdout.
	    sep:   string inserted between values, default a space.
	    end:   string appended after the last value, default a newline.
	    flush: whether to forcibly flush the stream.
	```
7. 解决方法
	* `单引号` 和 `双引号` `嵌套`
	```python
	>>> print("what's your  name?")
	what's your  name?
	```
	* `转义符`
	```python
	>>> print('what\'s your  name?')
	what's your  name?
	```

python常用转义字符及其说明

转义字符|描述|转义字符|描述
--------|----|--------|----
`\`	|行尾，续行符	|`\n`	|换行
`\\`	|反斜杠		|`\v`	|纵向制表符
`\'`	|单引号		|`\t`	|横向制表符
`\"`	|双引号		|`\r`	|回车
`\a`	|响铃		|`\f`	|换页
`\b`	|退格		|`\0yy`	|8进制数，yy代表字符，如`\012`表换行
`\e`	|转义		|`\xyy`	|16进制数。yy表字符，如`\x0a`表换行
`\000`	|空		|`\other`|其他字符以普通格式输出


```python
>>> print('sadf\x0a123\012abc')
sadf
123
abc
```
8. `原始字符串`与`长字符串`
	* 使用 `\` 实现转义是方便的做法
	* 字符串中出现 `\` 符号的解决办法
		1. 继续使用`转义符号` `\\`
		2. 使用`原始字符串` `[rR]"str"` ,该方法在web开发中设置网站目录结构时非常有用
		```python
		>>> print('c:\new')
		c:
		ew
		>>> print('c:\\new')
		c:\new
		>>> print(r'c:\new')
		c:\new
		```
	* 长字符串
	```python
	>>> print('abc\n123\ndef\n456')
	abc
	123
	def
	456
	>>> a= '''
	... 123
	... asd
	... 345
	... fgh
	... 4567'''
	>>> a
	'\n123\nasd\n345\nfgh\n4567'
	>>> a= '''123
	... asd
	... 456
	... gfh'''
	>>> a
	'123\nasd\n456\ngfh'
	>>> a='''asd
	... asd
	... 123
	... '''
	>>> a
	'asd\nasd\n123\n'
	>>> a='''123
	...     qwe
	...             a w
	... '''
	>>> a
	'123\n\tqwe\n\t\ta w\n'
	```

### 3.3.3 字符串基本操作

* 使用 `is` 判断两个对象是否为同一个

```python
>>> a='hello world'
>>> b='ehllo world'
>>> a is b
False
```
* 像`字符串`这样，其`元素`必须`按照特定顺序排列`的`对象`被称为`序列`

#### 序列存在一系列共性操作
1. `"+"`, 连接
	* 对于字符串，`"+"`  的作用效果是将字符串连接起来，得到一个新的字符串
	```python
	>>> m = 'python'
	>>> n = 'book'
	>>> r = m + ' ' + n
	>>> r
	'python book'
	>>> id(m);id(n);id(r)
	139996405607856
	139996403818096
	139996403817712
	>>> id(m),id(n),id(r)
	(139996405607856, 139996403818096, 139996403817712)
	```
	* 注意, `"+"` 连接的的对象`必须为同种类型`，否则报错
	```python
	>>> m+5
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: can only concatenate str (not "int") to str
	```
	* 可以使用`类型转换`的方式，将 `"+"` `两侧的对象`转化为`同种序列类型的对象`
	```python
	>>> m + str(5)
	'python5'
	```

2. `"*"`,重复元素
	+ 对于字符串(序列)，`"*"`表示要获得重复的元素
	```python
	>>> m * 3
	'pythonpythonpython'
	>>> '-'*10
	'----------'
	```

3. `len()函数`,求序列长度
	- 使用`内置函数 len()` 得到`序列的元素个数`(`字符串长度`)

	```python
	>>> help(len)
	Help on built-in function len in module builtins:

	len(obj, /)
	    Return the number of items in a container.
	(END)
	>>> len(r)
	11
	>>> type(len(r))
	<class 'int'>
	>>> len('派森')
	2
	```

4. `in`:判断元素是否在`容器`中
	- `字符串是容器`，`"in"`用于判断 `容器`中是否`存在某个元素`
	- 判断`字符`是否`在字符串内`
	- 判断`字符串`是否`在字符串内`
	- `返回类型`为`bool`

	```python
	>>> r
	'python book'
	>>> 'p' in r
	True
	>>> 'r' in r
	False
	>>> 'on' in r
	True
	>>> 'book' in r
	True
	>>> type(True)
	<class 'bool'>
	>>> type(False)
	<class 'bool'>
	```

### 3.3.4 索引和切片

1. 索引
	+ `字符串`是`序列`
	+ `字符串`中的每个`字符`都是`按照特定顺序排列`的，`不能随意更换位置`，因此可以`给每个字符进行编号`
	+ 可以把`序列`理解为`有序排列`，这些`编号`称为`索引`
	+ 对`字符串`中的`字符`(`序列`的`元素`）__进行`编号`（`索引`）__ 的 ***`方法有2种`***
		- __从左边开始编号__ ***递增***，依次为 0，1，2，3，。。。
		- __从右边开始编号__ ***递减***，依次为 -1，-2，-3，。。。
	+ 因为可以从`两个方向`开始编号，所以`每个字符有2个索引`

	+ 使用符号`[]`可以通过索引找到每个字符
	```python
	>>> r
	'python book'
	>>> r[0]
	'p'
	>>> r[-1]
	'k'
	>>> r[-11]
	'p'
	```
	+ 使用的`索引` __超出__该字符串的`索引范围`会报错
	+ `获得`字符串的`最后一个字符的索引`
		1. 使用内置函数 `len()` 得到`字符串的长度`
			```python
			>>> len(r)
			11
			```

		2. 使用`字符串对象`的 `str.index()`  方法
			```python
			>>> r.index('k') 
			10
			>>> help(r.index)

			index(...) method of builtins.str instance
			    S.index(sub[, start[, end]]) -> int
			    
			    Return the lowest index in S where substring sub is found,
			    such that sub is contained within S[start:end].  Optional
			    arguments start and end are interpreted as in slice notation.
			    
			    Raises ValueError when the substring is not found.
			(END)
			```

|索引方向|索引值|索引值	|索引值	|索引值	|索引值	|索引值	|索引值	|索引值	|索引值	|索引值	|索引值	|
|--------|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|从左开始|0	|1	|2	|3	|4	|5	|6	|7	|8	|9	|10	|
|字符串	 |p	|y	|t	|h	|o	|n	| 	|b	|o	|o	|k	|
|从右开始|-11	|-10	|-9	|-8	|-7	|-6	|-5	|-4	|-3	|-2	|-1	|			



2. 切片
	- 通过`索引`不仅可以`得到指定字符`，还能`得到若干字符`
	```python
	>>> r
	'python book'
	>>> r[1:8]
	'ython b'
	>>> 'python book'[1:8]
	'ython b'
	```
	- 通过 `r[1:8]` 方式从字符串`得到多个字符`，称为__切片(Slice)__
	- `切片` __没有破坏__`原字符串`
	```python
	>>> r
	'python book'
	```
	- `切片操作`的***普遍表达式***  ***Str[index<sub>start</sub>:index<sub>stop</sub>:step]***
		1. ***index<sub>start</sub>*** 表示 __开始的索引__ ，如果从`该方向`的`第一个字符开始`，`可以省略`
		2. ***index<sub>stop</sub>*** 表示 __结束的索引__ ***切片区间中不包含此索引对应的字符***如果`到该方向最后一个`，`包含最后一个`，`可以省略`
		3. ***step*** 表示**步长**，默认为1，可为 __正整数，表示从左向右__ ；或 __负整数，从右向左__ 。
		4. ***切片，顾头不顾尾***
			+ 省略index<sub>start</sub>索引，以字符串开始为切片开始
			```python
			>>> r[:8]
			'python b'
			>>> r[:-3]
			'python b'
			```
			+ 省略index<sub>stop</sub>，则表示切片范围到字符串结束，包含最后一个字符
			```python
			>>> r[1:]
			'ython book'
			```
			+ `r[1:]` 和  `r[1::1]` 的操作结果一样，但当步长不为1时，则按照步长切片
			```python
			>>> r[1::1]
			'ython book'
			>>> r[1::2]
			'yhnbo'
			>>> r[::2]
			'pto ok'
			```
			+ 步长为负数
			```python
			>>> r[::-1]
			'koob nohtyp'
			>>> r[10:0:-1]
			'koob nohty'
			>>> r[10:0:-2]
			'ko ot'
			>>> r[10::-2]
			'ko otp'
			```
		5. `切片`时，`索引`不区分从左边开始计数，还是从右边开始计数
		```python
		>>> r[1:8:2],r[1:-3:2],r[-10:8:2],r[-10:-3:2]
		('yhnb', 'yhnb', 'yhnb', 'yhnb')
		>>> r[8:1:-2],r[-3:1:-2],r[8:-10:-2],r[-3:-10:-2]
		('o ot', 'o ot', 'o ot', 'o ot')
		```
	- `切片的基本方法`适用于`所有序列类型的对象`


### 3.3.5 键盘输入

1. python提供内置函数`input()`用于`接收用户通过键盘输入`的`信息`

	```python
	>>> help(input)
	Help on built-in function input in module builtins:

	input(prompt=None, /)
	    Read a string from standard input.  The trailing newline is stripped.
	    
	    The prompt string, if given, is printed to standard output without a
	    trailing newline before reading input.
	    
	    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
	    On *nix systems, readline is used if available.
	(END)
	```
2. `input()`函数的`返回值`是一个`字符串类型`的对象

	```python
	>>> name = input('input your name:')
	input your name:python
	>>> name
	'python'
	>>> type(name)
	<class 'str'>
	```
3. __不论通过键盘输入什么字符，`input()`函数的返回值都是字符串__

	```python
	>>> age = input('how old are you? ')
	how old are you? 10
	>>> age
	'10'
	>>> type(age)
	<class 'str'>
	```
4. 编写一段程序，实现下列功能
	* 询问姓名和年龄
	* 计算10年后的年龄
	* 打印输入多的姓名和当前年龄，10年后的年龄
		```python
		#coding:utf-8
		'''
		your name and age.
			name.py
		'''

		name = input('your name: ')
		age = input('your age: ')

		after = int(age) + 10   #变量age引用字符串类型的对象，类型转换后才能参与运算

		print('your name is: ',name)
		#print('after ten years, you are ',after)

		print('you are ' + age + ' years old.')

		print('you will be ' +  str(after) + ' years old after ten years.') #整数 after 通过+ 号与字符串连接时，要转化为字符串类型.
		```

### 3.3.6 字符串的方法
#### 通过本节掌握查看文档的方法
- `字符串`是**对象类型**，__也是对象__
- 通过 `dir(str)` 查看`字符串对象`的所有__属性__和__方法__，可以粗略的__划分为2类__
	1.  一类是，以`双下划线` `__` 开始和结尾的，称为__特殊方法__和__特殊属性__
	2. 另一类是_看起来很普通的名称_，__笼统称为方法和属性__
	```python
	>>> dir(str)
	['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
	>>> 
	```


1. `"is"` 开头的方法
	+  仔细观察 `dir(str)`  的结果，其中有若干以 `is`  作为名称开始的方法
	+ 这些方法都返回了 __`bool`__ 类型， 只有 `True` 和 `False`  两个值
	```python
	>>> '34689'.isdigit()
	True
	>>> '34689asd'.isdigit()
	False
	>>> 'asd'.isdigit()
	False
	>>> '3.14'.isdigit()
	False
	```
	+ `Str.isdigit()`方法是用来判断当前字符串是否完全有数字字符[0-9]组成
	```python
	>>> help(str.isdigit)
	isdigit(self, /)
	    Return True if the string is a digit string, False otherwise.
	    
	    A string is a digit string if all characters in the string are digits and there
	    is at least one character in the string.
	```

2. 分隔`split`和组合`join`
	- 字符串对象提供了根据某个符号分割字符串内容的方法 `split()`

	```python
	>>> help(str.split)

	Help on method_descriptor:

	split(self, /, sep=None, maxsplit=-1)
	    Return a list of the words in the string, using sep as the delimiter string.
	    
	    sep
	      The delimiter according which to split the string.
	      None (the default value) means split according to any whitespace,
	      and discard empty strings from the result.
	    maxsplit
	      Maximum number of splits to do.
	      -1 (the default value) means no limit.
	```

	- __特别注意__ 如果没有指定特定的分隔符， python会默认空格 ` ` 为分隔符

	```python
	>>> a = 'l love python'
	>>> a.split()
	['l', 'love', 'python']
	>>> a.split(' ')
	['l', 'love', 'python']
	>>> a.split('')
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: empty separator
	```

	+ 字符串的 `join()` 方法类似 `split()` 方法的逆过程，可以用某个字符把另一种对象组合为一个字符串
	```python
	>>> help(str.join)
	Help on method_descriptor:
	join(self, iterable, /)
	    Concatenate any number of strings.
	    The string whose method is called is inserted in between each given string.
	    The result is returned as a new string.
	    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
	```

	+ 该方法的参数中 `"iterable"`  含义为 `可迭代的` ,`列表对象`和`字符串对象`都是`可迭代的`

	```python
	>>> a
	'l love python'
	>>> lst=a.split()
	>>> lst
	['l', 'love', 'python']
	>>> '.'.join(lst)
	'l.love.python'
	>>> ''.join(lst)
	'llovepython'
	>>> '-'.join(lst)
	'l-love-python'
	>>> '@@-'.join(lst)
	'l@@-love@@-python'
	>>> '-'.join('python')
	'p-y-t-h-o-n'
	```


3. 使用`str.strip()` ，`str,lstrip()` 和`str.rstrip()` 方法`移除`  __字符串开头和结尾__ 的 ___特定字符___ (默认空格)
	```python
	>>> help(str.strip)
	Help on method_descriptor:
	strip(self, chars=None, /)
	    Return a copy of the string with leading and trailing whitespace removed.
	    If chars is given and not None, remove characters in chars instead.
	(END)
	>>> help(str.lstrip)
	Help on method_descriptor:
	lstrip(self, chars=None, /)
	    Return a copy of the string with leading whitespace removed.
	    If chars is given and not None, remove characters in chars instead.
	(END)
	>>> help(str.rstrip)
	Help on method_descriptor:
	rstrip(self, chars=None, /)
	    Return a copy of the string with trailing whitespace removed.
	    
	    If chars is given and not None, remove characters in chars instead.
	(END)
	>>> s='    hello  '
	>>> s.strip()
	'hello'
	>>> s.lstrip()
	'hello  '
	>>> s.rstrip()
	'    hello'
	```

### 3.3.7 字符串格式化输出

1. 使用字符串的 `format` 方法，实现 **格式化输出**

```python
>>> help(str.format)
Help on method_descriptor:
format(...)
    S.format(*args, **kwargs) -> str
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').
(END)
>>> 'i like {0} and {1}.'.format('python','physics')
'i like python and physics.'
```

2. 占位符`{}`
	* 字符串 `'i like {0} and {1}.'` ，其中`{0}` 和`{1}` 占据了2个位置，它们就是占位符
	* `占位符`中的 __数字__ 就是 `format` 方法的`参数列表`的 __顺序号__ 
	* `format('python','physics')`是字符串格式化输出的方法，传入的两个字符串`python`和`physics` 分别对应占位符`{0}` 和`{1}` 
	* 进一步理解占位符中数字的含义
	```python
	>>> 'i like {1} and {0}, {0} is a programming language.'.format('python','physics')
	'i like physics and python, python is a programming language.'
	```

3. `格式化输出`的`指定格式`
	1. 占位符序号与格式化字符使用 `:` 分割
	2. `<`,`>` 和 `^` 分别表示 __左对齐__ ， __右对齐__ ，和 __居中__ 
	3. ___字符串作为参数___ ， __默认左对齐__
		+ 占位符处的`最少字符数`，不足用空格填充
		+ 指定`对齐方式`
		+ 指定`填充的单个字符`
		```python
		>>> 'i like {0:10} and {1:>15}'.format('python','physics')
		'i like python     and         physics'
		>>> 'i like {0:^10} and {1:<15}'.format('python','physics')
		'i like   python   and physics 
		>>> 'i like {0:音乐^10} and {1:<15}'.format('python','physics')
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		ValueError: Invalid format specifier
		>>> 'i like {0:乐^10} and {1:<15}'.format('python','physics')
		'i like 乐乐python乐乐 and physics       '
		```
		+ `{0:10}`表示引用`第0个位置的参数`，该位置`至少有10个字符`，默认`左对齐`，`不足10个默认使用空格填充`
		+ ___限制显示的字符个数___
		```python
		>>> 'i like {0:->.3} and {1:->15.3}'.format('python','physics')
		'i like pyt and ------------phy'
		```
		+ `.3` 前面`没有数字`表示该位置`长度自适应`即将放到此处的 字符串长度
		+  `.3` 表示截取传入字符串的前3个字符
	4. ___数字作为参数___ ， __默认右对齐__
		- `<`,`>` 和 `^` 分别表示左对齐，右对齐，和居中
		- `d`表示该位置的参数应为`整数int` ,`f`表示参数应为`浮点数float` ,且浮点数 的`小数位数` `默认的6位`
		- `{0:4d}` 设置此位置`长度为4个字符`，放置`整数`
		- `{0:04d}` 表示`空位用0填充`
		- `{1:.1f}` 表示 __采用四舍五入__ 的方式对`浮点数`进行`截取` `1位小数`
		- `{1:06.1f}` 表示该位置长度为6个字符，__用0填充__ ，取1位小数
		```python
		>>> 'she is {0:d} years old and {1:f} m in height.'.format(28,1.68)
		'she is 28 years old and 1.680000 m in height.'
		>>> 'she is {0:4d} years old and {1:.1f} m in height.'.format(28,1.68)
		'she is   28 years old and 1.7 m in height.'
		>>> 'she is {0:04d} years old and {1:06.1f} m in height.'.format(28,1.68)
		'she is 0028 years old and 0001.7 m in height.'
		>>> 'she is {0:04d} years old and {1:^06.1f} m in height.'.format(28,1.68)
		'she is 0028 years old and 01.700 m in height.'
		```

4. 字符串的`format` 方法进行格式化输出，实现的其他方式

```python
>>> str.format('i like {0} and {1}.','python','physics')
'i like python and physics.'
>>> 'i like {subject} and {lang}'.format(lang='python',subject='physics')
'i like physics and python'
```

5. 字符串有 `format` 方法，内置函数中也有 `format`  方法

```python
>>> h = 'hello world'
>>> format(h,'>20')
'         hello world'
>>> format(h,'<20')
'hello world         '
>>> format(h,'^20')
'    hello world     '
>>> format(h,'20')
'hello world         '
>>> format(h,'-^20')
'----hello world-----'
>>> format(h,'$^20')
'$$$$hello world$$$$$'
```

6. format 语法详细

```python
>>> help(format)
format(value, format_spec='', /)
    Return value.__format__(format_spec)
    
    format_spec defaults to the empty string.
    See the Format Specification Mini-Language section of help('FORMATTING') for
    details.
(END)
>>> help('FORMATTING')
```

-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap3.md
[pre_chap]: chap3_2_number.md
[next_chap]: chap3_4_list-and-tuple.md
