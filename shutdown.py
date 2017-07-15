import pandas as pd 

shutdown = pd.DataFrame(columns = ['Command','NL Queries'])

shutdown = shutdown.append({'Command':'shutdown -h now','NL Queries':['Halt and shut the system down now.','Shutdown this system now.']},ignore_index=True)
shutdown = shutdown.append({'Command':'shutdown -h +5 "Server is going down for upgrade. Please save your work."','NL Queries':['Shutdoen the system in 5 minutes. Flash a message "Server is going down for upgrade. Please save your work."','How do I shut down my system after 5 minutes with a mesasge "Server is going down for upgrade. Please save your work."']},ignore_index=True)
shutdown = shutdown.append({'Command':'shutdown -c','NL Queries':['Cancel shutdown of the system.','How do I keep my system on and not power off?','How do I interrupt the power off of the system?']},ignore_index=True)

print shutdown


