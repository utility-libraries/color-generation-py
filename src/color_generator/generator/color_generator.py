#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import random
from ..color import Color


generator_index = {}


def generationModes():
    return list(generator_index.keys())


def registerGenerator(fn):
    generator_index[fn.__name__.replace('_', '-')] = fn
    return fn


def generate(generator: str = 'colorful') -> Color:
    try:
        return generator_index[generator]()
    except KeyError:
        raise ValueError(f'unknown generator: {generator!r}')


@registerGenerator
def basic():
    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return Color(*rgb)


@registerGenerator
def no_mono():
    rgb = [random.randint(128, 255), random.randint(0, 255), random.randint(0, 128)]
    random.shuffle(rgb)
    return Color(*rgb)


@registerGenerator
def colorful():
    rgb = [random.randint(192, 255), random.randint(128, 255), random.randint(0, 128)]
    random.shuffle(rgb)
    return Color(*rgb)


@registerGenerator
def colorless():
    rgb = [random.randint(64, 128), random.randint(0, 128), random.randint(0, 64)]
    random.shuffle(rgb)
    return Color(*rgb)
