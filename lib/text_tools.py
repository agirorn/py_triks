# coding: utf-8
import difflib
import __future__


def print_string_diff(expected, actual):
    """
    Prints out a nice visual diff of two strings.
    """
    diff = difflib.ndiff(expected.splitlines(1),
                         actual.splitlines(1))
    diff = list(diff)  # materialize the generated delta into a list
    print "\n".join(diff)
