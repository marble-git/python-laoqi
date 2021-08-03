#coding:utf-8

'''
    filename:create_files.py 
        chap:9
    subject:create a file
    conditions:if file NOT exists,create it;other wise prompt to modify file name
    solution:def create_file
'''


def create_file(filename:'str'):
    '''create file with filename,
        if this file is not exist,
        create it and return file object
        other prompt to modify file name and return None
    '''
    try:
        f = open(filename,'xt')
    except FileExistsError:
        print(filename,'already exists, please modify file name!')
        return None
    return f






if __name__ == '__main__':
    filename = input('Please enter the *FILENAME* you want to create: ')
    f = create_file(filename)
    if f is not None:f.close()

