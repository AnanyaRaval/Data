import pandas as pd 

gnu = pd.DataFrame(columns = ['Command','NL Queries'])

gnu = gnu.append({'Command':'more instructions.txt','NL Queries':['Show content of instructions.txt enough to fit the command line.','How do I see a part of the file instructions.txt which fits the command line?','Show as much content of instructions.txt on the terminal.']},ignore_index=True)
gnu = gnu.append({'Command':'more +/"hope" myfile.txt','NL Queries':['Display the contents of file myfile.txt, beginning at the first line containing the string "hope".']},ignore_index=True)
gnu = gnu.append({'Command':'more +3 myfile.txt','NL Queries':['Show contents of myfile.txt starting from line 4.','Display contents of myfile.txt. Skip first 3 lines. Show only as much content as it fits the terminal.']},ignore_index=True)

print gnu


