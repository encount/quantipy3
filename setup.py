#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

versions = dict(numpy='1.20.2',
                scipy='1.6.3',
                pandas='1.2.4',
                ftfy='6.0.1')

precisions = dict(numpy='>=',
                  scipy='>=',
                  pandas='>=',
                  ftfy='>=')

libs = ['numpy',
        'scipy',
        'pandas',
        'ftfy',
        'xmltodict',
        'lxml',
        'xlsxwriter',
        # 'pillow',
        'prettytable',
        'decorator',
        'watchdog',
        'requests',
        'python-pptx']

def version_libs(libs, precisions, versions):
    return [lib + precisions[lib] + versions[lib]
            if lib in versions.keys() else lib
            for lib in libs]

if sys.platform == 'win32':
    INSTALL_REQUIRES = version_libs(libs[2:], precisions, versions)
else:
    INSTALL_REQUIRES = version_libs(libs, precisions, versions)

setup(name='quantipy3',
      version='0.2.5',
      author='Geir Freysson',
      author_email='geir@datasmoothie.com',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      install_requires=INSTALL_REQUIRES,
      )
