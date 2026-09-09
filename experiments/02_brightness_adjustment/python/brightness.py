import os
from PIL import Image
import numpy as np


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

INPUT_IMAGE = os.path.join(
    SCRIPT_DIR,
    "lena_rgb_input.png"
)

OUTPUT_IMAGE = os.path.join(
    PROJECT_ROOT,
    "results",
    "lena_python_brightness.png"
)

os.makedirs(
    os.path.dirname(OUTPUT_IMAGE),
    exist_ok=True
)


# Brightness value
K = 50


# Read image
image = Image.open(INPUT_IMAGE).convert("RGB")
pixels = np.array(image, dtype=np.uint8)


# Convert to wider type before addition
brightened = pixels.astype(np.int16) + K


# Saturation / clipping
brightened = np.clip(
    brightened,
    0,
    255
)


# Convert back to 8-bit
brightened = brightened.astype(np.uint8)


# Save image
output_image = Image.fromarray(
    brightened,
    "RGB"
)

output_image.save(OUTPUT_IMAGE)


print("========================================")
print("   EXPERIMENT 2 - BRIGHTNESS")
print("========================================")

print(f"Input     : {INPUT_IMAGE}")
print(f"Output    : {OUTPUT_IMAGE}")
print(f"Brightness: +{K}")
print(f"Size      : {pixels.shape[1]} x {pixels.shape[0]}")

print("----------------------------------------")
print("Brightness adjustment completed.")
print("Saturation limit = 255")
print("========================================")