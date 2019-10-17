//`include "Ckt_432_synthesized.v"
module tb_Circuit432 ();

  reg [8:0]    Ein,Ain,Bin,Cin;
  wire          PA, PB, PC;
  wire [3:0]    Chan;
  reg clk,clk1,clk2,select;
  
  TopLevel432 mod1(.E_in(Ein), .A_in(Ain), .B_in(Bin), .C_in(Cin), .PA_out(PA), .PB_out(PB), .PC_out(PC), .Chan_out(Chan),.clk(clk));
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
    Bin<= 9'b000000010;
    Cin<= 9'b000000010;


  end  

  always begin
  #43 clk1<=~clk1;

  end

  always begin
  #42.5 clk2<=~clk2;

  end


  assign clk = select?clk1:clk2;
  
  always 
  begin 
  #86 Ein<= 9'b111111101;
    Ain<= 9'b000000010;
    Bin<= 9'b000000010;
    Cin<= 9'b000000010;
  #86 Ein<= 9'b000000000;
    Ain<= 9'b000000010;
    Bin<= 9'b000000001;
    Cin<= 9'b000000000;
  
  #86 Ein<= 9'b000111100;
    Ain<= 9'b000000100;
    Bin<= 9'b000000011;
    Cin<= 9'b000000111;

  #86 Ein<= 9'b000000100;
    Ain<= 9'b000000100;
    Bin<= 9'b000000011;
    Cin<= 9'b000000100;

  #86 Ein<= 9'b000000011;
    Ain<= 9'b000000111;
    Bin<= 9'b000000100;
    Cin<= 9'b000000100;

   select<=0;
  #85 select <=1;
 	
  #1 Ein<= 9'b000011011;
    Ain<= 9'b000000111;
    Bin<= 9'b000000100;
    Cin<= 9'b000000100;

  #86 Ein<= 9'b000010011;
    Ain<= 9'b000000111;
    Bin<= 9'b000000100;
    Cin<= 9'b000000100;


  #86 Ein<= 9'b000110011;
    Ain<= 9'b000000111;
    Bin<= 9'b000000100;
    Cin<= 9'b000000100;


  #500 $finish();    
  end
  

endmodule /* Circuit432 */
