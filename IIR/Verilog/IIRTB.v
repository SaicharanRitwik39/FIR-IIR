module IIRfilter_tb;
  reg clk,rst;
  reg [3:0] a,x;
  wire [3:0] y;
  IIRfilter IIR1(.clk(clk),.rst(rst),.a(a),.x(x),.y(y));
  initial begin
    clk = 0;
  end
  always
    #5 clk=~clk;
  intitial begin
    rst = 1;
    a = 4'd2;
    x = 4'd1;
    #10 rst = 0;
    a = 4'd2;
    x = 4'd1;
  end
endmodule
