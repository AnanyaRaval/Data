import pandas as pd 

history = pd.DataFrame(columns = ['Command','NL Queries'])

history = history.append({'Command':'history','NL Queries':['Show all commands in this session.','How do I check the previous commands executed on this shell?','See a list of UNIX commands typed in this terminal.']},ignore_index=True)
history = history.append({'Command':'history -c','NL Queries':['Clear the whole list of commands typed in the session.','Command to delete the list of all commands.']},ignore_index=True)

print history


