import pandas as pd 

cp = pd.DataFrame(columns = ['Command','NL Queries'])

cp = cp.append({'Command':'cp main.c bak','NL Queries':['Copy main.c in curent folder to bak in the same folder.','How do I copy main.c to bak?','Command to copy contents of main.c to bak.']},ignore_index = True)
cp = cp.append({'Command':'cp *.py backup','NL Queries':['Copy all .py files to backup folder.','How do I copy all .py files to folder backup?','Command to replicate all files to folder backup in this directory.']},ignore_index=True)
cp = cp.append({'Command':'cp -u * ananya','NL Queries':['Copy all files in this folder to ananya only if they are not present in ananya.','Update folder ananya by copying files from this directory. Update only if file not present in ananya.']},ignore_index=True)
cp = cp.append({'Command':'cp -n instructions.txt backup','NL Queries':['Create a copy of instructions.txt named backup. Copy only if backup not present in current folder.','How do I copy instructions.txt to backup without overwriting it.']},ignore_index=True)

print cp
