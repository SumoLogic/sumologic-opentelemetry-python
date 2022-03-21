import io
import re
from os.path import abspath, dirname, join

from setuptools import find_packages, setup

here = abspath(dirname(__file__))

with open(join(here, "VERSION")) as VERSION_FILE:
    __versionstr__ = VERSION_FILE.read().strip()

with open(join(here, "requirements.txt")) as REQUIREMENTS:
    INSTALL_REQUIRES = REQUIREMENTS.read().split("\n")

with open(join(here, "requirements-extra.txt")) as REQUIREMENTS_EXTRA:
    INSTALL_REQUIRES_EXTRA = REQUIREMENTS_EXTRA.read().split("\n")

with io.open(join(here, "README.md"), encoding="utf-8") as f:
    text_type = type("")
    LONG_DESCRIPTION = re.sub(
        text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), f.read()
    )

EXTRAS_INSTALL = {"all": INSTALL_REQUIRES_EXTRA}

setup(
    name="sumologic-opentelemetry",
    version=__versionstr__,
    description=(
        "An all-in-one package for python projects used to enable "
        "OpenTelemetry auto-instrumentation"
    ),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/SumoLogic/sumologic-opentelemetry-python",
    license="Apache-2.0",
    author="Sumo Logic, Inc. Authors",
    author_email="support@sumologic.com",
    packages=find_packages(exclude=("tests",)),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_INSTALL,
    python_requires=">=3.6",
    # Trove classifiers
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    scripts=["scripts/sumologic-opentelemetry-instrument"],
    zip_safe=True,
    include_package_data=True,
)
