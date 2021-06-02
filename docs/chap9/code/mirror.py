#coding:utf-8

'''
    filename:mirror.py
    <fluent python,p372>
    with,contextmanager
'''


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



