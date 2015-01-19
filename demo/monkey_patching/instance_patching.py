#!/usr/bin/env python
# coding: utf-8
import __future__
import types
"""
Demonstrating the usage of Monky patching a class in python.
"""


class Monky:
    def __init__(_, name):
        _.name = name

    def eat_banana(_):
        print 'Jum jum'
        print '{name} is eating a banana'.format(name=_.name)


monky = Monky('Bubbles')
monky.eat_banana()


def eat_apple(_, *args):
    print 'Jum jum'
    print '{name} is eating a apple'.format(name=_.name)


monky.eat_apple = types.MethodType( eat_apple, monky )
monky.eat_apple()
