import pandas as pd 

sort = pd.DataFrame(columns = ['Command','NL Queries'])

sort = sort.append({'Command':'sort data.txt','NL Queries':['Sort the file data.txt in this directory.','What is the command to sort file data.txt in alphabetical order?','How do I sort contents of file data.txt present in this dorectory, in ascending order?']},ignore_index = True)
sort = sort.append({'Command':'sort -f data.txt','NL Queries':['Sort the file data.txt in alphabetical order. Ignore the case of the words.','How do I sort the contents of file data.txt in this folder with being case sensitive?']},ignore_index=True)
sort = sort.append({'Command':'sort -k2 test.txt','NL Queries':['Sort contents of text.txt using values in second column.','How do I sort test.txt using contents of second column?']},ignore_index=True)

print sort
