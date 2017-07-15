import pandas as pd 

gnu = pd.DataFrame(columns = ['Command','NL Queries'])

gnu = gnu.append({'Command':'less instructions.txt','NL Queries':['Show contents of instructions.txt enouogh to fit the teminal.', 'Display on command line, content of instructions.txt. do not show complete file, only the amount which fits the command line.']},ignore_index=True)
gnu = gnu.append({'Command':'less +4 instructions.txt','NL Queries':['Show contents of instructions.txt. Skip the first 4 lines though.','Show contents of instructions.txt starting from 5th line.','How do I see content of instructions.txt without the first four lines?']},ignore_index=True)
gnu = gnu.append({'Command':'less general.py ananya.py','NL Queries':['Show content of general.py and ananya.py.','Display lines of the files general.py and ananya.py.','Show contents of general.py and ananya.py.	']},ignore_index=True)

print gnu


