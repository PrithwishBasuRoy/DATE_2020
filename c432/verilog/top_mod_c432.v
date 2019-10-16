module TopLevel432 (E_in, A_in, B_in, C_in, PA_out, PB_out, PC_out, Chan_out,clk);

  input[8:0]	E_in, A_in, B_in, C_in;
  output     	PA_out, PB_out, PC_out;
  output[3:0]   Chan_out;
  reg [8:0]     reg_Ein, reg_Ain, reg_Bin, reg_Cin;
  reg 			reg_PA,reg_PB,reg_PC;
  reg [3:0]		reg_Chan_out;
  input clk;

  wire [8:0]    E, A, B, C;
  wire [8:0] 	X1, X2, I;
  wire 			PA,PB,PC;
  wire [3:0]	Chan;

  PriorityA M1(E, A, PA, X1);
  PriorityB M2(E, X1, B, PB, X2);
  PriorityC M3(E, X1, X2, C, PC);
  EncodeChan M4(E, A, B, C, PA, PB, PC, I);
  DecodeChan M5(I, Chan);

  always @ (posedge clk)
  begin
  		reg_Ein <= E_in;
  		reg_Ain <= A_in;
  		reg_Bin <= B_in;
  		reg_Cin <= C_in;
  		
  		reg_PA  <= PA;
  		reg_PB  <= PB;
  		reg_PC  <= PC;
  		reg_Chan_out <= Chan;

  end

  assign E = reg_Ein;
  assign A = reg_Ain;
  assign B = reg_Bin;
  assign C = reg_Cin;

  assign PA_out = reg_PA;
  assign PB_out = reg_PB;
  assign PC_out = reg_PC;
  assign Chan_out = reg_Chan_out;



endmodule /* TopLevel432 */