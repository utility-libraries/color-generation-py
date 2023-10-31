#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import sys
import setuptools
sys.path.append('./src')
from color_generator import __author__, __version__, __description__, __license__


setuptools.setup(
    name="color-generation",
    version=__version__,
    description=__description__,
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author=__author__,
    license=__license__,
    url="https://github.com/utility-libraries/color-generation-py",
    project_urls={
        "Author Github": "https://github.com/PlayerG9",
        "Organization Github": "https://github.com/utility-libraries",
        "Bug Tracker": "https://github.com/utility-libraries/color-generation-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires=">=3.5",
    include_package_data=True,
)
