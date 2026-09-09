# Experiment 2 — Brightness Adjustment

## Aim

To increase the brightness of an RGB image using Python and Verilog and verify that both implementations produce identical results.

---

## Input

- Image: `lena_rgb_input.png`
- Resolution: 512 × 512
- Color format: RGB888
- Bits per pixel: 24
- R = 8 bits
- G = 8 bits
- B = 8 bits

---

## Operation

A constant brightness value is added to each RGB channel.

For this experiment:

```text
K = +50