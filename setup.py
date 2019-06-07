#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


with open('requirements/base.pip') as f:
    BASE_REQS = f.read().splitlines()

with open('requirements/setup.pip') as f:
    SETUP_REQS = f.read().splitlines()

with open('requirements/test.pip') as f:
    TEST_REQS = f.read().splitlines()

with open('requirements/dev.pip') as f:
    DEV_REQS = f.read().splitlines()

with open('requirements/docs.pip') as f:
    DOCS_REQS = f.read().splitlines()

with open("README.md", "r") as freadme:
    long_description = freadme.read()

setup(
    name='football_simulation',
    author='J. J. Reed',
    url='https://github.com/jr-42/football_simulation',
    use_scm_version=True,
    description='A football simulation',
    long_description=long_description,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={'': ['*.json']},
    include_package_data=True,
    install_requires=BASE_REQS,
    setup_requires=SETUP_REQS,
    extras_require={
        'test': TEST_REQS,
        'develop': TEST_REQS + DEV_REQS,
        'docs':  DOCS_REQS
    },
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ]
)
