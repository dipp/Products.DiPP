# -*- coding: utf-8 -*-
"""
This module contains the tool of Products.DiPP
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

__version__ = read('Products','DiPP','version.txt').strip()

long_description = (
    read('README.txt')
    )

tests_require = ['zope.testing']

setup(name='Products.DiPP',
      version=__version__,
      description="Digital Peer Publishing",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='DiPP, Hochschulbibliothekszentrum NRW',
      author_email='dipp@hbz-nrw.de',
      url='http://www.dipp.nrw.de',
      license='DFSL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'Products.TextIndexNG3',
        'Products.ATVocabularyManager',
        'Products.LinguaPlone',
        'Products.qPloneCaptchas',
        'dipp.tools >= 0.3',
        'dipp.dipp2',
        'bibliograph.core',
        'dipp.fedora2 >= 2.2'
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='Products.DiPP.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """
      )
