
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 4.4 for循环语句

### 4.4.1 for循环基础应用


+ for语法

```
for_stmt ::=  "for" target_list "in" expression_list ":" suite
              ["else" ":" suite]
```

+ `target_list` 是赋值语句中的 等号左边的样式
+ `expression_list` 是由 赋值语句右边的样式为元素组成的 可迭代对象
+ 当循环规则 `target_list "in" expression_list` 不成立时;如果else子句块存在，则执行else分支
+ for 主句块中的 break 将导致循环终止;且不执行else 子句体
+ for 主句块中的 continue 将跳过子句体中剩余部分,并转往下一次循环;或没有下一项时执行else 子句体
+ 当 `expression_list` 在循环中被更改时 会引发问题;可以使用序列的切片来避免
```python
for x in a[:]
	if x<0:a.remove(x)
```







### 4.4.2 优化循环的函数

1. range 函数

+ 调用形式
```python
class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
```
+ 返回值是可迭代对象
+ range() 在循环中的一个重要作用是 ___可以创建序列对象的索引___
+ range() 生成可选范围内固定步长的序列
```python
>>> list(range(2,100,3))	#[2,100) 间隔 3
[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98]
```
+ step 可以为负
```python
>>> list(range(9,1,-1))
[9, 8, 7, 6, 5, 4, 3, 2]
```

2. zip 函数

+ zip参数是可迭代对象;值得关注的是返回值;返回的是zip对象,即生成器对象([详见6.11节]())
+ zip的作用就是将多个可迭代对象的元素进行映射
+ 将字典 d 的 key ,value 互换
```python
>>> d = dict(zip('abcdefgh',range(9))) ; d
{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
>>> dict(zip(d.values(),d.keys()))
{0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
```

3. enumerate 函数

+ enumerate(iterable,start=0) ->enumerate object
+ 参数为可迭代对象和计数索引起始值
+ 返回一个enumerate 生成器对象

+ 迭代器协议
- 迭代器协议:对象需要提供next方法,next方法要么返回迭代中的下一项，要么引起 Stopiteration 异常，以终止迭代
- 可迭代对象:实现了迭代器协议的对象
- 协议:是一种约定,可迭代对象实现迭代器协议，python的内置工具(for,sum,min,max等)使用迭代器协议访问对象
+ 有两种方法提供生成器
- 生成器函数:yield语句返回结果
- 生成器表达式:类似列表推导 `s = (x**2 for x in range(5))` 
+ 生成器只能遍历一遍


+ 生成器generator 总是迭代器iterator
+ 迭代器iterator总是可迭代的iterable
+ 迭代器iterator使用next(iterator)方法产生 next value
+ 可迭代对象iterable通过iter(iterable)返回一个迭代器对象iterator
+ 容器container通常是可迭代的iterable

4. random 模块[标准库]

+ random中的常用函数
+ 整数: random.randrange(stop)|random.randrange(start,stop[,step]) `a<= N <b`

+ random.randint(a,b) `a<= N <=b`
+ random.getrandbits(k) `0<= N < 2<sup>k<sup/>`
+ 序列: random.choice(seq) -> elem
+ random.shuffle(x[,random]) 将一个可变序列原地打乱顺序





### 4.4.3 列表解析 

+ [PEP 202 -- List Comprehensions](https://www.python.org/dev/peps/pep-0202/)
+ comprehension 列表`[]`,集合`{}`,字典`{}`  推导式
```pybnf
comprehension ::=  assignment_expression comp_for
comp_for      ::=  ["async"] "for" target_list "in" or_test [comp_iter]
comp_iter     ::=  comp_for | comp_if
comp_if       ::=  "if" expression_nocond [comp_iter]
```
+ `[f(x) for x in iterable]`
+ `[f(x) for x in iterable if cond(x)]`
+ `[f(x,y) for x in iterable for y in iterable]`
+ `[a if cond(x) else b for x in iterable]`





+ 生成器表达式 使用`()` [PEP 289 -- Generator Expressions](https://www.python.org/dev/peps/pep-0289/)
```pybnf
generator_expression ::=  "(" expression comp_for ")"
```






-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap4.md
[pre_chap]: chap4_3_if.md
[next_chap]: chap4_5_while.md
