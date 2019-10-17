import re 
import subprocess
import os
import matplotlib.pyplot as plt
import datetime 

initial_slack= 0.86
#present_slack=initial_slack
paths_violated=[]
for_slack=[]
now=datetime.datetime.now()
folder_path_time_stamp=str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)
	
#fc=open("Count_of_critical_non_critical_paths.txt","a")
#fc.write("Give the counts of critical and non critical paths for different value of the slack \n")
#os.system("cd reports")
os.system("mkdir critical_paths_"+folder_path_time_stamp)
fc=open("critical_paths_"+folder_path_time_stamp+"/Count_of_critical_non_critical_paths.txt","a")
#fc.write("Trying The third combination")
fc.write("Trying with lesser slacks")
#fc.write("Give the counts of critical and non critical paths for different value of the slack after changing U227195(AO12EHD) to AO12XLP \n")
#fc.write("Checking with a backup synthesized netlist  \n")
#fc.write("Give the counts of critical and non critical paths for different value of the slack after changing U159879(ND2HHD) to ND2KHD \n")
fc.write("Give the counts of Failing paths and Non Failing paths in c432 circuit \n")

fc.write("Give the counts of critical and non critical paths for different value of the slack  \n")
for i in range (0,1000):
	#present_slack= initial_slack - float(i)*initial_slack/100
	present_slack= initial_slack - float(i)*0.001#float(i)*initial_slack/100
	if present_slack < 0.2:
		break
	fc.write("---------------------------------------------------------------------\n")
	fc.write("-----------------------------Start -- For Slack Value "+str(present_slack)+"-------------------\n")
	fc.write("---------------------------------------------------------------------\n")


	fblocksdc=open("block1.sdc","w")
	fblocksdc.write("create_clock -name clk -period "+str(present_slack)+" -waveform {0 "+str(present_slack/2)+"} [get_ports clk]\n\tset_input_delay  0 -clock clk [all_inputs]\n\tset_output_delay 0 -clock clk [all_outputs]\nset_clock_uncertainty 0 clk")
	fblocksdc.close()
	#subprocess.call(['./klr_script.sh'])
	print("----------- executing KLR--------------------")
	os.system("sh klr_script.sh")
	#os.system("cd reports")
#	os.system("mkdir critical_paths_"+folder_path_time_stamp)
	with open("reports/all_critical_paths") as f:
		line=f.read()
		countMet= line.count("MET")
		countViolated= line.count("VIOLATED")

	print("Count met ---")
	print(countMet)
	fc.write("\nCount met ---\n")
        fc.write("M - "+str(countMet))
	print("Count violated ---")
	print(str(countViolated))
	paths_violated.append(countViolated)
	for_slack.append(present_slack)
	fc.write("\nCount violated ---\n")
        fc.write("V - "+str(countViolated))
	fc.write("\n---------------------------------------------------------------------\n")
        fc.write("-----------------------------Start -- For Slack Value "+str(present_slack)+"-------------------\n")
        fc.write("---------------------------------------------------------------------\n")

	f.close()
	os.system("cp reports/all_critical_paths critical_paths_"+folder_path_time_stamp+"/all_critical_paths_cycle_"+str(present_slack))
#	os.system("cd ..")
	

#plt.plot(paths_violated,for_slack,'ro')
plt.plot(for_slack,paths_violated,'m2')
#plt.axis([0,600,1.65,0])
plt.axis([0.86,0.2,0,250])
plt.xlabel("Clock Period (*10^3 ps)")
plt.ylabel("Nos of Failing Paths")
#plt.xlabel("Clock Cycle Length(*10^3 ps)")
plt.title("Nos Of Failed Paths vs Clock Period - c432")
plt.show()
fc.close()

