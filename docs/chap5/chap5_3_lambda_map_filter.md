## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------
## 5.3 特殊函数

### 5.3.1 lambda 函数

+ `lambda` 是只用1行就能解决问题的函数
+ lambda语法: `lambda [arg[,arg]*]: expression`
```python
lambda parameters : expression
<==>
def <lambda>(parameters):
    return expression
```
+ 实例
```python
>>> (lambda x:x+3)(4)
7
>>> [(lambda x:x+3)(i) for i in range(10)]
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

### 5.3.2 map 函数

+ map(function, iterable, ...) -> map object(迭代器)
+ map 的逻辑:
```python
def my_map(func,*iterables):
    for i in zip(*iterables)
        yield func(*i)
```
+ 实例:
```python
实现3个以整数为元素的列表的对应元素相加
>>> lst1;lst2;lst3
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 0]
[7, 8, 9, 2, 1]
>>> m = map(lambda x,y,z:x+y+z, lst1,lst2,lst3)i	#map + lambda
>>> list(m)
[14, 17, 20, 15, 6]
>>> m = map(lambda *args:sum(args), lst1,lst2,lst3)	#map + lambda + sum
>>> list(m)
[14, 17, 20, 15, 6]
>>> [x+y+z for x,y,z in zip(lst1,lst2,lst3)]	#comprehension
[14, 17, 20, 15, 6]
>>> [sum(i) for i in zip(lst1,lst2,lst3)]	#comprehension + sum
[14, 17, 20, 15, 6]
>>> [i for i in zip(lst1,lst2,lst3)]		#zip
[(1, 6, 7), (2, 7, 8), (3, 8, 9), (4, 9, 2), (5, 0, 1)]
```

+ `zip(iterables)`(iterables<sup>T</sup>) 与 `zip(*zip_obj)`(iterables) 互为转置矩阵,即: **iterables** =  `zip(*zip_obj)`
```python
>>> lst1;lst2;lst3
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 0]
[7, 8, 9, 2, 1]
>>> z = 'zip(lst1,lst2,lst3)'
>>> list(eval(z))
[(1, 6, 7), (2, 7, 8), (3, 8, 9), (4, 9, 2), (5, 0, 1)]
>>> zip(*eval(z))
<zip object at 0x7fd06ff1d240>
>>> list(zip(*eval(z)))
[(1, 2, 3, 4, 5), (6, 7, 8, 9, 0), (7, 8, 9, 2, 1)]
```


+ itertools.starmap(function, iterable,/)
```python
tertools.starmap(function, iterable)
'''
创建一个迭代器，使用从可迭代对象中获取的参数来计算该函数。
当参数对应的形参已从一个单独可迭代对象组合为元组时（数据已被“预组对”）
可用此函数代替 map()。
map() 与 starmap() 之间的区别可以类比 
function(a,b) 与 function(*c) 的区别
。大致相当于:
'''
def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)
```

### 5.3.3 filter 函数

+ [filter 官方文档](https://docs.python.org/zh-cn/3.9/library/functions.html#filter):
```
filter(function, iterable)¶
用 iterable 中函数 function 返回真的那些元素，构建一个新的迭代器。iterable 可以是一个序列，一个支持迭代的容器，或一个迭代器。如果 function 是 None ，则会假设它是一个身份函数，即 iterable 中所有返回假的元素会被移除。
请注意， filter(function, iterable) 相当于一个生成器表达式，当 function 不是 None 的时候为 (item for item in iterable if function(item))；function 是 None 的时候为 (item for item in iterable if item) 。
请参阅 itertools.filterfalse() 了解，只有 function 返回 false 时才选取 iterable 中元素的补充函数
```

+ filter 作过滤器使用
```
Help on class filter in module builtins:
class filter(object)
 |  filter(function or None, iterable) --> filter object
 |  
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
```
+ filter 逻辑:
```python
def my_filter(func,iterable):
    if func is None:
        func = bool
    for item in iterable:
        if func(item):
            yield item
```



+ 实例:
```python
>>> filter(lambda i:i>0, range(-5,5))
<filter object at 0x7fd06fccce20>
>>> list(filter(lambda i:i>0, range(-5,5)))
[1, 2, 3, 4]
```


+ itertools.filterfalse
```python
itertools.filterfalse(predicate, iterable)¶
'''
创建一个迭代器，
只返回 iterable 中 predicate 为 False 的元素。
如果 predicate 是 None，
返回真值测试为false的元素。
大致相当于：
'''
def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x
```

### functools.reduce()

+ [reduce 官方文档](https://docs.python.org/zh-cn/3.9/library/functools.html#functools.reduce)
```python
functools.reduce(function, iterable[, initializer])¶
将两个参数的 function 从左至右积累地应用到 iterable 的条目，以便将该可迭代对象缩减为单一的值。 例如，reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 是计算 ((((1+2)+3)+4)+5) 的值。 左边的参数 x 是积累值而右边的参数 y 则是来自 iterable 的更新值。 如果存在可选项 initializer，它会被放在参与计算的可迭代对象的条目之前，并在可迭代对象为空时作为默认值。 如果没有给出 initializer 并且 iterable 仅包含一个条目，则将返回第一项。
大致相当于：
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
请参阅 itertools.accumulate() 了解有关可产生所有中间值的迭代器。
```
+ help(functools.reduce)
```python
reduce(function, sequence[, initial]) -> value   
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
```

+ 实例:
```python
from functools import reduce
scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
             {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
             {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
             {'name':'Frances E. Allen', 'age':84, 'gender':'female'})
def reducer(accumulator , value):
    sum = accumulator + value['age']
    return sum
total_age = reduce(reducer, scientists, 0)
print(total_age)
```

+ reduce 测试:
```python
>>> lst = [1,1,1]
>>> reduce(lambda s,i:s*2+i,lst)
7
>>> reduce(lambda s,i:s*2+i,[])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: reduce() of empty sequence with no initial value
>>> reduce(lambda s,i:s*2+i,[],0)
0
>>> reduce(lambda s,i:s*2+i,[],2)
2
>>> reduce(lambda s,i:s*2+i,,2)
  File "<stdin>", line 1
    reduce(lambda s,i:s*2+i,,2)
                            ^
SyntaxError: invalid syntax
```

[一文搞懂python的map、reduce函数](https://zhuanlan.zhihu.com/p/77311224)



-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
