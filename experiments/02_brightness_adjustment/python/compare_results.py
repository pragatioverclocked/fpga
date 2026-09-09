import os
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

PYTHON_IMAGE = os.path.join(
    PROJECT_ROOT, "results", "lena_python_brightness.png"
)

VERILOG_IMAGE = os.path.join(
    PROJECT_ROOT, "results", "lena_verilog_brightness.png"
)

python_img = np.array(Image.open(PYTHON_IMAGE).convert("RGB"), dtype=np.float64)
verilog_img = np.array(Image.open(VERILOG_IMAGE).convert("RGB"), dtype=np.float64)

diff = np.abs(python_img - verilog_img)

mae = np.mean(diff)
mse = np.mean((python_img - verilog_img) ** 2)
max_error = np.max(diff)

if mse == 0:
    psnr = float("inf")
else:
    psnr = 10 * np.log10((255 ** 2) / mse)

ssim_value = ssim(
    python_img,
    verilog_img,
    channel_axis=2,
    data_range=255
)

pixel_accuracy = np.mean(
    np.all(python_img == verilog_img, axis=2)
) * 100

print("========================================")
print("   EXPERIMENT 2 - RESULT COMPARISON")
print("========================================")
print(f"Image Size      : {python_img.shape[1]} x {python_img.shape[0]}")
print("----------------------------------------")
print(f"Pixel Accuracy  : {pixel_accuracy:.2f}%")
print(f"MAE             : {mae:.6f}")
print(f"MSE             : {mse:.6f}")
print(f"Maximum Error   : {max_error:.6f}")
print(f"PSNR            : {psnr}")
print(f"SSIM            : {ssim_value:.6f}")
print("----------------------------------------")

if np.array_equal(python_img, verilog_img):
    print("RESULT          : PASS")
else:
    print("RESULT          : FAIL")

print("========================================")