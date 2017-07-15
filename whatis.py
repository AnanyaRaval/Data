import pandas as pd 

whatis = pd.DataFrame(columns = ['Command','NL Queries'])

whatis = whatis.append({'Command':'whatis head','NL Queries':['How do I know what the command head does?','Get one line description of head command.','How do I see what head command in linux does?']},ignore_index=True)
whatis = whatis.append({'Command':'whatis -s "2" open','NL Queries':['Show section 2 of documentation of command open.','How do I see section 2 of man pages of what command open does?']},ignore_index=True)

print whatis


