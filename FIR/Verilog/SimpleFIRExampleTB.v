`timescale 1ns / 1ps

module tb;

    // Inputs
    reg clk;
    reg signed [7:0] Xin;

    // Outputs
    wire signed [15:0] Yout;
  
    initial begin
    $dumpfile("dump.vcd");
    $dumpvars(0,tb);
    end

    // Instantiate the Unit Under Test (UUT)
    fir_4tap uut (
        .clk(clk), 
        .Xin(Xin), 
        .Yout(Yout)
    );
    
    //Generate a clock with 10 ns clock period.
    initial clk = 0;
    always #5 clk =~clk;

    // Testbench behavior
    initial begin
        // Apply input values with delays
        Xin = 0;  #40;
        Xin = -3; #50;
        Xin = 1;  #60;
        Xin = 0;  #70;
        Xin = -2; #80;
        Xin = -1; #90;
        Xin = 4;  #100;
        Xin = -5; #110;
        Xin = 6;  #120;
        Xin = 0;  #130;

        #1000; // Add a delay to continue simulation for 1000 time units
        $finish; // End the simulation
    end
      
endmodule
