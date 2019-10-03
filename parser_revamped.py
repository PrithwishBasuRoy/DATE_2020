# The Following piece of code parses the synthesized netlist in the ISPD 2013 contest's expected format
#for avoiding unwanted behaviours, please remove the comment section at the top of the synthesized netlist before using it in
#this tool

import os
import sys
filename=sys.stdin.readline().split()[0]
print filename
filelist = [ ]
filelist.append(filename)

outfile=open(filelist[0].replace(".v",'')+'_parsed.v','w')
reading_ports=False
reading_endmodule = False 
reading_cells = False
reading_wire = False
# output=False # set to true when outputs are being parsed
# wire=False #set to true when wires are being parsed
# cells=False #set to true when cells are being parsed
# write=False # set to true when cells are being written to file
tempstring=' '
strlist=[]
#count=1000# please check if the max instance count (eg: BUFLTX1 U100 , 100 is the instance count), is lesser than count.
port_list = []
port_lst_actual=[]
input_list=[]
output_list=[]
wire_list=[]
start_reading = False
input_width={}
output_width={}
wire_width={}
break_line= False
broken_line =''
reading_comments = True
assign_map={}
nos_of_assign=0
assign_set=[]
print filelist[0]
with open(filelist[0]) as infile:
	for line in infile:
		
		if 'module' in line and 'endmodule' not in line and not reading_ports and reading_comments:#finds the line where the module begins
			a=line.split(',')
			reading_comments = False

			temp=a[0].split('(')
			# print temp
			
			if '\n' in a or ' \n' in a :
				reading_ports = True

			name = temp[0].split(" ")	
			for strng in name :
				port_list.append(strng.replace(" ",''))
			port_list.append("(\n")
			port_list.append(temp[1].replace(" ",''))
			port_lst_actual.append(temp[1].replace(" ",''))

			a_length = len(a)
			for i in range (1,a_length) :
				#print(str(i)+" ------------------ "+a[i])
				if '\n' not in a[i] and ' \n' not in a[i]: 
					port_list.append(a[i].replace(" ",''))
					port_lst_actual.append(a[i].replace(" ",''))
				if ");\n" in a[i] :
					port_list.append(a[i].replace(");\n",'').replace(" ",''))
					# port_list.append(a[i].replace(" ",''))
					port_lst_actual.append(a[i].replace(");\n",'').replace(" ",''))	
					#port_lst_actual.append(a[i].replace(" ",''))	
			# print port_list		

		if reading_ports == True and 'input' not in line:
			if ")" in line :
				a=line.split(')')
				extra = a[0].split(',')
				for strng in extra :
					port_list.append(strng.replace(" ",''))
					port_lst_actual.append(strng.replace(" ",''))
				a_length= len(a)
				port_list.append(')')
				for i in range (1,a_length) :
					port_list.append(a[i].replace(" ",''))			
			# print port_list

		print port_lst_actual
		print port_list

		##  The following code checks when the input is encountered.
		##  On encountering it opens another instance of the file and checks for all the instances of ports and their widths
		##  At the same time it also records the list of wires and also the width of this wires
		if 'input' in line and start_reading == False:
			reading_ports = False# changed to false as list of ports has been aquired and port reading has been complete
			start_reading = True
			with open(filelist[0]) as infile_2:#opens a second file to get the different input, output and wires and their corresponding widths 
				for each_line in infile_2 :
					if 'input' in each_line :
						start_reading = True
					if start_reading :
						 for i in port_lst_actual :
							if i+"," in each_line or i+";" in each_line :
								if(i == "out"):
									tokens = each_line.split("out;")
								else :	
									tokens = each_line.split(i);
								for each_token in tokens :
									if "[" in each_token and "]" in each_token and ":" in each_token : #CHECKS whether range is defined or not
										width = each_token.split("[")[1].replace(" ",'').replace("[",'').replace("]",'').split(":")[0]
										print (each_token + " ---------- "+each_token.split("]")[1]+"  "+ width)
										if "input" in each_token:
											input_width[i]=int(width)+1
											input_list.append(i)
										if "output" in each_token:
											output_width[i]=int(width)+1
											output_list.append(i)
										# if "wire" in each_token:
											# wire_width[i]=int(width)+1
									else :
										if "input" in each_token:
											input_width[i]=1
											input_list.append(i)
										if "output" in each_token:
											output_width[i]=1
											output_list.append(i)
					
					#for first line of declaration
					if "wire" in each_line and start_reading :
						reading_wire=True 
						if ";" not in each_line:# more than one line containing wire declaration
							
							wire_set_per_line= each_line.replace("wire",'').replace(" ",'').replace("\n",'').split(',')
							for wire in wire_set_per_line:
								wire_list.append(wire)
						else :
							if ';' in each_line and ',' in each_line :#wire declaration completed in one line
								wire_set_per_line= each_line.replace("wire",'').replace(" ",'').replace("\n",'').split(',');
								if(len(wire_set_per_line) > 1) :
									for wire in wire_set_per_line:
										wire_list.append(wire)
								reading_wire = False
							elif ',' not  in each_line and ';' in each_line and "[" in each_line and "]" in each_line and ":" in each_line :
									print each_line
									wire_name=each_line.split("]")[1].replace(" ",'').replace("\n",'').replace(";",'')
									width = each_line.replace("wire",'').split("[")[1].replace(" ",'').split("]")[0]
									wire_width[wire_name] = width
									wire_list.append(wire_name);
									reading_wire = False 

					elif reading_wire:#incase there are multiple lines of declaration
						if ";" in each_line:# if declaration ends in this line
							reading_wire = False
							wire_set_per_line_temp = each_line.split(";")
							wire_set_per_line = wire_set_per_line_temp[0].split(",")
							if(len(wire_set_per_line) == 1) :#if only one wire instance is defined
								wire_list.append(wire_set_per_line[0].replace(" ",''))
						else :

							wire_set_per_line = each_line.split(",")
							# for wire in wire_set_per_line :
								# wire_list.append(wire.replace(" ",''))		

						for wire in wire_set_per_line:
							if '\n' not in wire:
								wire_list.append(wire.replace(" ",''))				
									
					if "assign" in each_line and start_reading:
						if('b0' not in line and 'b1' not in line):
							st=each_line.strip().split(';')[0].split()
							#print st
							#templine='BUFX1 U'+str(count)+' ( .I1('+st[3]+'), .O('+st[1]+') );\n'
							#tempstring=tempstring+templine.strip()
							print "assign blocks"
							print st
							assign_map[st[1]] = st[3]
							assign_set.append(st[1])
							nos_of_assign=nos_of_assign+1
									
					elif ", ." in each_line and start_reading and reading_wire:
						print each_line
						reading_wire = False
						start_reading = False				

					# elif reading_wire:#incase there are multiple lines of declaration
					# 	if ";" in each_line:# if declaration ends in this line
					# 		reading_wire = False
					# 		wire_set_per_line_temp = each_line.split(";")
					# 		wire_set_per_line = wire_set_per_line_temp[0].split(",")
					# 		if(len(wire_set_per_line) == 1) :#if only one wire instance is defined
					# 			wire_list.append(wire_set_per_line[0].replace(" ",''))
					# 	else :

					# 		wire_set_per_line = each_line.split(",")
					# 		# for wire in wire_set_per_line :
					# 			# wire_list.append(wire.replace(" ",''))		

					# 	for wire in wire_set_per_line:
					# 		if '\n' not in wire:
					# 			wire_list.append(wire.replace(" ",''))

					
			print("Input Width")
			print input_width
			print("Output Width")
			print output_width
			print("Assign Map")
			print assign_map
			#print wire_width
			#print wire_list	
		
		#Code for writing the ports begins 	
			first_line = True
			num_of_ports=len(input_list)+len(output_list)
			remaining_ports_to_be_written=num_of_ports
			print("Num of ports :"+str(num_of_ports)) 
			for tokens in port_list :
				if tokens == "(\n" :
					outfile.write(tokens)
					first_line = False
				else :
					if first_line == True :
						outfile.write(tokens + " ")

				if(first_line == False ) :
					if tokens in input_width:
						remaining_ports_to_be_written = remaining_ports_to_be_written - 1
						width = input_width[tokens]

						if width != 1:
							for i in range (0,width):
								if remaining_ports_to_be_written == 0 and i == width -1 :
									outfile.write(tokens+"_"+str(i)+"\n")
								else :	
									outfile.write(tokens+"_"+str(i)+",\n")
						else :
							if remaining_ports_to_be_written == 0 :
								outfile.write(tokens+"\n")
							else :		
								outfile.write(tokens+",\n")
					elif tokens in output_width:
						remaining_ports_to_be_written = remaining_ports_to_be_written - 1
						width = output_width[tokens]
						# if width != 1:
						# 	for i in range (0,width):
						# 		outfile.write(tokens+"_"+str(i)+",\n")
						# else :		
						# 		outfile.write(tokens+",\n")
						if width != 1:
							for i in range (0,width):
								if remaining_ports_to_be_written == 0 and i == width -1 :
									
									#if tokens == "out":
										#outfile.write(tokens+"_"+str(i)+"\n);\n")
										outfile.write(tokens+"_"+str(i)+"\n")	
									#else:
									# 	outfile.write(tokens+"_"+str(i)+"\n")
										
								else :	
									outfile.write(tokens+"_"+str(i)+",\n")
						else :
							if remaining_ports_to_be_written == 0 :
								outfile.write(tokens+"\n);\n")
							else :		
								outfile.write(tokens+",\n")

						# outfile.write(tokens+",\n")	
					elif ")" in tokens:
						outfile.write(tokens+";\n")
					elif " " == tokens :
						outfile.write(tokens+",\n")	
			#succesfully prints the port lidt of the graph		 	

			#writing the inputs 
			outfile.write(');\n//Start PIs\n')

			for i in input_list:
				width = input_width[i]
				#print (str(i)+" width -------- "+str(width))
				if width != 1 :#input has width more than 1 bit
					for w in range (0,width):
						if i != " "  :#if tokens are not spaces 
							outfile.write("input "+i.replace("\n",'')+"_"+str(w)+";\n")	
				else :#has width of only 1 bit
					if i != " " :#if tokens are not spaces 
						outfile.write("input "+i.replace("\n",'')+";\n")		
			#finished writing the inputs

			#writing the outputs			
			outfile.write('//Start POs\n')

			for i in output_list:
				width = output_width[i]
				if width != 1 :
					for w in range (0,width):
						outfile.write("output "+i.replace("\n",'')+"_"+str(w)+";\n")	
				else :
					outfile.write("output "+i.replace("\n",'')+";\n")


			#finished writing the outputs		

			#writing the wires 
			outfile.write('//Start wires\n')
			for i in wire_list:
				if i in wire_width:
					msb_lsb=wire_width[i].split(":")
					for w in range(int(msb_lsb[1]),int(msb_lsb[0])+1):
						outfile.write("wire "+i.replace("\n",'').replace('\\','_').replace('/','_')+"_"+str(w)+";\n")			
				else :
					if (('' != i and ' ' != i ) and i not in wire_width):
						if "[" in i and "]" in i:
							outfile.write("wire "+i.replace("\n",'').replace("[",'_').replace("]",'').replace('\\','_').replace('/','_')+";\n")
						else :
							outfile.write("wire "+i.replace("\n",'').replace('\\','_').replace('/','_')+";\n")							



			#finished writing the wires
			#break;

		if ", ." in line and reading_cells == False and not reading_ports:#demarkates the point from where we should start reading cells 
			reading_cells=True
			outfile.write('//Start cells\n')


		if reading_cells and start_reading:
		# k = ''

			if ";\n" not in line and break_line == False:#checks whther there in a line break in the cell instantiation
				
				break_line = True
				broken_line = line.replace("\n",'').replace(" [",'_').replace("[",'_').replace("]",'').replace('\\','_').replace('/','_').replace("\n",'');#parses the first line 
				#outfile.write(line.replace("\n",'').replace("[",'_').replace("]",'').replace('\\','_').replace('/','_').replace("\n",'').replace("(        ",'(').replace(",         .",", .").replace(")         )",") )"))
			else :#this part implements the logic of combining cell instances spread in more than 1 line into a single line
				if break_line == True and ";\n" in line :
					join_line = broken_line+line.replace(" [",'_').replace("[",'_').replace("]",'').replace('\\','_').replace('/','_')
				#outfile.write(line.replace("[",'_').replace("]",'').replace('\\','_').replace('/','_').replace("(        ",'(').replace(",         .",", .").replace(")         )",") )"))			
					outfile.write(join_line.replace("(        ",'(').replace(",         .",", .").replace(")         )",") )"))
					break_line = False
					broken_line=''
				elif break_line == True and ";\n" not in line :
					broken_line = broken_line + line.replace(" [",'_').replace("[",'_').replace("]",'').replace('\\','_').replace('/','_').replace("\n",''); 	

				elif break_line == False and ";\n" :
					outfile.write(line.replace(" [",'_').replace("[",'_').replace("]",'').replace('\\','_').replace('/','_'))
		

		if "endmodule" in line :#checks for the endmodule
			reading_cells=False
			start_reading = False
			if len(assign_set) == 0:
				outfile.write("endmodule\n")
			else :
				last_tokens=last_line.split(" ")	
				print "Last --- tokens "
				print last_tokens
				count=1
				last_cell_count=int(last_tokens[3].replace("U",''))
				for lhs in assign_set :
					rhs = assign_map[lhs]
					templine='  BUFCHD U'+str(last_cell_count+count)+' ( .I1('+lhs.replace("[",'_').replace("]",'')+'), .O('+rhs.replace("[",'_').replace("]",'')+') );\n'
					outfile.write(templine)
					count = count+1

				outfile.write("endmodule\n")

		if line !="\n":# keeps a track of the last line. Will be useful while adding the buffers for assign statements
			last_line= line	

		if reading_comments == True :
			continue;
	

