import numpy as np

INPUT_MEM = "test_vectors/lena_rgb_input.mem"
OUTPUT_MEM = "test_vectors/lena_rgb_output.mem"


def read_mem_file(filename):
    """Read 24-bit hexadecimal pixel values from a .mem file."""
    
    with open(filename, "r") as f:
        values = [
            int(line.strip(), 16)
            for line in f
            if line.strip()
        ]

    return np.array(values, dtype=np.uint32)


input_pixels = read_mem_file(INPUT_MEM)
output_pixels = read_mem_file(OUTPUT_MEM)


print("========================================")
print("       VERILOG OUTPUT VERIFICATION")
print("========================================")

print(f"Input pixels  : {len(input_pixels)}")
print(f"Output pixels : {len(output_pixels)}")


if len(input_pixels) != len(output_pixels):

    print("FAIL: Pixel count mismatch.")

    exit()


difference = np.abs(
    input_pixels.astype(np.int64)
    - output_pixels.astype(np.int64)
)


max_error = difference.max()
mae = difference.mean()
mse = np.mean(difference ** 2)

matching_pixels = np.sum(
    input_pixels == output_pixels
)

accuracy = (
    matching_pixels / len(input_pixels)
) * 100


print("----------------------------------------")
print(f"Matching pixels : {matching_pixels}")
print(f"Pixel accuracy  : {accuracy:.2f}%")
print(f"MAE             : {mae:.6f}")
print(f"MSE             : {mse:.6f}")
print(f"Maximum error   : {max_error}")
print("----------------------------------------")


if np.array_equal(input_pixels, output_pixels):

    print("RESULT: PASS")
    print("Python and Verilog outputs are IDENTICAL.")

else:

    print("RESULT: FAIL")
    print("Python and Verilog outputs are DIFFERENT.")


print("========================================")