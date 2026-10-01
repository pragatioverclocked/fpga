
`timescale 1ns/1ps

module mean_filter_image;

    parameter WIDTH = 512;
    parameter HEIGHT = 512;
    parameter N = WIDTH * HEIGHT;

    reg [23:0] input_mem [0:N-1];
    reg [23:0] output_mem [0:N-1];

    integer x, y, i;
    integer sum_r, sum_g, sum_b;
    integer idx;
    integer output_file;
    reg [7:0] avg_r, avg_g, avg_b;

    initial begin
        $readmemh("test_vectors/lena_rgb_input.hex", input_mem);

        output_file = $fopen("results/lena_mean_output.hex", "w");

        if (output_file == 0) begin
            $display("ERROR: Cannot open output file.");
            $finish;
        end

        // Preserve border pixels
        for (i = 0; i < N; i = i + 1)
            output_mem[i] = input_mem[i];

        // Apply 3x3 mean filter
        for (y = 1; y < HEIGHT-1; y = y + 1) begin
            for (x = 1; x < WIDTH-1; x = x + 1) begin

                sum_r = 0;
                sum_g = 0;
                sum_b = 0;

                for (integer dy = -1; dy <= 1; dy = dy + 1) begin
                    for (integer dx = -1; dx <= 1; dx = dx + 1) begin

                        idx = (y + dy) * WIDTH + (x + dx);

                        sum_r = sum_r + input_mem[idx][23:16];
                        sum_g = sum_g + input_mem[idx][15:8];
                        sum_b = sum_b + input_mem[idx][7:0];

                    end
                end

                idx = y * WIDTH + x;

                avg_r = sum_r / 9;
avg_g = sum_g / 9;
avg_b = sum_b / 9;

output_mem[idx] = {avg_r, avg_g, avg_b};

            end
        end

        for (i = 0; i < N; i = i + 1)
            $fwrite(output_file, "%06h\n", output_mem[i]);

        $fclose(output_file);

        $display("3x3 MEAN FILTER COMPLETE");
        $finish;
    end

endmodule
