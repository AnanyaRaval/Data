import pandas as pd 
'''
	-c, --changes
              like verbose but log only when a change is made

       -f, --silent, --quiet
              suppress most error messages

       -v, --verbose
              output a diagnostic for every file processed

       --no-preserve-root
              do not treat '/' specially (the default)

       --preserve-root
              fail to operate recursively on '/'

       --reference=RFILE
              use RFILE's mode instead of MODE values

       -R, --recursive
              change files and directories recursively
'''

chmod = pd.DataFrame(columns = ['Command','NL Queries'])

#-v and -c are same but -c generates a log only if changes are done but -v generates a log even if changes are not done. 
#Do chmod *** -v > new.txt to see the log in the text file 'new'.

chmod = chmod.append({'Command':'chmod filename --reference=newfile.','NL Queries':['Change permissions for file filename to match the permissions of newfile.', 
																				'How do I change permissions of file filename so that it matches the permissions of newfile.', 
																				'Give permissions to filename so that it is the same as that of newfile.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod filename -c --reference=newfile.','NL Queries':['Change permissions for file filename to match the permissions of newfile and generate a log if changes are done.', 
																				'How do I change permissions of file filename so that it matches the permissions of newfile and generate a log if changes are done.', 
																				'Give permissions to filename so that it is the same as that of newfile and generate a log if changes are done.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod filename -v --reference=newfile.','NL Queries':['Change permissions for file filename to match the permissions of newfile and generate a log of changes made.', 
																				'How do I change permissions of file filename so that it matches the permissions of newfile and generate a log of the changes made by the command.', 
																				'Give permissions to filename so that it is the same as that of newfile and generate a log if changes are made.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod filename -cf --reference=newfile.','NL Queries':['Change permissions for file filename to match the permissions of newfile and generate a log if changes are done and prevent error messages from being shown.', 
																				'How do I change permissions of file filename so that it matches the permissions of newfile and generate a log if changes are done and prevent error messages from being shown.', 
																				'Give permissions to filename so that it is the same as that of newfile and generate a log if changes are done and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod filename -vf --reference=newfile.','NL Queries':['Change permissions for file filename to match the permissions of newfile and generate a log and prevent error messages from being shown.', 
																				'How do I change permissions of file filename so that it matches the permissions of newfile and generate a log and prevent error messages from being shown.', 
																				'Give permissions to filename so that it is the same as that of newfile and generate a log and prevent error messages from being shown.']},ignore_index = True)

#This ends the reference flag commands 

chmod = chmod.append({'Command':'chmod u=rwx,g=rx,o=r filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it.', 
																				'Give permission for user to read, write and execute, group to read and execute and other users to read the file filename.',
																				'How do I change permissions of file filename so that user can do everything, group can only read and write and others can only read it.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -c u=rwx,g=rx,o=r filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made to the file.', 
																				'Give permission for user to read, write and execute, group to read and execute and other users to read the file filename. Generate a log if changes are made to the file.',
																				'How do I change permissions of file filename so that user can do everything, group can read and execute and others can only read it and generate a log if changes are made to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -cf u=rwx,g=rx,o=r filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made to the file and prevent error messages from being shown.', 
																				'Give permission for user to read, write and execute, group to read and execute and other users to read the file filename. Generate a log if changes are made to the file and prevent error messages from being shown.',
																				'How do I change permissions of file filename so that user can do everything, group can only read and execute and others can only read it and generate a log if changes are made to that file and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -f u=rwx,g=rx,o=r filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it. Prevent error messages from being shown.', 
																				'Give permission for user to read, write and execute, group to read and execute and other users to read the file filename. Prevent error messages from being shown.',
																				'How do I change permissions of file filename so that user can do everything, group can only read and execute and others can only read it and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -v u=rwx,g=rx,o=r filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it and generate a log.', 
																				'Give permission for user to read, write and execute, group to read and execute and other users to read the file filename. Generate a log.',
																				'How do I change permissions of file filename so that user can do everything, group can only read and execute and others can only read it and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -vf u=rwx,g=rx,o=r filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log and prevent error messages from being shown.', 
																				'Give permission for user to read, write and execute, Group to read and execute and other users to read the file filename. Generate a log and prevent error messages from being shown.',
																				'How do I change permissions of file filename so that user can do everything, group can only read and execute and others can only read it and generate a log and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rvf u=rwx,g=rx,o=r foldername/','NL Queries':['Change permissions for all the content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log and prevent error messages from being shown.', 												
																						'Change permissions for all the content folder in foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log and prevent error messages from being shown.',
																					'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it and generate a log and prevent error messages from being shown.',						
																					'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it and generate a log and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rcf u=rwx,g=rx,o=r foldername/','NL Queries':['Change permissions for all the content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made to the content and prevent error messages from being shown.', 												
																					'Change permissions for all the content folder in foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made to the content and prevent error messages from being shown.',
																					'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it and generate a log if changes are made to the content and prevent error messages from being shown.',						
																					'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it and generate a log if changes are made to the content and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rf u=rwx,g=rx,o=r foldername/','NL Queries':['Change permissions for all the content directory in foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Prevent error messages from being shown.',
																				'Change permissions for all the content folder in foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Prevent error messages from being shown.', 																				
																				'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it and Prevent error messages from being shown.',
																				'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it and Prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rc u=rwx,g=rx,o=r foldername/','NL Queries':['Change permissions for all the content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made to the file.', 																			
																						'Change permissions for all the content in folder foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made to the file.',
																						'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it and generate a log if changes are made to the file.',																		
																						'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rv u=rwx,g=rx,o=r foldername/','NL Queries':['Change permissions for all the content in folder foldername. User can read, write and execute. Group can read and execute it. Others can only read it. generate a log.', 
																				'Change permissions for all the content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log.',
																				'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it and generate a log.', 
																				'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it and generate a log.']},ignore_index = True)

#This ends all combinations for u=rwx,g=rx,o=r

chmod = chmod.append({'Command':'chmod 754 filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it.Others can only read it.', 
																	'How do I change permissions of file filename so that user can do everything, group can only read and write and others can only read it.',
																	'Give user full access to the filename while group can only read and execute and other users can read.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -c 754 filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it. Log is generated if changes are made to the file.', 
																	'How do I change permissions of file filename so that user can do everything, group can only read and write and others can only read it and a log is generated if changes are made to the file.',
																	'Give user full access to filename while group can only read and execute and other users can read. Generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -f 754 filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it. Errors are prevented from being shown.', 
																				'How do I change permissions of file filename so that user can do everything, group can only read and execute and others can only read it and prevent error messages from being shown.',
																				'Give user full access to filename while group can only read and execute and other users can read and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -vf 754 filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log and prevent errors from being shown.', 
																				'How do I change permissions of file filename so that user can do everything, group can only read and execute and others can only read it. Generate a log and prevent error messages.',
																				'Give user full access to filename while group can only read and execute and other users can read. Prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -cf 754 filename','NL Queries':['Change permissions for file filename. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made and prevent errors from being shown.', 
																				'How do I change permissions of file filename so that user can do everything, group can only read and execute and others can only read it. Generate a log if changes are made and prevent error messages.',
																				'Give user full access to filename while group can only read and execute and other users can read. Prevent error messages from being shown. Generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rvf 754 foldername/','NL Queries':['Change permissions for content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log and prevent errors from being shown.', 
																				'Change permissions for content in folder foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log and prevent errors from being shown.', 
																				'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log and prevent error messages.', 	
																				'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log and prevent error messages.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rcf 754 foldername/','NL Queries':['Change permissions for content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made and prevent errors from being shown.', 
																				'Change permissions for content in folder foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made and prevent errors from being shown.', 
																				'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log if changes are made and prevent error messages.', 
																				'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log if changes are made and prevent error messages.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rc 754 foldername/','NL Queries':['Change permissions for content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made.', 
																				'Change permissions for content in folder foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log if changes are made.', 
																				'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log if changes are made.', 
																				'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log if changes are made.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rv 754 foldername/','NL Queries':['Change permissions for content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log.', 
																				'Change permissions for content in folder foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log.', 
																				'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log.', 
																				'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rv 754 foldername/','NL Queries':['Change permissions for content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log.', 
																				'Change permissions for content in folder foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Generate a log.', 
																				'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log.', 
																				'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it. Generate a log.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rf 754 foldername/','NL Queries':['Change permissions for content in directory foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Prevent errors from being shown.', 
																				'Change permissions for content in folder foldername. User can read, write and execute. Group can read and execute it. Others can only read it. Prevent errors from being shown.', 
																				'How do I change permissions of all content in directory foldername so that user can do everything, group can only read and execute and others can only read it. Prevent error messages.', 
																				'How do I change permissions of all content in folder foldername so that user can do everything, group can only read and execute and others can only read it. Prevent error messages.']},ignore_index = True)

#This ends all combinations for 754

chmod = chmod.append({'Command':'chmod u+x filename','NL Queries':['Add execute permission to user for file filename.',	
																				'How do I make user perimssions of filename to execute also?',
																				'For file filename, add execute permission to user.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -c u+x filename','NL Queries':['Add execute permission to user for file filename and generate a log if changes are made.',	
																				'How do I make user have permissions of filename to execute and generate a log if changes are made?',
																				'For file filename, add execute permission to user and generate a log if changes are made.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -v u+x filename','NL Queries':['Add execute permission to user for file filename and generate a log.',	
																				'How do I make user have permissions of filename to execute and generate a log?',
																				'For file filename, add execute permission to user and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -f u+x filename','NL Queries':['Add execute permission to user for file filename and prevent error messages from being shown.',	
																				'How do I make user have permissions of filename to execute and prevent error messages from being shown?',
																				'For file filename, add execute permission to user and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -cf u+x filename','NL Queries':['Add execute permission to user for file filename and prevent error messages from being shown and generate a log if changes are made.',	
																				'How do I make user have permissions of filename to execute and prevent error messages from being shown and generate a log if changes are made?',
																				'For file filename, add execute permission to user and prevent error messages from being shown and generate a log if changes are made.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -vf u+x filename','NL Queries':['Add execute permission to user for file filename and prevent error messages from being shown and generate a log.',	
																				'How do I make user have permissions of filename to execute and prevent error messages from being shown and generate a log?',
																				'For file filename, add execute permission to user and prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rvf u+x foldername/','NL Queries':['Add execute permission to user for content in directory foldername and prevent error messages from being shown and generate a log.',		
																				'Add execute permission to user for content in folder foldername and prevent error messages from being shown and generate a log.',
																				'How do I make user have permissions of the content in directory foldername to execute and prevent error messages from being shown and generate a log?',
																				'How do I make user have permissions of the content in folder foldername to execute and prevent error messages from being shown and generate a log?'
																				'For all content in directory foldername, add execute permission to user and prevent error messages from being shown and generate a log.',
																				'For all content in folder foldername, add execute permission to user and prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rcf u+x foldername/','NL Queries':['Add execute permission to user for  all content in directory foldername and prevent error messages from being shown and generate a log if changes are made.',		
																				'Add execute permission to user for content in folder foldername and prevent error messages from being shown and generate a log if changes are made.',
																				'How do I make user have permissions of the content in directory foldername to execute and prevent error messages from being shown and generate a log if changes are made?',
																				'How do I make user have permissions of the content in folder foldername to execute and prevent error messages from being shown and generate a log if changes are made?'
																				'For all content in directory foldername, add execute permission to user and prevent error messages from being shown and generate a log if changes are made.',
																				'For all content in folder foldername, add execute permission to user and prevent error messages from being shown and generate a log if changes are made.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rc u+x foldername/','NL Queries':['Add execute permission to user for content in directory foldername and generate a log if changes are made.',		
																				'Add execute permission to user for content in folder foldername and generate a log if changes are made.',
																				'How do I make user have permissions of the content in directory foldername to execute and generate a log if changes are made?',
																				'How do I make user have permissions of the content in folder foldername to execute and generate a log if changes are made?'
																				'For all content in directory foldername, add execute permission to user and generate a log if changes are made.',	
																				'For all content in folder foldername, add execute permission to user and generate a log if changes are made.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rv u+x foldername/','NL Queries':['Add execute permission to user for content in directory foldername and generate a log.',		
																				'Add execute permission to user for content in folder foldername and generate a log.',
																				'How do I make user have permissions of the content in directory foldername to execute and generate a log?',
																				'How do I make user have permissions of the content in folder foldername to execute and generate a log?'
																				'For all content in directory foldername, add execute permission to user and generate a log.',	
																				'For all content in folder foldername, add execute permission to user and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command':'chmod -Rf u+x foldername/','NL Queries':['Add execute permission to user for content in directory foldername and prevent error messages from being shown.',		
																				'Add execute permission to user for content in folder foldername and prevent error messages from being shown.',
																				'How do I make user have permissions of the content in directory foldername to execute and prevent error messages from being shown?',
																				'How do I make user have permissions of the content in folder foldername to execute and prevent error messages from being shown?'
																				'For all content in directory foldername, add execute permission to user and prevent error messages from being shown.',
																				'For all content in folder foldername, add execute permission to user and prevent error messages from being shown.']},ignore_index = True)

#This ends all combinations for u+x

chmod = chmod.append({'Command': 'chmod -R 755 directory-name/','NL Queries':['Change permission of folder directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission.',
																				'Change permission of directory directory-name. User can read, write, execute. Group and Others can read and execute. All content should also have the same permission.',
																				'How do I give permission of the folder directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission?',
																				'How do I give permission of the directory directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission?',
																				'Give permission to all the content of the folder directory-name such that the User can have full access while group and other users can read and execute.',
																				'Give permission to all the content of the directory directory-name such that the User can have full access while group and Other users can read and execute.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 755 directory-name/','NL Queries':['Change permission of folder directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Generate a log if changes are made.',
																				'Change permission of directory directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Generate a log if changes are made.',
																				'How do I give permission of the folder directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and generate a log if changes are made?',
																				'How do I give permission of the directory directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and generate a log if changes are made?',
																				'Give permission to all the content of the folder directory-name such that the User can have full access while group and other users can read and execute. Generate a log if changes are made.',
																				'Give permission to all the content of the directory directory-name such that the user can have full access while group and other users can read and execute. Generate a log if changes are made.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 755 directory-name/','NL Queries':['Change permission of folder directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Generate a log.',
																				'Change permission of directory directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Generate a log.',
																				'How do I give permission of the folder directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and generate a log?',
																				'How do I give permission of the directory directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and generate a log?',
																				'Give permission to all the content of the folder directory-name such that the user can have full access while group and other users can read and execute. Generate a log.',
																				'Give permission to all the content of the directory directory-name such that the user can have full access while group and other users can read and execute. Generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 755 directory-name/','NL Queries':['Change permission of folder directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Generate a log. Prevent error messages from being shown.',
																				'Change permission of directory directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Generate a log. Prevent error messages from being shown.',
																				'How do I give permission of the folder directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and generate a log and prevent error messages from being shown?',
																				'How do I give permission of the directory directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and generate a log and prevent error messages from being shown?',
																				'Give permission to all the content of the folder directory-name such that the user can have full access while group and other users can read and execute. Generate a log. Prevent error messages from being shown.',
																				'Give permission to all the content of the directory directory-name such that the User can have full access while group and other users can read and execute. Generate a log. Prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 755 directory-name/','NL Queries':['Change permission of folder directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Generate a log if changes are made. Prevent error messages from being shown.',
																				'Change permission of directory directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Generate a log if changes are made. Prevent error messages from being shown.',
																				'How do I give permission of the folder directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and generate a log if changes are made and prevent error messages from being shown?',
																				'How do I give permission of the directory directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and generate a log if changes are made and prevent error messages from being shown?',
																				'Give permission to all the content of the folder directory-name such that the user can have full access while group and other users can read and execute. Generate a log if changes are made. Prevent error messages from being shown.',
																				'Give permission to all the content of the directory directory-name such that the user can have full access while group and other users can read and execute. Generate a log if changes are made. Prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 755 directory-name/','NL Queries':['Change permission of folder directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Prevent error messages from being shown.',
																				'Change permission of directory directory-name. User can read, write, execute. Group and others can read and execute. All content should also have the same permission. Prevent error messages from being shown.',
																				'How do I give permission of the folder directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and prevent error messages from being shown?',
																				'How do I give permission of the directory directory-name such that the user can have full access while group and others can read and execute and all content will have the same permission and prevent error messages from being shown?',
																				'Give permission to all the content of the folder directory-name such that the User can have full access while group and Other users can read and execute. Prevent error messages from being shown.',
																				'Give permission to all the content of the directory directory-name such that the User can have full access while group and Other users can read and execute. Prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod 755 filename','NL Queries':['Change permission of file filename. User can read, write, execute. Group and others can read and execute.',
																				'How do I give permission of the file filename such that the user can have full access while group and others can read and execute?',
																				'Give permission to the file filename such that the user can have full access while group and other users can read and execute.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 755 filename','NL Queries':['Change permission of file filename. User can read, write, execute. Group and others can read and execute. Generate a log if changes are made.',
																				'How do I give permission of the file filename such that the user can have full access while group and others can read and execute and generate a log if changes are made?',
																				'Give permission to the file filename such that the User can have full access while group and other users can read and execute. Generate a log if changes are made.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 755 filename','NL Queries':['Change permission of file filename. User can read, write, execute. Group and others can read and execute. Generate a log.',
																				'How do I give permission of the file filename such that the user can have full access while group and others can read and execute and generate a log?',
																				'Give permission to the file filename such that the user can have full access while group and other users can read and execute. Generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 755 filename','NL Queries':['Change permission of file filename. User can read, write, execute. Group and others can read and execute. Prevent error messages from being shown.',
																				'How do I give permission of the file filename such that the user can have full access while group and others can read and execute and prevent error messages from being shown?',
																				'Give permission to the file filename such that the user can have full access while group and other users can read and execute. Prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 755 filename','NL Queries':['Change permission of file filename. User can read, write, execute. Group and others can read and execute. Generate a log if changes are made. Prevent error messages from being shown.',
																				'How do I give permission of the file filename such that the user can have full access while group and others can read and execute and generate a log if changes are made and prevent error messages from being shown?',
																				'Give permission to the file filename such that the user can have full access while group and other users can read and execute. Generate a log if changes are made. Prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 755 filename','NL Queries':['Change permission of file filename. User can read, write, execute. Group and others can read and execute. Generate a log. Prevent error messages from being shown.',
																				'How do I give permission of the file filename such that the user can have full access while group and others can read and execute and generate a log and prevent error messages from being shown?',
																				'Give permission to the file filename such that the user can have full access while group and other users can read and execute. Generate a log. Prevent error messages from being shown.']},ignore_index = True)

#This ends all combinations for 755

chmod = chmod.append({'Command': 'chmod o-w filename','NL Queries':['Remove write permissions to other users for the file filename.', 
																				'How can I make the other users not have permission to write the file filename?', 																	
																				'Prevent other users of the system from writing to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c o-w filename','NL Queries':['Remove write permissions to other users for the file filename and generate a log if changes are made to the file.', 												
																				'How can I make the other users not have permission to write the file filename and get to know a change is made?', 									
																				'Prevent other users of the system from writing to the file filename and generate a log for the changes made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f o-w filename','NL Queries':['Remove write permissions to other users for the file filename and prevent error messages from being shown.', 										
																				'How can I make the other users not have permission to write the file filename and prevent error messages being shown?', 								
																				'Prevent other users of the system from writing to the file filename and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf o-w filename','NL Queries':['Remove write permissions to other users for the file filename and prevent error messages from being shown and generate a log if changes are made to the file.', 
																				'How can I make the other users not have permission to write the file filename and prevent error messages being shown and generate a log if changes are made to the file?', 
																				'Prevent other users of the system from writing to the file filename and prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf o-w filename','NL Queries':['Remove write permissions to other users for the file filename and prevent error messages from being shown and generate a log.', 
																				'How can I make the other users not have permission to write the file filename and prevent error messages being shown and generate a log?', 
																				'Prevent other users of the system from writing to the file filename and prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -R o-w foldername/','NL Queries':['Remove write permissions to other users for the content in the directory foldername recursively.', 												
																				'Remove write permissions to other users for the content in the folder foldername recursively.',													
																				'How can I make the other users not have permission to write all the content in the directory foldername?', 									
																				'How can I make the other users not have permission to write all the content in the folder foldername?',										
																				'Prevent other users of the system from writing to all the content in the directory foldername.', 													
																				'Prevent other users of the system from writing to all the content in the folder foldername.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf o-w foldername/','NL Queries':['Remove write permissions to other users for the content in the directory foldername recursively. Generate a log if changes are made and prevent error messages from being shown.', 
																				'Remove write permissions to other users for the content in the folder foldername recursively. Generate a log if changes are made and prevent error messages from being shown.',
																				'How can I make the other users not have permission to write all the content in the directory foldername, generate a log if changes are made and prevent error messages from being shown?', 
																				'How can I make the other users not have permission to write all the content in the folder foldername, generate a log if changes are made and prevent error messages from being shown?',
																				'Prevent other users of the system from writing to all the content in the directory foldername, generate a log if changes are made and prevent error messages from being shown.',
																				'Prevent other users of the system from writing to all the content in the folder foldername, generate a log if changes are made and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf o-w foldername/','NL Queries':['Remove write permissions to other users for the content in the directory foldername recursively. Generate a log and prevent error messages from being shown.', 
																				'Remove write permissions to other users for the content in the folder foldername recursively. Generate a log if changes are made and prevent error messages from being shown.',
																				'How can I make the other users not have permission to write all the content in the directory foldername, generate a log and prevent error messages from being shown?', 
																				'How can I make the other users not have permission to write all the content in the folder foldername, generate a log and prevent error messages from being shown?',
																				'Prevent other users of the system from writing to all the content in the directory foldername, generate a log and prevent error messages from being shown.',
																				'Prevent other users of the system from writing to all the content in the folder foldername, generate a log and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv o-w foldername/','NL Queries':['Remove write permissions to other users for the content in the directory foldername recursively. Generate a log.', 
																				'Remove write permissions to other users for the content in the folder foldername recursively. Generate a log.',
																				'How can I make the other users not have permission to write all the content in the directory foldername, generate a log?', 
																				'How can I make the other users not have permission to write all the content in the folder foldername, generate a log?',
																				'Prevent other users of the system from writing to all the content in the directory foldername, generate a log.',
																				'Prevent other users of the system from writing to all the content in the folder foldername, generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc o-w foldername/','NL Queries':['Remove write permissions to other users for the content in the directory foldername recursively. Generate a log if changes are made.', 
																				'Remove write permissions to other users for the content in the folder foldername recursively. Generate a log if changes are made.',
																				'How can I make the other users not have permission to write all the content in the directory foldername, generate a log if changes are made?', 
																				'How can I make the other users not have permission to write all the content in the folder foldername, generate a log if changes are made?',
																				'Prevent other users of the system from writing to all the content in the directory foldername, generate a log if changes are made.',
																				'Prevent other users of the system from writing to all the content in the folder foldername, generate a log if changes are made.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf o-w foldername/','NL Queries':['Remove write permissions to other users for the content in the directory foldername recursively. Prevent error messages from being shown.', 
																				'Remove write permissions to other users for the content in the folder foldername recursively. Prevent error messages from being shown.',
																				'How can I make the other users not have permission to write all the content in the directory foldername, prevent error messages from being shown?', 
																				'How can I make the other users not have permission to write all the content in the folder foldername, prevent error messages from being shown?',
																				'Prevent other users of the system from writing to all the content in the directory foldername, prevent error messages from being shown.',
																				'Prevent other users of the system from writing to all the content in the folder foldername, prevent error messages from being shown.']},ignore_index = True)

#This ends all combinations for o-w

chmod = chmod.append({'Command': 'chmod ugo=rx filename','NL Queries':['Add execute and read permissions to all users for the file filename.', 
																				'How can I give permission for all users to read and execute the file filename?',																			
																				'Give execute and read permissions for the file filename to all users.',																			
																				'Grant read and execute permissions to the file filename to all users.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c ugo=rx filename','NL Queries':['Add execute and read permissions to all users for the file filename. Generate a log if changes are made to the file.', 
																				'How can I give permission for all users to read and execute the file filename and generate a log if changes are made to the file?',						
																				'Give execute and read permissions for the file filename to all users. Generate a log if changes are made to the file.',																			
																				'Grant read and execute permissions to the file filename to all users. Generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v ugo=rx filename','NL Queries':['Add execute and read permissions to all users for the file filename. Generate a log.', 
																				'How can I give permission for all users to read and execute the file filename and generate a log?',														
																				'Give execute and read permissions for the file filename to all users. Generate a log.',														
																				'Grant read and execute permissions to the file filename to all users. Generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f ugo=rx filename','NL Queries':['Add execute and read permissions to all users for the file filename. Prevent error messages from being shown.', 
																				'How can I give permission for all users to read and execute the file filename and prevent error messages from being shown?',								
																				'Give execute and read permissions for the file filename to all users. Prevent error messages from being shown.',								
																				'Grant read and execute permissions to the file filename to all users. Prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf ugo=rx filename','NL Queries':['Add execute and read permissions to all users for the file filename. Generate a log and prevent error messages from being shown.', 
																				'How can I give permission for all users to read and execute the file filename, generate a log and prevent error messages from being shown?',				
																				'Give execute and read permissions for the file filename to all users. Generate a log and prevent error messages from being shown.',														
																				'Grant read and execute permissions to the file filename to all users. Generate a log and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf ugo=rx filename','NL Queries':['Add execute and read permissions to all users for the file filename. Generate a log if changes are made to the file and prevent error messages from being shown.', 
																				'How can I give permission for all users to read and execute filename, generate a log if changes are made to the file and prevent error messages from being shown?',				
																				'Give execute and read permissions for the file filename to all users. Generate a log if changes are made to the file and prevent error messages from being shown.',														
																				'Grant read and execute permissions to the file filename to all users. Generate a log and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc ugo=rx foldername/','NL Queries':['Add execute and read permissions to all users for the content in directory foldername recursively. Generate a log if changes are made to the file.', 
																				'Add execute and read permissions to all users for the content in folder foldername recursively. Generate a log if changes are made to the file.',
																				'How can I give permission for all users to read and execute the all the content in the directory foldername and generate a log if changes are made to the file?',
																				'How can I give permission for all users to read and execute the all the content in the folder foldername and generate a log if changes are made to the file?',							
																				'Give execute and read permissions for all the content in the directory foldername to all users. Generate a log if changes are made to the file.',
																				'Give execute and read permissions for all the content in the folder foldername to all users. Generate a log if changes are made to the file.',
																				'Grant read and execute permissions to all the content in the directory foldername to all the users. Generate a log if changes are made to the file.',					
																				'Grant read and execute permissions to all the content in the folder foldername to all the users. Generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv ugo=rx foldername/','NL Queries':['Add execute and read permissions to all users for the content in directory foldername recursively. Generate a log.', 
																				'Add execute and read permissions to all users for the content in folder foldername recursively. Generate a log.',
																				'How can I give permission for all users to read and execute the all the content in the directory foldername and generate a log?',
																				'How can I give permission for all users to read and execute the all the content in the folder foldername and generate a log?',							
																				'Give execute and read permissions for all the content in the directory foldername to all users. Generate a log.',
																				'Give execute and read permissions for all the content in the folder foldername to all users. Generate a log.',
																				'Grant read and execute permissions to all the content in the directory foldername to all the users. Generate a log.',					
																				'Grant read and execute permissions to all the content in the folder foldername to all the users. Generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf ugo=rx foldername/','NL Queries':['Add execute and read permissions to all users for the content in directory foldername recursively. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'Add execute and read permissions to all users for the content in folder foldername recursively. Generate a log if changes are made to the file. Prevent error messages from being shown.',
																				'How can I give permission for all users to read and execute the all the content in the directory foldername, generate a log if changes are made to the file and prevent error messages from being shown?',
																				'How can I give permission for all users to read and execute the all the content in the folder foldername, generate a log if changes are made to the file and prevent error messages from being shown?',																		
																				'Give execute and read permissions for all the content in the directory foldername to all users. Generate a log if changes are made to the file. Prevent error messages from being shown.',
																				'Give execute and read permissions for all the content in the folder foldername to all users. Generate a log if changes are made to the file. Prevent error messages from being shown.',
																				'Grant read and execute permissions to all the content in the directory foldername to all the users. Generate a log if changes are made to the file. Prevent error messages from being shown.',																			
																				'Grant read and execute permissions to all the content in the folder foldername to all the users. Generate a log if changes are made to the file. Prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf ugo=rx foldername/','NL Queries':['Add execute and read permissions to all users for the content in directory foldername recursively. Generate a log. Prevent error messages from being shown.', 
																				'Add execute and read permissions to all users for the content in folder foldername recursively. Generate a log. Prevent error messages from being shown.',
																				'How can I give permission for all users to read and execute the all the content in the directory foldername, generate a log and prevent error messages from being shown?',
																				'How can I give permission for all users to read and execute the all the content in the folder foldername, generate a log and prevent error messages from being shown?',																		
																				'Give execute and read permissions for all the content in the directory foldername to all users. Generate a log. Prevent error messages from being shown.',
																				'Give execute and read permissions for all the content in the folder foldername to all users. Generate a log. Prevent error messages from being shown.',
																				'Grant read and execute permissions to all the content in the directory foldername to all the users. Generate a log. Prevent error messages from being shown.',																			
																				'Grant read and execute permissions to all the content in the folder foldername to all the users. Generate a log. Prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf ugo=rx foldername/','NL Queries':['Add execute and read permissions to all users for the content in directory foldername recursively. Prevent error messages from being shown.', 
																				'Add execute and read permissions to all users for the content in folder foldername recursively. Prevent error messages from being shown.',
																				'How can I give permission for all users to read and execute the all the content in the directory foldername, prevent error messages from being shown?',
																				'How can I give permission for all users to read and execute the all the content in the folder foldername, prevent error messages from being shown?',																		
																				'Give execute and read permissions for all the content in the directory foldername to all users. Prevent error messages from being shown.',
																				'Give execute and read permissions for all the content in the folder foldername to all users. Prevent error messages from being shown.',
																				'Grant read and execute permissions to all the content in the directory foldername to all the users. Prevent error messages from being shown.',																			
																				'Grant read and execute permissions to all the content in the folder foldername to all the users. Prevent error messages from being shown.']},ignore_index = True)

#This ends all combinations for ugo=rx

chmod = chmod.append({'Command': 'chmod g-w filename','NL Queries':['Remove permission for the group to write into file filename.', 
																				'How can I remove permissions to the group to make file filename non-writable?',	
																				'Prevent the group users from writing any changes to the file filename.',	
																				'How can I prevent the group users from writing any changes to the file filename?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c g-w filename','NL Queries':['Remove permission for the group to write into file filename. Generate a log if changes have been made to the file filename.', 
																				'How can I remove permissions to the group to make file filename non-writable and generate a log if changes have been made to the file?',	
																				'Prevent the group users from writing any changes to the file and generate a log if changes have been made to the file filename.',	
																				'How can I prevent the group users from writing any changes to the file filename and generate a log if the file has changed.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v g-w filename','NL Queries':['Remove permission for the group to write into file filename. generate a log.', 
																				'How can I remove permissions to the group to make file filename non-writable and generate a log?',	
																				'Prevent the group users from writing any changes to the file filename and generate a log.',	
																				'How can I prevent the group users from writing any changes to the file filename and generate a log?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f g-w filename','NL Queries':['Remove permission for the group to write into file filename. Prevent error messages from being shown.', 
																				'How can I remove permissions to the group to make file filename non-writable and prevent error messages from being shown?',	
																				'Prevent the group users from writing any changes to filename and prevent error messages from being shown.',	
																				'How can I prevent the group users from writing any changes to the file filename and prevent error messages from being shown?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf g-w filename','NL Queries':['Remove permission for the group to write into file filename. Generate a log and prevent the error messages from being shown.', 
																				'How can I remove permissions to the group to make file filename non-writable, generate a log and prevent the error messages from being shown?',	
																				'Prevent the group users from writing any changes to filename, generate a log and prevent the error messages from being shown.',	
																				'How can I prevent the group users from writing any changes to the file filename, generate a log and prevent the error messages from being shown?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf g-w filename','NL Queries':['Remove permission for the group to write into file filename. Generate a log if changes are made to the file and prevent the error messages from being shown.', 
																				'How can I remove permissions to the group to make it non-writable, generate a log if the changes are made to filename and prevent the error messages from being shown?',	
																				'Prevent the group users from writing any changes to filename, generate a log if changes are made to the file and prevent the error messages from being shown.',
																				'How can I prevent the group users from writing any changes to the file filename, generate a log if changes are made to the file and prevent the error messages from being shown?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf g-w foldername/','NL Queries':['Remove permission for the group to write into content of folder foldername. Generate a log if changes are made to the file and prevent the error messages from being shown.', 
																				'Remove permission for the group to write into content of directory foldername. Generate a log if changes are made to the file and prevent the error messages from being shown.', 
																				'How can I remove permissions to the group to make content of folder foldername non-writable, generate a log if the changes are made to the file and prevent the error messages from being shown?',
																				'How can I remove permissions to the group to make content of directory foldername non-writable, generate a log if the changes are made to the file and prevent the error messages from being shown?',	
																				'Prevent the group users from writing any changes to the content of folder foldername, generate a log if changes are made to the file and prevent the error messages from being shown.',	
																				'Prevent the group users from writing any changes to the content of directory foldername, generate a log if changes are made to the file and prevent the error messages from being shown.',	
																				'How can I prevent the group users from writing any changes to the content of the folder foldername, generate a log if changes are made to the file and prevent the error messages from being shown?',
																				'How can I prevent the group users from writing any changes to the content of the directory foldername, generate a log if changes are made to the file and prevent the error messages from being shown?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf g-w foldername/','NL Queries':['Remove permission for the group to write into content of folder foldername. Generate a log and prevent the error messages from being shown.', 
																				'Remove permission for the group to write into content of directory foldername. Generate a log and prevent the error messages from being shown.', 
																				'How can I remove permissions to the group to make content of folder foldername non-writable, generate a log and prevent the error messages from being shown?',
																				'How can I remove permissions to the group to make content of directory foldername non-writable, generate a log and prevent the error messages from being shown?',	
																				'Prevent the group users from writing any changes to the content of folder foldername, generate a log and prevent the error messages from being shown.',	
																				'Prevent the group users from writing any changes to the content of directory foldername, generate a log and prevent the error messages from being shown.',	
																				'How can I prevent the group users from writing any changes to the content of the folder foldername, generate a log and prevent the error messages from being shown?',
																				'How can I prevent the group users from writing any changes to the content of the directory foldername, generate a log and prevent the error messages from being shown?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv g-w foldername/','NL Queries':['Remove permission for the group to write into content of folder foldername. Generate a log.', 
																				'Remove permission for the group to write into content of directory foldername. Generate a log.', 
																				'How can I remove permissions to the group to make content of folder foldername non-writable, generate a log?',
																				'How can I remove permissions to the group to make content of directory foldername non-writable, generate a log?',	
																				'Prevent the group users from writing any changes to the content of folder foldername, generate a log.',	
																				'Prevent the group users from writing any changes to the content of directory foldername, generate a log.',	
																				'How can I prevent the group users from writing any changes to the content of the folder foldername, generate a log?',
																				'How can I prevent the group users from writing any changes to the content of the directory foldername, generate a log?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc g-w foldername/','NL Queries':['Remove permission for the group to write into content of folder foldername. Generate a log if changes are made to the file.', 
																				'Remove permission for the group to write into content of directory foldername. Generate a log if changes are made to the file.', 
																				'How can I remove permissions to the group to make content of folder foldername non-writable, generate a log if the changes are made to the file?',
																				'How can I remove permissions to the group to make content of directory foldername non-writable, generate a log if the changes are made to the file?',	
																				'Prevent the group users from writing any changes to the content of folder foldername, generate a log if changes are made to the file.',	
																				'Prevent the group users from writing any changes to the content of directory foldername, generate a log if changes are made to the file.',	
																				'How can I prevent the group users from writing any changes to the content of the folder foldername, generate a log if changes are made to the file?',
																				'How can I prevent the group users from writing any changes to the content of the directory foldername, generate a log if changes are made to the file?']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf g-w foldername/','NL Queries':['Remove permission for the group to write into content of folder foldername. Prevent the error messages from being shown.', 
																				'Remove permission for the group to write into content of directory foldername. Prevent the error messages from being shown.', 
																				'How can I remove permissions to the group to make content of folder foldername non-writable, prevent the error messages from being shown?',
																				'How can I remove permissions to the group to make content of directory foldername non-writable, prevent the error messages from being shown?',	
																				'Prevent the group users from writing any changes to the content of folder foldername, prevent the error messages from being shown.',	
																				'Prevent the group users from writing any changes to the content of directory foldername, prevent the error messages from being shown.',	
																				'How can I prevent the group users from writing any changes to the content of the folder foldername, prevent the error messages from being shown?',
																				'How can I prevent the group users from writing any changes to the content of the directory foldername, prevent the error messages from being shown?']},ignore_index = True)

#This ends all combinations for g-w

chmod = chmod.append({'Command': 'chmod 600 filename','NL Queries':['Restore default permission state to user to read and write but removes permission for other users for the file filename to read and write.', 
																				'How can I revert the permissions to the original state to give only the owner read and write access to the file filename?',											
																				'Revert to the default permissions state for the file filename.', 
																				'Give the file filename its default permissions.',
																				'Provide only read and write permissions to the owner of the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 600 filename','NL Queries':['Restore default permission state to user to read and write but removes permission for other users to read and write for the file filename. Generate a log if changes are made to the file.', 
																				'How can I revert the permissions to the original state to give only the owner access to the file filename and generate a log if changes are made to the file?',											
																				'Revert to the default permissions state of the file filename and generate a log if changes are made to the file.', 
																				'Give the file filename its default permissions and generate a log if changes are made to the file.',
																				'Provide only read and write permissions to the owner of the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 600 filename','NL Queries':['Restore default permission state to user to read and write but removes permission for other users to read and write for the file filename. Generate a log.', 
																				'How can I revert the permissions to the original state to give only the owner access to the file filename and generate a log?',											
																				'Revert to the default permissions state of the file filename and generate a log.', 
																				'Give the file filename its default permissions and generate a log.',
																				'Provide only read and write permissions to the owner of the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 600 filename','NL Queries':['Restore default permission state to user to read and write but removes permission for other users to read and write for the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I revert the permissions to the original state to give only the owner access to the file filename, generate a log and prevent error messages from being shown?',											
																				'Revert to the default permissions state of the file filename, generate a log and prevent error messages from being shown.', 
																				'Give the file filename its default permissions, generate a log and prevent error messages from being shown.',
																				'Provide only read and write permissions to the owner of the file filename, generate a log and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 600 filename','NL Queries':['Restore default permission state to user to read and write but removes permission for other users to read and write for the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I revert the permissions to the original state to give only the owner access to the file filename, generate a log if changes are made to the file and prevent error messages from being shown?',											
																				'Revert to the default permissions state of the file filename, generate a log if changes are made to the file and prevent error messages from being shown.', 
																				'Give the file filename its default permissions, generate a log if changes are made to the file and prevent error messages from being shown.',
																				'Provide only read and write permissions to the owner of the file filename, generate a log if changes are made to the file and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 600 filename','NL Queries':['Restore default permission state to user to read and write but removes permission for other users to read and write for the file filename. Prevent error messages from being shown.', 
																				'How can I revert the permissions to the original state to give only the owner access to the file filename, prevent error messages from being shown?',											
																				'Revert to the default permissions state of the file filename, prevent error messages from being shown.', 
																				'Give the file filename its default permissions, prevent error messages from being shown.',
																				'Provide only read and write permissions to the owner of the file filename, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 600 foldername/','NL Queries':['Restore default permission state of user to read and write but removes permission for other users to read and write for all the content in the folder foldername. Prevent error messages from being shown.', 
																				'Restore default permission state of user to read and write but removes permission for other users to read and write for all the content in the directory foldername. Prevent error messages from being shown.',
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the directory foldername, prevent error messages from being shown?',	
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the folder foldername, prevent error messages from being shown?',										
																				'Revert to the default permissions state for all the content in the folder foldername, prevent error messages from being shown.', 
																				'Revert to the default permissions state for all the content in the directory foldername, prevent error messages from being shown.', 
																				'Give the content in the folder foldername its default permissions, prevent error messages from being shown.',							
																				'Give the content in the directory foldername its default permissions, prevent error messages from being shown.',
																				'Provide only read and write permissions to the owner of the content in the folder foldername, prevent error messages from being shown during execution',					
																				'Provide only read and write permissions to the owner of the content in the directory foldername, prevent error messages from being shown during execution']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 600 foldername/','NL Queries':['Restore default permission state of user to read and write but removes permission for other users to read and write for all the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'Restore default permission state of user to read and write but removes permission for other users to read and write for all the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.',
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file?',	
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file?',										
																				'Revert to the default permissions state for all the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.', 
																				'Revert to the default permissions state for all the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.', 
																				'Give the content in the folder foldername its default permissions, prevent error messages from being shown and generate a log if changes are made to the file.',							
																				'Give the content in the directory foldername its default permissions, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Provide only read and write permissions to the owner of the content in the folder foldername, prevent error messages from being shown during execution and generate a log if changes are made to the file.',					
																				'Provide only read and write permissions to the owner of the content in the directory foldername, prevent error messages from being shown during execution and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 600 foldername/','NL Queries':['Restore default permission state to user to read and write but removes permission for other users to read and write for all the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'Restore default permission state to user to read and write but removes permission for other users to read and write for all the content in the directory foldername. Generate a log. Prevent error messages from being shown.',
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the directory foldername, prevent error messages from being shown and generate a log?',	
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the folder foldername, prevent error messages from being shown and generate a log?',										
																				'Revert to the default permissions state for all the content in the folder foldername, prevent error messages from being shown and generate a log.', 
																				'Revert to the default permissions state for all the content in the directory foldername, prevent error messages from being shown and generate a log.', 
																				'Give the content in the folder foldername its default permissions, prevent error messages from being shown and generate a log.',							
																				'Give the content in the directory foldername its default permissions, prevent error messages from being shown and generate a log.',
																				'Provide only read and write permissions to the owner of the content in the folder foldername, prevent error messages from being shown during execution and generate a log.',					
																				'Provide only read and write permissions to the owner of the content in the directory foldername, prevent error messages from being shown during execution and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 600 foldername/','NL Queries':['Restore default permission state to user to read and write but removes permission for other users to read and write for all the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'Restore default permission state to user to read and write but removes permission for other users to read and write for all the content in the directory foldername. Generate a log if changes are made to the file.',
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the directory foldername, generate a log if changes are made to the file?',	
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the folder foldername, generate a log if changes are made to the file?',										
																				'Revert to the default permissions state for all the content in the folder foldername, generate a log if changes are made to the file.', 
																				'Revert to the default permissions state for all the content in the directory foldername, generate a log if changes are made to the file.', 
																				'Give the content in the folder foldername its default permissions, generate a log if changes are made to the file.',							
																				'Give the content in the directory foldername its default permissions, generate a log if changes are made to the file.',
																				'Provide only read and write permissions to the owner of the content in the folder foldername, generate a log if changes are made to the file.',					
																				'Provide only read and write permissions to the owner of the content in the directory foldername, generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 600 foldername/','NL Queries':['Restore default permission state to user to read and write but removes permission for other users to read and write for all the content in the folder foldername. Generate a log.', 
																				'Restore default permission state to user to read and write but removes permission for other users to read and write for all the content in the directory foldername. Generate a log.',
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the directory foldername, generate a log?',	
																				'How can I revert the permissions to the original state to give only the owner access to all the content in the folder foldername, generate a log?',										
																				'Revert to the default permissions state for all the content in the folder foldername, generate a log.', 
																				'Revert to the default permissions state for all the content in the directory foldername, generate a log.', 
																				'Give the content in the folder foldername its default permissions, generate a log.',							
																				'Give the content in the directory foldername its default permissions, generate a log.',
																				'Provide only read and write permissions to the owner of the content in the folder foldername, generate a log.',					
																				'Provide only read and write permissions to the owner of the content in the directory foldername, generate a log.']},ignore_index = True)

#This ends all combinations for 600

chmod = chmod.append({'Command': 'chmod a-x filename','NL Queries':['Remove execute permissions for everyone for the file filename.', 
																	'How can I remove execute permissions for all users for the file filename?',																			
																	'Restrict execute action for all users to the file filename.',
																	'Prevent execution of the file filename by all users.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c a-x filename','NL Queries':['Remove execute permissions for everyone for the file filename. Generate a log if changes are made to the file.', 
																				'How can I remove execute permissions for all users for the file filename and generate a log if changes are made to the file?',																			
																				'Restrict execute action for all users to the file filename and generate a log if changes are made to the file.',
																				'Prevent execution of the file filename by all users and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v a-x filename','NL Queries':['Remove execute permissions for everyone for the file filename. Generate a log.', 
																				'How can I remove execute permissions for all users for the file filename and generate a log?',																			
																				'Restrict execute action for all users to the file filename and generate a log.',
																				'Prevent execution of the file filename by all users and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f a-x filename','NL Queries':['Remove execute permissions for everyone for the file filename. Prevent error messages from being shown.', 
																				'How can I remove execute permissions for all users for the file filename and prevent error messages from being shown?',																			
																				'Restrict execute action for all users to the file filename and prevent error messages from being shown.',
																				'Prevent execution of the file filename by all users and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf a-x filename','NL Queries':['Remove execute permissions for everyone. Prevent error messages from being shown and generate a log if changes are made to the file.', 
																				'How can I remove execute permissions for all users for the file filename, prevent error messages from being shown and generate a log if changes are made to the file?',																			
																				'Restrict execute action for all users to the file filename, generate a log if changes are made to the file and prevent error messages from being shown.',
																				'Prevent execution of the file filename by all users, generate a log if changes are made to the file and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf a-x filename','NL Queries':['Remove execute permissions for everyone for the file filename. Prevent error messages from being shown and generate a log.', 
																				'How can I remove execute permissions for all users for the file filename, prevent error messages from being shown and generate a log?',																			
																				'Restrict execute action for all users to the file filename, generate a log and prevent error messages from being shown.',
																				'Prevent execution of the file filename by all users, generate a log and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf a-x foldername/','NL Queries':['Remove execute permissions for everyone for the content in the folder foldername. Prevent error messages from being shown and generate a log.', 		
																				'Remove execute permissions for everyone for the content in the directory foldername. Prevent error messages from being shown and Generate a log.',
																				'How can I remove execute permissions for all users for all the content in the folder foldername, prevent error messages from being shown and generate a log?',		
																				'How can I remove execute permissions for all users for all the content in the directory foldername, prevent error messages from being shown and generate a log?',
																				'Restrict execute action for all users for all the content in the folder foldername, generate a log and prevent error messages from being shown.',
																				'Restrict execute action for all users for all the content in the directory foldername, generate a log and prevent error messages from being shown.',
																				'Prevent execution of content in the folder foldername by all users, generate a log and prevent error messages from being shown.',
																				'Prevent execution of content in the directory foldername by all users, generate a log and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf a-x foldername/','NL Queries':['Remove execute permissions for everyone for the content in the folder foldername. Prevent error messages from being shown and generate a log if changes are made to the file.', 		
																				'Remove execute permissions for everyone for the content in the directory foldername. Prevent error messages from being shown and Generate a log if changes are made to the file.',
																				'How can I remove execute permissions for all users for all the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file?',		
																				'How can I remove execute permissions for all users for all the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Restrict execute action for all users for all the content in the folder foldername, generate a log if changes are made to the file and prevent error messages from being shown.',
																				'Restrict execute action for all users for all the content in the directory foldername, generate a log if changes are made to the file and prevent error messages from being shown.',
																				'Prevent execution of content in the folder foldername by all users, generate a log if changes are made to the file and prevent error messages from being shown.',
																				'Prevent execution of content in the directory foldername by all users, generate a log if changes are made to the file and prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv a-x foldername/','NL Queries':['Remove execute permissions for everyone for the content in the folder foldername. Generate a log.', 		
																				'Remove execute permissions for everyone for the content in the directory foldername. Generate a log.',
																				'How can I remove execute permissions for all users for all the content in the folder foldername, generate a log?',		
																				'How can I remove execute permissions for all users for all the content in the directory foldername, generate a log?',
																				'Restrict execute action for all users for all the content in the folder foldername, generate a log.',
																				'Restrict execute action for all users for all the content in the directory foldername, generate a log.',
																				'Prevent execution of content in the folder foldername by all users, generate a log.',
																				'Prevent execution of content in the directory foldername by all users, generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc a-x foldername/','NL Queries':['Remove execute permissions for everyone for the content in the folder foldername. Generate a log if changes are made to the file.', 		
																				'Remove execute permissions for everyone for the content in the directory foldername. Generate a log if changes are made to the file.',
																				'How can I remove execute permissions for all users for all the content in the folder foldername, generate a log if changes are made to the file?',		
																				'How can I remove execute permissions for all users for all the content in the directory foldername, generate a log if changes are made to the file?',
																				'Restrict execute action for all users for all the content in the folder foldername, generate a log if changes are made to the file.',
																				'Restrict execute action for all users for all the content in the directory foldername, generate a log if changes are made to the file.',
																				'Prevent execution of content in the folder foldername by all users, generate a log if changes are made to the file.',
																				'Prevent execution of content in the directory foldername by all users, generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf a-x foldername/','NL Queries':['Remove execute permissions for everyone for the content in the folder foldername. Prevent error messages from being shown.', 		
																				'Remove execute permissions for everyone for the content in the directory foldername. Prevent error messages from being shown.',
																				'How can I remove execute permissions for all users for all the content in the folder foldername, prevent error messages from being shown?',		
																				'How can I remove execute permissions for all users for all the content in the directory foldername, prevent error messages from being shown?',
																				'Restrict execute action for all users for all the content in the folder foldername, prevent error messages from being shown.',
																				'Restrict execute action for all users for all the content in the directory foldername, prevent error messages from being shown.',
																				'Prevent execution of content in the folder foldername by all users, prevent error messages from being shown.',
																				'Prevent execution of content in the directory foldername by all users, prevent error messages from being shown.']},ignore_index = True)

#This ends all possible combinations for a-x

chmod = chmod.append({'Command': 'chmod 700 filename','NL Queries':['Give permission such that only the owner of the file filename can have full access and all permissions to it.', 
																	'How can I provide full access and all permissions to the file filename only to the owner?', 
																	'Make the file filename private and accessible to the person who created it along with all permissions.',
																	'Give exclusive access to the owner to the file filename along with all permissions.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 700 filename','NL Queries':['Give permission such that only the owner of the file filename can have full access it and all permissions to it and generate a log if changes are made to the file.', 
																				'How can I give full access and all permissions to the file filename only to the owner and generate a log if changes are made to the file?', 
																				'Make the file filename private and accessible to the person who created it along with all the permissions and generate a log if changes are made to the file.',
																				'Give exclusive access to the owner to the file filename along with all permissions and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 700 filename','NL Queries':['Give permission such that only the owner of the file filename can have full access and all permissions to it. Generate a log.', 
																			'How can I give full access and all permissions to the file filename only to the owner and generate a log?', 
																			'Make the file filename private and accessible to the person who created it along with all permissions and generate a log.',
																			'Give exclusive access to the owner to the file filename along with all permissions and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 700 filename','NL Queries':['Give permission such that only the owner of the file filename can access it and all permissions to it, prevent error messages from being shown and generate a log.', 
																				'How can I give full access along with all permissions to the file filename only to the owner, prevent error messages from being shown and generate a log?', 
																				'Make the file filename private and accessible to the person who created it along with all permissions, prevent error messages from being shown and Generate a log.',
																				'Give exclusive access to the owner to the file filename along with all permissions, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 700 filename','NL Queries':['Give permission such that only the owner of the file filename can access it and all rights to it, prevent error messages from being shown and generate a log if changes are made to the file.', 
																				'How can I give full access to the file filename with all permissions only to the owner, prevent error messages from being shown and generate a log if changes are made to the file?', 
																				'Make the file filename private and accessible to the person who created it along with all permissions, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give exclusive access to the owner to the file filename along with all permissions, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 700 filename','NL Queries':['Give permission such that only the owner of the file filename can access it and all rights to it, prevent error messages from being shown.', 
																				'How can I give full access to the file filename with all permissions only to the owner, prevent error messages from being shown?', 
																				'Make the file filename private and accessible to the person who created it along with all permissions, prevent error messages from being shown.',
																				'Give exclusive access to the owner to the file filename along with all permissions, prevent error messages from being shown.']},ignore_index = True)		

chmod = chmod.append({'Command': 'chmod -Rvf 700 foldername/','NL Queries':['Only the owner of the content in the folder foldername can access and have all rights to it, prevent error messages from being shown and generate a log.', 
																				'How can I give full access along with all permissions to the content in the folder foldername only to the user, prevent error messages from being shown and generate a log?', 
																				'Make the content in the folder foldername private and accessible to the person who created it, prevent error messages from being shown and generate a log.',
																				'Give exclusive access and all permissions to the owner to the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Only the owner of the content in the directory foldername can access and have all rights to them, prevent error messages from being shown and generate a log.', 
																				'How can I provide full access and all permissions to the content in the directory foldername only to the user, prevent error messages from being shown and generate a log?', 
																				'Make the content in the directory foldername private and accessible along with all permissions to the person who created it, prevent error messages from being shown and generate a log.',
																				'Give exclusive access along with all permissions to the owner to the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 700 foldername/','NL Queries':['Only the owner of the content in the folder foldername can access and have all permissions to it, prevent error messages from being shown and Generate a log if changes are made to the file.', 
																				'How can I provide full access along with all permissions to the content in the folder foldername only to the user, prevent error messages from being shown and generate a log if changes are made to the file?', 
																				'Make the content in the folder foldername private and accessible along with all permissions to the person who created it, prevent error messages from being shown and Generate a log if changes are made to the file.',
																				'Give exclusive access and all rights to the owner to the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Only the owner of the content in the directory foldername can access and have all rights to them, prevent error messages from being shown and Generate a log if changes are made to the file.', 
																				'How can I give full access along with all permissions to the content in the directory foldername only to the user, prevent error messages from being shown and Generate a log if changes are made to the file?', 
																				'Make the content in the directory foldername private and accessible  with all permissions to the person who created it, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give exclusive access along with all permissions to the owner to the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 700 foldername/','NL Queries':['Only the owner of the content in the folder foldername can access and have all permissions to it, generate a log if changes are made to the file.', 
																				'How can I povide full access along with all permissions to the content in the folder foldername only to the user and generate a log if changes are made to the file?', 
																				'Make the content in the folder foldername private and accessible with all rights to the person who created it and generate a log if changes are made to the file.',
																				'Give exclusive access along with all permissions to the owner to the content in the folder foldername and generate a log if changes are made to the file.',
																				'Only the owner of the content in the directory foldername can access and have all permissions to them and generate a log if changes are made to the file.', 
																				'How can I provide full access along with all permissions to the content in the directory foldername only to the user and generate a log if changes are made to the file?', 
																				'Make the content in the directory foldername private and accessible along with all the rights to the person who created it and generate a log if changes are made to the file.',
																				'Give exclusive access along with all permissions to the owner to the content in the directory foldername and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 700 foldername/','NL Queries':['Only the owner of the content in the folder foldername can access and have all permissions to them, prevent error messages from being shown.', 
																				'How can I provide full access along with all rights to the content in the folder foldername only to the user, prevent error messages from being shown?', 
																				'Make the content in the folder foldername private and accessible along with all the rights to the person who created it, prevent error messages from being shown.',
																				'Give exclusive access along with all permissions to the owner to the content in the folder foldername, prevent error messages from being shown.',
																				'Only the owner of the content in the directory foldername can access and have all rights to them, prevent error messages from being shown.', 
																				'How can I provide full access along with all permissions to the content in the directory foldername only to the user, prevent error messages from being shown?', 
																				'Make the content in the directory foldername private and accessible along with all permissions to the person who created them, prevent error messages from being shown.',
																				'Give exclusive access along with all permissions to the owner to the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 700 foldername/','NL Queries':['Only the owner of the content in the folder foldername can access and have all permissions to them and generate a log.', 
																				'How can I provide full access along with all the permissions to the content in the folder foldername only to the user? Generate a log.',
																				'Make the content in the folder foldername private and accessible along with all permissions to the person who created it and generate a log.',
																				'Give exclusive access along with all permissions to the owner to the content in the folder foldername and generate a log.',
																				'Only the owner of the content in the directory foldername can access them and have all permissions. Generate a log.', 
																				'How can I fgive ull access along with all permissions to the content in the directory foldername only to the user and generate a log?', 
																				'Make the content in the directory foldername private and accessible along with all permissions to the person who created it and generate a log.',
																				'Give exclusive access along with all permissions to the owner to the content in the directory foldername and generate a log.']},ignore_index = True)

# This ends all combinations for 700
chmod = chmod.append({'Command': 'chmod 477 filename','NL Queries':['Give permission to the group and non group members users to read, write and execute the file filename but only read access to the user who owns it.'
																				'How do I give all permissions to the file filename to group members and non group members but read access to the person who owns it?',
																				'Make group and non group users have full access to the file filename and read access to the person who owns the file.',
																				'Only the group and non group users will be able to have full access to the file filename while the user who owns the file will have only read access.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 477 filename','NL Queries':['Give permission to all users to read, write and execute the file filename to the group and non group members but only read access to the user who owns it. Generate a log if changes are made to the file.'
																				'How do I give all permission to the file filename to group members and non group members but read access to the person who owns it and generate a log if changes are made to the file?',
																				'Make group and non group users have full access to the file filename and read access to the person who owns it and generate a log if changes are made to the file.',
																				'Only the group and non group users will be able to have full access to the file filename while the user who owns it will have only read access and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 477 filename','NL Queries':['Give permission to all users to read, write and execute the file filename to the group and non group members but only read access to the user executing it. generate a log.'
																				'How do I give all permission to the file filename to group members and non group members but read access to the person executing it and generate a log?',
																				'Make group and non group users have full access to the file filename and execute access to the person executing the command and generate a log.',
																				'Only the group and non group users will be able to have full access to the file filename while the user executing the command will have only read access and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 477 filename','NL Queries':['Give permission to all users to read, write and execute the file filename to the group and non group members but only read access to the user executing it. Generate a log if changes are made to the file. Prevent error messages from being shown.'
																				'How do I give all permission to the file filename to group members and non group members but read access to the person executing it, prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make group and non group users have full access to the file filename and execute access to the person executing the command, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Only the group and non group users will be able to have full access to the file filename while the user executing the command will have only read access, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 477 filename','NL Queries':['Give permission to all users to read, write and execute the file filename to the group and non group members but only read access to the user executing it. Generate a log. Prevent error messages from being shown.'
																				'How do I give all permission to the file filename to group members and non group members but read access to the person executing it, prevent error messages from being shown and generate a log?',
																				'Make group and non group users have full access to the file filename and execute access to the person executing the command, prevent error messages from being shown and generate a log.',
																				'Only the group and non group users will be able to have full access to the file filename while the user executing the command will have only read access, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 477 filename','NL Queries':['Give permission to all users to read, write and execute the file filename to the group and non group members but only read access to the user executing it. Prevent error messages from being shown.'
																				'How do I give all permission to the file filename to group members and non group members but read access to the person executing it and prevent error messages from being shown?',
																				'Make group and non group users have full access to the file filename and execute access to the person executing the command, prevent error messages from being shown.',
																				'Only the group and non group users will be able to have full access to the file filename while the user executing the command will have only read access, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 477 foldername/','NL Queries':['Give permission to all users to read, write and execute the contents in the folder foldername to the group and non group members but only read access to the user executing it. Generate a log if changes are made to the file. Prevent error messages from being shown.'
																				'How do I give all permission to the contents in the folder foldername to group members and non group members but read access to the person executing it, prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make group and non group users have full access to the contents in the folder foldername and execute access to the person executing the command, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Only the group and non group users will be able to have full access to the contents in the folder foldername while the user executing the command will have only read access, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give permission to all users to read, write and execute the contents in the directory foldername to the group and non group members but only read access to the user executing it. Generate a log if changes are made to the file. Prevent error messages from being shown.'
																				'How do I give all permission to the contents in the directory foldername to group members and non group members but read access to the person executing it, prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make group and non group users have full access to the contents in the directory foldername and execute access to the person executing the command, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Only the group and non group users will be able to have full access to the contents in the directory foldername while the user executing the command will have only read access, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 477 foldername/','NL Queries':['Give permission to all users to read, write and execute the content in the folder foldername to the group and non group members but only read access to the user executing it. Generate a log. Prevent error messages from being shown.'
																				'How do I give all permission to the content in the folder foldername to group members and non group members but read access to the person executing it, prevent error messages from being shown and generate a log?',
																				'Make group and non group users have full access to the content in the folder foldername and execute access to the person executing the command, prevent error messages from being shown and generate a log.',
																				'Only the group and non group users will be able to have full access to the content in the folder foldername while the user executing the command will have only read access, prevent error messages from being shown and generate a log.',
																				'Give permission to all users to read, write and execute the content in the directory foldername to the group and non group members but only read access to the user executing it. Generate a log. Prevent error messages from being shown.'
																				'How do I give all permission to the content in the directory foldername to group members and non group members but read access to the person executing it, prevent error messages from being shown and generate a log?',
																				'Make group and non group users have full access to the content in the directory foldername and execute access to the person executing the command, prevent error messages from being shown and generate a log.',
																				'Only the group and non group users will be able to have full access to the content in the directory foldername while the user executing the command will have only read access, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 477 foldername/','NL Queries':['Give permission to all users to read, write and execute the content in the folder foldername to the group and non group members but only read access to the user executing it. Generate a log if changes are made to the file.'
																				'How do I give all permission to the content in the folder foldername to group members and non group members but read access to the person executing it, generate a log if changes are made to the file?',
																				'Make group and non group users have full access to the content in the folder foldername and execute access to the person executing the command, generate a log if changes are made to the file.',
																				'Only the group and non group users will be able to have full access to the content in the folder foldername while the user executing the command will have only read access, generate a log if changes are made to the file.',
																				'Give permission to all users to read, write and execute the content in the directory foldername to the group and non group members but only read access to the user executing it. Generate a log if changes are made to the file.'
																				'How do I give all permission to the content in the directory foldername to group members and non group members but read access to the person executing it, generate a log if changes are made to the file?',
																				'Make group and non group users have full access to the content in the directory foldername and execute access to the person executing the command, generate a log if changes are made to the file.',
																				'Only the group and non group users will be able to have full access to the content in the directory foldername while the user executing the command will have only read access, generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 477 foldername/','NL Queries':['Give permission to all users to read, write and execute the content in the folder foldername to the group and non group members but only read access to the user executing it. Generate a log.'
																				'How do I give all permission to the content in the folder foldername to group members and non group members but read access to the person executing it, generate a log?',
																				'Make group and non group users have full access to the content in the folder foldername and execute access to the person executing the command, generate a log.',
																				'Only the group and non group users will be able to have full access to the content in the folder foldername while the user executing the command will have only read access, generate a log.',
																				'Give permission to all users to read, write and execute the content in the directory foldername to the group and non group members but only read access to the user executing it. Generate a log.'
																				'How do I give all permission to the content in the directory foldername to group members and non group members but read access to the person executing it, generate a log?',
																				'Make group and non group users have full access to the content in the directory foldername and execute access to the person executing the command, generate a log.',
																				'Only the group and non group users will be able to have full access to the content in the directory foldername while the user executing the command will have only read access, generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 477 foldername/','NL Queries':['Give permission to all users to read, write and execute the content in the folder foldername to the group and non group members but only read access to the user executing it. Prevent error messages from being shown.'
																				'How do I give all permission to the content in the folder foldername to group members and non group members but read access to the person executing it, prevent error messages from being shown?',
																				'Make group and non group users have full access to the content in the folder foldername and execute access to the person executing the command, prevent error messages from being shown.',
																				'Only the group and non group users will be able to have full access to the content in the folder foldername while the user executing the command will have only read access, prevent error messages from being shown.',
																				'Give permission to all users to read, write and execute the content in the directory foldername to the group and non group members but only read access to the user executing it. Prevent error messages from being shown.'
																				'How do I give all permission to the content in the directory foldername to group members and non group members but read access to the person executing it, prevent error messages from being shown?',
																				'Make group and non group users have full access to the content in the directory foldername and execute access to the person executing the command, prevent error messages from being shown.',
																				'Only the group and non group users will be able to have full access to the content in the directory foldername while the user executing the command will have only read access, prevent error messages from being shown.']},ignore_index = True)

#This ends all combinations for 477

chmod = chmod.append({'Command': 'chmod 777 filename','NL Queries':['Give permission to all users to read, write and execute the file filename.', 
																				'How can I give full access to the file filename to all users?',
																				'Make all users have full access to the file filename.',
																				'All the users will have full access to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 777 filename','NL Queries':['Give permission to all users to read, write and execute the file filename. Generate a log if changes are made to the file.', 
																				'How can I give full access to the file filename to all users and generate a log if changes are made to the file?',
																				'Make all users have full access to the file filename and generate a log if changes are made to the file.',
																				'All the users will have full access to the file filename and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 777 filename','NL Queries':['Give permission to all users to read, write and execute the file filename. Generate a log.', 
																				'How can I give full access to the file filename to all users and generate a log?',
																				'Make all users have full access to the file filename and generate a log.',
																				'All the users will have full access to the file filename and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 777 filename','NL Queries':['Give permission to all users to read, write and execute the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to all users and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make all users have full access to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'All the users will have full access to the file filename, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 777 filename','NL Queries':['Give permission to all users to read, write and execute the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to all users and prevent error messages from being shown and generate a log?',
																				'Make all users have full access to the file filename, prevent error messages from being shown and generate a log.',
																				'All the users will have full access to the file filename, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 777 filename','NL Queries':['Give permission to all users to read, write and execute the file filename. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to all users. Don\'t show error messages?',
																				'Make all users have full access to the file filename without any error messages.',
																				'All the users will have full access to the file filename and no error messages are displayed.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 777 foldername/','NL Queries':['Give permission to all users to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to all users and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make all users have full access to the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'All the users will have full access to the content in the folder foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.',
																				'Give permission to all users to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to all users and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make all users have full access to the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'All the users will have full access to the content in the directory foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 777 foldername/','NL Queries':['Give permission to all users to read, write and execute the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to all users and prevent error messages from being shown and generate a log?',
																				'Make all users have full access to the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'All the users will have full access to the content in the folder foldername, error messages are prevented from being shown and a log is generated.',
																				'Give permission to all users to read, write and execute the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to all users and prevent error messages from being shown and generate a log?',
																				'Make all users have full access to the content in the directory foldername, prevent error messages from being shown and generate a log.',
																				'All the users will have full access to the content in the directory foldername, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 777 foldername/','NL Queries':['Give permission to all users to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the content in the folder foldername to all users and generate a log if changes are made to the file?',
																				'Make all users have full access to the content in the folder foldername, generate a log if changes are made to the file.',
																				'All the users will have full access to the content in the folder foldername, a log is generated if changes are made to the file.',
																				'Give permission to all users to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the content in the directory foldername to all users and generate a log if changes are made to the file?',
																				'Make all users have full access to the content in the directory foldername, generate a log if changes are made to the file.',
																				'All the users will have full access to the content in the directory foldername, a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 777 foldername/','NL Queries':['Give permission to all users to read, write and execute the content in the folder foldername. Generate a log.', 
																				'How can I give full access to the content in the folder foldername to all users and generate a log?',
																				'Make all users have full access to the content in the folder foldername, generate a log.',
																				'All the users will have full access to the content in the folder foldername, a log is generated.',
																				'Give permission to all users to read, write and execute the content in the directory foldername. Generate a log.', 
																				'How can I give full access to the content in the directory foldername to all users and generate a log?',
																				'Make all users have full access to the content in the directory foldername, generate a log.',
																				'All the users will have full access to the content in the directory foldername, a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 777 foldername/','NL Queries':['Give permission to all users to read, write and execute the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to all users and prevent error messages from being shown?',
																				'Make all users have full access to the content in the folder foldername, prevent error messages from being shown.',
																				'All the users will have full access to the content in the folder foldername, error messages are prevented from being shown.',
																				'Give permission to all users to read, write and execute the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to all users and prevent error messages from being shown?',
																				'Make all users have full access to the content in the directory foldername, prevent error messages from being shown.',
																				'All the users will have full access to the content in the directory foldername, error messages are prevented from being shown.']},ignore_index = True)

#This ends all combinations for 777

chmod = chmod.append({'Command': 'chmod 700 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename.', 
																				'How can I give full access to the file filename to the owner?',
																				'Make the owner have full access to the file filename.',
																				'Command so that owner will have full access to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 700 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename. Generate a log if changes are made to the file.', 
																				'How can I give full access to the file filename to the owner and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename and generate a log if changes are made to the file.',
																				'Command so that the owner will have full access to the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 700 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename. Generate a log.', 
																				'How can I give full access to the file filename to the owner and generate a log?',
																				'Make the owner have full access to the file filename and generate a log.',
																				'The owner will have full access to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 700 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 700 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access to the file filename, prevent error messages from being shown and generate a log.',
																				'The owner will have full access to the file filename, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 700 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner without displaying any errors?',
																				'Make the owner have full access to the file filename. Don\'t show any errors.',
																				'The owner will have full access to the file filename. No error messages should be displayed.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 700 foldername/','NL Queries':['Give permission to the owner to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to the owner and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access to the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access to the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give permission to the owner to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to the owner and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access to the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access to the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 700 foldername/','NL Queries':['Give permission to the owner to read, write and execute the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to the owner and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access to the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access to the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Give permission to the owner to read, write and execute the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to the owner and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access to the content in the directory foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access to the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 700 foldername/','NL Queries':['Give permission to the owner to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the content in the folder foldername to the owner and generate a log if changes are made to the file?',
																				'Make the owner have full access to the content in the folder foldername, generate a log if changes are made to the file.',
																				'The owner will have full access to the content in the folder foldername, generate a log if changes are made to the file.',
																				'Give permission to the owner to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the content in the directory foldername to the owner and generate a log if changes are made to the file?',
																				'Make the owner have full access to the content in the directory foldername, generate a log if changes are made to the file.',
																				'The owner will have full access to the content in the directory foldername, generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 700 foldername/','NL Queries':['Give permission to the owner to read, write and execute the content in the folder foldername. Generate a log.', 
																				'How can I give full access to the content in the folder foldername to the owner and generate a log?',
																				'Make the owner have full access to the content in the folder foldername, generate a log.',
																				'The owner will have full access to the content in the folder foldername, generate a log.',
																				'Give permission to the owner to read, write and execute the content in the directory foldername. Generate a log.', 
																				'How can I give full access to the content in the directory foldername to the owner and generate a log?',
																				'Make the owner have full access to the content in the directory foldername, generate a log.',
																				'The owner will have full access to the content in the directory foldername, generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 700 foldername/','NL Queries':['Give permission to the owner to read, write and execute the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to the owner and prevent error messages from being shown?',
																				'Make the owner have full access to the content in the folder foldername, prevent error messages from being shown.',
																				'The owner will have full access to the content in the folder foldername, prevent error messages from being shown.',
																				'Give permission to the owner to read, write and execute the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to the owner and prevent error messages from being shown?',
																				'Make the owner have full access to the content in the directory foldername, prevent error messages from being shown.',
																				'The owner will have full access to the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

#This ends all combinations for 700

chmod = chmod.append({'Command': 'chmod 070 filename','NL Queries':['Give permission to all users of the group to read, write and execute the file filename.', 
																				'How can I give full access to the file filename to all users of the group?',
																				'Make all users of the group have full access to the file filename.',
																				'All the users of the group will have full access to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 070 filename','NL Queries':['Give permission to all users of the group to read, write and execute the file filename. Generate a log if changes are made to the file.', 
																				'How can I give full access to the file filename to all users of the group and generate a log if changes are made to the file?',
																				'Make all users of the group have full access to the file filename and generate a log if changes are made to the file.',
																				'All the users of the group will have full access to the file filename and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 070 filename','NL Queries':['Give permission to all users of the group to read, write and execute the file filename. Generate a log.', 
																				'How can I give full access to the file filename to all users of the group and generate a log?',
																				'Make all users of the group have full access to the file filename and generate a log.',
																				'All the users of the group will have full access to the file filename and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 070 filename','NL Queries':['Give permission to all users of the group to read, write and execute the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to all users of the group and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make all users of the group have full access to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'All the users of the group will have full access to the file filename, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 070 filename','NL Queries':['Give permission to all users of the group to read, write and execute the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to all users of the group and prevent error messages from being shown and generate a log?',
																				'Make all users of the group have full access to the file filename, prevent error messages from being shown and generate a log.',
																				'All the users of the group will have full access to the file filename, prevent error messages from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 070 filename','NL Queries':['Give permission to all users of the group to read, write and execute the file filename. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to all users of the group and generate a log?',
																				'Make all users of the group have full access to the file filename and generate a log.',
																				'All the users of the group will have full access to the file filename and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 070 foldername/','NL Queries':['Give permission to all users of the group to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to all users of the group and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make all users of the group have full access to the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'All the users of the group will have full access to the content in the folder foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.',
																				'Give permission to all users of the group to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to all users of the group and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make all users of the group have full access to the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'All the users of the group will have full access to the content in the directory foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 070 foldername/','NL Queries':['Give permission to all users of the group to read, write and execute the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to all users of the group and prevent error messages from being shown and generate a log?',
																				'Make all users of the group have full access to the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'All the users of the group will have full access to the content in the folder foldername, error messages are prevented from being shown and a log is generated.',
																				'Give permission to all users of the group to read, write and execute the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to all users of the group and prevent error messages from being shown and generate a log?',
																				'Make all users of the group have full access to the content in the directory foldername, prevent error messages from being shown and generate a log.',
																				'All the users of the group will have full access to the content in the directory foldername, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 070 foldername/','NL Queries':['Give permission to all users of the group to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the content in the folder foldername to all users of the group and generate a log if changes are made to the file?',
																				'Make all users of the group have full access to the content in the folder foldername, generate a log if changes are made to the file.',
																				'All the users of the group will have full access to the content in the folder foldername, a log is generated if changes are made to the file.',
																				'Give permission to all users of the group to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the content in the directory foldername to all users of the group and generate a log if changes are made to the file?',
																				'Make all users of the group have full access to the content in the directory foldername, generate a log if changes are made to the file.',
																				'All the users of the group will have full access to the content in the directory foldername, a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 070 foldername/','NL Queries':['Give permission to all users of the group to read, write and execute the content in the folder foldername. Generate a log.', 
																				'How can I give full access to the content in the folder foldername to all users of the group and generate a log?',
																				'Make all users of the group have full access to the content in the folder foldername, generate a log.',
																				'All the users of the group will have full access to the content in the folder foldername, a log is generated.',
																				'Give permission to all users of the group to read, write and execute the content in the directory foldername. Generate a log.', 
																				'How can I give full access to the content in the directory foldername to all users of the group and generate a log?',
																				'Make all users of the group have full access to the content in the directory foldername, generate a log.',
																				'All the users of the group will have full access to the content in the directory foldername, a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 070 foldername/','NL Queries':['Give permission to all users of the group to read, write and execute the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to all users of the group and prevent error messages from being shown?',
																				'Make all users of the group have full access to the content in the folder foldername, prevent error messages from being shown.',
																				'All the users of the group will have full access to the content in the folder foldername, error messages are prevented from being shown.',
																				'Give permission to all users of the group to read, write and execute the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to all users of the group and prevent error messages from being shown?',
																				'Make all users of the group have full access to the content in the directory foldername, prevent error messages from being shown.',
																				'All the users of the group will have full access to the content in the directory foldername, error messages are prevented from being shown.']},ignore_index = True)

#This ends all combinations for 070

chmod = chmod.append({'Command': 'chmod 007 filename','NL Queries':['Give permission to all non group users to read, write and execute the file filename.', 
																				'How can I give full access to the file filename to all non group users?',
																				'Make all non group users have full access to the file filename.',
																				'All the non group users will have full access to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 007 filename','NL Queries':['Give permission to all non group users to read, write and execute the file filename. Generate a log if changes are made to the file.', 
																				'How can I give full access to the file filename to all non group users and generate a log if changes are made to the file?',
																				'Make all non group users have full access to the file filename and generate a log if changes are made to the file.',
																				'All the non group users will have full access to the file filename and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 007 filename','NL Queries':['Give permission to all non group users to read, write and execute the file filename. Generate a log.', 
																				'How can I give full access to the file filename to all non group users and generate a log?',
																				'Make all non group users have full access to the file filename and generate a log.',
																				'All the non group users will have full access to the file filename and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 007 filename','NL Queries':['Give permission to all non group users to read, write and execute the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to all non group users and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make all non group users have full access to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'All the non group users will have full access to the file filename, prevent error messages from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 007 filename','NL Queries':['Give permission to all non group users to read, write and execute the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to all non group users and prevent error messages from being shown and generate a log?',
																				'Make all non group users have full access to the file filename, prevent error messages from being shown and generate a log.',
																				'All the non group users will have full access to the file filename, prevent error messages from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 007 filename','NL Queries':['Give permission to all non group users to read, write and execute the file filename. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to all non group users and generate a log?',
																				'Make all non group users have full access to the file filename and generate a log.',
																				'All the non group users will have full access to the file filename and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 007 foldername/','NL Queries':['Give permission to all non group users to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to all non group users and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make all non group users have full access to the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'All the non group users will have full access to the content in the folder foldername, prevent error messages from being shown and a log is generated if changes are made to the file.',
																				'Give permission to all non group users to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to all non group users and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make all non group users have full access to the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'All the non group users will have full access to the content in the directory foldername, prevent error messages from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 007 foldername/','NL Queries':['Give permission to all non group users to read, write and execute the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to all non group users and prevent error messages from being shown and generate a log?',
																				'Make all non group users have full access to the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'All the non group users will have full access to the content in the folder foldername, prevent error messages from being shown and a log is generated.',
																				'Give permission to all non group users to read, write and execute the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to all non group users and prevent error messages from being shown and generate a log?',
																				'Make all non group users have full access to the content in the directory foldername, prevent error messages from being shown and generate a log.',
																				'All the non group users will have full access to the content in the directory foldername, prevent error messages from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 007 foldername/','NL Queries':['Give permission to all non group users to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the content in the folder foldername to all non group users and generate a log if changes are made to the file?',
																				'Make all non group users have full access to the content in the folder foldername, generate a log if changes are made to the file.',
																				'All the non group users will have full access to the content in the folder foldername, a log is generated if changes are made to the file.',
																				'Give permission to all non group users to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the content in the directory foldername to all non group users and generate a log if changes are made to the file?',
																				'Make all non group users have full access to the content in the directory foldername, generate a log if changes are made to the file.',
																				'All the non group users will have full access to the content in the directory foldername, a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 007 foldername/','NL Queries':['Give permission to all non group users to read, write and execute the content in the folder foldername. Generate a log.', 
																				'How can I give full access to the content in the folder foldername to all non group users and generate a log?',
																				'Make all non group users have full access to the content in the folder foldername, generate a log.',
																				'All the non group users will have full access to the content in the folder foldername, a log is generated.',
																				'Give permission to all non group users to read, write and execute the content in the directory foldername. Generate a log.', 
																				'How can I give full access to the content in the directory foldername to all non group users and generate a log?',
																				'Make all non group users have full access to the content in the directory foldername, generate a log.',
																				'All the non group users will have full access to the content in the directory foldername, a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 007 foldername/','NL Queries':['Give permission to all non group users to read, write and execute the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the folder foldername to all non group users and prevent error messages from being shown?',
																				'Make all non group users have full access to the content in the folder foldername, prevent error messages from being shown.',
																				'All the non group users will have full access to the content in the folder foldername, error messages are prevented from being shown.',
																				'Give permission to all non group users to read, write and execute the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the content in the directory foldername to all non group users and prevent error messages from being shown?',
																				'Make all non group users have full access to the content in the directory foldername, prevent error messages from being shown.',
																				'All the non group users will have full access to the content in the directory foldername, error messages are prevented from being shown.']},ignore_index = True)
#This ends all combinations for 007

chmod = chmod.append({'Command': 'chmod 711 filename','NL Queries':['Give permission to the owner to read, write and execute and all other users to execute the file filename.', 
																				'How can I give full access to the file filename to the owner and only execute permissions to other users?',
																				'Make the owner have full access to the file filename and other users have execute permissions to the file.',
																				'The owner will have full access to the file filename and all other users will have execute permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 711 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to execute the file filename. Generate a log if changes are made to the file.', 
																				'How can I give full access to the file filename to the owner and execute permissions to all other users and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename and other users to execute the file filename and generate a log if changes are made to the file.',
																				'The owner will have full access to the file filename and other users will have execute permissions and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 711 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to execute the file filename. Generate a log.', 
																				'How can I give full access to the file filename to the owner and all other users to execute the file filename and generate a log?',
																				'Make the owner have full access to the file filename and all other users to execute the file filename and generate a log.',
																				'The owner will have full access to the file filename and all other users will have execute permissions and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 711 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to execute the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and all other users to execute the file filename and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename and all other users to execute the file, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access to the file filename and all other users will have execute permissions, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 711 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to execute the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and execute permissions to all other users and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access to the file filename and all other users to execute the file, prevent error messages from being shown and generate a log.',
																				'The owner will have full access to the file filename and all other users will have execute permissions, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 711 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to execute the file filename. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and execute permissions to all other users and generate a log?',
																				'Make the owner have full access to the file filename and all other users to execute the file filename and generate a log.',
																				'The owner will have full access to the file filename and all other users will have execute permissions and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 711 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to execute the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to execute the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users to execute the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to execute the content in the folder foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.',
																				'Give permission to the owner to read, write and execute and all other users to execute the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and execute permissions to all other users to the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users will have permissions to execute the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to execute the content in the directory foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 711 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to execute the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to execute the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access and all other users to execute the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access and all other users will have permissions to execute the content in the folder foldername, error messages are prevented from being shown and a log is generated.',
																				'Give permission to the owner to read, write and execute and all other users to execute the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and execute permissions to all other users to the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access and all other users will have permissions to execute the content in the directory foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access and all other users will have permissions to execute the content in the directory foldername, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 711 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to execute the content in the folder foldername. Generate a log.', 
																				'How can I give full access to the owner and all other users to execute the content in the folder foldername and generate a log?',
																				'Make the owner have full access and all other users to execute the content in the folder foldername, generate a log.',
																				'The owner will have full access and all other users will have permissions to execute the content in the folder foldername, a log is generated.',
																				'Give permission to the owner to read, write and execute and all other users to execute the content in the directory foldername. Generate a log.', 
																				'How can I give full access to the owner and execute permissions to all other users to the content in the directory foldername and generate a log?',
																				'Make the owner have full access and all other users will have permissions to execute the content in the directory foldername, and generate a log.',
																				'The owner will have full access and all other users will have permissions to execute the content in the directory foldername, and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 711 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to execute the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to execute the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have full access and all other users to execute the content in the folder foldername, prevent error messages from being shown.',
																				'The owner will have full access and all other users will have permissions to execute the content in the folder foldername, error messages are prevented from being shown.',
																				'Give permission to the owner to read, write and execute and all other users to execute the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and execute permissions to all other users to the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have full access and all other users will have permissions to execute the content in the directory foldername, prevent error messages from being shown.',
																				'The owner will have full access and all other users will have permissions to execute the content in the directory foldername, error messages are prevented from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 711 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to execute the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the owner and all other users to execute the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users to execute the content in the folder foldername, generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to execute the content in the folder foldername, a log is generated if changes are made to the file.',
																				'Give permission to the owner to read, write and execute and all other users to execute the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the owner and execute permissions to all other users to the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users will have permissions to execute the content in the directory foldername, and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to execute the content in the directory foldername, and a log is generated if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 711

chmod = chmod.append({'Command': 'chmod 766 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read and write.', 
																				'How can I give full access to the file filename to the owner and only read and write permissions to other users?',
																				'Make the owner have full access to the file filename and other users have read and write permissions to the file filename.',
																				'The owner will have full access to the file filename and all other users will have read and write permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 766 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read and write. Generate a log if changes are made to the file.', 
																				'How can I give full access to the file filename to the owner and read and write permissions to all other users and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename and other users to read and write the file and generate a log if changes are made to the file.',
																				'The owner will have full access to the file filename and other users will have read and write permissions and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 766 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read and write the file filename. Generate a log.', 
																				'How can I give full access to the file filename to the owner and all other users to read and write the file and generate a log?',
																				'Make the owner have full access to the file filename and all other users to read and write the file and generate a log.',
																				'The owner will have full access to the file filename and all other users will have read and write permissions and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 766 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read and write the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and all other users to read and write the file and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename and all other users to read and write the file, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access to the file filename and all other users will have read and write permissions, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 766 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read and write the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and read and write permissions to all other users and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access to the file filename and all other users to read and write the file, prevent error messages from being shown and generate a log.',
																				'The owner will have full access to the file filename and all other users will have read and write permissions, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 766 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read and write the file filename. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and read and write permissions to all other users and generate a log?',
																				'Make the owner have full access to the file filename and all other users to read and write the file and generate a log.',
																				'The owner will have full access to the file filename and all other users will have read and write permissions and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 766 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read and write the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to read and write the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users to read and write the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the folder foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.',
																				'Give permission to the owner to read, write and execute and all other users to read and write the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and read and write permissions to all other users to the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users will have permissions to read and write the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the directory foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 766 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read and write the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to read and write the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access and all other users to read and write the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the folder foldername, error messages are prevented from being shown and a log is generated.',
																				'Give permission to the owner to read, write and execute and all other users to read and write the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and read and write permissions to all other users to the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access and all other users will have permissions to read and write the content in the directory foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the directory foldername, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 766 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read and write the content in the folder foldername. Generate a log.', 
																				'How can I give full access to the owner and all other users to read and write the content in the folder foldername and generate a log?',
																				'Make the owner have full access and all other users to read and write the content in the folder foldername, generate a log.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the folder foldername, a log is generated.',
																				'Give permission to the owner to read, write and execute and all other users to read and write the content in the directory foldername. Generate a log.', 
																				'How can I give full access to the owner and read and write permissions to all other users to the content in the directory foldername and generate a log?',
																				'Make the owner have full access and all other users will have permissions to read and write the content in the directory foldername, and generate a log.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the directory foldername, and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 766 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read and write the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to read and write the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have full access and all other users to read and write the content in the folder foldername, prevent error messages from being shown.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the folder foldername, error messages are prevented from being shown.',
																				'Give permission to the owner to read, write and execute and all other users to read and write the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and read and write permissions to all other users to the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have full access and all other users will have permissions to read and write the content in the directory foldername, prevent error messages from being shown.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the directory foldername, error messages are prevented from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 766 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read and write the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the owner and all other users to read and write the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users to read and write the content in the folder foldername, generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the folder foldername, a log is generated if changes are made to the file.',
																				'Give permission to the owner to read, write and execute and all other users to read and write the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the owner and read and write permissions to all other users to the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users will have permissions to read and write the content in the directory foldername, and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to read and write the content in the directory foldername, and a log is generated if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 766

chmod = chmod.append({'Command': 'chmod 744 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read.', 
																				'How can I give full access to the file filename to the owner and only read permissions to other users?',
																				'Make the owner have full access to the file filename and other users have read permissions to the file filename.',
																				'The owner will have full access to the file filename and all other users will have read permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 744 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read. Generate a log if changes are made to the file.', 
																				'How can I give full access to the file filename to the owner and read permissions to all other users and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename and other users to read the file and generate a log if changes are made to the file.',
																				'The owner will have full access to the file filename and other users will have read permissions and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 744 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read the file filename. Generate a log.', 
																				'How can I give full access to the file filename to the owner and all other users to read the file and generate a log?',
																				'Make the owner have full access to the file filename and all other users to read the file and generate a log.',
																				'The owner will have full access to the file filename and all other users will have read permissions and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 744 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and all other users to read the file and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename and all other users to read the file, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access to the file filename and all other users will have read permissions, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 744 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and read permissions to all other users and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access to the file filename and all other users to read the file, prevent error messages from being shown and generate a log.',
																				'The owner will have full access to the file filename and all other users will have read permissions, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 744 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to read the file filename. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and read permissions to all other users? Don\'t show error messages.',
																				'Make the owner have full access to the file filename and all other users to read the file without displaying error messages.',
																				'The owner will have full access to the file filename and all other users will have read permissions. Don\'t  display error messages.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 744 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to eread the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users to read the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to read the content in the folder foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.',
																				'Give permission to the owner to read, write and execute and all other users to read the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and read permissions to all other users to the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users will have permissions to read the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to read the content in the directory foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 744 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to read the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access and all other users to read the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access and all other users will have permissions to read the content in the folder foldername, error messages are prevented from being shown and a log is generated.',
																				'Give permission to the owner to read, write and execute and all other users to read the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and read permissions to all other users to the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access and all other users will have permissions to read the content in the directory foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access and all other users will have permissions to read the content in the directory foldername, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 744 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read the content in the folder foldername. Generate a log.', 
																				'How can I give full access to the owner and all other users to read the content in the folder foldername and generate a log?',
																				'Make the owner have full access and all other users to read the content in the folder foldername, generate a log.',
																				'The owner will have full access and all other users will have permissions to read the content in the folder foldername, a log is generated.',
																				'Give permission to the owner to read, write and execute and all other users to read the content in the directory foldername. Generate a log.', 
																				'How can I give full access to the owner and read permissions to all other users to the content in the directory foldername and generate a log?',
																				'Make the owner have full access and all other users will have permissions to read the content in the directory foldername, and generate a log.',
																				'The owner will have full access and all other users will have permissions to read the content in the directory foldername, and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 744 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to read the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have full access and all other users to read the content in the folder foldername, prevent error messages from being shown.',
																				'The owner will have full access and all other users will have permissions to read the content in the folder foldername, error messages are prevented from being shown.',
																				'Give permission to the owner to read, write and execute and all other users to read the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and read permissions to all other users to the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have full access and all other users will have permissions to read the content in the directory foldername, prevent error messages from being shown.',
																				'The owner will have full access and all other users will have permissions to read the content in the directory foldername, error messages are prevented from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 744 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to read the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the owner and all other users to read the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users to read the content in the folder foldername, generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to read the content in the folder foldername, a log is generated if changes are made to the file.',
																				'Give permission to the owner to read, write and execute and all other users to read the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the owner and read permissions to all other users to the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users will have permissions to read the content in the directory foldername, and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to read the content in the directory foldername, and a log is generated if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 744

chmod = chmod.append({'Command': 'chmod 722 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to write.', 
																				'How can I give full access to the file filename to the owner and only write permissions to other users?',
																				'Make the owner have full access to the file filename and other users have write permissions to the file filename.',
																				'The owner will have full access to the file filename and all other users will have write permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 722 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to write. Generate a log if changes are made to the file.', 
																				'How can I give full access to the file filename to the owner and write permissions to all other users and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename and other users to write the file and generate a log if changes are made to the file.',
																				'The owner will have full access to the file filename and other users will have write permissions and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 722 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to write the file filename. Generate a log.', 
																				'How can I give full access to the file filename to the owner and all other users to write the file and generate a log?',
																				'Make the owner have full access to the file filename and all other users to write the file and generate a log.',
																				'The owner will have full access to the file filename and all other users will have write permissions and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 722 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to write the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and all other users to write the file and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access to the file filename and all other users to write the file, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access to the file filename and all other users will have write permissions, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 722 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to write the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and write permissions to all other users and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access to the file filename and all other users to write the file, prevent error messages from being shown and generate a log.',
																				'The owner will have full access to the file filename and all other users will have write permissions, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 722 filename','NL Queries':['Give permission to the owner to read, write and execute the file filename and all other users to write the file filename. Prevent error messages from being shown.', 
																				'How can I give full access to the file filename to the owner and write permissions to all other users. Don\'t show error messages?',
																				'Make the owner have full access to the file filename and all other users to write the file without displaying any error messages.',
																				'The owner will have full access to the file filename and all other users will have write permissions. No error messages.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 722 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to write the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to write the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users to write the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to write the content in the folder foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.',
																				'Give permission to the owner to read, write and execute and all other users to write the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and write permissions to all other users to the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users will have permissions to write the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to write the content in the directory foldername, error messages are prevented from being shown and a log is generated if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 722 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to write the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to write the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access and all other users to write the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access and all other users will have permissions to write the content in the folder foldername, error messages are prevented from being shown and a log is generated.',
																				'Give permission to the owner to read, write and execute and all other users to write the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and write permissions to all other users to the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have full access and all other users will have permissions to write the content in the directory foldername, prevent error messages from being shown and generate a log.',
																				'The owner will have full access and all other users will have permissions to write the content in the directory foldername, error messages are prevented from being shown and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 722 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to write the content in the folder foldername. Generate a log.', 
																				'How can I give full access to the owner and all other users to write the content in the folder foldername and generate a log?',
																				'Make the owner have full access and all other users to write the content in the folder foldername, generate a log.',
																				'The owner will have full access and all other users will have permissions to write the content in the folder foldername, a log is generated.',
																				'Give permission to the owner to read, write and execute and all other users to write the content in the directory foldername. Generate a log.', 
																				'How can I give full access to the owner and write permissions to all other users to the content in the directory foldername and generate a log?',
																				'Make the owner have full access and all other users will have permissions to write the content in the directory foldername, and generate a log.',
																				'The owner will have full access and all other users will have permissions to write the content in the directory foldername, and a log is generated.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 722 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to write the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and all other users to write the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have full access and all other users to write the content in the folder foldername, prevent error messages from being shown.',
																				'The owner will have full access and all other users will have permissions to write the content in the folder foldername, error messages are prevented from being shown.',
																				'Give permission to the owner to read, write and execute and all other users to write the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give full access to the owner and write permissions to all other users to the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have full access and all other users will have permissions to write the content in the directory foldername, prevent error messages from being shown.',
																				'The owner will have full access and all other users will have permissions to write the content in the directory foldername, error messages are prevented from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 722 foldername/','NL Queries':['Give permission to the owner to read, write and execute and all other users to write the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the owner and all other users to write the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users to write the content in the folder foldername, generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to write the content in the folder foldername, a log is generated if changes are made to the file.',
																				'Give permission to the owner to read, write and execute and all other users to write the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give full access to the owner and write permissions to all other users to the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have full access and all other users will have permissions to write the content in the directory foldername, and generate a log if changes are made to the file.',
																				'The owner will have full access and all other users will have permissions to write the content in the directory foldername, and a log is generated if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 722

chmod = chmod.append({'Command': 'chmod 417 filename','NL Queries':[' For filename, give permission to the owner to read, group can execute and all other users to read, write and execute.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the file filename?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 417 filename','NL Queries':['Give permission to the owner to read, group can execute and all other users to read, write and execute for the file filename. Generate a log if changes are made to the file.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users and generate a log if changes are made to the file filename?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions to the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 417 filename','NL Queries':[' For filename, give permission to the owner to read, group can execute and all other users to read, write and execute. Generate a log.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the file filename and generate a log?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions to the file and filename generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 417 filename','NL Queries':['Give permission to the owner to read, group can execute and all other users to read, write and execute for the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for file filename and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 417 filename','NL Queries':[' For filename, give permission to the owner to read, group can execute and all other users to read, write and execute. Generate a log. Prevent error messages from being shown.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the file filename and prevent error messages from being shown and generate a log?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions to the file filename, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 417 filename','NL Queries':['Give permission to the owner to read, group can execute and all other users to read, write and execute for filename. Prevent error messages from being shown.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the filename? Don\'t show any error messages.',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions to the file filename without displaying any error messages.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 417 foldername/','NL Queries':['Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the folder foldername, prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 417 foldername/','NL Queries':['Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 417 foldername/','NL Queries':['Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the folder foldername. Generate a log.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the folder foldername and generate a log?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the folder foldername, generate a log.',
																				'Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the directory foldername. Generate a log.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the directory foldername and generate a log?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the directory foldername, and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 417 foldername/','NL Queries':['Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the folder foldername, prevent error messages from being shown.',
																				'Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 417 foldername/','NL Queries':['Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the folder foldername, generate a log if changes are made to the file.',
																				'Give permission to the owner to read, group can execute and all other users to read, write and execute the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give read permission to owner, execute to group and all permissions to other users for the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have execute permissions and other users have all permissions for the content in the directory foldername, and generate a log if changes are made to the file.']},ignore_index = True)

#This ends all combinations for 417

chmod = chmod.append({'Command': 'chmod 740 filename','NL Queries':['Give all permissions for the file filename to the user, group can read and no permissions to other users.', 
																				'How can I give all permissions for the file filename to owner, read to group and no permissions to other users?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 740 filename','NL Queries':['Give all permissions for the file filename to the user, group can read and no permissions to other users. Generate a log if changes are made to the file.', 
																				'How can I give all permissions for the file filename to owner, read to group and no permissions to other users and generate a log if changes are made to the file?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions to the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 740 filename','NL Queries':['Give all permissions for the file filename to the user, group can read and no permissions to other users. Generate a log.', 
																				'How can I give all permissions for the file filename to owner, read to group and no permissions to other users and generate a log?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 740 filename','NL Queries':['Give all permissions for the file filename to the user, group can read and no permissions to other users. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give all permissions for the file filename to owner, read to group and no permissions to other users and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 740 filename','NL Queries':['Give all permissions for the file filename to the user, group can read and no permissions to other users. Generate a log. Prevent error messages from being shown.', 
																				'How can I give all permissions for the file filename to owner, read to group and no permissions to other users and prevent error messages from being shown and generate a log?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions to the file filename, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 740 filename','NL Queries':['Give all permissions for the file filename to the user, group can read and no permissions to other users. Prevent error messages from being shown.', 
																				'How can I give all permissions for the file filename to owner, read to group and no permissions to other users and generate a log?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 740 foldername/','NL Queries':['Give all permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the folder foldername , prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give all permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 740 foldername/','NL Queries':['Give all permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Give all permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 740 foldername/','NL Queries':['Give all permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Generate a log.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the folder foldername and generate a log?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the folder foldername, generate a log.',
																				'Give all permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Generate a log.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the directory foldername and generate a log?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the directory foldername, and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 740 foldername/','NL Queries':['Give all permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the folder foldername, prevent error messages from being shown.',
																				'Give all permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 740 foldername/','NL Queries':['Give all permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the folder foldername, generate a log if changes are made to the file.',
																				'Give all permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give all permissions to owner, read to group and no permissions to other users for the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have all permissions, group have read permissions and other users have no permissions for the content in the directory foldername, and generate a log if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 740

chmod = chmod.append({'Command': 'chmod 140 filename','NL Queries':['Give execute permissions for the file filename to the user, group can read and no permissions to other users.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the file filename?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 140 filename','NL Queries':['Give execute permissions for the file filename to the user, group can read and no permissions to other users. Generate a log if changes are made to the file.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the file filename and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions to the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 140 filename','NL Queries':['Give execute permissions for the file filename to the user, group can read and no permissions to other users. Generate a log.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the file filename and generate a log?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 140 filename','NL Queries':['Give execute permissions for the file filename to the user, group can read and no permissions to other users. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the file filename and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 140 filename','NL Queries':['Give execute permissions for the file filename to the user, group can read and no permissions to other users. Generate a log. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the file filename and prevent error messages from being shown and generate a log?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions to the file filename, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 140 filename','NL Queries':['Give execute permissions for the file filename to the user, group can read and no permissions to other users. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the file filename? Don\'t show any error messages.',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions to the file filename without displaying any error messages.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 140 foldername/','NL Queries':['Give execute permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the folder foldername , prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give execute permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 140 foldername/','NL Queries':['Give execute permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Give execute permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 140 foldername/','NL Queries':['Give execute permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Generate a log.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the folder foldername and generate a log?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the folder foldername, generate a log.',
																				'Give execute permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Generate a log.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the directory foldername and generate a log?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the directory foldername, and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 140 foldername/','NL Queries':['Give execute permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the folder foldername, prevent error messages from being shown.',
																				'Give execute permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 140 foldername/','NL Queries':['Give execute permissions to the user, group can read and no permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the folder foldername, generate a log if changes are made to the file.',
																				'Give execute permissions to the user, group can read and no permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give execute permissions to owner, read to group and no permissions to other users for the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have read permissions and other users have no permissions for the content in the directory foldername, and generate a log if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 140

chmod = chmod.append({'Command': 'chmod 571 filename','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the file filename.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the file filename?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 571 filename','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the file filename. Generate a log if changes are made to the file.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the file filename and generate a log if changes are made to the file?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions to the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 571 filename','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the file filename. Generate a log.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the file filename and generate a log?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 571 filename','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the file filename and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 571 filename','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the file filename and prevent error messages from being shown and generate a log?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions to the file filename, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 571 filename','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the file filename. Prevent error messages from being shown.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users? Don\'t show error messages.',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions to the file filename without displaying error messages.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 571 foldername/','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the folder foldername , prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 571 foldername/','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 571 foldername/','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the folder foldername. Generate a log.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the folder foldername and generate a log?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the folder foldername, generate a log.',
																				'Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the directory foldername. Generate a log.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the directory foldername and generate a log?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the directory foldername, and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 571 foldername/','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the folder foldername, prevent error messages from being shown.',
																				'Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 571 foldername/','NL Queries':['Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the folder foldername, generate a log if changes are made to the file.',
																				'Give read and execute permissions to the user, group has all permissions and execute permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give read and execute permissions to owner, all to group and execute permissions to other users for the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have read and execute permissions, group have read permissions and other users have execute permissions for the content in the directory foldername, and generate a log if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 571

chmod = chmod.append({'Command': 'chmod 404 filename','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the file filename.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the file filename?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 404 filename','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the file filename. Generate a log if changes are made to the file.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the file filename and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions to the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 404 filename','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the file filename. Generate a log.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the file filename and generate a log?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 404 filename','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the file filename and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 404 filename','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the file filename and prevent error messages from being shown and generate a log?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions to the file filename, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 404 filename','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the file filename. Prevent error messages from being shown.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the file filename and generate a log?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 404 foldername/','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the folder foldername , prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give read permissions to the user, group has no permissions and read permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 404 foldername/','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Give read permissions to the user, group has no permissions and read permissions to other users for the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 404 foldername/','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the content in the folder foldername. Generate a log.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the folder foldername and generate a log?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the folder foldername, generate a log.',
																				'Give read permissions to the user, group has no permissions and read permissions to other users for the content in the directory foldername. Generate a log.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the directory foldername and generate a log?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the directory foldername, and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 404 foldername/','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the folder foldername, prevent error messages from being shown.',
																				'Give read permissions to the user, group has no permissions and read permissions to other users for the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 404 foldername/','NL Queries':['Give read permissions to the user, group has no permissions and read permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the folder foldername, generate a log if changes are made to the file.',
																				'Give read permissions to the user, group has no permissions and read permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give read permissions to owner, no permissions to group and read permissions to other users for the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have read permissions, group have no permissions and other users have read permissions for the content in the directory foldername, and generate a log if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 404
chmod = chmod.append({'Command': 'chmod 000 filename','NL Queries':['Give no permissions to user, group and other users for the file filename.', 
																				'How can I give no permissions to user, group and other users for the file filename?',
																				'Make the owner, group and other users have no permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 000 filename','NL Queries':['Give no permissions to user, group and other users for the file filename. Generate a log if changes are made to the file.', 
																				'How can I give no permissions to user, group and other users for the file filename and generate a log if changes are made to the file?',
																				'Make the owner, group and other users have no permissions to the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 000 filename','NL Queries':['Give no permissions to user, group and other users for the file filename. Generate a log.', 
																				'How can I give no permissions to user, group and other users for the file filename and generate a log?',
																				'Make the owner, group and other users have no permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 000 filename','NL Queries':['Give no permissions to user, group and other users for the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give no permissions to user, group and other users for the file filename and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner, group and other users have no permissions to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 000 filename','NL Queries':['Give no permissions to user, group and other users for the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give no permissions to user, group and other users for the file filename and prevent error messages from being shown and generate a log?',
																				'Make the owner, group and other users have no permissions to the file filename, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 000 filename','NL Queries':['Give no permissions to user, group and other users for the file filename. Prevent error messages from being shown.', 
																				'How can I give no permissions to user, group and other users for the file filename and generate a log?',
																				'Make the owner, group and other users have no permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 000 foldername/','NL Queries':['Give no permissions to user, group and other users for the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give no permissions to user, group and other users for the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner, group and other users have no permissions for the content in the folder foldername , prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give no permissions to user, group and other users for the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give no permissions to user, group and other users for the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner, group and other users have no permissions for the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 000 foldername/','NL Queries':['Give no permissions to user, group and other users for the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give no permissions to user, group and other users for the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner, group and other users have no permissions for the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Give no permissions to user, group and other users for the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give no permissions to user, group and other users for the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner, group and other users have no permissions for the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 000 foldername/','NL Queries':['Give no permissions to user, group and other users for the content in the folder foldername. Generate a log.', 
																				'How can I give no permissions to user, group and other users for the content in the folder foldername and generate a log?',
																				'Make the owner, group and other users have no permissions for the content in the folder foldername, generate a log.',
																				'Give no permissions to user, group and other users for the content in the directory foldername. Generate a log.', 
																				'How can I give no permissions to user, group and other users for the content in the directory foldername and generate a log?',
																				'Make the owner, group and other users have no permissions for the content in the directory foldername, and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 000 foldername/','NL Queries':['Give no permissions to user, group and other users for the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give no permissions to user, group and other users for the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner, group and other users have no permissions for the content in the folder foldername, prevent error messages from being shown.',
																				'Give no permissions to user, group and other users for the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give no permissions to user, group and other users for the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner, group and other users have no permissions for the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 000 foldername/','NL Queries':['Give no permissions to user, group and other users for the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give no permissions to user, group and other users for the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner, group and other users have no permissions for the content in the folder foldername, generate a log if changes are made to the file.',
																				'Give no permissions to user, group and other users for the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give no permissions to user, group and other users for the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner, group and other users have no permissions for the content in the directory foldername, and generate a log if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 000

chmod = chmod.append({'Command': 'chmod 124 filename','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the file filename.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the file filename?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 124 filename','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the file filename. Generate a log if changes are made to the file.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the file filename and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions to the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 124 filename','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the file filename. Generate a log.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the file filename and generate a log?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 124 filename','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the file filename and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 124 filename','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the file filename and prevent error messages from being shown and generate a log?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions to the file filename, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 124 filename','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the file filename. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the file filename and generate a log?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 124 foldername/','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the folder foldername , prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give execute permissions to the user, group can write and read permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 124 foldername/','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Give execute permissions to the user, group can write and read permissions to other users for the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 124 foldername/','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the content in the folder foldername. Generate a log.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the folder foldername and generate a log?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the folder foldername, generate a log.',
																				'Give execute permissions to the user, group can write and read permissions to other users for the content in the directory foldername. Generate a log.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the directory foldername and generate a log?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the directory foldername, and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 124 foldername/','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the folder foldername, prevent error messages from being shown.',
																				'Give execute permissions to the user, group can write and read permissions to other users for the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 124 foldername/','NL Queries':['Give execute permissions to the user, group can write and read permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the folder foldername, generate a log if changes are made to the file.',
																				'Give execute permissions to the user, group can write and read permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give execute permissions to owner, write to group and read permissions to other users for the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have execute permissions, group have write permissions and other users have read permissions for the content in the directory foldername, and generate a log if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 124

chmod = chmod.append({'Command': 'chmod 227 filename','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the file filename.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the file filename?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions to the file filename.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -c 227 filename','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the file filename. Generate a log if changes are made to the file.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the file filename and generate a log if changes are made to the file?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions to the file filename and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -v 227 filename','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the file filename. generate a log.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the file filename and generate a log?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions to the file filename and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -cf 227 filename','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the file filename. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the file filename and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions to the file filename, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -vf 227 filename','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the file filename. Generate a log. Prevent error messages from being shown.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the file filename and prevent error messages from being shown and generate a log?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions to the file filename, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -f 227 filename','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the file filename. Prevent error messages from being shown.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the file filename without any error messages displayed?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions to the file filename. Don\'t show any error messages.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rcf 227 foldername/','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the folder foldername , prevent error messages from being shown and generate a log if changes are made to the file.',
																				'Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file. Prevent error messages from being shown.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log if changes are made to the file?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the directory foldername, prevent error messages from being shown and generate a log if changes are made to the file.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rvf 227 foldername/','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the folder foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the folder foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the folder foldername, prevent error messages from being shown and generate a log.',
																				'Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the directory foldername. Generate a log. Prevent error messages from being shown.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the directory foldername and prevent error messages from being shown and generate a log?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the directory foldername, prevent error messages from being shown and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rv 227 foldername/','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the folder foldername. Generate a log.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the folder foldername and generate a log?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the folder foldername, generate a log.',
																				'Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the directory foldername. Generate a log.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the directory foldername and generate a log?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the directory foldername, and generate a log.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rf 227 foldername/','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the folder foldername. Prevent error messages from being shown.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the folder foldername and prevent error messages from being shown?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the folder foldername, prevent error messages from being shown.',
																				'Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the directory foldername. Prevent error messages from being shown.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the directory foldername and prevent error messages from being shown?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the directory foldername, prevent error messages from being shown.']},ignore_index = True)

chmod = chmod.append({'Command': 'chmod -Rc 227 foldername/','NL Queries':['Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the folder foldername. Generate a log if changes are made to the file.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the folder foldername and generate a log if changes are made to the file?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the folder foldername, generate a log if changes are made to the file.',
																				'Give write permissions to the user, group can write and read, execute and write permissions to other users for the content in the directory foldername. Generate a log if changes are made to the file.', 
																				'How can I give write permissions to owner, write to group and read, execute and write permissions to other users for the content in the directory foldername and generate a log if changes are made to the file?',
																				'Make the owner have write permissions, group have write permissions and other users have read, execute and write permissions for the content in the directory foldername, and generate a log if changes are made to the file.']},ignore_index = True)
#This ends all combinations for 227

#754D 755D 600D 700D 477D 777D 700D 070D 007D
#TBA 711D 766D 744D 722D 417D 740D 140D 571D 404D 000D 124D 227D
print (chmod.shape)
