import pandas as pd 

du = pd.DataFrame(columns = ['Command','NL Queries'])

du = du.append({'Command':'du -s *.txt','NL Queries':['Display file size of all files in this folder with extension txt.','How do I check file sizes of all .txt files in this folder?']},ignore_index=True)
du = du.append({'Command':'du  -h /home/ananyaraval','NL Queries':['Show amount of memory occupied by all folders in /home/ananyaraval. Show the memory with units I understand.','Display the amount of memory occupied by each folder in /home/ananyaraval, using KiloBytes, MegaBytes as units.']},ignore_index=True)
du = du.append({'Command':'du -c /home/ananyaraval','NL Queries':['Display memory usage of each folder in /home/ananyaraval along with total memory usage of /home/ananyaraval.','Show  individual and cumulative diska usage of folders in /home/ananyaraval.']},ignore_index=True)

print du


