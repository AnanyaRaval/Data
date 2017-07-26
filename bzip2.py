import pandas as pd 

bzip2 = pd.DataFrame(columns = ['Command','NL Queries'])

bzip2 = bzip2.append({'Command':'bzip2 file.txt','NL Queries':['Compress file.txt present in this folder.','How do I zip file.txt?',
								'Command to compress file.txt using bzip2.','How do I compress file.txt?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c file.txt > file.txt.bz','NL Queries':['Compress file file.txt using bzip2. Name the compressed file as file.txt.bz and keep file.txt as it is.',
								'How do I compress file.txt using bzip2,keep the original file and name the compressed file file.txt.bz?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -d file.txt.bz2','NL Queries':['Decompress file.txt.bz.','How to decompress dataof file.txt.bz present in this folder?',
							'How do I unzip the file.txt.bz2']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -z myfile.txt','NL Queries':['How do I compress the file myfile.txt forcefully?','Forcefully compresses the file myfile.txt present in this folder.',
							'				How do I zip file myfile.txt present in this folder?']},ignore_index=True)
bzip2 = bzip2.append({'Command':'bzip2 -z new1.txt new2.txt','NL Queries':['Compresses the two files new1.txt and new2.txt into two different archives.',
									'How do I create two archives, one each for new1.txt and new2.txt?',
										'Zip the two files new1.txt and new2.txt into separate archives.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -zf hello.txt.bz2','NL Queries':['How do I force decompress the archive hello.txt.bz2 even if hello.txt exists?',
									'Overwrites the file hello.txt with the file from the archive hello.txt.bz2.',
								'How do I overwrite a file when I unzip from the archive names hello.txt.bz2?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -k game.txt','NL Queries':['Keep the existing file game.txt as it is and create an archive for it.',
							'How do I create an archive for game.txt without the file getting deleted?',
							'Create an archive for game.txt. Do not delete the current file.','Compress file game.txt. Keep original file.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -s new.txt','NL Queries':['How do I compress the file new.txt with limited memory.',
							'Compress the file new.txt, present in this folder, using reduced memory usage.',
									'How do I compress the file new.txt when I am low on memory?','Compress the file new.txt when memory is low.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -q file.txt','NL Queries':['How do I compress the file file.txt without giving any warning messages?',
									'How do I carry out a non-verbose compression on file.txt?',
									'Compress the file file.txt without any warnings.','Create an archive for file.txt without any command line output.']},ignore_index=True)

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
						'Compress file file.txt in this folder. Use level 2 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -9 file.txt','NL Queries':['How do I compress the file file1.txt with level 9 compression?',
						'Compress file file.txt in this folder. Use level 2 compression.',
						'Compress the file file.txt with level 9 compression.']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -tv hello.txt.bz2','NL Queries':['Check the integrity of the archive hello.txt.bz2',
							'How do I check the integrity of the archive hello.txt.bz2?',
							'How do I check if my archive hello.txt.bz2 is corrupted or not?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzip2 -c file2.txt >> files.txt.bz2','NL Queries':['Moves the content of file2.txt into files.txt in the archive files.txt.bz2.',
						'How do I copy content of file2.txt into files.txt in the archive?',
							'How do I move the content of file2.txt into files.txt in the archive?']},ignore_index=True)

bzip2 = bzip2.append({'Command':'bzcat file.txt.bz2','NL Queries':['How do I read the content of the file.txt in the archive file.txt.bz2?',
					'List the content in the archived file file.txt.',
						'How do I display the content from a zipped file file.txt?']},ignore_index=True)

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


print bzip2


