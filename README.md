# color-generator
generate random good-looking colors

## Installation
`pip install color-generation`

## usage example

```python
from color_generator import Color, generate

# simple color-generation
color = generate()
print(color)  # <Color (139,242,38)>

# specific color-generation
color = generate("colorless")
print(color)  # <Color (1,70,24)>

# and various formats depending on your need
print(color.rgb)  # (1, 70, 24)
print(color.hex)  # '#014618'
print(color.hls)  # (0.3888888888888889, 35.5, -1.0)
print(color.hsv)  # (0.3888888888888889, 0.9857142857142858, 70)
print(color.yiq)  # (44.239999999999995, -26.532799999999995, -29.053599999999996)

# and you can also transform between formats
Color.from_hex('#014618').rgb  # (1, 70, 24)
```

# generation modes
passed as string to `generate(mode)`

- [basic](#basic)
- [no-mono](#no-mono)
- [colorful](#colorful)
- [colorless](#colorless)

## basic
- can contain the full variety of colors
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-basic.png)

## no-mono
- attempts to avoid colors like black and white
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-no-mono.png)

## colorful
- generates brighter colors
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-colorful.png)

## colorless
- generates darker colors
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-colorless.png)
