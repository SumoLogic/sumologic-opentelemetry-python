#!/usr/bin/env bash

set -euxo pipefail


python3 setup.py clean
python3 setup.py sdist bdist_wheel
