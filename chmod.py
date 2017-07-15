import pandas as pd 

chmod = pd.DataFrame(columns = ['Command','NL Queries'])

chmod = chmod.append({'Command':'chmod u=rwx,g=rx,o=r myfile','NL Queries':['Change permissions for myfile. User can read, write and execute. Group can read and execute it.Others can only read it.','How do I change permissions of myfile so that user can do everything, group can only read and write and others can only read it.']},ignore_index = True)
chmod = chmod.append({'Command':'chmod 754 myfile','NL Queries':['Change permissions for myfile. User can read, write and execute. Group can read and execute it.Others can only read it.','How do I change permissions of myfile so that user can do everything, group can only read and write and others can only read it.']},ignore_index = True)
chmod = chmod.append({'Command':'chmod u+x filename','NL Queries':['Add execute persimission to user for file filename.','How do I make user persimssions of this file to execute also?','For filename, add execute persmission to user.']},ignore_index = True)
chmod = chmod.append({'Command': 'chmod -R 755 directory-name/','NL Queries':['Change permission of folder directory-name. User can read,write,execute. Group and Others can read and execute. All files should also have the same permission.']},ignore_index = True)


print chmod
