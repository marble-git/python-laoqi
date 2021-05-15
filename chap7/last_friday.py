#coding:utf-8

'''
    filename:last_friday.py
        chap:7
    subject:3
    conditions:module datetime,calendar
    solution:class LastFriday
'''

from datetime import datetime


class LastFriday:
    def __init__(self,date_string:'yyyy,mm,dd'):
        self.date = datetime.strptime(date_string, '%Y,%m,%d')
        self.lastFriday = self.get_lastFriday()
    def get_lastFriday(self):
        ordinal = self.date.toordinal()
        while True:
            tempday = datetime.fromordinal(ordinal)
            if tempday.isoweekday() == 5:
                return tempday
            ordinal-=1
    def __repr__(self):
        return 'LastFriday:{!r}'.format(self.lastFriday)



if __name__ == '__main__':
    today = LastFriday(datetime.today().strftime('%Y,%m,%d'))
    print(today)
