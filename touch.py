import pandas as pd 

touch = pd.DataFrame(columns = ['Command','NL Queries'])

touch = touch.append({'Command':'touch abc.py','NL Queries':['Create new file abc.py in current directory. Do not open it.','How do I create a new file abc.py via command line?','Make file abc.py.']},ignore_index = True)
touch = touch.append({'Command':'touch -a filename','NL Queries':['Change access time of file filename. Set it to current value from system.','How do I change values of access time of file filename to current time?']},ignore_index = True)
touch = touch.append({'Command':'touch -r file1 file2','NL Queries':['Update timestamp of file1 with file2.','How do I copy timestamp of file2 with that of file1?']},ignore_index = True)

print touch