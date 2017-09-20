import pandas as pd

whatis = pd.DataFrame(columns = ['Command','NL Queries'])

whatis = whatis.append({'Command':'whatis head','NL Queries':['How do I know what the command head does?',
																'Get one line description of head command.',
																'How do I see what head command in linux does?']},ignore_index=True)

whatis = whatis.append({'Command':'whatis -s "2" open','NL Queries':['Show section 2 of documentation of command open.',
																	'How do I see section 2 of man pages of what command open does?',
																	'Command to see section 2 of man pages of what command open does']},ignore_index=True)

whatis = whatis.append({'Command':'whatis -d ls','NL Queries':['Print Debugging informations of ls commands.',
																'How do I see Debugging options of ls command?',
																'Command to see Debugging options of ls command']},ignore_index=True)

whatis = whatis.append({'Command':'whatis -r ls','NL Queries':['Print all commands with 1 line descriptions which has ls in their names.',
																'How do I see 1 line Descriptions of all comands which have ls in their names?',
																'Command to see 1 line Descriptions of all comands which have ls in their names']},ignore_index=True)

whatis = whatis.append({'Command':'whatis -V','NL Queries':['Print the version of my whatis command.',
															'How do I see version of my whatis command?',
															'Command to know my current whatis version.']},ignore_index=True)

whatis = whatis.append({'Command':'whatis -l head','NL Queries':['How do I know what the command head does without trimming output?',
																'Get one line description of head command without trimming output.',
																'How do I see what head command in linux does without trimming output?']},ignore_index=True)









'''
whatis = whatis.append({'Command':'whatis head tail','NL Queries':['How do I know what the commands head and tail does in one line?','Get one line description of head & tail commands.','How do I see what head & tail commands in linux does?']},ignore_index=True)

whatis = whatis.append({'Command':'whatis whatis','NL Queries':['How do I know what the command whatis does?','Get one line description of whatis command.','How do I see what whatis command in linux does?']},ignore_index=True)

whatis = whatis.append({'Command':'whatis passwd | head -n 1','NL Queries':['How do I know what the top command of passwd does?','Get exactly top one line description of passwd command.','How do I see what passwd command in linux does in exactly top one line?']},ignore_index=True)

whatis = whatis.append({'Command':'whatis passwd | tail -n 1','NL Queries':['How do I know what the bottommost command of passwd does?','Get exactly bottommost one line description of passwd command.','How do I see what passwd command in linux does in exactly bottommost one line?']},ignore_index=True)

whatis = whatis.append({'Command':'man whatis','NL Queries':['How do I know what the command whatis could do?','Get complete details of whatis command.','How do I see all options of whatis command in linux?']},ignore_index=True)

whatis = whatis.append({'Command':'whatis man','NL Queries':['How do I know what the command man does?','Get one line description of man command.','How do I see what man command in linux does?']},ignore_index=True)

whatis = whatis.append({'Command':'whatis man >> lol.txt','NL Queries':['Append the details of man command in one line in lol.txt.','Append one line description of man command in lol.txt.','How can I append one lined man command discription in lol.txt?']},ignore_index=True)

whatis = whatis.append({'Command':'whatis man > lol.txt','NL Queries':['Overwrite lol.txt with the details of man command in one line.','Overwrite lol.txt with one line description of man command.','How can I Overwrite lol.txt with one lined man command discription?']},ignore_index=True)

whatis = whatis.append({'Command':'whatis man ; ls','NL Queries':['How do I know what the command man does and files and folders at our current location simantanously?','Get one line description of man command and know all files and folders at our current location simantanously.','How do I see what man command in linux does and files and folders at our current location simantanously?']},ignore_index=True)

#whatis -M manpath -w '*' | sort > manpath/whatis
'''
print (whatis.shape)
