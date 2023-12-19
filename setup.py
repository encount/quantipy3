#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

versions = dict(numpy='1.26.0',
                scipy='1.11.3',
                pandas='2.1.3',
                ftfy='6.1.1',
                pyreadstat='1.2.4')

precisions = dict(numpy='==',
                  scipy='==',
                  pandas='==',
                  ftfy='==',
                  pyreadstat='==')

libs = ['numpy',
        'scipy',
        'pandas',
        'ftfy',
        'xmltodict',
        'lxml',
        'xlsxwriter',
        'prettytable',
        'decorator',
        'watchdog',
        'requests',
        'python-pptx',
        'pyreadstat',
        'deprecated']

def version_libs(libs, precisions, versions):
    return [lib + precisions[lib] + versions[lib]
            if lib in versions.keys() else lib
            for lib in libs]

if sys.platform == 'win32':
    INSTALL_REQUIRES = version_libs(libs[2:], precisions, versions)
else:
    INSTALL_REQUIRES = version_libs(libs, precisions, versions)

setup(name='quantipy3',
      version='0.3.0',
      author='Geir Freysson',
      author_email='geir@datasmoothie.com',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      install_requires=INSTALL_REQUIRES,
      )
