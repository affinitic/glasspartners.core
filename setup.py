# -*- coding: utf-8 -*-

version = '0.1'

from setuptools import setup, find_packages

long_description = (open('README.rst').read() + '\n')

setup(name='glasspartners.core',
      version=version,
      description='Core package for Glass Partners website',
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
      ],
      keywords='',
      author='Glass Partners',
      author_email='support@lists.affinitic.be',
      url='https://github.com/affinitic/glasspartners.core',
      license='gpl',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.api',
          'Plone',
      ],
      entry_points={},
)
