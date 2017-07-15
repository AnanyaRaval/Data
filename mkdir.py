import pandas as pd 

mkdir = pd.DataFrame(columns = ['Command','NL Queries'])

mkdir = mkdir.append({'Command': 'mkdir ananya','NL Queries':['Make folder named ananya here.','Create folder ananya.','How do I create a new folder ananya?','Make folder ananya.']},ignore_index = True)
mkdir = mkdir.append({'Command': 'mkdir ../folder','NL Queries':['Empty folder in parent directory named folder.','Folder named folder in previous directory.','Make empty folder in parent directory called folder.']},ignore_index = True)
mkdir = mkdir.append({'Command': 'mkdir -m a=rwx mydir','NL Queries':['Create the mydir directory, and set its permissions such that all users may read, write, and execute the contents.','Make directory with name mydir. Set permissions:read,write,execute for all users.','How do I create a directory called mydir and set it\'s persmissions so that all users can read, execute and write  to it.']},ignore_index = True)

print mkdir