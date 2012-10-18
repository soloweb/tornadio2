#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

try:
    license = open('LICENSE').read()
except:
    license = None

try:
    readme = open('README.rst').read()
except:
    readme = None

setup(
    name='tornad_io2',
    version='0.0.4',
    author='Serge S. Koval',
    author_email='serge.koval@gmail.com',
    packages=['tornadio2'],
    scripts=[],
    url='https://github.com/soloweb/tornadio2/',
    license=license,
    description='Socket.io 0.7+ server implementation on top of Tornado framework',
    long_description=readme,
    requires=['simplejson', 'tornado'],
    install_requires=[
        'simplejson >= 2.1.0',
        'tornado >= 2.2.0'
    ]
)
