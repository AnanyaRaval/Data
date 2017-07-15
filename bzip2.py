import pandas as pd 

bzip2 = pd.DataFrame(columns = ['Command','NL Queries'])

bzip2 = bzip2.append({'Command':'bzip2 file.txt','NL Queries':['Compress file.txt present in this folder.','How do I zip file.txt?','Command to compress file.txt using bzip2.']},ignore_index=True)
bzip2 = bzip2.append({'Command':'bzip2 -c file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2. Name the compressed file as file.txt.bz an keep file.txt as it is.','How do I compress file.txt using bzip2,keep the original file and name the compressed file file.txt.bz?']},ignore_index=True)
bzip2 = bzip2.append({'Command':'bzip2 -d file.txt.bz2','NL Queries':['Decompress file.txt.bz.','How to decompress dataof file.txt.bz present in this folder?']},ignore_index=True)

print bzip2


