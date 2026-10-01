
import os
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(BASE_DIR, "test_vectors", "lena_rgb_input.png")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

os.makedirs(RESULTS_DIR, exist_ok=True)

image = np.array(Image.open(INPUT_PATH).convert("RGB"), dtype=np.uint8)
height, width, _ = image.shape

output = image.copy()

kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
], dtype=np.uint16)

for y in range(1, height - 1):
    for x in range(1, width - 1):
        for c in range(3):
            total = 0

            for ky in range(3):
                for kx in range(3):
                    pixel = int(image[y + ky - 1, x + kx - 1, c])
                    total += pixel * int(kernel[ky, kx])

            output[y, x, c] = (total + 8) // 16

output_path = os.path.join(RESULTS_DIR, "lena_python_gaussian.png")
Image.fromarray(output).save(output_path)

print("Python Gaussian blur completed.")
print("Output:", output_path)
print("Image dimensions:", width, "x", height)
