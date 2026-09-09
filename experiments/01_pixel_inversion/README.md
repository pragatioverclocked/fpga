# Experiment 01 — Pixel Inversion

## Objective

Implement pixel inversion in Python and Verilog and verify that both produce identical results.

## Equation

Y = 255 - X

## Python

OpenCV/NumPy reference implementation.

## Verilog

8-bit combinational RTL implementation.

## Verification

Python output compared against Verilog output.

## Results

Pixel Accuracy: 100%
MAE: 0
MSE: 0
Max Error: 0
SSIM: 1.0

## FPGA

LUT: ...
FF: ...
BRAM: ...
DSP: ...
Fmax: ...
Latency: ...

## Conclusion

The Verilog implementation reproduced the Python
reference output exactly.