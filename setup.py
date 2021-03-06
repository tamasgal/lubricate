#!/usr/bin/env python
# Filename: setup.py
"""
The lubricate setup script.

"""
import os
from setuptools import setup

__author__ = 'Zineb Aly and Tamas Gal'
__email__ = 'zaly@km3net.de, tgal@km3net.de'


THISPATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(THISPATH, "requirements.txt")) as fobj:
    requirements = [l.strip() for l in fobj.readlines()]

with open(os.path.join(THISPATH, "README.md")) as f:
    long_description = f.read()

setup(
    name='lubricate',
    url='https://github.com/tamasgal/lubricate/',
    description=long_description,
    author=__author__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email=__email__,
    packages=['lubricate'],
    include_package_data=True,
    platforms='any',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=requirements,
    python_requires='>=3.5',
    entry_points={
        'console_scripts': ['lubricate=lubricate.cmd:main'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
    ],
)
