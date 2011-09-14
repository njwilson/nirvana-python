#!/usr/bin/env python

import nirvana

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='nirvana',
    version=nirvana.__version__,
    description=('Library for interacting with the Nirvana task manager '
                 '(nirvanahq.com)'),
    long_description=long_description,
    author='Nick Wilson',
    author_email='nick@njwilson.net',
    url='http://nirvana-python.readthedocs.org',
    license='MIT',
    packages=['nirvana'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
