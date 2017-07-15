import pandas as pd 

gzip2 = pd.DataFrame(columns = ['Command','NL Queries'])

gzip2 = gzip2.append({'Command':'gzip file1.txt file2.txt file3.txt','NL Queries':['Command to compress file1.txt, file2.tzt and file3.txt.','Compress the following files individually: file1.txt, file2.txt, file3.txt.']},ignore_index=True)
gzip2 = gzip2.append({'Command':'gunzip -c file.txt.gz > file.txt','NL Queries':['Command to decompress file.txt.gz and store to file.txt. Keep the original file.','How do I decompress file.txt.gz and store the contents to file.txt while keeping file.txt.gz intact?']},ignore_index=True)
gzip2 = gzip2.append({'Command':'gzip -c file2.txt >> files.gz','NL Queries':['Command to compress file2.txt and add it to archive files.gz.Keep the original file.','How do I add compress file2.txt and add it to files.gz while keeping file2.txt as it is.']},ignore_index=True)

print gzip2


