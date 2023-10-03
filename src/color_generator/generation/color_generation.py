#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import random
from ..color import Color


generator_index = {}


def generation_modes():
    return list(generator_index.keys())


def format_name(name: str) -> str:
    return name.replace('_', '-').lower()


def register_generator(fn):
    generator_index[format_name(fn.__name__)] = fn
    return fn


def generate(generator: str = 'colorful') -> Color:
    generator = format_name(generator)
    try:
        return generator_index[generator]()
    except KeyError:
        raise ValueError(f'unknown generator: {generator!r}')


@register_generator
def basic() -> Color:
    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return Color(*rgb)


@register_generator
def no_mono() -> Color:
    rgb = [random.randint(128, 255), random.randint(0, 255), random.randint(0, 128)]
    random.shuffle(rgb)
    return Color(*rgb)


@register_generator
def colorful() -> Color:
    rgb = [random.randint(192, 255), random.randint(128, 255), random.randint(0, 128)]
    random.shuffle(rgb)
    return Color(*rgb)


@register_generator
def colorless() -> Color:
    rgb = [random.randint(64, 128), random.randint(0, 128), random.randint(0, 64)]
    random.shuffle(rgb)
    return Color(*rgb)
