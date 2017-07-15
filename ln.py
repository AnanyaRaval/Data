import pandas as pd 

ln = pd.DataFrame(columns = ['Command','NL Queries'])

ln = ln.append({'Command':'ln -s /full/path/of/original/file /full/path/of/soft/link/file', 'NL Queries':['Create soft link from /full/path/original/file to /full/path/of/soft/link/file.','Command to create soft link from full path of original file to full path of soft link file.','Soft link of /full/path/original/file at /full/path/of/soft/link/file','Symbolic link of /full/path/original/file at /full/path/of/soft/link.','Soft link from /full/path/of/soft/link to /full/path/original/file.']},ignore_index = True)
ln = ln.append({'Command':'ln --backup -s ex1.c ex2.c','NL Queries':['Backup current files. Create Symbolic link from ex2.c to ex1.c.','Make a soft link of ex1.c named ex2.c after taking backup.','How do I take backup of current files and create soft link from ex2.c to ex1.c.']},ignore_index = True)
ln = ln.append({'Command':'ln -s ../first-dir/*.c -t .','NL Queries':['Create soft links in current directory for all .c files in first-dir.','How to create symbolic links from all .c files in first directory in current folder.']},ignore_index = True)
ln = ln.append({'Command':'ln src_original.txt dst_link.txt','NL Queries':['Create hard link from dst_link.txt to src_original.txt.','How to create hard link of src_original.txt named dst_link.txt?','Make link from dst_link.txt to src_original.txt in current directory. It should be a hard link, not soft.']},ignore_index= True)
ln = ln.append({'Command':'ln ananya ananya_new','NL Queries':['Create link of ananya folder in current directory named ananya_new, also in the curent diretory.']},ignore_index = True)

ln.to_csv('ln.csv',index = False)

print ln