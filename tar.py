import pandas as pd 

tar = pd.DataFrame(columns = ['Command','NL Queries'])

tar = tar.append({'Command':'tar cvzf MyImages-14-09-12.tar.gz /home/MyImages','NL Queries':['Create a new tar archive for /home/MyImages folder in current directory. It\'s name should be MyImages-14-09-12.tar.gz. Display the progress of files.']},ignore_index = True)
tar = tar.append({'Command':'tar -xvf compressed.tar','NL Queries':['Untar compressed.tar in current directory. Show the files in the tar archive.']},ignore_index=True)
tar = tar.append({'Command':'tar -xvf Phpfiles-org.tar --wildcards \'*.php\'','NL Queries':['Extract all .php files from Phpfiles-org.tar in the current folder.','How do I extract the files ending with .php from Phpfiles-org.tar']},ignore_index = True)

print tar
