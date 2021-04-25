#coding:utf-8

'''
    filename:singleton_metaclass.py
    singleton using metaclass
'''


class Singleton(type):
    instance = {}
    def __call__(inscls,*args,**kwargs):
        if inscls not in inscls.instance:
            inscls.instance[inscls] = type.__call__(inscls,*args,**kwargs)
        return inscls.instance[inscls]

class Spam(metaclass = Singleton):pass

x = Spam()
y = Spam()
print(x)
print(x is y)

print(Singleton.__dict__)
print(Spam.__dict__)
print(x.__dict__)

