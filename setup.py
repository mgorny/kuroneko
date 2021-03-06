#!/usr/bin/env python
# (c) 2021 Michał Górny
# 2-clause BSD license

from setuptools import setup

import kuroneko


setup(
    name='kuroneko',
    version=kuroneko.__version__,
    description=kuroneko.__doc__,

    author='Michał Górny',
    author_email='mgorny@gentoo.org',
    license='BSD',
    url='http://github.com/mgorny/kuroneko',

    packages=['kuroneko'],
    entry_points={
        'console_scripts': [
            'kuroneko=kuroneko.__main__:main',
        ],
    },

    install_requires=[
        'colorama',
        'pkgcore',
        'requests',
    ],
    extras_require={
        'scraper': [
            'bracex',
        ],
        'test': [
            'bracex',
            'pytest',
            'responses',
        ],
    },
)
