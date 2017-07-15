import pandas as pd 

uniq = pd.DataFrame(columns = ['Command','NL Queries'])

uniq = uniq.append({'Command':'uniq myfile.txt','NL Queries':['Display all unique lines in the file myfile.txt.','Filter all unique lines from myfile.txt.','Command to check all distinct lines in myfile.txt.']},ignore_index=True)
uniq = uniq.append({'Command':'uniq -d myfile.txt','NL Queries':['Show only repeated lines from myfile.txt.','Display contents of myfile.txt. Show lines ,which have count more than 1, of file myfile.txt.']},ignore_index=True)
uniq = uniq.append({'Command':'uniq -u instructions.txt','NL Queries':['Print only unique lines in the file instructions.txt on command line.','Show lines of instructions.txt which have count = 1.']},ignore_index=True)

print uniq


