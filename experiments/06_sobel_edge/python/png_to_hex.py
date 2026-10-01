
import os
import numpy as np
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

INPUT_IMAGE = os.path.join(
    PROJECT_ROOT, "test_vectors", "lena_rgb_input.png"
)

OUTPUT_HEX = os.path.join(
    PROJECT_ROOT, "test_vectors", "lena_rgb_input.hex"
)

image = Image.open(INPUT_IMAGE).convert("RGB")
pixels = np.array(image, dtype=np.uint8)

height, width, _ = pixels.shape

os.makedirs(os.path.dirname(OUTPUT_HEX), exist_ok=True)

with open(OUTPUT_HEX, "w") as f:
    for row in pixels:
        for r, g, b in row:
            pixel = (int(r) << 16) | (int(g) << 8) | int(b)
            f.write(f"{pixel:06X}\n")

print("PNG to HEX conversion complete")
print(f"Resolution : {width} x {height}")
print(f"Total pixels: {width * height}")
print(f"Output     : {OUTPUT_HEX}")
