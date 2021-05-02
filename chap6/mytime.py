#coding:utf-8

'''
    filename:mytime.py
        chap:6
    subject:14
    conditions:instance_method [showtime:(time_fmt='hh:mm:ss'),
                time_difference:arg_time-instance_time]
    solution:class MyTime
'''

import time


class MyTime:
    in_fmt = '%H,%M,%S'
    show_fmt = '%H:%M:%S'
    def __init__(self,timestr:"%H,%M,%S"):
        self.t = time.strptime(timestr,self.in_fmt)
    def showtime(self):
        print(time.strftime(self.show_fmt,self.t))
    def timedifference(self,timestr):
        arg_time = time.strptime(timestr,self.in_fmt)
        t_diff_seconds = time.mktime(arg_time) - time.mktime(self.t)
        sign = "+"
        if t_diff_seconds < 0:
            sign = "-"
        t_diff_seconds = abs(t_diff_seconds)
        t_diff = time.gmtime(t_diff_seconds)
        print(sign+time.strftime(self.show_fmt,t_diff))



if __name__ == '__main__':
    a=MyTime('13,14,55')
    a.showtime()
    a.timedifference('15,40,57')



