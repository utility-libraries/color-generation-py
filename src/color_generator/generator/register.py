# -*- coding=utf-8 -*-
r"""

"""


GENERATORS = {}


def get_generators():
    return list(GENERATORS.keys())


def register_generator(fn):
    GENERATORS[fn.__name__.lower().replace('_', '-')] = fn
    return fn
