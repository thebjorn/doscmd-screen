#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup


setup(
    name='dosbox-screen',
    version='0.0.1',
    requires=['ctypes', 'colorama'],
    description='The Screen class lets you position the cursor in the dosbox.',
    author=u'Bjørn Pettersen',
    author_email='bjorn@tkbe.org',
    url='https://github.com/thebjorn/doscmd-screen',
    py_modules=['screen']
)
