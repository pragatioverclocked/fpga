module pixel_inversion (
    input  wire [23:0] pixel_in,
    output wire [23:0] pixel_out
);

    // RGB888 format
    // [23:16] = Red
    // [15:8]  = Green
    // [7:0]   = Blue

    wire [7:0] red_in;
    wire [7:0] green_in;
    wire [7:0] blue_in;

    wire [7:0] red_out;
    wire [7:0] green_out;
    wire [7:0] blue_out;

    assign red_in   = pixel_in[23:16];
    assign green_in = pixel_in[15:8];
    assign blue_in  = pixel_in[7:0];

    // Invert each color channel
    assign red_out   = 8'd255 - red_in;
    assign green_out = 8'd255 - green_in;
    assign blue_out  = 8'd255 - blue_in;

    // Reconstruct 24-bit output pixel
    assign pixel_out = {
        red_out,
        green_out,
        blue_out
    };

endmodule