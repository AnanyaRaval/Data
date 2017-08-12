import pandas as pd 

whereis = pd.DataFrame(columns = ['Command','NL Queries'])

#whereis = whereis.append({'Command':'man whereis','NL Queries':['How do I know what the command whereis could do?',
#																'Get complete details of whereis command.',
#																'How do I see all options of whereis command in linux?']},ignore_index=True)

#whereis = whereis.append({'Command':'whatis whereis','NL Queries':['How do I know what the command whereis does?',
#																	'Get one line description of whereis command.',
#																	'How do I see what whereis command in linux does?']},ignore_index=True)

#whereis = whereis.append({'Command':'whereis whatis','NL Queries':['How do I find all paths containing whatis?',
#																	'Locate whatis.',
#																	'List folders where whatis source files, documentaion and binaries are stored.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis python','NL Queries':['How do I find all paths containing python?',
																	'Locate python.',
																	'List folders where python source files, documentation and binaries are stored.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis ls cat','NL Queries':['How do I find all paths containing ls and cat?',
																	'Locate ls and cat both.',
																	'List folders where ls and cat source files, documentaion and binaries are stored.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -b python','NL Queries':['How do I find all the location of only binary files of python?',
																		'Show all locations of binary files of python.',
																		'List folders where python source files are binaries.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -m python','NL Queries':['How do I find all the location of only manual files of python?',
																	'Show all locations of manual files of python.',
																	'List folders where python manual source files are stored.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -s python','NL Queries':['How do I find all the location of only source code files of python?',
																		'Show all locations of source code files of python.',
																		'List folders where python source files are stored.']},ignore_index=True)

#whereis = whereis.append({'Command':'whereis -B /bin -f ls gcc','NL Queries':['How do I find all the locations of all files of ls and gcc inside /bin/ only?',
#																			'Show all locations of ls and gcc inside /bin/.',
#																			'List folders where ls and gcc files are stored inside /bin/.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -u -M /usr/man/man1 -S /usr/src -f *','NL Queries':['Find all files in the current directory that are not documented in /usr/man/man1, whose source resides in /usr/src.']},ignore_index=True)

#whereis -B /bin/ -f gcc

whereis = whereis.append({'Command':'whereis -b -m python','NL Queries':['How do I find all the location of both binary files and manual files of python?',
																		'Show all locations of binary files and manual files of python.',
																		'List folders where python source files are both binary and manual.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -b -s python','NL Queries':['How do I find all the location of both binary files and source code files of python?',
																	'Show all locations of binary files and source code files of python.',
																	'List folders where python source files are both binary and source code.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -s -m python','NL Queries':['How do I find all the location of both source code files and manual files of python?',
																		'Show all locations of source code files and manual files of python.',
																		'List folders where python source files are both source code and manual.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -s -m -b python','NL Queries':['How do I find all the location of source code files, manual and binary files of python?',
																			'Show all locations of source code files, manual files and binary files of python.',
																			'List folders where python source files are source code, manual and binary.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -V','NL Queries':['How can I know which version of whereis am I using?',
																'Show which version of whereis am I using.',
																'List version of whereis which is currently in use.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -h','NL Queries':['How can I get help related to whereis command?',	
															'Show help provided with whereis command.',
															'List help options of whereis command.']},ignore_index=True)


print (whereis.shape)
