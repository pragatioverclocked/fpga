module rgb_to_grayscale_fixed(
    input wire [23:0] pixel_in,
    output wire [7:0] gray_out
);

    wire [7:0] R;
    wire [7:0] G;
    wire [7:0] B;

    wire [15:0] weighted_sum;

    assign R = pixel_in[23:16];
    assign G = pixel_in[15:8];
    assign B = pixel_in[7:0];

    assign weighted_sum =
        (77 * R) +
        (150 * G) +
        (29 * B);

    assign gray_out = (weighted_sum + 16'd128) >> 8;

endmodule