import pandas as pd 

less = pd.DataFrame(columns = ['Command','NL Queries'])

less = less.append({'Command':'less instructions.txt','NL Queries':['Show contents of instructions.txt enough to fit the teminal.', 
							'Display on command line, content of instructions.txt. Do not show complete file, only the amount which fits the command line.']},ignore_index=True)

less = less.append({'Command':'less +4 instructions.txt','NL Queries':['Show contents of instructions.txt. Skip the first 4 lines though.',
					'Show contents of instructions.txt starting from 5th line.',
						'How do I see content of instructions.txt without the first four lines?']},ignore_index=True)

less = less.append({'Command':'less general.py ananya.py','NL Queries':['Show content of general.py and ananya.py.','Display lines of the files general.py and ananya.py.',
						'Show contents of general.py and ananya.py.']},ignore_index=True)

#17 July
less = less.append({'Command':'less -a new.txt','NL Queries':['Open file with name new.txt. Start forward search from bottom of screen and backward search from top of screen.',
						'Open file new.txt to search for a pattern in the file skipping all lines displayed on the screen.',
							'How to search in lines of the file new.txt not displayed on screen ,while using less?',
							'Search for pattern in new.txt in this folder using less. Do not search in lines displayed on the screen.']},ignore_index = True)

less = less.append({'Command':'less --search-skip-screen new.txt','NL Queries':['Open new.txt with less. While searching, start forward search from bottom of the screen and backward search from top of screen.',
							'How to search in lines of the file new.txt not displayed on screen ,while using less?',
								'Search for a pattern in new.txt in this folder using less. While searching, skip all lines displayed on the screen.'
								'Open file new.txt to search for a pattern in the file skipping all lines displayed on the screen.']},ignore_index = True)
#----

less = less.append({'Command':'less -b3 new.txt','NL Queries':['Open file new.txt with less.Allow only a buffer space of 3Kb.',
								'Allocate 3kb buffer space while opening file new.txt.','How do I allocate only 3kb of buffer space to new.txt while opening it?']},ignore_index = True)

less = less.append({'Command':'less --buffers=128 new.txt','NL Queries':['Open file new.txt with less.Allow buffer space of 128 Kb.',
											'Allocate 128kb buffer space while opening file new.txt.']},ignore_index = True)

less = less.append({'Command':'less -e ~/hi.txt','NL Queries':['Open hi.txt and exit a file immediately after reaching the end.',
						'Open ~/hi.txt with less and exit the file after reaching the end.', 'Open file hi.txt in home directory and close it once it\'s last line is reached.'
							'Display contents of hi.txt using less command. Exit once end of file has reached.',
								'Show contents on hi.txt present in home folder. Close file once end has reached.']},ignore_index = True)

less = less.append({'Command':'less --quit-at-eof hi.txt','NL Queries':['Open file hi.txt in this folder. Quit immediately after reaching the end.',
								'Open hi.txt with less.Quit the file once end of file has reached.',
									'Display contents of hi.txt using less command. Exit once end of file has reached.',
									'Show contents of hi.txt present in the current folder. Close file once end of file has reached.']},ignore_index = True)

less = less.append({'Command':'less -E ../hi.txt','NL Queries':['Open file hi.txt, present in previous folder and exit immediately after reaching the end.',
								'Open ../hi.txt with less.Quit the file after reaching the end.',
									'Display contents of hi.txt, present in parent folder, using less command.Exit once end of file has reached.',
										'Show contents of hi.txt present in previous folder.Close file once end of file has reached.']},ignore_index = True)

less = less.append({'Command':'less --QUIT-AT-EOF hi.txt','NL Queries':['Open file hi.txt in this folder. Quit immediately after reaching the end.',
								'Open hi.txt with less.Quit the file once end of file has reached.',
									'Display contents of hi.txt using less command. Exit once end of file has reached.',
									'Show contents of hi.txt present in the current folder. Close file once end of file has reached.']},ignore_index = True)

#--- Add commands for -g, -G, -h, -i, -I, -j, -t, -T, -y. For -p, add about 10 queries with different patterns for searching. Also, add as many combinations of these as you can.
less = less.append({'Command':'less -f dir1','NL Queries':['Open a directory "dir1" in less','How to force-open dir1 directory in less ?','Open non-regular file -> dir1 in less.']},ignore_index = True)

less = less.append({'Command':'less -F list.txt','NL Queries':['Only open list.txt in command line, if it is more than a page wide','Open list.txt with less.If lists.txt has less than one screen of data,quit it automatically.','Display a pageful of lists.txt, if the total content is more than one page.']},ignore_index = True)

less = less.append({'Command':'less -g list.txt','NL Queries':['Open list.txt in command line,one pageful at a time.While searching, highlight the last locations where the query was found in that pageful.','Open list.txt in "less" mode.Highlight only the last locations that match the query.','How to highlight only the last matching items found while seaching the file = list.txt in command line.']},ignore_index = True)

less = less.append({'Command':'less -G list.txt','NL Queries':['Open list.txt in command line,one pageful at a time.While searching, go to the location where the query is matched in that pageful.','Open list.txt in "less" mode. Display the location where the query was matched, without highlighting the query word.','How to supress highlighting, while searching the file => list.txt in command line.']},ignore_index = True)

#less = less.append({'Command':'','NL Queries':['','','']},ignore_index = True)

'''
less = less.append({'Command':'less --search-skip-screen new.txt','NL Queries':['Open new.txt with less.While searchig,do it from the back','Search for a pattern in new.txt starting from the back','How to search backward while using less?']},ignore_index = True)

less = less.append({'Command':'less --help','NL Queries':['Show help for less command.','Man page for less in command line','What are the options available for less command']},ignore_index = True)

less = less.append({'Command':'less -?','NL Queries':['Show help for less command.','Man page for less in command line','What are the options available for less command']},ignore_index = True)

less = less.append({'Command':'man help','NL Queries':['Show man page for help','Information about less command','What are the flags for less command?']},ignore_index = True)

less = less.append({'Command':'less --version','NL Queries':['Version of less command','Copy right information about less','What is the version of less command?']},ignore_index = True)
'''

print less.shape


