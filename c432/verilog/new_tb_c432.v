module tb_Circuit432 ();

  reg [8:0]    Ein,Ain,Bin,Cin;
  wire          PA, PB, PC;
  wire [3:0]    Chan;
  reg clk,clk1,clk2,select;
  
  TopLevel432 mod_1(.E_in(E_in), .A_in(A_in), .B_in(B_in), .C_in(C_in), .PA_out(PA), .PB_out(PB), .PC_out(PC), .Chan_out(Chan),.clk(clk));
  initial
  begin
    $dumpfile("dump_c432.vcd");
    $dumpvars(0,tb_Circuit432);
    $monitor("time:%t,Ein:%h,Ain:%h,Bin:%h,Cin:%h,PA:%h,PB;%h,PC:%h,Chan:%h",$time,Ein,Ain,Bin,Cin,PA,PB,PC,Chan);
    

    select<=1;
    $sdf_annotate("Ckt_432.sdf",mod1);
    clk1<=1;
    clk2<=1;

    Ein<= 9'b111111111;
    Ain<= 9'b000000010;
    Bin<= 9'b000000001;
    Cin<= 9'b000000000;


  end  

  always begin
  #43 clk1<=~clk1;

  end

  always begin
  #21.5 clk1<=~clk1;

  end


  assign clk = select?clk1:clk2;


endmodule /* Circuit432 */
