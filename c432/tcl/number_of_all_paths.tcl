#remove_design -all
source .synopsys_dc_130.setup
read_verilog "./Ckt_432_synthesized.v"
#read_verilog "./CLEFIA_altered_13_09_01.v"
#read_verilog "./AES_Composite_enc_synthesized.v"
current_design "TopLevel432"
link
source ./block.sdc
report_timing -path full > reports/all_paths 
report_timing -max_paths 10000 > reports/all_critical_paths_old_lib
exit 
