## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
-----------------------------------------------------------------------------------

## 7.4 第3方包


+ 标准库提供的模块已经非常多了，但在实际问题面前仍然不足，所以还要造更多的工具
+ 于是有了海量的 ***第三方包(Python packages)*** :不是标准库里面的模块，也不是自己开发的，是别人开发并分享出来的，供任何人使用
+ 这些第三方包通常被放到[pypi.org网站上](https://pypi.org)
+ 要使用第三方包，就要先将它安装到本地，推荐使用 `pip`
+ 安装pip:

```
#1 从linux 包管理安装
root@kali-book:~# apt-get install python3-pip
root@kali-book:~# pip3 --version
pip 21.1.1 from /usr/local/lib/python3.9/dist-packages/pip (python 3.9)
#2 下载安装脚本安装
root@kali-book:~# curl  https://bootstrap.pypa.io/get-pip.py -o get-pip.py
root@kali-book:~# python3 get-pip.py 
#3 源码安装
wget https://github.com/pypa/pip/archive/refs/tags/21.1.1.tar.gz
tar -xzvf 21.1.1.tar.gz 
cd pip-21.1.1/
python3 setup.py install
```
+ [配置pip,更换清华源](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

```
root@kali-book:~# cat .config/pip/pip.conf 
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
root@kali-book:~# pip config edit --editor vim
pip国内镜像地址
阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban) http://pypi.douban.com/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
————————————————
临时使用
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
注意，simple 不能少, 是 https 而不是 http
设为默认
升级 pip 到最新的版本 (>=10.0.0) 后进行配置：
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

+ 使用pip安装第三方包

```
root@kali-book:~# pip install requests
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Requirement already satisfied: requests in /usr/local/lib/python3.9/dist-packages (2.25.1)
Requirement already satisfied: chardet<5,>=3.0.2 in /usr/lib/python3/dist-packages (from requests) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests) (2020.6.20)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/lib/python3/dist-packages (from requests) (1.25.8)
Requirement already satisfied: idna<3,>=2.5 in /usr/lib/python3/dist-packages (from requests) (2.9)
WARNING: Running pip as root will break packages and permissions. You should install packages reliably by using venv: https://pip.pypa.io/warnings/venv   
>>> import requests
>>> r = requests.get("https://github.com")
>>> type(r)
<class 'requests.models.Response'>
>>> r
<Response [200]>
>>> r.
r.apparent_encoding      r.encoding               r.iter_lines(            r.raw
r.close(                 r.headers                r.json(                  r.reason
r.connection             r.history                r.links                  r.request
r.content                r.is_permanent_redirect  r.next                   r.status_code
r.cookies                r.is_redirect            r.ok                     r.text
r.elapsed                r.iter_content(          r.raise_for_status(      r.url
>>> dir(r)
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
>>> r.status_code
200
>>> r.headers['content-type']
'text/html; charset=utf-8'
>>> r.encoding
'utf-8'
>>> r.text[:100]
'\n\n\n\n\n<!DOCTYPE html>\n<html lang="en"  class="html-fluid">\n  <head>\n    <meta charset="utf-8">\n  <lin'
```

+ 源码安装第三方包

```
git clone git@github.com:USER/project.git
#git clone https://github.com/USER/project.git
##wget url-to-project.tar.gz
##tar -xzvf project.tar.gz
cd project
python3 setup.py install
```







-----------------------------------------------------------------------------------
## [返回目录][catalogue]or[上一章][pre_chap]or[下一章][next_chap]
[catalogue]: ../2021-01-21-chap7.md
[pre_chap]: chap7_3_standard_library.md
[next_chap]: chap7_5_release_package.md
