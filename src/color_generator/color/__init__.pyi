#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t


class Color:
    @t.overload
    def __init__(self, color: str): ...
    @t.overload
    def __init__(self, color: t.Tuple[int, int, int]): ...
    @t.overload
    def __init__(self, r: int, g: int, b: int): ...

    r: int
    g: int
    b: int
    rgb: t.Type[int, int, int]

    hex: str
