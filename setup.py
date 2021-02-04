# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in tester/__init__.py
from tester import __version__ as version

setup(
	name='tester',
	version=version,
	description='TESTER',
	author='Manduul',
	author_email='manduul@hello.mn',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
