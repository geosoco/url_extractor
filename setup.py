#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import url_extractor

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def read_lines(filename):
    return open(filename, "r").readlines()


#long_description = read('README.txt', 'CHANGES.txt')
long_description = "<<TODO: Write Long Description!>>"


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='url_extractor',
    version=url_extractor.__version__,
    url='http://github.com/geosoco/url_extractor/',
    license='MIT License',
    author='John Robinson',
    tests_require=['pytest'],
    install_requires=read_lines("requirements/base.txt"),
    cmdclass={'test': PyTest},
    author_email='soco@uw.edu',
    description='URL analysis API and toolset',
    long_description=long_description,
    packages=['url_extractor'],
    include_package_data=True,
    platforms='any',
    test_suite='test.test_url_extractor',
    classifiers=[
        ],
    extras_require={
        'testing': ["pytest", "tox"],
    }
)
