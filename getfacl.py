import pandas as pd 

getfacl = pd.DataFrame(columns = ['Command','NL Queries'])

getfacl = getfacl.append({'Command':'getfacl instructions.txt.','NL Queries':['Display file name,owner, group, access control list of instructions.txt.',
															'Show all information about the file instuctions.txt present in this folder.',
															'Display the filename, permissions, acl of the file instructions.txt.',
															'Display all ownership related information about the file instructions.txt present in the current directory.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -a instructions.txt','NL Queries':['Display access control list for file instructions.txt.',
																	 'How do I see the access control list of instructions.txt?',
																	 'Show the permissions,named user,named group,effective rights mask of the file instructions.txt.',
																	 'What are the base Acl entries,named user and group entries and rights mask of instructions.txt ?']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -n instructions.txt','NL Queries':['Display file name, owner, group, access control list of instructions.txt. Show numeric owner and group IDs.',
										'Show all information of file instructions.txt with numeric IDs.',
										'Display the filename, permissions, acl of the file instructions.txt with numeric user and group IsDs',
										'Display all ownership related information, with numeric user and group IDs, about the file instructions.txt present in the current directory.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -d newdir','NL Queries':['Display the default access control list for the directory newdir.', 
													'How do I see the default access control list of newdir ?',
													'Show the default acl of newdir.',
													'What are the default owner, group names for the directory newdir ?']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -c instructions.txt','NL Queries':['Display file name,owner, group, access control list of instructions.txt without the header.',
													'Show all information about the file instuctions.txt present in this folder. Don\'t display the comment header.',
													'Display the filename, permissions, acl of the file instructions.txt without the file name,owner name, group name.',
													'Display all ownership related information about the file instructions.txt present in the current directory.Don\'t print the header comments.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -e ~/sample','NL Queries':['Display file name, owner, group, access control list of ~/sample along with all the effective permissions.',
								'Show all information about the directory ~/sample with comments for effective rights.',
								'Display the filename, permissions, acl of ~/sample along with the comments about effective permissions.',
								'Display all ownership related information about the file ~/sample present in the home directory. Also display the comments about the effective rights.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -E ../sample/files','NL Queries':['Display file name, owner, group, access control list of ../sample/files without the effective permissions.',
				'Show all information about the directory ../sample/files without the comments for effective rights.',
				'Display the filename, permissions, acl of ../sample/files .Don\'t display the comments about effective permissions.',
				'Display all ownership related information about the file named files present in the sample folder in the previous directory.Do not display the comments about the effective rights.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -s smallfile.txt','NL Queries':['Display file name,owner, group, access control list of smallfile.txt if it has other than the base ACL entries.',
											'If the file => smallfile.txt has only base ACL entries, show all information about the it.',
											'Display the filename, permissions, acl of smallfile.txt, if it has other than the base ACL entries.',
											'Skip showing the details about the file = smallfile.txt if it has only the base ACL entries.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -R somedir','NL Queries':['Display file name,owner, group, access control list of directory, somedir recursively including somedir.',
						'Show all information about the file and folders inside somedir, including somedir itself.',
						'Display the filename, permissions, acl of the all files and folders recursively for the folder somedir.',
						'Display all ownership related information about the folder somedir.Recursively display the information about all the subfiles and folders.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -t instructions.txt.','NL Queries':['Display file name,owner, group, access control list of instructions.txt.Show it in a tabular format.',
					'Show all information about the file instuctions.txt in a tabular format.The file is present in this folder.',
					'Display the filename, permissions, acl of the file instructions.txt. Instead of a list, use a tabular format.',
					'Display all ownership related information about the file instructions.txt present in the current directory in a table.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -v','NL Queries':['Show the version of getfacl',
									'What is the version of getfacl?',
									'Display the version of getfacl and return to the command line prompt',
									'Print the version in the command line of getfacl and exit.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -h','NL Queries':['Show help for getfacl.',
					'What are the various flags available with getfacl command?',
					'Display all the flags available for getfacl and their uses',
					'Print help for getfacl, explaining the options.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -.','NL Queries':['Display file name,owner, group, access control list of files when their names are input via the std input.',
					'Show all information about every file whose path is given in the command line as input.',
					'Names of files will be given as input. Display the filename, permissions, acl of each file.',
					'Display all ownership related information about each file, whose path is input in the command line.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -- -queries.','NL Queries':['Display file name,owner, group, access control list of -queries, whose name starts with a - character.',
					'Show all information about the file -queries present in this folder.',
					'Display the filename, permissions, acl of the file -queries, having a "-" in the start of the name.',
					'Display all ownership related information about the file "-queries" present in the current directory.Dont let the - be considered as a flag.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl problems solutions.','NL Queries':['Display file name,owner, group, access control list of the files problems, solutions .',
						'Show all information about files problems, solutions present in this folder.',
						'Display the filename, permissions, acl of the files problems , solutions.',
						'Display all ownership related information about files => problems, solutions.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -ac news.txt','NL Queries':['Display access control list for file news.txt, omitting the headers.', 
						'How do I see the access control list of news.txt, without the comment headers?',
						'Show the permissions,named user,named group,effective rights mask of the file news.txt. Don\'t show the headers about filename, user name and group name .',
						'What are the base Acl entries,named user and group entries and rights mask of news.txt ?.Don\'t display the first 3 lines of the output?']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -an dir1','NL Queries':['Display access control list for the directory dir1 .Show numeric user and group IDs', 
						'How do I see the access control list of dir1 with numeric user and group IDs?',
						'Show the permissions,named user,named group,effective rights mask,numeric user and group IDs of the directory dir1.',
						'What are the base Acl entries,named user and group entries and rights mask of dir1.txt ? Include numbered user and group IDs.']},ignore_index=True)


getfacl = getfacl.append({'Command':'getfacl -ad instructions.txt.','NL Queries':['Display file name,owner, group, access control list,default acl, of instructions.txt.',
						'Show all information about the file instuctions.txt present in this folder along with the default access control list.',
						'Display the filename, permissions, acl , default acl of the file instructions.txt.',
						'Display all ownership related information about the file instructions.txt present in the current directory.Also include the default acl.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -ae instructions.txt.','NL Queries':['Display file name,owner, group, access control list of instructions.txt along with the effective rights comments.',
					'Show all information about the file instuctions.txt present in this folder.Also include comments about the effective rights',
					'Display the filename, permissions, acl of the file instructions.txt with comments on the effective rights.',
					'Display all ownership related information about the file instructions.txt present in the current directory. Include comments about effective rights,even though they are identical to the rights in the ACL entry.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -aE instructions.txt.','NL Queries':['Display file name,owner, group, access control list of instructions.txt without effective rights comments.',
				'Show all information about the file instuctions.txt present in this folder.No need to display effective rights comments.',
				'Display the filename, permissions, acl of the file instructions.txt. Effective rights shouldn\'t be displayed',
				'Display all ownership related information about the file instructions.txt present in the current directory without effective rights permissions.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -as a.txt b.txt','NL Queries':['Display access control list for files a.txt and b.txt only if the file has other than base entries.',
						 'How do I see the access control list of a.txt and b.txt? Show the details for each file if it has other than the base acl entries?']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -aR dir3','NL Queries':['Display access control list for directory dir3 recursively.', 
						'How do I see the access control list of all files and folders in dir3 directory rec?',
						'Show the permissions,named user,named group,effective rights mask of the file and folders inside dir3 directory recursively.',
						'What are the base Acl entries,named user and group entries and rights mask of dir3?']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -at instructions.txt','NL Queries':['Display access control list for file instructions.txt in a tabular form.',
							 'How do I see the access control list of instructions.txt in a table?',
							 'Show the permissions,named user,named group,effective rights mask of the file instructions.txt. Give the output in a table.',
							 'What are the base Acl entries,named user and group entries and rights mask of instructions.txt in a table with acl and default acl columns?']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -nd instructions.txt','NL Queries':['Display file name, owner, group, default access control list of instructions.txt. Show numeric owner and group IDs.',
					'Show all information of file instructions.txt with numeric IDs.',
					'Display the filename, permissions, acl of the file instructions.txt with numeric user and group IDs',
					'Display all ownership related information, with numeric user and group IDs, about the file instructions.txt present in the current directory.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -nc processes.txt','NL Queries':['Display file name, owner, group, access control list of processes.txt. Show numeric owner and group IDs but do not show the headers.',
						'Show all information of file processes.txt with numeric IDs. Don\'t show the headers',
						'Display the filename, permissions, acl of the file processes.txt with numeric user and group IDs but exclude the comments regarding file name, user name, group name.',
						'Display all ownership related information, with numeric user and group IDs, about the file processes.txt present in the current directory.No need of displaying the comments in the top 3 lines.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -ne pictures','NL Queries':['Display file name, owner, group, access control list of pictures. Show numeric owner and group IDs  and the effective rights column.',
					'Show all information of pictures with numeric IDs and effective rights comments.',
					'Display the filename, permissions, acl of pictures with numeric user and group IDs and effective rights.',
					'Display all ownership related information, with numeric user and group IDs, about the file pictures present in the current directory. Also display a column on the effective rights of users and groups, default and otherwise.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -nE pictures','NL Queries':['Display file name, owner, group, access control list of pictures. Show numeric owner and group IDs but not the effective rights column.',
					'Show all information of pictures with numeric IDs. Exclude the effective rights comments.',
					'Display the filename, permissions, acl of pictures with numeric user and group IDs. Don\'t display the effective rights of user and group.',
					'Display all ownership related information, with numeric user and group IDs, about the file pictures present in the current directory. Don\'t display a column on the effective rights.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -nR myfolder','NL Queries':['Display file name, owner, group, access control list of all files and folders in myfolder, recursively. Show numeric owner and group IDs.',
					'Show all information of all files and folders in myfolders with numeric IDs.Do it recursively',
					'Display the filename, permissions, acl of the folder => myfolder with numeric user and group IDs recursively.',
					'Display all ownership related information, with numeric user and group iDs, about the folder myfolder recursively.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -ns instructions.txt','NL Queries':['Display file name, owner, group, access control list of instructions.txt. Show numeric owner and group IDs; ACL , default ACL in a table.',
					'Show all information of file instructions.txt with numeric IDs in a table.',
					'Display the filename, permissions, acl of the file instructions.txt with numeric user and group IDs, in a table',
					'Display all ownership related information, with numeric user and group IDs, about the file instructions.txt present in the current directory. Give the output in a table.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -dc newdir','NL Queries':['Display the default access control list for the directory newdir without the header comments.',
				 'How do I see the default access control list of newdir,without header comments ?',
				 'Show the default acl of newdir.Don\'t print the header comments ']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -de newdir','NL Queries':['Display the default access control list , with the default effective rights,for the directory newdir.',
				 'How do I see the default access control list of newdir along with the effective rights comments?',
				 'Show the default acl of newdir along with the effective rights.',
				 'What are the default owner, group names and default effective rights for the directory newdir ?']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -dE newdir','NL Queries':['Display the default access control list , without the default effective rights,for the directory newdir.', 
				'How do I see the default access control list of newdir along without the effective rights comments?',
				'Show the default acl of newdir without the effective rights.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -dR newdir','NL Queries':['Display the default access control lists for all files and folders in the directory newdir recursively.',
			 'How do I see the default access control list of all files and folders in newdir recursively?',
			 'Show the default acl of all files and folders in newdir, including newdir itself.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -dt ../newdir','NL Queries':['Display the default access control list for the directory ../newdir in a table.', 
			'How do I see the default access control list of ../newdir in a table?',
			'Show the default acl of newdir present in the parent folder. Show in a table.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -ce news.txt','NL Queries':['Display file name,owner, group, access control list, effective rights comments of news.txt without the header.',
				'Show all information about the file news.txt present in this folder. Don\'t display the comment header but display the effective rights comments.',
				'Display the filename, permissions, acl, effective rights comments  of the file => news.txt without the file name,owner name, group name.',
				'Display all ownership related information about the file news.txt present in the current directory. Print the comments about the effective user and group rights. Don\'t print the header comments.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -cE news.txt','NL Queries':['Display file name,owner, group, access control list of news.txt without the header and effective rights comments.',
			'Show all information about the file news.txt present in this folder. Don\'t display the comment header and the effective rights comments.',
			'Display the filename, permissions, acl of the file => news.txt without the file name,owner name, group name and effective rights of user and group.',
			'Display all ownership related information about the file news.txt present in the current directory. Don\'t print the comments about the effective user and group rights and the header comments.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -cR myfolder','NL Queries':['Display file name,owner, group, access control list of all files and folders, recursively, in myfolder without the header.',
		'Show all information about the files and folders in myfolder, recursively. Don\'t display the comment header',
		'Display the filename, permissions, acl of all files and folders in myfolder, without the file name,owner name, group name.',
		'Display all ownership related information about all the files and folders in myfolder. Don\'t print the header comments.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -eR ~/sample','NL Queries':['Display file name, owner, group, access control list of all files and folders in ~/sample along with all the effective permissions, recursively.',
	'Show all information about all the files and folders in the directory ~/sample with comments for effective rights, recursively.',
	'Display the filename, permissions, acl of all files and folders in ~/sample along with the comments about effective permissions, in a recursive way.',
	'Display all ownership related information about all files and folders in sample,present in the home directory, recursively. Also display the comments about the effective rights.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -ER ../sample/files','NL Queries':['Display file name, owner, group, access control list of all files and folders in ../sample/files recursively,without the effective permissions.',
		'Show all information about all the files and folders in the directory ../sample/files without the comments for effective rights.',
		'Display the filename, permissions, acl of all files and folders in ../sample/files recursively.Don\'t display the comments about effective permissions.',
		'Display all ownership related information about all the files and folders in  ../sample/files, in a recursive fashion. Do not display the comments about the effective rights.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -Et ../sample/files','NL Queries':['Display file name, owner, group, access control list of ../sample/files without the effective permissions in a tabular format.',
		'Show all information about the directory ../sample/files without the comments for effective rights in a table.',
		'Display the filename, permissions, acl of ../sample/files . Don\'t display the comments about effective permissions.',
		'Display all ownership related information about the file ../sample/files. Do not display the comments about the effective rights.']},ignore_index=True)

getfacl = getfacl.append({'Command':'getfacl -sR myfile','NL Queries':['Display file name,owner, group, access control list of all files and folders in myfile, recursively, if it has other than the base ACL entries.',
			'If files and folders in myfile has not only the base ACL entries, show all information about it.',
			'Display the filename, permissions, acl of all files and folders in myfile directory, recursively, if it has other than the base ACL entries.',
			'Skip showing the details about any file or folder in myfile if it has only the base ACL entries. Else recursively show the details for all files.']},ignore_index=True)

#getfacl.to_csv('/home/ananyaraval/Documents/Thesis/Data/UNIX/csv_files/getfacl.csv',index=False)
print getfacl.shape

#getfacl = getfacl.append({'Command':'getfacl','NL Queries':['','','','']},ignore_index=True)

