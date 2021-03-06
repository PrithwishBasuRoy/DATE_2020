
module EncodeChan(E, A, B, C, PA, PB, PC, I);

  input[8:0] E, A, B, C; 
  input PA, PB, PC;
  output[8:0] I;

  wire [8:0] APA, BPB, CPC;

  nand APA0(APA[0], A[0], PA);
  nand APA1(APA[1], A[1], PA);
  nand APA2(APA[2], A[2], PA);
  nand APA3(APA[3], A[3], PA);
  nand APA4(APA[4], A[4], PA);
  nand APA5(APA[5], A[5], PA);
  nand APA6(APA[6], A[6], PA);
  nand APA7(APA[7], A[7], PA);
  nand APA8(APA[8], A[8], PA);

  nand BPB0(BPB[0], B[0], PB);
  nand BPB1(BPB[1], B[1], PB);
  nand BPB2(BPB[2], B[2], PB);
  nand BPB3(BPB[3], B[3], PB);
  nand BPB4(BPB[4], B[4], PB);
  nand BPB5(BPB[5], B[5], PB);
  nand BPB6(BPB[6], B[6], PB);
  nand BPB7(BPB[7], B[7], PB);
  nand BPB8(BPB[8], B[8], PB);
 
  nand CPC0(CPC[0], C[0], PC);
  nand CPC1(CPC[1], C[1], PC);
  nand CPC2(CPC[2], C[2], PC);
  nand CPC3(CPC[3], C[3], PC);
  nand CPC4(CPC[4], C[4], PC);
  nand CPC5(CPC[5], C[5], PC);
  nand CPC6(CPC[6], C[6], PC);
  nand CPC7(CPC[7], C[7], PC);
  nand CPC8(CPC[8], C[8], PC);

  nand I0(I[0], E[0], APA[0], BPB[0], CPC[0]);
  nand I1(I[1], E[1], APA[1], BPB[1], CPC[1]);
  nand I2(I[2], E[2], APA[2], BPB[2], CPC[2]);
  nand I3(I[3], E[3], APA[3], BPB[3], CPC[3]);
  nand I4(I[4], E[4], APA[4], BPB[4], CPC[4]);
  nand I5(I[5], E[5], APA[5], BPB[5], CPC[5]);
  nand I6(I[6], E[6], APA[6], BPB[6], CPC[6]);
  nand I7(I[7], E[7], APA[7], BPB[7], CPC[7]);
  nand I8(I[8], E[8], APA[8], BPB[8], CPC[8]);

endmodule /* EncodeChan */