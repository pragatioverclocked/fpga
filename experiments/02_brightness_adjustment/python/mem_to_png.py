import os
from PIL import Image
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

INPUT_MEM = os.path.join(
    PROJECT_ROOT,
    "test_vectors",
    "lena_rgb_verilog_brightness.mem"
)

OUTPUT_IMAGE = os.path.join(
    PROJECT_ROOT,
    "results",
    "lena_verilog_brightness.png"
)

WIDTH = 512
HEIGHT = 512

os.makedirs(
    os.path.dirname(OUTPUT_IMAGE),
    exist_ok=True
)

pixels = []

with open(INPUT_MEM, "r") as f:
    for line in f:
        value = int(line.strip(), 16)

        r = (value >> 16) & 0xFF
        g = (value >> 8) & 0xFF
        b = value & 0xFF

        pixels.append([r, g, b])

image_array = np.array(
    pixels,
    dtype=np.uint8
).reshape(HEIGHT, WIDTH, 3)

image = Image.fromarray(
    image_array,
    "RGB"
)

image.save(OUTPUT_IMAGE)

print("========================================")
print("   VERILOG MEM -> PNG")
print("========================================")
print(f"Input  : {INPUT_MEM}")
print(f"Output : {OUTPUT_IMAGE}")
print(f"Size   : {WIDTH} x {HEIGHT}")
print("----------------------------------------")
print("Conversion completed successfully.")
print("========================================")