#!/bin/sh

python ./hello_world.py
python ./exc_class.py
python ./exc_class2.py
python ./exc_file.py 23
python ./exc_list.py
python ./exc_time.py
for f in $(ls leetcode/*py); do python $f; done