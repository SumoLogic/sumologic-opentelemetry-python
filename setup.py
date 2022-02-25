import io
import os
import re

from setuptools import find_packages
from setuptools import setup
from os.path import join
from os.path import dirname
from os.path import abspath

here = abspath(dirname(__file__))

with open(join(here, 'VERSION')) as VERSION_FILE:
    __versionstr__ = VERSION_FILE.read().strip()


with open(join(here, 'requirements.txt')) as REQUIREMENTS:
    INSTALL_REQUIRES = REQUIREMENTS.read().split('\n')

with io.open(join(here, 'README.md'), encoding='utf-8') as f:
    # long_description = f.read()
    text_type = type(u"")
    LONG_DESCRIPTION = re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), f.read())


setup(
    name="sumologic-opentelemetry",
    version=__versionstr__,
    url="https://github.com/jmroz-sumo/sumologic-opentelemetry-python",
    license='Apache',

    author="Sumo Logic, Inc. Authors",
    author_email="jmroz@sumologic.com",

    description="An all-in-one package for python projects used to enable OpenTelemetry auto-instrumentation",
    
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',

    packages=find_packages(exclude=('tests',)),

    install_requires=INSTALL_REQUIRES,

    # Trove classifiers
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    zip_safe=True,
    include_package_data=True,

    # # $ setup.py publish support.
    # cmdclass={
    #     'upload': UploadCommand,
    # },
)
