# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from ..color import Color


def generate(generator: t.Union[t.Literal["basic", 'no-mono', "colorful", "colorless"], str] = "color") -> Color: ...

def registerGenerator(fn: t.Callable): ...

def generationModes() -> t.List[str]: ...
