import pandas as pd 

export = pd.DataFrame(columns = ['Command','NL Queries'])

export = export.append({'Command':'export -p','NL Queries':['Show all bash environment variables.','How do I print all enironment variables?','View all variables in shell environment.']},ignore_index = True)
export = export.append({'Command':'export VAR=1','NL Queries':['Create an environment variable called VAR. Initialise it\'s value to 1.','How do I create a new environment variable VAR with value = 1?','What is the command to make a variable VAR and equate it\'s value to 1?']},ignore_index=True)
export = export.append({'Command':'export PATH=$PATH:/home/himanshu/practice/','NL Queries':['Command to add /home/himanshu/practice/ to variable PATH.','How do I append the string /home/himanshu/practice/ to shell variable PATH?']},ignore_index=True)

print export
