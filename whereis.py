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
#																	'List folders where whatis source files, documentation and binaries are stored.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis python','NL Queries':['How do I find all paths containing python?',
																	'Locate python.',
																	'List folders where python source files, documentation and binaries are stored.']},ignore_index=True)

#whereis = whereis.append({'Command':'whereis ls cat','NL Queries':['How do I find all paths containing ls and cat?',
#																	'Locate ls and cat both.',
#																	'List folders where ls and cat source files, documentation and binaries are stored.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -b python','NL Queries':['How do I find all the location of only binary files of python?',
																		'Locate all locations of binary files of python.',
																		'List folders where python source files are binaries.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -m python','NL Queries':['How do I find all the location of only manual files of python?',
																		'Locate all locations of manual files of python.',
																		'List folders where python source files are manual.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -s python','NL Queries':['How do I find all the location of only source code files of python?',
																	'Locate all locations of source code files of python.',
																	'List folders where python source files are of source code.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -B /bin -f ls gcc','NL Queries':['How do I find all the location of all files of ls and gcc inside /bin/ only?',
																			'Locate all locations of ls and gcc inside /bin/.',
																			'List folders where ls and gcc files are stored inside /bin/.']},ignore_index=True)

#whereis -B /bin/ -f gcc

whereis = whereis.append({'Command':'whereis -V','NL Queries':['How can I know which version of whereis am I using?',
																'Show which version of whereis am I using.',
																'List version of whereis which is currently in use.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -h','NL Queries':['How can I get help related to whereis command?',
																'Show help provided with whereis command.',
																'List help options of whereis command.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -b -m python','NL Queries':['How do I find all the location of both binary files and manual files of python?',
																		'Locate all locations of binary files and manual files of python.',
																		'List folders where python source files are both binary and manual.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -b -s python','NL Queries':['How do I find all the location of both binary files and source code files of python?',
																		'Locate all locations of binary files and source code files of python.',
																		'List folders where python source files are both binary and source code.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -s -m python','NL Queries':['How do I find all the location of both source code files and manual files of python?',
																		'Locate all locations of source code files and manual files of python.',
																		'List folders where python source files are both source code and manual.']},ignore_index=True)







whereis = whereis.append({'Command':'whereis -B /bin -b python','NL Queries':['How do I find all the location of only binary files of python inside /bin/ only?',
																			'Locate all locations of binary files of python inside /bin/ only.',
																			'List folders where python source files are binaries inside /bin/ only.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -M /bin -m python','NL Queries':['How do I find all the location of only manual files of python inside /bin/ only?',
																			'Locate all locations of manual files of python inside /bin/ only.',
																			'List folders where python source files are manual inside /bin/ only.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -S /bin -s python','NL Queries':['How do I find all the location of only source code files of python inside /bin/ only?',
																			'Locate all locations of source code files of python inside /bin/ only.',
																			'List folders where python source files are of source code inside /bin/ only.']},ignore_index=True)




whereis = whereis.append({'Command':'whereis -B /bin -b -M /bin -m python','NL Queries':['How do I find all the location of only binary and manual files of python inside /bin/ only?',
																						'Locate all locations of binary and manual files of python inside /bin/ only.',
																						'List folders where python source files are binaries and manual inside /bin/ only.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -B /bin -b -S /bin -s python','NL Queries':['How do I find all the location of only binary and source code files of python inside /bin/ only?',
																						'Locate all locations of binary and source code files of python inside /bin/ only.',
																						'List folders where python source files are binaries and source code inside /bin/ only.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -M /bin -m -S /bin -s python','NL Queries':['How do I find all the location of only manual and source code files of python inside /bin/ only?',
																						'Locate all locations of manual and source code files of python inside /bin/ only.',
																						'List folders where python source files are manual and source code inside /bin/ only.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -B /bin -b -M /bin -m -S /bin -s python','NL Queries':['How do I find all the location of binary,manual and source code files of python inside /bin/ only?',
																									'Locate all locations of binary,manual and source code files of python inside /bin/ only.',
																									'List folders where python source files are binary,manual and source code inside /bin/ only.']},ignore_index=True)





'''
whereis = whereis.append({'Command':'whereis -u -B /bin/python -f *','NL Queries':['How do I find all the location of binary files of python inside /bin/ only?',
																					'Locate all locations of binary files of python inside /bin/ only.',
																					'List folders where python binary files are inside /bin/ only.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -u -M /bin/python -f *','NL Queries':['How do I find all the location of manual files of python inside /bin/ only?',
																					'Locate all locations of manual files of python inside /bin/ only.',
																					'List folders where python manual files are inside /bin/ only.']},ignore_index=True)

whereis = whereis.append({'Command':'whereis -u -S /bin/python -f *','NL Queries':['How do I find all the location of source code files of python inside /bin/ only?',	
																					'Locate all locations of source code files of python inside /bin/ only.',
																					'List folders where python source code files are inside /bin/ only.']},ignore_index=True)

'''

print (whereis.shape)
