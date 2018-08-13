"""
# ==============================================================================
# Name:             setup.py
#                   -
# Purpose:          -
#                   -
#                   -
# Author:           Jef Neefs
# Created:          13/08/2018
# Copyright:        (c) Jef Neefs 2018
# Licence:          GPLv3
# ==============================================================================
# Extra used pypi modules which may need to be installed:
#
# ==============================================================================
"""
# !/usr/bin/env python

from distutils.core import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(name='pyBus',
      version='0.0.01',
      description='Python Distribution Utilities',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='studioj',
      author_email='neefsj@mail.com',
      url='https://github.com/studioj/pyBus',
      packages=['serial', 'mpd'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      )
