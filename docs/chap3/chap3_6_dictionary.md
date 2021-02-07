## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------
## 3.6 字典 `dictionary`
* 字典`dictionary` 是专门为 **创建映射关系** 而提供的内置对象
* 字典的属性和方法
```python
>>> dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```
### 3.6.1 创建字典

#### 1. 使用`dict()`函数创建字典
+ `dict` 是字典类型名称，跟其他类型一样，也有相应的函数形式
```python
Help on class dict in module builtins:
class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
```
+ 创建字典格式 `dict()`;`dict(**kwargs)` ;`a = dict(str1=value1, str2=value2, str3=value3)` str 表示字符串类型的键，value 表示键对应的值。使用此方式创建字典时，字符串不能带引号
```python
>>> d = dict()
>>> type(d) ; d
<class 'dict'>
{}
>>> dict(a=1,b=2)
{'a': 1, 'b': 2}
```
+ 创建字典格式 `dict(mapping)`
```python
>>> keys = ['a','b','c']
>>> values = [1,2,3]
>>> zip(keys,values)
<zip object at 0x7fbddfb6d300>
>>> dict(zip(keys,values))
{'a': 1, 'b': 2, 'c': 3}
```
	- `map` 函数会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
	```python
	>>> help(map)
	Help on class map in module builtins:
	class map(object)
	 |  map(func, *iterables) --> map object
	 |  
	 |  Make an iterator that computes the function using arguments from
	 |  each of the iterables.  Stops when the shortest iterable is exhausted.
	>>> map(lambda x,y:(x * 2,y * 3),keys,values)
	<map object at 0x7fbddfb8ca00>
	>>> list(map(lambda x,y:(x * 2,y * 3),keys,values))
	[('aa', 3), ('bb', 6), ('cc', 9)]
	>>> dict(map(lambda x,y:(x * 2,y * 3),keys,values))
	{'aa': 3, 'bb': 6, 'cc': 9}
	>>> tuple(map(lambda x,y:(x * 2,y * 3),keys,values))
	(('aa', 3), ('bb', 6), ('cc', 9))
	```
+ 创建字典格式 `dict(iterable)` 
```python
>>> demo = (('a',11),('bb',22),['c',33])
>>> d = dict(demo) ; d ; type(d)
{'a': 11, 'bb': 22, 'c': 33}
<class 'dict'>
```


#### 2. 使用 `{}`创建字典 `dictname = {'key':'value1', 'key2':'value2', ..., 'keyn':valuen}`

```python
>>> d = {} ; d ; type(d)
{}
<class 'dict'>
>>> person = {'name':'qiwsir','language':'python'} ; person ; type(person)
{'name': 'qiwsir', 'language': 'python'}
<class 'dict'>
```
#### 3. 通过`fromkeys()`方法创建字典
+ 这种创建方式通常用于初始化字典，设置 value 的默认值
```python
>>> help(dict.fromkeys)
Help on built-in function fromkeys:
fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.
(END)
>>> knowledge = ['math','english','physics']
>>> scores = dict.fromkeys(knowledge,60) ; scores ; type(scores)
{'math': 60, 'english': 60, 'physics': 60}
<class 'dict'>
>>> dict.fromkeys('python',None)
{'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}
```

#### 4. 字典的组成部分

{	|'name'	|:		     |'qiwsir'|,		|'language'|:		     |'python'|}
--------|-------|--------------------|--------|-----------------|----------|-----------------|--------|----
字典标志|键`key`|`键`与`值`的`分隔符`|值`value`|`键值对`的分隔符	|键`key`|`键`与`值`的`分隔符`|值`value|字典标志


#### 5. 字典的 *键`key`* 与 *值`value`* 的要求

+ **键** `key` 的要求
	- 唯一的，不能重复
	- 必须是不可变对象
+ **值** `value` 的要求
	- 值对应于键，值可以重复，也可以是任何类型的对象

* 字典的键不能使用 **列表，字典类型的对象** ，因为它们是 `unhashable`类型；`unhashable`的内容详见3.7.1节
```python
>>> s1 = 'python' ; s2 = 'language' ; num1 = 2 ; lst1 = ['java',1] ; t1 = (1,2) ;d1 = {1:2}>>> s1 ;s2 ; num1 ; lst1 ;t1 ; d1
'python'
'language'
2
['java', 1]
(1, 2)
{1: 2}
>>> {s1:s2,num1:lst1}
{'python': 'language', 2: ['java', 1]}
>>> {lst1:s1}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> {t1:s1}
{(1, 2): 'python'}
>>> {d1:s1}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
```


#### 6. 字典不是序列
+ 字典表达的是一种 **映射关系** 
+ 字典没有列表和字符串中的`index()`方法，说明字典不是序列
+ 理解: 
	- 序列的特点是元素有序排列，索引与元素对应
	- 字典中已经实现了键与值的对应关系，所以不需要给每个键值对建立索引了

```python
>>> hasattr(list,'index')
True
>>> hasattr(dict,'index')
False
```


### 3.6.2 字典的基本操作

```python
>>> cities = ['soochow','shanghai','hangzhou']
>>> phone = ('0512','021','0571')
>>> cities_phone = dict(zip(cities,phone))
>>> cities_phone
{'soochow': '0512', 'shanghai': '021', 'hangzhou': '0571'}
```

#### 1. `len(d)` 返回字典d中 键值对的数量
```python
>>> len(cities_phone)
3
```

#### 2. `d[key]` 返回字典d中 键 key 的值
```python
>> cities_phone[soochow]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'soochow' is not defined
>>> cities_phone['soochow']
'0512'
```
#### 3. `d[key]=value` 将值 value 赋值给字典d中 的键 key
+ 给字典增加键值对可以使用下述方式
+ 该操作没有生成新的字典，原地修改
```python
>>> cities_phone ; id(cities_phone)
{'soochow': '0512', 'shanghai': '021', 'hangzhou': '0571'}
140453479351296
>>> cities_phone['beijing']='010' ; cities_phone ; id(cities_phone)
{'soochow': '0512', 'shanghai': '021', 'hangzhou': '0571', 'beijing': '010'}
140453479351296
```


#### 4. `del d[key]` 删除字典d 的键key项(将该键值对删除) `python 关键字 del`
+ 该操作没有生成新的字典，原地修改
```python
>>> cities_phone ; id(cities_phone)
{'soochow': '0512', 'shanghai': '021', 'hangzhou': '0571', 'beijing': '010'}
140453479351296
>>> del cities_phone['shanghai'] ; cities_phone ; id(cities_phone)
{'soochow': '0512', 'hangzhou': '0571', 'beijing': '010'}
140453479351296
```
+ 查看 **关键字** `keyword` 的帮助文档的方法
```python
>>> help()
Welcome to Python 3.9's help utility!
If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.
Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".
To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".
help> del
The "del" statement
   del_stmt ::= "del" target_list
Deletion is recursively defined very similar to the way assignment is
defined. Rather than spelling it out in full details, here are some
hints.
.....
```

#### 5. `key in d` 检查字典d中 是否含有键为key的项
```python
>>> 'hangzhou' in cities_phone
True
>>> 'shanghai' in cities_phone
False
>>> cities_phone
{'soochow': '0512', 'hangzhou': '0571', 'beijing': '010'}
```

### 3.6.3 字典的方法

#### 1. 读取 **值** 的方法

+ 通过 `d[k]` 的方式得到 **键** 对应的 **值**
	- 前提是 `d[k]` 中的 `k` 必须是字典d 中已有的键，否则报错
	```python
	>>> d
	{'a': 1, 'lang': 'python'}
	>>> d['lang']
	'python'
	>>> d['pub']
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'pub'
	```
+ 解决`d[k]`方式可能的报错方法有: `D.get(k[,d])` `D.setdefault(k[,d])`

```python
>>> help(d.get)
Help on built-in function get:
get(key, default=None, /) method of builtins.dict instance
    Return the value for key if key is in the dictionary, else default.
(END)
>>> help(d.setdefault)
Help on built-in function setdefault:
setdefault(key, default=None, /) method of builtins.dict instance
    Insert key with a value of default if key is not in the dictionary.
    Return the value for key if key is in the dictionary, else default.
(END)
```
+ 使用`D.get(k[,d])` 方法
	- 当 `k in D` 时，结果与 `d[k]`相同；当`k not in D`时，返回`d` 的值
	```python
	>>> d
	{'a': 1, 'lang': 'python'}
	>>> d.get('lang')
	'python'
	>>> d.get('lang','php')
	'python'
	>>> d.get('pub')
	>>> d.get('pub','php')
	'php'
	>>> d
	{'a': 1, 'lang': 'python'}
	```
+ 使用 `D.setdefault(k[,d])` 方法
	- 当 `k in D` 时，结果与 `d[k]`相同
	```python
	>>> d
	{'a': 1, 'lang': 'python'}
	>>> d.setdefault('lang') ;d
	'python'
	{'a': 1, 'lang': 'python'}
	>>> d.setdefault('lang','php') ;d
	'python'
	{'a': 1, 'lang': 'python'
	```
	- 当`k not in D`时，将键值对 `k:d` 添加到字典中; 并返回 `d` 的值
	```python
	>>> d
	{'a': 1, 'lang': 'python'}
	>>> d.setdefault('pub') ; d
	{'a': 1, 'lang': 'python', 'pub': None}
	>>> d.setdefault('author','laoqi') ; d
	'laoqi'
	{'a': 1, 'lang': 'python', 'pub': None, 'author': 'laoqi'}
	```



#### 2. 视图对象
+ **视图对象 `view object`** 是 `python 3`所特有的， `python 2`版本不具有视图对象
+ 字典获得视图对象的方法有 `D.items()`,`D.keys()`,`D.values()`
```python
>>> help(d.items)
Help on built-in function items:
items(...) method of builtins.dict instance
    D.items() -> a set-like object providing a view on D's items
(END)
>>> help(d.keys)
Help on built-in function keys:
keys(...) method of builtins.dict instance
    D.keys() -> a set-like object providing a view on D's keys
(END)
>>> help(d.values)
Help on built-in function values:
values(...) method of builtins.dict instance
    D.values() -> an object providing a view on D's values
(END)
>>> d
{'a': 1, 'lang': 'python', 'pub': None, 'author': 'laoqi'}
>>> di = d.items() ; type(di) ; di ;id(di)
<class 'dict_items'>
dict_items([('a', 1), ('lang', 'python'), ('pub', None), ('author', 'laoqi')])
140453479345936
>>> dk = d.keys() ; type(dk) ; dk ;id(dk)
<class 'dict_keys'>
dict_keys(['a', 'lang', 'pub', 'author'])
140453479343056
>>> dv = d.values() ; type(dv) ; dv ;id(dv)
<class 'dict_values'>
dict_values([1, 'python', None, 'laoqi'])
140453479344112
```


+ 视图对象绑定于相应的字典，视图对象随字典的变化而动态变化

```python
>>> del d['a']
>>> d
{'lang': 'python', 'pub': None, 'author': 'laoqi'}
>>> di ;id(di)
dict_items([('lang', 'python'), ('pub', None), ('author', 'laoqi')])
140453479345936
>>> dk ; id(dk)
dict_keys(['lang', 'pub', 'author'])
140453479343056
>>> dv ; id(dv)
dict_values(['python', None, 'laoqi'])
140453479344112
```
+ 视图对象可以转化为其他类型的对象，转化后不能动态反应字典的变化

```python
>>> d
{'lang': 'python', 'pub': None, 'author': 'laoqi'}
>>> i_lst = list(di) ; i_lst
[('lang', 'python'), ('pub', None), ('author', 'laoqi')]
>>> k_lst = list(dk) ; k_lst
['lang', 'pub', 'author']
>>> v_lst = list(dv) ; v_lst
['python', None, 'laoqi']
>>> del d['author']
>>> di ; i_lst ; dk ; k_lst ; dv ; v_lst
dict_items([('lang', 'python'), ('pub', None)])
[('lang', 'python'), ('pub', None), ('author', 'laoqi')]
dict_keys(['lang', 'pub'])
['lang', 'pub', 'author']
dict_values(['python', None])
['python', None, 'laoqi']
```

#### 3. 增加键值对
+ 向字典增加键值对的方法有 `d[k] = v` ,  `d1 |= d2` 和 `D.update()`
+ `d[k]= v ` 方式 **一次增加一个键值对**

```python
>>> d
{'lang': 'python', 'pub': None}
>>> d['size'] = 67
>>> d
{'lang': 'python', 'pub': None, 'size': 67}
```
+ `d1 |= d2`使用字典 d2 更新d1 ;`d1 | d2` 方式合并2个字典
```python
>>> d
{'ab': 'c1', '22': 44}
>>> d1 | d
{'lang': 'python', 'ab': 'c1', '22': 44}
>>> d1 ; d
{'lang': 'python'}
{'ab': 'c1', '22': 44}
>>> d1 |= d ; d1 ;d
{'lang': 'python', 'ab': 'c1', '22': 44}
{'ab': 'c1', '22': 44}
```


+ `D.update()` 方式 **一次增加多个键值对**
	- [`*arg` 与 `**kwargs` 参数的用法](https://www.cnblogs.com/xujiu/p/8352635.html)
	- [`Python之可变参数，*参数，**参数，以及传入*参数，**参数解包`](https://blog.csdn.net/cadi2011/article/details/84871401)

	```python
	>>> help(d.update)
	Help on built-in function update:
	update(...) method of builtins.dict instance
	    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
	    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
	    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
	    In either case, this is followed by: for k in F:  D[k] = F[k]
	(END)
	```

	- `D.update([E, ]**F)`  中，`E` 表示 **字典或者可迭代对象** ;`**F` (即 `**kwargs` 作 __函数定义__ 时,表示 __收集所有未匹配的`关键字参数`组成1个dict对象__ ) 表示 *0个或者多个关键字参数* 即 **可变参数**
	- **关键字参数** `sorted(iterable, /, *, key=None, reverse=False)` 中 `key=None` 和 `reverse=False` 形式的参数 即为关键字参数
	- `**kwargs` 作 __函数调用__ 时 表示 解包dict对象的每个元素，作为一个一个的关键字参数传入到函数中

	- `update()` 格式 `D.update(**F)` E 不存在 ，F 为关键字参数
	```python
	>>> d = {}
	>>> d
	{}
	>>> d.update() ; d
	{}
	>>> d.update(lang='python',pub='PHEI') ; d
	{'lang': 'python', 'pub': 'PHEI'}
	```
	- `update()` 格式 `D.update(E,**F)` E 存在 ，且拥有`.keys()`方法 ;E 为 dict
	```python
	>>> d1 = {'lang':'python'} ; d2 = {'song':'I dreamed a dream'} ; d1 ;d2
	{'lang': 'python'}
	{'song': 'I dreamed a dream'}
	>>> d1.update(d2) ; d1
	{'lang': 'python', 'song': 'I dreamed a dream'
	>>> d1 = {'lang':'python'} ; d2 = {'song':'I dreamed a dream'} ; d1 ;d2
	{'lang': 'python'}
	{'song': 'I dreamed a dream'}
	>>> d1.update(d2,pub='php',auther='laoqi')
	>>> d1
	{'lang': 'python', 'song': 'I dreamed a dream', 'pub': 'php', 'auther': 'laoqi'}
	```
	- `update()` 格式 `D.update(E,**F)` E 存在 ，且不含`.keys()`方法 ; E 为含有映射关系的可迭代对象
	```python
	>>> d
	{'lang': 'python', 'pub': 'PHEI'}
	>>> d.update([['price','3.14'],((22,334),2)]) ;d
	{'lang': 'python', 'pub': 'PHEI', 'price': '3.14', (22, 334): 2}
	>>> d
	{'lang': 'python', 'pub': 'PHEI'}
	>>> d.update([['price','3.14'],((22,334),2)],a=1,b=22) ;d
	{'lang': 'python', 'pub': 'PHEI', 'price': '3.14', (22, 334): 2, 'a': 1, 'b': 22}
	```




#### 4. 删除键值对

+ 删除字典键值对的方法有 `del d[k]` ,`D.pop(k[,d])`,`D.popitem()`和`D.clear()`
	- 这几种方法都是 **原地修改** 
	```python
	>>> help(d.pop)
	Help on built-in function pop:
	pop(...) method of builtins.dict instance
	    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
	    If key is not found, default is returned if given, otherwise KeyError is raised
	(END)
	>>> help(d.popitem)
	Help on built-in function popitem:
	popitem() method of builtins.dict instance
	    Remove and return a (key, value) pair as a 2-tuple.
	    Pairs are returned in LIFO (last-in, first-out) order.
	    Raises KeyError if the dict is empty.
	(END)
	>>> help(d.clear)
	Help on built-in function clear:
	clear(...) method of builtins.dict instance
	    D.clear() -> None.  Remove all items from D.
	(END)
	```

	- `del d[k]` 若`k not in d` 会报错
	```python
	>>> d
	{'ab': 'c1', '22': 44, 'song': 'I dreamed a dream'}
	>>> del d['ab']
	>>> d
	{'22': 44, 'song': 'I dreamed a dream'}
	>>> del d['ab'] ;d
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'ab'
	```
	- `D.pop(k[,d])` 删除指定的键的键值对(参数 k 不可省略);
		* `if k in D` 删除并返回 D[k]
		* `if k not in D` ,参数中提供d时，返回d;否则报错
		```python
		>>> d
		{'lang': 'python', 'pub': 'PHEI', 'author': 'laoqi', 'price': 3.14, 'color': 'white'}
		>>> d.pop('lang') ; d
		'python'
		{'pub': 'PHEI', 'author': 'laoqi', 'price': 3.14, 'color': 'white'}
		>>> d.pop('lang') ; d
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		KeyError: 'lang'
		>>> d.pop('lang','php') ; d
		'php'
		{'pub': 'PHEI', 'author': 'laoqi', 'price': 3.14, 'color': 'white'}
		```
	- `D.popitem()` 从字典中选择1个键值对删除，并返回该(键值对,元组)，直到字典被删空，再删报错
	```python
	>>> d2
	{'song': 'I dreamed a dream'}
	>>> d2.popitem() ; d2
	('song', 'I dreamed a dream')
	{}
	>>> d2.popitem() ; d2
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'popitem(): dictionary is empty'
	```
	- `D.clear()` 清空字典的元素，使字典为空,但字典还存在
	* 注意区分 与`del d` 的区别; `del d` 从内存删除字典d
	```python
	>>> d ; id(d)
	{'pub': 'PHEI', 'author': 'laoqi', 'price': 3.14, 'color': 'white'}
	140453478856128
	>>> d.clear() ; d ;id(d)
	{}
	140453478856128
	>>> del d ; id(d) ; d
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'd' is not defined
	```



### 3.6.4 浅拷贝和深拷贝

* 含有 `copy()` 方法的内置对象有 `list`,`dict`,`set`,`frozenset`
```python
>>> hasattr(list,'copy') ;  hasattr(dict,'copy') ; hasattr(set,'copy') ; hasattr(frozenset,'copy') ;
True
True
True
True
>>> help(list.copy)
copy(self, /)
    Return a shallow copy of the list.
(END)
>>> help(dict.copy)
copy(...)
    D.copy() -> a shallow copy of D
(END)
>>> help(set.copy)
copy(...)
    Return a shallow copy of a set.
(END)
>>> help(frozenset.copy)
copy(...)
    Return a shallow copy of a set.
(END)
```

* 使用`copy` 模块的`copy.copy()`方法也可以对其他类型的对象进行 浅复制

```python
>>> import copy
>>> copy.copy(123)
123
>>> copy.copy('abcd')
'abcd'
>>> copy.copy((123,435,'asd'))
(123, 435, 'asd')
>>> copy.copy(3.14)
3.14
```

#### 1. 赋值 
+ 引用: 对象在内存中所在位置的地址，称为引用 ; 引用实际是内存中的1个数字地址编号
+ 变量: 在python中，变量就是地址的1种表示形式，并不开辟存储空间
+ 通过1个例子说明变量和变量指向的引用就是一个东西
```python
>>> b = 18
>>> id(b) ; id(18) ; b is 18
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
140453484145488
140453484145488
True
```
+ `is` 用于判断2个对象是否为同一个，即id内存地址一致 ;`==` 用于检验2个对象的内容是否一致
```python
>>> b1 = ['name',123,['python','pascal']]
>>> b2 = b1
>>> b2 is b1
True
>>> b2 == b1
True
```

#### 2. 浅拷贝
+ 浅拷贝的对象与原对象不是同一个对象
```python
>>> b3 = b1.copy()
>>> b3 is b1 ; b3 == b1 ; id(b1) ;id(b2) ;id(b3)
False
True
140453478872448
140453478872448
140453478835584
```
+ 浅拷贝的对象与原对象 中的每个元素仍然是同一个对象

```python
>>> [id(e) for e in b1] ; [id(e) for e in b3] #列表解析
[140453484347696, 140453484337328, 140453478873088]
[140453484347696, 140453484337328, 140453478873088]
```
+ 可见，`'浅拷贝'` 就是新建1个容器对象，但容器中的子对象还是引用原容器中的，实质上只复制了1层
+ [python 中的可变（不可变）对象以及可哈希（不可哈希）的定义](https://blog.csdn.net/wx6gml18/article/details/108164004)
+ 修改b3 中的不可变对象元素，即让该位置引用1个新的对象，b1的该位置不受影响

```python
>>> b1 ; b3
['name', 123, ['python', 'pascal']]
['name', 123, ['python', 'pascal']]
>>> b3[1] = 3.14
>>> b1 ; b3
['name', 123, ['python', 'pascal']]
['name', 3.14, ['python', 'pascal']]
```
+ **修改b3中的可变对象** ，该元素进行原地修改，**b1的该位置随b3而变化**

```python
>>> b3[2].append(999)
>>> b1 ; b3
['name', 123, ['python', 'pascal', 999]]
['name', 3.14, ['python', 'pascal', 999]]
```

+ **替换b3 中的可变对象元素** ，即让该位置引用1个新的对象， **b1的该位置不受影响**

```python
>>> b3[2] = 11
>>> b1 ; b3
['name', 123, ['python', 'pascal', 999]]
['name', 3.14, 11]
```

#### 3. 深拷贝

+ `copy.deepcopy()` 进行 深拷贝

```python
>>> import copy
>>> b4 = copy.deepcopy(b1)
>>> id(b1) ; id(b4)
140453478872448
140453478912576
```

+ 深拷贝不但新建1个容器对象，而且容器中的 **容器元素也新建了** ，可以将深拷贝理解为复制过程的递归，即 **容器中的容器也复制** 

```python
>>> [id(e) for e in b1] ; [id(e) for e in b4]
[140453484347696, 140453484337328, 140453478873088]
[140453484347696, 140453484337328, 140453478843008]
>>> 
```

+ 深拷贝后，b1 与b4不再相干

```python
>>> b1 ; b4
['name', 123, ['python', 'pascal', 999]]
['name', 123, ['python', 'pascal', 999]]
>>> b4[2].pop()
999
>>> b4[1] = 1111
>>> b1 ; b4
['name', 123, ['python', 'pascal', 999]]
['name', 1111, ['python', 'pascal']]
```

#### 4. 总结
+ 结论:无论深拷贝还是浅拷贝，复制的是容器对象，区别在于1层还是多层;对数字，字符串元组等没有内置拷贝方法
+ 浅拷贝只拷贝顶层引用
+ 深拷贝会逐层进行拷贝，直到拷贝的所有引用都是不可变引用为止



-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
