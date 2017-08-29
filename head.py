import pandas as pd

head = pd.DataFrame(columns = ['Command','NL Queries'])

head = head.append({'Command':'head instructions.txt','NL Queries':['Print first few lines of the file instructions.txt.',
																	'Show the starting lines of the file instructions.txt.',
																	'How do I see the first few lines of the file instructions.txt in command line?']},ignore_index=True)

head = head.append({'Command':'head instructions.txt lol.txt','NL Queries':['Print first few lines of the file instructions.txt and lol.txt.',
																			'Show the starting lines of the file instructions.txt and lol.txt.',
																			'How do I see the first few lines of the file instructions.txt and lol.txt in command line?']},ignore_index=True)

head = head.append({'Command':'head -n 2 /etc/passwd','NL Queries':['Print first 2 lines of the file /etc/passwd.',
																	'Show the first two lines of /etc/passwd.',
																	'Command to show first two lines of /etc/passwd.',
																	'How do I see the starting two lines of etc/passwd?']},ignore_index=True)

head = head.append({'Command':'head -n 2 instructions.txt lol.txt','NL Queries':['Print first 2 lines of the file instructions.txt and lol.txt.',
																	'Show the first two lines of instructions.txt and lol.txt.',
																	'Command to show first two lines of instructions.txt and lol.txt.',
																	'How do I see the starting two lines of instructions.txt and lol.txt?']},ignore_index=True)

#head = head.append({'Command':'head -c 80k instructions.txt','NL Queries':['Print first 80 x 1024 characters of the file instructions.txt.',
#																		'Show the starting 80 x 1024 characters of the file instructions.txt.',
#																		'How do I see the first 80 x 1024 characters of the file instructions.txt in command line?']},ignore_index=True)

head = head.append({'Command':'head -c 80 instructions.txt','NL Queries':['Print first 80 characters of the file instructions.txt.',
																		'Show the starting 80 characters of the file instructions.txt.',
																		'How do I see the first 80 characters of the file instructions.txt in command line?']},ignore_index=True)

head = head.append({'Command':'head -c 80 instructions.txt lol.txt','NL Queries':['Print first 80 characters of the file instructions.txt and lol.txt.',
																		'Show the starting 80 characters of the file instructions.txt and lol.txt.',
																		'How do I see the first 80 characters of the files instructions.txt and lol.txt in command line?']},ignore_index=True)

head = head.append({'Command':'head -n 2 lol.txt > file.txt','NL Queries':['Overwrite file.txt with first 2 lines of the file lol.txt.',
																			'Overwrite file.txt with the first two lines of lol.txt.',
																			'Command to overwrite file.txt with first two lines of lol.txt.']},ignore_index=True)

head = head.append({'Command':'head -n 2 lol.txt >> file.txt','NL Queries':['Append file.txt with first 2 lines of the file lol.txt.',
																			'Append file.txt with the first two lines of lol.txt.',
																			'Command to append file.txt with first two lines of lol.txt.']},ignore_index=True)

head = head.append({'Command':'head -c 80 lol.txt > file.txt','NL Queries':['Overwrite file.txt with first 80 characters of the file lol.txt.',
																			'Overwrite file.txt with the first 80 characters lines of lol.txt.',
																			'Command to overwrite file.txt with first 80 characters lines of lol.txt.']},ignore_index=True)

head = head.append({'Command':'head -c 80 lol.txt >> file.txt','NL Queries':['Append file.txt with first 80 characters lines of the file lol.txt.',
																			'Append file.txt with the first 80 characters lines of lol.txt.',
																			'Command to append file.txt with first 80 characters lines of lol.txt.']},ignore_index=True)


#head = head.append({'Command':'head -n 2 lol.txt','NL Queries':['Print first 2 lines of the file lol.txt.',
#																'Show the first two lines of lol.txt.',
#																'Command to show first two lines of lol.txt.']},ignore_index=True)

#head = head.append({'Command':'head *.txt','NL Queries':['Print first few lines of all txt files.',
#'Show the starting lines of all .txt files.',
#'How do I see the first few lines of .txt all files in command line?']},ignore_index=True)

#head = head.append({'Command':'head -q *.txt','NL Queries':['Print first few lines of all .txt files without any header before contents of each file.',
#															'Show the starting lines of all .txt files without any header before contents of each file.',
#															'How do I see the first few lines of .txt all files without any header before contents of each file in command line?']},ignore_index=True)

head = head.append({'Command':'head -q instructions.txt lol.txt','NL Queries':['Print first few lines of the file instructions.txt and lol.txt without header.',
																				'Show the starting lines of the file instructions.txt and lol.txt without header.',
																				'How do I see the first few lines of the file instructions.txt and lol.txt in command line without header?']},ignore_index=True)

head = head.append({'Command':'head -q instructions.txt','NL Queries':['Print first few lines of the file instructions.txt without header.',
																		'Show the starting lines of the file instructions.txt without header.',
																		'How do I see the first few lines of the file instructions.txt in command line without header?']},ignore_index=True)

head = head.append({'Command':'head -v *.txt','NL Queries':['Print first few lines of all .txt files with header before contents of each file.',
															'Show the starting lines of all .txt files with header before contents of each file.',
															'How do I see the first few lines of .txt all files with header before contents of each file in command line?']},ignore_index=True)

#head = head.append({'Command':'head -v instructions.txt','NL Queries':['Print first few lines of the file instructions.txt with header.',
#																		'Show the starting lines of the file instructions.txt with header.',
#																		'How do I see the first few lines of the file instructions.txt in command line with header?']},ignore_index=True)

head = head.append({'Command':'head -v instructions.txt lol.txt','NL Queries':['Print first few lines of the file instructions.txt and lol.txt with header.',
																				'Show the starting lines of the file instructions.txt and lol.txt with header.',
																				'How do I see the first few lines and header of the files instructions.txt and lol.txt in command line?']},ignore_index=True)

head = head.append({'Command':'head -v -n 2 /etc/passwd','NL Queries':['Print first 2 lines of the file /etc/passwd with header.',
																		'Show the first two lines of /etc/passwd with header.',
																		'Command to show first two lines of /etc/passwd with header.',
																		'How do I see the starting two lines of etc/passwd with header?']},ignore_index=True)


head = head.append({'Command':'head -v -c 80 instructions.txt','NL Queries':['Print first 80 characters of the file instructions.txt with header.',
																			'Show the starting 80 characters of the file instructions.txt with header.',
																			'How do I see the first 80 characters of the file instructions.txt in command line with header?']},ignore_index=True)

#head = head.append({'Command':'head -v -c 80k instructions.txt','NL Queries':['Print first 80 x 1024 characters of the file instructions.txt with header.',
#																			'Show the starting 80 x 1024 characters of the file instructions.txt with header.',
#																			'How do I see the first 80 x 1024 characters of the file instructions.txt in command line with header?']},ignore_index=True)

head = head.append({'Command':'head -q -n 2 /etc/passwd','NL Queries':['Print first 2 lines of the file /etc/passwd without header.',
																		'Show the first two lines of /etc/passwd with header.',
																		'Command to show first two lines of /etc/passwd without header.',
																		'How do I see the starting two lines of etc/passwd without header?']},ignore_index=True)


#head = head.append({'Command':'head -q -c 80 instructions.txt','NL Queries':['Print first 80 characters of the file instructions.txt without header.',
#																			'Show the starting 80 characters of the file instructions.txt without header.',
#																			'How do I see the first 80 characters of the file instructions.txt in command line without header?']},ignore_index=True)

head = head.append({'Command':'head -q -c 80k instructions.txt','NL Queries':['Print first 80 x 1024 characters of the file instructions.txt without header.',
																			'Show the starting 80 x 1024 characters of the file instructions.txt without header.',
																			'How do I see the first 80 x 1024 characters of the file instructions.txt in command line without header?']},ignore_index=True)

head = head.append({'Command':'head -q -n 2 lol.txt','NL Queries':['Print first 2 lines of the file lol.txt without header.',
																	'Show the first two lines of lol.txt without header.',
																	'Command to show first two lines of lol.txt without header.']},ignore_index=True)

head = head.append({'Command':'head --help','NL Queries':['Print what options do I have with head command.',
														'Show help related to head command.',
														'How do I get help related to head command?']},ignore_index=True)

head = head.append({'Command':'head --version','NL Queries':['Print the version of head command.',
															'Show the version of head command.',
															'How do I get to know the version of head command?']},ignore_index=True)














'''
head = head.append({'Command':'head -11 lol.txt | tail -n 5 >> lol2.txt','NL Queries':['Append all lines between 7 to 11 of lol.txt into lol2.txt.','How do I append lines 7 to 10 of lol.txt into lol2.txt?','How can i append any specific no. of lines from between of any files into any another file?']},ignore_index=True)

head = head.append({'Command':'head -11 lol.txt | tail -n 5 > lol2.txt','NL Queries':['Clear lol2.txt and Append all lines between 7 to 11 of lol.txt into lol2.txt.','How do I Clear lol2.txt append lines 7 to 10 of lol.txt into lol2.txt?','How can i Clear lol2.txt append any specific no. of lines from between of any files into any another file?']},ignore_index=True)

head = head.append({'Command':'tail -5 lol.txt | head -n 2','NL Queries':['Show lines last 5th and last 4th of lol.txt.','How do I see lines last 5th and last 4th of lol.txt?','How can i see any specific no. of lines nearer from last of any file?']},ignore_index=True)

head = head.append({'Command':'tail -5 lol.txt | head -n 2 >> lol2.txt','NL Queries':['Append all lines last 5th and last 4th of lol.txt into lol2.txt.','How do I append lines last 5th and last 4th of lol.txt into lol2.txt?','How can i append any specific no. of lines from nearer from last of any files into any another file?']},ignore_index=True)

head = head.append({'Command':'tail -5 lol.txt | head -n 5 > lol2.txt','NL Queries':['Clear lol2.txt and Append all lines last 5th and last 4th of lol.txt into lol2.txt.','How do I Clear lol2.txt append lines last 5th and last 4th of lol.txt into lol2.txt?','How can i Clear lol2.txt and append any specific no. of lines from last of any file into any another file?']},ignore_index=True)

head = head.append({'Command':'head -4 lol.txt | tail -3; head -6 lol.txt | tail -1','NL Queries':['Show dicrete set of lines between 2 to 4 and 6th of lol.txt.','How do I see 2 to 4 and 6th lines of lol.txt?','How can i see discontionous set of lines of a file?']},ignore_index=True)

head = head.append({'Command':'head -4 lol.txt | tail -3; head -6 lol2.txt | tail -1','NL Queries':['Show dicrete set of lines between 2 to 4 of lol.txt and 6th of lol2.txt.','How do I see 2 to 4 lines of lol.txt and 6th line of lol2.txt?','How can i see discontionous set of lines of more then 1 files?']},ignore_index=True)

head = head.append({'Command':'{head -4 lol.txt | tail -3; head -6 lol.txt | tail -1} >> file.txt','NL Queries':['Append dicrete set of lines between 2 to 4 and 6th of lol.txt into file.txt.','How do I append 2 to 4 and 6th lines of lol.txt into file.txt?','How can i append discontionous set of lines of a file into another file?']},ignore_index=True)

head = head.append({'Command':'{head -4 lol.txt | tail -3; head -6 lol.txt | tail -1} > file.txt','NL Queries':['Overwrite dicrete set of lines between 2 to 4 and 6th of lol.txt in file.txt.','How do I overwrite file.txt with 2 to 4 and 6th lines of lol.txt in file.txt?','How can i overwrite discontionous set of lines of a file into another file?']},ignore_index=True)

head = head.append({'Command':'{head -4 lol.txt | tail -3; head -6 lol2.txt | tail -1} >> file.txt','NL Queries':['Append dicrete set of lines between 2 to 4 of lol.txt and 6th of lol2.txt into file.txt.','How do I append 2 to 4 lines of lol.txt and 6th of lol2.txt into file.txt?','How can i append discontionous set of lines from different files into another file?']},ignore_index=True)

head = head.append({'Command':'{head -4 lol.txt | tail -3; head -6 lol2.txt | tail -1} > file.txt','NL Queries':['Overwrite dicrete set of lines between 2 to 4 of lol.txt and 6th of lol2.txt in file.txt.','How do I overwrite file.txt with 2 to 4 of lol.txt and 6th of lol2.txt in file.txt?','How can i overwrite discontionous set of lines from multiple files into another file?']},ignore_index=True)

head = head.append({'Command':'{head -4 | tail -3; head -6 | tail -1} < lol.txt > file.txt','NL Queries':['Overwrite dicrete set of lines between 2 to 4 and 6th single file lol.txt in file.txt.','How do I overwrite file.txt with 2 to 4 and 6th lines single file lol.txt in file.txt?','How can i overwrite discontionous set of lines from a single file into another file?']},ignore_index=True)

head = head.append({'Command':'{head -4 | tail -3; head -6 | tail -1} < lol.txt >> file.txt','NL Queries':['Append dicrete set of lines between 2 to 4 and 6th single file lol.txt in file.txt.','How do I Append file.txt with 2 to 4 and 6th lines single file lol.txt in file.txt?','How can i Append discontionous set of lines from a single file into another file?']},ignore_index=True)



head = head.append({'Command':'ls | head ','NL Queries':['Print first few lines of output of ls.','Show the first few lines of output of ls command.','Command to show first few lines of output of ls command.']},ignore_index=True)

head = head.append({'Command':'ls | head >> lol.txt','NL Queries':['Append first few lines of output of ls into lol.txt.','Append the first few lines of outut of ls command into lol.txt.','Command to append first few lines of output of ls command into another file.']},ignore_index=True)

head = head.append({'Command':'ls | heapythd > lol.txt','NL Queries':['Overwrite lol.txt with first few lines of output of ls.','Overwrite lol.txt with the first few lines of output of ls command.','Command to Overwrite a file with first few lines of output of ls command.']},ignore_index=True)

head = head.append({'Command':'man head','NL Queries':['Show all options of head command.','How does head command works?','What\'s the power of head command?']},ignore_index=True)

head = head.append({'Command':'ls | head | sort -r >> lol.txt','NL Queries':['Append reverse sorted first few lines of output of ls into lol.txt.','Append reverse sorted the first few lines of output of ls command into lol.txt.','Command to append reverse sorted first few lines of output of ls command into another file.']},ignore_index=True)

head = head.append({'Command':'ls | head | sort >> lol.txt','NL Queries':['Append sorted first few lines of output of ls into lol.txt.','Append sorted the first few lines of output of ls command into lol.txt.','Command to append sorted first few lines of output of ls command into another file.']},ignore_index=True)

head = head.append({'Command':'ls -la | head | sort -r >> lol.txt','NL Queries':['Append reverse sorted first few lines of output of ls with hidden files and in detail into lol.txt.','Append reverse sorted the first few lines of output of ls with hidden files and in detail command into lol.txt.','Command to append reverse sorted first few lines of output of ls command with hidden files and in detail into another file.']},ignore_index=True)

head = head.append({'Command':'ls -la | head | sort >> lol.txt','NL Queries':['Append sorted first few lines of output of ls with hidden files and in detail into lol.txt.','Append sorted the first few lines of output of ls command with hidden files and in detail into lol.txt.','Command to append sorted first few lines of output of ls command with hidden files and in detail into another file.']},ignore_index=True)

'''

print (head.shape)
