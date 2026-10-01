
import os
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")

# Load Python and Verilog outputs
PYTHON_IMAGE = os.path.join(RESULTS_DIR, "lena_python_mean.png")
VERILOG_IMAGE = os.path.join(RESULTS_DIR, "lena_verilog_mean.png")

python_img = np.array(Image.open(PYTHON_IMAGE).convert("RGB"), dtype=np.uint8)
verilog_img = np.array(Image.open(VERILOG_IMAGE).convert("RGB"), dtype=np.uint8)

if python_img.shape != verilog_img.shape:
    raise ValueError("Image dimensions do not match!")

# Calculate metrics
diff = np.abs(python_img.astype(np.int16) - verilog_img.astype(np.int16))

pixel_accuracy = np.mean(np.all(python_img == verilog_img, axis=2)) * 100
mae = np.mean(diff)
mse = np.mean(diff ** 2)
max_error = np.max(diff)

if mse == 0:
    psnr = float("inf")
else:
    psnr = 10 * np.log10((255 ** 2) / mse)

ssim_value = ssim(python_img, verilog_img, data_range=255, channel_axis=-1)

# Display results
print("\n========== MEAN FILTER COMPARISON ==========")
print(f"Image dimensions : {python_img.shape[1]} x {python_img.shape[0]}")
print(f"Pixel Accuracy  : {pixel_accuracy:.2f}%")
print(f"MAE             : {mae:.6f}")
print(f"MSE             : {mse:.6f}")
print(f"Maximum Error   : {max_error}")
print(f"PSNR            : {psnr:.4f} dB")
print(f"SSIM            : {ssim_value:.6f}")

if np.array_equal(python_img, verilog_img):
    print("\nPASS: Python and Verilog outputs match exactly!")
else:
    print("\nDIFFERENCE DETECTED: Outputs do not match exactly.")

# Save metrics
metrics_file = os.path.join(RESULTS_DIR, "comparison_metrics.txt")

with open(metrics_file, "w") as f:
    f.write("3x3 Mean Filter - Comparison Results\n")
    f.write("-----------------------------------\n")
    f.write(f"Pixel Accuracy: {pixel_accuracy:.2f}%\n")
    f.write(f"MAE: {mae:.6f}\n")
    f.write(f"MSE: {mse:.6f}\n")
    f.write(f"Maximum Error: {max_error}\n")
    f.write(f"PSNR: {psnr:.4f} dB\n")
    f.write(f"SSIM: {ssim_value:.6f}\n")

print(f"\nMetrics saved to: {metrics_file}")
