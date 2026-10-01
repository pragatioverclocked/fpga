
module gaussian_blur_image;

    parameter WIDTH = 512;
    parameter HEIGHT = 512;
    parameter N = WIDTH * HEIGHT;

    reg [23:0] input_mem [0:N-1];
    reg [23:0] output_mem [0:N-1];

    integer x, y, idx;
    integer r_sum, g_sum, b_sum;
    integer kx, ky;
    integer pixel_idx;

    integer r, g, b;
    integer r_blur, g_blur, b_blur;

    initial begin

        // Read input RGB image
        $readmemh("test_vectors/lena_rgb_input.hex", input_mem);

        // Copy input image to preserve border pixels
        for (idx = 0; idx < N; idx = idx + 1) begin
            output_mem[idx] = input_mem[idx];
        end

        // Apply 3x3 Gaussian blur
        for (y = 1; y < HEIGHT-1; y = y + 1) begin
            for (x = 1; x < WIDTH-1; x = x + 1) begin

                r_sum = 0;
                g_sum = 0;
                b_sum = 0;

                // Process 3x3 neighborhood
                for (ky = -1; ky <= 1; ky = ky + 1) begin
                    for (kx = -1; kx <= 1; kx = kx + 1) begin

                        pixel_idx = (y + ky) * WIDTH + (x + kx);

                        r = input_mem[pixel_idx][23:16];
                        g = input_mem[pixel_idx][15:8];
                        b = input_mem[pixel_idx][7:0];

                        // Center pixel: weight 4
                        if (ky == 0 && kx == 0) begin
                            r_sum = r_sum + 4*r;
                            g_sum = g_sum + 4*g;
                            b_sum = b_sum + 4*b;
                        end

                        // Horizontal and vertical neighbors: weight 2
                        else if (ky == 0 || kx == 0) begin
                            r_sum = r_sum + 2*r;
                            g_sum = g_sum + 2*g;
                            b_sum = b_sum + 2*b;
                        end

                        // Diagonal neighbors: weight 1
                        else begin
                            r_sum = r_sum + r;
                            g_sum = g_sum + g;
                            b_sum = b_sum + b;
                        end

                    end
                end

                // Divide by 16 with rounding
                r_blur = (r_sum + 8) >> 4;
                g_blur = (g_sum + 8) >> 4;
                b_blur = (b_sum + 8) >> 4;

                // Store blurred RGB pixel
                output_mem[y*WIDTH+x] = {
                    r_blur[7:0],
                    g_blur[7:0],
                    b_blur[7:0]
                };

            end
        end

        // Write output HEX file
        begin
            integer file;

            file = $fopen("results/lena_gaussian_output.hex", "w");

            if (file == 0) begin
                $display("ERROR: Could not open output file.");
                $finish;
            end

            for (idx = 0; idx < N; idx = idx + 1) begin
                $fwrite(file, "%06h\n", output_mem[idx]);
            end

            $fclose(file);
        end

        $display("Gaussian blur completed.");
        $finish;

    end

endmodule
