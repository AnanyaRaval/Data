import pandas as pd 

whereis = pd.DataFrame(columns = ['Command','NL Queries'])

whereis = whereis.append({'Command':'whereis python','NL Queries':['How do I find all paths containing python?','Locate python.','List folders where python source files, documentaion and binaries are stored.']},ignore_index=True)
whereis = whereis.append({'Command':'whereis -u -M /usr/man/man1 -S /usr/src -f *','NL Queries':['Find all files in the current directory that are not documented in /usr/man/man1, whose source resides in /usr/src.']},ignore_index=True)

print whereis


