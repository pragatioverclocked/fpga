
import os
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")

python_img = np.array(
    Image.open(os.path.join(RESULTS_DIR, "lena_python_sobel.png")).convert("L"),
    dtype=np.uint8
)

verilog_img = np.array(
    Image.open(os.path.join(RESULTS_DIR, "lena_verilog_sobel.png")).convert("L"),
    dtype=np.uint8
)

if python_img.shape != verilog_img.shape:
    raise ValueError("Image dimensions do not match!")

diff = np.abs(python_img.astype(np.int16) - verilog_img.astype(np.int16))

accuracy = np.mean(python_img == verilog_img) * 100
mae = np.mean(diff)
mse = np.mean(diff ** 2)
max_error = np.max(diff)

psnr = float("inf") if mse == 0 else 10 * np.log10(255**2 / mse)
ssim_value = ssim(python_img, verilog_img, data_range=255)

print("\n========== SOBEL COMPARISON ==========")
print(f"Pixel Accuracy : {accuracy:.2f}%")
print(f"MAE            : {mae:.6f}")
print(f"MSE            : {mse:.6f}")
print(f"Maximum Error  : {max_error}")
print(f"PSNR           : {psnr:.4f} dB")
print(f"SSIM           : {ssim_value:.6f}")

if np.array_equal(python_img, verilog_img):
    print("\nPASS: Python and Verilog outputs match exactly!")
else:
    print("\nDIFFERENCE DETECTED")

with open(os.path.join(RESULTS_DIR, "comparison_metrics.txt"), "w") as f:
    f.write("Sobel Edge Detection - Comparison Results\n")
    f.write(f"Pixel Accuracy: {accuracy:.2f}%\n")
    f.write(f"MAE: {mae:.6f}\n")
    f.write(f"MSE: {mse:.6f}\n")
    f.write(f"Maximum Error: {max_error}\n")
    f.write(f"PSNR: {psnr:.4f} dB\n")
    f.write(f"SSIM: {ssim_value:.6f}\n")
