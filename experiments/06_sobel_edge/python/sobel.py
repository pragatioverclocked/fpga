
import os
import numpy as np
from PIL import Image

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_IMAGE = os.path.join(PROJECT_ROOT, "test_vectors", "lena_rgb_input.png")
OUTPUT_IMAGE = os.path.join(PROJECT_ROOT, "results", "lena_python_sobel.png")

# Read RGB image
image = np.array(Image.open(INPUT_IMAGE).convert("RGB"), dtype=np.uint32)
height, width, _ = image.shape

# Convert RGB to grayscale
R = image[:, :, 0]
G = image[:, :, 1]
B = image[:, :, 2]

gray = (77 * R + 150 * G + 29 * B + 128) >> 8

# Output image
output = np.zeros((height, width), dtype=np.uint8)

# Sobel edge detection
for y in range(1, height - 1):
    for x in range(1, width - 1):

        p = gray[y-1:y+2, x-1:x+2]

        gx = (
            -int(p[0, 0]) + int(p[0, 2])
            - 2*int(p[1, 0]) + 2*int(p[1, 2])
            - int(p[2, 0]) + int(p[2, 2])
        )

        gy = (
            -int(p[0, 0]) - 2*int(p[0, 1]) - int(p[0, 2])
            + int(p[2, 0]) + 2*int(p[2, 1]) + int(p[2, 2])
        )

        magnitude = abs(gx) + abs(gy)

        output[y, x] = min(magnitude, 255)

# Save output
os.makedirs(os.path.dirname(OUTPUT_IMAGE), exist_ok=True)
Image.fromarray(output).save(OUTPUT_IMAGE)

print("Sobel edge detection completed!")
print(f"Resolution: {width} x {height}")
print(f"Output: {OUTPUT_IMAGE}")
