#coding:utf-8

'''
    filename:clsmethod.py
    learn class method
'''



class Message:
    msg = 'Python is a smart language.'

    def get_msg(self):
        print('self :',self)
        print('attrs of class(Message.msg):',Message.msg)
        print('use type(self).msg:',type(self).msg)
        cls = type(self)
        print('[cls = type(self)] cls:',cls)
        print('attrs of class(cls.msg):',cls.msg)


    @classmethod
    def get_cls_msg(cls):
        print('cls :',cls)
        print('attrs of class(cls.msg):',cls.msg)


mess = Message()
mess.get_msg()
print('-'*50)
mess.get_cls_msg()


