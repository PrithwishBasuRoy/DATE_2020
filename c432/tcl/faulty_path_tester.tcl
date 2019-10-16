#remove_design -all
source .synopsys_dc_130.setup
#set power_enable_analysis "true"
#set startpoint [list U216187/O s9[58]]
#set startpoint [list U14489/O]
set startpoint [list reg_Ein_reg[0]/Q  reg_Ein_reg[1]/Q  reg_Ein_reg[2]/Q  reg_Ein_reg[3]/Q  reg_Ein_reg[4]/Q  reg_Ein_reg[5]/Q  reg_Ein_reg[6]/Q  reg_Ein_reg[7]/Q  reg_Ein_reg[8]/Q  reg_Ain_reg[0]/Q  reg_Ain_reg[1]/Q  reg_Ain_reg[2]/Q  reg_Ain_reg[3]/Q  reg_Ain_reg[4]/Q  reg_Ain_reg[5]/Q  reg_Ain_reg[6]/Q  reg_Ain_reg[7]/Q  reg_Ain_reg[8]/Q  reg_Bin_reg[0]/Q  reg_Bin_reg[1]/Q  reg_Bin_reg[2]/Q  reg_Bin_reg[3]/Q  reg_Bin_reg[4]/Q  reg_Bin_reg[5]/Q  reg_Bin_reg[6]/Q  reg_Bin_reg[7]/Q  reg_Bin_reg[8]/Q  reg_Cin_reg[0]/Q  reg_Cin_reg[1]/Q  reg_Cin_reg[2]/Q  reg_Cin_reg[3]/Q  reg_Cin_reg[4]/Q  reg_Cin_reg[5]/Q  reg_Cin_reg[6]/Q  reg_Cin_reg[7]/Q  reg_Cin_reg[8]/Q ]
set endpoint [list reg_PA_reg/D reg_PB_reg/D reg_PC_reg/D reg_Chan_out_reg[0]/D reg_Chan_out_reg[1]/D reg_Chan_out_reg[2]/D reg_Chan_out_reg[3]/D] 
read_verilog "./Ckt_432_synthesized.v"
current_design "TopLevel432"
link
source ./block.sdc
#report_timing -max_paths 100000 -from ${startpoint} -to ${endpoint} > reports_test/test_path_fault_verifier
report_timing -max_paths 100000 -from ${startpoint} -to ${endpoint}  > reports/all_paths_in_out
exit 
