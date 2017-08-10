import pandas as pd 

chown = pd.DataFrame(columns = ['Command','NL Queries'])

chown = chown.append({'Command':'chown root tmpfile','NL Queries':['Change ownership of tmpfile to root.',
								'How do I make root owner of tmpfile?',
									'How do I change ownership of file tmpfile to root?']},ignore_index=True)

chown = chown.append({'Command':'chown --from=guest root tmpfile','NL Queries':['Change ownership of tmpfile from guest to root.',
													'How do make root the owner of tmpfile instead of guest?',
													'How do I replace the owner of tmpfile from guest to root?',
													'The owner of tmpfile is guest. Change it to root.']},ignore_index=True)

chown = chown.append({'Command':'chown -c --from=guest root tmpfile','NL Queries':['Change ownership of tmpfile from guest to root.Display any changes which occured.',
																					'How do make root the owner of tmpfile instead of guest and see the changes in ownership which occured?',
																					'How do I replace the owner of tmpfile from guest to root?How do I see the change in ownership',
																					'The owner of tmpfile is guest. Change it to root and show the change,if any.']},ignore_index=True)

chown = chown.append({'Command':'chown -f --from=guest root tmpfile','NL Queries':['Change ownership of tmpfile from guest to root. Suppress any warnings or error messages.',
																					'How do make root the owner of tmpfile instead of guest and not see any errors during the process?',
																					'How do I replace the owner of tmpfile from guest to root without any error messages displayed?',
																					'The owner of tmpfile is guest. Change it to root. Don\'t show any error messages.']},ignore_index=True)

chown = chown.append({'Command':'chown -v --from=guest root tmpfile','NL Queries':['Change ownership of tmpfile from guest to root. Suppress any warnings or error messages.',
																					'How do make root the owner of tmpfile instead of guest and not see any errors during the process?',
																					'How do I replace the owner of tmpfile from guest to root without any error messages displayed?',
																					'The owner of tmpfile is guest. Change it to root. Don\'t show any error messages.']},ignore_index=True)

chown = chown.append({'Command':'chown --from= root new1.txt','NL Queries':['How to change the ownership of file new1.txt to root?',
																			'How do I change the ownership of the file new1.txt to root without knowing the current owner?',
																			'Change ownership of new1.txt to root without knowing the current owner.',
																			'Change ownership of file new1.txt to root. I do not know the current owner.']},ignore_index=True)

chown = chown.append({'Command':'chown -c --from= root new1.txt','NL Queries':['How to change the ownership of file new1.txt to root without knowing the current owner? Show the changes made, if any.',
																				'How do I change the ownership of the file new1.txt to root without knowing the current owner and see the changes made?',
																				'Change ownership of new1.txt to root without knowing the current owner. See the changes occurred.',
																				'Change ownership of file new1.txt to root and show the change of ownership which occured. I do not know the current owner.']},ignore_index=True)

chown = chown.append({'Command':'chown -f --from= root new1.txt','NL Queries':['How to change the ownership of file new1.txt to root without any error messages or warnings?',
																				'How do I change the ownership of the file new1.txt to root without knowing the current owner and without any error messages?',
																				'Change ownership of new1.txt to root without knowing the current owner. Don\'t display any error messages.',
																				'Change ownership of file new1.txt to root withoout any display or warnings or error messages. I do not know the current owner.']},ignore_index=True)

chown = chown.append({'Command':'chown -v --from= root new1.txt','NL Queries':['How to change the ownership of file new1.txt to root? Display the ownership details for each file.',
																			'How do I change the ownership of the file new1.txt to root without knowing the current owner and see the owners after the operation? ',
																			'Change ownership of new1.txt to root without knowing the current owner. Show the ownership of new1.txt.',
																			'Change ownership of file new1.txt to root. I do not know the current owner. Show verbose explanation of the owner.']},ignore_index=True)

#chown = chown.append({'Command':'chown -R mark:sales /path/to/directory','NL Queries':['Changer owner of path/to/directory and it\'s contents from mark to sales.',
#						'How do I replace ownership of /path/to/directory from mark to sales? Change ownership of all files and folders inside /path/to/directory to mark.']},ignore_index=True)

chown = chown.append({'Command':'chown -c root file.txt','NL Queries':['Change the ownership of file.txt to root. Display what changes occured.',
																		'Show the changes in ownership to the file file.txt after making the change in ownership to root.',	
																		'How do I know what files\' ownership changed when I try changing ownership of file file.txt to root?',
																		'Make root the owner of file.txt. Show the changes occured.']},ignore_index=True)

chown = chown.append({'Command':'chown -f root newfile.txt','NL Queries':['How do I suppress all my error messages when I change ownership of the file newfile.txt to root?',
																			'Don\'t display the error messages during change of ownership of file newfile.txt',
																			'How do I change ownership of file newfile.txt to root wthout any error messages displayed?',
																			'Change ownership of newfile.txt in this folder. Don\'t show error messages.']},ignore_index=True)

chown = chown.append({'Command':'chown -v root file.txt','NL Queries':['Change the ownership of file.txt to root. Display the ownership for file.txt.',
																		'Show the ownership information of the file file.txt after making the change in ownership to root.',
																		'How do I know who are the owners of file.txt when I try changing ownership of file.txt to root?',
																		'Show verbose explanation when changing ownership of file.txt to root.']},ignore_index=True)

###
chown = chown.append({'Command':'chown :mygroup demo.txt','NL Queries':['How do I change only the group ownership of the file demo.txt to mygroup?',
																		'Change only group ownership of the file demo.txt to mygroup.',
																		'How do I change the group ownership to mygroup without changing the user ownership of the file demo.txt.']},ignore_index=True)

chown = chown.append({'Command':'chown -c :mygroup demo.txt','NL Queries':['How do I change only the group ownership of the file demo.txt to mygroup and see the changes which occured?',
																			'Change only group ownership of the file demo.txt to mygroup. Display the changes which occured.',
																			'How do I change the group ownership to mygroup without changing the user ownership of the file demo.txt and see the changes occured.',
																			'Make mygroup the group owner of demo.txt. Show the changes occured.']},ignore_index=True)

chown = chown.append({'Command':'chown -v :mygroup file.txt','NL Queries':['Change the group ownership of file.txt to mygroup. Display the ownership of file.txt.',
																			'Show the ownership of file file.txt after making the change in group ownership to mygroup.',
																			'How do I know who are the files\' owners when I try changing group ownership of file.txt to mygroup?',
																			'Show verbose explanation when changing group ownership of file.txt to mygroup.']},ignore_index=True)

chown = chown.append({'Command':'chown -f :mygroup demo.txt','NL Queries':['How do I change only the group ownership of the file demo.txt to mygroup with any error/warning messages?',
																			'Change only group ownership of the file demo.txt to mygroup. Don\'t show any error messages.',
																			'How do I change the group ownership to mygroup without changing the user ownership of the file demo.txt and without any error messages displayed.']},ignore_index=True)

chown = chown.append({'Command':'chown bob:group1 file1','NL Queries':['How do I change the ownership of file1 to user with name bob and and change its group to group1?',
																		'Change the ownership of file1 to user named bob and group to group1',
																		'How do I change both the user ownership to bob and group ownership to group1 of file1?']},ignore_index=True)

chown = chown.append({'Command':'chown -v myuser:mygroup myfile','NL Queries':['Change the user ownership to myuser and group ownership to mygroup for the file myfile. Display the ownership details of myfile.',
																				'Show the ownership of file myfile after making the change in user ownership/group ownership to myuser/mygroup.',
																				'How do I know who are the files\' owners when I try changing user ownership to myuser and group ownership to mygroup in myfile?',
																				'Show verbose explanation when changing the user ownership to myuser and group ownership to mygroup in myfile.']},ignore_index=True)


chown = chown.append({'Command':'chown -c myuser:mygroup myfile','NL Queries':['Change the user ownership to myuser and group ownership to mygroup for the file myfile. Display the ownership changes of myfile.',
																				'Show the change, if any, in ownership of file myfile after making the change in user ownership/group ownership to myuser/mygroup.',
																				'How do I see the changes when I try changing user ownership to myuser and group ownership to mygroup in myfile?',
																				'Show any ownership changes when changing the user ownership to myuser and group ownership to mygroup in myfile.']},ignore_index=True)


chown = chown.append({'Command':'chown -f myuser:mygroup myfile','NL Queries':['Change the user ownership to myuser and group ownership to mygroup for the file myfile. Don\'t display the ownership details of myfile.',
																				'Make the change  of myfile in user ownership/group ownership to myuser/mygroup and suppress any warnings/errors.',
																				'Change user ownership to myuser and group ownership to mygroup in myfile without any warnings.',
																				'Without any explanation, change the user ownership to myuser and group ownership to mygroup of myfile.']},ignore_index=True)

chown = chown.append({'Command':'chown myself file1.txt file2.txt','NL Queries':['How do I change the ownership of two files file1.txt and file2.txt to myself?',
																					'Change ownership of two files file1.txt and file2.txt to myself.',
																				'Make myself as the owner of file.txt and file2.txt present in this folder.']},ignore_index=True)

chown = chown.append({'Command':'chown -c myself file1.txt file2.txt','NL Queries':['How do I change the ownership of two files file1.txt and file2.txt to myself and display any changes which occured?',
																					'Change ownership of two files file1.txt and file2.txt to myself and show any ownership changes.',
																					'Make myself as the owner of file.txt and file2.txt present in this folder. Show changes of ownership.']},ignore_index=True)

chown = chown.append({'Command':'chown -v myself file1.txt file2.txt','NL Queries':['How do I change the ownership of two files file1.txt and file2.txt to myself and see the ownership information after the operation?',
																					'Change ownership of two files file1.txt and file2.txt to myself.Show the ownership information of file1.txt and file2.txt',
																					'Show verbose explanation after making myself as the owner of file.txt and file2.txt present in this folder.']},ignore_index=True)

chown = chown.append({'Command':'chown -f myself file1.txt file2.txt','NL Queries':['How do I change the ownership of two files file1.txt and file2.txt to myself? Suppress any warnings/errors which occured.',
																					'Change ownership of two files file1.txt and file2.txt to myself.Don\'t show any warning messages.',
																					'Make myself as the owner of file1.txt and file2.txt present in this folder without any error messages.']},ignore_index=True)

#chown = chown.append({'Command':'chown -v root:myname file.txt','NL Queries':['Change the user ownership of file.txt to root and group ownership to root. Display the owners of file.txt.',
#																				'Show the owners of the file file.txt after changing user ownership to root and group ownership to myname.',
#																				'Change user owner of file.txt to root and group owner to myname. How do I know the file\'s owner after I change ownership details?']},ignore_index=True)

#chown = chown.append({'Command':'chown myname:myname myfile.txt','NL Queries':['Change ownership of myfile.txt to myname and group ownership is also changed to myname.',
#				'How do I change both ownership and group ownership of myfile.txt to myname?',
#				'Make myname the owner of myfile.txt. Make myname the group owner of myfile.txt.']},ignore_index=True)


#chown = chown.append({'Command':'chown root /foo','NL Queries':['How do I change the ownership of /foo to root?',
#					'Change ownership of /foo to root.',
#					'How do I change the ownership of the directory foo under / to root?']},ignore_index=True)

#chown = chown.append({'Command':'chown root:httpd /foo','NL Queries':['Changes ownership to root and group ownership to httpd of /foo',
#					'How do I change ownership of /foo to root and group ownership to httpd?',
#					'How do I change the ownership to root and group ownership of the directory foo under / to foo?']},ignore_index=True)

chown = chown.append({'Command':'chown rahul: file2','NL Queries':['Change the ownership of file2 to rahul and group to rahul\'s group.',
																	'How do I change the ownership of file2 to rahul and group to rahul\'s group.',
																	'How do I change group ownership to the same group as the user named rahul?']},ignore_index=True)

chown = chown.append({'Command':'chown -c rahul: file2','NL Queries':['Change the ownership of file2 to rahul and group to rahul\'s group. Display the changes occured.',
																'How do I change the ownership of file2 to rahul and group to rahul\'s group and see the changes which occured?',
																'How do I change user ownership to rahul and group ownership to the same group as the user rahul? How do I see the change of ownership of file2?' ]},ignore_index=True)

chown = chown.append({'Command':'chown -v rahul: file2','NL Queries':['Change the ownership of file2 to rahul and group to rahul\'s group and see the ownership details of file2.',
																		'How do I change the ownership of file2 to rahul and group to rahul\'s group? How do I see the ownership details after the operation?',
																		'How do I see a verbose explanation of change in user ownership to rahul and group ownership to the same group as the user named rahul?']},ignore_index=True)

chown = chown.append({'Command':'chown -f rahul: file2','NL Queries':['Change the ownership of file2 to rahul and group to rahul\'s group. Don\'t show any error messages.',
																		'How do I change the ownership of file2 to rahul and group to rahul\'s group without any errors or warnings.',
																		'How do I change user ownership to rahul and group ownership to the same group as the user named rahul without any warnings?']},ignore_index=True)
###
chown = chown.append({'Command':'chown --from=:group1 :group2 new.txt','NL Queries':['Change the group ownership of new.txt to group2 only if current group owner is group1',
																						'How do I change the group ownership of new.txt to group2 only if current current owner is group1?',
																						'If the current group ownership is known to be group1, change the group ownership of the file new.txt to group2?']},ignore_index=True)

chown = chown.append({'Command':'chown -c --from=:group1 :group2 new.txt','NL Queries':['Change the group ownership of new.txt to group2 only if current group owner is group1 and display the changes occured.',
																						'How do I change the group ownership of new.txt to group2 only if current current owner is group1 and see the changes after the operation?',
																						'If the current group ownership is known to be group1, change the group ownership of the file new.txt to group2. Show the changes in ownership which occured.']},ignore_index=True)

chown = chown.append({'Command':'chown -v --from=:group1 :group2 new.txt','NL Queries':['Change the group ownership of new.txt to group2 only if current group owner is group1. Show ownership details of new.txt.',
																						'How do I change the group ownership of new.txt to group2 only if current current owner is group1 and see the ownership details of new.txt?',
																						'If the current group ownership is known to be group1, change the group ownership of the file new.txt to group2. Show verbose explanation of ownership of new.txt.']},ignore_index=True)

chown = chown.append({'Command':'chown -f --from=:group1 :group2 new.txt','NL Queries':['Change the group ownership of new.txt to group2 only if current group owner is group1. Don\'t show any warnings/error messages.',
																						'How do I change the group ownership of new.txt to group2 without any error messages and only if current current owner is group1?',
																						'If the current group ownership is known to be group1, change the group ownership of the file new.txt to group2 and skip the error display.']},ignore_index=True)
###
chown = chown.append({'Command':'chown --from=user1 :group1 file.txt','NL Queries':['Change the group ownership of file.txt to group1 only if current owner is user1.',
																					'How do I change the group ownership of file.txt to group1 only if current user is user1?',
																					'If the current user is known to be user1, change the group ownership of file.txt to group1 only.']},ignore_index=True)

chown = chown.append({'Command':'chown -c --from=user1 :group1 file.txt','NL Queries':['Change the group ownership of file.txt to group1 only if current owner is user1. Show the changes in ownership.',
																						'How do I change the group ownership of file.txt to group1 only if current user is user1 and see the changes applied?',
																						'If the current user is known to be user1, change the group ownership of file.txt to group1 only. Display the changes.']},ignore_index=True)

chown = chown.append({'Command':'chown -v --from=user1 :group1 file.txt','NL Queries':['Change the group ownership of file.txt to group1 only if current owner is user1. Show verbose explanation of the changes.',
																					'How do I change the group ownership of file.txt to group1 only if current user is user1? How do I see the ownersip details after the operation?',
																					'If the current user is known to be user1, change the group ownership of file.txt to group1 only. Display the ownership of file.txt.']},ignore_index=True)

chown = chown.append({'Command':'chown -f --from=user1 :group1 file.txt','NL Queries':['Change the group ownership of file.txt to group1 only if current owner is user1. Suppress the warnings/errors.',
																					'How do I change the group ownership of file.txt to group1 only if current user is user1 without any warnings?',
																					'If the current user is known to be user1, change the group ownership of file.txt to group1. Don\'t display any error/warnings.']},ignore_index=True)
###
chown = chown.append({'Command':'chown --from=:group1 user1 file.txt','NL Queries':['Change the ownership of file.txt to user1 if the group owner is group1.',
																					'How do I change the ownership of file.txt to user1 if group owner is group1?',
																					'If the current group owner of file.txt is group1, change the owner of the file to user1.']},ignore_index=True)

chown = chown.append({'Command':'chown -c --from=:group1 user1 file.txt','NL Queries':['Change the ownership of file.txt to user1 if the group owner is group1. Show the changes which occured.',
																					'How do I change the ownership of file.txt to user1 if group owner is group1 and see the changes made?',
																					'If the current group owner of file.txt is group1, change the owner of the file to user1 and show the changes which occured after the operation.']},ignore_index=True)

chown = chown.append({'Command':'chown -v --from=:group1 user1 file.txt','NL Queries':['Change the ownership of file.txt to user1 if the group owner is group1. Show verbose explanation of the ownership details of file.txt.',
																					'How do I change the ownership of file.txt to user1 if group owner is group1 and see the ownership details of file.txt?',
																					'If the current group owner of file.txt is group1, change the owner of the file to user1 and see the owners of file.txt.']},ignore_index=True)

chown = chown.append({'Command':'chown -f --from=:group1 user1 file.txt','NL Queries':['Change the ownership of file.txt to user1 if the group owner is group1.Suppress the warnings/errors.',
																					'How do I change the ownership of file.txt to user1 if group owner is group1 without any warnings?',
																					'If the current group owner of file.txt is group1, change the owner of the file to user1. Don\'t display any error/warnings.']},ignore_index=True)
####
chown = chown.append({'Command':'chown -h root:friends tmp_link','NL Queries':['How do I change the ownership of the symbolic file tmp_link to user as root and group as friends?',
																				'Change the ownership for the symbolic file tmp_link. Make root as owner and friends as group owner.',
																				'Make root the owner of symbolic file tmp_link. How do I make friends as it\'s group owner?']},ignore_index=True)

chown = chown.append({'Command':'chown -c -h root:friends tmp_link','NL Queries':['How do I change the ownership of the symbolic file tmp_link to user as root and group as friends and see the changes which occured?',
																				'Change the ownership for the symbolic file tmp_link and display the changes. Make root as owner and friends as group owner.',
																				'Make root the owner of symbolic file tmp_link. How do I make friends as it\'s group owner? How do I see any changes made?']},ignore_index=True)

chown = chown.append({'Command':'chown -v -h root:friends tmp_link','NL Queries':['How do I change the ownership of the symbolic file tmp_link to user as root and group as friends? Show verbose explanation of change in ownership.',
																				'Change the ownership for the symbolic file tmp_link. Make root as owner and friends as group owner and display the ownership details of tmp_link.',
																				'Make root the owner of symbolic file tmp_link. How do I make friends as it\'s group owner? Show ownership information of tmp_link.']},ignore_index=True)

chown = chown.append({'Command':'chown -f -h root:friends tmp_link','NL Queries':['How do I change the ownership of the symbolic file tmp_link to user as root and group as friends without any errors? ',
																				'Change the ownership for the symbolic file tmp_link root. Make root as owner and friends as group owner. Suppress the warnings/errors.',
																				'Make root the owner of symbolic file tmp_link. How do I make friends as it\'s group owner? Don\'t display any error/warnings.']},ignore_index=True)
###
chown = chown.append({'Command':'chown -h root tmp_link','NL Queries':['How do I change the ownership of the symbolic file tmp_link to root?',
																		'Change the ownership for the symbolic file tmp_link. Make root as owner',
																		'Make root the owner of symbolic file tmp_link.']},ignore_index=True)

chown = chown.append({'Command':'chown -c -h root tmp_link','NL Queries':['How do I change the ownership of the symbolic file tmp_link to root and see the changes in ownership?',
																		'Change the ownership for the symbolic file tmp_link. Make root as owner. Display the change of ownership after the operation.',
																		'Make root the owner of symbolic file tmp_link. Show the changes made.']},ignore_index=True)

chown = chown.append({'Command':'chown -v -h root tmp_link','NL Queries':['How do I change the ownership of the symbolic file tmp_link to root? Show verbose explanation of ownership of tmp_link.',
																		'Change the ownership for the symbolic file tmp_link. Make root as owner. Show ownership details of tmp_link.',
																		'Make root the owner of symbolic file tmp_link and show the ownership details of tmp_link.']},ignore_index=True)

chown = chown.append({'Command':'chown -f -h root tmp_link','NL Queries':['How do I change the ownership of the symbolic file tmp_link to root? Suppress the warnings/errors.',
																		'Change the ownership for the symbolic file tmp_link. Make root as owner without any errors displayed.',
																		'Make root the owner of symbolic file tmp_link. Don\'t display any error/warnings.']},ignore_index=True)
###
chown = chown.append({'Command':'chown -h :friends tmp_link','NL Queries':['How do I change the group ownership of the symbolic file tmp_link to friends?',
																			'Change the group ownership for the symbolic file tmp_link to friends.',
																			'Make friends the group owner of the symbolic file tmp_link.']},ignore_index=True)

chown = chown.append({'Command':'chown -c -h :friends tmp_link','NL Queries':['How do I change the group ownership of the symbolic file tmp_link to friends and see the changes in ownership?',
																			'Change the group ownership for the symbolic file tmp_link to friends. Display the change of ownership.',
																			'Make friends the group owner of the symbolic file tmp_link. Show the changes which occured.']},ignore_index=True)

chown = chown.append({'Command':'chown -v -h :friends tmp_link','NL Queries':['How do I change the group ownership of the symbolic file tmp_link to friends? Show verbose explanation of ownership of tmp_link.',
																			'Change the group ownership for the symbolic file tmp_link to friends. Show ownership details of tmp_link.',
																			'Make friends the group owner of the symbolic file tmp_link and show the ownership details of tmp_link.']},ignore_index=True)

chown = chown.append({'Command':'chown -f -h :friends tmp_link','NL Queries':['How do I change the group ownership of the symbolic file tmp_link to friends? Suppress the warnings/errors.',
																			'Change the group ownership for the symbolic file tmp_link to friends without any errors displayed.',
																			'Make friends the group owner of the symbolic file tmp_link. Don\'t display any error/warnings.']},ignore_index=True)
###

chown = chown.append({'Command':'chown --dereference root:friends tmp_link','NL Queries':['How do I change the ownership of the reference to the symbolic link tmp_link to root? Change group ownership to friends.',
																						'Change the ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to root. Make friends as group owners.',
																						'Make root the owner and friends as group owners of the file of which symbolic link is tmp_link.']},ignore_index=True)

chown = chown.append({'Command':'chown -c --dereference root:friends tmp_link','NL Queries':['How do I change the ownership of the reference to the symbolic link tmp_link to root? Change group ownership to friends. Show the changes.',
																						'Change the ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to root. Make friends as group owners and display the changes of ownership.',
																						'Make root the owner, friends as group owners of the file of which symbolic link is tmp_link and show the changes.']},ignore_index=True)

chown = chown.append({'Command':'chown -v --dereference root:friends tmp_link','NL Queries':['How do I change the ownership of the reference to the symbolic link tmp_link to root? Change group ownership to friends.Show verbose explanation of ownership of tmp_link.',
																						'Change the ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to root. Make friends as group owners. Show ownership details of tmp_link.',
																						'Make root the owner and friends as group owners of the file of which symbolic link is tmp_link and and show the ownership details of tmp_link.']},ignore_index=True)

chown = chown.append({'Command':'chown -f --dereference root:friends tmp_link','NL Queries':['How do I change the ownership of the reference to the symbolic link tmp_link to root? Change group ownership to friends. Suppress the warnings/errors.',
																						'Change the ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to root. Make friends as group owners without showing any errors displayed.',
																						'Make root the owner and friends as group owners of the file of which symbolic link is tmp_link. Don\'t display any error/warnings.']},ignore_index=True)

###
chown = chown.append({'Command':'chown --dereference root tmp_link','NL Queries':['How do I change the ownership of the reference to the symbolic link tmp_link to root?',
																				'Change the ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to root.'
																				'Make root the owner of the file of which symbolic link is tmp_link.']},ignore_index=True)


chown = chown.append({'Command':'chown -c --dereference root tmp_link','NL Queries':['How do I change the ownership of the reference to the symbolic link tmp_link to root? Show the changes.',
																				'Change the ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to root and display the changes.'
																				'Make root the owner of the file of which symbolic link is tmp_link and show the changes.']},ignore_index=True)

chown = chown.append({'Command':'chown -v --dereference root tmp_link','NL Queries':['How do I change the ownership of the reference to the symbolic link tmp_link to root? Show verbose explanation of ownership.',
																				'Change the ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to root and display the ownership  details.'
																				'Make root the owner of the file of which symbolic link is tmp_link and display the ownership details.']},ignore_index=True)

chown = chown.append({'Command':'chown -f --dereference root tmp_link','NL Queries':['How do I change the ownership of the reference to the symbolic link tmp_link to root? Suppress the warnings/errors.',
																				'Change the ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to root without any errors displayed.'
																				'Make root the owner of the file of which symbolic link is tmp_link. Don\'t display any error/warnings.']},ignore_index=True)
###
chown = chown.append({'Command':'chown --dereference :friends tmp_link','NL Queries':['How do I change the group ownership of the reference to the symbolic link tmp_link to friends?',
																						'Change the group ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to friends.',
																						'Make friends the group owner of the file of which symbolic link is tmp_link.']},ignore_index=True)

chown = chown.append({'Command':'chown -c --dereference :friends tmp_link','NL Queries':['How do I change the group ownership of the reference to the symbolic link tmp_link to friends? Show the changes in ownership occured.',
																						'Change the group ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to friends. Display the changes.',
																						'Make friends the group owner of the file of which symbolic link is tmp_link and show the changes occured, if any.']},ignore_index=True)

chown = chown.append({'Command':'chown -v --dereference :friends tmp_link','NL Queries':['How do I change the group ownership of the reference to the symbolic link tmp_link to friends? Show verbose explanation of ownership.',
																						'Change the group ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to friends. Display the ownership details.',
																						'Make friends the group owner of the file of which symbolic link is tmp_link and display the ownership details.']},ignore_index=True)

chown = chown.append({'Command':'chown -f --dereference :friends tmp_link','NL Queries':['How do I change the group ownership of the reference to the symbolic link tmp_link to friends? Suppress the warnings/errors.',
																						'Change the group ownership of the reference to the symbolic link tmp_link and not the symbolic link itself to friends. Don\'t display any error/warnings.',
																						'Make friends the group owner of the file of which symbolic link is tmp_link without showing any errors displayed.']},ignore_index=True)
###
chown = chown.append({'Command':'chown --reference=oldfile newfile','NL Queries':['How do I copy the ownership details from oldfile to newfile?',
																					'Copy the owner/group settings from oldfile to newfile.',
																					'How do I get the same ownership details for newfile similar to the oldfile?']},ignore_index=True)

chown = chown.append({'Command':'chown -c --reference=oldfile newfile','NL Queries':['How do I copy the ownership details from oldfile to newfile? Display the changes which occured.',
																					'Copy the owner/group settings from oldfile to newfile and show the changes, if any.',
																					'How do I get the same ownership details for newfile similar to the oldfile and display changes of ownership of newfile?']},ignore_index=True)

chown = chown.append({'Command':'chown -f--reference=oldfile newfile','NL Queries':['How do I copy the ownership details from oldfile to newfile? Suppress the warnings/errors.',
																					'Copy the owner/group settings from oldfile to newfile. Don\'t display any error/warnings.',
																					'How do I get the same ownership details for newfile similar to the oldfile without showing any error warnings?']},ignore_index=True)

chown = chown.append({'Command':'chown -v --reference=oldfile newfile','NL Queries':['How do I copy the ownership details from oldfile to newfile?Show verbose explanation of ownership.',
																					'Copy the owner/group settings from oldfile to newfile.Display the ownership details.',
																					'How do I get the same ownership details for newfile similar to the oldfile and see the ownership details of newfile after the operation?']},ignore_index=True)
###
chown = chown.append({'Command':'chown -R -H guest:family linux_symlnk','NL Queries':['How do I forcefully change the user/group ownership to guest/family of all files and folders referenced by symbolic link linux_symlnk recursively?',
																					'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make guest the owner and family the group owner.',
																					'How do I change the user ownership to guest for all the files and folders referenced in the symbolic link linux_symlnk. Make family the group owner.']},ignore_index=True)

chown = chown.append({'Command':'chown -c -R -H guest:family linux_symlnk','NL Queries':['How do I forcefully change the user/group ownership to guest/family of all files and folders referenced by symbolic link linux_symlnk recursively and see the changes made?',
																					'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make guest the owner and family the group owner. Display the changes in ownership,if any.',
																					'How do I change the user ownership to guest for all the files and folders referenced in the symbolic link linux_symlnk. Make family the group owner and show the ownership changes.']},ignore_index=True)

chown = chown.append({'Command':'chown -v -R -H guest:family linux_symlnk','NL Queries':['How do I forcefully change the user/group ownership to guest/family of all files and folders referenced by symbolic link linux_symlnk recursively? Show the verbose explanation of ownership of linux_symlnk.',
																					'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make guest the owner and family the group owner. Display ownership details of linux_symlnk.',
																					'How do I change the user ownership to guest for all the files and folders referenced in the symbolic link linux_symlnk. Make family the group owner and show who are the owners of linux_symlnk.']},ignore_index=True)

chown = chown.append({'Command':'chown -f -R -H guest:family linux_symlnk','NL Queries':['How do I forcefully change the user/group ownership to guest/family of all files and folders referenced by symbolic link linux_symlnk recursively? Suppress the warnings/errors.' ,
																					'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make guest the owner and family the group owner without showing any errors and warnings.',
																					'How do I change the user ownership to guest for all the files and folders referenced in the symbolic link linux_symlnk. Make family the group owner. Don\'t display any error/warnings.']},ignore_index=True)
###
chown = chown.append({'Command':'chown -R -H guest linux_symlnk','NL Queries':['How do I forcefully change the user ownership to guest of all files and folders referenced by symbolic link linux_symlnk recursively?',
																				'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make guest the owner.',
																				'How do I change the user ownership to guest for all the files and folders referenced in the symbolic link linux_symlnk.']},ignore_index=True)

chown = chown.append({'Command':'chown -c -R -H guest linux_symlnk','NL Queries':['How do I forcefully change the user ownership to guest of all files and folders referenced by symbolic link linux_symlnk recursively and see the changes made?',
																				'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make guest the owner. Display the changes in ownership,if any.',
																				'How do I change the user ownership to guest for all the files and folders referenced in the symbolic link linux_symlnk and see the ownership changes.']},ignore_index=True)

chown = chown.append({'Command':'chown -v -R -H guest linux_symlnk','NL Queries':['How do I forcefully change the user ownership to guest of all files and folders referenced by symbolic link linux_symlnk recursively? Show the verbose explanation of ownership of linux_symlnk.',
																				'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make guest the owner. Display ownership details of linux_symlnk.',
																				'How do I change the user ownership to guest for all the files and folders referenced in the symbolic link linux_symlnk and see who are the owners of linux_symlnk?']},ignore_index=True)

chown = chown.append({'Command':'chown -f -R -H guest linux_symlnk','NL Queries':['How do I forcefully change the user ownership to guest of all files and folders referenced by symbolic link linux_symlnk recursively? Suppress the warnings/errors.',
																				'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make guest the owner without showing any errors and warnings. ',
																				'How do I change the user ownership to guest for all the files and folders referenced in the symbolic link linux_symlnk. Don\'t display any error/warnings.']},ignore_index=True)

###
chown = chown.append({'Command':'chown -R -H :family linux_symlnk','NL Queries':['How do I forcefully change the group ownership to family of all files and folders referenced by symbolic link linux_symlnk recursively?',
																				'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make family the group owner.',
																				'How do I change the group ownership of all the files and folders referenced in the symbolic link linux_symlnk to family?']},ignore_index=True)

chown = chown.append({'Command':'chown -c -R -H :family linux_symlnk','NL Queries':['How do I forcefully change the group ownership to family of all files and folders referenced by symbolic link linux_symlnk recursively and see the changes in ownership?',
																				'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make family the group owner.Display the changes in ownership,if any.',
																				'How do I change the group ownership of all the files and folders referenced in the symbolic link linux_symlnk to family and see the ownership changes?']},ignore_index=True)

chown = chown.append({'Command':'chown -v -R -H :family linux_symlnk','NL Queries':['How do I forcefully change the group ownership to family of all files and folders referenced by symbolic link linux_symlnk recursively? Show the verbose explanation of ownership of linux_symlnk.',
																				'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make family the group owner. Display ownership details of linux_symlnk.',
																				'How do I change the group ownership of all the files and folders referenced in the symbolic link linux_symlnk to family and see who are the owners of linux_symlnk?']},ignore_index=True)

chown = chown.append({'Command':'chown -f -R -H :family linux_symlnk','NL Queries':['How do I forcefully change the group ownership to family of all files and folders referenced by symbolic link linux_symlnk recursively? Suppress the warnings/errors.',
																				'Change the ownership of files and folders referenced by symbolic link linux_symlnk recursively. Make family the group owner without showing any errors and warnings.',
																				'How do I change the group ownership of all the files and folders referenced in the symbolic link linux_symlnk to family? Don\'t display any error/warnings.']},ignore_index=True)
###	
chown = chown.append({'Command':'chown -v -R guest linux','NL Queries':['How do I list all the ownership details when I recursively change the ownership of folder linux to guest?',
																		'List the ownership details when I recursively change the ownership for the folder linux to guest.',
																		'Change the ownership of the directory linux and all its files and folders to guest. List the ownership for all the files and folders.']},ignore_index=True)

chown = chown.append({'Command':'chown -R guest linux','NL Queries':['How do I recursively change the ownership of folder linux to guest?',
																	'Recursively change the ownership for the folder linux to guest.',
																	'Change the ownership of the directory linux and all its files and folders to guest.']},ignore_index=True)

chown = chown.append({'Command':'chown -c -R guest linux','NL Queries':['How do I list all the ownership changes when I recursively change the ownership of folder linux to guest?',
																		'List the ownership changes when I recursively change the ownership for the folder linux to guest.',
																		'Change the ownership of the directory linux and all its files and folders to guest. List the changes in ownership for all the files and folders.']},ignore_index=True)

chown = chown.append({'Command':'chown -f -R guest linux','NL Queries':['How do I recursively change the ownership of folder linux to guest? Suppress all warnings/errors.',
																		'Recursively change the ownership for the folder linux to guest without showing any warnings or errors.',
																		'Change the ownership of the directory linux and all its files and folders to guest. List the ownership for all the files and folders without showing any warnings or errors.']},ignore_index=True)
###
chown = chown.append({'Command':'chown -v -R :family linux','NL Queries':['How do I list all the ownership details when I recursively change the group ownership of folder linux to family.',
																		'List the ownership details when I recursively change the group ownership for the folder linux to family.',
																		'Change the group ownership of the directory linux and all its files and folders to family. List the ownership for all the files and folders.']},ignore_index=True)

chown = chown.append({'Command':'chown -R :family linux','NL Queries':['How do I recursively change the group ownership of folder linux to family.',
																		'Recursively change the group ownership for the folder linux to family.',
																		'Change the group ownership of the directory linux and all its files and folders to family.']},ignore_index=True)

chown = chown.append({'Command':'chown -c -R :family linux','NL Queries':['How do I list all the ownership changes when I recursively change the group ownership of folder linux to family.',
																		'List the ownership changes when I recursively change the group ownership for the folder linux to family.',
																		'Change the group ownership of the directory linux and all its files and folders to family. List the changes in ownership for all the files and folders.']},ignore_index=True)

chown = chown.append({'Command':'chown -f -R :family linux','NL Queries':['How do I recursively change the group ownership of folder linux to family. Suppress all errors/warnings.',
																		'Recursively change the group ownership for the folder linux to family without showing any warnings or errors.',
																		'Change the group ownership of the directory linux and all its files and folders to family without showing any errors or warnings.']},ignore_index=True)

###
chown = chown.append({'Command':'chown -v -R guest:family linux','NL Queries':['How do I list all the ownership details when I recursively change the user/group ownership of folder linux to guest/family?',
																				'List the ownership details when I recursively change the user ownership and group ownership for the folder linux to guest and family respectively.',
																				'Change the user ownership to guest and group ownership of the directory linux and all its files and folders to family. List the ownership for all the files and folders.']},ignore_index=True)

chown = chown.append({'Command':'chown -R guest:family linux','NL Queries':['How do I recursively change the user/group ownership of folder linux to guest/family?',
																				'Recursively change the user ownership and group ownership for the folder linux to guest and family respectively.',
																				'Change the user ownership to guest and group ownership of the directory linux and all its files and folders to family.']},ignore_index=True)

chown = chown.append({'Command':'chown -c -R guest:family linux','NL Queries':['How do I list all the ownership changes when I recursively change the user/group ownership of folder linux to guest/family',
																				'List the ownership changes when I recursively change the user ownership and group ownership for the folder linux to guest and family respectively.',
																				'Change the user ownership to guest and group ownership of the directory linux and all its files and folders to family. List the ownership changes for all the files and folders.']},ignore_index=True)

chown = chown.append({'Command':'chown -f -R guest:family linux','NL Queries':['How do I recursively change the user/group ownership of folder linux to guest/family? Suppress all warnings and errors.',
																				'Recursively change the user ownership and group ownership for the folder linux to guest and family respectively without showing any errors or warnings.',
																				'Change the user ownership to guest and group ownership of the directory linux and all its files and folders to family. Don\'t show any wrrors or warnings.']},ignore_index=True)
###
chown = chown.append({'Command':'chown --version','NL Queries':['How do I find the version of my chown command?',
																'Display the version of the chown command.',
																'Output the chown version and exit.']},ignore_index=True)

chown = chown.append({'Command':'chown --help','NL Queries':['How do I get help related to the chown command?',
															'Display help for chown command along with many options.',
															'Output the flags available with chown command.']},ignore_index=True)


#chown = chown.append({'Command':'chown jim /path/to/file1 /path/to/file2 /path/to/file3','NL Queries':['How do I change the owner of file2 and file3 in the directory /path/to? to jim?',
#				'Change the ownership of file2 and file3 in a given path /path/to .',
#				'How do I change the ownerhsip of multiples files file2 and file3 in /path/to to jim?']},ignore_index=True)
#chown = chown.append({'Command':'chown 625:874 file1','NL Queries':['How do I change ownership of file1 if I know the user ID 625 and group ID 874?','Changes the owner of file1 to UID 625 and GID 874.','Can I change the ownership of a file file1 to a particular user ID 625 group ID 874?']},ignore_index=True)
#chown = chown.append({'Command':'chown root *','NL Queries':['How do I change the ownership details for all files in the current directory to root?','Changes the ownership for the files present in the current directory to root.']},ignore_index=True)


print chown.shape
