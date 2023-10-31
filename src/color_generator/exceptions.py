# -*- coding=utf-8 -*-
r"""

"""


__all__ = [
    'ColorGenerationError',
    'InvalidColorError', 'UnknownColorError', 'BadColorTypeError', 'BadColorRangeError',
    'UnknownGeneratorError'
]


class ColorGenerationError(Exception):
    pass


class InvalidColorError(ColorGenerationError):
    pass


class UnknownColorError(ColorGenerationError):
    pass


class BadColorTypeError(InvalidColorError):
    pass


class BadColorRangeError(InvalidColorError):
    pass


class UnknownGeneratorError(ColorGenerationError):
    pass
