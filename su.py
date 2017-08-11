import pandas as pd 

su = pd.DataFrame(columns = ['Command','NL Queries'])

su = su.append({'Command':'su - john -c "TestProgram"','NL Queries':['Run TestProgram as user john.',
																	'How do I run TestProgram as user john?']},ignore_index=True)

su = su.append({'Command':'su guest','NL Queries':['Login as username guest.',
										'How do I login as user guest?']},ignore_index=True)

su = su.append({'Command':'su guest -c date','NL Queries':['Login as username guest and show date and time after that.',
											'How do I login as user guest and have a look at date and time simantanously']},ignore_index=True)

#su = su.append({'Command':'su --shell /bin/sh guest ; ls','NL Queries':['Login as username guest while Changing the default user login shell to /bin/sh.',
#											'How do I login as user guest while Changing the default user login shell to /bin/sh?']},ignore_index=True)

su = su.append({'Command':'su -m guest','NL Queries':['Login as username guest without resetting my current environment.',
														'How do I login as user guest without resetting my current environment?',
														'Login as guest. Don\'t reset the current environment.',
														'Login as username guest while preserving my current account.',
														'How do I login as user guest and preserve my current account also?']},ignore_index=True)

su = su.append({'Command':'su -l guest','NL Queries':['Make my curent shell as login shell for user guest.',
									'How can I make my current shell as login shell for user guest?']},ignore_index=True)

su = su.append({'Command':'su guest -c time','NL Queries':['Login as username guest and have a look on real , user and system time taken to complete the request.',
															'How do I login as user guest and have a look on real , user and system time taken to complete the request?',
															'Login as guest. Show real,user and system time information for the operation.',
															'After logging in as user guest, display real,user and system time information on command line for the request.']},ignore_index=True)

su = su.append({'Command':'su guest -c exit','NL Queries':['Exit session just after Logging to username guest.',
															'How do I Exit just after logging as user guest?']},ignore_index=True)

#su = su.append({'Command':'su -p guest','NL Queries':['Login as username guest while preserving my current account.',
#													'How do I login as user guest and preserve my current account also?']},ignore_index=True)

su = su.append({'Command':'sudo su','NL Queries':['Shift to root user.',
												'Shift to root user via sudo command?']},ignore_index=True)

su = su.append({'Command':'su --help','NL Queries':['Help me related to su command.','How can I get help regarding su command?']},ignore_index=True)










'''

su = su.append({'Command':'whatis su','NL Queries':['How do I know what the command su does?','Get one line description of su command.','How do I see what su command in linux does?']},ignore_index=True)

su = su.append({'Command':'man su','NL Queries':['How do I know what the command su could do?','Get complete details of su command.','How do I see all options of su command in linux?']},ignore_index=True)

su = su.append({'Command':'whereis su','NL Queries':['How do I find all paths containing su?','Locate su.','List folders where su source files, documentaion and binaries are stored.']},ignore_index=True)


su = su.append({'Command':'su -','NL Queries':['Login as root user.','How do I login as root user?']},ignore_index=True)

su = su.append({'Command':'su guest ; ls','NL Queries':['Login as username guest and after exiting session run command ls.','How do I login as user guest and after exiting session run command ls?']},ignore_index=True)



'''



#su bournvita -c date
#su bournvita -c time
#multiple commands
#piping




print (su.shape)
