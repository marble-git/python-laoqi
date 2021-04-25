#coding:utf-8

'''
    filename:classifynum.py
    classify number set.
'''


class OddEven:
    def __init__(self,numbers):
        self.odds = [x for x in numbers if self.is_odd(x)]
        self.evens = [x for x in numbers if x not in self.odds]
    @staticmethod
    def is_odd(x):
        if x%2:
            return True
        else:
            return False


n = list(range(11))

print('numbers:',n)
r = OddEven(n)
print('odds:',r.odds)
print('evens:',r.evens)

        



