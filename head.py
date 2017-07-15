import pandas as pd 

head = pd.DataFrame(columns = ['Command','NL Queries'])

head = head.append({'Command':'head -n 2 /etc/passwd','NL Queries':['Print first 2 lines of the file /etc/passwd.','Show the first two lines of /etc/passwd.','Command to show first two lines of /etc/passwd.']},ignore_index=True)
head = head.append({'Command':'head instructions.txt','NL Queries':['Print first few lines of the file instructions.txt.','Show the starting lines of the file instructions.txt.','How do I see the first few lines of the file instructions.txt in command line?']},ignore_index=True)

print head


