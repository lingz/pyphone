#!/usr/bin/env python3

from distutils.core import setup
setup(
  name = 'pyphone',
  packages = ['pyphone'], # this must be the same as the name above
  version = '0.1.5',
  description = 'Phonetic manipulation library',
  author = 'Ling Zhang',
  author_email = 'lz@ling.nz',
  url = 'https://github.com/lingz/pyphone', # use the URL to the github repo
  install_requires = [
    'scipy'
  ],
  include_package_data = True,
  keywords = ['nlp', 'phonetic', 'ipa'],
    package_data = {
        'pyphone': ['data/mappings/*.json']
    }
)

