#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import re
import colorsys
from ..exceptions import UnknownColorError, BadColorTypeError, BadColorRangeError


class Color:
    _r, _g, _b = 0, 0, 0

    def __init__(self, *color):
        r"""
        Color(r, g, b)
        Color((r, g, b))
        Color([r, g, b])
        Color('#HEXCOL')
        """
        if len(color) == 1:
            color = color[0]

        if isinstance(color, (tuple, list)) and len(color) == 3:
            r, g, b = color
        elif isinstance(color, str) and len(color) == 7:
            color = color.lstrip('#')
            r, g, b = tuple(int(color[i:i+2], 16) for i in range(0, len(color), 2))
        else:
            raise UnknownColorError(f'invalid color: {color!r}')

        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def from_rgb(cls, r: int, g: int, b: int) -> 'Color':
        return cls(r, g, b)

    @classmethod
    def from_hex(cls, hex_color: str, *, allow_irregular: bool = False) -> 'Color':
        r"""

        :param hex_color: '#HEXCOL'
        :param allow_irregular: allow '#HEX' variants
        :return:
        """
        if allow_irregular:
            if re.fullmatch(r"#[0-9A-F]{3}", hex_color, re.IGNORECASE):
                hex_color = hex_color.lstrip('#')
                r, g, b = (int(hex_color[i:i+2], 16) for i in range(0, len(hex_color), 2))
                return cls(r, g, b)
            # maybe also len 9 or so
        if re.fullmatch(r"#[0-9A-F]{6}", hex_color, re.IGNORECASE):
            hex_color = hex_color.lstrip('#')
            r, g, b = (int(hex_color[i:i+2], 16) for i in range(0, len(hex_color), 2))
            return cls(r, g, b)
        raise UnknownColorError(f"invalid hex color passed ({hex_color!r})")

    @classmethod
    def from_hls(cls, h: float, l: float, s: float) -> 'Color':
        r"""
        :param h: color-angle
        :param l: luma
        :param s: saturation
        """
        r, g, b = colorsys.hls_to_rgb(h=h, l=l, s=s)
        return cls(r, g, b)

    @classmethod
    def from_hsv(cls, h: float, s: float, v: float) -> 'Color':
        r"""
        :param h: hue
        :param s: saturation
        :param v: value
        """
        r, g, b = colorsys.hsv_to_rgb(h=h, s=s, v=v)
        return cls(r, g, b)

    @classmethod
    def from_yiq(cls, y: float, i: float, q: float) -> 'Color':
        r"""
        :param y: luma
        :param i: cyan-orange
        :param q: magenta-green
        """
        r, g, b = colorsys.yiq_to_rgb(y=y, i=i, q=q)
        return cls(r, g, b)

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        if isinstance(value, float):
            value = int(value)
        if not isinstance(value, int):
            raise BadColorTypeError('color requires an integer')
        if not (0 <= value <= 255):
            raise BadColorRangeError('invalid color-range')
        self._r = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        if isinstance(value, float):
            value = int(value)
        if not isinstance(value, int):
            raise BadColorTypeError('color requires an integer')
        if not (0 <= value <= 255):
            raise BadColorRangeError('invalid color-range')
        self._g = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if isinstance(value, float):
            value = int(value)
        if not isinstance(value, int):
            raise BadColorTypeError('color requires an integer')
        if not (0 <= value <= 255):
            raise BadColorRangeError('invalid color-range')
        self._b = value

    @property
    def rgb(self):
        return self.r, self.g, self.b

    @rgb.setter
    def rgb(self, value):
        if not isinstance(value, (tuple, list)) or len(value) != 3:
            raise BadColorTypeError('rgb requires tuple or list of length 3')
        _r, _g, _b = self.rgb
        r, g, b = value
        try:
            self.r = r
            self.g = g
            self.b = b
        except BaseException as err:
            # restore color if something failed
            self._r = _r
            self._g = _g
            self._b = _b
            raise err

    @property
    def hex(self):
        return '#%02x%02x%02x' % self.rgb

    @property
    def hls(self):
        return colorsys.rgb_to_hls(self.r, self.g, self.b)

    @property
    def hsv(self):
        return colorsys.rgb_to_hsv(self.r, self.g, self.b)

    @property
    def yiq(self):
        return colorsys.rgb_to_yiq(self.r, self.g, self.b)

    def __repr__(self):
        return f'<{self.__class__.__qualname__} ({self.r},{self.g},{self.b})>'


if __name__ == '__main__':
    c1 = Color(255, 255, 255)
    print(c1, c1.hex)
    try:
        Color('#123')
    except ValueError:
        pass
    else:
        raise Exception()
    c4 = Color('#123456')
    print(c4, c4.hex)
    try:
        Color('#123456789')
    except ValueError:
        pass
    else:
        raise Exception()
