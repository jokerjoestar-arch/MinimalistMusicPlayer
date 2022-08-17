#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="mmp",
    version="2022.8.17",
    author="Stefano Di Rienzo",
    python_requires=">=3.6",
    description="A python minimalist music player",
    packages=find_packages(where="src"),
    package_dir={"": "src/", "mmp": "src/mmp"},
    entry_points={"console_scripts": ["mmp=mmp.cli:mmp"]},
    requires=["mutagen", "pygame"],
    keywords="mmp",
    
)