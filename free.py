import pandas as pd 

free = pd.DataFrame(columns = ['Command','NL Queries'])

free = free.append({'Command':'free','NL Queries':['How much free memory do I have on my disk?','Show the amount of free memory on my computer.','Get statistics of available memory.']},ignore_index=True)
free = free.append({'Command':'	free -s 1','NL Queries':['Display usage of RAM every 1 second.','How do I check the usage of my RAM every second?']},ignore_index=True)
free = free.append({'Command':'	free -m','NL Queries':['Show the amount of memory in Megabytes.','Display free RAM memory in MB.','How do I check the statistics of available RAM in MB?']},ignore_index=True)

print free


