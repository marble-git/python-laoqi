## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 4.3 条件语句

### 4.3.1 条件语句语法格式

```pybnf
if_stmt ::=  "if" assignment_expression ":" suite
             ("elif" assignment_expression ":" suite)*
             ["else" ":" suite]
```

+ 注意使用 `:=` 

```python
if s:= 2+3
	print(s)
```

### 4.3.2 简写格式

```
x = 1
a = 'python' if x>2 else 'physics'
```





-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
