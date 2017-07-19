import pandas as pd 

sleep = pd.DataFrame(columns = ['Command','NL Queries'])

sleep = sleep.append({'Command':'sleep 4','NL Queries':['Sleep for 4 seconds', 'Pause command line for 4 seconds.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 8s','NL Queries':['Make command line sleep for 8 seconds.','Sleep for 8 seconds.',
							'Suspend current process for 8 seconds.','Pause for 8 seconds.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 10m','NL Queries':['Make command line sleep for 10 minutes.','Sleep for 10 minutes.',
						'Suspend current process for 10 minutes.','Pause for 8 minutes.','Pause command line for 8 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 2h','NL Queries':['Make command line sleep for 2 hours.','Sleep for 2 hours.',
							'Suspend current process for 2 hours.','Pause for 2 hours.','Pause command line for 2 hours.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 3d','NL Queries':['Make command line sleep for 3 days.','Sleep for 3 days.',
						'Suspend current process for 3 days.''Pause for 3 days.','Pause command line for 3 days.']},ignore_index=True)
#----
#Add permutations (s,m),(s,h),(s,d)
sleep = sleep.append({'Command':'sleep 7 3s','NL Queries':['Make command line sleep for 7 seconds and then 3 seconds.',
						'Sleep for 7 seconds + 3 seconds.','Suspend current process for 7 seconds first and then 3 seconds.','Pause command line for 7 seconds and 3 seconds.'
						'Pause for 7 and then 3 seconds.']},ignore_index=True)
# Add permutations (m,h),(m,d), (m,m)
sleep = sleep.append({'Command':'sleep 1m 30s','NL Queries':['Make command line sleep for 1 minute and 30 seconds.','Sleep for 1.5 minutes.',
									'Suspend current process for 1.5 minutes.','Pause for 1 minute and 30 seconds.',
										'Pause command line for 1 minute and then 30 seconds.']},ignore_index=True)
#Add permutations (h,s),(h,d),(h,h)
sleep = sleep.append({'Command':'sleep 1h 30m','NL Queries':['Make command line sleep for 1 hour and 30 minutes.','Sleep for 1 hour and 30 minutes.',
													'Suspend current process for 1.5 hours.','Pause command line for 1 hour 30 minutes.'
													'Pause for 1 hour and then 30 minutes.']},ignore_index=True)
#Add permutations (d,s), (d,m), (d,d)
sleep = sleep.append({'Command':'sleep 1d 6h','NL Queries':['Make command line sleep for 1 day, 6 hours.',
											'Sleep for 1 day, 6 hours.','Suspend current process for 1 day, 6 hours.',
											'Pause for a day and then 6 hours.','Pause command line for 1 day and then for 6 hoours more.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 1.5m','NL Queries':['Make command line sleep for 1.5 minutes.','Sleep for 1.5 minutes.','Suspend current process for 1.5 minutes.',
												'Pause for 1.5 minutes.','Pause command line for 1.5 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 0.001s','NL Queries':['Make command line sleep for a millisecond.',
									'Sleep for 1 milli second.','Suspend current process for 1 millisecond.','Sleep for a time 10^-3 of a second.',
									'Pause for 0.001 second.','Pause command line for 10^-3 of a second.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 2.5m','NL Queries':['Make command line sleep for 2.5 minutes.','Sleep for 2.5 minutes.','Suspend current process for 2.5 minutes.',
													'Pause command line for 2.5 minutes exactly.','Pause for 2.5 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 1.5h 10m','NL Queries':['Make command line sleep for 1 hour and 40 minutes.','Sleep for 1 hour and 40 minutes.','Suspend current process for 1 hour and 40 minutes.',
						'Pause for 1.5 hours and then 10 minutes more.','Pause command line for 1.5 hours + 10 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 1.0e-1m','NL Queries':['Make command line sleep for 1e-1  minute.','Sleep for 1/10 minute.','Suspend current process for 10^-1 minutes.',
								'Pause for 1.0e-1 minutes.','Pause command line for 1.0e-1 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 1h 2m 3s','NL Queries':['Make command line sleep for 1 hour,2 minutes and 3 seconds.','Sleep for 1 hr, 2 min, 3 sec.',
							'Pause command line for 1 hours, 2 minutes and 3 seconds.','Pause for 1 hour, 2 minutes and 3 seconds.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep --help','NL Queries':['Display man page for sleep in command line.','What are the options for sleep command ?','Help for sleep command.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep --version','NL Queries':['Display the version info for sleep.','What is the version for sleep command ?','Version for sleep command.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 3h; gedit','NL Queries':['Open gedit application after 3 hours.','Sleep for 3 hours, then open gedit.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 0.5m;vim a.txt','NL Queries':['Make command line sleep for 10 minutes.','Sleep for 10 minutes.','Suspend current process for 10 minutes.']},ignore_index=True)


#sleep = sleep.append({'Command':'sleep 60s;vim','NL Queries':['Open vim after one minute.','Sleep for 1 min, then open vim.']},ignore_index=True)



#sleep = sleep.append({'Command':'man sleep','NL Queries':['Man page for sleep command.','Manual for sleep command.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 1m;echo "Hi"','NL Queries':['Make command line sleep for 1 minute.Print "Hi" in command line','Print "Hi" in command line after a minute.']},ignore_index=True)


#sleep = sleep.append({'Command':'sleep 10m','NL Queries':['Make command line sleep for 10 minutes.','Sleep for 10 minutes.','Suspend current process for 10 minutes.']},ignore_index=True)

print sleep

    
