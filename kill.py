import pandas as pd 

kill = pd.DataFrame(columns = ['Command','NL Queries'])

kill = kill.append({'Command':'kill -l','NL Queries':['List signal names which can be sent to a process.',
													'Show all types of ways to terminate a process.',
													'Display a list of signlas which can be sent to the currently executing processes of the system.']},ignore_index=True)

kill = kill.append({'Command':'kill 485','NL Queries':['Terminate process with PID 485.',
														'How do I end process having PID 485?',
														'Command to make process 485 stop executing.']},ignore_index=True)

kill = kill.append({'Command':'kill -l 11','NL Queries':[' Show the signal number 11 to it\'s name.',
														'What is the  name of signal 11?',
														'Display the string name of signal number 11.']},ignore_index=True)

kill = kill.append({'Command':'kill 123 543 2341 3453','NL Queries':['End all processes with ids 123 543 2341 3453.',
																	'Terminate all processes with ids 123 543 2341 3453.',
																	'How do I end processses 123 543 2341 3453?']},ignore_index=True)

kill = kill.append({'Command':'kill SIGTERM 986','NL Queries':['Send SIGTERM to process 986.',
																'How do I send the SIGTERM singla to the process with PID 986.',
																'Command to send signal SIGTERM to currently executing process 986.']},ignore_index=True)

#kill.to_csv('/home/ananyaraval/Documents/Thesis/Data/UNIX/csv_files/kill.csv',index=False)
print kill.shape


