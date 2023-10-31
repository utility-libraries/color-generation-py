# color-generator
generate random good-looking colors

## Installation
`pip install color-generation`

## usage example

```python
import color_generator

color = color_generator.generate()
print(color)  # <Color (139,242,38)>
color = color_generator.generate("colorless")
print(color)  # <Color (1,70,24)>
print(color.hex)  # '#014618'
```

# generation modes
passed as string to `generate(mode)`

## basic
- can contain the full variety of colors
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-basic.png)

## no-mono
- attempts to avoid colors like black and white
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-no-mono.png)

## colorful
- generates light colors
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-colorful.png)

## colorless
- generates darker colors
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-colorless.png)
