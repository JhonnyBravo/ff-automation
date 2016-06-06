#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="ff-automation",
    version="1.0",
    description="Firefox automation utility.",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/ff-automation.git",
    packages=find_packages(),
    install_requires=["selenium"],
    entry_points={
        "console_scripts": [
            "get_content_by_css_selector=ps_firefox.bin.get_content_by_css_selector:main",
            "get_content_by_tag_name=ps_firefox.bin.get_content_by_tag_name:main",
            "get_content_by_xpath=ps_firefox.bin.get_content_by_xpath:main"
        ]
    },
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
