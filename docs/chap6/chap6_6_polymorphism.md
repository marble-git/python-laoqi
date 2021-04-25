## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 6.6 多态


+ python语言天然具有多态特性
+ [多态(polymorphism)是OOP的重要概念](https://www.wanweibaike.com/wiki-%E5%A4%9A%E6%80%81_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6))
+ 在编程语言和类型论中，多态（英语：polymorphism）指为不同数据类型的实体提供统一的接口[1]，或使用一个单一的符号来表示多个不同的类型[2]。
+ Python 不检查传入对象的类型，这种方式被称为“隐式类型(Laten Typing)”或者“结构式类型(Structual Typing)”或者[“鸭子类型(Duck Typing)”](https://www.wanweibaike.com/wiki-%E9%B8%AD%E5%AD%90%E7%B1%BB%E5%9E%8B)
+ `鸭子类型(Duck Typing)`:意味着可以向任何对象发送消息，语言只关心该对象能否接收该消息，不强求该对象是否为某一种特定的类型
+ 类型检查是毁掉多态的利器
+ 慎用`type isinstance issubclass` 类型检查函数

```python
#coding:utf-8
'''
    filename:ducktyping.py
'''
class Cat:
    def speak(self):
        print('cat speak:meow')
class Dog:
    def speak(self):
        print('Dog speak:woof!')
class Bob:
    def speak(self):
        print('Bob speak:welcome')
    def bow(self):
        print('thank you')
    def drive(self):
        print('beep,beep')
def cmd(pet):
    pet.speak()
pets = [Cat(),Dog(),Bob()]
for pet in pets:
    cmd(pet)
```





-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
