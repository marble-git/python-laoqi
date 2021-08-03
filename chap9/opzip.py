#coding:utf-8

'''
    filename:opzip.py 
        chap:9
    subject:read and write zip file
    conditions:module zipfile,os.walk
    solution:class OpZip
'''

import zipfile
import os
import random

class OpZip():
    def __init__(self,filename):
        self.filename = filename
        self.zf = zipfile.ZipFile(filename,'a')
    def close(self):
        self.zf.close()
    def testzip(self):
        self.zf.testzip()
    def listdir(self):
        '''list all files in zipfile'''
        self.zf.printdir()
    def append(self,filename,arcname=None):
        '''append file or dir to zipfile.'''

        if not os.path.isdir(filename):
            '''if filename is normal file
            just append it to zipfile'''
            self.zf.write(filename,arcname=None)
        else:
            '''if filename is dir
            append subdirs and subfile to zipfile'''
            pathpre = filename if arcname is None else arcname
            for dirpath,dirnames,files in os.walk(filename):
                '''append subdirs and subfile to zipfile'''
                for dirname in dirnames:
                    '''append subdirs to zipfile'''
                    srcpath = os.path.join(dirpath,dirname)
                    destpath = os.path.join(dirpath.replace(filename,pathpre),dirname)
                    self.zf.write(srcpath,destpath)
                for file in files:
                    '''append subfiles to zipfile'''
                    srcpath = os.path.join(dirpath,file)
                    destpath = os.path.join(dirpath.replace(filename,pathpre),file)
                    self.zf.write(srcpath,destpath)


    def remove(self,filename):
        '''remove 'filename[/*]' from zipfile.'''
        namelist = self.zf.namelist()

        '''remove filename[/*] from namelist'''
        if filename in namelist:
            '''if filename is file'''
            namelist.remove(filename)
        else:
            '''if filename is dir,remove everything under this dir.'''
            for file in namelist[::]:
                if file.startswith(filename+os.sep):
                    namelist.remove(file)
        '''copy remained files to a temp zipfile.'''
        tempname = self._tempname()
        tempnamezf = zipfile.ZipFile(tempname,'w')
        for name in namelist:
            zipinfo = self.zf.getinfo(name)
            data = self.zf.read(zipinfo.filename)
            tempnamezf.writestr(zipinfo,data)
        self.zf.close()
        tempnamezf.close()
        '''delete origin zipfile, 
        and rename the tempzipfile to origin zipfile's name,
        init this instance again.'''
        os.remove(self.filename)
        os.rename(tempname,self.filename)
        self.__init__(self.filename)
    @staticmethod
    def _tempname():
        '''return an unique tempname.'''
        while True:
            tempname = str(random.random())[2::]
            if tempname not in os.listdir():
                return tempname

    def extract(self,filename,path=None):
        self.zf.extract(filename,path)
    def extractall(self,path=None,files=None):
        self.zf.extractall(path,files)






if __name__ == '__main__':
    zf = OpZip('test.zip')
    print('zf.testzip() : ',zf.testzip())

    print('start files in zf :')
    zf.listdir()

    zf.append('../docs','ddd')
    print('after append new files :')
    zf.listdir()

    zf.remove('ddd')
    print('after remove: ')
    zf.listdir()
