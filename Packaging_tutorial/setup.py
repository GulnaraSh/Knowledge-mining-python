# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:11:01 2020

@author: gulsha
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-gulnaracodes", # Replace with your own username
    version="0.0.1",
    author="Gulnara",
    author_email="gulsha@chalmers.se",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GulnaraSh/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)