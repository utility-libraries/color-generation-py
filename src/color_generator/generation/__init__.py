#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from .color_generation import generate, register_generator, generation_modes
from .color_generation import (
    basic as generate_basic,
    no_mono as generate_no_mono,
    colorful as generate_colorful,
    colorless as generate_colorless,
)
