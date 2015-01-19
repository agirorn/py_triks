#!/usr/bin/env python
# coding: utf-8
import __future__
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


def eat_apple(_):
    print 'Jum jum'
    print '{name} is eating a apple'.format(name=_.name)


Monky.eat_apple = eat_apple
monky.eat_apple()
