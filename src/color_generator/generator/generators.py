# -*- coding=utf-8 -*-
r"""

"""
import random
from ..color import Color
from .register import register_generator


@register_generator
def basic():
    rgb = [
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    ]
    # random.shuffle(rgb)  # not needed
    return Color(*rgb)


@register_generator
def no_mono():
    rgb = [
        random.randint(100, 255),
        random.randint(0, 255),
        random.randint(0, 150),
    ]
    random.shuffle(rgb)
    return Color(*rgb)


@register_generator
def colorful():
    rgb = [
        random.randint(0, 128),
        random.randint(192, 255),
        random.randint(128, 255),
    ]
    random.shuffle(rgb)
    return Color(*rgb)


@register_generator
def colorless():
    rgb = [
        random.randint(0, 64),
        random.randint(0, 128),
        random.randint(64, 128),
    ]
    random.shuffle(rgb)
    return Color(*rgb)
