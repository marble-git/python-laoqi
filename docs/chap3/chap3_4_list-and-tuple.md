## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------
## 3.4 列表
* `列表list` 是python 的内置对象，具有强大的功能
* __列表是个筐，什么都能装__


### 3.4.1 创建列表


1. 列表创建的语法

```python
>>> lst = []
>>> type(lst)
<class 'list'>
>>> list('book')
['b', 'o', 'o', 'k']
>>> help(list)
Help on class list in module builtins:
class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
```

2. 上述`变量lst` 名称没有使用`list`，因为list用来表示了列表对象，即 ___变量的名称尽可能不与类型名重复___
3. 定义`空列表`， `"空"数字`，`"空"字符串`

```python
>>> list()
[]
>>> int()
0
>>> float()
0.0
>>> str()
''
```

4. `列表`也是一个`容器`， __`容器`中可以放的东西称为 列表的`元素`__，`列表的元素`可以是`任何类型的python对象`------ __‘什么都能装’__

```python
>>> a_lst = [1,2.2,'python',[],[1,2]]
>>> type(a_lst)
<class 'list'>
>>> a_lst
[1, 2.2, 'python', [], [1, 2]]
```

	+ 该列表的元素包含 `数字`，`字符串`，`空列表`，`非空列表`；还可以包含后续要学习的`任何python对象`，也包括`自定义的对象类型`( ___函数，类___  等)

5. `多维列表`，类似`数学中的矩阵`，`"列表套列表"`,当然，可以做`更多层的嵌套`

```python
>>> mul_lst = [ [1,2,3], [4,5,6], [7,8,9] ] 
>>> mul_lst
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
	+ 2维列表可以用来表示矩阵，第1个元素表示矩阵的第1行，以此类推
	+ 一个 `3 * 3` 的`单位矩阵`
	```python
	>>> lst = [ [1,0,0], [0,1,0], [0,0,1] ]
	>>> lst
	[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
	```


6. ___列表是序列，列表的元素可以重复，对位置敏感___

```python
>>> lst1 = [1,2,3,3]
>>> lst2 = [2,1,3,3]
>>> lst1 is lst2
False
>>> id(lst1);id(lst2)
140169419285568
140169420334912
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

### 3.4.2 索引和切片

1. 索引
	-  列表的索引建立方式与字符串一样
	```python
	>>> lst = list('abcde')
	>>> lst
	['a', 'b', 'c', 'd', 'e']
	>>> lst[0]
	'a'
	>>> lst[-1]
	'e'
	>>> lst[4]
	'e'
	>>> lst[-5]
	'a'
	>>> lst.index('a')
	0
	>>> lst.index('e')
	4
	```


2. 切片
	- 对列表进行切片的基本方法与字符串中的方法也一致
	-  __列表的切片公式__  ___L[index<sub>start</sub>:index<sub>stop</sub>:step]___ 与字符串类似，只是对象由字符串换成列表
	- `每次切片`都是`新建了对象`， __不对原列表进行修改__ ，这种特点与字符串依然相同
	```python
	>>> lst = list('abcde')
	>>> lst
	['a', 'b', 'c', 'd', 'e']
	>>> lst[1:3]
	['b', 'c']
	>>> lst[-4:3]
	['b', 'c']
	>>> lst[:3]
	['a', 'b', 'c']
	>>> lst[1:]
	['b', 'c', 'd', 'e']
	>>> lst[::2]
	['a', 'c', 'e']
	>>> lst[::-1]
	['e', 'd', 'c', 'b', 'a']
	>>> lst
	['a', 'b', 'c', 'd', 'e']
	```

3. __获取多维列表中的元素__

```python
>>> mul_lst
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> mul_lst[0]
[1, 2, 3]
>>> mul_lst[0][2]
3
>>> mul_lst[0][1:]
[2, 3]
>>> mul_lst[1:]
[[4, 5, 6], [7, 8, 9]]
```

4. `列表`和`字符串`的`最大区别`，  ___列表创建后，可以进行修改，而字符串不能修改___

```python
>>> lst[0] = 111
>>> lst
[111, 'b', 'c', 'd', 'e']
>>> s= 'abc'
>>> s[0]=111
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> s[0]='1'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> s
'abc'
```

### 3.4.3 列表的基本操作

1. `"+"` `连接`
2. `"*"` `重复`
3. `“len()”` `获取元素个数`
4. `“in”` 判断 __元素__ 是否在 ___容器___ 中
5. 上述操作都是新生成了一个列表，没有对原列表进行修改

```python
>>> lst1 = list('abc')
>>> lst2 = [1,2,3]
>>> lst1 +lst2
['a', 'b', 'c', 1, 2, 3]
>>> lst1 * 3
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
>>> len(lst1)
3
>>> 'a' in lst1
True
>>> 1 in lst1
False
>>> lst1
['a', 'b', 'c']
>>> lst2
[1, 2, 3]
>>> help(len)
Help on built-in function len in module builtins:
len(obj, /)
    Return the number of items in a container.
(END)
```

### 3.4.4 列表的方法

#### 1. 查看列表的方法

+ 使用`dir(list)`查看列表的方法

```python
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

+ Python中，命名都本着 ***望文生义*** 的原则，通过对象的名称可以猜测其大致功能

#### 2. 增加列表的元素

+ 增加列表元素的方法包括 `append()` ,`insert()`, `extend()`
+ 通过`help()`函数查看并阅读对象的方法的帮助文档

```python
>>> help(list.append)
Help on method_descriptor:
append(self, object, /)
    Append object to the end of the list.
(END)
>>> help(list.insert)
Help on method_descriptor:
insert(self, index, object, /)
    Insert object before index.
(END)
>>> help(list.extend)
Help on method_descriptor:
extend(self, iterable, /)
    Extend list by appending elements from the iterable.
(END)
```

+ 列表方法的几个注意点: `返回值`,`原地修改 id()`

```python
>>> cities = ['soochow','beijing'] ; id(cities) ; cities
140477373115840
['soochow', 'beijing']
```

+ `append()`方法

```python
>>> r = cities.append('hangzhou') ; id(cities) ; cities ;print(r)
140477373115840
['soochow', 'beijing', 'hangzhou']
None
```

+ `insert()`方法 实现了在列表任何位置插入对象的操作

```python
>>> r = cities.insert(1,'shanghai') ; id(cities) ; cities ;print(r)
140477373115840
['soochow', 'shanghai', 'beijing', 'hangzhou']
None
>>> r = cities.insert(len(cities),'ningbo') ; id(cities) ; cities ;print(r)
140477373115840
['soochow', 'shanghai', 'beijing', 'hangzhou', 'ningbo']
None
>>> r = cities.insert(99,'ningbo') ; id(cities) ; cities ;print(r)
140477373115840
['soochow', 'shanghai', 'beijing', 'hangzhou', 'ningbo', 'ningbo']
None
>>> r = cities.insert(-99,'ningbo') ; id(cities) ; cities ;print(r)
140477373115840
['ningbo', 'soochow', 'shanghai', 'beijing', 'hangzhou', 'ningbo', 'ningbo']
None
```

+ `extend()` 方法
	- 参数对象必须是`iterable` 可迭代的

	```python
	>>> lst = [1,2,3]
	>>> r = cities.extend(lst) ; id(cities) ; cities ;print(r)
	140477373115840
	['ningbo', 'soochow', 'shanghai', 'beijing', 'hangzhou', 'ningbo', 'ningbo', 1, 2, 3]
	None
	>>> r = cities.extend('python') ; id(cities) ; cities ;print(r)
	140477373115840
	['ningbo', 'soochow', 'shanghai', 'beijing', 'hangzhou', 'ningbo', 'ningbo', 1, 2, 3, 'p', 'y', 't', 'h', 'o', 'n']
	None
	>>> r = cities.extend(123) ; id(cities) ; cities ;print(r)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'int' object is not iterable
	>>> a = range(5)
	>>> a
	range(0, 5)
	>>> r = cities.extend(a) ; id(cities) ; cities ;print(r)
	140477373115840
	['ningbo', 'soochow', 'shanghai', 'beijing', 'hangzhou', 'ningbo', 'ningbo', 1, 2, 3, 'p', 'y', 't', 'h', 'o', 'n', 0, 1, 2, 3, 4]
	None
	```

	- 判断对象是否是可迭代的
		* 使用内建函数 `hasattr()` 判断一个对象是否可迭代,该方法本质是看类型中是否有 `__iter__()` 这个特殊方法.  <==> __`'__iter__' in  dir(str)`__
		```python
		>>> help(hasattr)
		Help on built-in function hasattr in module builtins:
		hasattr(obj, name, /)
		    Return whether the object has an attribute with the given name.
		    This is done by calling getattr(obj, name) and catching AttributeError.
		(END)
		>>> a_str = 'python'
		>>> hasattr(a_str,'__iter__')
		True
		>>> a_lst= []
		>>> hasattr(a_lst,'__iter__')
		True
		>>> hasattr(3,'__iter__')
		False
		```

+ 比较 `append` 和`extend`

```python
>>> cities ; lst
['soochow', 'shanghai', 'beijing', 'hangzhou']
[1, 2, 3]
>>> cities.append(lst) ; cities
['soochow', 'shanghai', 'beijing', 'hangzhou', [1, 2, 3]]
>>> cities.pop() ; cities; 
[1, 2, 3]
['soochow', 'shanghai', 'beijing', 'hangzhou']
>>> cities.extend(lst) ; cities
['soochow', 'shanghai', 'beijing', 'hangzhou', 1, 2, 3]
```

#### 3. 删除列表的元素

+ 删除列表元素的方法包括 `remove()` **根据值删除元素** ; 和 `pop()` **根据索引删除元素** ; `clear()` **清空列表**

```python
>>> help(list.remove)
Help on method_descriptor:
remove(self, value, /)
    Remove first occurrence of value.
    Raises ValueError if the value is not present.
(END)
>>> help(list.pop)
Help on method_descriptor:
pop(self, index=-1, /)
    Remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.
(END)
```

+  `remove()` **根据值删除元素** ；如果指定元素不在列表中，报错；避免报错方法，提前判断元素是否在列表中

```python
>>> cities ; id(cities)
['soochow', 'shanghai', 'beijing', 'hangzhou', 1, 2, 3]
140477373151680
>>> r = cities.remove(1) ; cities ; id(cities) ; print(r)
['soochow', 'shanghai', 'beijing', 'hangzhou', 2, 3]
140477373151680
None
>>> r = cities.remove(1) ; cities ; id(cities) ; print(r)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 1 in cities
False
>>> 2 in cities
True
>>> r = cities.remove(2) ; cities ; id(cities) ; print(r)
['soochow', 'shanghai', 'beijing', 'hangzhou', 3]
140477373151680
None
```

+ `pop()` **根据索引删除元素** ; 返回被删除的元素的值  ;若 `pop()` 方法的参数列表为空，则删除列表的最后一个元素；

```python
>>> cities ; id(cities)
['soochow', 'shanghai', 'beijing', 'hangzhou', 3]
140477373151680
>>> r = cities.pop(1) ; cities ; id(cities) ; print(r)
['soochow', 'beijing', 'hangzhou', 3]
140477373151680
shanghai
>>> r = cities.pop() ; cities ; id(cities) ; print(r)
['soochow', 'beijing', 'hangzhou']
140477373151680
3
```

+ `clear()` **清空列表** ,将列表变为空列表; 列表的内存地址没变，即对象还是原来的对象

```python
>>> cities ; id(cities)
['soochow', 'beijing', 'hangzhou']
140477373151680
>>> r = cities.clear() ; cities ; id(cities) ; print(r)
[]
140477373151680
None
```

	- 下述操作与`clear`结果看似一样，都是最终得到一个空列表；但这里的`temp`实质上是变量先后引用了2个不同的对象
	```python
	>>> temp = ['hello'] ; temp ; id(temp)
	['hello']
	140477373174016
	>>> temp = [] ; temp ; id(temp)
	[]
	140477372675776
	```

#### 4. 列表元素的排序

+ 对列表元素排序的方法有 `list.sort()` **列表的方法** ; `sorted()` **内置函数**

```python
>>> help(list.sort)
Help on method_descriptor:
sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).
    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.
    The reverse flag can be set to sort in descending order.
(END)
>>> help(sorted)
Help on built-in function sorted in module builtins:
sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
(END)
```

+ `list.sort()` 方法;原地修改;没有返回值;默认由小到大排序;`reverse=True`参数由大到小 ; `key` 根据指定方法排序

```python
>>> a = [6,1,5,3] ; id(a) ; a
140477373176896
[6, 1, 5, 3]
>>> s = a.sort() ; id(a) ; a ; print(s)
140477373176896
[1, 3, 5, 6]
None
>>> s = a.sort(reverse=True) ; id(a) ; a ; print(s)
140477373176896
[6, 5, 3, 1]
None
```
	- `sort()` 方法的 `key` 参数
	```python
	>>> lst = ['python','java','c','pascal','basic','c++'] ; lst
	['python', 'java', 'c', 'pascal', 'basic', 'c++']
	>>> lst.sort() ; lst
	['basic', 'c', 'c++', 'java', 'pascal', 'python']
	>>> lst.sort(key = len) ; lst
	['c', 'c++', 'java', 'basic', 'pascal', 'python']
	>>> lst.sort(key = lambda x:x[-1]) ; lst
	['c++', 'java', 'c', 'basic', 'pascal', 'python']
	```

+ 内置函数 `sorted()`, **返回1个新的列表对象** ***这是两种排序方法最大的区别***

```python
>>> s = sorted(lst) ; id(lst) ; lst ; print(s) ;id(s)
140477373152192
['python', 'java', 'c', 'pascal', 'basic', 'c++']
['basic', 'c', 'c++', 'java', 'pascal', 'python']
140477373115840
```


#### 5. 列表元素的反转

+ 列表元素反转方法有: *列表`切片`* *列表的方法`list.reverse()`* *内置函数`reversed()`*

```python
>>> help(list.reverse)
Help on method_descriptor:
reverse(self, /)
    Reverse *IN PLACE*.
(END)
>>> help(reversed)
Help on class reversed in module builtins:
class reversed(object)
 |  reversed(sequence, /)
 |  Return a reverse iterator over the values of the given sequence.
```

- 列表切片

```python
>>> lst
['python', 'java', 'c', 'pascal', 'basic', 'c++']
>>> lst[::-1]
['c++', 'basic', 'pascal', 'c', 'java', 'python']
```

- 列表的 `list.reverse()` 方法，原地修改；没有返回值；

```python
>>> lst ; id(lst) ; 
['python', 'java', 'c', 'pascal', 'basic', 'c++']
140477373151872
>>> r = lst.reverse() ; lst ;id(lst) ;print(r)
['c++', 'basic', 'pascal', 'c', 'java', 'python']
140477373151872
None
```

- 内置函数 `reversed()`，得到1个新的 **迭代器** 对象；函数参数可以是任何序列；迭代器对象转化为列表

```python
>>> lst ; id(lst) ; 
['c++', 'basic', 'pascal', 'c', 'java', 'python']
140477373151872
>>> r = reversed(lst) ; lst ;id(lst) ;print(r) ; r ;type(r) ;list(r)
['c++', 'basic', 'pascal', 'c', 'java', 'python']
140477373151872
<list_reverseiterator object at 0x7fc36fe74850>
<list_reverseiterator object at 0x7fc36fe74850>
<class 'list_reverseiterator'>
['python', 'java', 'c', 'pascal', 'basic', 'c++']
>>> s = 'python' ; id(s)
140477377383920
>>> r = reversed(s) ; s ;id(s) ;print(r) ; r ;type(r) ;list(r) ;str(r) ; id(r) 
'python'
140477377383920
<reversed object at 0x7fc370209670>
<reversed object at 0x7fc370209670>
<class 'reversed'>
['n', 'o', 'h', 't', 'y', 'p']
'<reversed object at 0x7fc370209670>'
140477376534128
```

#### 6. 字符串和列表的相互转化
+ 字符串转化为列表`list(String)` `L.extend(String)`

```python
>>> list('python')
['p', 'y', 't', 'h', 'o', 'n']
>>> list.extend('python')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor 'extend' for 'list' objects doesn't apply to a 'str' object
>>> lst=[]
>>> lst.extend('python')
>>> lst
['p', 'y', 't', 'h', 'o', 'n']
```

+ 列表转化为字符串 `''.join(L)`

```python
>>> lst 
['p', 'y', 't', 'h', 'o', 'n']
>>> s = ''.join(lst)
>>> s
'python'
>>> lst
['p', 'y', 't', 'h', 'o', 'n']
>>> s = str(lst)
>>> s
"['p', 'y', 't', 'h', 'o', 'n']
>>> lst.append(2)
>>> lst
['p', 'y', 't', 'h', 'o', 'n', 2]
>>> s = ''.join(lst)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 6: expected str instance, int found
>>> help(''.join)
Help on built-in function join:
join(iterable, /) method of builtins.str instance
    Concatenate any number of strings.
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
(END)
```

## 3.5 元组

#### 1. 元组的定义

+ 元组使用圆括号`()` , `tuple([Iterable])` 进行定义

```python
>>> t = (1,"a",[1,2]) ; t ;type(t)
(1, 'a', [1, 2])
<class 'tuple'>
>>> t2 = tuple() ; t2 ; type(t2)
()
<class 'tuple'>
>>> t3 = () ; t3 ; type(t3)
()
<class 'tuple'>
>>> tuple([1,2,3])
(1, 2, 3)
```

+ **注意** ***如果定义的元组中只有一个元素，需要添加 `,`***

```python
>>> one = (1,)
>>> one = (1,) ; type(one) ; one
<class 'tuple'>
(1,)
>>> one2 = (1) ; type(one2) ; one2
<class 'int'>
1
>>> one3 = [1] ; type(one3) ; one3
<class 'list'>
[1]
>>> tuple(one3)
(1,)
```


#### 2. 元组属于序列，具有序列的所有特点和基本操作

+ 元组的索引和切片

```python
>>> t = (1,'23',[123,'abc'],('python','learn'))
>>> t
(1, '23', [123, 'abc'], ('python', 'learn'))
>>> t[2]
[123, 'abc']
>>> t[2][1]
'abc'
>>> t[3][1]
'learn'
>>> t[1][1]
'3'
>>> t[::-1]
(('python', 'learn'), [123, 'abc'], '23', 1)
>>> t[::2]
(1, [123, 'abc'])
```

+ 元组的序列的基本操作 `+`,`*`,`len()`,`in`

```python
>>> t1 = (1,2,3)
>>> t2 = tuple('abc')
>>> t1 ; t2
(1, 2, 3)
('a', 'b', 'c')
>>> t1 + t2
(1, 2, 3, 'a', 'b', 'c')
>>> t1 * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> len(t1)
3
>>> 1 in t1
True
>>> 'a' in t1
False
>>> 'a' in t2
True
```

#### 3. 元组和列表的最大差别，元组不能通过索引修改某个元素

```python
>>> dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t
(1, '23', [123, 'abc'], ('python', 'learn'))
>>> t[2] = 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t[2][0] = 0
>>> t
(1, '23', [0, 'abc'], ('python', 'learn'))
```

#### 4. 元组和列表的相互转化
+ 元组不可修改，如果要修改元组但可以变通, **将元组转化为列表，然后修改元素，再转化为元组**
+ 使用`list()` 和`tuple()` 进行列表和元组的转化

```python
>>> t
(1, '23', [0, 'abc'], ('python', 'learn'))
>>> tls = list(t) ; tls
[1, '23', [0, 'abc'], ('python', 'learn')]
>>> t_tuple = tuple(tls) ; t_tuple
(1, '23', [0, 'abc'], ('python', 'learn'))
>>> tt = tuple('book')
>>> tt
('b', 'o', 'o', 'k')
>>> ''.join(tt)
'book'
```

#### 5. 相较于列表， ***元组的使用场景***
+ 元组比列表操作速度快。如果定义了一个值，并且唯一要用它做的是 **不断地遍历它** ，使用元组
+ 对不需要修改的数据(即该数据是 **常量** )进行 **"写保护"** ，使用元组; 如果必须改变这些值，则可以转换为列表修改
+ 元组可以在`字典`中被用作`key`,而列表不可以;字典的`key`必须是不可变的


-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap3.md
[pre_chap]: chap3_3_char-and-string.md
[next_chap]: chap3_6_dictionary.md
