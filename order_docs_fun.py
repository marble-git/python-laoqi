
#coding=utf-8

'''
order /docs/*
'''
import os
import re
from functools import singledispatch


current_chap='chap5'
path_of_this_to_cata_dir='docs/'








def get_fnames(pattern:'re r-string')->'filenames_list':
    '''
    get filenames list
    cwd : in files dir
    '''

    allfiles_lst = list(os.popen('ls -1 '))
    filenames_list = re.findall(pattern,''.join(allfiles_lst))
    filenames_list.sort()
    print('filenames:',filenames_list)
    return filenames_list



def back_up_file(fname,path:'path to file'='./'):
    '''
    back up file
    cwd : default in it's own dir
    '''

    full_fname = path+fname
    os.popen('cp '+full_fname+ ' ' + full_fname+'~')
    print(full_fname,'backed up.')


#def del_links_and_tags(fname):
#    '''
#    del <old '[catalogue]','[pre_chap]','[next_chap]' tags>
#    and <links '[chapx_y]'>
#
#    cwd : in files dir
#    '''
#    result = []
#    with open(fname ,  'rt')  as f:
#        text_lst = f.readlines()
#    del_prefix = ('[cat','[pre','[next','[chap')
#    for i in text_lst:
#        if not i.startswith(del_prefix):
#            result.append(i)
#    rst = ''.join(result)
#    with open(fname , 'wt') as f:
#        f.write(rst)
#    print('del links and tags from:' + fname)
def del_links(fname):
    '''
    del <links '[chapx_y]'>
    cwd : in files dir
    '''
    result = []
    with open(fname ,  'rt')  as f:
        text_lst = f.readlines()
    del_prefix = ('[chap')
    for i in text_lst:
        if not i.startswith(del_prefix):
            result.append(i)
    rst = ''.join(result)
    with open(fname , 'wt') as f:
        f.write(rst)
    print('del links from:' + fname)


def del_tags(fname):
    '''
    del <old '[catalogue]','[pre_chap]','[next_chap]' tags>
    cwd : in files dir
    '''
    result = []
    with open(fname ,  'rt')  as f:
        text_lst = f.readlines()
    del_prefix = ('[cat','[pre','[next')
    for i in text_lst:
        if not i.startswith(del_prefix):
            result.append(i)
    rst = ''.join(result)
    with open(fname , 'wt') as f:
        f.write(rst)
    print('del tags from:' + fname)


def del_links_and_tags(fname):
    '''
    del <old '[catalogue]','[pre_chap]','[next_chap]' tags>
    and <links '[chapx_y]'>

    cwd : in files dir
    '''
    del_links(fname)
    del_tags(fname)




def add_links_to_cata(fcata,fnames,path:'path of sub to cata',cata_to_file:'path of cata to sub',):
    '''
    gen cata file links
    cwd : in file dir
    '''
    rst = []
    fcata = path + fcata
    for fn in fnames:
        if fn[:4].isdigit():
            pre=fn[-8:-3]
        else:
            pre=fn[:7]
        rst.append('['+pre+']: ' + cata_to_file + fn + '\n')
    with open(fcata  , 'at') as f:
        f.write(''.join(rst))
    print('add links to cata:',fcata)



def add_tags_to_files(fcata,fnames,path:'path of sub to cata'):
    '''
    add <new '[catalogue]','[pre_chap]','[next_chap]' tags>
    cwd : in files dir
    '''
    to_cata = path + fcata
    for i,fname in enumerate(fnames):
        pre = to_cata if fname == fnames[0] else fnames[i-1]
        nxt = to_cata if fname == fnames[-1] else fnames[i+1]
        with open( fname , 'at') as f:
            print('[catalogue]: '+ to_cata ,file=f)
            print('[pre_chap]: '+  pre,file=f)
            print('[next_chap]: '+ nxt ,file=f)
        print('add tags to file:',fname)
@singledispatch
def restore_file(fnames):
    print('wrong tyoe!')

@restore_file.register(list)
def _(fnames):
    for fn in fnames:
        bk = fn+'~'
        os.popen('cp -f '+bk+' '+fn)
        print('restore : ',fn)
@restore_file.register(str)
def _(fn):
    bk = fn+'~'
    os.popen('cp -f '+bk+' '+fn)
    print('restore : ',fn)





def main(*,mode,chap,path_this_to_cata,flag=None):
    if mode == 'chap':
        path_cata_to_file = chap+'/'
        path_file_to_cata = '../'
        pattern= r'(chap.*md)\n'
        fcata = '2021-01-21-'+ chap  +'.md'
    elif mode == 'dir':
        path_cata_to_file = './'
        path_file_to_cata = './'
        pattern= r'(2021-01-21-chap.*md)\n'
        fcata = '2021-01-21-catalogue.md'
    else:
        raise ValueError("""<mode> values must be 'chap' or 'dir'.""")

    print('-'*25,'mode:',mode,'chap:',chap,'-'*25)
    print('CWD:',os.getcwd())
    pre_cwd = os.getcwd()
    path_this_to_file = os.path.normpath(path_this_to_cata + path_cata_to_file)
    os.chdir(path_this_to_file)
    print('CWD:',os.getcwd())
    filenames_list = get_fnames(pattern)


    if flag == 'R':
        restore_file(filenames_list)
        restore_file(path_file_to_cata+fcata)
        return

    for fn in filenames_list:
        back_up_file(fn)
        del_tags(fn)
    
    back_up_file(path_file_to_cata+fcata)
    del_links_and_tags(path_file_to_cata+fcata)
    add_links_to_cata(fcata,filenames_list,path_file_to_cata,path_cata_to_file)
    add_tags_to_files(fcata,filenames_list,path_file_to_cata)

    os.chdir(pre_cwd)
    print('-'*60)



if __name__ == '__main__':
    print('starting')

    main(mode='chap',chap=current_chap,path_this_to_cata=path_of_this_to_cata_dir)
    main(mode='dir',chap=current_chap,path_this_to_cata=path_of_this_to_cata_dir,flag='Rs')

    print('done......')




