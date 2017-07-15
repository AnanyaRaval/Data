import pandas as pd 

awk = pd.DataFrame(columns = ['Command','NL Queries'])

awk = awk.append({'Command':'awk \'{print}\' marks.txt','NL Queries':['Print contents of table.txt.','How do I print marks.txt?']},ignore_index=True)
awk = awk.append({'Command':'awk \'/a/ {print $4 "\t" $3}\' marks.txt','NL Queries':['Print tab-separated columns 4 and 3 of marks.txt containing string "a".','How do I see the columns 4 and 3 of table in marks.txt? I need to see only those which have "a" in their value.']},ignore_index=True)
awk = awk.append({'Command':'awk -F, \'{print $2}\' table.csv','NL Queries':['Print second column of comma separated table in table.csv.','How do I print second column from table.csv which has , as their separator?']},ignore_index=True)

print awk
