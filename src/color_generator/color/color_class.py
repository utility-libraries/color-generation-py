#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""


class Color:
    _r, _g, _b = 0, 0, 0

    def __init__(self, *color):
        # only one argument passed
        if isinstance(color, tuple) and len(color) == 1:
            color = color[0]

        if isinstance(color, str) and len(color) in (6, 7):
            color = color.lstrip('#')
            r, g, b = tuple(int(color[i:i+2], 16) for i in range(0, len(color), 2))
        elif isinstance(color, (tuple, list)) and len(color) == 3:
            r, g, b = color
        else:
            raise ValueError('invalid color')

        self.r = r
        self.g = g
        self.b = b

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        if not isinstance(value, int):
            raise TypeError('color requires an integer')
        if not (0 <= value <= 255):
            raise ValueError('invalid color-range')
        self._r = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        if not isinstance(value, int):
            raise TypeError('color requires an integer')
        if not (0 <= value <= 255):
            raise ValueError('invalid color-range')
        self._g = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, int):
            raise TypeError('color requires an integer')
        if not (0 <= value <= 255):
            raise ValueError('invalid color-range')
        self._b = value

    @property
    def rgb(self):
        return self.r, self.g, self.b

    @rgb.setter
    def rgb(self, value):
        if not isinstance(value, (tuple, list)):
            raise TypeError('color requires an integer')
        self.r = value[0]
        self.g = value[1]
        self.b = value[2]

    @property
    def hex(self):
        return '#%02x%02x%02x' % self.rgb

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
