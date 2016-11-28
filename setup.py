__author__ = 'liaopengfei'

# Always prefer setuptools over distutils
from setuptools import setup,find_packages
# To use a consistent encoding

from codecs import open

from os import path

here = path.abspath(path.dirname(__file__))



setup(
    name="BaiDuTrans",
    version='1.0.0',
    description='Baidu location Trans',
    packages=find_packages(),
    install_requires=['httplib2','pymssql','requests','tzlocal']
)
