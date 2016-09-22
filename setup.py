#!/usr/bin/env python
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='scrap-groceries',
    version='0.1',
    description="A web scrap tool to extract groceries from Sainsbury's",
    long_description=read('README.md'),
    author='Guillem Barba',
    author_email='guillem@alcarrer.net',
    url='https://github.com/gbarba/sainsbury_technical_test',
    # download_url='',
    # keywords='',
    # classifiers=[],
    # license='',
    install_requires=[
        'cssselect >=0.9.2',
        'lxml >=3.6.4',
        'requests >=2.11.1',
        'simplejson >=3.8.2',
    ],
    entry_points='''
        [console_scripts]
        scrap-groceries=scrap_groceries:main
        ''',
    test_suite='tests.test_scrap_groceries',
    dependency_links=[],
)
