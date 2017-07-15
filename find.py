import pandas as pd 

find = pd.DataFrame(columns = ['Command','NL Queries'])

find = find.append({'Command':'find . -name tecmint.txt','NL Queries':['Find all the files whose name is tecmint.txt in a current working directory.','How do I list all files named techmint.txt in this folder?']},ignore_index = True)
find = find.append({'Command':'find /home -iname tecmint.txt','NL Queries':['Find all the files whose name is tecmint.txt and contains both capital and small letters in /home directory.','List all techmint.txt irrespective of their case in /home folder.']},ignore_index=True)
find = find.append({'Command':'find /home/Documents -type d -name Data','NL Queries':['Find all directories whose name is Data in /home/Documents directory.','How do I list all folders named Data in /home/Documents?']},ignore_index=True)

print find