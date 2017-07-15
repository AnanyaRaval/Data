import pandas as pd 

cat = pd.DataFrame(columns = ['Command','NL Queries'])

cat = cat.append({'Command':'cat >foo.txt','NL Queries':['Create new file foo.txt. Open it in command line.','How do I start a file foo.txt so that I can add lines to it?','Start a file foo.txt in command line.']},ignore_index = True)
cat = cat.append({'Command':'cat instructions.txt','NL Queries':['Open file instructions.txt','Show contents of file instructions.txt.','Display data in file instructions.txt. It\'s contents are in this folder.','How do I see what is in the file instructions.txt?']},ignore_index = True)
cat = cat.append({'Command':'cat -n instructions.txt','NL Queries':['Open file instructions.txt. Show line numbers.','Display file instructions.txt with line numbers.','How do I see contents of instructions.txt along with numbered lines?']},ignore_index = True)
cat = cat.append({'Command':'cat *','NL Queries':['Display contents of all files.','How can I see data in all files?']},ignore_index = True)
cat = cat.append({'Command':'cat ln.csv ls.csv > total.csv','NL Queries':['Combine ln.csv and ls.csv in a new file total.csv.','Create new file with contents of ln.csv and ls.csv. Name the new file total.csv.','How do I merge contents of files ln.csv and ls.csv into total.csv?']},ignore_index=True)

print cat
