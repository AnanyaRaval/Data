import pandas as pd 

mv = pd.DataFrame(columns = ['Command','NL Queries'])

mv = mv.append({'Command':'mv ananya.py ananya_new.py','NL Queries':['Copy ananya.py. Rename ananya.py to ananya_new.py.','Change name to ananya.py to ananya_new.py and copy the file.','How do I create a copy of ananya.py named ananya_new.py?']},ignore_index=True)
mv = mv.append({'Command':'mv *.c backup','NL Queries':['Move all .c files from current folder to folder backup.','How do I shift all .c files from this folder to a different folder named backup?','Command to move all .c files to backup folder.']},ignore_index=True)
mv = mv.append({'Command':'mv bak/* .','NL Queries':['Shift all files from back folder in this directory to this folder.','How do I move all files from folder bak/ to this folder?']},ignore_index=True)

print mv



