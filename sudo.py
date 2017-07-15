import pandas as pd 

sudo = pd.DataFrame(columns = ['Command','NL Queries'])

sudo = sudo.append({'Command':'sudo -u comphope ls /home/comphope/hope','NL Queries':['List the contents of the /home/comphope/hope directory as the comphope user.','See contents of /home/comphope/hope as user comphope.']},ignore_index=True)
sudo = sudo.append({'Command':'sudo k','NL Queries':['Kill authentication of current user.','How do I terminate authentication of current active user.']},ignore_index=True)

print sudo


