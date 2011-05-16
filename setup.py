from setuptools import setup, find_packages
import sys, os

version = '0.8.0'

try:
    readme = open('README.txt').read()
    changes = open("CHANGES.txt").read()
    readme = "%s\n%s" % (changes, readme)
except:
    readme = ""

setup(name='opencore-listen',
      version=version,
      description="listen is a mailing list product for Plone",
      long_description=readme,
      classifiers=[],
      keywords='',
      author='Robert Marianski, Alec Mitchell, Chris Abraham, Rob Miller, Ethan Jucovy',
      author_email='listen-dev at lists.coactivate.org',
      url='http://trac.socialplanning.org/listen',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      dependency_links=[
        'https://svn.socialplanning.org/svn/vendor/Products.MailBoxer#egg=Products.MailBoxer-0.1vendor',
        'https://svn.socialplanning.org/svn/vendor/Products.ManageableIndex#egg=Products.ManageableIndex-0.1vendor',
        'https://svn.socialplanning.org/svn/vendor/Products.OFolder#egg=Products.OFolder-0.1vendor',
        ],
      install_requires=[
        'setuptools',
        'Products.MailBoxer==0.1vendor',
        'Products.ManageableIndex==0.1vendor',
        'Products.OFolder==0.1vendor',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
