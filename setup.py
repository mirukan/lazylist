#!/usr/bin/env python3

from setuptools import setup, find_packages


def get_readme():
    with open("README.md", "r") as readme:
        return readme.read()


setup(
    name        = "lazylist",
    version     = "0.2.0",

    author       = "Andrew Barnert, miruka",
    author_email = "abarnert@yahoo.com, miruka@disroot.org",
    license      = "MIT",

    description                   = "Lazy list",
    long_description              = get_readme(),
    long_description_content_type = "text/markdown",

    python_requires  = ">=3.5, <4",

    packages = find_packages(),

    keywords = "lazy list generator iterator",
    url      = "https://github.com/mirukan/lazylist",

    classifiers=[
        "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",

        "Intended Audience :: Developers",

        "Topic :: Utilities",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
