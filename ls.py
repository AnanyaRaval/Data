import pandas as pd 

ls = pd.DataFrame(columns = ['Command','NL Queries'])

ls = ls.append({'Command':'ls','NL Queries':['List all files and folders in current directory',
											'Which folders and files do  I have in my current directory?',
											'Name all contents of my working directory.']},ignore_index = True)

ls = ls.append({'Command':'ls / ','NL Queries': ['Contents of root directory.',
												'What are the names of files/folders in my root directory.',
												'How do I check what is present in the root directory?']},ignore_index = True)

ls = ls.append({'Command':'ls ..','NL Queries':['Stuff in one directory before current one.',
												'Files and folders present in parent directory.',
												'Show contents of previous directory on command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -l','NL Queries':['List all the files and folders in the current directory along with their details.',
												'Give details of all files and folders present in the current directory.',
												'How to see the details of all the files/folders in the current folder?',
												'Single command to get a detailed list of all files/folders in the current folder.']},ignore_index = True)

ls = ls.append({'Command':'ls -a','NL Queries':['List all contents including hidden ones present in the current directory.',
												'How to see all files/folders including hidden ones present in the current directory?',
												'How to see a list hidden files and folders of the current directory?',
												'Single command to see files that start with . symbol']},ignore_index = True)

ls = ls.append({'Command':'ls -lh','NL Queries':['List all files/folders of this directory in human readable format, along with their details.',
												'List all files and folders with details present in the current directory. The size should be rounded off.',
												'How to see the details of the contents present in the current directory in human readable format?',
												'Single command to see details of files and folders in human readable format.']},ignore_index = True)

ls = ls.append({'Command':'ls -F','NL Queries':['List all files with folders highlighted with / character at the end.',
												'List contents of current directory and denote folders with a / symbol at the end.',
												'Highlight folders present in this directory with / character.',
												'Denote folders present in this directory with / symbol at the end.']},ignore_index = True)

ls = ls.append({'Command':'ls -r','NL Queries':['List files in reverse alphabetical order.',
												'How to see the contents of present directory in reverse alphabetical order?',
												'Single command to list files and folders in reverse alphabetical order.',
												'Show all folders of this directory in reverse alphabetical order on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -R','NL Queries':['List all files and folders of this directory and it\'s sub directories.',
												'Show the contents of this directory and the folders present in the current directory with their contents on the command line.',
												'How to see contents of this directory and it\'s sub directories?',
												'What is contained in this directory and folders of this directory?']},ignore_index = True)

ls = ls.append({'Command':'ls -R -l','NL Queries':['List all files and folders of this directory and it\'s sub directories along with their details.',
													'Show detailed content of this directory.Show the folders present in the current directory with their contents and details on the command line.',
													'How to see contents of this directory and sub directories along with detailed information?',
													'What are the details of the contents of the files present in this directory and their subdirectories?']},ignore_index = True)
#??
ls = ls.append({'Command':'ls -R -l ..','NL Queries':['List all files and folders of the previous directory and it\'s sub directories with details.',
													'Show the contents and folders present in the previous directory with their contents and details on the command line.',
													'How to see contents of the parent directory with their sub directories along with detailed information?',
													'What are the details of the contents of previous directory and the folders present in the previous directory?']},ignore_index = True)

ls = ls.append({'Command':'ls -lt','NL Queries':['List all files in order of modified time with details, newest modified first.',
												'Show contents of present folder with their details. Sort them in the order of newest modified to last modified.',
												'How to see the files and folders of this directory with details in order of last modified?',
												'Single command to get detailed list of files in order of last modified on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -1','NL Queries':['Show contents of present directory in a vertical list.',
												'List out files and folders of this directory with one element per line.',
												'How to see what all folders are present in this directory in a vertical list?',
												'Single command to see contents of the current directory. Each file or folder should occupy one line.']},ignore_index = True)

#EDIT
ls = ls.append({'Command':'ls -ltr','NL Queries':['Give detailed list of files present in the current folder. Sort them in order of modification time, oldest first.',
												'How to see the files of this directory with their details sorted in order of oldest modified to newest modified?',
												'Single command to get a detailed list of files contained in the present folder. The files that have not been accessed recently are placed at the top.',
												'Sort all files and folders of the current directory in order of modification time, oldest first.']},ignore_index = True)

ls = ls.append({'Command':'ls -lr','NL Queries':['Give detailed list of files and folders present in current directory. Sort them in reverse alphabetical order.',
												'How to get detailed information about the files present in this directory sorted in reverse alphabetical order?',
												'Single command to see the contents of this folder with their details in reverse order.',
												'Show the folders present in this directory with details. Sort them in reverse alphabetical order.']},ignore_index = True)

ls = ls.append({'Command':'ls -S','NL Queries':['Give list of files and folders present in current directory. Sort them in order of file size.',
												'How to see the files present in this directory sorted in order of file size?',
												'Single command to see the contents of this folder in order of size.',
												'Show the folders present in this directory. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -i','NL Queries':['List files and folders of this folder with it\'s inode number.',
												'Show contents of present directory with it\'s inode number.',
												'What are the contents of this folder and give their inode number?',
												'How to see the inode number of each file/folder in this directory?']},ignore_index = True)

ls = ls.append({'Command':'ls --version','NL Queries':['Show version of ls command.',
														'Who wrote ls command?','What is the version of ls command?',
														'Who is the author of ls command?']},ignore_index = True)

ls = ls.append({'Command':'ls --help','NL Queries':['Show all options of ls command.',
													'What all can be done using ls command?',
													'What are the options available with ls command?',
													'Display all the additions that can be made to the ls command.']},ignore_index = True)

ls = ls.append({'Command':'ls -n','NL Queries':['List files of this directory with user and group IDs',
												'Show contents of present folder with user and group IDs',
												'How to see the user and group IDs of each file in this folder?',
												'What are the user and group IDs of the files in this directory?']},ignore_index = True)

ls = ls.append({'Command':'ls Batch_with_3','NL Queries':['List all files inside the folder named Batch_with_3 present in this directory.',
														'What are the contents of the folder Batch_with_3?',
														'In the folder Batch_with_3 present in this directory, what all files are present?',
														'How to see the files and folders present in the directory Batch_with_3?']},ignore_index = True)
#To keep or not to keep
ls = ls.append({'Command':'ls -l Notes','NL Queries':['List all the files and folders in the Notes directory along with their details.',
														'Give details of all files and folders present in the Notes directory.',
														'How to see the details of all the files and folders in the Notes folder?',
														'Single command to get a detailed list of all files and folders in the folder named Notes.']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -a Books','NL Queries':['List all contents including hidden ones present in the Books directory.',
														'How to see all files including hidden ones present in the Books directory?',
														'How to see hidden files and folders of the directory called Books?',
														'Single command to see files located in the Books directory that start with . symbol.']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -lh Steve','NL Queries':['List all files and folders present in the folder named Steve in human readable format.',
													'List all files and folders with details present in the directory Steve. The file size should be rounded off.',
													'How to see the details of the files and folders present in the directory titled Steve in human readable format?',
													'Single command to see details of files and folders located inside the Steve directory in human readable format']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -F Exercise','NL Queries':['List all files with folders present in Exercise directory highlighted with / character at the end.',
														'List contents of directory named Exercise and denote folders with a / symbol at the end.',
														'Highlight folders present in the Exercise directory with / character.',
														'Denote folders present in the directory Exercise with / symbol at the end.']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -r Aditi','NL Queries':['List files of the directory titled Aditi in reverse alphabetical order.',
													'How to see the contents of the directory named Aditi in reverse order?',
													'Single command to list files and folders of the directory titled Aditi in reverse alphabetical order.',
													'Show all folders of the directory Aditi in reverse order on the command line.']},ignore_index = True) 
#To Keep or not to keep
ls = ls.append({'Command':'ls -R Card_Info','NL Queries':['List all files and folders of the Card_Info directory and it\'s sub directories.','Show the files and folders present in the directory titled Card_Info along with folders\' contents on the command line.','How to see contents of the directory named Card_Info with the contents of sub directories?','What is contained in the Card_Info directory and it\'s folders?']},ignore_index = True)

#To Keep or not to keep
ls = ls.append({'Command':'ls -lt Instructions','NL Queries':['List all files of Instructions directory in order of last modified with details.',
															'Show contents of the folder titled Instructions with their details. Sort them in the order of last modified.',
															'How to see the files and folders of the directory Instructions with details in order of last modified?',
															'Single command to get detailed list of files located inside the directory titled Instructions in order of last modified on the command line.']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -1 ISB','NL Queries':['Show contents of the ISB directory in a vertical list.',
													'List out files and folders of the directory titled ISB with one file per line.',
													'How to see what all folders and files are present in the directory named ISB in a vertical list?',
													'Single command to see contents of the ISB directory. Each file should occupy one line.']},ignore_index = True)

#ltr
ls = ls.append({'Command':'ls -ltr ..','NL Queries':['Give detailed list of files present in the parent folder. Sort them in order of modification time, oldest first.',
													'How to see the files of the previous directory with their details sorted in order of oldest modified to newest modified?',
													'Single command to get a detailed list of files contained in the parent folder. The files that have not been accessed recently are placed at the top.',
													'Sort all files and folders of the preceding directory in order of modification time, oldest first.']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -lr Sample','NL Queries':['Give detailed list of files and folders present in the Sample directory. Sort them in reverse alphabetical order.',
														'How to get detailed information about the files present in the directory named Sample sorted in reverse alphabetical order?',
														'Single command to see the contents of the folder titled Sample with their details in reverse order.',
														'Show the folders present in the Sample directory with details. Sort them in reverse alphabetical order.']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -S Project','NL Queries':['Give list of files and folders present in the Project directory. Sort them in order of file size.',
													'How to see the files present in the directory titled Project sorted in order of file size?',
													'Single command to see the contents of the Project folder in order of size.',
													'Show the folders present in the directory named Project. Sort them in decreasing order of file size.']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -i Tesla','NL Queries':['List files and folders of the directory named Tesla with their inode number.',
														'Show contents of Tesla directory with their inode number.',
														'What are the contents of the folder titled Tesla and give their inode number?',
														'How to see the inode number of each file and folder in the Tesla directory?']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -n Submissions','NL Queries':['List files of the Submissions directory with user and group IDs.',
															'Show contents of folder titled Submissions with user and group IDs.',
															'How to see the user and group IDs of each file of the folder Submissions?',
															'What are the user and group IDs of the files in the directory named Submissions?']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls ../Bats','NL Queries':['List all files inside the folder Bats located in the previous directory',
													'What are the contents of the folder Bats located in the previous folder?',
													'In the folder Bats present in the previous folder, what all files are present?',
													'How to see the files and folders present in the directory Bats which is located in the preceding folder?']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -l ..','NL Queries':['List all the files and folders in the parent directory along with their details.',
													'Give details of all files and folders present in the previous directory.',
													'How to see the details of all the files and folders in the preceding folder?',
													'Single command to get a detailed list of all files and folders in the parent folder.']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -lh ..','NL Queries':['List all files and folders present in previous folder in human readable format',
													'List all files and folders with details present in the parent directory. The file size should be rounded off.',
													'How to see the details of the files and folders present in the directory before the current one in human readable format?',
													'Single command to see details of files and folders located inside the parent directory in human readable format']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -r ..','NL Queries':['List files of the previous directory in reverse alphabetical order.',
													'How to see the contents of parent directory in reverse order?',
													'Single command to list files and folders of the parent directory in reverse alphabetical order.',
													'Show all folders of the preceding directory in reverse order on the command line.']},ignore_index = True) 
#To Keep or not to keep
ls = ls.append({'Command':'ls -lt ..','NL Queries':['List all files of previous directory in order of last modified with details.',
												'Show contents of the parent folder with their details. Sort them in the order of last modified.',
												'How to see the files and folders of the directory before the current one with details in order of last modified?',
												'Single command to get detailed list of files located inside the parent directory in order of last modified on the command line.']},ignore_index = True)
#To Keep or not to keep
ls = ls.append({'Command':'ls -lr ..','NL Queries':['Give detailed list of files and folders present in the preceding directory. Sort them in reverse alphabetical order.',
													'How to get detailed information about the files present in the parent directory sorted in reverse alphabetical order?',
													'Single command to see the contents of the previous folder with their details in reverse order.',
													'Show the folders present in the parent directory with details. Sort them in reverse alphabetical order.']},ignore_index = True)

ls = ls.append({'Command':'ls -i ..','NL Queries':['List files and folders of previous directory with their inode number.',
													'Show contents of parent directory with their inode number.',
													'What are the contents of the preceding folder and give their inode number?',
													'How to see the inode number of each file and folder in the previous directory?']},ignore_index = True)

ls = ls.append({'Command':'ls -la','NL Queries':['Give a detailed list of all the contents including hidden ones present in the current directory.',
												'How to see all files including hidden ones along with their details present in the current directory?',
												'How to see hidden files and folders of the current directory with their details?',
												'Single command to get a detailed list of files that start with . symbol']},ignore_index = True)

ls = ls.append({'Command':'ls -lS','NL Queries':['Give detailed list of files and folders present in current directory. Sort them in order of file size.',
												'How to see the files present in this directory with their details, sorted in order of file size?',
												'Single command to see the contents of this folder along with their details, sorted in order of size.',
												'Show the folders present in this directory with their details. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i','NL Queries':['Give list of files and folders present in current directory with their inode number. Sort them in order of size.',
												'How to see the files/folders present in this directory along with their inode number, sorted in order of size?',
												'Single command to see the contents of this folder with their inode number, sorted in order of size.',
												'Show the folders /files present in this directory with their inode number. Sort them in decreasing order of size.']},ignore_index = True)

ls = ls.append({'Command':'ls -li','NL Queries':['List all the files and folders in the current directory along with their details including inode number.',
												'Give details of all files and folders present in the current directory. Also show the inode number',
												'How to see the details of all the files in the current folder including inode number?',
												'Single command to get a detailed list of all files in the current folder including inode number.']},ignore_index = True)

ls = ls.append({'Command':'ls -t','NL Queries':['List all files in order of modified time, newest first.',
												'Show contents of present folder. Sort them in the order of newest modified to oldest modified.',
												'How to see the files and folders of this directory sorted in order of modification time, newest first?',
												'Single command to get a list of files sorted in order of modification time on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr','NL Queries':['List all files in order of modified time, oldest first.',
												'Show contents of present folder. Sort them in the order of oldest modified to newest modified.',
												'How to see the files and folders of this directory sorted in order of modification time, oldest first?',
												'Single command to get a list of files contained in the present folder. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -la Sam','NL Queries':['Give a detailed list of all the contents including hidden ones present in the Sam directory.',
													'How to see all files including hidden ones along with their details present in the directory named Sam?',
													'How to see hidden files and folders of the directory titled Sam with their details?',
													'Single command to get a detailed list of files located in the Sam folder that start with . symbol']},ignore_index = True)

ls = ls.append({'Command':'ls -lS Apple','NL Queries':['Give detailed list of files and folders present in Apple directory. Sort them in order of file size.',
													'How to see the files present in the directory Apple with their details, sorted in order of file size?',
													'Single command to see the contents of the folder named Apple along with their details, sorted in order of size.',
													'Show the folders present in the directory titled Apple with their details. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i Backpack','NL Queries':['Give list of files and folders present in the Backpack directory with their inode number. Sort them in order of file size.',
													'How to see the files present in the directory Backpack along with their inode number, sorted in order of file size?',
													'Single command to see the contents of the folder titled Backpack with their inode number, sorted in order of size.',
													'Show the folders present in the directory named Backpack with their inode number. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -li Dataset','NL Queries':['List all the files and folders in the directory named Dataset along with their details including inode number.',
														'Give details of all files and folders present in the Dataset directory. Also show the inode number',
														'How to see the details of all the files in the folder titled Dataset including inode number?',
														'Single command to get a detailed list of all files in the folder Dataset including inode number.']},ignore_index = True)

ls = ls.append({'Command':'ls -t Institution','NL Queries':['List all files of the folder Institution in order of modified time, newest first.',
															'Show contents of Institution folder. Sort them in the order of newest modified to last modified.',
															'How to see the files and folders of the directory named Institution sorted in order of modification time, newest first?',
															'Single command to get a list of files located inside the folder titled Institution sorted in order of modification time on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr School','NL Queries':['List all files of the folder School in order of modified time, oldest first.',
														'Show contents of the School folder. Sort them in the order of oldest modified to newest modified.',
														'How to see the files and folders of the directory titled School sorted in order of modification time, oldest first?',
														'Single command to get a list of files contained in the folder named School. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

###
ls = ls.append({'Command':'ls -la ..','NL Queries':['Give a detailed list of all the contents including hidden ones present in the parent directory.',
													'How to see all files including hidden ones along with their details present in the preceding directory?',
													'How to see hidden files and folders of the directory before this one with their details?',
													'Single command to get a detailed list of files contained in the previous folder that start with . symbol']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i ..','NL Queries':['Give list of files and folders present in previous directory with their inode number. Sort them in order of file size.',
													'How to see the files present in the directory before the current one along with their inode number, sorted in order of file size?',
													'Single command to see the contents of the parent folder with their inode number, sorted in order of size.',
													'Show the folders present in the directory before this one with their inode number. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -t ..','NL Queries':['List all files contained inside the preceding folder in order of modified time, newest first.',
													'Show contents of parent folder. Sort them in the order of newest modified to last modified.',
													'How to see the files and folders of the previous directory sorted in order of modification time, newest first?','Single command to get a list of files located in the preceding folder sorted in order of modification time on the command line.']},ignore_index = True)

###
ls = ls.append({'Command':'ls -a -1','NL Queries':['List all contents including hidden ones present in the current directory, one per line.',
													'How to see all files including hidden ones present in the current directory in a vertical list?',
													'How to see hidden files and folders of the current directory, one per line?',
													'Single command to see files that start with . symbol in a vertical list.']},ignore_index = True)

ls = ls.append({'Command':'ls -F -1','NL Queries':['List all files with folders highlighted with / character at the end, one per line.',
													'Give a vertical list of the contents of current directory and denote folders with a / symbol at the end.',
													'Highlight folders present in this directory with / character in a vertical list.',
													'Denote folders, one per line, present in this directory with / symbol at the end.']},ignore_index = True)

ls = ls.append({'Command':'ls -r -1','NL Queries':['Show a verical list of files sorted in reverse alphabetical order',
													'How to see the contents of present directory, one per line, in reverse order?',
													'Single command to list files and folders vertically in reverse alphabetical order.',
													'Show all folders of this directory, one per line, in reverse order on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -R -1','NL Queries':['List all files and folders of this directory and it\'s sub directories, one per line.',
													'Show the contents of this directory and the folders present in the current directory with their contents on the command line in a vertical list.',
													'How to see contents of this directory and it\'s sub directories, one per line?',
													'What is contained in this directory and folders of this directory? Show the results in a vertical list.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -1','NL Queries':['Give a vertical list of files and folders present in current directory. Sort them in order of file size.',
													'How to see the files present in this directory sorted in order of file size, one per line?',
													'Single command to see the contents of this folder in order of size, one per line.',
													'Show the folders present in this directory in a vertical list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -i -1','NL Queries':['List files vertically with it\'s inode number.',
													'Show contents of present directory with it\'s inode number in a vertical list.',
													'What are the contents of this folder and give their inode number? Show the results one per line',
													'How to see the inode number of each file in this directory, one per line?']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i -1','NL Queries':['Give list of files and folders present in current directory with their inode number. Sort them in order of file size in a vertical list.',
														'How to see the files present in this directory, one per line, along with their inode number, sorted in order of file size?',
														'Single command to see the contents of this folder, one per line, with their inode number, sorted in order of size.',
														'Show the folders present in this directory with their inode number in a vertical list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -t -1','NL Queries':['List all files, one per line, in order of modified time, newest first.',
													'Show contents of present folder in a vertical list. Sort them in the order of newest modified to last modified.',
													'How to see the files and folders of this directory, one per line, sorted in order of modification time, newest first?',
													'Single command to get a vertical list of files sorted in order of modification time on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr -1','NL Queries':['List all files, one per line, in order of modified time, oldest first.',
													'Show contents of present folder in a vertical list. Sort them in the order of oldest modified to newest modified.',
													'How to see the files and folders of this directory, one per line, sorted in order of modification time, oldest first?',
													'Single command to get a vertical list of files contained in the present folder. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

ls = ls.append({'Command':'ls -a -1 ..','NL Queries':['List all contents including hidden ones present in the parent directory, one per line.',
														'How to see all files including hidden ones present in the previous directory in a vertical list?',
														'How to see hidden files and folders of the preceding directory, one per line?',
														'Single command to see files located in the parent folder that start with . symbol in a vertical list.']},ignore_index = True)
ls = ls.append({'Command':'ls -r -1 ..','NL Queries':['Show a verical list of files located in the previous folder sorted in reverse alphabetical order.',
														'How to see the contents of parent folder, one per line, in reverse order?',
														'Single command to list files and folders of the preceding folder, vertically in reverse alphabetical order.',
														'Show all folders of the parent directory, one per line, in reverse order on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -1 ..','NL Queries':['Give a vertical list of files and folders present in the directory before the current one. Sort them in order of file size.',
													'How to see the files present in the parent directory sorted in order of file size, one per line?',
													'Single command to see the contents of the previous folder in order of size, one per line.',
													'Show the folders present in the preceding directory in a vertical list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i -1 ..','NL Queries':['Give list of files and folders present in the previous directory with their inode number. Sort them in order of file size in a vertical list.',
														'How to see the files present in the parent directory, one per line, along with their inode number, sorted in order of file size?',
														'Single command to see the contents of the preceding folder, one per line, with their inode number, sorted in order of size.',
														'Show the folders present in the directory before this one, with their inode number in a vertical list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr -1 ..','NL Queries':['List all files of the parent folder, one per line, in order of modified time, oldest first.',
														'Show contents of the previous folder in a vertical list. Sort them in the order of oldest modified to newest modified.',
														'How to see the files and folders of the preceding directory, one per line, sorted in order of modification time, oldest first?',
														'Single command to get a vertical list of files contained in the folder before this one. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -a -1 Jobs','NL Queries':['List all contents including hidden ones present in the Jobs directory, one per line.',
													'How to see all files including hidden ones present in the directory Jobs in a vertical list?',
													'How to see hidden files and folders of the directory titled Jobs, one per line?',
													'Single command to see files, one per line, located in the folder Jobs, that start with . symbol.']},ignore_index = True)

ls = ls.append({'Command':'ls -F -1 Space','NL Queries':['From the folder Space, list all files with folders highlighted with / character at the end, one per line.',
														'Give a vertical list of the contents of the directory named Space and denote folders with a / symbol at the end.',
														'Highlight folders present in the Space directory with / character in a vertical list.',
														'Denote folders, one per line, present in the directory Space with / symbol at the end.']},ignore_index = True)

ls = ls.append({'Command':'ls -r -1 Test','NL Queries':['Show a verical list of files located inside the folder Test sorted in reverse alphabetical order',
														'How to see the contents of the directory Test, one per line, in reverse order?',
														'Single command to list files and folders of the directory titled Test, vertically in reverse alphabetical order.',
														'Show all folders of the Test directory, one per line, in reverse order on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -R -1 Toronto','NL Queries':['List all files and folders of the Toronto directory and it\'s sub directories, one per line.',
															'Show the contents of the folder Toronto and the folders present in it with their contents on the command line in a vertical list.',
															'How to see contents of the Toronto directory and it\'s sub directories, one per line?',
															'What is contained in the directory named Toronto and folders of that directory? Show the results in a vertical list.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -1 Atlanta','NL Queries':['Give a vertical list of files and folders present in Atlanta directory. Sort them in order of file size.',
															'How to see the files/folders present in the directory Atlanta, sorted in order of file size, one per line?',
															'Single command to see the contents of the folder named Atlanta, in order of size, one per line.',
															'Show the files/folders present in the Atlanta directory in a vertical list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -i -1 Sample','NL Queries':['List files of directory Sample, vertically with it\'s inode number.',
															'Show contents of Sample directory with it\'s inode number in a vertical list.',
															'What are the contents of the folder named Sample and give their inode number? Show the results one per line.',
															'How to see the inode number of each file in the directory titled Sample, one per line?']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i -1 Combination','NL Queries':['Give list of files and folders present in Combination directory with their inode number. Sort them in order of file size in a vertical list.',
																'How to see the files present in the directory titled Combination, one per line, along with their inode number, sorted in order of file size?',
																'Single command to see the contents of the folder Combination, one per line, with their inode number, sorted in order of size.',
																'Show the folders present in the directory named Combination with their inode number in a vertical list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -t -1 Instructables','NL Queries':['List all files of the folder Instructables, one per line, in order of modified time, newest first.',
																'Show contents of Instructables folder in a vertical list. Sort them in the order of newest modified to last modified.',
																'How to see the files and folders of the directory named Instructables, one per line, sorted in order of modification time, newest first?',
																'Single command to get a vertical list of files located inside the folder Instructables, sorted in order of modification time on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr -1 Story','NL Queries':['List all folders/files of the folder Story, one per line, in order of modified time, oldest first.',
														'Show contents of Story folder in a vertical list. Sort them in the order of oldest modified to newest modified.',
														'How to see the files and folders of the directory named Story, one per line, sorted in order of modification time, oldest first?',
														'Single command to get a vertical list of files/folders contained in the folder Story. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

ls = ls.append({'Command':'ls -l --author','NL Queries':['List all the files and folders in the current directory along with their details including author\'s name.',
														'Give details of all files and folders present in the working directory. Also show the name of the author',
														'How to see the details of all the files in the current folder including author\'s name?',
														'Single command to get a detailed list of all files/folders in the current folder including name of the author.']},ignore_index = True)

ls = ls.append({'Command':'ls -B','NL Queries':['List files in current directory. Ignore the backup files.',
												'Files excluding the backup ones present in this directory.',
												'Name all contents, except the backup files, of my working directory.',
												'Show the files of the working directory. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f','NL Queries':['List all files including hidden ones in current directory without color coding.',
											'Files present in this directory, including hidden ones. Do not sort or color the files.',
											'Name all contents of my working directory without any color coding. Output should also include hidden files.',
											'Show the files of the working directory, including hidden ones. Do not sort or color the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -m','NL Queries':['Show contents of present folder in a comma separated list.',
												'List out files and folders of this directory in a comma separated list.',
												'How to see what all folders are present in this directory in a comma separated list?',
												'Single command to see contents of the current folder. The output should be a comma separated list.']},ignore_index = True)

ls = ls.append({'Command':'ls -s','NL Queries':['List files along with the size allocated to them in blocks.',
												'Show contents of present directory with allocated size in blocks.',
												'What are the contents of this folder and give their allocated size in blocks?',
												'How to see the allocated block size of each file in this directory?']},ignore_index = True)

ls = ls.append({'Command':'ls -U','NL Queries':['Show contents of present folder. Do not sort the files, show in directory order.',
												'List out files of this folder in directory order.',
												'How to see what all files are present in this folder in directory order?',
												'Single command to see contents of the current directory. The output should be in directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -x','NL Queries':['Show contents of present folder line-wise and not column-wise.',
												'List out files and folders of this directory line-wise.',
												'How to see what all folders are present in this directory line-wise?',
												'Single command to see contents of the current folder. The output should be line-wise and not column-wise.']},ignore_index = True)
####
ls = ls.append({'Command':'ls -l --author Smartphones','NL Queries':['List all the files and folders in the Smartphones directory along with their details including author\'s name.',
																'Give details of all files and folders present in the directory Smartphones. Also show the name of the author',
																'How to see the details of all the files in the folder titled Smartphones including author\'s name?',
																'Single command to get a detailed list of all files in the folder named Smartphones including name of the author.']},ignore_index = True)

ls = ls.append({'Command':'ls -B Artificial','NL Queries':['List files in the Artificial directory. Ignore the backup files.',
															'Files excluding the backup ones present in the directory Artificial.',
															'Name all contents, except the backup files, of the directory named Artificial.',
															'Show the files of the directory titled Artificial. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f Machines','NL Queries':['List files in the Machines directory without color coding. Output should include hidden files.',
														'Files present in the directory Machines, including hidden ones. Do not sort or color the files.',
														'Name all contents, including hidden ones, of the Machines directory without any color coding.',
														'Show the files of the directory named Machines, including hidden files. Do not sort or color the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -m Colors','NL Queries':['Show contents of Colors folder in a comma separated list.',
													'List out files and folders of the directory named Colors in a comma separated list.',
													'How to see what all folders are present in the Colors directory in a comma separated list?',
													'Single command to see contents of the Colors folder. The output should be a comma separated list.']},ignore_index = True)

#REad from here.
ls = ls.append({'Command':'ls -s Cost','NL Queries':['List files located in the Cost folder along with the size allocated to them in blocks.',
													'Show contents of the directory Cost with allocated size in blocks.',
													'What are the contents of the folder titled Cost and give their allocated size in blocks?',
													'How to see the allocated size of each file in the directory named Cost?']},ignore_index = True)

ls = ls.append({'Command':'ls -U Personal','NL Queries':['Show contents of the folder titled Personal. Do not sort the files, show in directory order',
														'List out files of the Personal folder in directory order.',
														'How to see what all files are present in the folder Personal in directory order?',
														'Single command to see contents of the directory named Personal. The output should be in directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -x Bhavesh','NL Queries':['Show contents of the folder Bhavesh line-wise and not column-wise.',
														'List out files and folders of the Bhavesh directory line-wise.',
														'How to see what all folders are present in the directory Bhavesh line-wise?',
														'Single command to see contents of the folder named Bhavesh. The output should be line-wise and not column-wise.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -l --author ..','NL Queries':['List all the files and folders in the parent directory along with their details including author\'s name.',
															'Give details of all files and folders present in the preceding directory. Also show the name of the author',
															'How to see the details of all the files in the previous folder including author\'s name?',
															'Single command to get a detailed list of all files in the parent folder including name of the author.']},ignore_index = True)

ls = ls.append({'Command':'ls -f ..','NL Queries':['List files in parent directory without color coding. Output should include hidden files.',
												'Files present in the directory before this one, including hidden ones. Do not sort or colorize the files.',
												'Name all contents of the previous directory without any color coding. The output should include hidden files.','Show the files of the preceding directory, including hidden ones. Do not sort or colorize the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s ..','NL Queries':['List files of the previous directory along with the size allocated to them in blocks.',
													'Show contents of the parent directory with allocated size in blocks.',
													'What are the contents of the preceding folder and give their allocated size in blocks?',
													'How to see the allocated size of each file in the previous directory?']},ignore_index = True)

ls = ls.append({'Command':'ls -x ..','NL Queries':['Show contents of parent folder line-wise and not column-wise.',
													'List out files and folders of the previous directory line-wise.',
													'How to see what all folders are present in the preceding directory line-wise?',
													'Single command to see contents of the parent folder. The output should be line-wise and not column-wise.']},ignore_index = True)

#####
ls = ls.append({'Command':'ls -B -1','NL Queries':['List files in current directory in a vertical list. Ignore the backup files.',
													'Files excluding the backup ones present in this directory, one per line.',
													'Name all contents, except the backup files, of my working directory in a vertical list.',
													'Show the files of the working directory, one per line. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f -1','NL Queries':['Give a vertical list of files in current directory without color coding. The output should include hidden files.',
													'Files present in this directory, including hidden ones. Do not sort or color the files. The output should be one per line',
													'Name all contents, including hidden ones of my working directory without any color coding in a vertical list.',
													'Show the files, including hidden ones, of the working directory in a vertical list. Do not sort or colorize the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -1','NL Queries':['List files along with the size allocated to them in blocks in a vertical list.',
												'Show contents of present directory with allocated size in blocks, one per line.',
												'What are the contents of this folder and give their allocated size in blocks in a vertical list?',
												'How to see the allocated size of each file in this directory in a vertical list?']},ignore_index = True)

ls = ls.append({'Command':'ls -U -1','NL Queries':['Show contents of present folder in a vertical list. Do not sort the files, show in directory order',
													'List out files of this folder in directory order, one per line.',
													'How to see what all files are present in this folder in directory order, one per line?',
													'Single command to see contents of the current directory in a vertical list. The output should be in directory order.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -B -1 Documents','NL Queries':['List files in Documents folder in a vertical list. Ignore the backup files.',
															'Files excluding the backup ones present in the directory Documents, one per line.',
															'Name all contents, except the backup files, of the Documents directory in a vertical list.',
															'Show the files of the directory titled Documents, one per line. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f -1 Photos','NL Queries':['Give a vertical list of files in Photos folder without color coding. The output should include hidden files.',
														'Files present in the directory titled Photos, including hidden ones. Do not sort or colorize the files. The output should be one per line',
														'Name all contents, including hidden ones, of the directory Photos without any color coding in a vertical list.',
														'Show the files, including hidden ones, of the Photos directory in a vertical list. Do not sort or colorize the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -1 Videos','NL Queries':['List files located inside the Videos folder along with the size allocated to them in blocks in a vertical list.',
															'Show contents of Videos directory with allocated size in blocks, one per line.',
															'What are the contents of the folder Videos and give their allocated size in blocks in a vertical list?',
															'How to see the allocated size of each file in the Videos directory in a vertical list?']},ignore_index = True)

ls = ls.append({'Command':'ls -U -1 Films','NL Queries':['Show contents of the folder Films in a vertical list. Do not sort the files, show in directory order',
														'List out files of the Films folder in directory order, one per line.',
														'How to see what all files are present in the Films folder in directory order, one per line?',
														'Single command to see contents of the directory Films in a vertical list. The output should be in directory order.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -B -1 ..','NL Queries':['List files in parent directory in a vertical list. Ignore the backup files.',
														'Files excluding the backup ones present in the preceding directory, one per line.',
														'Name all contents, except the backup files, of the previous directory in a vertical list.',
														'Show the files of the preceding directory, one per line. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -1 ..','NL Queries':['List files located in the parent directory along with the size allocated to them in blocks in a vertical list.',
													'Show contents of previous directory with allocated size in blocks, one per line.',
													'What are the contents of the folder before this one and give their allocated size in blocks in a vertical list?',
													'How to see the allocated size of each file in the preceding directory in a vertical list?']},ignore_index = True)

####
ls = ls.append({'Command':'ls -a -m','NL Queries':['List all contents including hidden ones present in the current directory in a comma separated list.',
													'How to see all files including hidden ones present in the current directory in a comma separated list?',
													'How to see hidden files and folders of the current directory, separated by commas?',
													'Single command to see files that start with . symbol in a comma separated list']},ignore_index = True)

ls = ls.append({'Command':'ls -F -m','NL Queries':['List all files with folders highlighted with / character at the end, separated by commas.',
													'Give a comma separated list of the contents of current directory and denote folders with a / symbol at the end.',
													'Highlight folders present in this directory with / character in a comma separated list.',
													'Denote folders, separated by commas, present in this directory with / symbol at the end.']},ignore_index = True)

ls = ls.append({'Command':'ls -r -m','NL Queries':['Show a comma separated list of files sorted in reverse alphabetical order',
													'How to see the contents of present directory, separated by commas, in reverse order?',
													'Single command to list files and folders in reverse alphabetical order, separated by commas.',
													'Show all folders of this directory, separated by commas, in reverse order on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -R -m','NL Queries':['List all files and folders of this directory and it\'s sub directories in a comma separated list.',
												'Show the contents of this directory and the folders present in the current directory with their contents on the command line in a comma separated list.',
												'How to see contents of this directory and it\'s sub directories, separated by commas?',
												'What is contained in this directory and folders of this directory? Show the results in a comma separated list.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -m','NL Queries':['Give a comma separated list of files and folders present in current directory. Sort them in order of file size.',
													'How to see the files present in this directory sorted in order of file size, separated by commas?',
													'Single command to see the contents of this folder in order of size, separated by commas.',
													'Show the folders present in this directory in a comma separated list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -i -m','NL Queries':['List files, separated by commas, with it\'s inode number.',
												'Show contents of present directory with it\'s inode number in a comma separated list.',
												'What are the contents of this folder and give their inode number? Show the results separated by commas.',
												'How to see the inode number of each file in this directory, separated by commas?']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i -m','NL Queries':['Give list of files and folders present in current directory with their inode number. Sort them in order of file size in a comma separated list.',
													'How to see the files present in this directory, separated by commas, along with their inode number, sorted in order of file size?',
													'Single command to see the contents of this folder, separated by commas, with their inode number, sorted in order of size.',
													'Show the folders present in this directory with their inode number in a comma separated list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -t -m','NL Queries':['List all files, separated by commas, in order of modified time, newest first.',
													'Show contents of present folder in a comma separated list. Sort them in the order of newest modified to last modified.',
													'How to see the files and folders of this directory, separated by commas, sorted in order of modification time, newest first?',
													'Single command to get a comma separated list of files sorted in order of modification time on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr -m','NL Queries':['List all files, separated by commas, in order of modified time, oldest first.',
													'Show contents of present folder in a comma separated list. Sort them in the order of oldest modified to newest modified.',
													'How to see the files and folders of this directory, separated by commas, sorted in order of modification time, oldest first?',
													'Single command to get a comma separated list of files contained in the present folder. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -a -m Documents','NL Queries':['List all contents including hidden ones present in the Documents directory in a comma separated list.',
															'How to see all files including hidden ones present in the directory Documents in a comma separated list?',
															'How to see hidden files and folders of the directory titled Documents, separated by commas?',
															'Single command to see files located in the Documents folder that start with . symbol in a comma separated list.']},ignore_index = True)

ls = ls.append({'Command':'ls -F -m Videos','NL Queries':['List all files with folders highlighted with / character at the end, separated by commas.',
														'Give a comma separated list of the contents of current directory and denote folders with a / symbol at the end.',
														'Highlight folders present in this directory with / character in a comma separated list.',
														'Denote folders, separated by commas, present in this directory with / symbol at the end.']},ignore_index = True)

ls = ls.append({'Command':'ls -r -m Pictures','NL Queries':['Show a comma separated list of files sorted in reverse alphabetical order',
														'How to see the contents of present directory, separated by commas, in reverse order?',
														'Single command to list files and folders in reverse alphabetical order, separated by commas.',
														'Show all folders of this directory, separated by commas, in reverse order on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -R -m Music','NL Queries':['List all files and folders of this directory and it\'s sub directories in a comma separated list.',
														'Show the contents of this directory and the folders present in the current directory with their contents on the command line in a comma separated list.',
														'How to see contents of this directory and it\'s sub directories, separated by commas?',
														'What is contained in this directory and folders of this directory? Show the results in a comma separated list.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -m Festival','NL Queries':['Give a comma separated list of files and folders present in current directory. Sort them in order of file size.',
														'How to see the files present in this directory sorted in order of file size, separated by commas?',
														'Single command to see the contents of this folder in order of size, separated by commas.',
														'Show the folders present in this directory in a comma separated list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -i -m Carnival','NL Queries':['List files, separated by commas, with it\'s inode number.',
															'Show contents of present directory with it\'s inode number in a comma separated list.',
															'What are the contents of this folder and give their inode number? Show the results separated by commas.',
															'How to see the inode number of each file in this directory, separated by commas?']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i -m Tunes','NL Queries':['Give list of files and folders present in current directory with their inode number. Sort them in order of file size in a comma separated list.',
															'How to see the files present in this directory, separated by commas, along with their inode number, sorted in order of file size?',
															'Single command to see the contents of this folder, separated by commas, with their inode number, sorted in order of size.',
															'Show the folders present in this directory with their inode number in a comma separated list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -t -m Box','NL Queries':['List all files, separated by commas, in order of modified time, newest first.',
														'Show contents of present folder in a comma separated list. Sort them in the order of newest modified to last modified.',
														'How to see the files and folders of this directory, separated by commas, sorted in order of modification time, newest first?',
														'Single command to get a comma separated list of files sorted in order of modification time on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr -m Cards','NL Queries':['List all files, separated by commas, in order of modified time, oldest first.',
														'Show contents of present folder in a comma separated list. Sort them in the order of oldest modified to newest modified.',
														'How to see the files and folders of this directory, separated by commas, sorted in order of modification time, oldest first?',
														'Single command to get a comma separated list of files contained in the present folder. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

###
ls = ls.append({'Command':'ls -a -m ..','NL Queries':['List all contents including hidden ones present in the current directory in a comma separated list.',
													'How to see all files including hidden ones present in the current directory in a comma separated list?',
													'How to see hidden files and folders of the current directory, separated by commas?',
													'Single command to see files that start with . symbol in a comma separated list']},ignore_index = True)

ls = ls.append({'Command':'ls -r -m ..','NL Queries':['Show a comma separated list of files sorted in reverse alphabetical order',
													'How to see the contents of present directory, separated by commas, in reverse alphabetical order?',
													'Single command to list files and folders in reverse alphabetical order, separated by commas.',
													'Show all folders of this directory, separated by commas, in reverse alphabetical order on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -m ..','NL Queries':['Give a comma separated list of files and folders present in current directory. Sort them in order of file size.',
													'How to see the files present in this directory sorted in order of file size, separated by commas?',
													'Single command to see the contents of this folder in order of size, separated by commas.',
													'Show the folders present in this directory in a comma separated list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i -m ..','NL Queries':['Give list of files and folders present in current directory with their inode number. Sort them in order of file size in a comma separated list.',
														'How to see the files present in this directory, separated by commas, along with their inode number, sorted in order of file size?',
														'Single command to see the contents of this folder, separated by commas, with their inode number, sorted in order of size.',
														'Show the folders present in this directory with their inode number in a comma separated list. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr -m ..','NL Queries':['List all files, separated by commas, in order of modified time, oldest first.',
														'Show contents of present folder in a comma separated list. Sort them in the order of oldest modified to newest modified.',
														'How to see the files and folders of this directory, separated by commas, sorted in order of modification time, oldest first?',
														'Single command to get a comma separated list of files contained in the present folder. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

#####
ls = ls.append({'Command':'ls -a -x','NL Queries':['List all contents including hidden ones present in the current directory line-wise, not column-wise.',
													'How to see all files including hidden ones present in the current directory line by line?',
													'How to see hidden files and folders of the current directory, line by line?',
													'Single command to see files that start with . symbol. The output should listed line-wise and not column-wise.']},ignore_index = True)

ls = ls.append({'Command':'ls -F -x','NL Queries':['List all files with folders highlighted with / character at the end, line by line.',
												'Give contents, line by line, of the current directory and denote folders with a / symbol at the end.',
												'Highlight folders present in this directory with / character, line-wise and not column-wise.','Denote folders, line-wise, present in this directory with / symbol at the end.']},ignore_index = True)

ls = ls.append({'Command':'ls -r -x','NL Queries':['Show files, line by line, sorted in reverse alphabetical order',
												'How to see the contents of present directory, line-wise, in reverse order?',
												'Single command to list files and folders in reverse alphabetical order, line-wise.',
												'Show all folders of this directory, line by line, in reverse order on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -R -x','NL Queries':['List all files and folders of this directory and it\'s sub directories, line-wise and not column-wise.',
												'Show the contents of this directory and the folders present in the current directory with their contents on the command line. List entries by lines.',
												'How to see contents of this directory and it\'s sub directories, listed by lines?',
												'What is contained in this directory and folders of this directory? Show the results by lines and not by columns.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -x','NL Queries':['Give files and folders, line-wise, present in current directory. Sort them in order of file size.',
												'How to see the files present in this directory sorted in order of file size, listed by lines?',
												'Single command to see the contents of this folder in order of size, listed by lines.',
												'Show the folders present in this directory, line by line. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -i -x','NL Queries':['List files by lines, with it\'s inode number.',
												'Show contents of present directory with it\'s inode number. List the entries by lines and not by columns',
												'What are the contents of this folder and give their inode number? Show the results line by line.',
												'How to see the inode number of each file in this directory, line-wise?']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i -x','NL Queries':['Give list of files and folders present in current directory with their inode number. Sort them in order of file size, line by line.',
											'How to see the files present in this directory, listed by lines, along with their inode number, sorted in order of file size?',
											'Single command to see the contents of this folder, line-wise, with their inode number, sorted in order of size.',
											'Show the folders present in this directory with their inode number, listed by lines. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -t -x','NL Queries':['List all files, line by line, in order of modified time, newest first.',
													'Show contents of present folder, line by line. Sort them in the order of newest modified to last modified.',
													'How to see the files and folders of this directory, listed by lines, sorted in order of modification time, newest first?',
													'Single command to get files sorted in order of modification time, listed by lines.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr -x','NL Queries':['List all files, line-wise, in order of modified time, oldest first.',
													'Show contents of present folder, line by line. Sort them in the order of oldest modified to newest modified.',
													'How to see the files and folders of this directory, listed by lines, sorted in order of modification time, oldest first?',
													'Single command to get a list of files contained in the present folder, line by line. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -a -x Documents','NL Queries':['List all contents including hidden ones present in the Documents folder line-wise, not column-wise.',
															'How to see all files including hidden ones present in the directory Documents line by line?',
															'How to see hidden files and folders of the directory titled Documents, line by line?',
															'Single command to see files in the Documents folder that start with . symbol. The output should listed line-wise and not column-wise.']},ignore_index = True)

ls = ls.append({'Command':'ls -F -x Pictures','NL Queries':['List all files inside the Pictures folder with folders highlighted with / character at the end, line by line.',
															'Give contents, line by line, of the directory Pictures and denote folders with a / symbol at the end.',
															'Highlight folders present in the Pictures directory with / character, line-wise and not column-wise.',
															'Denote folders, line-wise, present in the directory Pictures with / symbol at the end.']},ignore_index = True)

ls = ls.append({'Command':'ls -r -x Videos','NL Queries':['Show files of the folder Videos, line by line, sorted in reverse alphabetical order',
														'How to see the contents of Videos directory, line-wise, in reverse order?',
														'Single command to list files and folders inside the directory Videos in reverse alphabetical order, line-wise.',
														'Show all folders of the Videos directory, line by line, in reverse order on the command line.']},ignore_index = True)

ls = ls.append({'Command':'ls -R -x Photos','NL Queries':['List all files and folders of the Photos directory and it\'s sub directories, line-wise and not column-wise.',
														'Show the contents of the Photos directory and the folders present inside it with their contents on the command line. List entries by lines.',
														'How to see contents of the Photos folder and it\'s sub directories, listed by lines?',
														'What is contained in the Videos directory and it\'s folders ? Show the results by lines and not by columns.']},ignore_index = True)

ls = ls.append({'Command':'ls -S -x Music','NL Queries':['Give files and folders, line-wise, present in Music directory. Sort them in order of file size.',
														'How to see the files present in the directory Music sorted in order of file size, listed by lines?',
														'Single command to see the contents of the Music folder in order of size, listed by lines.',
														'Show the folders present in the directory named Music, line by line. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -i -x Tones','NL Queries':['List files by lines of the directory Tones, with it\'s inode number.',
														'Show contents of Tones directory with it\'s inode number. List the entries by lines and not by columns',
														'What are the contents of the folder Tones and give their inode number? Show the results line by line.',
														'How to see the inode number of each file in the Tones directory, line-wise?']},ignore_index = True)

ls = ls.append({'Command':'ls -S -i -x Tunes','NL Queries':['Give list of files and folders present in Tunes directory with their inode number. Sort them in order of file size, line by line.',
															'How to see the files present in the directory named Tunes, listed by lines, along with their inode number, sorted in order of file size?',
															'Single command to see the contents of the folder Tunes, line-wise, with their inode number, sorted in order of size.',
															'Show the folders present in the Tunes directory with their inode number, listed by lines. Sort them in decreasing order of file size.']},ignore_index = True)

ls = ls.append({'Command':'ls -t -x Library','NL Queries':['List all files of the folder named Library, line by line, in order of modified time, newest first.',
														'Show contents of Library folder, line by line. Sort them in the order of newest modified to last modified.',
														'How to see the files and folders of the directory titled Library, listed by lines, sorted in order of modification time, newest first?',
														'Single command to get files of the Library directory sorted in order of modification time, listed by lines.']},ignore_index = True)

ls = ls.append({'Command':'ls -tr -x Books','NL Queries':['List all files of the Books folder, line-wise, in order of modified time, oldest first.',
														'Show contents of folder named Books, line by line. Sort them in the order of oldest modified to newest modified.',
														'How to see the files and folders of the directory Books, listed by lines, sorted in order of modification time, oldest first?',
														'Single command to get a list of files contained in the Books folder, line by line. The files that have not been accessed recently are placed at the beginning.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -F -x ..','NL Queries':['From the parent directory, list all files with folders highlighted with / character at the end, line by line.',
												'Give contents, line by line, of the previous directory and denote folders with a / symbol at the end.',
												'Highlight folders present in the preceding directory with / character, line-wise and not column-wise.',
												'Denote folders, line-wise, present in the preceding directory with / symbol at the end.']},ignore_index = True)

ls = ls.append({'Command':'ls -R -x ..','NL Queries':['List all files and folders of the parent directory and it\'s sub directories, line-wise and not column-wise.',
													'Show the contents of the preceding directory and the folders present in the current directory with their contents on the command line. List entries by lines.',
													'How to see contents of the previous directory and it\'s sub directories, listed by lines?',
													'What is contained in the preceding directory and folders of this directory? Show the results by lines and not by columns.']},ignore_index = True)

ls = ls.append({'Command':'ls -i -x ..','NL Queries':['List files located inside the parent directory, line by line, with it\'s inode number.',
													'Show contents of previous directory with it\'s inode number. List the entries by lines and not by columns',
													'What are the contents of the parent folder and give their inode number? Show the results line by line.',
													'How to see the inode number of each file in the previous directory, line-wise?']},ignore_index = True)

ls = ls.append({'Command':'ls -t -x ..','NL Queries':['List all files of the parent folder, line by line, in order of modified time, newest first.',
													'Show contents of previous folder, line by line. Sort them in the order of newest modified to last modified.',
													'How to see the files and folders of the preceding directory, listed by lines, sorted in order of modification time, newest first?',
													'Single command to get files of the parent folder sorted in order of modification time, listed by lines.']},ignore_index = True)

#####
ls = ls.append({'Command':'ls -B -l','NL Queries':['List details of files in current directory. Ignore the backup files.',
												'Detailed list of files excluding the backup ones present in this directory.',
												'Show details of contents, except the backup files, of my working directory.',
												'Show the details of files of the working directory. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f -l','NL Queries':['List details of all files including hidden ones in current directory without color coding.',
												'Detailed list of files present in this directory, including hidden ones. Do not sort or color the files.',
												'Show details of all contents of my working directory without any color coding. Output should also include hidden files.',
												'Show detailed list of files of the working directory, including hidden ones. Do not sort or color the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -l','NL Queries':['List details of files along with the size allocated to them in blocks.',
													'Show details of contents of present directory with allocated size in blocks.',
													'What are the details of the contents of this folder and give their allocated size in blocks?',
													'How to see detailed information about each file in this directory along with their allocated size in blocks?']},ignore_index = True)

ls = ls.append({'Command':'ls -U -l','NL Queries':['Show details of contents of present folder. Do not sort the files, show in directory order.',
													'List out details of files of this folder in directory order.',
													'How to see details of all files that are present in this folder in directory order?',
													'Single command to see a detailed list of contents of the current directory. The output should be in directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -m','NL Queries':['List files, separated by commas, in current directory. Ignore the backup files.',
													'Show a comma separated list of files excluding the backup ones present in this directory.',
													'Name all contents, separated by commas, except the backup files, of my working directory.',
													'Show the files of the working directory in a comma separated list. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f -m','NL Queries':['Give a comma separated list of all files including hidden ones in current directory without color coding.',
													'Files present in this directory, including hidden ones, separated by commas. Do not sort or color the files.',
													'Name all contents of my working directory without any color coding in a comma separated list. Output should also include hidden files.',
													'Show the files of the working directory, including hidden ones in a comma separated list. Do not sort or colorize the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -m','NL Queries':['Show a comma separated list of files along with the size allocated to them in blocks.',
													'Show contents of present directory with allocated size in blocks, separated by commas.',
													'What are the contents of this folder and give their allocated size in blocks in a comma separated list?',
													'How to see the allocated size of each file in this directory in a comma separated list?']},ignore_index = True)

ls = ls.append({'Command':'ls -U -m','NL Queries':['Show contents of present folder in a comma separated list. Do not sort the files, show in directory order',
													'List out files of this folder by directory order, in a comma separated list.',
													'How to see what all files are present in this folder, separated by commas in directory order?',
													'Single command to see contents of the current directory in a comma separated list. The output should be in directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -x','NL Queries':['List files in current directory, line by line. Ignore the backup files.',
													'Show files, line-wise, excluding the backup ones present in this directory.',
													'Name all contents, except the backup files, of my working directory, line by line.',
													'Show the files of the working directory, line-wise. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f -x','NL Queries':['List all files, line by line, including hidden ones in current directory without color coding.',
													'Show files, line-wise, present in this directory, including hidden ones. Do not sort or color the files.',
													'Name all contents of my working directory without any color coding. Output should also include hidden files and be listed line by line.',
													'Show the files of the working directory, including hidden ones, line by line. Do not sort or color the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -x','NL Queries':['List files along with the size allocated to them in blocks, line by line.',
														'Show contents of present directory with allocated size in blocks, line-wise and not column-wise.',
														'What are the contents of this folder and give their allocated size in blocks? Show the ouput line by line.',
														'How to see the allocated size of each file in this directory, listed line-wise?']},ignore_index = True)

ls = ls.append({'Command':'ls -U -x','NL Queries':['Show contents of present folder line by line. Do not sort the files, show in directory order',
												'List out files of this folder by directory order, line-wise and not column-wise.',
												'How to see what all files are present in this folder in directory order, listed line by line?',
												'Single command to see contents of the current directory. The output should be in directory order and listed line-wise.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -f','NL Queries':['List files in current directory and include hidden elements. Ignore the backup files and give output without color coding.',
												'Files excluding the backup ones but including hidden ones, present in this directory. The output should not be sorted or color coded.',
												'Name all contents, except the backup files, of my working directory without sorting or color coding.',
												'Show the files of the working directory including hidden files. Ignore the backup files and do not color code.']},ignore_index = True)

ls = ls.append({'Command':'ls -U -B','NL Queries':['Show contents of present folder excluding backup files. Do not sort the files, show in directory order.',
													'List out files of this folder, excluding backup files, by directory order.',
													'How to see what all files are present in this folder, excluding the backup files, in directory order?',
													'Single command to see contents of the current directory. The output should not contain backup files and be listed by directory order.']},ignore_index = True)
####
ls = ls.append({'Command':'ls -B -l Documents','NL Queries':['List details of files/folders in Documents directory. Ignore the backup files.',
															'Detailed list of files/folders excluding the backup ones present in the directory titled Documents.',
															'Show details of contents, except the backup files, of the directory named Documents.',
															'Show the details of files of the Documents directory. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f -l Videos','NL Queries':['List details of all files/folders including hidden ones in Videos directory without color coding.',
														'Detailed list of files and folders present in the directory named Videos, including hidden ones. Do not sort or colorize the files.',
														'Show details of all contents of the Videos directory without any color coding. Output should also include hidden files.',
														'Show detailed list of files of the directory titled Videos, including hidden ones. Do not sort or colorize the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -l Photos','NL Queries':['List details of files present in the Photos folder along with the size allocated to them in blocks.',
														'Show details of contents of Photos directory with allocated size in blocks.',
														'What are the details of the contents of the folder Photos and give their allocated size in blocks?',
														'How to see detailed information about each file in the Photos directory along with their allocated size in blocks?']},ignore_index = True)

ls = ls.append({'Command':'ls -U -l Contacts','NL Queries':['Show details of contents of Contacts folder. Do not sort the files, show in directory order.',
															'List out details of files of the folder Contacts in directory order.',
															'How to see details of all files that are present in the folder Contacts in directory order?',
															'Single command to see a detailed list of contents of the directory named Contacts. The output should be in directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -m Pictures','NL Queries':['List files, separated by commas, located in Pictures directory. Ignore the backup files.',
															'Show a comma separated list of files excluding the backup ones present in the directory named Pictures.',
															'Name all contents, separated by commas, except the backup files, of the directory titled Pictures.',
															'Show the files of the Pictures directory in a comma separated list. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f -m Music','NL Queries':['Give a comma separated list of all files including hidden ones in the Music directory without color coding.',
														'Files present in the directory Music, including hidden ones, separated by commas. Do not sort or color the files.',
														'Name all contents of the Music directory without any color coding in a comma separated list. Output should also include hidden files.',
														'Show the files of the directory Music, including hidden ones in a comma separated list. Do not sort or color the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -m Songs','NL Queries':['Show a comma separated list of files present in the folder Songs along with the size allocated to them in blocks.',
														'Show contents of Songs directory with allocated size in blocks, separated by commas.',
														'What are the contents of the folder Songs and give their allocated size in blocks in a comma separated list?',
														'How to see the allocated size of each file in the directory Songs in a comma separated list?']},ignore_index = True)

ls = ls.append({'Command':'ls -U -m Tunes','NL Queries':['Show contents of the Tunes folder in a comma separated list. Do not sort the files, show in directory order.',
														'List out files of the folder Tunes by directory order, in a comma separated list.',
														'How to see what all files are present in the folder named Tunes, separated by commas in directory order?',
														'Single command to see contents of the Tunes directory in a comma separated list. The output should be in directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -x Tones','NL Queries':['List files in the Tones directory, line by line. Ignore the backup files.',
														'Show files, line-wise, excluding the backup ones present in the directory named Tones.',
														'Name all contents, except the backup files, of the directory Tones, line by line.',
														'Show the files of the Tones directory, line-wise. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -f -x Motion','NL Queries':['List all files, line by line, including hidden ones in the Motion directory without color coding.',
														'Show files, line-wise, present in the directory Motion, including hidden ones. Do not sort or colorize the files.',
														'Name all contents of the directory Motion without any color coding. Output should also include hidden files and be listed line by line.',
														'Show the files of the Motion directory, including hidden ones, line by line. Do not sort or colorize the files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -x Animation','NL Queries':['List files present in the Animation folder along with the size allocated to them in blocks, line by line.',
															'Show contents of Animation directory with allocated size in blocks, line-wise and not column-wise.',
															'What are the contents of the folder Animation and give their allocated size in blocks? Show the ouput line by line.',
															'How to see the allocated size of each file in the directory named Animation, listed line-wise?']},ignore_index = True)

ls = ls.append({'Command':'ls -U -x PDF','NL Queries':['Show contents of the PDF folder line by line. Do not sort the files, show in directory order.',
														'List out files of the folder PDF by directory order, line-wise and not column-wise.',
														'How to see what all files are present in the PDF folder in directory order, listed line by line?',
														'Single command to see contents of the directory named PDF. The output should be in directory order and listed line-wise.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -f Sample','NL Queries':['List files in the Sample directory and include hidden elements. Ignore the backup files and give output without color coding.',
															'Files excluding the backup ones but including hidden ones, present in the directory named Sample. The output should not be sorted or color coded.',
															'Name all contents, except the backup files, of the Sample directory without sorting or color coding.',
															'Show the files of the directory Sample including hidden files. Ignore the backup files and do not color code.']},ignore_index = True)

ls = ls.append({'Command':'ls -U -B Habits','NL Queries':['Show contents of the Habits folder excluding backup files. Do not sort the files, show in directory order',
															'List out files of the folder named Habits, excluding backup files, by directory order.',
															'How to see what all files are present in the folder titled Habits, excluding the backup files, in directory order?',
															'Single command to see contents of the directory named Habits. The output should not contain backup files and be listed by directory order.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -B -l ..','NL Queries':['List details of files in the parent directory. Ignore the backup files.',
														'Detailed list of files excluding the backup ones present in the previous directory.',
														'Show details of contents, except the backup files, of the directory before this one.',
														'Show the details of files of the preceding directory. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -l ..','NL Queries':['List details of files located in the parent folder along with the size allocated to them in blocks.',
														'Show details of contents of the previous directory with allocated size in blocks.',
														'What are the details of the contents of the preceding folder and give their allocated size in blocks?',
														'How to see detailed information about each file in the previous directory along with their allocated size in blocks?']},ignore_index = True)

ls = ls.append({'Command':'ls -B -m ..','NL Queries':['List files, separated by commas, located in the parent directory. Ignore the backup files.',
														'Show a comma separated list of files excluding the backup ones present in the preceding directory.',
														'Name all contents, separated by commas, except the backup files, of the previous directory.',
														'Show the files of the parent directory in a comma separated list. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -m ..','NL Queries':['Show a comma separated list of files located in the previous folder along with the size allocated to them in blocks.',
													'Show contents of preceding directory with allocated size in blocks, separated by commas.',
													'What are the contents of the parent folder and give their allocated size in blocks in a comma separated list?',
													'How to see the allocated size of each file in the previous directory in a comma separated list?']},ignore_index = True)

ls = ls.append({'Command':'ls -B -x ..','NL Queries':['List files in the previous directory, line by line. Ignore the backup files.',
													'Show files, line-wise, excluding the backup ones present in the preceding directory.',
													'Name all contents, except the backup files, of the parent directory, line by line.',
													'Show the files of the preceding directory, line-wise. Ignore the backup files.']},ignore_index = True)

ls = ls.append({'Command':'ls -s -x ..','NL Queries':['List files present in the previous folder along with the size allocated to them in blocks, line by line.',
													'Show contents of parent directory with allocated size in blocks, line-wise and not column-wise.',
													'What are the contents of the previous folder and give their allocated size in blocks? Show the ouput line by line.',
													'How to see the allocated size of each file in the parent directory, listed line-wise?']},ignore_index = True)

ls = ls.append({'Command':'ls -B -f ..','NL Queries':['List files in preceding folder and include hidden elements. Ignore the backup files and give output without color coding.',
														'Show files excluding the backup ones but including hidden ones, present in the parent directory. The output should not be sorted or color coded.',
														'Name all contents, except the backup files, of my the previous folder without sorting or color coding.',
														'Show the files of the preceding folder including hidden files. Ignore the backup files and do not color code.']},ignore_index = True)

###
ls = ls.append({'Command':'ls -B -f -1','NL Queries':['Give a vertical list of files in current directory and include hidden elements. Ignore the backup files and give output without color coding.',
													'Files excluding the backup ones but including hidden ones, present in this directory. The output should not be sorted or color coded and be listed one per line.',
													'Name all contents, except the backup files, of my working directory without sorting or color coding in a vertical list.',
													'Show the files of the working directory including hidden files in a vertical list. Ignore the backup files and do not color code.']},ignore_index = True)

ls = ls.append({'Command':'ls -U -B -1','NL Queries':['Show contents of present folder excluding backup files. Do not sort the files, show in directory order, one per line',
													'List out files of this folder, excluding backup files, by directory order in a vertical list.',
													'How to see what all files are present in this folder, excluding the backup files, in directory order one per line?',
													'Single command to see contents of the current directory in a vertical list. The output should not contain backup files and be listed by directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -f -m','NL Queries':['List files in current directory and include hidden elements. Ignore the backup files and give output without color coding in a comma separated list.',
													'Files excluding the backup ones but including hidden ones, present in this directory. The output should not be sorted or color coded and be listed in a comma separated list.',
													'Name all contents, except the backup files, of my working directory without sorting or color coding in a comma separated list.',
													'Show the files of the working directory, separated by commas, including hidden files. Ignore the backup files and do not color code.']},ignore_index = True)

ls = ls.append({'Command':'ls -U -B -m','NL Queries':['Show contents of present folder excluding backup files. Do not sort the files, show by directory order in a comma separated list.',
													'List out files of this folder, excluding backup files, by directory order in a comma separated list.',
													'How to see what all files are present in this folder, excluding the backup files, in directory order? The output should be in a comma separated list.',
													'Single command to see contents of the current directory in a comma separated list. The output should not contain backup files and be listed by directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -f -x','NL Queries':['List files in current directory and include hidden elements. Ignore the backup files and give output without color coding, line by line.',
													'Files excluding the backup ones but including hidden ones, present in this directory, listed line-wise. The output should not be sorted or color coded.',
													'Name all contents, except the backup files, of my working directory without sorting or color coding, listed line by line.',
													'Show the files of the working directory including hidden files. Ignore the backup files and do not color code. The output should be listed line-wise.']},ignore_index = True)

ls = ls.append({'Command':'ls -U -B -x','NL Queries':['Show contents of present folder excluding backup files. Do not sort the files, show by directory order, listed line by line.',
														'List out files of this folder, excluding backup files, by directory order. The output should be listed line by line, not by columns.',
														'How to see what all files are present in this folder, excluding the backup files, in directory order, listed line-wise?',
														'Single command to see contents of the current directory. The output should not contain backup files and be listed by directory order, line by line.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -B -f -1 Delivery','NL Queries':['Give a vertical list of files in the Delivery directory and include hidden elements. Ignore the backup files and give output without color coding.',
															'Files excluding the backup ones but including hidden ones, present in the directory named Delivery. The output should not be sorted or color coded and be listed one per line.',
															'Name all contents, except the backup files, of the Delivery directory without sorting or color coding in a vertical list.',
															'Show the files of the directory Delivery including hidden files in a vertical list. Ignore the backup files and do not color code.']},ignore_index = True)

ls = ls.append({'Command':'ls -U -B -1 Clothes','NL Queries':['Show contents of Clothes folder excluding backup files. Do not sort the files, show in directory order, one per line',
														'List out files of the folder Clothes, excluding backup files, by directory order in a vertical list.',
														'How to see what all files are present in the folder Clothes, excluding the backup files, in directory order one per line?',
														'Single command to see contents of the Clothes directory in a vertical list. The output should not contain backup files and be listed by directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -f -m Diamonds','NL Queries':['List files in the Diamonds directory and include hidden elements. Ignore the backup files and give output without color coding in a comma separated list.',
														'Files excluding the backup ones but including hidden ones, present in the directory titled Diamonds. The output should not be sorted or color coded and be listed in a comma separated list.',
														'Name all contents, except the backup files, of the directory Diamonds without sorting or color coding in a comma separated list.',
														'Show the files of the Diamonds folder, separated by commas, including hidden files. Ignore the backup files and do not color code.']},ignore_index = True)

ls = ls.append({'Command':'ls -U -B -m Birds','NL Queries':['Show contents of Birds folder excluding backup files. Do not sort the files, show by directory order in a comma separated list.',
													'List out files of the folder named Birds, excluding backup files, by directory order in a comma separated list.',
													'How to see what all files are present in the Birds folder, excluding the backup files, in directory order? The output should be in a comma separated list.',
													'Single command to see contents of the Birds directory in a comma separated list. The output should not contain backup files and be listed by directory order.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -f -x Invoice','NL Queries':['List files in the Invoice directory and include hidden elements. Ignore the backup files and give output without color coding, line by line.',
															'Files excluding the backup ones but including hidden ones, present in the directory Invoice, listed line-wise. The output should not be sorted or color coded.',
															'Name all contents, except the backup files, of my the Invoice folder without sorting or color coding, listed line by line.',
															'Show the files of the Invoice directory including hidden files. Ignore the backup files and do not color code. The output should be listed line-wise.']},ignore_index = True)

ls = ls.append({'Command':'ls -U -B -x Magic','NL Queries':['Show contents of the Magic folder excluding backup files. Do not sort the files, show by directory order, listed line by line.',
															'List out files of the folder named Magic, excluding backup files, by directory order. The output should be listed line by line, not by columns.',
															'How to see what all files are present in the folder titled Magic, excluding the backup files, in directory order, listed line-wise?',
															'Single command to see contents of the Magic directory. The output should not contain backup files and be listed by directory order, line by line.']},ignore_index = True)

###
ls = ls.append({'Command':'ls -B -f -1 ..','NL Queries':['Give a vertical list of files in parent directory and include hidden elements. Ignore the backup files and give output without color coding.',
														'Files excluding the backup ones but including hidden ones, present in the previous directory. The output should not be sorted or color coded and be listed one per line.',
														'Name all contents, except the backup files, of the previous folder without sorting or color coding in a vertical list.',
														'Show the files of the parent directory including hidden files in a vertical list. Ignore the backup files and do not color code.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -f -m ..','NL Queries':['List files in preceding directory and include hidden elements. Ignore the backup files and give output without color coding in a comma separated list.',
														'Files excluding the backup ones but including hidden ones, present in the parent directory. The output should not be sorted or color coded and be listed in a comma separated list.',
														'Name all contents, except the backup files, of the preceding directory without sorting or color coding in a comma separated list.',
														'Show the files of the parent directory, separated by commas, including hidden files. Ignore the backup files and do not color code.']},ignore_index = True)

ls = ls.append({'Command':'ls -B -f -x ..','NL Queries':['List files in the preceding directory and include hidden elements. Ignore the backup files and give output without color coding, line by line.',
														'Files excluding the backup ones but including hidden ones, present in the parent directory, listed line-wise. The output should not be sorted or color coded.',
														'Name all contents, except the backup files, of the previous folder without sorting or color coding, listed line by line.',
														'Show the files of the parent directory including hidden files. Ignore the backup files and do not color code. The output should be listed line-wise.']},ignore_index = True)

###
ls = ls.append({'Command':'ls -lt -u','NL Queries':['Show a detailed list of files in the working directory and sort them by time of last access, newest first.',
													'List files of the current directory with their details, including the time of last access. Also, sort them by this time, newest first.',
													'Show and sort a detailed list of files in the present directory by their time of last access, newest first.',
													'Single command to see a detailed list of files of this folder sorted from the most recently accessed file to the oldest accessed file.']},ignore_index = True)

ls = ls.append({'Command':'ls -lt -c','NL Queries':['Show a detailed list of files in the working directory and sort them by time of last modification of file status, newest first.',
													'List files of the current directory with their details, including the time of last modification of file status. Also, sort them by this time, newest first.',
													'Show and sort a detailed list of files in the present directory by their time of last modification of file status, newest first.',
													'Single command to see a detailed list of files of this folder sorted from the most recently modified file to the oldest modified file.']},ignore_index = True)

ls = ls.append({'Command':'ls -lt -u -r','NL Queries':['Show a detailed list of files in the working directory and sort them by time of last access, oldest first.',
														'List files of the current directory with their details, including the time of last access. Also, sort them by this time, oldest first.',
														'Show and sort a detailed list of files in the present directory by their time of last access, oldest first.',
														'Single command to see a detailed list of files of this folder sorted from the oldest accessed file to the most recently accessed file.']},ignore_index = True)

ls = ls.append({'Command':'ls -lt -c -r','NL Queries':['Show a detailed list of files in the working directory and sort them by time of last modification of file status, oldest first.',
														'List files of the current directory with their details, including the time of last modification of file status. Also, sort them by this time, oldest first.',
														'Show and sort a detailed list of files in the present directory by their time of last modification of file status, oldest first.',
														'Single command to see a detailed list of files of this folder sorted from the oldest modified file to the most recently modified file.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -lt -u Food','NL Queries':['Show a detailed list of files in the Food directory and sort them by time of last access, newest first.',
														'List files of the directory Food with their details, including the time of last access. Also, sort them by this time, newest first.',
														'Show and sort a detailed list of files in the folder Food by their time of last access, newest first.',
														'Single command to see a detailed list of files of the Food folder sorted from the most recently accessed file to the oldest accessed file.']},ignore_index = True)

ls = ls.append({'Command':'ls -lt -c Juices','NL Queries':['Show a detailed list of files in the Juices directory and sort them by time of last modification of file status, newest first.',
													'List files of the directory Juices with their details, including the time of last modification of file status. Also, sort them by this time, newest first.',
													'Show and sort a detailed list of files in the directory Juices by their time of last modification of file status, newest first.',
													'Single command to see a detailed list of files of the folder Juices sorted from the most recently modified file to the oldest modified file.']},ignore_index = True)

ls = ls.append({'Command':'ls -lt -u -r Cakes','NL Queries':['Show a detailed list of files in the Cakes directory and sort them by time of last access, oldest first.',
															'List files of the directory titled Cakes with their details, including the time of last access. Also, sort them by this time, oldest first.',
															'Show and sort a detailed list of files in the directory named Cakes by their time of last access, oldest first.',
															'Single command to see a detailed list of files of the folder Cakes sorted from the oldest accessed file to the most recently accessed file.']},ignore_index = True)

ls = ls.append({'Command':'ls -lt -c -r Cookies','NL Queries':['Show a detailed list of files in the directory named Cookies and sort them by time of last modification of file status, oldest first.',
															'List files of the Cookies directory with their details, including the time of last modification of file status. Also, sort them by this time, oldest first.',
															'Show and sort a detailed list of files in the directory Cookies by their time of last modification of file status, oldest first.',
															'Single command to see a detailed list of files of the Cookies folder sorted from the oldest modified file to the most recently modified file.']},ignore_index = True)

####
ls = ls.append({'Command':'ls -lt -u ..','NL Queries':['Show a detailed list of files in the parent directory and sort them by time of last access, newest first.',
													'List files of the previous directory with their details, including the time of last access. Also, sort them by this time, newest first.',
													'Show and sort a detailed list of files in the preceding directory by their time of last access, newest first.',
													'Single command to see a detailed list of files of the previous folder sorted from the most recently accessed file to the oldest accessed file.']},ignore_index = True)

ls = ls.append({'Command':'ls -lt -c ..','NL Queries':['Show a detailed list of files in the preceding directory and sort them by time of last modification of file status, newest first.',
													'List files of the previous directory with their details, including the time of last modification of file status. Also, sort them by this time, newest first.',
													'Show and sort a detailed list of files in the parent directory by their time of last modification of file status, newest first.',
													'Single command to see a detailed list of files of the parent folder sorted from the most recently modified file to the oldest modified file.']},ignore_index = True)

ls = ls.append({'Command':'ls -lt -u -r ..','NL Queries':['Show a detailed list of files in the preceding directory and sort them by time of last access, oldest first.',
														'List files of the parent directory with their details, including the time of last access. Also, sort them by this time, oldest first.',
														'Show and sort a detailed list of files in the preceding directory by their time of last access, oldest first.',
														'Single command to see a detailed list of files of the previous folder sorted from the oldest accessed file to the most recently accessed file.']},ignore_index = True)

ls = ls.append({'Command':'ls -lt -c -r ..','NL Queries':['Show a detailed list of files in the parent directory and sort them by time of last modification of file status, oldest first.',
														'List files of the parent directory with their details, including the time of last modification of file status. Also, sort them by this time, oldest first.',
														'Show and sort a detailed list of files in the previous directory by their time of last modification of file status, oldest first.',
														'Single command to see a detailed list of files of the preceding folder sorted from the oldest modified file to the most recently modified file.']},ignore_index = True)

print ls.shape
