#coding:utf-8

'''
    filename:roomhouse.py
        chap:6
    subject:21
    conditions:room:square=length*width,house:total_square=sum(room.square for room in rooms)
    solution:class Room,class House
'''


class Room:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.square = length*width

class House:
    def __init__(self,*rooms):
        self.rooms=rooms
        self.total_square = sum(room.square for room in self.rooms)
    def __eq__(self,other):
        '''对于 __ne__()，
        默认会委托给 __eq__() 并对结果取反，
        除非结果为 NotImplemented
        '''
#        print('in eq ',self,other)
        if  isinstance(other,type(self)):
            if (self.total_square == other.total_square):
                return True
            else:
                return False
        else:
            return NotImplemented
    def __lt__(self,other):
        ''' __lt__() 和 __gt__() 互为对方的反射， 
        __le__() 和 __ge__() 互为对方的反射，
        而 __eq__() 和 __ne__() 则是它们自己的反射
        '''
#        print('in lt ',self,other)
        if  isinstance(other,type(self)):
            if (self.total_square < other.total_square):
                return True
            else:
                return False
        else:
            return NotImplemented
    def __le__(self,other):
        ''' __lt__() 和 __gt__() 互为对方的反射， 
        __le__() 和 __ge__() 互为对方的反射，
        而 __eq__() 和 __ne__() 则是它们自己的反射
        '''
#        print('in le ',self,other)
        if  isinstance(other,type(self)):
            if (self.total_square <= other.total_square):
                return True
            else:
                return False
        else:
            return NotImplemented


if __name__ == '__main__':
    r4 = Room(2,2)
    r8 = Room(2,4)
    r12 = Room(3,4)
    h4 = House(r4)
    h8 = House(r4,r4)
    h12 = House(r4,r8)
    print(h4 == h8)
    print(h4 < h8,h4<=h8)
    print(h4 > h8,h4>=h8)
    print(h4 != h8)
    print(h4 == 4)
    print(h4 != 4)
    print(h4 <= 4)
    print(h4 > 4)
    print(4 == h4)
    print(4 < h4)

