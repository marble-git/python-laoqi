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

