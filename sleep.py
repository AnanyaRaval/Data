import pandas as pd 

sleep = pd.DataFrame(columns = ['Command','NL Queries'])

sleep = sleep.append({'Command':'sleep 4','NL Queries':['Sleep for 4 seconds', 'Pause command line for 4 seconds.']},ignore_index=True)
sleep = sleep.append({'Command':'sleep 10m','NL Queries':['Make command line sleep for 10 minutes.','Sleep for 10 minutes.','Suspend current process for 10 minutes.']},ignore_index=True)
sleep = sleep.append({'Command':'sleep 3h; gedit','NL Queries':['Open gedit application after 3 hours.','Sleep for 3 hours, then open gedit.']},ignore_index=True)

print sleep


