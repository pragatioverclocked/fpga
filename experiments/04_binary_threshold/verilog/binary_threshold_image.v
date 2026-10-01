
`timescale 1ns/1ps

module binary_threshold_image;

    parameter integer WIDTH = 512;
    parameter integer HEIGHT = 512;
    parameter integer N = WIDTH * HEIGHT;
    parameter integer THRESHOLD = 128;

    // Input and output image memories
    reg [23:0] input_mem [0:N-1];
    reg [7:0] output_mem [0:N-1];

    // RGB components
    reg [7:0] R, G, B;

    // Grayscale calculation
    integer weighted_sum;
    integer gray_value;

    integer i;
    integer output_file;

    initial begin

        $display("========================================");
        $display(" EXPERIMENT 4 - BINARY THRESHOLDING");
        $display("========================================");

        // Read input image
        $readmemh(
            "test_vectors/lena_rgb_input.hex",
            input_mem
        );

        // Open output file
        output_file = $fopen(
            "results/lena_binary_output.hex",
            "w"
        );

        if (output_file == 0) begin
            $display("ERROR: Cannot open output file.");
            $finish;
        end

        // Process every pixel
        for (i = 0; i < N; i = i + 1) begin

            // Extract RGB
            R = input_mem[i][23:16];
            G = input_mem[i][15:8];
            B = input_mem[i][7:0];

            // Fixed-point grayscale conversion
            weighted_sum =
                  (77 * R)
                + (150 * G)
                + (29 * B);

            // Round and divide by 256
            gray_value = (weighted_sum + 128) >> 8;

            // Binary threshold
            if (gray_value >= THRESHOLD)
                output_mem[i] = 8'hFF;
            else
                output_mem[i] = 8'h00;

            // Write output pixel
            $fwrite(
                output_file,
                "%02h\n",
                output_mem[i]
            );

        end

        $fclose(output_file);

        $display("----------------------------------------");
        $display("Resolution : %0d x %0d", WIDTH, HEIGHT);
        $display("Total pixels: %0d", N);
        $display("Threshold  : %0d", THRESHOLD);
        $display("Output     : results/lena_binary_output.hex");
        $display("----------------------------------------");
        $display("PROCESSING COMPLETE");
        $display("========================================");

        $finish;

    end

endmodule
