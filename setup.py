# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='huffman-project',
    version='0.2.2',
    description='huffman-project package to reduce data based on character frequency',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Maverick Perrollaz',
    author_email='maverick.perrollaz@pm.me',
    url='https://github.com/M4verickFr/huffman-project',
    license='Apache 2 License',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
