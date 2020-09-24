#!/usr/bin/env python3
from setuptools import setup

setup(
    name="ugit",
    version="1.0",
    packages=['src'],
    entry_points={
        'console_scripts': [
            "ugit = src.cli:main"
        ]
    }
)
