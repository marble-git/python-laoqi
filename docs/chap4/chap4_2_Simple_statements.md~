## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 4.2 简单语句

### 4.2.1 impot 语句

+ `import` 语句作用: 导入模块
+ ___import___  math  
+ ___import___ math ___as___ shuxue
+ ___import___ module [  ___as___  newnamw] (, module [as newname])*
+ ___from___ module  ___import___ idf [ ___as___ newidf ] (, idf [ as newidf ])*
+ ___from___ module ___import___ *



### 4.2.2 赋值 语句

+ 语法格式

```
assignment_stmt ::=  (target_list "=")+ (starred_expression | yield_expression)
target_list     ::=  target ("," target)* [","]
target          ::=  identifier
                     | "(" [target_list] ")"
                     | "[" [target_list] "]"
                     | attributeref
                     | subscription
                     | slicing
                     | "*" target
```



+ `unpacking` `star_list` ___[PEP 3132 -- Extended Iterable Unpacking](https://www.python.org/dev/peps/pep-3132/)___

+ x,y,z = 1,'python',['hello','world']
+ a = 1,2,3
+ `*a , = 3,4,5`
+ a,b = b,a
+ a = b = c = 333
+ `a,*b,c = range(7)`
+ `+=  -=  *=  /=  %= //= **= <<= >>= &= ^= |=` [PEP 203 -- Augmented Assignments](https://www.python.org/dev/peps/pep-0203/) 



```python
>>> x,y,z = 1 ,  'python' , ['hello','world']
>>> x ; y;z
1
'python'
['hello', 'world']
>>> a = 1,2,3 ; a
(1, 2, 3)
>>> a = b = c = 333; a;b;c
333
333
333
>>> *a , = 2,3,4
>>> a
[2, 3, 4]
>>> *a = 2,3,4
  File "<stdin>", line 1
SyntaxError: starred assignment target must be in a list or tuple
>>> a,*b,c=range(7) ; a ;b ;c
0
[1, 2, 3, 4, 5]
6
```





-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap4.md
[pre_chap]: chap4_1_operator.md
[next_chap]: chap4_3_if.md
