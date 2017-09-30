from __future__ import absolute_import, division, print_function, unicode_literals  # isort:skip # noqa

import os

from setuptools import find_packages, setup

README = ''

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='tox-travis-example',
    version='0.1',
    install_requires=['six'],
    packages=find_packages(),
    include_package_data=True,
    license='Public domain',
    description='Just an example project',
    long_description=README,
    url='https://www.example.com/',
    author='w0rp',
    author_email='devw0rp@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
