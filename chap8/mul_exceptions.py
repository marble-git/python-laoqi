#coding:utf-8

'''
    filename:mul_exceptions.py
    handling multiple exceptions.
'''

while True:
    try:
        a = float(input('First number : '))
        b = float(input('Second number : '))
        r = a/b
        print('{} / {} = {}'.format(a,b,r))
        break
#    except ZeroDivisionError:
#        print('The second number cannot be zero. Try again')
#    except ValueError:
#        print('Please enter number.Try again')
    except (ValueError,ZeroDivisionError) as e:
        print(e)
        print('Try again')
    except :
        break





