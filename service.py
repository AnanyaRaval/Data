import pandas as pd 

service = pd.DataFrame(columns = ['Command','NL Queries'])

service = service.append({'Command':'service sshd stop','NL Queries':['Stop the sshd service.','How do I stop the sshd service?']},ignore_index=True)
service = service.append({'Command':'service sshd start','NL Queries':['Start the sshd service','How do I start the sshd service?']},ignore_index=True)
service = service.append({'Command':'service sshd restart','NL Queries':['Restart the sshd service.','How do I restart the sshd serivce?']},ignore_index=True)


print service


