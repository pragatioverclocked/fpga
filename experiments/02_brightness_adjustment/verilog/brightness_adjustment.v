module brightness_adjustment #(
    parameter integer K = 50
)(
    input  wire [23:0] pixel_in,
    output wire [23:0] pixel_out
);

    // RGB888 input
    wire [7:0] r_in;
    wire [7:0] g_in;
    wire [7:0] b_in;

    // 9-bit temporary values
    // Needed because 255 + 50 = 305
    wire [8:0] r_temp;
    wire [8:0] g_temp;
    wire [8:0] b_temp;

    // Final 8-bit RGB values
    wire [7:0] r_out;
    wire [7:0] g_out;
    wire [7:0] b_out;

    // Extract RGB channels
    assign r_in = pixel_in[23:16];
    assign g_in = pixel_in[15:8];
    assign b_in = pixel_in[7:0];

    // Add brightness
    assign r_temp = r_in + K;
    assign g_temp = g_in + K;
    assign b_temp = b_in + K;

    // Saturation at 255
    assign r_out = (r_temp > 9'd255) ? 8'd255 : r_temp[7:0];
    assign g_out = (g_temp > 9'd255) ? 8'd255 : g_temp[7:0];
    assign b_out = (b_temp > 9'd255) ? 8'd255 : b_temp[7:0];

    // Recombine RGB
    assign pixel_out = {
        r_out,
        g_out,
        b_out
    };

endmodule