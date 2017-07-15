import pandas as pd 

pwd = pd.DataFrame(columns = ['Command','NL Queries'])

pwd = pwd.append({'Command': 'pwd','NL Queries' :['Current Directory','Where am I?', "What is my current path?","What is the path till current directory?","Working Directory"]},ignore_index = True)
pwd = pwd.append({'Command': 'pwd -L','NL Queries' :['Print working directory from environment','What is my logical working directory?','Working Directory with symbolic links']},ignore_index = True)
pwd = pwd.append({'Command': 'pwd -P', 'NL Queries': ['Print current physical directory', 'What is current physical location','Print current directory. Ignore symbolic links',]},ignore_index = True)

pwd.to_csv('pwd.csv',index = False)