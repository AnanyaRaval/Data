import pandas as pd 

kill = pd.DataFrame(columns = ['Command','NL Queries'])

kill = kill.append({'Command':'kill -l','NL Queries':['List signal names for kill.','Show all types of ways to terminate a perocess.']},ignore_index=True)

print kill


