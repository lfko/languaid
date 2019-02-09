#!/bin/sh

CWD=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
export PYTHONPATH=$CWD:$PYTHONPATH
python3.5 python/languaid/main/languaidMain.py

