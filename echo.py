import pandas as pd 

echo = pd.DataFrame(columns = ['Command','NL Queries'])

echo = echo.append({'Command':' echo My name is Ananya','NL Queries':['Print My name is Ananya',
																	'Output this string: \'My name is Ananya.\'',
																	'How do I print My name is Ananya in command line?']},ignore_index = True)

echo = echo.append({'Command':'echo -e \'Column1 \t Column2\'','NL Queries':['Enable interpretation of backslash escape sequences and print \'Column1 \t Column2\'.' ,
																			'How do I enable interpretation of backslash escape sequences and print tab separated \'Column1 \t Column2\'?',
																			'Print \'Column \t Column2\' after enabling interpretation of backslash escape sequences.']},ignore_index =  True)

echo = echo.append({'Command':'echo -E \'Column1 \t Column2\'','NL Queries':['Disable interpretation of backslash escape sequences and print \'Column1 \t Column2\'.' ,
																			'How do I disable interpretation of backslash escape sequences and print \'Column1 \t Column2\'?',
																			'Print \'Column \t Column2\' after disabling interpretation of backslash escape sequences.']},ignore_index =  True)

echo = echo.append({'Command':'echo $X','NL Queries':['Print value of variable X.',
														'What is the value of shell variable x?',
														'How do I output the value of variable x?']},ignore_index = True)

echo = echo.append({'Command':'echo *','NL Queries':['Print all file names in current folder.',
													'What files are present in this folder?',
													'How do I find out the files present in this folder?',
													'List all files in this folder.']},ignore_index = True)


echo = echo.append({'Command':'echo -n \'Hello World\'','NL Queries':['Print string \'Hello World\' without a trailing newline.',
																				'How do I print \'Hello World\' without a new line at the end of the command output.',
																				'Display string \'Hello World\' on command line without a newline inserted at the end of the output.']},ignore_index = True)

echo = echo.append({'Command':'echo -n -e \'A \v B\'','NL Queries':['Enable interpretation of backslash escape sequences and print \'A \v B\'. Do not insert newline after the output.' ,
																'How do I enable interpretation of backslash escape sequences and print tab separated \'A \v B\' without a newline at the end of the command?',
																'Print \'A \v B\' after enabling interpretation of backslash escape sequences. Do not add new line at the end of output.']},ignore_index =  True)

echo = echo.append({'Command':'echo -E \'Firstname \\ Lastname\'','NL Queries':['Disable interpretation of backslash escape sequences and print \'Firstname \\ Lastname\'. Do not insert newline after the output.' ,
																			'How do I disable interpretation of backslash escape sequences and print \'Firstname \\ Lastname\' without a newline at the end of the command??',
																			'Print \'Firstname \\ Lastname\' after disabling interpretation of backslash escape sequences. Do not add new line at the end of output.']},ignore_index =  True)

#echo.to_csv('/home/ananyaraval/Documents/Thesis/Data/UNIX/csv_files/echo.csv',index=False)
print echo.shape