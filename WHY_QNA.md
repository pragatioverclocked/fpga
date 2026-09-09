1. Why 24 bits pixel input for an image?
A. In an RGB image, each RGB and B are represented by 8 bits each (0-255) i.e. 8+8+8 = 24

2. How does one know that lower bits are B, middle bits G and higher bits R?
A. when Python creates the .mem file, it is intentionally packed it this way:
pixel = (r << 16) | (g << 8) | b