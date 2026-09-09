# Experiment 1 — Pixel Inversion

## Aim
To perform pixel-wise color inversion on an RGB image using Python and Verilog.

## Input
- RGB image
- 8 bits for R, G and B
- Total: 24 bits per pixel

## Operation

R_out = 255 - R_in
G_out = 255 - G_in
B_out = 255 - B_in

## Workflow

Image
→ Python inversion
→ Verilog inversion
→ Compare outputs

## Tools
- Python
- NumPy
- Pillow
- Verilog
- Icarus Verilog

## Result

Python and Verilog produced identical inverted images.

## Metrics
- Pixel Accuracy: 100%
- MAE: 0
- MSE: 0
- Maximum Error: 0
- PSNR: Infinity
- SSIM: 1.0

## Conclusion
Pixel inversion was successfully implemented and verified in Python and Verilog.