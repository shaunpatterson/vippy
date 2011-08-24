#!/bin/sh

PYTHONPATH=/usr/local/eclipse/eclipse/plugins/org.python.pydev.debug_2.2.1.2011071313/pysrc/
PYTHONPATH=/usr/lib64/python31.zip:$PYTHONPATH
PYTHONPATH=/usr/lib64/python3.1/site-packages/:$PYTHONPATH
PYTHONPATH=/usr/lib64/python3.1/:$PYTHONPATH
PYTHONPATH=/usr/lib64/python3.1/plat-linux2/:$PYTHONPATH
PYTHONPATH=/usr/lib64/python3.1/lib-dynload/:$PYTHONPATH
PYTHONPATH=./src/:$PYTHONPATH
PYTHONPATH=.:$PYTHONPATH

export PYTHONPATH

python3.1 ./src/vippy/Vippy.py
