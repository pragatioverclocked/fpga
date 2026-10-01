import os
import sys
import numpy as np
from PIL import Image


def hex_to_png(input_hex, output_png, width, height, mode):
    # Read HEX values
    with open(input_hex, "r") as f:
        pixels = [int(line.strip(), 16) for line in f if line.strip()]

    expected_pixels = width * height

    if len(pixels) != expected_pixels:
        raise ValueError(
            f"Expected {expected_pixels} pixels, but found {len(pixels)}"
        )

    # Convert based on image type
    if mode.lower() == "gray":
        image_array = np.array(pixels, dtype=np.uint8)
        image_array = image_array.reshape((height, width))
        image = Image.fromarray(image_array, mode="L")

    elif mode.lower() == "rgb":
        image_array = np.array(pixels, dtype=np.uint32)

        R = (image_array >> 16) & 0xFF
        G = (image_array >> 8) & 0xFF
        B = image_array & 0xFF

        rgb_array = np.stack((R, G, B), axis=-1)
        rgb_array = rgb_array.astype(np.uint8)
        rgb_array = rgb_array.reshape((height, width, 3))

        image = Image.fromarray(rgb_array, mode="RGB")

    else:
        raise ValueError("Mode must be 'gray' or 'rgb'")

    # Create output directory if needed
    os.makedirs(os.path.dirname(output_png) or ".", exist_ok=True)

    # Save PNG
    image.save(output_png)

    print("Conversion successful!")
    print(f"Input HEX : {input_hex}")
    print(f"Output PNG: {output_png}")
    print(f"Resolution: {width} x {height}")
    print(f"Mode      : {mode}")


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            "Usage: python hex_to_png.py "
            "<input.hex> <output.png> <width> <height> <gray/rgb>"
        )
        sys.exit(1)

    input_hex = sys.argv[1]
    output_png = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    mode = sys.argv[5]

    hex_to_png(input_hex, output_png, width, height, mode)