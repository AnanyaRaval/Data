import pandas as pd 

bzip2 = pd.DataFrame(columns = ['Command','NL Queries'])

bzip2 = bzip2.append({'Command':'bzip2 file.txt','NL Queries':['Compress file.txt present in this folder.',
																'How do I zip file.txt?',
																'Command to compress file.txt using bzip2.',
																'How do I compress file.txt?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -d file.txt.bz2','NL Queries':['Decompress file.txt.bz.',
																'How to decompress data of file.txt.bz present in this folder?',
																'How do I unzip the file.txt.bz2']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -z myfile.txt','NL Queries':['How do I compress the file myfile.txt forcefully?',
													'Forcefully compresses the file myfile.txt present in this folder and overwrite if myfile.txt.bz2 exists.',
							'						How do I zip file myfile.txt present in this folder?',
													'Compress the myfile.txt even if myfile.txt.bz2 is present in the folder.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -z new1.txt new2.txt','NL Queries':['Compresses the two files new1.txt and new2.txt into two different archives.',
									'How do I create two archives, one each for new1.txt and new2.txt?',
										'Zip the two files new1.txt and new2.txt into separate archives.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -zf hello.txt','NL Queries':['How do I force compress the file hello.txt even if hello.txt.bz2 exists?',
									'Compress hello.txt and overwrite the file hello.txt with the file from the archive hello.txt.bz2.',
								'How do I overwrite a file hello.txt when I zip to an archive hello.txt.bz2?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -k game.txt','NL Queries':['Keep the existing file game.txt as it is and create an archive for it.',
								'How do I create an archive for game.txt without the file getting deleted?',
								'Create an archive for game.txt. Do not delete the current file.',
								'Compress file game.txt. Keep original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -s new.txt','NL Queries':['How do I compress the file new.txt with limited memory.',
							'Compress the file new.txt, present in this folder, using reduced memory usage.',
									'How do I compress the file new.txt when I am low on memory?',
									'Compress the file new.txt when memory is low.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -sv new.txt','NL Queries':['How do I compress the file new.txt with limited memory and see the compression ratio.',
							'Compress the file new.txt, present in this folder, using reduced memory usage. Show the compression ratio.',
									'How do I compress the file new.txt when I am low on memory and see the compression ratio?',
									'Compress the file new.txt when memory is low and show the compression ratio.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -q file.txt','NL Queries':['How do I compress the file file.txt without giving any warning messages?',
									'How do I carry out a non-verbose compression on file.txt?',
									'Compress the file file.txt without any warnings.',
									'Create an archive for file.txt without any command line output.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -v file.txt','NL Queries':['Compress the file file.txt. Along with compression, display the compression ratio,',
								'How do I compress the file file.txt and get the compression ratio?',
									'Compress the file file.txt. Give the compression ratio.',
									'Archive file.txt present in this folder and show the compression ratio.',
										'How do I zip file.txt and see the compression ratio?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 --help','NL Queries':['How do I get help for the bzip2 command?',
							'What are the possible flags I can use with bzip2 command?',
								'Display help message for bzip2 command on the screen.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -V','NL Queries':['What is the current version of bzip2 command?',
							'List the version of the bzip2 command.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 file1.txt file2.txt','NL Queries':['How do I compress the two files file2.txt and file2.txt into two different archives?',
						'Compress the two files file1.txt and file2.txt. Create one archive for each file.',
							'How do I zip two files file1.txt and file2.txt separately?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 file1.txt file2.txt','NL Queries':['How do I compress the two files file2.txt and file2.txt into two different archives and see the compression ratio?',
						'Compress the two files file1.txt and file2.txt. Create one archive for each file and show compression ratio for both.',
							'How do I zip two files file1.txt and file2.txt separately and see the compression ratio for each file?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -1 file.txt','NL Queries':['How do I compress the file file1.txt with level 1 compression?',
								'Compress the file file.txt with level 1 compression.',
								'Compress the file file.txt. Use level 1 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -2 file.txt','NL Queries':['How do I compress the file file1.txt with level 2 compression?',
									'Compress the file file.txt with level 2 compression.',
									'Compress file file.txt in this folder. Use level 2 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -3 file.txt','NL Queries':['How do I compress the file file1.txt with level 3 compression?'
								,'Compress the file file.txt with level 3 compression.',
									'Compress file file.txt in this folder. Use level 3 compression. ']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -4 file.txt','NL Queries':['How do I compress the file file1.txt with level 4 compression?',
								'Compress the file file.txt with level 4 compression.',
								'Compress file file.txt. Use level 4 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -5 file.txt','NL Queries':['How do I compress the file file1.txt with level 5 compression?',
						'Compress the file file.txt with level 5 compression.'
						'Compress file file.txt in this folder. Use level 5 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -6 file.txt','NL Queries':['How do I compress the file file1.txt with level 6 compression?',
							'Compress the file file.txt with level 6 compression.',
							'Compress file file.txt in this folder. Use level 6 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -7 file.txt','NL Queries':['How do I compress the file file1.txt with level 7 compression?',
						'Compress the file file.txt with level 7 compression.',
							'Compress file file.txt in this folder. Use level 7 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -8 file.txt','NL Queries':['How do I compress the file file1.txt with level 8 compression?',
						'Compress the file file.txt with level 8 compression.',
						'Compress file file.txt in this folder. Use level 8 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -9 file.txt','NL Queries':['How do I compress the file file1.txt with level 9 compression?',
						'Compress file file.txt in this folder. Use level 9 compression.',
						'Compress the file file.txt with level 9 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -tv hello.txt.bz2','NL Queries':['Check the integrity of the archive hello.txt.bz2',
							'How do I check the integrity of the archive hello.txt.bz2?',
							'How do I check if my archive hello.txt.bz2 is corrupted or not?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c file2.txt >> files.txt.bz2','NL Queries':['Copy the content of file2.txt to files.txt and add to the archive files.txt.bz2.',
						'How do I copy content of file2.txt into files.txt in the archive files.txt.bz2?',
							'How do I copy the content of file2.txt into files.txt and compress to archive files.txt.bz2?']},ignore_index=True)

#bzip2 = bzip2.append({'Command':'bzcat file.txt.bz2','NL Queries':['How do I read the content of the file.txt in the archive file.txt.bz2?',
#					'List the content in the archived file file.txt.',
#						'How do I display the content from a zipped file file.txt?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -f -1 file.txt','NL Queries':['How do I force compress file.txt using level 1 compression?',
																	'Compress the file file.txt with level 1 compression forcefully.',
																	'Compress file file.txt  forcefully in this folder. Use level 1  compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -f -2 file.txt','NL Queries':['How do I force compress file.txt using level 2 compression?',
																	'Compress the file file.txt forcefully with level 2 compression.',
																	'Compress file file.txt fforcefully in this folder. Use level 2 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -f -3 file.txt','NL Queries':['How do I force compress file.txt forcefully using level 3 compression?',
																	'Compress the file file.txt forcefully with level 3 compression.',
																	'Compress file file.txt forcefully in this folder. Use level 3 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -f -4 file.txt','NL Queries':['How do I force compress file.txt using level 4 compression?',
																	'Compress the file file.txt forcefully with level 4 compression.',
																	'Compress file file.txt forcefully in this folder. Use level 4 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -f -5 file.txt','NL Queries':['How do I force compress file.txt using level 5 compression?',
																	'Compress the file file.txt forcefully with level 5 compression.',
																	'Compress file file.txt forcefully in this folder. Use level 5 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -f -6 file.txt','NL Queries':['How do I force compress file.txt using level 6 compression?',
																	'Compress the file file.txt forcefully with level 6 compression.',
																	'Compress file file.txt forcefully in this folder. Use level 6 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -f -7 file.txt','NL Queries':['How do I force compress file.txt forcefully using level 7 compression?',
																	'Compress the file file.txt forcefully with level 7 compression.',
																	'Compress file file.txt forcefully in this folder. Use level 7 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -f -8 file.txt','NL Queries':['How do I force compress file.txt using level 8 compression?',
																	'Compress the file file.txt with level 8 compression.',
																	'Compress file file.txt in this folder. Use level 8 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -f -9 file.txt','NL Queries':['How do I force compress file.txt using level 9 compression?',
																	'Compress the file file.txt forcefully with level 9 compression.',
																	'Compress file file.txt forcefully in this folder. Use level 9 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c -1 file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2 using level 1 compression. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2, level 1 compression,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz using level 1 compression and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c -2 file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2 using level 2 compression. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2 level 2 compression,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz using level 2 compression and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c -3 file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2 using level 3 compression. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2 level 3 compression,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz using level 3 compression and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c -4 file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2 using level 4 compression. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2 level 4 compression,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz using level 4 compression and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c -5 file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2 using level 5 compression. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2 level 5 compression,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz using level 5 compression and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c -6 file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2 using level 6 compression. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2 level 6 compression,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz using level 6 compression and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c -7 file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2 using level 7 compression. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2 level 7 compression,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz using level 7 compression and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c -8 file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2 using level 8 compression. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2 level 8 compression,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz using level 8 compression and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c -9 file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2 using level 9 compression. Name the compressed file as file.txt.bz and keep file.txt as it is.',
																			'How do I compress file.txt using bzip2 level 9 compression,keep the original file and name the compressed file file.txt.bz?',
																			'Zip file.txt to file.txt.bz using level 9 compression and keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -1 -v file.txt','NL Queries':['How do I compress the file file1.txt with level 1 compression and see the compression ratio?',
								'Compress the file file.txt with level 1 compression and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 1 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -2 -v file.txt','NL Queries':['How do I compress the file file1.txt with level 2 compression and see the compression ratio?',
								'Compress the file file.txt with level 2 compression and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 2 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -3 -v file.txt','NL Queries':['How do I compress the file file1.txt with level 3 compression and see the compression ratio?',
								'Compress the file file.txt with level 3 compression and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 3 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -4 -v file.txt','NL Queries':['How do I compress the file file1.txt with level 4 compression and see the compression ratio?',
								'Compress the file file.txt with level 4 compression and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 4 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -5 -v file.txt','NL Queries':['How do I compress the file file1.txt with level 5 compression and see the compression ratio?',
								'Compress the file file.txt with level 5 compression and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 5 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -6 -v file.txt','NL Queries':['How do I compress the file file1.txt with level 6 compression and see the compression ratio?',
								'Compress the file file.txt with level 6 compression and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 6 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -7 -v file.txt','NL Queries':['How do I compress the file file1.txt with level 7 compression and see the compression ratio?',
								'Compress the file file.txt with level 7 compression and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 7 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -8 -v file.txt','NL Queries':['How do I compress the file file1.txt with level 8 compression and see the compression ratio?',
								'Compress the file file.txt with level 8 compression and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 8 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -9 -v file.txt','NL Queries':['How do I compress the file file1.txt with level 9 compression and see the compression ratio?',
								'Compress the file file.txt with level 9 compression and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 9 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -1 -v -k file.txt','NL Queries':['How do I compress the file file1.txt with level 1 compression and see the compression ratio? Keep file.txt as it is.',
								'Compress the file file.txt with level 1 compression without deleting file.txt and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 1 compression. Do not delete file.txt']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -2 -v -k file.txt','NL Queries':['How do I compress the file file1.txt with level 2 compression and see the compression ratio? Keep file.txt as it is.',
								'Compress the file file.txt with level 2 compression without deleting file.txt and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 2 compression. Do not delete file.txt']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -3 -v -k file.txt','NL Queries':['How do I compress the file file1.txt with level 3 compression and see the compression ratio? Keep file.txt as it is.',
								'Compress the file file.txt with level 3 compression without deleting file.txt and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 3 compression. Do not delete file.txt']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -4 -v -k file.txt','NL Queries':['How do I compress the file file1.txt with level 4 compression and see the compression ratio? Keep file.txt as it is.',
								'Compress the file file.txt with level 4 compression without deleting file.txt and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 4 compression. Do not delete file.txt']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -5 -v -k file.txt','NL Queries':['How do I compress the file file1.txt with level 5 compression and see the compression ratio? Keep file.txt as it is.',
								'Compress the file file.txt with level 5 compression without deleting file.txt and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 5 compression. Do not delete file.txt']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -6 -v -k file.txt','NL Queries':['How do I compress the file file1.txt with level 6 compression and see the compression ratio? Keep file.txt as it is.',
								'Compress the file file.txt with level 6 compression without deleting file.txt and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 6 compression. Do not delete file.txt']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -7 -v -k file.txt','NL Queries':['How do I compress the file file1.txt with level 7 compression and see the compression ratio? Keep file.txt as it is.',
								'Compress the file file.txt with level 7 compression without deleting file.txt and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 7 compression. Do not delete file.txt']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -8 -v -k file.txt','NL Queries':['How do I compress the file file1.txt with level 8 compression and see the compression ratio? Keep file.txt as it is.',
								'Compress the file file.txt with level 8 compression without deleting file.txt and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 8 compression. Do not delete file.txt']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -9 -v -k file.txt','NL Queries':['How do I compress the file file1.txt with level 9 compression and see the compression ratio? Keep file.txt as it is.',
								'Compress the file file.txt with level 9 compression without deleting file.txt and show the compression ratio.',
									'Compress the file file.txt and show the comrpession ratio. Use level 9 compression. Do not delete file.txt']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -1 -k file.txt','NL Queries':['How do I compress the file file1.txt with level 1 compression without deleting the original file.txt?',
								'Compress the file file.txt with level 1 compression and don\'t delete file.txt.',
								'Compress the file file.txt. Use level 1 compression.Keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -2 -k file.txt','NL Queries':['How do I compress the file file1.txt with level 2 compression without deleting the original file.txt?',
								'Compress the file file.txt with level 2 compression and don\'t delete file.txt.',
								'Compress the file file.txt. Use level 2 compression.Keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -3 -k file.txt','NL Queries':['How do I compress the file file1.txt with level 3 compression without deleting the original file.txt?',
								'Compress the file file.txt with level 3 compression and don\'t delete file.txt.',
								'Compress the file file.txt. Use level 3 compression.Keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -4 -k file.txt','NL Queries':['How do I compress the file file1.txt with level 4 compression without deleting the original file.txt?',
								'Compress the file file.txt with level 4 compression and don\'t delete file.txt.',
								'Compress the file file.txt. Use level 4 compression.Keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -5 -k file.txt','NL Queries':['How do I compress the file file1.txt with level 5 compression without deleting the original file.txt?',
								'Compress the file file.txt with level 5 compression and don\'t delete file.txt.',
								'Compress the file file.txt. Use level 5 compression.Keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -6 -k file.txt','NL Queries':['How do I compress the file file1.txt with level 6 compression without deleting the original file.txt?',
								'Compress the file file.txt with level 6 compression and don\'t delete file.txt.',
								'Compress the file file.txt. Use level 6 compression.Keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -7 -k file.txt','NL Queries':['How do I compress the file file1.txt with level 7 compression without deleting the original file.txt?',
								'Compress the file file.txt with level 7 compression and don\'t delete file.txt.',
								'Compress the file file.txt. Use level 7 compression.Keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -8 -k file.txt','NL Queries':['How do I compress the file file1.txt with level 8 compression without deleting the original file.txt?',
								'Compress the file file.txt with level 8 compression and don\'t delete file.txt.',
								'Compress the file file.txt. Use level 8 compression.Keep the original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -9 -k file.txt','NL Queries':['How do I compress the file file1.txt with level 9 compression without deleting the original file.txt?',
								'Compress the file file.txt with level 9 compression and don\'t delete file.txt.',
								'Compress the file file.txt. Use level 9 compression.Keep the original file.']},ignore_index=True)

'''
bzip2 = bzip2.append({'Command':'bzmore my.txt.bz2','NL Queries':['How do I display the more version of the file my.txt from the archive my.txt.bz2?',
			'Display the more version of the archived file file.txt.',
				'How do I list the more version of the zipped file?']},ignore_index=True)
bzip2 = bzip2.append({'Command':'bzless my.txt.bz2','NL Queries':['How do I display the less version of the file my.txt from the archive my.txt.bz2?',
				'Display the less version of the archived file file.txt.',
				'How do I list the less version of the zipped file?']},ignore_index=True)
bzip2 = bzip2.append({'Command':'bzip2recover filename.bz2','NL Queries':['Recover the data from a broken filename.bz2 archive.',
				'How do I recover the data from a broken filename.bz2?','The bz2 file is broken. How do I recover my data?']},ignore_index=True)
bzip2 = bzip2.append({'Command':'bzcmp file1.bz2 file2.bz2','NL Queries':['How do I compare two bz2 archives file1.bz2 and file2.bz2?',
		'How do I run the cmp version with two archived files file1.bz2 and file2.bz2?','How do I use cmp in two zipped files file1.bz1 and file2.bz2?']},ignore_index=True)
bzip2 = bzip2.append({'Command':'bzdiff my1.bz2 my2.bz2','NL Queries':['How do I run the diff version on two archived files my1.bz2 and my2.bz2?','How do I diff the two archived files my1.bz2 and my2.bz2?','How do I use diff in two zipped files my1.bz2 and my2.bz2?']},ignore_index=True)
'''

bzip2 = bzip2.append({'Command':'bzip2 -vd linux_img.bz2','NL Queries':['Decompress linux_img.bz2 and let me know if the file got successfully decompressed.',
															'How do I get to know if linux_img.bz2 got successfully decompressed when I try decompressing the file?',
															'Decompress archive linux_img.bz2 and show the success of the oepration.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -vdf linux_img.bz2','NL Queries':['Forcefully decompress linux_img.bz2 even if linux_img exists in the current directory. Show the files decompressed.',	
																		'How do I ensure that the existing linux_img gets replaced by the file decompressed from linux_img.bz2? Show the files decompressed.',
																		'How do I forcefully decompress linux_img.bz2 and show the files decompressed?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -dk myfile.bz2','NL Queries':['Decompress the files from archive myfile.bz2 and keep the archive as it is.',
																		'How do I decompress files from myfile.bz2 without deleting the archive?',
																		'Decompress files from myfile.bz2 and do not delete the archive.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -kf new.txt','NL Queries':['Keep the original new.txt as it is and forcefully create a new archive for it.',
																'How do I compress hello.txt even if hello.txt.bz2 exists and also not delete the current hello.txt?']},ignore_index=True)

print bzip2.shape


