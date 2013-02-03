#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""dosbox-screen: The Screen class allows you to do positioned writes to
   the dos terminal (dosbox). It also allows you to specify the colors
   for foreground and background, to the extent the dosbox allows.
"""

classifiers = """\
Development Status :: 3 - Alpha
Environment :: Win32 (MS Windows)
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Operating System :: Microsoft :: MS-DOS
Programming Language :: Python
Topic :: Software Development :: Libraries
Topic :: System :: Shells
Topic :: Terminals
"""

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
