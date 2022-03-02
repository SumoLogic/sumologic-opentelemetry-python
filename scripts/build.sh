#!/usr/bin/env bash

set -euxo pipefail

rm -rf dist
python3 setup.py clean
python3 setup.py sdist bdist_wheel
