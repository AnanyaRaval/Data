import pandas as pd 

chown = pd.DataFrame(columns = ['Command','NL Queries'])

chown = chown.append({'Command':'chown root tmpfile','NL Queries':['Change ownership of tmpfile to root.',
						'How do I make root owner of tmpfile?',
						'How do I change ownership of file tmpfile to root?']},ignore_index=True)

chown = chown.append({'Command':'chown --from=guest root tmpfile','NL Queries':['Change ownership of tmpfile from guest to root.',
							'How do make root the owner of tmpfile instead of root?',
								'How do I replace root as owner of tmpfile instead of guest?']},ignore_index=True)

chown = chown.append({'Command':'chown -R mark:sales /path/to/directory','NL Queries':['Changer owner of path/to/directory and it\'s contents from mark to sales.',
							'How do I replace ownership of /path/to/directory from mark to sales? Change ownership of all files and folders inside /path/to/directory to mark.',
								'How do I make replace the owner of directory folder from mark to sales? The full path of the folder is /path/to/directory.']},ignore_index=True)

chown = chown.append({'Command':'chown -c root file.txt','NL Queries':['Change the ownership of file.txt to root. Display what changes occured.',
								'Show the changes in ownership to the file file.txt after making the change in ownership to root.',
									'How do I know what files\' ownership changed when I try changing ownership of files to root?',
									'Make root owner of file.txt. Display the changes occuring.']},ignore_index=True)

chown = chown.append({'Command':'chown -c root:myname file.txt','NL Queries':['Change the ownership of file.txt to myname from root. Display if change in ownership occured.',
								'Show the changes in ownership of the file file.txt after making the change in ownership from root to myname.',
								'How do I know what files\' ownership of file.txt from root to myname?',
								'Replace the owner root of file.txt with myname. Show any changes which occured on command line.']},ignore_index=True)

chown = chown.append({'Command':'chown -f root newfile.txt','NL Queries':['How do I suppress all my error messages when I try changing ownership of the file newfile.txt to root?',
								'Don\'t display the error messages during change of ownershipof newfile.txt to root.',
								'How do I not get any error messages when I try to change ownership of file myfile.txt to root?',
									'Change owner of newfile.txt present in the current folder to root. Do not display error messages.',
									'Suppress warning or errors. Change ownership of newfile.txt to root.']},ignore_index=True)

chown = chown.append({'Command':'chown -v root file.txt','NL Queries':['Change the ownership of file.txt to root. Display the ownership for the file.',
								'Show the owner of the file file.txt after making the change in ownership to root.',
								'How do I know what files\' owners when I try changing ownership of file.txt to root?',
									'Change ownership of file.txt present in this folder to root. Display permission information of file.txt.']},ignore_index=True)

chown = chown.append({'Command':'chown -v root:myname file.txt','NL Queries':['Change the ownership of file.txt to myname from root. Display the owners for each file.','Show the owners of the file file.txt after making the change in ownership from root to myname.','How do I know the files\' owner after I change ownership of the file from root to myname?']},ignore_index=True)

chown = chown.append({'Command':'chown --version','NL Queries':['How do I find the version of my chown command?','Displays the version of the chown command.','Outputs the chown version and exit.']},ignore_index=True)

chown = chown.append({'Command':'chown --help','NL Queries':['How do I get help related to the chown command?','Displays help for chown command along with many options.','Outputs the flags available with chown command.']},ignore_index=True)

chown = chown.append({'Command':'chown --from= root new1.txt','NL Queries':['How to change the ownership of a file to root?','How do I change the ownership of a file without knowing the current owner?','Changes ownership to root without knowing the current owner.']},ignore_index=True)

chown = chown.append({'Command':'chown myname:myname myfile.txt','NL Queries':['Ownership is changed to myname and group ownership is also changed to myname.','How do I change both ownership and group ownership to myname?']},ignore_index=True)

chown = chown.append({'Command':'chown :mygroup demo.txt','NL Queries':['How do I change only the group ownership of the file demo.txt to myname?','Changes only group ownership of the file.','How do I change the group ownership without changing the ownership of the file demo.txt']},ignore_index=True)

chown = chown.append({'Command':'chown root /foo','NL Queries':['How do I change the ownership of /foo to root?','Changes ownership of /foo to root.','How do I change the ownership of the directory foo under /?']},ignore_index=True)

chown = chown.append({'Command':'chown root:httpd /foo','NL Queries':['Changes ownership to root and group ownership to httpd of /foo','How do I change ownership of /foo to root and group ownership to httpd?','How do I change the ownership to root and group ownership of the directory foo under / to foo?']},ignore_index=True)

chown = chown.append({'Command':'chown myself file1.txt file2.txt','NL Queries':['How do I change the ownership of two files file1.txt and file2.txt to myself?','Changes ownership of two files.','How do I change the ownership of two files to myself?']},ignore_index=True)

chown = chown.append({'Command':'chown myself file1 dir1','NL Queries':['Change the ownership of file1 and directory dir1 to myself.','How do I change the ownership of file1 and directory dir1 to myself?','How do I simultaneously change the ownership of a file and directory at the same time?']},ignore_index=True)

chown = chown.append({'Command':'chown bob:group1 file1','NL Queries':['How do I change the ownership of file to user with name bob and and change its group to group1?','Changes the ownership of file to user named bob and group to group1','How do I change both the user ownership and group ownership of the file?']},ignore_index=True)

chown = chown.append({'Command':'chown rahul: file2','NL Queries':['Change the ownership of file2 to rahul and group to rahul\'s group.','How do I change the ownership of file2 to rahul and group to rahul\'s group.','How do I change group ownership to the same group as the user?']},ignore_index=True)


print chown.size
