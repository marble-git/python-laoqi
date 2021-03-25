#coding:utf-8

'''
    filename:average_std_deviation.py
        chap:5
    subject:8
    conditions:names and scores
    solution:fun average std_deviation
'''


import math
import random
import operator


def average(iterable):
    return sum(iterable)/len(iterable)

def std_deviation(iterable):
    aver = average(iterable)
    variance = sum((i-aver)**2 for i in iterable) / len(iterable)
    return math.sqrt(variance)



def get_names_scores():
    names = '''程河闻州鱼茂郜昪简鑫汪丞双叔常辑宓旭糜龄索功汲书廖锋潘瀛卓士厉峰曹珺养旭常飙籍吏黎世周彪双奇燕朗耿钧夏渝史墨赵石江寒终莱钟飞郑兴那信麴天权侃晏峰高彬国林饶实羿轼袁豪广煊寇助蓬旷鄂宪王成蔡诚訾天双帝潘稼聂岩益竹边仓扶邶杜强蓬丕浦安慕石杜键宫时盖乔叶颁耿弢郁俯富光潘丕谷则甘魁易桓彭佳殳含越龄融杰班辑居冕谢封茹镇吴佑融坤瞿时徐涵于铿苏宪沈学钭矢融森顾融禄儋余欧印助詹蔚蓟弼袁颔汪妍袁彭訾轮薛驾郭卓黄善卢矗'''
    name_list = [names[i:i+2] for i in range(0,200,2)]
    score_list = [random.randint(50,100) for i in range(100)]
    return dict(zip(name_list,score_list))



if __name__ == '__main__':

    names_scores = get_names_scores()
    #print(names_scores,len(names_scores))
    names_scores = dict(sorted(names_scores.items(),key=operator.itemgetter(1)))
    print('sorted dict:',names_scores,len(names_scores))


    print('average :',average(names_scores.values()))
    print('standard deviation:',std_deviation(names_scores.values()))
