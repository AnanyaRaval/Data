import pandas as pd 

getfacl = pd.DataFrame(columns = ['Command','NL Queries'])

getfacl = getfacl.append({'Command':'getfacl instructions.txt.','NL Queries':['Display filename,owner, group, access control list of instructions.txt.','Show all information about the file instuctions.txt present in this folder.']},ignore_index=True)
getfacl = getfacl.append({'Command':'getfacl -a instructions.txt','NL Queries':['Display access control list for file instructions.txt.', 'How do I see the access control list of instructions.txt?']},ignore_index=True)
getfacl = getfacl.append({'Command':'getfacl -n instructions.txt','NL Queries':['Display filename, owner, group, access control list of instructions.txt. Show numeric owner and group IDs.','Show all insformation of file instrucitons.txt with numeric IDs.']},ignore_index=True)

print getfacl


