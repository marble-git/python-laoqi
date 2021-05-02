#coding:utf-8

'''
    filename:arabic2roman.py
        chap:6
    subject:6
    conditions:translate Arabic numerals to Roman numerals
    solution:class Arabic2Roman
'''



class Arabic2Roman:
    trans = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
#        'I(a)X(b)V(c)I(d)'
    trans_unit = {1:(0,0,0,1),2:(0,0,0,2),3:(0,0,0,3),
            4:(1,0,1,0),5:(0,0,1,0),
            6:(0,0,1,1),7:(0,0,1,2),8:(0,0,1,3),
            9:(1,1,0,0)}
    def __init__(self,digit):
        self.digit = digit
        self.roman = self.get_roman()
    def __str__(self):
        return f'{self.digit:4} : {self.roman}'

    def get_roman(self):
        if self.digit >= 4000 or self.digit <=0:
            raise ValueError('Input moust LT 4000 and GT 0')
        lst = []
        n = self.digit
        for i in (1000,100,10,1):
            q=n//i
            r=n%i
            n=r
            lst.append(self.get_str(q,i))
        return ''.join(lst)
    def get_str(self,q:"0<= q <=9",i:'1,10,100,1000'):
        rst = ''
        if not q:
            # q == 0
            return rst
        unit = self.trans_unit[q]
        for s,u in zip((1,10,5,1),unit):
#        'I(a)X(b)V(c)I(d)'
            rst += self.trans.get(s*i,'') * u
        return rst

if __name__ == '__main__':
    for i in range(1,120):
        print(Arabic2Roman(i))
    while True:
        digit = int(input('Enter an integer :'))
        print(Arabic2Roman(digit))
