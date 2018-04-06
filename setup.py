import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='oq-platform-taxtweb',
    version='1.2.0',
    packages=["openquakeplatform_taxtweb"],
    include_package_data=True,
    license='BSD License',  # example license
    description='Taxtweb - GEM building taxonomy editor',
    long_description=README,
    url='http://github.com/gem/oq-platform-taxtweb',
    author='GEM Foundation',
    author_email='devops@openquake.org',
    install_requires=[
        'django >=1.5, <2.1',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Scientists',
        'License :: OSI Approved :: AGPL3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
