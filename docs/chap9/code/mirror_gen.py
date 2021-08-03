#coding:utf-8

'''
    filename:mirror_gen.py
    <fluent python,p376>
    with,contextmanager
'''

from contextlib import contextmanager


@contextmanager
def looking_glass():
    print('Enter gen')
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ""
    try:
        yield 'ContextManager_gen'
    except ZeroDivisionError:
        msg = "Do Not divide by zero"
    except :
        raise 
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)
        print('Leaving gen')



class LookingGlass:
    def __enter__(self):
        print('Enter')
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'ABCD1234'
    def reverse_write(self,text):
        self.original_write(text[::-1])
    def __exit__(self,exc_type,exc_value,traceback):
        print('Exit')
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('please DO NOT divide by zero')
            return True



