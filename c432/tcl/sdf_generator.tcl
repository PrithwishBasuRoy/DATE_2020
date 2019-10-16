# things to do 
# create folder for each benchmark circuit let it be ckt1
# inside ckt1 create folder called reports
# copy these three files .synopsys_dc_130.setup, synth.tcl & block.sdc * Note: verilog file also should be inside ckt1
# rename aes_128 to the name of the random verilog file that is created
# synthesize once with clock at 0 in block.sdc & max_delay 0.0 note the delay value in reports/modulename_timing.txt
# replace clock with magnitude value and set period accordingly and max_delay to the same value and resynthesize
# run using the following command  1. source /tools/setup.sh 2. dc_shell -f synth.tcl


remove_design -all 
source .synopsys_dc_130.setup
set myFiles [list Ckt_432_synthesized.v]; # replace with verilog files that you want to synthesize
set myTop TopLevel432; # check the name of the module in the verilog file that you are synthesizing and replace it here
analyze -library WORK -format verilog ${myFiles} > reports/Ckt_432_report.txt 
elaborate ${myTop} -architecture verilog -library DEFAULT >> reports/Ckt_432_report.txt 
current_design ${myTop} >> reports/Ckt_432_report.txt 
link
source ./block.sdc 
#ungroup -all -flatten 
#set_max_area 0
set_max_delay 0.86  -from [all_inputs] -to [all_outputs]
write_sdf Ckt_432.sdf > reports/Ckt_432_sdf.txt
exit



