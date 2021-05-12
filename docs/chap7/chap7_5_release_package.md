## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------


## 7.5 发布包

+ 让别人使用自己编写的程序
+ 放到github.com上是一种方式
+ 在python生态环境中，还可以放到pypi.org上，让它成为每个开发者可以通过pip安装的第三方包


+ 发布包流程
+ 第一步，创建一个包

```root@kali-book:~/python-laoqi/chap7/test_project_release# tree -F
.
├── __init__.py
├── javaspeak/
│   ├── __init__.py
│   └── javaspeak.py
├── langspeak.py
├── pythonspeak/
│   ├── __init__.py
│   └── pythonspeak.py
├── rustspeak/
│   ├── __init__.py
│   └── rustspeak.py
└── setup.py
3 directories, 9 files
```


+ 第二步，编写 `setup.py`

```
#coding=utf-8
'''
    filename:setup.py
    setup config for the package.
'''
import os
from setuptools import setup,find_packages
setup(
        name='test_pkg_marble',
        version='0.0.1',
        author='marble_z',
        author_email='516018505@qq.com',
        description='this is a test package. test_pkg',
        url='',
        py_modules=['langspeak'],
        packages=find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            ],
        ) 
```

+ [setuptools keywords](https://setuptools.readthedocs.io/en/latest/references/keywords.html)
+ name:`str`将来发布到Pypi上时显示的名称(不一定与import或本包的顶级目录名称相同)
+ py_modules:`list`本包中与setup.py同级的`.py`模块
+ packages:`list`用于声明本包中的子包
```
name
    A string specifying the name of the package.
version
    A string specifying the version number of the package.
description
    A string describing the package in a single line.
long_description
    A string providing a longer description of the package.
long_description_content_type
    A string specifying the content type is used for the long_description (e.g. text/markdown)
author
    A string specifying the author of the package.
author_email
    A string specifying the email address of the package author.
url
    A string specifying the URL for the package homepage.
packages
    A list of strings specifying the packages that setuptools will manipulate.
py_modules
    A list of strings specifying the modules that setuptools will manipulate.
classifiers
    A list of strings describing the categories for the package.
```


+ 第三步，本地安装测试
```
python3 setup.py install
python3
....
```

+ 第四步，安装，升级 `setuptools,wheel,twine`
```
pip install -U setuptools wheel twine
```
+ 文件打包,创建分发包，源码包，二进制包
```
python3 setup.py sdist bdist
├── dist
│   ├── test_pkg_marble-0.0.1-py3-none-any.whl
│   └── test_pkg_marble-0.0.1.tar.gz
root@kali-book:~/python-laoqi/chap7/test_project_release# tree
.
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       ├── javaspeak
│       │   ├── __init__.py
│       │   └── javaspeak.py
│       ├── langspeak.py
│       ├── pythonspeak
│       │   ├── __init__.py
│       │   └── pythonspeak.py
│       └── rustspeak
│           ├── __init__.py
│           └── rustspeak.py
├── dist
│   ├── test_pkg_marble-0.0.1-py3-none-any.whl
│   └── test_pkg_marble-0.0.1.tar.gz
├── __init__.py
├── javaspeak
│   ├── __init__.py
│   └── javaspeak.py
├── langspeak.py
├── LICENSE
├── pythonspeak
│   ├── __init__.py
│   └── pythonspeak.py
├── README.md
├── rustspeak
│   ├── __init__.py
│   └── rustspeak.py
├── setup.py
└── test_pkg_marble.egg-info
    ├── dependency_links.txt
    ├── PKG-INFO
    ├── SOURCES.txt
    └── top_level.txt
```
+ 第五步，发布包
```
root@kali-book:~/python-laoqi/chap7/test_project_release# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: marble-pypi
Enter your password: 
Uploading test_pkg_marble-0.0.1-py3-none-any.whl
100%|█████████████████████████████████████████████████████████████████████████████████████████████| 5.86k/5.86k [00:07<00:00, 803B/s]
Uploading test_pkg_marble-0.0.1.tar.gz
100%|███████████████████████████████████████████████████████████████████████████████████████████| 4.54k/4.54k [00:01<00:00, 3.74kB/s]
View at:
https://test.pypi.org/project/test-pkg-marble/0.0.1/
```



+ 下载，安装，测试
```
root@kali-book:~# pip install -i https://test.pypi.org/simple/ test-pkg-marble==0.0.1
Looking in indexes: https://test.pypi.org/simple/
Collecting test-pkg-marble==0.0.1
  Downloading https://test-files.pythonhosted.org/packages/69/63/ebae2eee89b16a81291ed40c0dab6b2b775600366166fb4cbb1ca3196108/test_pkg_marble-0.0.1-py3-none-any.whl (2.9 kB)
Installing collected packages: test-pkg-marble
Successfully installed test-pkg-marble-0.0.1
WARNING: Running pip as root will break packages and permissions. You should install packages reliably by using venv: https://pip.pypa.io/warnings/venv                                         
root@kali-book:~# pip show test-pkg-marble
Name: test-pkg-marble
Version: 0.0.1
Summary: this is a test package. test_pkg
Home-page: UNKNOWN
Author: marble_z
Author-email: 516018505@qq.com
License: UNKNOWN
Location: /usr/local/lib/python3.9/dist-packages
Requires: 
Required-by: 
```






-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[pre_chap]: 2021-01-21-chap0.md
[next_chap]: 2021-01-21-chap2.md
[catalogue]: 2021-01-21-catalogue.md
