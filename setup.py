#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import subastas_repo
version = subastas_repo.__version__

setup(
    name='subastas',
    version=version,
    author='',
    author_email='diegoduncan21@gmail.com',
    packages=[
        'subastas_repo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['subastas_repo/manage.py'],
)
