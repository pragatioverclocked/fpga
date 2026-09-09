module pixel_passthrough (
    input  wire [23:0] pixel_in,
    output wire [23:0] pixel_out
);

    assign pixel_out = pixel_in;

endmodule