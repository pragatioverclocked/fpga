import os
from PIL import Image
import numpy as np


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_IMAGE = os.path.join(
    SCRIPT_DIR,
    "lena_rgb_input.png"
)

OUTPUT_IMAGE = os.path.join(
    SCRIPT_DIR,
    "..",
    "results",
    "lena_python_inverted.png"
)


# Create results directory
os.makedirs(
    os.path.dirname(OUTPUT_IMAGE),
    exist_ok=True
)


# Read image
image = Image.open(INPUT_IMAGE).convert("RGB")

pixels = np.array(
    image,
    dtype=np.uint8
)


# Pixel inversion
inverted = 255 - pixels


# Convert back to image
output_image = Image.fromarray(
    inverted,
    "RGB"
)


# Save result
output_image.save(
    OUTPUT_IMAGE
)


print("========================================")
print("       EXPERIMENT 1 - PIXEL INVERSION")
print("========================================")
print(f"Input  : {INPUT_IMAGE}")
print(f"Output : {OUTPUT_IMAGE}")
print(f"Size   : {pixels.shape[1]} x {pixels.shape[0]}")
print("----------------------------------------")
print("Pixel inversion completed successfully.")
print("========================================")