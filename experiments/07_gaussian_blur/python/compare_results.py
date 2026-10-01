
import os
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, "results")

python_img = np.array(
    Image.open(os.path.join(RESULTS_DIR, "lena_python_gaussian.png")).convert("RGB"),
    dtype=np.float64
)

verilog_img = np.array(
    Image.open(os.path.join(RESULTS_DIR, "lena_verilog_gaussian.png")).convert("RGB"),
    dtype=np.float64
)

diff = np.abs(python_img - verilog_img)

mae = np.mean(diff)
mse = np.mean(diff ** 2)
max_error = np.max(diff)
accuracy = np.mean(python_img == verilog_img) * 100

if mse == 0:
    psnr = float("inf")
else:
    psnr = 10 * np.log10((255 ** 2) / mse)

ssim_value = ssim(
    python_img.astype(np.uint8),
    verilog_img.astype(np.uint8),
    channel_axis=2,
    data_range=255
)

print("\n--- Gaussian Blur Comparison ---")
print(f"Pixel Accuracy : {accuracy:.2f}%")
print(f"MAE            : {mae:.6f}")
print(f"MSE            : {mse:.6f}")
print(f"Maximum Error  : {max_error}")
print(f"PSNR           : {psnr:.4f} dB")
print(f"SSIM           : {ssim_value:.6f}")

if np.array_equal(python_img, verilog_img):
    print("\nMATCH: Python and Verilog outputs are identical.")
else:
    print("\nDIFFERENCE DETECTED.")
