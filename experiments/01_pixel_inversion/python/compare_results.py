import os
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

PYTHON_IMAGE = os.path.join(
    PROJECT_ROOT,
    "results",
    "lena_python_inverted.png"
)

VERILOG_IMAGE = os.path.join(
    PROJECT_ROOT,
    "results",
    "lena_verilog_inverted.png"
)


# Load images
python_img = np.array(
    Image.open(PYTHON_IMAGE).convert("RGB"),
    dtype=np.uint8
)

verilog_img = np.array(
    Image.open(VERILOG_IMAGE).convert("RGB"),
    dtype=np.uint8
)


print("========================================")
print("     PYTHON vs VERILOG COMPARISON")
print("========================================")

print(f"Python image  : {python_img.shape[1]} x {python_img.shape[0]}")
print(f"Verilog image : {verilog_img.shape[1]} x {verilog_img.shape[0]}")

# Check dimensions
if python_img.shape != verilog_img.shape:

    print("FAIL: Image dimensions do not match.")

    exit()


# Convert to signed integer
python_data = python_img.astype(np.int16)
verilog_data = verilog_img.astype(np.int16)

# Absolute pixel difference
difference = np.abs(
    python_data - verilog_data
)

# Metrics
max_error = np.max(difference)

mae = np.mean(difference)

mse = np.mean(
    difference ** 2
)

# Pixel accuracy
matching_pixels = np.all(
    python_img == verilog_img,
    axis=2
)

matching_count = np.sum(matching_pixels)

total_pixels = python_img.shape[0] * python_img.shape[1]

accuracy = (
    matching_count / total_pixels
) * 100


# PSNR
if mse == 0:
    psnr = float("inf")
else:
    psnr = 10 * np.log10(
        (255 ** 2) / mse
    )


# SSIM
ssim_value = ssim(
    python_img,
    verilog_img,
    channel_axis=2,
    data_range=255
)


print("----------------------------------------")
print(f"Total pixels    : {total_pixels}")
print(f"Matching pixels : {matching_count}")
print(f"Pixel accuracy  : {accuracy:.4f}%")
print(f"MAE             : {mae:.6f}")
print(f"MSE             : {mse:.6f}")
print(f"Maximum error   : {max_error}")

if np.isinf(psnr):
    print("PSNR            : Infinity")
else:
    print(f"PSNR            : {psnr:.6f} dB")

print(f"SSIM            : {ssim_value:.6f}")
print("----------------------------------------")


# Final result
if np.array_equal(
    python_img,
    verilog_img
):

    print("RESULT: PASS")
    print("Python and Verilog images are IDENTICAL.")

else:

    print("RESULT: FAIL")
    print("Python and Verilog images are DIFFERENT.")


print("========================================")