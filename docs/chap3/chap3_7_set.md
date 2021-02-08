## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------
## 3.7 集合 set

+ 无序性: 集合不是序列,没有 `index` 方法 ，也不能使用 `s[1]`形式访问集合元素
+ 互异性: 元素唯一，不能重复;set 对象是由具有唯一性的 hashable 对象所组成的无序多项集
+ 确定性: 元素必须是不可变对象，immutable
+ `set` 的[官方详解](https://docs.python.org/zh-cn/3/library/stdtypes.html#set-types-set-frozenset)
```python
>>> s = set('python') ; s
{'p', 'o', 't', 'h', 'n', 'y'}
>>> s[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
```

### 3.7.1 创建集合
#### 1. 可以使用 `{}` 和 `set()` 创建集合
```python
>>> help(set)
Help on class set in module builtins:
class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
```
+ **只能使用 `set()` 创建空集** ; `{}` 创建的是空字典，不是空集
```python
>>> set() ; type(set()) ; {} ; type({})
set()
<class 'set'>
{}
<class 'dict'>
```
+ 使用 `{}` 创建集合
```python
>>> s = {1,2,3,3,2,1,1}
>>> s
{1, 2, 3}
```
+ 使用 `set()` 创建集合;无参数创建空集;参数为 **可迭代对象 `iterable`** 
```python
>>> set()
set()
>>> set([1,2,3,2,3,1,1])
{1, 2, 3}
>>> hasattr(list,'__iter__') ; set([1,2,3,1,2,3,3,4])
True
{1, 2, 3, 4}
>>> hasattr(dict,'__iter__') ; set(dict(a=1,b=2,c=3))
True
{'a', 'c', 'b'}
>>> hasattr(set,'__iter__') ; set(set([1,2,3,4,2,3,1,2]))
True
{1, 2, 3, 4}
```


#### 2. `hashable` 可哈希
+ 关于 `mutable` `immutable` `hashable` 的[官方解释](https://docs.python.org/zh-cn/3/glossary.html)
> **hashable -- 可哈希**
> 一个对象的哈希值如果在其生命周期内绝不改变，就被称为 可哈希 （它需要具有 __hash__() 方法），并可以同其他对象进行比较（它需要具有 __eq__() 方法）。可哈希对象必须具有相同的哈希值比较结果才会相同。
> 
> 可哈希性使得对象能够作为字典键或集合成员使用，因为这些数据结构要在内部使用哈希值。
> 大多数 Python 中的不可变内置对象都是可哈希的；可变容器（例如列表或字典）都不可哈希；不可变容器（例如元组和 frozenset）仅当它们的元素均为可哈希时才是可哈希的。 用户定义类的实例对象默认是可哈希的。 它们在比较时一定不相同（除非是与自己比较），它们的哈希值的生成是基于它们的 id() 
>
> **mutable -- 可变**
> 可变对象可以在其 id() 保持固定的情况下改变其取值。另请参见 immutable
>
> **immutable -- 不可变**
> 具有固定值的对象。不可变对象包括数字、字符串和元组。这样的对象不能被改变。如果必须存储一个不同的值，则必须创建新的对象。它们在需要常量哈希值的地方起着重要作用，例如作为字典中的键。

```Python
>>> s = {'google'} ; s
{'google'}
>>> s = {'google',['python','java','pascal']} ; s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> s = {'google',{'city':'soochow','age':29}} ; s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
```
+ `hashable` 对象是  `immutable`不可变的
+ `mutable`对象都是   `unhashable` 不可散列的
```python
>>> t1 = (1,2,3)
>>> t2 = (1,[2,3])
>>> hash(t1)
529344067295497451
>>> hash(t2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> t2 ; id(t2) ; t2[1][0]='php' ; t2 ; id(t2)
(1, [2, 3])
140677681473472
(1, ['php', 3])
140677681473472
```

#### 3. `re` 正则表达式 `regular expression` `regex` `regexp` `RE`

[正则表达式的官方文档](https://docs.python.org/zh-cn/3/library/re.html#raw-string-notation)
> **原始字符串标记¶** 
> 原始字符串记法 `(r"text")` 保持正则表达式正常。否则，每个正则式里的反斜杠`('\')` 都必须前缀一个反斜杠来转义

```python
>>> help(re.split)
Help on function split in module re:
split(pattern, string, maxsplit=0, flags=0)
    Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.  If
    capturing parentheses are used in pattern, then the text of all
    groups in the pattern are also returned as part of the resulting
    list.  If maxsplit is nonzero, at most maxsplit splits occur,
    and the remainder of the string is returned as the final element
    of the list.
(END)
```
+ 去掉下面这段话中重复的单词
```
  Brothers,it is clear to me that I have not come to that knowledge; but one thing I do,
letting go those things which are past, and stretching out to the things which are before, I
go forward to the mark,even the reward of the high purpose of God in Christ Jesus.
```
```python
>>> s = '''Brothers,it is clear to me that I have not come to that knowledge; but one thing I do,
letting go those things which are past, and stretching out to the things which are before, I
go forward to the mark,even the reward of the high purpose of God in Christ Jesus.'''
>>> s
'Brothers,it is clear to me that I have not come to that knowledge; but one thing I do,\nletting go those things which are past, and stretching out to the things which are before, I\ngo forward to the mark,even the reward of the high purpose of God in Christ Jesus.'
>>> import re
>>> lst = re.split(r'\W+',s) ; lst
['Brothers', 'it', 'is', 'clear', 'to', 'me', 'that', 'I', 'have', 'not', 'come', 'to', 'that', 'knowledge', 'but', 'one', 'thing', 'I', 'do', 'letting', 'go', 'those', 'things', 'which', 'are', 'past', 'and', 'stretching', 'out', 'to', 'the', 'things', 'which', 'are', 'before', 'I', 'go', 'forward', 'to', 'the', 'mark', 'even', 'the', 'reward', 'of', 'the', 'high', 'purpose', 'of', 'God', 'in', 'Christ', 'Jesus', '']
>>> len(lst) ; set1 = set(lst) ;len(set1)
54
40
>>> set1
{'Jesus', 'stretching', '', 'Brothers', 'have', 'me', 'not', 'but', 'I', 'thing', 'mark', 'do', 'high', 'are', 'those', 'before', 'clear', 'reward', 'and', 'knowledge', 'come', 'is', 'go', 'of', 'past', 'letting', 'which', 'it', 'one', 'to', 'things', 'Christ', 'even', 'purpose', 'that', 'in', 'God', 'forward', 'the', 'out'}
```

### 3.7.2 集合的方法
+ 集合 set 的 所有方法和属性
```python
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
```

#### 1. 增加元素
+ 增加集合元素的方法有: `set.add(elem)` `set.update(*others)`
```python
>>> help(set.add)
Help on method_descriptor:
add(...)
    Add an element to a set.
    This has no effect if the element is already present.
(END)
>>> help(set.update)
Help on method_descriptor:
update(...)
    Update a set with the union of itself and others.
(END)
```
+ `set.add(elem)`向集合添加1个元素;即使添加集合的已有元素也没影响
```python
>>> s = set(); s
set()
>>> s.add('python') ; s
{'python'}
>>> s.add('python',23) ; s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set.add() takes exactly one argument (2 given)
>>> s.add(23) ; s
{'python', 23}
>>> s.add(23) ; s
{'python', 23}
```
+ `set.update(*others)` (参数为 iterable)更新集合，添加来自 others 中的所有元素。
	- <==> `s |= set(other1) | set(other2) | ...`
	```python
	>>> s
	{'python', 23}
	>>> s.update(set('hello'))
	>>> s.update(set('hello')) ;s
	{'o', 'l', 'h', 'e', 23, 'python'}
	>>> s.update([1,2,3]) ;s
	{1, 2, 3, 'o', 'l', 'h', 'e', 23, 'python'}
	>>> s.update('abc') ;s
	{1, 2, 3, 'b', 'o', 'l', 'a', 'h', 'e', 'c', 23, 'python'}
	>>> s.update([99,100],('aaa','bbb')) ;s
	{1, 2, 3, 99, 'b', 100, 'o', 'l', 'a', 'h', 'aaa', 'e', 'c', 23, 'bbb', 'python'}
	>>> a = [1,2,3] ; b = ('99','00') ; c = 'abc'
	>>> s = set() ; s.update(a,b,c) ; s
	{1, 2, 3, 'b', '99', 'a', '00', 'c'}
	>>> s = set() ; s |= set(a) | set(b) | set(c) ; s
	{1, 2, 3, 'b', '99', 'a', '00', 'c'}
	>>> s = set() ; s |= a | b | c ; s
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: unsupported operand type(s) for |: 'list' and 'tuple'
	```

#### 2. 删除元素
+ 删除元素的方法有 `set.pop()` `set.remove(elem)` `set.discard(elem)` `set.clear()`  

```python
>>> help(set.pop)
pop(...)
    Remove and return an arbitrary set element.
    Raises KeyError if the set is empty.
(END)
>>> help(set.remove)
remove(...)
    Remove an element from a set; it must be a member.
    If the element is not a member, raise a KeyError.
(END)
>>> help(set.discard)
discard(...)
    Remove an element from a set if it is a member.
    If the element is not a member, do nothing.
(END)
>>> help(set.clear)
clear(...)
    Remove all elements from this set.
(END)
```


+ 请注意，`__contains__(), remove() 和 discard()` 方法的 elem 参数可能是一个 set。 为支持对一个等价的 frozenset 进行搜索，会根据 elem 临时创建一个该类型对象
+ 请注意，非运算符版本的 `update(), intersection_update(), difference_update() 和 symmetric_difference_update()` 方法将接受任意可迭代对象作为参数。


+ `set.pop()` 从集合中移除并返回任意一个元素。 如果集合为空则会引发 KeyError。
```python
>>> s
{1, 2, 3, 'b', '99', 'a', '00', 'c'}
>>> s.pop() ; s
1
{2, 3, 'b', '99', 'a', '00', 'c'}
>>> ss = set(); ss ; ss.pop() ; ss
set()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
```

+ `set.remove(elem)` 从集合中移除元素 elem;无返回值; 如果 elem 不存在于集合中则会引发 KeyError。
```python
>>> s
{3, 'b', '99', 'a', '00', 'c'}
>>> s.remove(3) ; s ;
{'b', '99', 'a', '00', 'c'}
>>> s.remove(3) ; s ;
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
```
+ `set.discard(elem)` 如果元素 elem 存在于集合中则将其移除;无返回值 ; 若不存在,不报错
```python
>>> s
{'b', 'a', '00', 'c'}
>>> s.discard('00') ; s
{'b', 'a', 'c'}
>>> s.discard('00') ; s
{'b', 'a', 'c'}
```

+ `set.clear()`  从集合中移除所有元素。无返回值
```python
>>> s = set('python') ; s ; s.clear() ; s
{'p', 'o', 't', 'h', 'n', 'y'}
set()
```



### 3.7.3 不变的集合

+ 以 `set()` 函数创建的集合都是 **可原地修改** 的集合，即 **可变集合**
+ 还有1种集合是 **不可变集合** ，创建这种集合要使用 `frozenset()` 函数

```python
>>> help(frozenset)
Help on class frozenset in module builtins:
class frozenset(object)
 |  frozenset() -> empty frozenset object
 |  frozenset(iterable) -> frozenset object
 |  
 |  Build an immutable unordered collection of unique elements.
>>> s = frozenset() ; s ;type(s)
frozenset()
<class 'frozenset'>
>>> frozenset('python') 
frozenset({'p', 'o', 't', 'h', 'n', 'y'})
>>> frozenset(set('abc')) 
frozenset({'a', 'c', 'b'})
```

+ 使用 `dir(frozenset)` 查看其属性和方法

```python
>>> dir(frozenset)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
```

+ `frozenset` 没有`set` 那些实现集合更改的操作方法;但两者都有一些与运算相关的方法
+ 不可变集合 `frozenset` 可以作为字典的键，而可变集合 `set` 不可以

```python
>>> f_s = frozenset('abc') ; f_s ; {f_s:1}
frozenset({'a', 'c', 'b'})
{frozenset({'a', 'c', 'b'}): 1}
>>> s = set('abc') ; s ; {s:1}
{'a', 'c', 'b'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
```

### 3.7.4 集合的关系和运算

* 元素与集合的关系只有一种: `'in' 'not in'`
* 集合与集合间的关系有:`'==' '!=' 'issubset <=' 'issuperset >=' 'isdisjoint'` 
* 集合间的运算有: `'union |' 'intersection &' 'difference -' 'symmetric_difference ^'`

#### 1. 元素与集合的关系

```python
>>> s = set('python') ; s 
{'p', 'o', 't', 'h', 'n', 'y'}
>>> 'a' in s ; 'p' in s
False
True
>>> 'a' not in s ; 'p' not in s
True
False
```

+ 使用 `len` 计算集合的元素个数

```python
>>> s ;len(s)
{'p', 'o', 't', 'h', 'n', 'y'}
6
```


#### 2. 集合与集合的关系

+ `'==' ‘!=’` 两个集合的元素完全一样，即两个集合相等 ; 否则不等
```python
>>> s1 = {1,2,3} ; s2 = {2,2,1,1,3,3,2,1} ;s1 ;s2
{1, 2, 3}
{1, 2, 3}
>>> s1 == s2 ; s1 != s2
True
False
>>> s 
{'p', 'o', 't', 'h', 'n', 'y'}
>>> s != s1
True
```
 + 'issubset <=' 子集关系和 ;真子集 `<`
 + 'superset >=' 超集;真超集 `>`
```python
>>> s1 ; s2 ; a ; b
{1, 2, 3}
{1, 2, 3}
{2, 4}
{2, 4, 6}
>>> s1.issubset(s2) ; s1 <= s2 ; s1 < s2
True
True
False
>>> s2.issuperset(s2) ; s2 >= s1 ; s2 > s1
True
True
False
>>> a.issubset(b) ; a <=b ; a < b
True
True
True
>>> b.issuperset(a) ; b >= a ; b > a
True
True
True
```

+ 'isdisjoint'` 集合相交与否
```python
>>> a = {1,2,3,4,5} ; b = {1,3,5,7,9} ; c = {2,4,6,8}
>>> a.isdisjoint(b) ; a.isdisjoint(c) ; b.isdisjoint(c)
False
False
True
```

#### 3. 集合间的运算

1. 'union |' 并集,结果是生成1个新的对象;`update |=` 是更新调用该方法的集合 
```python
>>> set.union.__doc__
'Return the union of sets as a new set.\n\n(i.e. all elements that are in either set.)'
>>> set.update.__doc__
'Update a set with the union of itself and others.'
>>> a = {1,3,5} ; b = {3,6,9}
>>> a.union(b) ; a | b
{1, 3, 5, 6, 9}
{1, 3, 5, 6, 9}
>>> a ; b
{1, 3, 5}
{9, 3, 6}
>>> a.update(b) ; a ; b
{1, 3, 5, 6, 9}
{9, 3, 6}
>>> a = {1,3,5} ; b = {3,6,9} ; a|=b ; a ; b
{1, 3, 5, 6, 9}
{9, 3, 6}
>>> s = set() ; s.union([1,2,3],'abc') ; s
{1, 2, 3, 'b', 'a', 'c'}
set()
>>> s = set() ; s.update([1,2,3],'abc') ;s
{1, 2, 3, 'b', 'a', 'c'}
```

2. 'intersection &'交集,结果是生成1个新的对象;`ntersection_update &=` 是更新调用该方法的集合 
```python
>>> set.intersection.__doc__
'Return the intersection of two sets as a new set.\n\n(i.e. all elements that are in both sets.)'
>>> set.intersection_update.__doc__
'Update a set with the intersection of itself and another.'
>>> a = {1,3,5} ; b = {3,6,9}
>>> a.intersection(b) ; a & b
{3}
{3}
>>> a.intersection_update(b) ; a ; b
{3}
{9, 3, 6}
>>> a = {1,3,5} ; b = {3,6,9} ; a &= b ; a ; b
{3}
{9, 3, 6}
>>> s = set('abcd1234') ; s.intersection('abc123','bcd2345') ;s
{'c', 'b', '2', '3'}
{'b', '2', 'a', '4', 'd', 'c', '3', '1'}
>>> s = set('abcd1234') ; s.intersection_update('abc123','bcd2345') ;s
{'c', 'b', '2', '3'}
```


 3. 'difference -'差集,结果是生成1个新的对象;`difference_update -=` 是更新调用该方法的集合 
```python
>>> set.difference.__doc__
'Return the difference of two or more sets as a new set.\n\n(i.e. all elements that are in this set but not the others.)'
>>> set.difference_update.__doc__
'Remove all elements of another set from this set.'
>>> a = {1,3,5} ; b = {3,6,9} 
>>> a.difference(b) ; a - b
{1, 5}
{1, 5}
>>> a.difference_update(b) ; a ; b
{1, 5}
{9, 3, 6}
>>> a = {1,3,5} ; b = {3,6,9} ; a -= b ; a ; b
{1, 5}
{9, 3, 6}
>>> s = set('abcd1234') ; s.difference('abcefg','123567') ; s
{'4', 'd'}
{'b', '2', 'a', '4', 'd', 'c', '3', '1'}
>>> s = set('abcd1234') ; s.difference_update('abcefg','123567') ; s
{'4', 'd'}
>>> a = {1,3,5} ; b = {3,6,9} 
>>> a - b ; b - a
{1, 5}
{9, 6}
```



 4. 'symmetric_difference ^'对称差集,结果是生成1个新的对象;`symmetric_difference_update ^=` 是更新调用该方法的集合 
```python
>>> set.symmetric_difference.__doc__
'Return the symmetric difference of two sets as a new set.\n\n(i.e. all elements that are in exactly one of the sets.)'
>>> set.symmetric_difference_update.__doc__
'Update a set with the symmetric difference of itself and another.'
>>> a = {1,3,5} ; b = {3,6,9} 
>>> a.symmetric_difference(b) ; a ^ b
{1, 5, 6, 9}
{1, 5, 6, 9}
>>> (a - b) | (b - a)
{1, 5, 9, 6}
>>> (a | b) - (a & b)
{1, 5, 6, 9}
>>> a - b | b - a  # <==> (a - b) | (b - a)注意 () 的作用
{1, 5, 9, 6}
>>> a | b - a & b  # <==> a | ((b -a) & b)  没有 () 时 按运算符优先级与结合性运算
{1, 3, 5, 6, 9}
>>> a = {1,3,5} ; b = {3,6,9}
>>> a ; b
{1, 3, 5}
{9, 3, 6}
>>> a.symmetric_difference_update(b) ; a ; b
{1, 5, 6, 9}
{9, 3, 6}
>>> a = {1,3,5} ; b = {3,6,9} ; a ^= b ; a ; b
{1, 5, 6, 9}
{9, 3, 6}
>>> s = set('abcd1234') ; s.symmetric_difference('abcxyz','1234567')  ; s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set.symmetric_difference() takes exactly one argument (2 given)
>>> s = set('abcd1234') ; s.symmetric_difference_update('abcxyz','1234567')  ; s
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set.symmetric_difference_update() takes exactly one argument (2 given)
```
[Python 运算符优先级和结合性一览表](http://c.biancheng.net/view/2190.html)

-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap3.md
[pre_chap]: chap3_6_dictionary.md
[next_chap]: ../2021-01-21-chap3.md
