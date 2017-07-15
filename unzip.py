import pandas as pd 

unzip = pd.DataFrame(columns = ['Command','NL Queries'])

unzip = unzip.append({'Command':'unzip letters','NL Queries':['Extract all files and sub directories in the archive named letters.','Uncompress the letters archive and store all the files in current folder and subdirectories below the current folder.','How do I extract all files of letters to this directory anf subdirectories in corresponding subdirectories?']},ignore_index=True)
unzip = unzip.append({'Command':'unzip -j letters','NL Queries':['How do I extract all contents of letters to this directory itself?','Uncompress letters and store all files and folders in this folder.']},ignore_index=True)
unzip = unzip.append({'Command':'unzip Trash.zip -d /home/music/Alice Cooper/Trash','NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash','How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash']},ignore_index=True)

print unzip


