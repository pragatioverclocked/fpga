`timescale 1ns/1ps

module tb_brightness_adjustment;

    parameter WIDTH  = 512;
    parameter HEIGHT = 512;
    parameter N      = WIDTH * HEIGHT;

    reg [23:0] input_mem [0:N-1];

    reg [23:0] pixel_in;
    wire [23:0] pixel_out;

    integer i;
    integer out_file;

    // Instantiate the brightness module
    brightness_adjustment #(
        .K(50)
    ) dut (
        .pixel_in(pixel_in),
        .pixel_out(pixel_out)
    );

    initial begin

        $display("========================================");
        $display("   EXPERIMENT 2 - BRIGHTNESS");
        $display("========================================");

        // Read input image pixels
        $readmemh(
            "test_vectors/lena_rgb_input.mem",
            input_mem
        );

        // Create output file
        out_file = $fopen(
            "test_vectors/lena_rgb_verilog_brightness.mem",
            "w"
        );

        if (out_file == 0) begin
            $display("ERROR: Cannot open output file.");
            $finish;
        end

        pixel_in = 24'h000000;

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
        $display("Brightness : +50");
        $display("Output     : test_vectors/lena_rgb_verilog_brightness.mem");
        $display("----------------------------------------");
        $display("SIMULATION COMPLETE");
        $display("========================================");

        $finish;

    end

endmodule