#coding:utf-8

'''
    filename:paycalculator.py
        chap:6
    subject:10
    conditions:pay_rate,compute_pay
    solution:class PayCalculator
'''

from betweendates import BetDate

class PayCalculator:
    def __init__(self,pay_rate):
        self.pay_rate = pay_rate
    def compute_pay(self,start_str,end_str):
        dates = BetDate(start_str,end_str)
        days = dates.days()
        pay = self.pay_rate * days
        fmt = '{:14}:{}'
        p = fmt.format('Pay Rate',self.pay_rate)
        b = fmt.format('Between Dates',dates)
        d = fmt.format('Days',days)
        pay_t = fmt.format('Pay',pay)
        print( '\n'.join([p,b,d,pay_t]))
        return pay
    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__,self.pay_rate)

if __name__ == '__main__':
    ming = PayCalculator(130)
    print(ming)
    print(ming.compute_pay('2021,4,1','2021,4,26'))

