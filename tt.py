#coding:utf-8

'''
    filename:
        chap:
    subject:
    conditions:
    solution:
'''

import time
import functools


def get_attrs(f:'function name'):
    print('*'*25,f.__name__,'*'*25)
    attrs=dir(f)
    for item in attrs:
        f_attr=f.__name__+'.'+item
        print(f_attr,' : ',eval(f_attr))
    print('-'*60)



def get_code_attrs(f:'func name'):
    print('*'*25,f.__name__,'*'*25)
    attrs = dir(f.__code__)
    for item in attrs:
        if item.startswith('co_'):
            f_code_attr = f.__name__ + '.__code__.' + item
            print(f_code_attr,':',eval(f_code_attr))
    print('-'*60)
        



def bar(ba=11,bb=12,*arg,ko='kw-only',**kws):
    l = []
    bar.ll = [1,2,3]
    ll = [1,2,3]
    ss = 'abc'

    def foo(x=22,fa=23,*args:'args......',**kwsargs):
        l.append(x)
        ll.append(x)
        print('foo locals():',locals())
        #print(l)
        #get_attrs(foo)
        #get_code_attrs(foo)
    print('bar locals():',locals())
    #get_attrs(bar)
    #get_code_attrs(bar)
    print(foo.__closure__[1].cell_contents)
    return foo

#foo = bar(111,222,333,4444,aaa=1111,bbbb=1222222)
#foo(999,998,997,996,f1=11,f2=22,f3=33)


#print(dir(bar))

#print(globals())

#def foo():
#    global gga
#    gga = 'global var'
#    nl = 11
#    print(globals())
#    def bar():
#        nonlocal gga
#        gga ='nonl var'
#        print(gga)
#    bar()

#foo()



def dec(f):
    print('>'*10,'in dec')
    def inner(*a,**k):
        print('>'*10,'in inner f_name: ',f.__name__)
        return f(*a,**k)
    return inner



def timer(func):
    print('timer start ',timer.__name__,func.__name__)
    #@functools.wraps(func)
    @dec
    def wrapper(*arg,**kwargs):
        start = time.time()
        print('wrapper start ',wrapper.__name__)
        rst = func(*arg,**kwargs)
        stop = time.time()
        print('wrapper stop ',wrapper.__name__)
        print(func.__name__,' cost time: ',stop-start)
        print('-'*60)
        return rst,stop-start
   # functools.update_wrapper(wrapper,func)
    print('timer stop ',timer.__name__,func.__name__)
    print('-'*60)
    return wrapper


#@timer
def test_list_append(count,/):
    lst = []
    for i in range(count):
        lst.append(count)
    return lst

#@timer
def test_list_compre(count,/):
    return [i for i in range(count)]

count = 10000000
#_,t1 = test_list_append(count)
#_,t2 = test_list_compre(count)
#print(t1/t2)
#print('func name :',test_list_append.__name__,test_list_compre.__name__)
#ta = timer(test_list_append)
#print('ta :',ta.__name__)
#print('func name :',test_list_append.__name__,test_list_compre.__name__)





def log(log_level='INFO',/):
    def outer(func):
        @functools.wraps(func)
        def wrapper(*arg,**kwargs):
            print(log_level,':',func.__name__,'is running.')
            return func(*arg,**kwargs)
        return wrapper
    return outer

@log('WARRING')
def foo():pass
foo()

@log()
def bar():pass
bar()
print(foo.__name__,bar.__name__)



def dec1(f):
    print('exec dec1')
    def inner1(*a,**k):
        print('exec inner1')
        rst = f(*a,**k)
        print('ending inner1')
        return rst
    print('ending dec1')
    return inner1



def dec2(f):
    print('exec dec2')
    def inner2(*a,**k):
        print('exec inner2')
        rst = f(*a,**k)
        print('ending inner2')
        return rst
    print('ending dec2')
    return inner2


@dec1
@dec2
def foo():
    print('exec foo')

print('-'*20,'start foo','-'*20)
foo()






def dec(func):
    #@functools.wraps(func)
    @dec1
    def indec(*a,**k):
        rst = func(*a,**k)
        return rst
    print('indec name:',indec.__name__)
    return indec

@dec
def foo():pass

print('-'*20,'start foo','-'*20)
foo()



def mp(f,*its):
    min_len = min(len(it) for it in its)
    for i in range(min_len):
        args = []
        for it in its:
            args.append(it[i])
        yield f(*args)

print(a:=mp(lambda *a:''.join(a),'abcde','1234567'))
print(list(a))



def ft(f,it):
    if f==None:
        for i in it:
            if i:yield i
    else:
        for i in it:
            if f(i):
                yield i

lst = [[], 1, {}, 2, None, 3, '', 4, ' ', 5, (), 6]
print(a:=ft(lambda x:x%2,range(-5,6)))
print(list(a))

while True:
    s= input('eval string cmd :')
    if s == 'exit':break
    print(eval(s))










