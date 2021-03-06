import pandas as pd 

ln = pd.DataFrame(columns = ['Command','NL Queries'])

ln = ln.append({'Command':'ln -s /full/path/of/original/file /full/path/of/soft/link/file', 'NL Queries':['Create soft link from /full/path/original/file to /full/path/of/soft/link/file.',
																											'Command to create soft link from full path of original file to full path of soft link file.',
																											'Make a soft link of /full/path/original/file named /full/path/of/soft/link/file',
																											'Symbolic link of /full/path/original/file at /full/path/of/soft/link.']},ignore_index = True)
																											

ln = ln.append({'Command':'ln --backup -s ex1.c ex2.c','NL Queries':['Backup current files. Create Symbolic link from ex2.c to ex1.c.',
																	'Make a soft link of ex1.c named ex2.c after taking backup.',
																	'How do I take backup of current files and create soft link from ex2.c to ex1.c.']},ignore_index = True)

ln = ln.append({'Command':'ln -s ../first-dir/*.c -t .','NL Queries':['Create soft links in current directory for all .c files in first-dir.',
																	'How to create symbolic links from all .c files in first directory in current folder.']},ignore_index = True)

ln = ln.append({'Command':'ln src_original.txt dst_link.txt','NL Queries':['Create hard link from dst_link.txt to src_original.txt.',
																			'How to create hard link of src_original.txt named dst_link.txt?',
																			'Make link from dst_link.txt to src_original.txt in current directory. It should be a hard link, not soft.']},ignore_index= True)

#ln = ln.append({'Command':'ln ananya ananya_new','NL Queries':['Create link of ananya folder in current directory named ananya_new, also in the curent diretory.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup file1.txt file2.txt','NL Queries':['Backup current file named file2.txt. Create a hard link named file2.txt in the current directory that links to the data of file1.txt, also in the present directory.',
																		'How to take a backup of any existing file named file2.txt and create a hard link from file2.txt to file1.txt?',
																		'Single command to backup existing file titled file2.txt and create a hard link from file2.txt to file1.txt.',
																		'Backup current file named file2.txt and create a link named file2.txt to the data of file1.txt. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln -d Cloud Virtual','NL Queries':['Create a hard link named Virtual in the current directory that links to the folder Cloud, also in the present directory.',
															'How to create a hard link from Virtual to Cloud?',
															'Single command to create a hard link from Virtual to Cloud',
															'Create a link named Virtual to the data of Cloud. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln -f books.txt journal.txt','NL Queries':['Remove any existing files named journal.txt. Create a hard link named journal.txt in the current directory that links to the data of books.txt, also in the present directory.',
																	'How to remove current files titled journal.txt and create a hard link from journal.txt to books.txt?',
																	'Single command to remove any files named journal.txt and create a hard link from journal.txt to books.txt.',
																	'Remove current files named journal.txt and create a link named journal.txt to the data of books.txt. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln -i pragati.txt mishra.txt','NL Queries':['Create a hard link named mishra.txt in the current directory that links to the data of pragati.txt, also in the present directory. Ask permission before removing mishra.txt if it already exists in the folder.',
																	'How to create a hard link from mishra.txt to pragati.txt? If mishra.txt already exists, ask for permission to remove it.',
																	'Single command to create a hard link from mishra.txt to pragati.txt. If the destination file already exists, remove it after asking for permission.',
																	'Remove current files named mishra.txt after asking for permission and create a link named mishra.txt to the data of pragati.txt. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln -P src_original.txt dst_link.txt','NL Queries':['Create hard link from dst_link.txt to the symlink src_original.txt.',
																				'How to create hard link of the symbolic link src_original.txt named dst_link.txt?',
																				'Make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft.']},ignore_index= True)

ln = ln.append({'Command':'ln -s ../Batch_with_3 docs','NL Queries':['Create a soft link named docs in the current directory that points to the contents of the folder Batch_with_3 present in the parent directory.',
																	'How to create a symlink docs that points to the contents of the folder Batch_with_3 located in the previous directory.',
																	'Single command to create a symbolic link named docs pointing to the contents of the directory Batch_with_3 present in the preceding folder.',
																	'How to create a soft link from docs, present in the current directory to Batch_with_3, located in the parent directory?']},ignore_index = True)

ln = ln.append({'Command':'ln newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous hard link in the lint directory, which is located in the parent folder, that links to the newfile.txt, present in the current directory.',
																	'How to create a hard link to newfile.txt at ../lint/?',
																	'Single command to create a hard link to newfile.txt in the lint directory. This directory is located in the parent folder.',
																	'Create a link named newfile.txt to the data of newfile.txt. The link should be hard, not soft and should be located at ../lint/.']},ignore_index = True)

ln = ln.append({'Command':'ln -v target.txt destination.txt','NL Queries':['Create a hard link named destination.txt in the current directory that links to the data of source.txt, also in the present directory. Print the name of each linked file.',
																			'How to create a hard link from destination.txt to source.txt and get a printed confirmation for the same on the command line?',
																			'Single command to create a hard link from destination.txt to source.txt and print the names of the linked files.',
																			'Create a hard link named destination.txt to the data of source.txt. Give a textual representation of the same on the command line.']},ignore_index = True)

###
ln = ln.append({'Command':'ln --backup -d Cloud Virtual','NL Queries':['Backup existing folder named Virtual. Create a hard link named Virtual in the current directory that links to the folder Cloud, also in the present directory.',
																		'How to backup current folder titled Virtual and create a hard link from Virtual to Cloud?',
																		'Single command to backup existing Virtual directory and create a hard link from Virtual to Cloud.',
																		'Create a link named Virtual to the data of Cloud. The link should be hard, not soft and existing folder Virtual should be backed up.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -f books.txt journal.txt','NL Queries':['Backup current file named journal.txt. Remove any existing files named journal.txt. Create a hard link named journal.txt in the current directory that links to the data of books.txt, also in the present directory.',
																				'How to backup existing file named journal.txt and remove current files titled journal.txt? Create a hard link from journal.txt to books.txt.',
																				'Single command to backup any existing file named journal.txt, remove any files named journal.txt and create a hard link from journal.txt to books.txt.',
																				'Backup existing file titled journal.txt. Remove current files named journal.txt and create a link named journal.txt to the data of books.txt. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -i pragati.txt mishra.txt','NL Queries':['Backup any existing mishra.txt. Create a hard link named mishra.txt in the current directory that links to the data of pragati.txt, also in the present directory. Ask permission before removing mishra.txt if it already exists in the folder.',
																				'How to create a hard link from mishra.txt to pragati.txt? If mishra.txt already exists, create a backup and ask for permission to remove it.',
																				'Single command to create a hard link from mishra.txt to pragati.txt. If the destination file already exists, backup it up and remove it after asking for permission.',
																				'Backup any current files named mishra.txt. Remove current files named mishra.txt after asking for permission and create a link named mishra.txt to the data of pragati.txt. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -P src_original.txt dst_link.txt','NL Queries':['Backup any current files named dst_link.txt. Create hard link from dst_link.txt to the symlink src_original.txt.',
																					'How to backup current file named dst_link.txt and create hard link of the symbolic link src_original.txt named dst_link.txt?',
																					'Backup existing file named dst_link.txt. Make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft.']},ignore_index= True)

ln = ln.append({'Command':'ln --backup -s ../Batch_with_3 docs','NL Queries':['Backup current file named docs. Create a soft link named docs in the current directory that points to the contents of the folder Batch_with_3 present in the parent directory.',
																			'How to backup existing file titled docs and create a symlink docs that points to the contents of the folder Batch_with_3 located in the previous directory.',
																			'Single command to backup current file named docs and create a symbolic link named docs pointing to the contents of the directory Batch_with_3 present in the preceding folder.',
																			'How to create a soft link from docs, present in the current directory to Batch_with_3, located in the parent directory? Also, backup any current file named docs.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup newfile.txt -t ../lint/', 'NL Queries':['Backup current files. Create an eponymous hard link in the lint directory, which is located in the parent folder, that links to the newfile.txt, present in the current directory.',
																				'How to backup current files and create a hard link to newfile.txt at ../lint/?',
																				'Single command to backup current files and create a hard link to newfile.txt in the lint directory. This directory is located in the parent folder.',
																				'Backup current files. Create a link named newfile.txt to the data of newfile.txt. The link should be hard, not soft and be located at ../lint/.']},ignore_index = True)
#####
ln = ln.append({'Command':'ln --backup file1.txt file2.txt -t New_Folder','NL Queries':['Backup current files. Create hard links named file1.txt and file2.txt in the New_Folder directory that links to the data of these files, present in the current directory.',
																						'How to take a backup of current files and create hard links to file1.txt and file2.txt in the New_Folder directory?',
																						'Single command to backup current files and create hard links named file1.txt and file2.txt in the New_Folder directory. These files would link to files of the same name in the current directory.',
																						'Backup current files and create links named file1.txt and file2.txt to the data of file1.txt and file2.txt, present in the current directory. The link should be hard, not soft and be located in the New_Folder directory.']},ignore_index = True)

ln = ln.append({'Command':'ln -d Cloud -t Virtual/','NL Queries':['Create a eponymously named hard link in the Virtual directory that links to the folder Cloud, present in the current directory.',
																'How to create a hard link in the folder Virtual to the folder Cloud which is present in the current directory?',
																'Single command to create a hard link in the directory Virtual to the directory Cloud present in the current folder.',
																'Create a eponymously named link to the data of Cloud in the folder Virtual. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln -f books.txt journal.txt -t ../Archive','NL Queries':['Remove any existing files named books.txt and journal.txt located at ../Archive. Create hard links named books.txt and journal.txt in the Archive directory, present in the previous folder that links to the data of books.txt and journal.txt, present in the current directory.',
																					'How to remove current files titled books.txt or journal.txt from the location ../Archive and create hard links there of the same name? The files to be linked also have the same title and are located in the working directory.',
																					'Single command to remove any files named books.txt or journal.txt from ../Archive and create hard links books.txt and journal.txt in that folder. The links would point to files of the same name present in this directory.',
																					'Remove current files named books.txt or journal.txt from lint folder in the preceding directory. Create links named books.txt and journal.txt in that folder to the data of books.txt and journal.txt, present in the working directory. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln -i pragati.txt -t Friend','NL Queries':['Create a hard link named mishra.txt in the Friend directory that links to the data of mishra.txt, present in this directory. Ask permission before removing mishra.txt if it already exists in the Friend folder.',
																	'How to create a hard link mishra.txt in the Friend directory to mishra.txt in the working directory? If mishra.txt already exists in the Friend directory, ask for permission to remove it.',
																	'Single command to create a hard link mishra.txt of Friend folder to mishra.txt of the current folder. If the destination file already exists, remove it after asking for permission.',
																	'Remove current files named mishra.txt from the Friend folder after asking for permission and create a link named mishra.txt there to the data of mishra.txt, present in the current folder. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln -P data.txt -t Sample','NL Queries':['In the folder Sample, create a hard link to the symlink data.txt which is present in the current directory.',
																	'How to create hard link of the symbolic link data.txt with the same name in the folder Sample?',
																	'Make a link in the folder Sample to the symlink data.txt, present in the current directory. It should be a hard link, not soft.']},ignore_index= True)

ln = ln.append({'Command':'ln -s newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous soft link in the lint directory, which is located in the parent folder, that links to the newfile.txt, present in the current directory.',
																		'How to create a soft link to newfile.txt at ../lint/?',
																		'Single command to create a soft link to newfile.txt in the lint directory. This directory is located in the parent folder.',
																		'Create a link named newfile.txt to the data of newfile.txt. The link should be soft, not hard and be located at ../lint/.']},ignore_index = True)

ln = ln.append({'Command':'ln -v newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous hard link in the lint directory, which is located in the parent folder, that links to the newfile.txt, present in the current directory. Print the name of each linked file.',
																		'How to create a hard link to newfile.txt at ../lint/ and get a printed confirmation for the same?',
																		'Single command to create a hard link to newfile.txt in the lint directory and print the names of the linked files. This directory is located in the parent folder.',
																		'Create a link named newfile.txt to the data of newfile.txt. The link should be hard, not soft and be located at ../lint/. Give a textual representation of the same on the command line.']},ignore_index = True)

####
ln = ln.append({'Command':'ln --backup -v alpha.txt beta.txt','NL Queries':['Backup current files. Create a hard link named beta.txt in the current directory that links to the data of alpha.txt, also in the present directory. Print the name of each linked file.',
																			'How to take a backup of current files and create a hard link from beta.txt to alpha.txt? Also give a printed confirmation for the same on the command line.',
																			'Single command to backup current files and create a hard link from beta.txt to alpha.txt. Print the names of the linked files.',
																			'Backup current files and create a link named beta.txt to the data of alpha.txt. The link should be hard, not soft. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln -d -v Head Tail','NL Queries':['Create a hard link named Tail in the current directory that links to the folder Head, also in the present directory. Print the name of each linked directory.',
															'How to create a hard link from Tail to Head? Also give a printed confirmation for the same on the command line.',
															'Single command to create a hard link from Tail to Head. Print the names of the linked folders.',
															'Create a link named Tail to the data of Head. The link should be hard, not soft. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln -f -v class.txt section.txt','NL Queries':['Remove any existing files named section.txt. Create a hard link named section.txt in the current directory that links to the data of class.txt, also in the present directory. Give a textual representation of the same on the command line.',
																		'How to remove current files titled section.txt and create a hard link from section.txt to class.txt? Print the names of the linked files.',
																		'Single command to remove any files named section.txt and create a hard link from section.txt to class.txt. Print the name of each linked file.',
																		'Remove current files named section.txt and create a link named section.txt to the data of class.txt. The link should be hard, not soft. Also give a printed confirmation for the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln -i -v samarth.txt bharti.txt','NL Queries':['Create a hard link named bharti.txt in the current directory that links to the data of samarth.txt, also in the present directory. Ask permission before removing bharti.txt if it already exists in the folder. Also give a printed confirmation for the same on the command line.',
																		'How to create a hard link from bharti.txt to samarth.txt? If bharti.txt already exists, ask for permission to remove it. Print the name of each linked file.',
																		'Single command to create a hard link from bharti.txt to samarth.txt. If the destination file already exists, remove it after asking for permission. Print the names of the linked files.',
																		'Remove current files named bharti.txt after asking for permission and create a link named bharti.txt to the data of samarth.txt. The link should be hard, not soft. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln -P -v src_original.txt dst_link.txt','NL Queries':['Create hard link from dst_link.txt to the symlink src_original.txt. Also give a printed confirmation for the same on the command line.',
																				'How to create hard link of the symbolic link src_original.txt named dst_link.txt? Print the name of each linked file.',
																				'Make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft. Give a textual representation of the same on the command line.']},ignore_index= True)

ln = ln.append({'Command':'ln -s -v steve.txt jobs.txt','NL Queries':['Create a soft link named jobs.txt in the current directory that links to the data of steve.txt, also in the present directory. Print the name of each linked file.',
																		'How to create a symlink link from jobs.txt to steve.txt and get a printed confirmation for the same on the command line?',
																		'Single command to create a symbolic link from jobs.txt to steve.txt and print the names of the linked files.',
																		'Create a soft link named jobs.txt to the data of steve.txt. Give a list of the files created on the command line.']},ignore_index = True)
####
ln = ln.append({'Command':'ln -d -f Cloud Virtual','NL Queries':['Remove any folders named Virtual. Create a hard link named Virtual in the current directory that links to the folder Cloud, also in the present directory.',
																'How to remove existing folders titled Virtual and create a hard link from Virtual to Cloud?',
																'Single command to remove current folders named Virtual and create a hard link from Virtual to Cloud.',
																'Remove any existing folders titled Virtual. Create a link named Virtual to the data of Cloud. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln -d -i Books Journal','NL Queries':['Create a hard link named Journal in the current directory that links to the folder Books, also in the present directory. Ask permission before removing Journal if it already exists in the folder.',
																'How to create a hard link from Journal to Books? If Journal already exists, ask for permission to remove it.',
																'Single command to create a hard link from Journal to Books. If the destination file already exists, remove it after asking for permission.',
																'Remove current folders named Journal after asking for permission and create a link named Journal to the data of Books. The link should be hard, not soft.']},ignore_index = True)

###
ln = ln.append({'Command':'ln -P -f src_original.txt dst_link.txt','NL Queries':['Remove any existing files named dst_link.txt. Create hard link from dst_link.txt to the symlink src_original.txt.',
																				'How to remove current files titled dst_link.txt and create hard link of the symbolic link src_original.txt named dst_link.txt?',
																				'Remove any existing files named dst_link.txt and make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft.']},ignore_index= True)

ln = ln.append({'Command':'ln -P -i src_original.txt dst_link.txt','NL Queries':['Create hard link from dst_link.txt to the symlink src_original.txt. Ask permission before removing dst_link.txt if it already exists in the folder.',
																				'How to create hard link of the symbolic link src_original.txt named dst_link.txt? If dst_link.txt already exists, ask for permission to remove it.',
																				'Remove current files named dst_link.txt after asking for permission and make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft.']},ignore_index= True)

####
ln = ln.append({'Command':'ln --backup -d -f Cloud Virtual','NL Queries':['Create a backup of current folder named Virtual and remove that folder. Create a hard link named Virtual in the current directory that links to the folder Cloud, also in the present directory.',
																		'How to backup existing folder titled Virtual, remove it and create a hard link from Virtual to Cloud?',
																		'Single command to backup current Virtual directory, remove it and create a hard link from Virtual to Cloud.',
																		'Create a link named Virtual to the data of Cloud. The link should be hard, not soft and any existing folder named Virtual should be backed up and then removed.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -d -i Books Journal','NL Queries':['Backup folder named Journal if it exists. Create a hard link named Journal in the current directory that links to the folder Books, also in the present directory. Ask permission before removing Journal if it already exists in the folder.',
																		'How to create a hard link from Journal to Books? If Journal already exists, create a backup and ask for permission to remove it.',
																		'Single command to create a hard link from Journal to Books. If the destination file already exists, make a backup and remove it after asking for permission.',
																		'Backup and remove current folders named Journal after asking for permission and create a link named Journal to the data of Books. The link should be hard, not soft.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -d Cloud -t Virtual/','NL Queries':['Backup existing folder titled Cloud in the Virtual directory. Create a eponymously named hard link in the Virtual directory that links to the folder Cloud, present in the current directory.',
																			'How to backup any existing folder named Cloud in the Virtual directory and create a hard link in the folder Virtual to the folder Cloud which is present in the current directory?',
																			'Single command to backup current folder titled Cloud in the Virtual directory and create a hard link in the directory Virtual to the directory Cloud present in the current folder.',
																			'Create a eponymously named link to the data of Cloud in the folder Virtual. The link should be hard, not soft. Also, backup any folder named Cloud in the Virtual directory if it exists.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -d -v Cloud Virtual','NL Queries':['Backup existing folder named Virtual. Create a hard link named Virtual in the current directory that links to the folder Cloud, also in the present directory. Print the name of each linked folder.',
																			'How to backup current folder titled Virtual and create a hard link from Virtual to Cloud? Also, give a printed confirmation for the same on the command line.',
																			'Single command to backup existing Virtual directory and create a hard link from Virtual to Cloud. Print the names of the linked folders.',
																			'Create a link named Virtual to the data of Cloud. The link should be hard, not soft and existing folder Virtual should be backed up. Give a textual representation of the same on the command line.']},ignore_index = True)

####
ln = ln.append({'Command':'ln --backup -f -v books.txt journal.txt','NL Queries':['Backup current file named journal.txt. Remove any existing files named journal.txt. Create a hard link named journal.txt in the current directory that links to the data of books.txt, also in the present directory. Print the name of each linked file.',
																					'How to backup existing file named journal.txt and remove current files titled journal.txt? Create a hard link from journal.txt to books.txt. Also, give a printed confirmation for the same on the command line.',
																					'Single command to backup any existing file named journal.txt, remove any files named journal.txt and create a hard link from journal.txt to books.txt. Print the names of the linked files.',
																					'Backup existing file titled journal.txt. Remove current files named journal.txt and create a link named journal.txt to the data of books.txt. The link should be hard, not soft. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -i -v pragati.txt mishra.txt','NL Queries':['Backup any existing mishra.txt. Create a hard link named mishra.txt in the current directory that links to the data of pragati.txt, also in the present directory. Ask permission before removing mishra.txt if it already exists in the folder. Print the name of each linked file.',
																					'How to create a hard link from mishra.txt to pragati.txt? If mishra.txt already exists, create a backup and ask for permission to remove it. Also, give a printed confirmation for the same on the command line.',
																					'Single command to create a hard link from mishra.txt to pragati.txt. If the destination file already exists, backup it up and remove it after asking for permission. Print the names of the linked files.',
																					'Backup any current files named mishra.txt. Remove current files named mishra.txt after asking for permission and create a link named mishra.txt to the data of pragati.txt. The link should be hard, not soft. Give a textual representation of the same on the command line.']},ignore_index = True)

###
ln = ln.append({'Command':'ln --backup -P -f src_original.txt dst_link.txt','NL Queries':['Backup any current files named dst_link.txt and remove the same. Create hard link from dst_link.txt to the symlink src_original.txt.',
																							'How to backup current file named dst_link.txt, remove the existing file and create hard link of the symbolic link src_original.txt named dst_link.txt?',
																							'Backup existing file named dst_link.txt and remove the same. Make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft.']},ignore_index= True)

ln = ln.append({'Command':'ln --backup -P -i src_original.txt dst_link.txt','NL Queries':['Backup any current files named dst_link.txt. Create hard link from dst_link.txt to the symlink src_original.txt. Ask permission before removing dst_link.txt if it already exists in the folder.',
																						'How to backup current file named dst_link.txt and create hard link of the symbolic link src_original.txt named dst_link.txt? Ask permission before removing dst_link.txt if it already exists in the folder.',
																						'Backup existing file named dst_link.txt. Make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft. Remove current files named dst_link.txt after asking for permission.']},ignore_index= True)

ln = ln.append({'Command':'ln --backup -P -v src_original.txt dst_link.txt','NL Queries':['Backup any current files named dst_link.txt. Create hard link from dst_link.txt to the symlink src_original.txt. Ask permission before removing dst_link.txt if it already exists in the folder. Print the name of each linked file.',
																							'How to backup current file named dst_link.txt and create hard link of the symbolic link src_original.txt named dst_link.txt? Also, give a printed confirmation for the same on the command line.',
																							'Backup existing file named dst_link.txt. Make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft. Give a textual representation of the same on the command line.']},ignore_index= True)

####
ln = ln.append({'Command':'ln --backup -s -f ../Batch_with_3 docs','NL Queries':['Backup current file named docs and remove the same. Create a soft link named docs in the current directory that points to the contents of the folder Batch_with_3 present in the parent directory.',
																				'How to backup existing file titled docs, remove the file and create a symlink docs that points to the contents of the folder Batch_with_3 located in the previous directory.',
																				'Single command to backup current file named docs, remove the existing file and create a symbolic link named docs pointing to the contents of the directory Batch_with_3 present in the preceding folder.',
																				'How to create a soft link from docs, present in the current directory to Batch_with_3, located in the parent directory? Also, backup any current file named docs and then remove the same.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -s -i ../Batch_with_3 docs','NL Queries':['Backup current file named docs. Create a soft link named docs in the current directory that points to the contents of the folder Batch_with_3 present in the parent directory. Ask permission before removing docs if it already exists in the folder.',
																				'How to backup existing file titled docs, remove it after receiving permission and create a symlink docs that points to the contents of the folder Batch_with_3 located in the previous directory.',
																				'Single command to backup current file named docs and create a symbolic link named docs pointing to the contents of the directory Batch_with_3 present in the preceding folder. Remove current files named docs after asking for permission.',
																				'How to create a soft link from docs, present in the current directory to Batch_with_3, located in the parent directory? Also, backup any current file named docs and ask permission before removing docs if it already exists in the folder.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -s -v ../Batch_with_3 docs','NL Queries':['Backup current file named docs. Create a soft link named docs in the current directory that points to the contents of the folder Batch_with_3 present in the parent directory. Print the name of each linked file.',
																				'How to backup existing file titled docs and create a symlink docs that points to the contents of the folder Batch_with_3 located in the previous directory. Print the names of the linked files.',
																				'Single command to backup current file named docs and create a symbolic link named docs pointing to the contents of the directory Batch_with_3 present in the preceding folder. Also, give a printed confirmation for the same on the command line.',
																				'How to create a soft link from docs, present in the current directory to Batch_with_3, located in the parent directory? Also, backup any current file named docs. Give a textual representation of the same on the command line.']},ignore_index = True)

####
ln = ln.append({'Command':'ln --backup -f newfile.txt -t lint/', 'NL Queries':['Backup existing file named newfile.txt in the folder lint and then remove the same. Create an eponymous hard link in the lint directory, which is located in the parent folder, that links to the newfile.txt, present in the current directory.',
																				'How to backup existing file named newfile.txt in the lint directory, remove this file and create a hard link to newfile.txt at lint/?',
																				'Single command to backup current file titled newfile.txt in the lint folder, remove that file and create a hard link to newfile.txt in the lint directory. This directory is located in the current folder.',
																				'Backup current newfile.txt located in the lint directory and then remove it. Create a link named newfile.txt to the data of newfile.txt. The link should be hard, not soft and be located at lint/.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -i newfile.txt -t lint/', 'NL Queries':['Backup existing file named newfile.txt in the folder lint and then ask for permission to remove the same. Create an eponymous hard link in the lint directory, which is located in the parent folder, that links to the newfile.txt, present in the current directory.',
																				'How to backup existing file named newfile.txt in the lint directory, remove this file after taking permission and create a hard link to newfile.txt at lint/?',
																				'Single command to backup current file titled newfile.txt in the lint folder, remove that file after taking permission and create a hard link to newfile.txt in the lint directory. This directory is located in the current folder.',
																				'Backup current newfile.txt located in the lint directory and then ask for permission to remove it. Create a link named newfile.txt to the data of newfile.txt. The link should be hard, not soft and be located at lint/.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -v newfile.txt -t lint/', 'NL Queries':['Backup existing file named newfile.txt in the folder lint. Create an eponymous hard link in the lint directory, which is located in the parent folder, that links to the newfile.txt, present in the current directory. Print the name of each linked file.',
																				'How to backup existing file named newfile.txt in the lint directory and create a hard link to newfile.txt at lint/? Print the names of the linked files.',
																				'Single command to backup current file titled newfile.txt in the lint folder and create a hard link to newfile.txt in the lint directory. This directory is located in the current folder. Also, give a printed confirmation for the same on the command line.',
																				'Backup current newfile.txt located in the lint directory. Create a link named newfile.txt to the data of newfile.txt. The link should be hard, not soft and be located at lint/. Give a textual representation of the same on the command line.']},ignore_index = True)

#####
ln = ln.append({'Command':'ln -P -f data.txt -t Sample','NL Queries':['In the folder Sample, remove any existing file titled data.txt and create a hard link to the symlink data.txt which is present in the current directory.',
																	'How to remove any current file named data.txt from the Sample directory and create hard link of the symbolic link data.txt with the same name in the folder Sample?',
																	'Make a link in the folder Sample to the symlink data.txt after removing any existing files of the same name, present in the current directory. It should be a hard link, not soft.']},ignore_index= True)

ln = ln.append({'Command':'ln -P -i data.txt -t Sample','NL Queries':['In the folder Sample, remove any existing file titled data.txt after taking permission and create a hard link to the symlink data.txt which is present in the current directory.',
																	'How to remove any current file named data.txt from the Sample directory after getting permission and create hard link of the symbolic link data.txt with the same name in the folder Sample?',
																	'Make a link in the folder Sample to the symlink data.txt after removing any existing files of the same name with the user\'s permission, present in the current directory. It should be a hard link, not soft.']},ignore_index= True)

ln = ln.append({'Command':'ln -P -f -v data.txt -t Sample','NL Queries':['In the folder Sample, remove any existing file titled data.txt and create a hard link to the symlink data.txt which is present in the current directory. Give a textual representation of the same on the command line.',
																		'How to remove any current file named data.txt from the Sample directory and create hard link of the symbolic link data.txt with the same name in the folder Sample? Also, give a printed confirmation for the same on the command line.',
																		'Make a link in the folder Sample to the symlink data.txt after removing any existing files of the same name, present in the current directory. It should be a hard link, not soft. Print the names of the linked files.']},ignore_index= True)

ln = ln.append({'Command':'ln -P -i -v data.txt -t Sample','NL Queries':['In the folder Sample, remove any existing file titled data.txt after taking permission and create a hard link to the symlink data.txt which is present in the current directory. Give a textual representation of the same on the command line.',
																		'How to remove any current file named data.txt from the Sample directory after getting permission and create hard link of the symbolic link data.txt with the same name in the folder Sample? Also, give a printed confirmation for the same on the command line.',
																		'Make a link in the folder Sample to the symlink data.txt after removing any existing files of the same name with the user\'s permission, present in the current directory. It should be a hard link, not soft. Print the names of the linked files.']},ignore_index= True)
####
ln = ln.append({'Command':'ln --backup -P -f data.txt -t Sample','NL Queries':['In the folder Sample, backup and then remove any existing file titled data.txt. Create a hard link to the symlink data.txt which is present in the current directory.',
																				'How to backup, remove any current file named data.txt from the Sample directory and create hard link of the symbolic link data.txt with the same name in the folder Sample?',
																				'Make a link in the folder Sample to the symlink data.txt after backing up and removing any existing files of the same name, present in the current directory. It should be a hard link, not soft.']},ignore_index= True)

ln = ln.append({'Command':'ln --backup -P -i data.txt -t Sample','NL Queries':['In the folder Sample, backup and then remove any existing file titled data.txt after taking permission and create a hard link to the symlink data.txt which is present in the current directory.',
																				'How to backup, remove any current file named data.txt from the Sample directory after getting permission and create hard link of the symbolic link data.txt with the same name in the folder Sample?',
																				'Make a link in the folder Sample to the symlink data.txt after backing up and removing any existing files of the same name with the user\'s permission, present in the current directory. It should be a hard link, not soft.']},ignore_index= True)

ln = ln.append({'Command':'ln --backup -P -f -v data.txt -t Sample','NL Queries':['In the folder Sample, backup and then remove any existing file titled data.txt and create a hard link to the symlink data.txt which is present in the current directory. Give a textual representation of the same on the command line.',
																					'How to backup, remove any current file named data.txt from the Sample directory and create hard link of the symbolic link data.txt with the same name in the folder Sample? Also, give a printed confirmation for the same on the command line.',
																					'Make a link in the folder Sample to the symlink data.txt after backing up and removing any existing files of the same name, present in the current directory. It should be a hard link, not soft. Print the names of the linked files.']},ignore_index= True)

ln = ln.append({'Command':'ln --backup -P -i -v data.txt -t Sample','NL Queries':['In the folder Sample, backup and then remove any existing file titled data.txt after taking permission and create a hard link to the symlink data.txt which is present in the current directory. Give a textual representation of the same on the command line.',
																					'How to backup, remove any current file named data.txt from the Sample directory after getting permission and create hard link of the symbolic link data.txt with the same name in the folder Sample? Also, give a printed confirmation for the same on the command line.',
																					'Make a link in the folder Sample to the symlink data.txt after backing up and removing any existing files of the same name with the user\'s permission, present in the current directory. It should be a hard link, not soft. Print the names of the linked files.']},ignore_index= True)

#####
ln = ln.append({'Command':'ln -s -f newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous soft link in the lint directory after removing any existing files of that name, which is located in the parent folder, that links to the newfile.txt, present in the current directory.',
																			'How to create a soft link to newfile.txt at ../lint/ after removing current files of that name?',
																			'Single command to create a soft link to newfile.txt in the lint directory after removing existing files of the name newfile.txt. This directory is located in the parent folder.',
																			'Create a link named newfile.txt to the data of newfile.txt after removing current files of that name. The link should be soft, not hard and be located at ../lint/.']},ignore_index = True)

ln = ln.append({'Command':'ln -s -i newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous soft link in the lint directory after getting permission to remove any existing files of that name, which is located in the parent folder, that links to the newfile.txt, present in the current directory.',
																			'How to create a soft link to newfile.txt at ../lint/ after asking for permission to remove current files of that name?',
																			'Single command to create a soft link to newfile.txt in the lint directory after getting permission to remove existing files of the name newfile.txt. This directory is located in the parent folder.',
																			'Create a link named newfile.txt to the data of newfile.txt after asking for permission to remove current files of that name. The link should be soft, not hard and be located at ../lint/.']},ignore_index = True)

ln = ln.append({'Command':'ln -s -f -v newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous soft link in the lint directory after removing any existing files of that name, which is located in the parent folder, that links to the newfile.txt, present in the current directory. Print names of the linked files.',
																				'How to create a soft link to newfile.txt at ../lint/ after removing current files of that name? Print the name of each linked file.',
																				'Single command to create a soft link to newfile.txt in the lint directory after removing existing files of the name newfile.txt. This directory is located in the parent folder. Also, give a printed confirmation for the same on the command line.',
																				'Create a link named newfile.txt to the data of newfile.txt after removing current files of that name. The link should be soft, not hard and be located at ../lint/. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln -s -i -v newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous soft link in the lint directory after getting permission to remove any existing files of that name, which is located in the parent folder, that links to the newfile.txt, present in the current directory. Print names of the linked files.',
																				'How to create a soft link to newfile.txt at ../lint/ after asking for permission to remove current files of that name? Print the name of each linked file.',
																				'Single command to create a soft link to newfile.txt in the lint directory after getting permission to remove existing files of the name newfile.txt. This directory is located in the parent folder. Also, give a printed confirmation for the same on the command line.',
																				'Create a link named newfile.txt to the data of newfile.txt after asking for permission to remove current files of that name. The link should be soft, not hard and be located at ../lint/. Give a textual representation of the same on the command line.']},ignore_index = True)

####
ln = ln.append({'Command':'ln --backup -s -f newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous soft link in the lint directory after backing up and removing any existing files of that name, which is located in the parent folder, that links to the newfile.txt, present in the current directory.',
																					'How to create a soft link to newfile.txt at ../lint/ after backing up and removing current files of that name?',
																					'Single command to create a soft link to newfile.txt in the lint directory after backing up and removing existing files of the name newfile.txt. This directory is located in the parent folder.',
																					'Create a link named newfile.txt to the data of newfile.txt after backing up and removing current files of that name. The link should be soft, not hard and be located at ../lint/']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -s -i newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous soft link in the lint directory after backing up and getting permission to remove any existing files of that name, which is located in the parent folder, that links to the newfile.txt, present in the current directory.',
																					'How to create a soft link to newfile.txt at ../lint/ after backing up and asking for permission to remove current files of that name?',
																					'Single command to create a soft link to newfile.txt in the lint directory after backing up and getting permission to remove existing files of the name newfile.txt. This directory is located in the parent folder.',
																					'Create a link named newfile.txt to the data of newfile.txt after backing up and asking for permission to remove current files of that name. The link should be soft, not hard and be located at ../lint/.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -s -f -v newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous soft link in the lint directory after backing up and removing any existing files of that name, which is located in the parent folder, that links to the newfile.txt, present in the current directory. Print names of the linked files.',
																						'How to create a soft link to newfile.txt at ../lint/ after backing up and removing current files of that name? Print the name of each linked file.',
																						'Single command to create a soft link to newfile.txt in the lint directory after backing up and removing existing files of the name newfile.txt. This directory is located in the parent folder. Also, give a printed confirmation for the same on the command line.',
																						'Create a link named newfile.txt to the data of newfile.txt after backing up and removing current files of that name. The link should be soft, not hard and be located at ../lint/. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -s -i -v newfile.txt -t ../lint/', 'NL Queries':['Create an eponymous soft link in the lint directory after backing up and getting permission to remove any existing files of that name, which is located in the parent folder, that links to the newfile.txt, present in the current directory. Print names of the linked files.',
																						'How to create a soft link to newfile.txt at ../lint/ after backing up and asking for permission to remove current files of that name? Print the name of each linked file.',
																						'Single command to create a soft link to newfile.txt in the lint directory after backing up and getting permission to remove existing files of the name newfile.txt. This directory is located in the parent folder. Also, give a printed confirmation for the same on the command line.',
																						'Create a link named newfile.txt to the data of newfile.txt after backing up and asking for permission to remove current files of that name. The link should be soft, not hard and be located at ../lint/. Give a textual representation of the same on the command line.']},ignore_index = True)

#### 
ln = ln.append({'Command':'ln -d -f -v Cloud Virtual','NL Queries':['Remove any folders named Virtual. Create a hard link named Virtual in the current directory that links to the folder Cloud, also in the present directory. Print the name of each linked folder.',
																	'How to remove existing folders titled Virtul and create a hard link from Virtual to Cloud? Print the names of the linked folders.',
																	'Single command to remove current folders named Virtual and create a hard link from Virtual to Cloud. Also, give a printed confirmation for the same on the command line.',
																	'Remove any existing folders titled Virtual. Create a link named Virtual to the data of Cloud. The link should be hard, not soft. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln -d -i -v Books Journal','NL Queries':['Create a hard link named Journal in the current directory that links to the folder Books, also in the present directory. Ask permission before removing Journal if it already exists in the folder. Print the name of each linked folder.',
																	'How to create a hard link from Journal to Books? If Journal already exists, ask for permission to remove it. Print the names of the linked folders.',
																	'Single command to create a hard link from Journal to Books. If the destination file already exists, remove it after asking for permission. Also, give a printed confirmation for the same on the command line.',
																	'Remove current folders named Journal after asking for permission and create a link named Journal to the data of Books. The link should be hard, not soft. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln -P -f -v src_original.txt dst_link.txt','NL Queries':['Remove any existing files named dst_link.txt. Create hard link from dst_link.txt to the symlink src_original.txt. Print the name of each linked file.',
																					'How to remove current files titled dst_link.txt and create hard link of the symbolic link src_original.txt named dst_link.txt? Print the names of the linked files.',
																					'Remove any existing files named dst_link.txt and make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft. Give a textual representation of the same on the command line.']},ignore_index= True)

ln = ln.append({'Command':'ln -P -i -v src_original.txt dst_link.txt','NL Queries':['Create hard link from dst_link.txt to the symlink src_original.txt. Ask permission before removing dst_link.txt if it already exists in the folder. Print the name of each linked file.',
																				'How to create hard link of the symbolic link src_original.txt named dst_link.txt? If dst_link.txt already exists, ask for permission to remove it. Print the names of the linked files.',
																				'Remove current files named dst_link.txt after asking for permission and make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft. Give a textual representation of the same on the command line.']},ignore_index= True)

ln = ln.append({'Command':'ln --backup -d -f -v Cloud Virtual','NL Queries':['Create a backup of current folder named Virtual and remove that folder. Create a hard link named Virtual in the current directory that links to the folder Cloud, also in the present directory. Print the name of each linked folder.',
																			'How to backup existing folder titled Virtual, remove it and create a hard link from Virtual to Cloud? Print the names of the linked folders.',
																			'Single command to backup current Virtual directory, remove it and create a hard link from Virtual to Cloud. Also, give a printed confirmation for the same on the command line.',
																			'Create a link named Virtual to the data of Cloud. The link should be hard, not soft and any existing folder named Virtual should be backed up and then removed. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -d -i -v Books Journal','NL Queries':['Backup folder named Journal if it exists. Create a hard link named Journal in the current directory that links to the folder Books, also in the present directory. Ask permission before removing Journal if it already exists in the folder. Print the name of each linked folder.',
																			'How to create a hard link from Journal to Books? If Journal already exists, create a backup and ask for permission to remove it. Print the names of the linked folders.',
																			'Single command to create a hard link from Journal to Books. If the destination file already exists, make a backup and remove it after asking for permission. Also, give a printed confirmation for the same on the command line.',
																			'Backup and remove current folders named Journal after asking for permission and create a link named Journal to the data of Books. The link should be hard, not soft. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -d -v Cloud -t Virtual/','NL Queries':['Backup existing folder titled Cloud in the Virtual directory. Create a eponymously named hard link in the Virtual directory that links to the folder Cloud, present in the current directory. Print the name of each linked folder.',
																			'How to backup any existing folder named Cloud in the Virtual directory and create a hard link in the folder Virtual to the folder Cloud which is present in the current directory? Print the names of the linked folders.',
																			'Single command to backup current folder titled Cloud in the Virtual directory and create a hard link in the directory Virtual to the directory Cloud present in the current folder. Also, give a printed confirmation for the same on the command line.',
																			'Create a eponymously named link to the data of Cloud in the folder Virtual. The link should be hard, not soft. Also, backup any folder named Cloud in the Virtual directory if it exists. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -P -f -v src_original.txt dst_link.txt','NL Queries':['Backup any current files named dst_link.txt and remove the same. Create hard link from dst_link.txt to the symlink src_original.txt. Print the name of each linked file.',
																							'How to backup current file named dst_link.txt, remove the existing file and create hard link of the symbolic link src_original.txt named dst_link.txt? Print the names of the linked files.',
																							'Backup existing file named dst_link.txt and remove the same. Make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft. Also, give a printed confirmation for the same on the command line.']},ignore_index= True)

ln = ln.append({'Command':'ln --backup -P -i -v src_original.txt dst_link.txt','NL Queries':['Backup any current files named dst_link.txt. Create hard link from dst_link.txt to the symlink src_original.txt. Ask permission before removing dst_link.txt if it already exists in the folder. Print the name of each linked file.',
																							'How to backup current file named dst_link.txt and create hard link of the symbolic link src_original.txt named dst_link.txt? Ask permission before removing dst_link.txt if it already exists in the folder. Print the names of the linked files.',
																							'Backup existing file named dst_link.txt. Make link from dst_link.txt to the symlink src_original.txt in current directory. It should be a hard link, not soft. Remove current files named dst_link.txt after asking for permission. Also, give a printed confirmation for the same on the command line.']},ignore_index= True)

ln = ln.append({'Command':'ln --backup -s -f -v ../Batch_with_3 docs','NL Queries':['Backup current file named docs and remove the same. Create a soft link named docs in the current directory that points to the contents of the folder Batch_with_3 present in the parent directory. Print the name of each linked file.',
																					'How to backup existing file titled docs, remove the file and create a symlink docs that points to the contents of the folder Batch_with_3 located in the previous directory. Print the names of the linked files.',
																					'Single command to backup current file named docs, remove the existing file and create a symbolic link named docs pointing to the contents of the directory Batch_with_3 present in the preceding folder. Also, give a printed confirmation for the same on the command line.',
																					'How to create a soft link from docs, present in the current directory to Batch_with_3, located in the parent directory? Also, backup any current file named docs and then remove the same. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -s -i -v ../Batch_with_3 docs','NL Queries':['Backup current file named docs. Create a soft link named docs in the current directory that points to the contents of the folder Batch_with_3 present in the parent directory. Ask permission before removing docs if it already exists in the folder. Print the name of each linked file.',
																					'How to backup existing file titled docs, remove it after receiving permission and create a symlink docs that points to the contents of the folder Batch_with_3 located in the previous directory. Print the names of the linked files.',
																					'Single command to backup current file named docs and create a symbolic link named docs pointing to the contents of the directory Batch_with_3 present in the preceding folder. Remove current files named docs after asking for permission. Also, give a printed confirmation for the same on the command line.',
																					'How to create a soft link from docs, present in the current directory to Batch_with_3, located in the parent directory? Also, backup any current file named docs and ask permission before removing docs if it already exists in the folder. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -f -v newfile.txt -t lint/', 'NL Queries':['Backup existing file named newfile.txt in the folder lint and then remove the same. Create an eponymous hard link in the lint directory, which is located in the parent folder, that links to the newfile.txt, present in the current directory. Print the name of each linked file.',
																				'How to backup existing file named newfile.txt in the lint directory, remove this file and create a hard link to newfile.txt at lint/? Print the names of the linked files.',
																				'Single command to backup current file titled newfile.txt in the lint folder, remove that file and create a hard link to newfile.txt in the lint directory. This directory is located in the current folder. Also, give a printed confirmation for the same on the command line.',
																				'Backup current newfile.txt located in the lint directory and then remove it. Create a link named newfile.txt to the data of newfile.txt. The link should be hard, not soft and be located at lint/. Give a textual representation of the same on the command line.']},ignore_index = True)

ln = ln.append({'Command':'ln --backup -i -v newfile.txt -t lint/', 'NL Queries':['Backup existing file named newfile.txt in the folder lint and then ask for permission to remove the same. Create an eponymous hard link in the lint directory, which is located in the parent folder, that links to the newfile.txt, present in the current directory. Print the name of each linked file.',
																					'How to backup existing file named newfile.txt in the lint directory, remove this file after taking permission and create a hard link to newfile.txt at lint/? Print the names of the linked files.',
																					'Single command to backup current file titled newfile.txt in the lint folder, remove that file after taking permission and create a hard link to newfile.txt in the lint directory. This directory is located in the current folder. Also, give a printed confirmation for the same on the command line.',
																					'Backup current newfile.txt located in the lint directory and then ask for permission to remove it. Create a link named newfile.txt to the data of newfile.txt. The link should be hard, not soft and be located at lint/. Give a textual representation of the same on the command line.']},ignore_index = True)

####
ln = ln.append({'Command':'ln --help','NL Queries':['Show all options of ln command.',
													'What all can be done using ln command?',
													'What are the options available with ln command?',
													'Display all the additions that can be made to the ln command.']},ignore_index = True)

ln = ln.append({'Command':'ln --version','NL Queries':['Show version of ln command.',
														'Who wrote ln command?',
														'What is the version of ln command?',
														'Who is the author of ln command?']},ignore_index = True)

#ln.to_csv('ln.csv',index = False)

print ln.shape
