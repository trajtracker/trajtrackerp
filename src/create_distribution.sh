#!/bin/bash

rm -rf dist trajtrackerp.egg-info build

export PYTHONPATH=/git/trajtracker/src
python setup.py bdist_wheel --universal

