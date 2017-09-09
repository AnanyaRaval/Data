import pandas as pd 

sleep = pd.DataFrame(columns = ['Command','NL Queries'])
.
sleep = sleep.append({'Command':'sleep 4','NL Queries':['Pause shell for 4 seconds.',
														 'Pause command line for 4 seconds.',
														 'Suspend current processes for4 seconds .']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 8s','NL Queries':['Make command line pause for 8 seconds.',
														'Delay for 8 seconds.',
														'Suspend current process for 8 seconds.',
														'Pause for 8 seconds.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 10m','NL Queries':['Make command line pause for 10 minutes.',
														'Delay for 10 minutes.',
														'Suspend current process for 10 minutes.',
														'Pause for 8 minutes.',
														'Pause command line for 8 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 2h','NL Queries':['Make command line pause for 2 hours.',
														'Delay for 2 hours.',
														'Suspend current process for 2 hours.',
														'Pause for 2 hours.',
														'Pause command line for 2 hours.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 3d','NL Queries':['Make command line pause for 3 days.',
														'Delay for 3 days.',
														'Suspend current process for 3 days.',
														'Pause for 3 days.',
														'Pause command line for 3 days.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 7 3s','NL Queries':['Make command line pause for 7 seconds and then 3 seconds.',
														'Delay for 7 seconds + 3 seconds.',
														'Suspend current process for 7 seconds first and then 3 seconds.',
														'Pause command line for 7 seconds and 3 seconds.',
														'Pause for 7 and then 3 seconds.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 5s 2m','NL Queries':['Make command line pause for 5 seconds and then 2 minutes.',
															'Delay for 5 seconds + 2 minutes.',
															'Suspend current process for 5 seconds first and then 2 minutes.',
															'Pause command line for 5 seconds and 2 hours.',
															'Pause for 5 seconds and then 3 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 4s 3h','NL Queries':['Make command line pause for 4 seconds and then 3 hours.',
															'Delay for 4 seconds + 3 hours.',
															'Suspend current process for 4 seconds first and then 3 hours.',
															'Pause command line for 4 seconds and 3 hours.',
															'Pause for 4 seconds and then 3 hours.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 6s 1d','NL Queries':['Make command line pause for 6 seconds and then 1 days.',
															'Delay for 6 seconds + 1 day.',
															'Suspend current process for 6 seconds first and then 1 day.',
															'Pause command line for 6 seconds and 1 day.',
															'Pause for 6 seconds and then 1 day.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 1m 30s','NL Queries':['Make command line pause for 1 minute and 30 seconds.',
															'Delay for 1.5 minutes.',
															'Suspend current process for 1.5 minutes.',
															'Pause for 1 minute and 30 seconds.',
															'Pause command line for 1 minute and then 30 seconds.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 7m 7m','NL Queries':['Make command line pause for 7 minutes + 7 minutes.',
															'Delay for 7 minutes and 7 minutes.',
															'Pause for 7 minutes and 7 minutes.',
															'Pause command line for 7 minutes and then 7 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 3m 4h','NL Queries':['Make command line pause for 3 minutes and 4 hours.',
															'Delay for 3 minutes and 4 hours.',
															'Pause for 3 minutes and 4 hours.',
															'Pause command line for 3 minutes and then 4 hours.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 20m 15d','NL Queries':['Make command line pause for 20 minutes and 15 days.',
															'Delay for 20 minutes and 15 days.',
															'Pause for 20 minutes and 15 days.',
															'Pause command line for 20 minutes and then 15 days.']},ignore_index=True)

#Add permutations (h,s),(h,d),(h,h)

sleep = sleep.append({'Command':'sleep 1h 15s','NL Queries':['Make command line pause for 1 hour and 15 seconds.',
															'Delay for 1 hour and 15 seconds.',
															'Suspend current process for 1 hour + 15 seconds.',
															'Pause command line for 1 hour 15 seconds.',
															'Pause for 1 hour and then 15 seconds.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 2h 30m','NL Queries':['Make command line pause for 2 hours and 30 minutes.',
															'Delay for 2 hours and 30 minutes.',
															'Pause command line for 2 hours 30 minutes.',
															'Pause for 2 hours and then 30 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 1h 3h','NL Queries':['Make command line pause for 1 hour and 3 hours.',	
															'Delay for 1 hour + 3 hours.',
															'Suspend current process for 1 hour + 3 hours.',
															'Pause command line for 1 hour + 3 hours.',
															'Pause for 1 hour and then 3 hours.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 5h 4d','NL Queries':['Make command line pause for 5 hours and 4 days.',
															'Delay for 5 hours and 4 days.',
															'Suspend current process for 5 hours + 4 days.',
															'Pause command line for 5 hours 4 days.',
															'Pause for 4 hours and then 5 days.']},ignore_index=True)

#Add permutations (d,s), (d,m), (d,d)

sleep = sleep.append({'Command':'sleep 2d 3s','NL Queries':['Make command line pause for 2 days, 3 seconds.',
															'Delay for 2 days, 3 seconds.',
															'Suspend current process for 2 days, 3 seconds.',
															'Pause for 2 days and then 3 seconds.',
															'Pause command line for 2 days and then for 3 seconds more.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 1d 6h','NL Queries':['Make command line pause for 1 day, 6 hours.',
															'Delay for 1 day, 6 hours.',
															'Suspend current process for 1 day, 6 hours.',
															'Pause for a day and then 6 hours.',
															'Pause command line for 1 day and then for 6 hours more.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 3d 4m','NL Queries':['Make command line pause for 3 days, 4 minutes.',
															'Delay for days, 4 minutes.',
															'Suspend current process for 3 days, 4 minutes.',
															'Pause for 3 days and then 4 minutes.',
															'Pause command line for 3 days and then for 4 minutes more.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 3d 4d','NL Queries':['Make command line pause for 3 days, 4 days.',
															'Delay for 3 days, 4 days.',
															'Suspend current process for 3 days, 4 days.',
															'Pause for 3 days and then 4 days.',
															'Pause command line for 3 days and then for 4 days more.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 1.5m','NL Queries':['Make command line sleep for 1.5 minutes.','Sleep for 1.5 minutes.','Suspend current process for 1.5 minutes.','Pause for 1.5 minutes.','Pause command line for 1.5 minutes.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 0.001s','NL Queries':['Make command line sleep for a millisecond.','Sleep for 1 milli second.','Suspend current process for 1 millisecond.','Sleep for a time 10^-3 of a second.','Pause for 0.001 second.','Pause command line for 10^-3 of a second.']},ignore_index=True)


#sleep = sleep.append({'Command':'sleep 1.5h 10m','NL Queries':['Make command line sleep for 1 hour and 40 minutes.','Sleep for 1 hour and 40 minutes.','Suspend current process for 1 hour and 40 minutes.','Pause for 1.5 hours and then 10 minutes more.','Pause command line for 1.5 hours + 10 minutes.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 1.0e-1m','NL Queries':['Make command line sleep for 1e-1  minute.','Sleep for 1/10 minute.','Suspend current process for 10^-1 minutes.','Pause for 1.0e-1 minutes.','Pause command line for 1.0e-1 minutes.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 1h 2m 3s','NL Queries':['Make command line pause for 1 hour,2 minutes and 3 seconds.',
																'Delay for 1 hr, 2 min, 3 sec.',
																'Pause command line for 1 hours, 2 minutes and 3 seconds.',
																'Pause for 1 hour, 2 minutes and 3 seconds.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep --help','NL Queries':['Display man page for sleep in command line.',
															'What are the options for sleep command ?',
															'Help for sleep command.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep --version','NL Queries':['Display the version information for sleep.',
																'What is the version for sleep command ?',
																'Version for sleep command.']},ignore_index=True)

sleep = sleep.append({'Command':'sleep 12s 2s 4s','NL Queries':['Make command line pause for 12 seconds , 2 seconds and 4 seconds.',
																'Delay for 12 seconds , 2 seconds and 4 seconds.',
																'Suspend current process for 12 seconds + 2 seconds + 4 seconds.',
																'Pause command line for 12 seconds , 2 seconds and 4 seconds.',
																'Pause for 12 seconds , 2 seconds and then 4 seconds.']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 6s 16s 5m','NL Queries':['Make command line pause for 6 seconds , 16 seconds and 5 minutes.',
																'Delay for 6 seconds , 16 seconds and 5 minutes.',
																'Suspend current process for 6 seconds + 16 seconds + 5 minutes .',
																'Pause command line for 6 seconds , 16 seconds and 5 minutes.',
																'Pause for 6 seconds , 16 seconds and then 5 minutes.']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 8s 17s 13h','NL Queries':['Make command line pause for 8 seconds , 17 seconds and 13 hours .',
																'Delay for 8 seconds , 17 seconds and 13 hours .',
																'Suspend current process for 8 seconds + 17 seconds + 13 hours .',
																'Pause command line for 8 seconds , 17 seconds and 13 hours .',
																'Pause for 8 seconds , 17 seconds and then 13 hours .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 2s 2s 12d','NL Queries':['Make command line pause for 2 seconds , 2 seconds and 12 days.',
																'Delay for 2 seconds , 2 seconds and 12 days .',
																'Suspend current process for 2 seconds + 2 seconds + 12 days .',
																'Pause command line for 2 seconds , 2 seconds and 12 days .',
																'Pause for 2 seconds , 2 seconds and then 12 days .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 2s 11m 15m','NL Queries':['Make command line pause for 2 seconds , 11 minutes and 15 minutes .',
																'Delay for 2 seconds , 11 minutes and 15 minutes .',
																'Suspend current process for 2 seconds + 11 minutes + 15 minutes .',
																'Pause command line for 2 seconds , 11 minutes and 15 minutes .',
																'Pause for 2 seconds , 11 minutes and then 15 minutes .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 14s 13m 14h','NL Queries':['Make command line pause for 14 seconds , 13 minutes and 14 hours .',
																'Delay for 14 seconds , 13 minutes and 14 hours .',
																'Suspend current process for 14 seconds + 13 minutes + 14 hours .',
																'Pause command line for 14 seconds , 13 minutes and 14 hours .',
																'Pause for 14 seconds , 13 minutes and then 14 hours .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 10s 18m 6d','NL Queries':['Make command line pause for 10 seconds , 18 minutes and 6 days .',
																'Delay for 10 seconds , 18 minutes and 6 days .',
																'Suspend current process for 10 seconds + 18 minutes + 6 days .',
																'Pause command line for 10 seconds , 18 minutes and 6 days .',
																'Pause for 10 seconds , 18 minutes and then 6 days .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 4s 10h 14h','NL Queries':['Make command line pause for 4 seconds , 10 hours and 14 hours .',
																'Delay for 4 seconds , 10 hours and 14 hours .',
																'Suspend current process for 4 seconds + 10 hours + 14 hours .',
																'Pause command line for 4 seconds , 10 hours and 14 hours .',
																'Pause for 4 seconds , 10 hours and then 14 hours .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 5s 3h 5d','NL Queries':['Make command line pause for 5 seconds , 3 hours and 5 days .',
																'Delay for 5 seconds , 3 hours and 5 days .',
																'Suspend current process for 5 seconds + 3 hours + 5 days .',
																'Pause command line for 5 seconds , 3 hours and 5 days .',
																'Pause for 5 seconds , 3 hours and then 5 days .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 10s 5d 11d','NL Queries':['Make command line pause for 10 seconds , 5 days and 11 days .',
																'Delay for 10 seconds , 5 days and 11 days .',
																'Suspend current process for 10 seconds + 5 days + 11 days .',
																'Pause command line for 10 seconds , 5 days and 11 days .',
																'Pause for 10 seconds , 5 days and then 11 days .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 4m 8m 19m','NL Queries':['Make command line pause for 4 minutes , 8 minutes and 19 minutes .',
																'Delay for 4 minutes , 8 minutes and 19 minutes .',
																'Suspend current process for 4 minutes + 8 minutes + 19 minutes .',
																'Pause command line for 4 minutes , 8 minutes and 19 minutes .',
																'Pause for 4 minutes , 8 minutes and then 19 minutes .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 20m 3m 13h','NL Queries':['Make command line pause for 20 minutes , 3 minutes and 13 hours .',	
																'Delay for 20 minutes , 3 minutes and 13 hours .',
																'Suspend current process for 20 minutes + 3 minutes + 13 hours .',
																'Pause command line for 20 minutes , 3 minutes and 13 hours .',
																'Pause for 20 minutes , 3 minutes and then 13 hours .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 12m 15m 12d','NL Queries':['Make command line pause for 12 minutes , 15 minutes and 12 days .',
																'Delay for 12 minutes , 15 minutes and 12 days .',
																'Suspend current process for 12 minutes + 15 minutes + 12 days .',
																'Pause command line for 12 minutes , 15 minutes and 12 days .',
																'Pause for 12 minutes , 15 minutes and then 12 days .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 4m 3h 17h','NL Queries':['Make command line pause for 4 minutes , 3 hours and 17 hours .',
																'Delay for 4 minutes , 3 hours and 17 hours .',
																'Suspend current process for 4 minutes + 3 hours + 17 hours .',
																'Pause command line for 4 minutes , 3 hours and 17 hours .',
																'Pause for 4 minutes , 3 hours and then 17 hours .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 9m 7h 9d','NL Queries':['Make command line pause for 9 minutes , 7 hours and 9 days .',
																'Delay for 9 minutes , 7 hours and 9 days .',
																'Suspend current process for 9 minutes + 7 hours + 9 days .',
																'Pause command line for 9 minutes , 7 hours and 9 days .',
																'Pause for 9 minutes , 7 hours and then 9 days .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 18m 9d 15d','NL Queries':['Make command line pause for 18 minutes , 9 days and 15 days .',
																'Delay for 18 minutes , 9 days and 15 days .',
																'Suspend current process for 18 minutes + 9 days + 15 days .',
																'Pause command line for 18 minutes , 9 days and 15 days .',
																'Pause for 18 minutes , 9 days and then 15 days .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 5h 17h 6h','NL Queries':['Make command line pause for 5 hours , 17 hours and 6 hours .',
																'Delay for 5 hours , 17 hours and 6 hours .',
																'Suspend current process for 5 hours + 17 hours + 6 hours .',
																'Pause command line for 5 hours , 17 hours and 6 hours .',
																'Pause for 5 hours , 17 hours and then 6 hours .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 9h 13h 13d','NL Queries':['Make command line pause for 9 hours , 13 hours and 13 days .',
																'Delay for 9 hours , 13 hours and 13 days .',
																'Suspend current process for 9 hours + 13 hours + 13 days .',
																'Pause command line for 9 hours , 13 hours and 13 days .',
																'Pause for 9 hours , 13 hours and then 13 days .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 11h 15d 10d','NL Queries':['Make command line pause for 11 hours , 15 days and 10 days .',
																'Delay for 11 hours , 15 days and 10 days .',
																'Suspend current process for 11 hours + 15 days + 10 days .',
																'Pause command line for 11 hours , 15 days and 10 days .',
																'Pause for 11 hours , 15 days and then 10 days .']},ignore_index=True)


sleep = sleep.append({'Command':'sleep 12d 9d 14d','NL Queries':['Make command line pause for 12 days , 9 days and 14 days .',
																'Delay for 12 days , 9 days and 14 days .',
																'Suspend current process for 12 days + 9 days + 14 days .',
																'Pause command line for 12 days , 9 days and 14 days .',
																'Pause for 12 days , 9 days and then 14 days .']},ignore_index=True)


#sleep = sleep.append({'Command':'sleep 3h; gedit','NL Queries':['Open gedit application after 3 hours.','Sleep for 3 hours, then open gedit.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 0.5m;vim a.txt','NL Queries':['Make command line sleep for 10 minutes.','Sleep for 10 minutes.','Suspend current process for 10 minutes.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 60s;vim','NL Queries':['Open vim after one minute.','Sleep for 1 min, then open vim.']},ignore_index=True)

#sleep = sleep.append({'Command':'man sleep','NL Queries':['Man page for sleep command.','Manual for sleep command.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 1m;echo "Hi"','NL Queries':['Make command line sleep for 1 minute.Print "Hi" in command line','Print "Hi" in command line after a minute.']},ignore_index=True)

#sleep = sleep.append({'Command':'sleep 10m','NL Queries':['Make command line sleep for 10 minutes.','Sleep for 10 minutes.','Suspend current process for 10 minutes.']},ignore_index=True)

#print sleep
#sleep.to_csv('/home/ananyaraval/Documents/Thesis/Data/UNIX/csv_files/sleep.csv',index=False)
print sleep.shape	
