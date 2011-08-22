#!/usr/bin/env python

from distutils.core import setup
setup (
        name = 'constraints',
        packages = ['constraints'],
        version = '0.9.2',
        description = 'Returns a constrained subset of the members of a dict of dicts',
        author = 'James Polley',
        author_email = 'jamezpolley@gmail.com',
        url = 'https://github.com/jamezpolley/constraints',
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        requires = [
            'PyYAML',
            'unittest2'
        ],

)
