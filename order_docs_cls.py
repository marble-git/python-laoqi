
#coding=utf-8

'''
order /docs/*
'''
import os
import re
from functools import singledispatchmethod,singledispatch

CHAP = 'chap9'
CATAFILE = '2021-01-21-'+ CHAP  +'.md'
ABSPATHTOCATADIR = '/root/python-laoqi/docs/'
ABSPATHTOARTICLESDIR = '/root/python-laoqi/docs/'+CHAP
ARTICLESPATTERN = r'(chap.*md)\n'
PREFIXSPATTERN = r'chap[0-9]+_[0-9]+'



@singledispatch
#singledispatch[method] 多层嵌套装饰器时必须为最外层的装饰器
def backup(fnames):
    ''' backup files'''
    print('default backup',fnames)
@backup.register(str)
def _(fname):
    print('backup str',fname)
    os.popen('cp '+fname+' '+fname+'~')
@backup.register(list)
def _(fnames):
    print('backup list',fnames)
    for fname in fnames:
        backup(fname)

@singledispatch
def restore(fnames):
    '''restore files'''
    print('default restore',fnames)
@restore.register(str)
def _(fname):
    print('restore str',fname)
    os.popen('cp -f '+fname+'~ '+fname)
@restore.register(list)
def _(fnames):
    print('restore list',fnames)
    for fname in fnames:
        restore(fname)

@singledispatch
def del_links_tags(fnames,mode):
    print('defualt del_links_tags',fnames,mode)
@del_links_tags.register(str)
def _(fname,mode):
    print('del_links_tags str',fname,mode)
    result = []
    links_prefix=('[chap',)
    tags_prefix=('[cat','[pre','[next')
    if mode == 'links':
        del_prefix = links_prefix
    elif mode == 'tags':
        del_prefix = tags_prefix
    elif mode == 'all':
        del_prefix = links_prefix + tags_prefix
    else:
        raise ValueError("<mode> must be 'links' or 'tags' or 'all'.")
    with open(fname,'rt') as f:
        text_lst = f.readlines()
    for line in text_lst:
        if not line.startswith(del_prefix):
            result.append(line)
    with open(fname,'wt') as f:
        f.writelines(result)
    print(f'del mode {mode} from {fname}')
@del_links_tags.register(list)
def _(fnames,mode):
    print('del_links_tags list',fnames,mode)
    for fname in fnames:
        del_links_tags(fname,mode)


class DocFile:
    def __init__(self,fnames:'str or list'):
        self.fnames = fnames
    def backup(self):
        global backup
        backup(self.fnames)
    def restore(self):
        global restore
        restore(self.fnames)
    def del_links_tags(self,mode):
        global del_links_tags
        del_links_tags(self.fnames,mode)




class Article(DocFile):
    '''本类的所有方法执行时，当前目录都为文章所在目录'''
    def __init__(self,pattern,path_to_cata):
        self.pattern = pattern
        self.path_to_cata = path_to_cata
        super().__init__(self.get_articlenames())
        print('articles :',self.fnames)
    def get_articlenames(self):
        allfiles_list = list(os.popen('ls -1'))
        fnames = re.findall(self.pattern,''.join(allfiles_list))
        fnames.sort(key=(lambda fname:int(re.findall(r'chap[0-9]+_([0-9]+)',fname)[0])))
        return fnames
    def add_tags(self,cata:'Catalogue'):
        fnames = self.fnames
        for i,fname in enumerate(fnames):
            to_cata = self.path_to_cata+cata.fnames 
            pre = to_cata if fname == fnames[0] else fnames[i-1]
            nxt = to_cata if fname == fnames[-1] else fnames[i+1]
            with open( fname , 'at') as f:
                f.write('[catalogue]: '+ to_cata +'\n')
                f.write('[pre_chap]: '+  pre + '\n')
                f.write('[next_chap]: '+ nxt + '\n')

        

class Catalogue(DocFile):
    '''本类的所有方法执行时，当前目录都为"目录"所在目录'''
    def __init__(self,fname,path_to_articles,links_pattern):
        self.path_to_articles = path_to_articles
        self.links_pattern = links_pattern
        super().__init__(fname)
    def add_links(self,articles:'Article'):
        prefixs = re.findall(self.links_pattern,''.join(articles.fnames))
        result = []
#        print('prefixs:',prefixs)
#        print('articles.fnames :',articles.fnames)
        for prefix,fname in zip(prefixs,articles.fnames):
            result.append('['+prefix+']: '+ self.path_to_articles+fname+'\n')
        with open(self.fnames,'at') as f:
            f.writelines(result)
        print(f'''added links to cata :{self.fnames} \n{result} \n{'-'*60}''')
        

        
def main():
    os.chdir(ABSPATHTOARTICLESDIR)
    articles = Article(ARTICLESPATTERN,'../')
    articles.backup()
    articles.del_links_tags(mode='tags')

    os.chdir(ABSPATHTOCATADIR)
    cata = Catalogue(CATAFILE,CHAP+'/',PREFIXSPATTERN)
    cata.backup()
    cata.del_links_tags(mode='links')
    cata.add_links(articles)


    
    os.chdir(ABSPATHTOARTICLESDIR)
    articles.add_tags(cata)



if __name__ == '__main__':
    print('starting')
    main()
    print('done......')




