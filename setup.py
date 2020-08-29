#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from setuptools import setup
import io
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="crunchapilyb",
    version = "1.0.0",
    author="Yibang (Christopher) Liu",
    author_email="yibang.christopher.liu@gmail.com",
    description="A Crunch API by Christopher",
    license='Apache',
    long_description=long_description,
    url='https://github.com/ChristopherLiu618/CrunchAPI',
    packages=['crunchapilyb'],
    install_requires=['pandas', 'requests'],
    platforms=['any'],
    keywords='pandas, Crunch, API'
)