#!/usr/bin/env python
# coding: utf-8
from lib.text_tools import print_string_diff

expected = 'abs-cda'
actual = 'abs_cda'

print_string_diff(expected, actual)
