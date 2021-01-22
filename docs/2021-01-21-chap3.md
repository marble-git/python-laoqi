## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
----------------------------------------------------------------------------------
# 第3章  内置对象类型

##	3.1 初步了解对象

1. python中，世界是由`对象`组成的
2. 对象的`属性`，是什么
3. 对象的`方法`，能做什么


##	3.2 数字


### 3.2.1 整数

1. 使用`int` 表示整数

2. 使用`type()`查看数字的类型

```python
>>> 3
3
>>> type(3)
<class 'int'>
```

### 3.2.2 查看文档


#### 查看文档方法

1. 访问[python官方网站](https://python.org)查看[官方文档](https://docs.python.org/3/library/functions.html)
2. 使用内置函数`help（object)`查看本地文档


### 3.2.3 浮点数

1. 使用`float` 表示浮点数

```python
>>> 3.14
3.14
>>> type(3.14)
<class 'float'>
```

2. 数据类型转化`int()` `float()`

```python
>>> int(3.14)
3
>>> float(3)
3.0
```

3. 查看2个对象是否为同一个,使用函数`id()`取得对象的内存地址

```python
>>> id(3)
140058915744112
>>> id(3.0)
140058914305008
```

4. 综上，`int`和`float`除了表示类型和类别，还能够实现对象的类型转换


### 3.2.4 变量

1. `变量`依附于`对象`而存在
	> python中一个重要观点: *** 对象有类型，变量无类型 *** 

```python
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

2. `变量`通过 `=` 引用`对象`，`这种关系` 称为`引用`

```python
>>> x=6.3
>>> x
6.3
```

3. 变量 ___引用___ 对象后， ***就代表了那个对象*** 

```python
>>> x=6
>>> type(x)
<class 'int'>
>>> x=6.6
>>> type(x)
<class 'float'>
```

4. 变量命名的基本规则
	* `变量名称`由`小写字母`、`数字`、`下划线`组成，且**不以数字**开头  `[a-z_]+[a-z0-9_]*`
	* 不使用`保留字`(`关键字`)	`keywords`
	* 单词之间用`下划线连接`	`python_book`
	* 使用`有意义的`单词		

##### 获取 关键字 列表

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### 3.2.5 简单的计算

1. 变量引用对象，即 变量赋值

`>>> a = 10 ; b= 2.5` 注意这种写法，多个语句之间使用英文 `;` 分割

等价于如下写法

```python
>>> a =10 
>>> b = 2.5
```

2. 数字的 `+` `-`  `*` 运算

```python
>>> a+b
12.5
>>> a-b
7.5
>>> a*b
25.0
```

3. 数字的 除法 `/` ,整除 `//` ,取余 `%` ,内置函数 `divmod()` 运算

```python
>>> 5/2
2.5
>>> 5//2
2
>>> 5%2
1
>>> divmod(5,2)
(2, 1)

```

4. 其他简单运算方式  乘方`a ** b` ,绝对值 `abs()`

```python
>>> 2**3
8
>>> abs(-23)
23
```

5. 计算机的10进制 2进制转换问题

```python
>>> 0.1+0.2
0.30000000000000004
>>> 0.1+0.1-0.2
0.0
>>> 0.1+0.1+0.1-0.3
5.551115123125783e-17
>>> 0.1+0.1+0.1-0.2
0.1000000000000000
```
##### 解决方法

* 简单的将结果四舍五入

```python
>>> round(1.23456,2)
1.23
>>> round(1.23456,3)
1.235
>>> round(1.2345,3)	#round()函数也无法幸免进制转换问题
1.234			#应该是: 1.235
```

* [彻底解决](#ancher) 依赖其他工具
详细见 3.2.7 节

6.  科学计数法 `a * 10 ^ b` 使用 `a [eE] b` 表示

```python
>>> 1.2 e 4
12000.0
>>> 1.2 E 4
12000.0
```

### 3.2.6 math 标准库

`标准库`随python附带安装，包含了`内置函数`中没有的常用`模块`
关于 `模块` ，详情见[第7章](2021-01-21-chap7.md)

1. 使用 `import` 引入一个模块

```python
>>> import math
```

2. 使用 `dir()` 查看模块提供的所有函数

```python
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```

3. 使用 `help()` 查看模块的方法的本地帮助文档 
 
```python
>>> help(math.pow)
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).
(END)

```

4. 使用 `math` 标准库

计算数学表达式 `sin(PI/4) + lg5 * e^2` ，结果保留2位小数

```python
>>> round( math.sin(math.pi/4) + math.log10(5) * math.exp(2) , 2)
5.87
```

### 3.2.7 解决异常

1. `decimal` 实现了进制数的精确运算

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> import decima
>>> help(decimal.Decimal)
Help on class Decimal in module decimal:

class Decimal(builtins.object)
 |  Decimal(value='0', context=None)
 |  
 |  Construct a new Decimal object. 'value' can be an integer, string, tuple,
 |  or another Decimal object. If no value is given, return Decimal('0'). The
 |  context does not affect the conversion and is only passed to determine if
 |  the InvalidOperation trap is active.

>>> a = decimal.Decimal(0.1)
>>> a
Decimal('0.1000000000000000055511151231257827021181583404541015625')
>>> a = decimal.Decimal('0.1')	#
>>> a
Decimal('0.1')
>>> b = decimal.Decimal('0.2')
>>> a + b
Decimal('0.3')
```


2. `fractions`实现了基于有理数的运算

```python
>>> import fractions
>>> help(fractions.Fraction)
Help on class Fraction in module fractions:

class Fraction(numbers.Rational)
 |  Fraction(numerator=0, denominator=None, *, _normalize=True)
 |  
 |  This class implements rational numbers.
 |  
 |  In the two-argument form of the constructor, Fraction(8, 6) will
 |  produce a rational number equivalent to 4/3. Both arguments must
 |  be Rational. The numerator defaults to 0 and the denominator
 |  defaults to 1 so that Fraction(3) == 3 and Fraction() == 0.
 |  
 |  Fractions can also be constructed from:
 |  
 |    - numeric strings similar to those accepted by the
 |      float constructor (for example, '-2.3' or '1e10')
 |  
 |    - strings of the form '123/456'
 |  
 |    - float and Decimal instances
 |  
 |    - other Rational instances (including integers)
 |  
 |  Method resolution order:
 |      Fraction
 |      numbers.Rational
 |      numbers.Real
 |      numbers.Complex
 |      numbers.Number
 |      builtins.object
>>> fractions.Fraction(10,3)
Fraction(10, 3)
>>> fractions.Fraction(10/6)
Fraction(7505999378950827, 4503599627370496)
>>> c = fractions.Fraction('10/6')
Fraction(5, 3)
```


3. `decimal` 和 `fractions` 不是 `int` ,`float`类型 ，但仍然能够参与数学运算


运算结果类型|		|			|			|			|
------------------------|-----------------------|-----------------------|-----------------------|-------------------
`类型/类型`		|`int`			|`float`		|`decimal.Decimal`	|`fractions.Fraction`
`int`			|int			|float			|decimal.Decimal	|fractions.Fraction
`float`			|float			|float			|TypeError		|float
`decimal.Decimal`	|Decimal.Decimal	|TypeError		|decimal.Decimal	|TypeError
`fractions.Fraction`	|fractions.Fraction	|float			|TypeError		|fractions.Fraction

```python
>>> a
Decimal('0.1')
>>> b
Decimal('0.2')
>>> c
Fraction(5, 3)
>>> 1 + a
Decimal('1.1')
>>> 1 + c
Fraction(8, 3)
>>> 1.0 + c
2.666666666666667
```

4. 注意 `decimal` 和 `fractions` 不能混用

```python
>>> a
Decimal('0.1')
>>> c
Fraction(5, 3)
>>> a + c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'Fraction'

```



### 3.2.8 溢出

```python
>>> bin(40)
'0b101000'	#0b 后是二进制形式

```

在有的语言中整数有位数限制，超出范围会出现`整数溢出`

1. python中整数 `int` 是`任意精度`

```python
>>> a = 2 ** 10000
>>> a
19950631168807583848837421626835850838234968318861924548520089498529438830221946631919961684036194597899331129423209124271556491349413781117593785932096323957855730046793794526765246551266059895520550086918193311542508608460618104685509074866089624888090489894838009253941633257850621568309473902556912388065225096643874441046759871626985453222868538161694315775629640762836880760732228535091641476183956381458969463899410840960536267821064621427333394036525565649530603142680234969400335934316651459297773279665775606172582031407994198179607378245683762280037302885487251900834464581454650557929601414833921615734588139257095379769119277800826957735674444123062018757836325502728323789270710373802866393031428133241401624195671690574061419654342324638801248856147305207431992259611796250130992860241708340807605932320161268492288496255841312844061536738951487114256315111089745514203313820202931640957596464756010405845841566072044962867016515061920631004186422275908670900574606417856951911456055068251250406007519842261898059237118054444788072906395242548339221982707404473162376760846613033778706039803413197133493654622700563169937455508241780972810983291314403571877524768509857276937926433221599399876886660808368837838027643282775172273657572744784112294389733810861607423253291974813120197604178281965697475898164531258434135959862784130128185406283476649088690521047580882615823961985770122407044330583075869039319604603404973156583208672105913300903752823415539745394397715257455290510212310947321610753474825740775273986348298498340756937955646638621874569499279016572103701364433135817214311791398222983845847334440270964182851005072927748364550578634501100852987812389473928699540834346158807043959118985815145779177143619698728131459483783202081474982171858011389071228250905826817436220577475921417653715687725614904582904992461028630081535583308130101987675856234343538955409175623400844887526162643568648833519463720377293240094456246923254350400678027273837755376406726898636241037491410966718557050759098100246789880178271925953381282421954028302759408448955014676668389697996886241636313376393903373455801407636741877711055384225739499110186468219696581651485130494222369947714763069155468217682876200362777257723781365331611196811280792669481887201298643660768551639860534602297871557517947385246369446923087894265948217008051120322365496288169035739121368338393591756418733850510970271613915439590991598154654417336311656936031122249937969999226781732358023111862644575299135758175008199839236284615249881088960232244362173771618086357015468484058622329792853875623486556440536962622018963571028812361567512543338303270029097668650568557157505516727518899194129711337690149916181315171544007728650573189557450920330185304847113818315407324053319038462084036421763703911550639789000742853672196280903477974533320468368795868580237952218629120080742819551317948157624448298518461509704888027274721574688131594750409732115080498190455803416826949787141316063210686391511681774304792596709376

```


2. 小心浮点数 `float溢出`

```python
>>> a * 0.1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: int too large to convert to float

```


3. 无穷大 `float('inf')` `float('-inf')` 与非数字 `float('nan')`

```python
>>> a=float('inf')
>>> b=float('-inf')
>>> c=float('nan')
>>> a
inf
>>> b
-inf
>>> c
nan
>>> a+1
inf
>>> b+1
-inf
>>> c+1
nan
>>> a+b
nan
>>> a/b
nan
>>> a*b
-inf
>>> a-b
inf
>>> b-a
-inf
>>> 2/a
0.0
>>> a/b
nan
>>> 2/c
nan

```


### 3.2.9  运算优先级

1. 在程序中，`可读性`非常重要

2. 在复杂表达式中，使用括号`()`能让表达式的可读性更强

3. `同一级别`的运算，按 `从左到右` 的顺序进行计算

python 中`优先级从低到高`的常用运算符

运算符|描述|运算符|描述
----------------|---------------|----|----------------
`or`		|布尔或		|`&`|按位与
`and`		|布尔与		|`<<,>>`|移位
`not x`		|布尔非		|`+,-`|加减
`in,not in`	|是否是其中成员	|`*,/,%`|乘，除，取余
`is,is not`	|两个对象是否为同一个|`+x,-x`|正负号
`<,<=,>,>=,!=,==`|比较		|`~x`|按位翻转
`\|`		|按位或		|`**`|指数
`^`		|按位异或		

### 3.2.10 一个简单的程序


1. 文件命名 `*.py`
> [force.py][force.py]
2. 文件组成

* 第一行 声明文件的编码格式 `#coding[=:] <encoding_format>`
* 由`3对` 单引号 `'` 或双引号 `"` 包裹的`本文档说明`
* 程序正文





###### force.py

```python
#coding=utf-8		# 编码说明
'''
my first program.	# 块注释，对本程序文件的说明
filename: force.py
'''

import math
f1 = 20
f2 = 10
alpha = math.pi / 3

x_force = f1+f2*math.sin(alpha)
y_force = f2*math.cos(alpha)

force = math.sqrt(x_force * x_force + y_force ** 2 )

print("The result is: ",round(force,2),'N')

```

3. 运行程序 `python3 *.py`

```python
root@computer:~/python# python3 force.py 
The result is:  29.09 N

```



------------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
[force.py]: ../force.py

