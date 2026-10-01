
import os
import numpy as np
from PIL import Image

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_IMAGE = os.path.join(PROJECT_ROOT, "test_vectors", "lena_rgb_input.png")
OUTPUT_IMAGE = os.path.join(PROJECT_ROOT, "results", "lena_python_mean.png")

image = np.array(Image.open(INPUT_IMAGE).convert("RGB"), dtype=np.uint32)
height, width, _ = image.shape

output = image.copy()

for y in range(1, height - 1):
    for x in range(1, width - 1):
        region = image[y-1:y+2, x-1:x+2, :]
        output[y, x, :] = np.sum(region, axis=(0, 1)) // 9

output = output.astype(np.uint8)

os.makedirs(os.path.dirname(OUTPUT_IMAGE), exist_ok=True)
Image.fromarray(output).save(OUTPUT_IMAGE)

print("3x3 Mean Filtering completed!")
print(f"Resolution: {width} x {height}")
print(f"Output: {OUTPUT_IMAGE}")
