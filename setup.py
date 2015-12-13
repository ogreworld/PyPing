#!usr/bin/python
# -*- coding: utf-8 -*-
#
# file_name: setup
# description: 
# author: libo
# Histort:
# 	first created: 2015/11/25

__author__ = 'libo'

import sys
from setuptools import setup, find_packages
from glob import glob

sys.path.insert(0, './lib/')

import PyPing

rc_doc = glob('doc/*')

setup(name          = 'PyPing',
      version       = PyPing.__version__,
      package_dir   = {'' : 'lib'},
      packages      = ['PyPing'],
      description   = 'PyPing',
      include_package_data = True,
      data_files    = [('doc', rc_doc)],
      )