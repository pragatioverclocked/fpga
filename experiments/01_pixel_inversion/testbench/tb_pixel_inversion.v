`timescale 1ns/1ps

module tb_pixel_inversion;

    parameter WIDTH  = 512;
    parameter HEIGHT = 512;
    parameter N      = WIDTH * HEIGHT;

    reg [23:0] input_mem [0:N-1];

    reg  [23:0] pixel_in;
    wire [23:0] pixel_out;

    integer i;
    integer out_file;

    // Instantiate the image-processing module
    pixel_inversion dut (
        .pixel_in(pixel_in),
        .pixel_out(pixel_out)
    );

    initial begin

        $display("========================================");
        $display("       EXPERIMENT 1 - PIXEL INVERSION");
        $display("========================================");

        // Load image pixels
        $readmemh(
            "test_vectors/lena_rgb_input.mem",
            input_mem
        );

        // Open output file
        out_file = $fopen(
            "test_vectors/lena_rgb_verilog_inverted.mem",
            "w"
        );

        if (out_file == 0) begin
            $display("ERROR: Cannot open output file.");
            $finish;
        end

        // Process every pixel
        for (i = 0; i < N; i = i + 1) begin

            pixel_in = input_mem[i];

            #1;

            $fwrite(
                out_file,
                "%06h\n",
                pixel_out
            );

        end

        $fclose(out_file);

        $display("----------------------------------------");
        $display("Resolution : %0d x %0d", WIDTH, HEIGHT);
        $display("Pixels     : %0d", N);
        $display("Output     : test_vectors/lena_rgb_verilog_inverted.mem");
        $display("----------------------------------------");
        $display("SIMULATION COMPLETE");
        $display("========================================");

        $finish;

    end

endmodule