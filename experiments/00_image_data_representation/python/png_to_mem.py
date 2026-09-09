import os
from PIL import Image
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

INPUT_IMAGE = os.path.join(SCRIPT_DIR, "lena_rgb_input.png")
OUTPUT_MEM = os.path.join(PROJECT_ROOT, "test_vectors", "lena_rgb_input.mem")

os.makedirs(os.path.dirname(OUTPUT_MEM), exist_ok=True)

image = Image.open(INPUT_IMAGE).convert("RGB")
pixels = np.array(image, dtype=np.uint8)

height, width, channels = pixels.shape

with open(OUTPUT_MEM, "w") as f:
    for y in range(height):
        for x in range(width):
            r = int(pixels[y, x, 0])
            g = int(pixels[y, x, 1])
            b = int(pixels[y, x, 2])

            pixel = (r << 16) | (g << 8) | b
            f.write(f"{pixel:06X}\n")

print(f"Image      : {width} x {height}")
print(f"Pixels     : {width * height}")
print(f"MEM file   : {OUTPUT_MEM}")
print("SUCCESS")