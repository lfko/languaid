#!/bin/sh
# script for a local build
sudo rm -r dist/ LanguAid.egg-info/
sudo python setup.py sdist --formats=gztar,zip