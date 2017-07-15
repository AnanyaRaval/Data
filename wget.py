import pandas as pd 

wget = pd.DataFrame(columns = ['Command','NL Queries'])

wget = wget.append({'Command':'wget http://fly.srk.fer.hr/','NL Queries':['Download data from URL http://fly.srk.fer.hr/','How to get data from link http://fly.srk.fer.hr/']},ignore_index=True)
wget = wget.append({'Command':'wget -t 45 -o log http://fly.srk.fer.hr/jpg/flyweb.jpg &','NL Queries':['Download data from link: http://fly.srk.fer.hr/jpg/flyweb.jpg.Try 45 times and write progress to logfile.Run wget in the background.']},ignore_index=True)
wget = wget.append({'Command':'wget -i ananya.txt','NL Queries':['Get data from links listed in file ananya.txt.','Download data from multiple links specified in the file ananya.txt.']},ignore_index=True)

print wget

