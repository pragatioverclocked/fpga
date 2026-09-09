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
    "lena_python_grayscale.png"
)

os.makedirs(
    os.path.dirname(OUTPUT_IMAGE),
    exist_ok=True
)

# Read RGB image
image = Image.open(INPUT_IMAGE).convert("RGB")
pixels = np.array(image, dtype=np.float64)

# Separate RGB channels
R = pixels[:, :, 0]
G = pixels[:, :, 1]
B = pixels[:, :, 2]

# Floating-point grayscale conversion
grayscale = (
    0.299 * R +
    0.587 * G +
    0.114 * B
)

# Round and convert to 8-bit
grayscale = np.round(grayscale).astype(np.uint8)

# Save grayscale image
output_image = Image.fromarray(
    grayscale,
    "L"
)

output_image.save(OUTPUT_IMAGE)

print("========================================")
print("    EXPERIMENT 3 - RGB TO GRAYSCALE")
print("========================================")
print(f"Input     : {INPUT_IMAGE}")
print(f"Output    : {OUTPUT_IMAGE}")
print(f"Size      : {pixels.shape[1]} x {pixels.shape[0]}")
print("----------------------------------------")
print("Method    : Floating-point luminance")
print("Formula   : 0.299R + 0.587G + 0.114B")
print("----------------------------------------")
print("Grayscale conversion completed.")
print("========================================")