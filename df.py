import pandas as pd 

df = pd.DataFrame(columns = ['Command','NL Queries'])

df = df.append({'Command':'df','NL Queries':['Display file system usage.','Show the statistics of file system.']},ignore_index=True)
df = df.append({'Command':'df -a','NL Queries':['Show statistics of all file systems. Along with dummy ones.','Show device name,total blocks,total disk space,available disk space and mount points of the system, along with those of dummy file system.']},ignore_index=True)
df = df.append({'Command':'df -T','NL Queries':['Display file system type and other statistics of file system.','Display device name,total blocks,total disk space,available disk space and mount points of the system,file type.']},ignore_index=True)

print df


