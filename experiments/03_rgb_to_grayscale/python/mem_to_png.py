import os
from PIL import Image
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

INPUT_MEM = os.path.join(
    PROJECT_ROOT,
    "test_vectors",
    "lena_gray_verilog_fixed.mem"
)

OUTPUT_IMAGE = os.path.join(
    PROJECT_ROOT,
    "results",
    "lena_verilog_grayscale_fixed.png"
)

WIDTH = 512
HEIGHT = 512

pixels = []

with open(INPUT_MEM, "r") as f:
    for line in f:
        pixels.append(int(line.strip(), 16))

image_array = np.array(
    pixels,
    dtype=np.uint8
).reshape(HEIGHT, WIDTH)

image = Image.fromarray(
    image_array,
    "L"
)

image.save(OUTPUT_IMAGE)

print("========================================")
print("   VERILOG GRAYSCALE MEM -> PNG")
print("========================================")
print(f"Input  : {INPUT_MEM}")
print(f"Output : {OUTPUT_IMAGE}")
print(f"Size   : {WIDTH} x {HEIGHT}")
print("----------------------------------------")
print("Conversion completed successfully.")
print("========================================")