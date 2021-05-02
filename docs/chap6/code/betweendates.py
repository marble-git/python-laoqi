#coding:utf-8

'''
    filename:betweendates.py
    calculate days,weeks between two dates.
'''

import datetime
from dateutil import rrule


class BetDate:
    def __init__(self,start_date,end_date):
        fmt = '%Y,%m,%d'
        self.start = datetime.datetime.strptime(start_date,fmt)
        self.stop = datetime.datetime.strptime(end_date,fmt)

    def days(self):
        d = self.stop - self.start
        return d.days if d.days > 0 else False

    def weeks(self):
        w = rrule.rrule(rrule.WEEKLY,dtstart=self.start,until=self.stop)
        return w.count()

dates = BetDate('2015,5,1','2015,5,25')
days = dates.days()
weeks = dates.weeks()

print('Between ',dates)
print('Days :',days)
print('Weeks :',weeks)

