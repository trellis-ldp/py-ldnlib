#!/usr/bin/env python

from setuptools import setup

setup(name='py-ldn',
      version='0.1.0',
      description='Python-based linked data notification libraries',
      author='Aaron Coburn',
      author_email='acoburn@amherst.edu',
      maintainer='Aaron Coburn',
      maintainer_email='acoburn@amherst.edu',
      classifiers=[
	"Programming Language :: Python",
	"Programming Language :: Python :: 3",
	"License :: OSI Approved :: Apache Software License",
        "Topic :: Internet :: WWW/HTTP"],
      url='https://github.com/trellis-ldp/py-ldn',
      packages=['ldn'],
      install_requires=[
          'requests',
          'rdflib>=4.2',
          'rdflib-jsonld>=4.2'])

