#!/usr/bin/env zsh
source `which virtualenvwrapper.sh`
workon py_triks | mkvirtualenv py_triks && workon py_triks
pip install -r requirements.txt
