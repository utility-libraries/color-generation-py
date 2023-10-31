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
    def __init__(self, color: t.List[int]): ...
    @t.overload
    def __init__(self, r: int, g: int, b: int): ...

    @classmethod
    def from_hex(cls, hex_color: str, *, allow_irregular: bool = False) -> Color: ...

    @classmethod
    def from_hls(cls, h: float, l: float, s: float) -> Color: ...

    @classmethod
    def from_hsv(cls, h: float, s: float, v: float) -> Color: ...

    @classmethod
    def from_yiq(cls, y: float, i: float, q: float) -> Color: ...

    r: int
    g: int
    b: int
    rgb: t.Tuple[int, int, int]

    hex: str
    hls: t.Tuple[float, float, float]
    hsv: t.Tuple[float, float, float]
    yiq: t.Tuple[float, float, float]
