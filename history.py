import pandas as pd 

history = pd.DataFrame(columns = ['Command','NL Queries'])

history = history.append({'Command':'history','NL Queries':['Show all commands in this session.',
															'How do I check the previous commands executed on this shell?',
															'See a list of UNIX commands typed in this terminal.']},ignore_index=True)

history = history.append({'Command':'history -c','NL Queries':['Clear the whole list of commands typed in the session.',
																'Command to delete the list of all commands.',
																'How do I delete all commands which were executed in this session?']},ignore_index=True)

history = history.append({'Command':'history 5','NL Queries':['Show the lasst 5 commands executed in this session.',
																'How do I see a list of last 5 Linux commands executed in this session?',
																'Display 5 most recent commands executed in this session.']},ignore_index=True)

history = history.append({'Command':'history -a','NL Queries':['Write the current commands executed to history file.',
																'Command to write the new linux commands to history file.',
																'How do I immediately write the new commands executed in command line to the history file?']},ignore_index=True)

#history.to_csv('/home/ananyaraval/Documents/Thesis/Data/UNIX/csv_files/history.csv',index=False)
print history.shape


