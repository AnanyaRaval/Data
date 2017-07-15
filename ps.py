import pandas as pd 

ps = pd.DataFrame(columns = ['Command','NL Queries'])

ps = ps.append({'Command':'ps -ef','NL Queries':['Show all processes.','Display the state of all process currently being executed on the system.','Show p']},ignore_index=True)
ps = ps.append({'Command':'ps -f -u www-data','NL Queries':['Show processes runn by user www-data.','How do I see the state of all processes run by www-data?',]},ignore_index=True)
ps = ps.append({'Command':'ps -f -p 3150,7298,6544','NL Queries':['Show state of process of the following ids:3150,7298,654.','How do I check the status of processes 3150,6544 and 7298?']},ignore_index=True)

print ps


