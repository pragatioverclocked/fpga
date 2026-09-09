# Experiment 3 — RGB to Grayscale Conversion

## Aim

To convert a 24-bit RGB image into an 8-bit grayscale image using Verilog RTL and compare the hardware implementation with a Python reference implementation.

This experiment also establishes the basis for comparing fixed-point and floating-point implementations for FPGA-based image processing.

---

## Objective

The objectives of this experiment are:

1. Convert RGB888 pixels into grayscale pixels.
2. Implement the grayscale operation using Verilog RTL.
3. Generate a reference output using Python.
4. Compare Python and Verilog outputs using image-quality metrics.
5. Implement a floating-point version using Vivado Floating-Point IP.
6. Compare fixed-point and floating-point implementations in terms of:
   - Image accuracy
   - LUT utilization
   - Flip-Flop utilization
   - DSP utilization
   - BRAM utilization
   - Timing / maximum frequency

---

## Input Image

- Image: `lena_rgb_input.png`
- Resolution: 512 × 512
- Color format: RGB888
- Bits per pixel: 24

Each pixel contains:

```text
R[7:0] | G[7:0] | B[7:0]
   8   |   8   |   8 bits