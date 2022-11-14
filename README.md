# color-generator
generate random good-looking colors


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
- (0-255, 0-255, 0-255)
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-basic.png)

## no-mono
- attempts to avoid colors like black and white
- (128-255, 0-255, 0-128)
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-no-mono.png)

## colorful
- generates light colors
- (192-255, 128-255, 0-128)
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-colorful.png)

## colorless
- generates darker colors
- (64-128, 0-128, 0-64)
![example: basic](https://github.com/PlayerG9/py-color-generator/raw/main/README.assets/example-colorless.png)
