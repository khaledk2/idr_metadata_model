#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

sys.path.append(".")

def read(fname):
    """
    Utility function to read the README file.
    :rtype : String
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()



setup(
    name="idr-metadata-model",
    version="0.1",
    description="metadata_model.IDR",
    long_description=read("README.md"),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],  # Get strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    author="The Open Microscopy Team",
    author_email="ome-devel@lists.openmicroscopy.org.uk",
    url="https://github.com/khaledk2/idr_metadata_model",
    packages=find_packages(exclude=("test",)),
    python_requires=">=3.9",
    install_requires=[
    "linkml==1.8.1",
    "linkml-runtime==1.8.0"
    ],
    include_package_data=True,
    license = "Apache-2.0",

)

# python setup.py bdist_wheel

