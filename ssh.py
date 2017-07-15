import pandas as pd 

ssh = pd.DataFrame(columns = ['Command','NL Queries'])

ssh = ssh.append({'Command':'ssh jhawkins@collie.stanford.edu','NL Queries':['Login to collie.stanford.edu with username jhawkins.','Command to remote login. Username is jhawkins. Remote host is collie.stanford.edu.']},ignore_index = True)
ssh = ssh.append({'Command':'ssh -l uname gatech','NL Queries':['Login to server with uname.','How do I login to a remote server with username uname and server name gatech.']},ignore_index=True)
ssh = ssh.append({'Command':'ssh 192.168.0.103 -p 1234','NL Queries':['Connect to address 192.168.0.03 to port 1234.','How do I connect to server 192.168.0.103 and port 1234']},ignore_index=True)

print ssh

