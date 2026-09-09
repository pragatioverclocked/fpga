import os
from PIL import Image
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

MEM_FILE = os.path.join(
    PROJECT_ROOT,
    "test_vectors",
    "lena_rgb_verilog_inverted.mem"
)

OUTPUT_IMAGE = os.path.join(
    PROJECT_ROOT,
    "results",
    "lena_verilog_inverted.png"
)

os.makedirs(
    os.path.dirname(OUTPUT_IMAGE),
    exist_ok=True
)


def read_mem_file(filename):

    with open(filename, "r") as f:
        values = [
            int(line.strip(), 16)
            for line in f
            if line.strip()
        ]

    return np.array(values, dtype=np.uint32)


pixels = read_mem_file(MEM_FILE)

# Current image is 512 x 512
WIDTH = 512
HEIGHT = 512

if len(pixels) != WIDTH * HEIGHT:
    raise ValueError(
        f"Expected {WIDTH * HEIGHT} pixels, "
        f"but found {len(pixels)}"
    )

# Reshape into image
pixels = pixels.reshape((HEIGHT, WIDTH))

# Extract RGB channels
red = (pixels >> 16) & 0xFF
green = (pixels >> 8) & 0xFF
blue = pixels & 0xFF

# Combine channels
rgb = np.stack(
    [red, green, blue],
    axis=2
).astype(np.uint8)

# Save PNG
image = Image.fromarray(rgb, "RGB")
image.save(OUTPUT_IMAGE)

print("========================================")
print("   VERILOG MEM → PNG")
print("========================================")
print(f"Input  : {MEM_FILE}")
print(f"Output : {OUTPUT_IMAGE}")
print(f"Size   : {WIDTH} x {HEIGHT}")
print("----------------------------------------")
print("PNG reconstruction successful.")
print("========================================")