`timescale 1ns/1ps

module tb_rgb_to_grayscale_fixed;

    parameter WIDTH  = 512;
    parameter HEIGHT = 512;
    parameter N      = WIDTH * HEIGHT;

    reg [23:0] input_mem [0:N-1];

    reg [23:0] pixel_in;
    wire [7:0] gray_out;

    integer i;
    integer out_file;

    rgb_to_grayscale_fixed dut (
        .pixel_in(pixel_in),
        .gray_out(gray_out)
    );

    initial begin

        $display("========================================");
        $display("   EXPERIMENT 3 - RGB TO GRAYSCALE");
        $display("========================================");

        $readmemh(
            "test_vectors/lena_rgb_input.mem",
            input_mem
        );

        out_file = $fopen(
            "test_vectors/lena_gray_verilog_fixed.mem",
            "w"
        );

        if (out_file == 0) begin
            $display("ERROR: Cannot open output file.");
            $finish;
        end

        pixel_in = 24'h000000;

        for (i = 0; i < N; i = i + 1) begin

            pixel_in = input_mem[i];

            #1;

            $fwrite(
                out_file,
                "%02h\n",
                gray_out
            );

        end

        $fclose(out_file);

        $display("----------------------------------------");
        $display("Resolution : %0d x %0d", WIDTH, HEIGHT);
        $display("Pixels     : %0d", N);
        $display("Method     : Fixed-point");
        $display("Output     : test_vectors/lena_gray_verilog_fixed.mem");
        $display("----------------------------------------");
        $display("SIMULATION COMPLETE");
        $display("========================================");

        $finish;

    end

endmodule