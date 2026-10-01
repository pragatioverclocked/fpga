
`timescale 1ns/1ps

module sobel_edge_image;

    parameter WIDTH = 512;
    parameter HEIGHT = 512;
    parameter N = WIDTH * HEIGHT;

    reg [23:0] input_mem [0:N-1];
    reg [7:0] gray_mem [0:N-1];
    reg [7:0] output_mem [0:N-1];

    integer x, y, i, idx;
    integer gx, gy, magnitude;
    integer output_file;

    reg [7:0] R, G, B;

    initial begin

        $readmemh("test_vectors/lena_rgb_input.hex", input_mem);

        output_file = $fopen("results/lena_sobel_output.hex", "w");

        if (output_file == 0) begin
            $display("ERROR: Cannot open output file.");
            $finish;
        end

        // RGB to grayscale
        for (i = 0; i < N; i = i + 1) begin

            R = input_mem[i][23:16];
            G = input_mem[i][15:8];
            B = input_mem[i][7:0];

            gray_mem[i] = (77*R + 150*G + 29*B + 128) >> 8;

            output_mem[i] = 8'd0;

        end

        // Sobel edge detection
        for (y = 1; y < HEIGHT-1; y = y + 1) begin
            for (x = 1; x < WIDTH-1; x = x + 1) begin

                gx = 0;
                gy = 0;

                // Sobel X
                gx =
                    -gray_mem[(y-1)*WIDTH + (x-1)]
                    +gray_mem[(y-1)*WIDTH + (x+1)]
                    -2*gray_mem[y*WIDTH + (x-1)]
                    +2*gray_mem[y*WIDTH + (x+1)]
                    -gray_mem[(y+1)*WIDTH + (x-1)]
                    +gray_mem[(y+1)*WIDTH + (x+1)];

                // Sobel Y
                gy =
                    -gray_mem[(y-1)*WIDTH + (x-1)]
                    -2*gray_mem[(y-1)*WIDTH + x]
                    -gray_mem[(y-1)*WIDTH + (x+1)]
                    +gray_mem[(y+1)*WIDTH + (x-1)]
                    +2*gray_mem[(y+1)*WIDTH + x]
                    +gray_mem[(y+1)*WIDTH + (x+1)];

                magnitude = (gx < 0 ? -gx : gx)
                          + (gy < 0 ? -gy : gy);

                idx = y*WIDTH + x;

                if (magnitude > 255)
                    output_mem[idx] = 8'd255;
                else
                    output_mem[idx] = magnitude;

            end
        end

        // Write output HEX
        for (i = 0; i < N; i = i + 1)
            $fwrite(output_file, "%02h\n", output_mem[i]);

        $fclose(output_file);

        $display("SOBEL EDGE DETECTION COMPLETE");
        $finish;

    end

endmodule
