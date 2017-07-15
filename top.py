import pandas as pd 

top = pd.DataFrame(columns = ['Command','NL Queries'])

top = top.append({'Command':'top','NL Queries':['Display processes which are currently executing along with their statistics.',\
				'How do I display the running state of the system?','How do I check how much is the CPU usage of the system?',\
				'Command to display Process ID,User ID, Priority, Nice level,Virtual Memory by process,Resident memory used by a process,Shareable memory,CPU used by process as a percentage,Memory used by process as a percentage,Time process has been running and Command for each process.'\
				'Display task, CPU, Memory, Swap etc. of the system.']},ignore_index=True)
top = top.append({'Command':'top -i','NL Queries':['Show all running processes and their information which are not idle.','How do I see information about non-idle processes?','Show the state of the System. Only the processes which are running.']},ignore_index=True)


print top


