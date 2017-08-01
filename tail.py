import pandas as pd 

tail = pd.DataFrame(columns = ['Command','NL Queries'])

tail = tail.append({'Command':'tail -c 500 /var/log/messages','NL Queries':['Show last 500 bytes of /var/log/messages.',
							'How do I see ending of /var/log/messages? I want to see only last 500 bytes.']},ignore_index=True)

tail = tail.append({'Command':'tail -c 500 /var/log/messages lol.txt','NL Queries':['Show last 500 bytes of /var/log/messages and lol.txt.',
										'How do I see ending of /var/log/messages and lol.txt? I want to see only last 500 bytes of both.']},ignore_index=True)

#tail = tail.append({'Command':'tail -c 500k /var/log/messages','NL Queries':['Show last 500k(500 x 1024) bytes of /var/log/messages.','How do I see ending of /var/log/messages? I want to see only last 500k bytes.']},ignore_index=True)

#Incomplete Description. Add description for -f
#tail = tail.append({'Command':'tail -f /var/log/secure /var/log/cron','NL Queries':['Show last few lines of /var/log/secure and /var/log/cron.','How do I see ending of /var/log/cron and /var/log/secure?']},ignore_index=True)

tail = tail.append({'Command':'tail -f /var/log/secure','NL Queries':['Show last few lines of /var/log/secure.',
															'How do I see ending of /var/log/secure?']},ignore_index=True)

tail = tail.append({'Command':'tail lol.txt','NL Queries':['Show last 10 lines of lol.txt.',
													'How do I see last 10 lines of lol.txt?',
													'How can I see last 10 lines of some file?']},ignore_index=True)

#tail = tail.append({'Command':'tail lol.txt lol2.txt','NL Queries':['Show last 10 lines of both lol.txt and lol2.txt.','How do I see last 10 lines of lol.txt and lol2.txt?','How can i see last 10 lines of mutiple files in single command?']},ignore_index=True)

tail = tail.append({'Command':'tail -n7 lol.txt','NL Queries':['Show last 7 lines of lol.txt.',
											'How do I see last 7 lines of lol.txt?',
											'How can I see last 7 lines of lol.txt?']},ignore_index=True)

#tail = tail.append({'Command':'tail -n7 lol.txt lol2.txt','NL Queries':['Show last 7 lines of lol.txt nad lol2.txt.','How do I see last 7 lines of lol.txt and lol2.txt?','How can i see last n lines of lol.txt and lol2.txt?']},ignore_index=True)

tail = tail.append({'Command':'tail -7 lol.txt','NL Queries':['Show last 7 lines of lol.txt.',
															'How do I see last 7 lines of lol.txt?',
															'How can I see last 7 lines of lol.txt?']},ignore_index=True)

#tail = tail.append({'Command':'tail -7 lol.txt lol2.txt','NL Queries':['Show last 7 lines of lol.txt nad lol2.txt.','How do I see last 7 lines of lol.txt and lol2.txt?','How can i see last n lines of lol.txt and lol2.txt?']},ignore_index=True)

tail = tail.append({'Command':'tail -n+2 lol.txt','NL Queries':['Show all lines starting from line no. 2 of lol.txt.',
													'How do I see all lines starting from line no. 2 of lol.txt?',
													'How can I see all lines starting from line no. 2?']},ignore_index=True)

#tail = tail.append({'Command':'tail -n+2 lol.txt lol2.txt','NL Queries':['Show all lines starting from line no. 2 of lol.txt and lol2.txt.','How do I see all lines starting from line no. 2 of lol.txt and lol2.txt?','How can i see all lines starting from line no. n for multiple files at once?']},ignore_index=True)

tail = tail.append({'Command':'tail -c+80 lol.txt','NL Queries':['Print all characters starting from 80th character of lol.txt.',
																'How do I print all characters starting from 80th character of lol.txt?',
																'How can I see all characters starting from 80th character of lol.txt']},ignore_index=True)

#tail = tail.append({'Command':'tail -c+80 lol.txt lol2.txt','NL Queries':['Print all characters starting from 80th character of lol.txt and lol2.txt.','How do I Prints all characters starting from 80th character of lol.txt and lol2.txt?','How can i see all caracters starting from nth character of lol.txt and lol2.txt']},ignore_index=True)

#tail = tail.append({'Command':'man tail','NL Queries':['Show all options of tail command.','How does Tail command works?','What\'s the power of tail command?']},ignore_index=True)

#tail = tail.append({'Command':'tail +2 lol.txt','NL Queries':['Show all lines starting from line no. 2 of lol.txt without use of -n option.',
#															'How do I see all lines starting from line no. 2 of lol.txt without use of -n option?',
#															'How can I see all lines starting from line no. n without use of -n option.?']},ignore_index=True)

##tail = tail.append({'Command':'tail +2 lol.txt lol2.txt','NL Queries':['Show all lines starting from line no. 2 of lol.txt and lol2.txt without use of -n option.','How do I see all lines starting from line no. 2 of lol.txt lol.txt and lol2.txt without use of -n option?','How can i see all lines starting from line no. n without use of -n option.?']},ignore_index=True)

#tail = tail.append({'Command':'tail +80c lol.txt','NL Queries':['Print all characters starting from 80th character of lol.txt without using - sign.','How do I Prints all characters starting from 80th character of lol.txt without using - sign?','How can i see all characters starting from nth character of lol.txt without using - sign?']},ignore_index=True)

#tail = tail.append({'Command':'tail +80c lol.txt lol2.txt','NL Queries':['Print all characters starting from 80th character of lol.txt and lol2.txt without using - sign.','How do I Prints all characters starting from 80th character of lol.txt and lol2.txt without using - sign?','How can i see all characters starting from nth character of lol.txt and lol2.txt without using - sign?']},ignore_index=True)

#tail = tail.append({'Command':'tail -n 12 lol.txt >> file.txt','NL Queries':['Fill last 12 lines of lol.txt into file.txt.','how can i send data of last 12 lines of lol.txt into file.txt?','How can I append output of tail of one file into another file?']},ignore_index=True)

#tail = tail.append({'Command':'tail lol.txt >> file.txt','NL Queries':['Fill last 10 lines of lol.txt into file.txt.','how can i send data of last 10 lines of lol.txt into file.txt?','How can I append output of tail of one file into another file?']},ignore_index=True)

#tail = tail.append({'Command':'tail -n 12 lol.txt lol2.txt >> file.txt','NL Queries':['Fill last 12 lines of lol.txt and lol2.txt into file.txt.','how can i send data of last 12 lines of lol.txt and lol2.txt into file.txt?','How can I append output of tail of more then one files into another file?']},ignore_index=True)

#tail = tail.append({'Command':'tail lol.txt lol2.txt >> file.txt','NL Queries':['Fill last 10 lines of lol.txt and lol2.txt into file.txt.','how can i send data of last 10 lines of lol.txt and lol2.txt into file.txt?','How can I append output of tail of more then one files into another file?']},ignore_index=True)
'''
tail = tail.append({'Command':'ls | tail','NL Queries':['Show last 10 lines of output of ls.','How can I print last 10 lines of output of ls?','How to see data of last 10 output of ls?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail','NL Queries':['Show last 10 lines of output of ls with detail.','How can I print last 10 lines of output of ls with details?','How to see data of last 10 output of ls with details?']},ignore_index=True)

tail = tail.append({'Command':'ls -la | tail','NL Queries':['Show last 10 lines of output of ls with hidden files and folders and in detail.','How can I print last 10 lines of output of ls with hidden files and folders and in detail?','How to see data of last 10 output of ls with hidden files and folders and in detail?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail','NL Queries':['Show last 10 lines of output of ls including hidden files.','How can I print last 10 lines of output of ls including hidden files?','How to see data of last 10 output of ls including hidden files?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail >> lol.txt','NL Queries':['Append last 10 lines of output of ls into file lol.txt.','How can I Append last 10 lines of output of ls into file lol.txt?','How to Append data of last 10 output of ls into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail >> lol.txt','NL Queries':['Append last 10 lines of output of ls with details into file lol.txt.','How can I Append last 10 lines of output of ls with details into file lol.txt?','How to Append data of last 10 output of ls with details into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail >> lol.txt','NL Queries':['Append last 10 lines of output of ls including hidden files into file lol.txt.','How can I Append last 10 lines of output of ls including hidden files into file lol.txt?','How to Append data of last 10 output of ls including hidden files into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail >> lol.txt','NL Queries':['Append last 10 lines of output of ls including hidden files and with details into file lol.txt.','How can I Append last 10 lines of output of ls including hidden files and with details into file lol.txt?','How to Append data of last 10 output of ls including hidden files and with details into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail > lol.txt','NL Queries':['Clear lol.txt and Append last 10 lines of output of ls into file lol.txt.','How can I Clear lol.txt and Append last 10 lines of output of ls into file lol.txt?','How to Clear lol.txt and Append data of last 10 output of ls into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail > lol.txt','NL Queries':['Clear lol.txt and Append last 10 lines of output of ls with details into file lol.txt.','How can I Clear lol.txt and Append last 10 lines of output of ls with details into file lol.txt?','How to Clear lol.txt and Append data of last 10 output of ls with details into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail > lol.txt','NL Queries':['Clear lol.txt and Append last 10 lines of output of ls including hidden files into file lol.txt.','How can I Clear lol.txt and Append last 10 lines of output of ls including hidden files into file lol.txt?','How to Clear lol.txt and Append data of last 10 output of ls including hidden files into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail > lol.txt','NL Queries':['Clear lol.txt and Append last 10 lines of output of ls including hidden files and with details into file lol.txt.','How can I Clear lol.txt and Append last 10 lines of output of ls including hidden files and with details into file lol.txt?','How to Clear lol.txt and Append data of last 10 output of ls including hidden files and with details into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail -n 2','NL Queries':['Show last 2 lines of output of ls.','How can I print last 10 lines of output of ls?','How to see data of last 2 output of ls?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail -n 2','NL Queries':['Show last 2 lines of output of ls with detail.','How can I print last 2 lines of output of ls with details?','How to see data of last 2 output of ls with details?']},ignore_index=True)

tail = tail.append({'Command':'ls -la | tail -n 2','NL Queries':['Show last 2 lines of output of ls with hidden files and folders and in detail.','How can I print last 2 lines of output of ls with hidden files and folders and in detail?','How to see data of last 2 output of ls with hidden files and folders and in detail?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail','NL Queries':['Show last 2 lines of output of ls including hidden files.','How can I print last 2 lines of output of ls including hidden files?','How to see data of last 2 output of ls including hidden files?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail  -n 2 >> lol.txt','NL Queries':['Append last 2 lines of output of ls into file lol.txt.','How can I Append last 2 lines of output of ls into file lol.txt?','How to Append data of last 2 output of ls into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail -n 2 >> lol.txt','NL Queries':['Append last 2 lines of output of ls with details into file lol.txt.','How can I Append last 2 lines of output of ls with details into file lol.txt?','How to Append data of last 2 output of ls with details into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail  -n 2 >> lol.txt','NL Queries':['Append last 2 lines of output of ls including hidden files into file lol.txt.','How can I Append last 2 lines of output of ls including hidden files into file lol.txt?','How to Append data of last 2 output of ls including hidden files into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail  -n 2 >> lol.txt','NL Queries':['Append last 2 lines of output of ls including hidden files and with details into file lol.txt.','How can I Append last 2 lines of output of ls including hidden files and with details into file lol.txt?','How to Append data of last 2 output of ls including hidden files and with details into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail  -n 2 > lol.txt','NL Queries':['Clear lol.txt and Append last 2 lines of output of ls into file lol.txt.','How can I Clear lol.txt and Append last 2 lines of output of ls into file lol.txt?','How to Clear lol.txt and Append data of last 2 output of ls into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail  -n 2 > lol.txt','NL Queries':['Clear lol.txt and Append last 2 lines of output of ls with details into file lol.txt.','How can I Clear lol.txt and Append last 2 lines of output of ls with details into file lol.txt?','How to Clear lol.txt and Append data of last 2 output of ls with details into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail  -n 2 > lol.txt','NL Queries':['Clear lol.txt and Append last 2 lines of output of ls including hidden files into file lol.txt.','How can I Clear lol.txt and Append last 2 lines of output of ls including hidden files into file lol.txt?','How to Clear lol.txt and Append data of last 2 output of ls including hidden files into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail  -n 2 > lol.txt','NL Queries':['Clear lol.txt and Append last 2 lines of output of ls including hidden files and with details into file lol.txt.','How can I Clear lol.txt and Append last 2 lines of output of ls including hidden files and with details into file lol.txt?','How to Clear lol.txt and Append data of last 2 output of ls including hidden files and with details into file lol.txt?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail | sort -r >> lol.txt','NL Queries':['Append last 10 lines of output of ls in reverse sorted way in lol.txt','How to append last 10 lines of output of ls in reverse sorted way in lol.txt?','How to Append last 10 lines of output of ls in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail | sort -r >> lol.txt','NL Queries':['Append last 10 lines of output of ls in details in reverse sorted way in lol.txt','How to append last 10 lines of output of ls in details in reverse sorted way in lol.txt?','How to Append last 10 lines of output of ls in details in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail | sort -r >> lol.txt','NL Queries':['Append last 10 lines of output of ls with hidden files in reverse sorted way in lol.txt','How to append last 10 lines of output of ls with hidden files in reverse sorted way in lol.txt?','How to Append last 10 lines of output of ls with hidden files in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail | sort -r >> lol.txt','NL Queries':['Append last 10 lines of output of ls with hidden files and details in reverse sorted way in lol.txt','How to append last 10 lines of output of ls with hidden files and details in reverse sorted way in lol.txt?','How to Append last 10 lines of output of ls with hidden files and details in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail | sort >> lol.txt','NL Queries':['Append last 10 lines of output of ls in sorted way in lol.txt','How to append last 10 lines of output of ls in sorted way in lol.txt?','How to Append last 10 lines of output of ls in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail | sort >> lol.txt','NL Queries':['Append last 10 lines of output of ls in details in sorted way in lol.txt','How to append last 10 lines of output of ls in details in sorted way in lol.txt?','How to Append last 10 lines of output of ls in details in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail | sort >> lol.txt','NL Queries':['Append last 10 lines of output of ls with hidden files in  sorted way in lol.txt','How to append last 10 lines of output of ls with hidden files in sorted way in lol.txt?','How to Append last 10 lines of output of ls with hidden files in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail | sort >> lol.txt','NL Queries':['Append last 10 lines of output of ls with hidden files and details in sorted way in lol.txt','How to append last 10 lines of output of ls with hidden files and details in sorted way in lol.txt?','How to Append last 10 lines of output of ls with hidden files and details in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail | sort -r > lol.txt','NL Queries':['Overwrite lol.txt with last 10 lines of output of ls in reverse sorted way in lol.txt','How to Overwrite lol.txt with last 10 lines of output of ls in reverse sorted way in lol.txt?','How to Overwrite lol.txt with last 10 lines of output of ls in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail | sort -r > lol.txt','NL Queries':['Overwrite lol.txt with last 10 lines of output of ls in details in reverse sorted way in lol.txt','How to Overwrite lol.txt with last 10 lines of output of ls in details in reverse sorted way in lol.txt?','How to Overwrite a file with last 10 lines of output of ls in details in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail | sort -r > lol.txt','NL Queries':['Overwrite lol.txt with last 10 lines of output of ls with hidden files in reverse sorted way in lol.txt','How to Overwrite lol.txt with last 10 lines of output of ls with hidden files in reverse sorted way in lol.txt?','How to Overwrite a file with last 10 lines of output of ls with hidden files in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail | sort -r > lol.txt','NL Queries':['Overwrite lol.txt with last 10 lines of output of ls with hidden files and details in reverse sorted way in lol.txt','How to Overwrite lol.txt with last 10 lines of output of ls with hidden files and details in reverse sorted way in lol.txt?','How to Overwrite a file with last 10 lines of output of ls with hidden files and details in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail | sort > lol.txt','NL Queries':['Overwrite lol.txt with last 10 lines of output of ls in sorted way in lol.txt','How to Overwrite lol.txt with last 10 lines of output of ls in sorted way in lol.txt?','How to Overwrite a file with last 10 lines of output of ls in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail | sort > lol.txt','NL Queries':['Overwrite lol.txt with last 10 lines of output of ls in details in sorted way in lol.txt','How to Overwrite lol.txt with last 10 lines of output of ls in details in sorted way in lol.txt?','How to Overwrite a file with last 10 lines of output of ls in details in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail | sort > lol.txt','NL Queries':['Overwrite lol.txt with last 10 lines of output of ls with hidden files in  sorted way in lol.txt','How to Overwrite lol.txt with last 10 lines of output of ls with hidden files in sorted way in lol.txt?','How to Overwrite a file with last 10 lines of output of ls with hidden files in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail | sort > lol.txt','NL Queries':['Overwrite lol.txt with last 10 lines of output of ls with hidden files and details in sorted way in lol.txt','How to Overwrite lol.txt with last 10 lines of output of ls with hidden files and details in sorted way in lol.txt?','How to Overwrite a file with last 10 lines of output of ls with hidden files and details in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail -n 2 | sort -r >> lol.txt','NL Queries':['Append last 2 lines of output of ls in reverse sorted way in lol.txt','How to append last 2 lines of output of ls in reverse sorted way in lol.txt?','How to Append last 2 lines of output of ls in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail -n 2 | sort -r >> lol.txt','NL Queries':['Append last 2 lines of output of ls in details in reverse sorted way in lol.txt','How to append last 2 lines of output of ls in details in reverse sorted way in lol.txt?','How to Append last 2 lines of output of ls in details in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail -n 2 | sort -r >> lol.txt','NL Queries':['Append last 2 lines of output of ls with hidden files in reverse sorted way in lol.txt','How to append last 2 lines of output of ls with hidden files in reverse sorted way in lol.txt?','How to Append last 2 lines of output of ls with hidden files in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail -n 2 | sort -r >> lol.txt','NL Queries':['Append last 2 lines of output of ls with hidden files and details in reverse sorted way in lol.txt','How to append last 2 lines of output of ls with hidden files and details in reverse sorted way in lol.txt?','How to Append last 2 lines of output of ls with hidden files and details in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail -n 2 | sort >> lol.txt','NL Queries':['Append last 2 lines of output of ls in sorted way in lol.txt','How to append last 2 lines of output of ls in sorted way in lol.txt?','How to Append last 2 lines of output of ls in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail -n 2 | sort >> lol.txt','NL Queries':['Append last 2 lines of output of ls in details in sorted way in lol.txt','How to append last 2 lines of output of ls in details in sorted way in lol.txt?','How to Append last 2 lines of output of ls in details in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail -n 2 | sort >> lol.txt','NL Queries':['Append last 2 lines of output of ls with hidden files in  sorted way in lol.txt','How to append last 2 lines of output of ls with hidden files in sorted way in lol.txt?','How to Append last 2 lines of output of ls with hidden files in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail -n 2 | sort >> lol.txt','NL Queries':['Append last 2 lines of output of ls with hidden files and details in sorted way in lol.txt','How to append last 2 lines of output of ls with hidden files and details in sorted way in lol.txt?','How to Append last 2 lines of output of ls with hidden files and details in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail -n 2 | sort -r > lol.txt','NL Queries':['Overwrite lol.txt with last 2 lines of output of ls in reverse sorted way in lol.txt','How to Overwrite lol.txt with last 2 lines of output of ls in reverse sorted way in lol.txt?','How to Overwrite lol.txt with last 2 lines of output of ls in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail -n 2 | sort -r > lol.txt','NL Queries':['Overwrite lol.txt with last 2 lines of output of ls in details in reverse sorted way in lol.txt','How to Overwrite lol.txt with last 2 lines of output of ls in details in reverse sorted way in lol.txt?','How to Overwrite a file with last 2 lines of output of ls in details in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail -n 2 | sort -r > lol.txt','NL Queries':['Overwrite lol.txt with last 2 lines of output of ls with hidden files in reverse sorted way in lol.txt','How to Overwrite lol.txt with last 2 lines of output of ls with hidden files in reverse sorted way in lol.txt?','How to Overwrite a file with last 2 lines of output of ls with hidden files in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail -n 2 | sort -r > lol.txt','NL Queries':['Overwrite lol.txt with last 2 lines of output of ls with hidden files and details in reverse sorted way in lol.txt','How to Overwrite lol.txt with last 2 lines of output of ls with hidden files and details in reverse sorted way in lol.txt?','How to Overwrite a file with last 2 lines of output of ls with hidden files and details in reverse sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls | tail -n 2 | sort > lol.txt','NL Queries':['Overwrite lol.txt with last 2 lines of output of ls in sorted way in lol.txt','How to Overwrite lol.txt with last 2 lines of output of ls in sorted way in lol.txt?','How to Overwrite a file with last 2 lines of output of ls in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -l | tail -n 2 | sort > lol.txt','NL Queries':['Overwrite lol.txt with last 2 lines of output of ls in details in sorted way in lol.txt','How to Overwrite lol.txt with last 2 lines of output of ls in details in sorted way in lol.txt?','How to Overwrite a file with last 2 lines of output of ls in details in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -a | tail -n 2 | sort > lol.txt','NL Queries':['Overwrite lol.txt with last 2 lines of output of ls with hidden files in  sorted way in lol.txt','How to Overwrite lol.txt with last 2 lines of output of ls with hidden files in sorted way in lol.txt?','How to Overwrite a file with last 2 lines of output of ls with hidden files in sorted way in a file?']},ignore_index=True)

tail = tail.append({'Command':'ls -al | tail -n 2 | sort > lol.txt','NL Queries':['Overwrite lol.txt with last 2 lines of output of ls with hidden files and details in sorted way in lol.txt','How to Overwrite lol.txt with last 2 lines of output of ls with hidden files and details in sorted way in lol.txt?','How to Overwrite a file with last 2 lines of output of ls with hidden files and details in sorted way in a file?']},ignore_index=True)




tail = tail.append({'Command':'ls -t /etc | tail','NL Queries':['Show last 10 oldest files and folder at /etc.','How can I see oldest 10 files and folders at /etc?','How can i see last 10 of oldest created files or folder at some path?']},ignore_index=True)

tail = tail.append({'Command':'ls -t /etc | tail -n 5','NL Queries':['Show last 5 oldest files and folder at /etc.','How can I see oldest 5 files and folders at /etc?','How can i see last 5 of oldest created files or folder at some path?']},ignore_index=True)

tail = tail.append({'Command':'head -11 lol.txt | tail -n 5','NL Queries':['Show all lines between 7 to 11 of lol.txt.','How do I see lines 7 to 10 of lol.txt?','How can i see any specific no. of lines from between of any files?']},ignore_index=True)

tail = tail.append({'Command':'head -11 lol.txt | tail -n 5 >> lol2.txt','NL Queries':['Append all lines between 7 to 11 of lol.txt into lol2.txt.','How do I append lines 7 to 10 of lol.txt into lol2.txt?','How can i append any specific no. of lines from between of any files into any another file?']},ignore_index=True)

tail = tail.append({'Command':'head -11 lol.txt | tail -n 5 > lol2.txt','NL Queries':['Clear lol2.txt and Append all lines between 7 to 11 of lol.txt into lol2.txt.','How do I Clear lol2.txt append lines 7 to 10 of lol.txt into lol2.txt?','How can i Clear lol2.txt append any specific no. of lines from between of any files into any another file?']},ignore_index=True)

tail = tail.append({'Command':'tail -5 lol.txt | head -n 2','NL Queries':['Show lines last 5th and last 4th of lol.txt.','How do I see lines last 5th and last 4th of lol.txt?','How can i see any specific no. of lines nearer from last of any file?']},ignore_index=True)

tail = tail.append({'Command':'tail -5 lol.txt | head -n 2 >> lol2.txt','NL Queries':['Append all lines last 5th and last 4th of lol.txt into lol2.txt.','How do I append lines last 5th and last 4th of lol.txt into lol2.txt?','How can i append any specific no. of lines from nearer from last of any files into any another file?']},ignore_index=True)

tail = tail.append({'Command':'tail -5 lol.txt | head -n 5 > lol2.txt','NL Queries':['Clear lol2.txt and Append all lines last 5th and last 4th of lol.txt into lol2.txt.','How do I Clear lol2.txt append lines last 5th and last 4th of lol.txt into lol2.txt?','How can i Clear lol2.txt and append any specific no. of lines from last of any file into any another file?']},ignore_index=True)

tail = tail.append({'Command':'head -4 lol.txt | tail -3; head -6 lol.txt | tail -1','NL Queries':['Show dicrete set of lines between 2 to 4 and 6th of lol.txt.','How do I see 2 to 4 and 6th lines of lol.txt?','How can i see discontionous set of lines of a file?']},ignore_index=True)

tail = tail.append({'Command':'head -4 lol.txt | tail -3; head -6 lol2.txt | tail -1','NL Queries':['Show dicrete set of lines between 2 to 4 of lol.txt and 6th of lol2.txt.','How do I see 2 to 4 lines of lol.txt and 6th line of lol2.txt?','How can i see discontionous set of lines of more then 1 files?']},ignore_index=True)

tail = tail.append({'Command':'{head -4 lol.txt | tail -3; head -6 lol.txt | tail -1} >> file.txt','NL Queries':['Append dicrete set of lines between 2 to 4 and 6th of lol.txt into file.txt.','How do I append 2 to 4 and 6th lines of lol.txt into file.txt?','How can i append discontionous set of lines of a file into another file?']},ignore_index=True)

tail = tail.append({'Command':'{head -4 lol.txt | tail -3; head -6 lol.txt | tail -1} > file.txt','NL Queries':['Overwrite dicrete set of lines between 2 to 4 and 6th of lol.txt in file.txt.','How do I overwrite file.txt with 2 to 4 and 6th lines of lol.txt in file.txt?','How can i overwrite discontionous set of lines of a file into another file?']},ignore_index=True)

tail = tail.append({'Command':'{head -4 lol.txt | tail -3; head -6 lol2.txt | tail -1} >> file.txt','NL Queries':['Append dicrete set of lines between 2 to 4 of lol.txt and 6th of lol2.txt into file.txt.','How do I append 2 to 4 lines of lol.txt and 6th of lol2.txt into file.txt?','How can i append discontionous set of lines from different files into another file?']},ignore_index=True)

tail = tail.append({'Command':'{head -4 lol.txt | tail -3; head -6 lol2.txt | tail -1} > file.txt','NL Queries':['Overwrite dicrete set of lines between 2 to 4 of lol.txt and 6th of lol2.txt in file.txt.','How do I overwrite file.txt with 2 to 4 of lol.txt and 6th of lol2.txt in file.txt?','How can i overwrite discontionous set of lines from multiple files into another file?']},ignore_index=True)

tail = tail.append({'Command':'{head -4 | tail -3; head -6 | tail -1} < lol.txt > file.txt','NL Queries':['Overwrite dicrete set of lines between 2 to 4 and 6th single file lol.txt in file.txt.','How do I overwrite file.txt with 2 to 4 and 6th lines single file lol.txt in file.txt?','How can i overwrite discontionous set of lines from a single file into another file?']},ignore_index=True)

tail = tail.append({'Command':'{head -4 | tail -3; head -6 | tail -1} < lol.txt >> file.txt','NL Queries':['Append dicrete set of lines between 2 to 4 and 6th single file lol.txt in file.txt.','How do I Append file.txt with 2 to 4 and 6th lines single file lol.txt in file.txt?','How can i Append discontionous set of lines from a single file into another file?']},ignore_index=True)
'''
print (tail)
