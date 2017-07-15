import pandas as pd 

rm = pd.DataFrame(columns = ['Command','NL Queries'])

rm = rm.append({'Command':'rm linuxfile.log','NL Queries':['Remove file linuxfile.log.','Delete file linuxfile.log.','Command to delete linuxfile.log present in this diretory.','Command to delete file linuxfile.log from the current folder.']},ignore_index = True)
rm = rm.append({'Command':'rm abc.txt efg.py cdf','NL Queries':['Delete the following files: abc.txt,efg.py and cdf.','Remove multiple files from this directory: abc.txt, efg.py, cdf.']},ignore_index=True)
rm = rm.append({'Command':'rm -f log{1..5}.txt','NL Queries':['Delete all files with names starting with log, ending with .txt and numbers 1 to 5 in between.','Remove 5 files from this directory. Names start with the word log, have numbers 1 to 5 after,end with .txt']},ignore_index=True)
rm = rm.append({'Command':'rm *','NL Queries':['Remove all files in current directory.','Empty this folder by deleting all files.','Delete all files of this folder.']},ignore_index = True)

print rm