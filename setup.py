#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import sys
import setuptools
sys.path.append('./src')
from color_generator import __author__, __version__


setuptools.setup(
    name="color-generator",
    version=__version__,
    author=__author__,
    # author_email="author@example.com",
    description="generate random good-looking colors",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PlayerG9/py-color-generator",
    project_urls={
        "Author Github": "https://github.com/PlayerG9",
        "Bug Tracker": "https://github.com/PlayerG9/py-color-generator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5",
)
