import pandas as pd 

uname = pd.DataFrame(columns = ['Command','NL Queries'])

uname = uname.append({'Command':'uname -a','NL Queries':['Show linux kernel version information.','How do I check linux kernel version?','Command to check kernel version.','Check OS information.']},ignore_index=True)
uname = uname.append({'Command':'uname -p','NL Queries':['How do I check processor information?','What types of processor am I using?','Command to check which processor I am using']},ignore_index=True)

print uname


