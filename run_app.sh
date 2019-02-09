#!/bin/sh

CWD=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
export PYTHONPATH=$CWD:$PYTHONPATH
python python/languaid/main/languaidMain.py

