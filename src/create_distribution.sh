#!/bin/bash

rm -rf dist trajtrackerp.egg-info build

export PYTHONPATH=/git/trajtracker/src
python setup.py bdist_wheel --universal

rm -rf trajtrackerp.egg-info build

# After the distribution was tested, upload it to PyPi by writing:
# twine upload <distribution_file_name>

