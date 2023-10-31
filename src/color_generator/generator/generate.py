# -*- coding=utf-8 -*-
r"""

"""
from ..exceptions import UnknownGeneratorError
from .register import GENERATORS


def generate(generator: str = 'colorful'):
    try:
        return GENERATORS[generator]()
    except KeyError:
        raise UnknownGeneratorError(generator)
