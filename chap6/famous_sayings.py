#coding:utf-8

'''
    filename:famous_sayings.py
        chap:6
    subject:17
    conditions:format output string
    solution:class FamousSayings
'''


class FamousSayings:
    def __init__(self,author,sayings):
        self.author = author
        self.sayings = sayings
    def __repr__(self):
        return '{}: {}'.format(self.author,self.sayings)

if __name__ == '__main__':
    pass
    s1 = FamousSayings('子曰','学而时习之，不亦乐乎。')
    s2 = FamousSayings('李白','安能摧眉折腰事权贵，使我不得开心颜。')
    print(s1)
    print(s2)

