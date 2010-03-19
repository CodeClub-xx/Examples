from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='CodeClubExamples',
      version=version,
      description="CodeClub Examples",
      long_description="""\
CodeClub examples""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='codeclub',
      author_email='codeclub-discussion@lists.coactivate.org',
      url='http://github.com/codeclub',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
