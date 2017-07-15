import pandas as pd 

ls = pd.DataFrame(columns = ['Command','NL Queries'])

ls = ls.append({'Command':'ls','NL Queries':['List all files in current directory', 'Which folders and files do  I have in my current directory?','Files present in this directory.','Folders present in this directory.','Name all contents of my working directory.']},ignore_index = True)
ls = ls.append({'Command':'ls / ','NL Queries': ['Contents of root directory.','What are the names of files/folders in my root directory.']},ignore_index = True)
ls = ls.append({'Command':'ls ..','NL Queries':['Stuff in one directory before current one.','Files and folders present in parent directory.']},ignore_index = True)

ls.to_csv('ls.csv',index = False)