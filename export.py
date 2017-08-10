import pandas as pd 

export = pd.DataFrame(columns = ['Command','NL Queries'])

export = export.append({'Command':'export -p','NL Queries':['Show all bash environment variables.',
															'How do I print all environment variables?',
															'View all variables in shell environment.',
																'Display all variables in bash envirnment.']},ignore_index = True)

export = export.append({'Command':'export VAR=1','NL Queries':['Create an environment variable called VAR. Initialise it\'s value to 1.',
															'How do I create a new environment variable VAR with value = 1?',
															'What is the command to make a variable VAR and equate it\'s value to 1?']},ignore_index=True)

export = export.append({'Command':'export PATH=$PATH:/home/himanshu/practice/','NL Queries':['Command to add /home/himanshu/practice/ to variable PATH.',
								'How do I append the string /home/himanshu/practice/ to shell variable PATH?',
									'Add the path /home/himanshu/practice/ to PATH environment variable.',
									'Change value of PATH environment variable by adding /home/himanshu/practice to it.']},ignore_index=True)

export = export.append({'Command':'export EDITOR=/usr/bin/vim','NL Queries':['How do I create an environment variable called EDITOR and assign it the shortcurt /usr/bin/vim?',
																		'Command to add short-cut to /usr/bin/vim to variable EDITOR',
																		'Make an environment variable EDITOR.Assign path /usr/bin/vim to it.']},ignore_index=True)

export = export.append({'Command':'export PS1=\'\[\e[1;32m\][\u@\h \W]\$\[\e[0m\] \'','NL Queries':['How do I change the prompt in command line to include current folder name?',
																								'Includes the current directory name in the command line prompt.',
																								'Command line prompt changes to accomodate the directory name as well.']},ignore_index=True)

export = export.append({'Command':'export FOO','NL Queries':['Allowes usage of variable FOO in the child processes.',
																'How do I use the variable FOO in my child processes?']},ignore_index=True)

export = export.append({'Command':'export -f function_name','NL Queries':['How do I export a shell function?',
																		'Allows the usage of function function_name to all the child processes.',
																		'Exports a shell function to child processes.']},ignore_index=True)

export = export.append({'Command':'export -n EDITOR','NL Queries':['How do I remove EDITOR from the export variable list?',
																	'Delete EDITOR from exported list.',
																	'Remove the variable EDITOR from exported list.']},ignore_index=True)


print export.shape
