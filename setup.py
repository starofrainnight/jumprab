#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import io
from setuptools import setup, find_packages

with io.open("README.rst", encoding="utf-8") as readme_file, io.open(
    "HISTORY.rst", encoding="utf-8"
) as history_file:
    long_description = readme_file.read() + "\n\n" + history_file.read()

install_requires = [
    "click>=6.0",
    "simplejson",
]

setup_requires = [
    "pytest-runner",
    # TODO(starofrainnight): put setup requirements (distutils extensions, etc.) here
]

tests_requires = [
    "pytest",
    # TODO: put package test requirements here
]

setup(
    name="jumprab",
    version="0.0.1",
    description="A program to set mirror or proxy for development in some restricted network environment",
    long_description=long_description,
    author="Hong-She Liang",
    author_email="sorn@taorules.com",
    url="https://github.com/starofrainnight/jumprab",
    packages=find_packages(),
    entry_points={"console_scripts": ["jumprab=jumprab.__main__:main"]},
    include_package_data=True,
    install_requires=install_requires,
    license="Apache Software License",
    zip_safe=False,
    keywords="jumprab",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    tests_require=tests_requires,
    setup_requires=setup_requires,
)
