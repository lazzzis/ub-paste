#!/usr/bin/env python

from setuptools import find_packages, setup

import ub_paste

setup(
    name='ub-paste',
    version=ub_paste.__version__,
    license='MIT',
    author='lazzzis',
    author_email='shenlijin@outlook.com',
    description='Help you paste your file content to ubuntu pastebin',
    long_description=open('README.md').read(),
    url='https://github.com/lazzzis/ub-paste',
    packages=find_packages(),
    platforms='any',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
        'requests',
    ],
    entry_points={'console_scripts': ['ub-paste=ub_paste.ub_paste:cli']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Intended Audience :: Developers",
    ], )
