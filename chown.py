import pandas as pd 

chown = pd.DataFrame(columns = ['Command','NL Queries'])

chown = chown.append({'Command':'chown root tmpfile','NL Queries':['Change ownership of tmpfile to root.',
								'How do I make root owner of tmpfile?',
									'How do I change ownership of file tmpfile to root?']},ignore_index=True)

chown = chown.append({'Command':'chown --from=guest root tmpfile','NL Queries':['Change ownership of tmpfile from guest to root.',
					'How do make root the owner of tmpfile instead of guest?',
						'How do I replace root as owner of tmpfile instead of guest?']},ignore_index=True)

chown = chown.append({'Command':'chown -R mark:sales /path/to/directory','NL Queries':['Changer owner of path/to/directory and it\'s contents from mark to sales.',
						'How do I replace ownership of /path/to/directory from mark to sales? Change ownership of all files and folders inside /path/to/directory to mark.']},ignore_index=True)

chown = chown.append({'Command':'chown -c root file.txt','NL Queries':['Change the ownership of file.txt to root. Display what changes occured.',
					'Show the changes in ownership to the file file.txt after making the change in ownership to root.',
							'How do I know what files\' ownership changed when I try changing ownership of file file.txt to root?']},ignore_index=True)

chown = chown.append({'Command':'chown -c root:myname file.txt','NL Queries':['Change the ownership of file.txt to myname from root. Display if change in ownership occured.',
					'Show the changes in ownership to the file file.txt after making the change in ownership from root to myname.',
						'How do I know what files\' ownership changed to myname from root?']},ignore_index=True)

chown = chown.append({'Command':'chown -f root newfile.txt','NL Queries':['How do I suppress all my error messages when I try changing ownership of the file newfile.txt to root?',
					'Don\'t display the error messages during change of ownership of file myfile.txt',
						'How do I not get any error messages when I try to change ownership of file myfile.txt?',
						'Change ownership of newfile.txt in this folder. Don\'t show error messages.']},ignore_index=True)

chown = chown.append({'Command':'chown -v root file.txt','NL Queries':['Change the ownership of file.txt to root. Display the ownership for each file.',
					'Show the owner of the file file.txt after making the change in ownership to root.',
					'How do I know what files\' owners when I try changing ownership of files.txt to root?',
					'Show verbose explanation when changing ownership of file.txt to root. ']},ignore_index=True)

chown = chown.append({'Command':'chown -v root:myname file.txt','NL Queries':['Change the ownership of file.txt to myname from root. Display the owners for each file.',
					'Show the owners of the file file.txt after making the change in ownership from root to myname.',
						'Change owner of file.txt from root to my name.How do I know the files\' owner after I change ownership of the file from root to myname?']},ignore_index=True)

chown = chown.append({'Command':'chown --version','NL Queries':['How do I find the version of my chown command?',
				'Display the version of the chown command.',
					'Output the chown version and exit.']},ignore_index=True)

chown = chown.append({'Command':'chown --help','NL Queries':['How do I get help related to the chown command?',
				'Display help for chown command along with many options.',
				'Output the flags available with chown command.']},ignore_index=True)

chown = chown.append({'Command':'chown --from= root new1.txt','NL Queries':['How to change the ownership of file new1.txt to root?',
				'How do I change the ownership of the file new1.txt without knowing the current owner?',
					'Change ownership to root without knowing the current owner.',
					'Change ownership of file new1.txt to root. I do not know the current owner.']},ignore_index=True)

#chown = chown.append({'Command':'chown myname:myname myfile.txt','NL Queries':['Change ownership of myfile.txt to myname and group ownership is also changed to myname.',
#				'How do I change both ownership and group ownership of myfile.txt to myname?',
#				'Make myname the owner of myfile.txt. Make myname the group owner of myfile.txt.']},ignore_index=True)

#chown = chown.append({'Command':'chown :mygroup demo.txt','NL Queries':['How do I change only the group ownership of the file demo.txt to myname?',
#				'Change only group ownership of the file demo.txt to demo.txt.',
#				'How do I change the group ownership without changing the ownership of the file demo.txt.']},ignore_index=True)

#chown = chown.append({'Command':'chown root /foo','NL Queries':['How do I change the ownership of /foo to root?',
#					'Change ownership of /foo to root.',
#					'How do I change the ownership of the directory foo under / to root?']},ignore_index=True)

#chown = chown.append({'Command':'chown root:httpd /foo','NL Queries':['Changes ownership to root and group ownership to httpd of /foo',
#					'How do I change ownership of /foo to root and group ownership to httpd?',
#					'How do I change the ownership to root and group ownership of the directory foo under / to foo?']},ignore_index=True)

chown = chown.append({'Command':'chown myself file1.txt file2.txt','NL Queries':['How do I change the ownership of two files file1.txt and file2.txt to myself?',
				'Change ownership of two files file1.txt and file2.txt to myself.',
				'Make myself owner of file.txt and file2.txt present in this folder.']},ignore_index=True)

#chown = chown.append({'Command':'chown myself file1 dir1','NL Queries':['Change the ownership of file1 and directory dir1 to myself.',
#				'How do I change the ownership of file1 and directory dir1 to myself?',
#				'How do I simultaneously change the ownership of a file and directory at the same time?']},ignore_index=True)

chown = chown.append({'Command':'chown bob:group1 file1','NL Queries':['How do I change the ownership of file1 to user with name bob and and change its group to group1?',
				'Change the ownership of file1 to user named bob and group to group1',
				'How do I change both the user ownership to bob and group ownership to group1 of file1?']},ignore_index=True)

chown = chown.append({'Command':'chown rahul: file2','NL Queries':['Change the ownership of file2 to rahul and group to rahul\'s group.',
			'How do I change the ownership of file2 to rahul and group to rahul\'s group.',
					'How do I change group ownership to the same group as the user named rahul?']},ignore_index=True)

chown = chown.append({'Command':'chown --from=root andrew jokes.txt','NL Queries':['Change the ownership of jokes.txt to andrew only if the current owner is root.',
				'How do I change the owner to andrew only if current owner is root.',
					'How do I change ownership only if I am sure the current owner is root?',
					'Change ownership of jokes.txt from root to andrew.']},ignore_index=True)

chown = chown.append({'Command':'chown --from=:group1 :group2 new.txt','NL Queries':['Change the group ownership of new.txt to group2 only if current group owner is group1',
			'How do I change the group ownership to group2 only if current current owner is group1?',
			'How do I change the group ownership of the file new.txt only if the current group ownership is known to be group1?']},ignore_index=True)

#chown = chown.append({'Command':'chown --from=user1 :group1 file.txt','NL Queries':['Change the group ownership of file.txt to group1 only if current owner is user1.',
#				'How do I change the group ownership to group1 only if current user is user1?',
#					'How do I change the group ownership to group1 only when the current user is known to be user1?']},ignore_index=True)

#chown = chown.append({'Command':'chown --from=:group1 user1 file.txt','NL Queries':['Change the ownership to user1 if the group owner is group1.',
#					'How do I change the ownership to user1 if group owner is group1?',
#					'How do I change the ownership of file file.txt only if the group owner is know?']},ignore_index=True)

chown = chown.append({'Command':'chown -h root:friends tmp_link','NL Queries':['How do I change the ownership of the symbolic file tmp_link to user as root and group as friends?',
				'Change the ownership for the symbolic file tmp_link root. MAke root as owner and friends as group owner.',
					'How to only change the ownership of the symbolic file tmp_link to root? How do I make friends as it\'s group user?']},ignore_index=True)

chown = chown.append({'Command':'chown --dereference root:friends tmp_link','NL Queries':['How do I change the ownership of the reference to the symbolic link tmp_link?',
			'Change the ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to root. Make friends as group owners.',]},ignore_index=True)

chown = chown.append({'Command':'chown --reference=oldfile newfile','NL Queries':['How do I copy the ownership details from oldfile to newfile?',
			'Copy the owner/group settings from oldfile to newfile.',
			'How do I get the same ownership details for newfile similar to the oldfile?']},ignore_index=True)

chown = chown.append({'Command':'chown -R -H guest:family linux_symlnk','NL Queries':['How do I forcefully change the owner/group to guest/family of a symbolic link linux_symlnk recursively?',
				'Change the ownership of a symbolic link linux_symlnk recursively. Make guest the owner and family the group owner.',
				'How do I change the ownership to guest for all the files and folders referenced in the symbolic link linux_symlnk. Make family the group owner.?']},ignore_index=True)

chown = chown.append({'Command':'chown -v -R guest linux','NL Queries':['How do I list all the ownership details when I recursively change the ownership of folder linux?',
				'List the ownership details when I recursively change the ownership for the folder linux.',
				'Change the ownership of the directory linux and all its files and folders. List the ownership for all the files and folders.']},ignore_index=True)

#chown = chown.append({'Command':'chown jim /path/to/file1 /path/to/file2 /path/to/file3','NL Queries':['How do I change the owner of file2 and file3 in the directory /path/to? to jim?',
#				'Change the ownership of file2 and file3 in a given path.',
#				'How do I change the ownerhsip of multiples files to jim?']},ignore_index=True)
#chown = chown.append({'Command':'chown 625:874 file1','NL Queries':['How do I change ownership if I know the user ID 625 and group ID 874?','Changes the owner to UID 625 and GID 874.','Can I change the ownership of a file to a particular user ID 625 group ID 874?']},ignore_index=True)
#chown = chown.append({'Command':'chown root *','NL Queries':['How do I change the ownership details for all files in the current directory to root?','Changes the ownership for the files present in the current directory to root.']},ignore_index=True)


print chown.shape
