#coding:utf-8

'''
    filename:betweendates.py
        chap:6
    subject:3
    conditions:在6.2.2基础上继续编写，计算2个日期间的月份数量(不足1个月按1个月计算)
    solution:class BetDates
'''


import datetime
from dateutil import rrule

class BetDate:
    def __init__(self,start_date,end_date):
        fmt = '%Y,%m,%d'
        self._start_str =start_date 
        self._end_str =end_date 
        self.start = datetime.datetime.strptime(start_date,fmt)
        self.stop = datetime.datetime.strptime(end_date,fmt)
    def __repr__(self):
        return '{}({!r},{!r})'.format(self.__class__.__name__,self._start_str,self._end_str)

    def days(self):
        d = self.stop - self.start
        return d.days if d.days > 0 else False

    def weeks(self):
        w = rrule.rrule(rrule.WEEKLY,dtstart=self.start,until=self.stop)
        return w.count()

    def months(self):
        m = rrule.rrule(rrule.MONTHLY,dtstart=self.start,until=self.stop)
        return m.count()
if __name__ == '__main__':
    dates = BetDate('2015,5,1','2015,5,25')
    days = dates.days()
    weeks = dates.weeks()
    print(dates)
    print('Between ',dates)
    print('Days :',days)
    print('Weeks :',weeks)
    print('Months',dates.months())

