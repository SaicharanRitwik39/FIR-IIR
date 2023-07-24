`timescale 1ns / 1ps

module fir_4tap(
        input clk,
        input signed [7:0] Xin,
        output reg signed [15:0] Yout
        );
    
    //Internal variables.
    wire signed   [7:0] H0,H1,H2,H3;
    wire signed   [15:0] MCM0,MCM1,MCM2,MCM3,add_out1,add_out2,add_out3;
    wire signed     [15:0] Q1,Q2,Q3;
    
//Filter coefficient initialization.
//H = [-2 -1 3 4].
    assign H0 = -2;
    assign H1 = -1;
    assign H2 = 3;
    assign H3 = 4;

//Multiple constant multiplications.
    assign MCM3 = H3*Xin;
    assign MCM2 = H2*Xin;
    assign MCM1 = H1*Xin;
    assign MCM0 = H0*Xin;

//adders
    assign add_out1 = Q1 + MCM2;
    assign add_out2 = Q2 + MCM1;
    assign add_out3 = Q3 + MCM0;    

//flipflop instantiations (for introducing a delay).
    DFF dff1 (.clk(clk),.D(MCM3),.Q(Q1));
    DFF dff2 (.clk(clk),.D(add_out1),.Q(Q2));
    DFF dff3 (.clk(clk),.D(add_out2),.Q(Q3));

//Assign the last adder output to final output.
  always@ (posedge clk)
        Yout <= add_out3;

endmodule

module DFF
       (input clk,
        input [15:0] D,
        output reg [15:0]   Q
        );
    
    always@ (posedge clk)
        Q = D;
endmodule
