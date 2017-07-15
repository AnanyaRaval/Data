import pandas as pd 

wc = pd.DataFrame(columns = ['Command','NL Queries'])

wc = wc.append({'Command':'wc -l general.py','NL Queries':['Print number of lines in the file.','How do I know the number of liens in general.py?','Show total number of lines in the file general.py.']},ignore_index=True)

print wc


