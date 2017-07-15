import pandas as pd 

diff = pd.DataFrame(columns = ['Command','NL Queries'])

diff = diff.append({'Command':'diff file1.txt file2.txt','NL Queries':['How do I find the difference between files file1.txt and file2.txt?','What is the difference between file1.txt and file2.txt? Both files are in this folder.','How do I display lines which are different in file1.txt and file2.txt?']},ignore_index = True)
diff = diff.append({'Command':'diff -u file1.txt file2.txt','NL Queries':['How do I find the difference between file1.txt and file2.txt? Print all unique rows from both files.','How do I print a unified set of all distinct rows in file1.txt and file2.txt?']},ignore_index=True)
diff = diff.append({'Command':'diff -i file1.txt file2.txt','NL Queries':['How do I perform a case insensitive comparision of file1.txt and file2.txt? Print the difference on Command Line.','Command to print case insensitive difference between file1.txt and file2.txt in this folder.']},ignore_index=True)

print diff
