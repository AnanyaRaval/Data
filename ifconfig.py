import pandas as pd 

ifconfig = pd.DataFrame(columns = ['Command','NL Queries'])

ifconfig = ifconfig.append({'Command':'ifconfig','NL Queries':['Show all interactive network interface details.','How do I check link, hardware address, inetaddress, broadcast address etc. of all network interfaces?','How do I check which network hardware I have in my computer?']},ignore_index=True)
ifconfig = ifconfig.append({'Command':'ifonfig eth0 up','NL Queries':['Turn device eth0 up.','Turn card eth0 up.','How do I turn up my eth0 card?']},ignore_index=True)
ifconfig = ifconfig.append({'Command':'ifconfig eth0 172.16.25.125','NL Queries':['Make ip address of eth0 to be 172.16.25.125.','How do I assign ip address 172.16.25.125 to inerface eth0?','Change ip address of eth0 = 172.16.25.125.']},ignore_index=True)

print ifconfig


