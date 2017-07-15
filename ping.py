import pandas as pd 

ping = pd.DataFrame(columns = ['Command','NL Queries'])

ping = ping.append({'Command':'ping -i 127.0.0.1','NL Queries':['Find out whether address 127.0.0.1 is reachable. Send packet every 5 seconds.','Ping IP address 127.0.0.1. Time interval between packets should be minutes.']},ignore_index=True)
ping = ping.append({'Command':'ping 0','NL Queries':['Ping local host.','How do I check whether local inteface is up?','Check local host connectivity by pinging.']},ignore_index=True)
ping = ping.append({'Command':'ping -s 100 localhost','NL Queries':['Send packet of size 100 bytes to local host.','Check connectivity of localhost by sending packet of size 100.']},ignore_index=True)

print ping


