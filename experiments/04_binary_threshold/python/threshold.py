
import os
import numpy as np
from PIL import Image

# Project directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input and output paths
INPUT_IMAGE = os.path.join(PROJECT_ROOT, "test_vectors", "lena_rgb_input.png")
OUTPUT_IMAGE = os.path.join(PROJECT_ROOT, "results", "lena_python_binary.png")

# Threshold value
THRESHOLD = 128

# Read RGB image
image = Image.open(INPUT_IMAGE).convert("RGB")
pixels = np.array(image, dtype=np.uint32)

# Extract RGB channels
R = pixels[:, :, 0]
G = pixels[:, :, 1]
B = pixels[:, :, 2]

# Convert RGB to grayscale using fixed-point arithmetic
gray = (77 * R + 150 * G + 29 * B + 128) >> 8

# Apply binary thresholding
binary = np.where(gray >= THRESHOLD, 255, 0).astype(np.uint8)

# Save output image
os.makedirs(os.path.dirname(OUTPUT_IMAGE), exist_ok=True)
Image.fromarray(binary).save(OUTPUT_IMAGE)

print("Binary thresholding completed successfully!")
print(f"Input image  : {INPUT_IMAGE}")
print(f"Output image : {OUTPUT_IMAGE}")
print(f"Resolution   : {image.width} x {image.height}")
print(f"Threshold    : {THRESHOLD}")
