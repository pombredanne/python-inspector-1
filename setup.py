import os
from setuptools import setup, find_packages
setup(name='inspector',
      version='0.1.0',
      description=("Reads your code and returns a JSON description you can use to generate documentation. Like Sphinx AutoDoc but without Sphinx."),
      #long_description=open('README.rst').read(),
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'
                    ],
      install_requires=[
            'docopt>=0.6', 
      ], 
      keywords='documentation inspect inspection introspection autodoc sphinx',
      author='Stijn Debrouwere',
      author_email='stijn@stdout.be',
      download_url='http://www.github.com/stdbrouw/python-inspector/tarball/master',
      license='ISC',
      packages=find_packages(),
      entry_points = {
          'console_scripts': [
                'inspect = inspector:cli', 
          ],
      })