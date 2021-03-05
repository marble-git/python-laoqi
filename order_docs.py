
#coding=utf-8

'''
order /docs/*
'''
import os
import re

target_dir = 'docs/chap4/'
cata = '../2021-01-21-chap4.md'

lst = list(os.popen('ls -1 ' + target_dir ))
file_names  = re.findall(r'(chap.*md)\n',''.join(lst))

file_names.sort()


def add_links_to_cata(fcata,fnames):
    '''
    gen cata file links
    '''
    rst = []
    for i in fnames:
        rst.append('['+ i[:7] + ']: ' + i[:5] + '/' + i + '\n')

    with open( fcata  , 'at') as f:
        f.write(''.join(rst))



def del_tags(file_name):
    '''
    del old catalogue,pre,next tags
    '''
    result = []
    with open(file_name ,  'rt')  as f:
        text_lst = f.readlines()

    del_fix = ('[cat','[pre','[next')
    for i in text_lst:
        if not i.startswith(del_fix):
            result.append(i)

    #print(result)
    os.popen('cp ' + file_name + ' '  + file_name + '~'  )
    rst = ''.join(result)
    print('\ndel fix from.....' + file_name)
    with open(file_name , 'wt') as f:
        f.write(rst)



#del_tags(target_dir + 'chap3_2_number.md')

print('starting')

add_links_to_cata(target_dir + cata,file_names)

for i in range(len(file_names)):
    pre = cata if i == 0 else file_names[i-1]
    nxt = cata if i == (len(file_names)-1) else file_names[i+1]
    fname = target_dir + file_names[i]
    del_tags( fname)
    with open( fname , 'at') as f:
        print('[catalogue]: '+ cata ,file=f)
        print('[pre_chap]: '+  pre,file=f)
        print('[next_chap]: '+ nxt ,file=f)
    print( '\n' + fname + '.....done')

        
        
