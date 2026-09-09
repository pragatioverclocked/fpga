from PIL import Image
import numpy as np
import os

WIDTH = 512
HEIGHT = 512

INPUT_MEM = "test_vectors/lena_rgb_output.mem"
OUTPUT_IMAGE = "results/lena_rgb_verilog_output.png"


def read_mem_file(filename):

    with open(filename, "r") as f:
        values = [
            int(line.strip(), 16)
            for line in f
            if line.strip()
        ]

    return np.array(values, dtype=np.uint32)


pixels = read_mem_file(INPUT_MEM)

# Extract RGB channels
r = (pixels >> 16) & 0xFF
g = (pixels >> 8) & 0xFF
b = pixels & 0xFF

image_array = np.stack((r, g, b), axis=1)

# Reshape into image
image_array = image_array.reshape(
    HEIGHT,
    WIDTH,
    3
).astype(np.uint8)

image = Image.fromarray(image_array, "RGB")

# Create results folder if it does not exist
os.makedirs("results", exist_ok=True)
image.save(OUTPUT_IMAGE)

print("========================================")
print("      MEM TO IMAGE RECONSTRUCTION")
print("========================================")
print(f"Resolution : {WIDTH} x {HEIGHT}")
print(f"Output     : {OUTPUT_IMAGE}")
print("SUCCESS")
print("========================================")