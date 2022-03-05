# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import fastentrypoints

dependencies = ["click"]

config = {
    "version": "0.1",
    "name": "mp2null",
    "url": "https://github.com/jakeogh/mp2null",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "convert messagepacked stdin to null terminated stdout",
    "long_description": __doc__,
    "packages": find_packages(exclude=["tests"]),
    "package_data": {"mp2null": ["py.typed"]},
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
    "entry_points": {
        "console_scripts": [
            "mp2null=mp2null.mp2null:cli",
        ],
    },
}

setup(**config)
