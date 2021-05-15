#coding:utf-8

'''
    filename:deque.py
        chap:7
    subject:1
    conditions:collections.deque, 
            自定义固定尺寸的缓存对象，
            达到最大长度时，最老的元素被删除
    solution:container = deque(maxlen=5)
'''


from collections import deque

container = deque(maxlen=5)



if __name__ == '__main__':
    for i in range(7):
        container.append(i)
        print(container)
