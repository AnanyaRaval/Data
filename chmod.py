import pandas as pd 

chmod = pd.DataFrame(columns = ['Command','NL Queries'])

chmod = chmod.append({'Command':'chmod u=rwx,g=rx,o=r myfile','NL Queries':['Change permissions for myfile. User can read, write and execute. Group can read and execute it.Others can only read it.',
																		'How do I change permissions of myfile so that user can do everything, group can only read and write and others can only read it.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod 754 myfile','NL Queries':['Change permissions for myfile. User can read, write and execute. Group can read and execute it.Others can only read it.',
																'How do I change permissions of myfile so that user can do everything, group can only read and write and others can only read it.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod u+x filename','NL Queries':['Add execute permission to user for file filename.',
																'How do I make user persimssions of this file to execute also?',
																'For filename, add execute persmission to user.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -R 755 directory-name/','NL Queries':['Change permission of folder directory-name. User can read,write,execute. Group and Others can read and execute. All files should also have the same permission.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod o-w filename','NL Queries':['Add execute permissions to other users for the file filename', 
																	'How can I make the other users have permission to execute the file?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod ugo=rx filename','NL Queries':['Add execute and read permissions to all users for the file filename', 
																	'How can I give permission for all users to read and execute the file?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod g-w filename','NL Queries':['Remove permission for the group to write into filename', 
																	'How can I remove permissions to the group to make it non-writable?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -R +w,g=rw,o-rw, directory-name/','NL Queries':['Gives permission to members of a group to write the file and removes permission for other users to read and write but gives both permission to execute.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod 600 filename','NL Queries':['Restores default permission state to user to read and write but removes permission for other users to read and write.', 
																'How can I revert the permissions to the original state to give only the owner access to the file?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod g-rwx,o-rwx filename','NL Queries':['Remove access to all users from reading and writing to a file',
																		 'How can I remove permissions to all users?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod 700 filename','NL Queries':['Only the owner of the file can access it',
																 'How can I full access to the file only to the user?',
																  'Makes the file private and accessible to the person who created it']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod 477 filename','NL Queries':['Give permission to all users to read, write and execute a file to the group and non group members but only read access to the user executing it.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod 777 filename','NL Queries':['Give permission to all users to read, write and execute a file',
																	 'How can I full access to the file to all users?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod a-x filename','NL Queries':['Remove execute permissions for everyone.',
																	 'How can I remove execute permissions for all users?']},ignore_index = True)


print chmod.shape
