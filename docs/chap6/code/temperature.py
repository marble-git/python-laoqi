#coding:utf-8

'''
    filename:temperature.py
    The type of temperature.
'''

class Temperature:
    #[C or F] to K 
    coefficient = {'c':(1,-273.15),'f':(1.8,-459.67)}
    def __init__(self,**kwargs):
        v = set(kwargs.keys()).intersection('cfkCFK')
        print(v)
        # 'cfkCFK' to set('cfkCFK')
        assert set(kwargs.keys()).intersection('cfkCFK'),f"Invalid arguments {kwargs}"
        name,value = kwargs.popitem()
        name = name.lower()
        #set self.k = value_to_k
        setattr(self,name, float(value))
    def __getattr__(self,name):
        try:
            eq = self.coefficient[name.lower()]
        except KeyError:
            raise AttributeError(name)
        return self.k*eq[0] + eq[1]
    def __setattr__(self,name,value):
        name = name.lower()
        if name in self.coefficient:
            eq = self.coefficient[name]
            self.k = (value - eq[1])/eq[0]
        elif name == 'k':
            #self.k = value  递归
            object.__setattr__(self,name,value)
        else:
            raise AttributeError(name)
    def __str__(self):
        return '{} K'.format(self.k)
    def __repr__(self):
        return '{}(K = {})'.format(type(self).__name__,self.k)


t= Temperature(c=64)
print('c = 64, f = ',t.f)
print(t)
print(repr(t))
t.f = 23
print('f = 23,c = ',t.c)
t.k=0
print(t.c)


