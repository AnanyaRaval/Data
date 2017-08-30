import pandas as pd 

cd = pd.DataFrame(columns = ['Command','NL Queries'])

cd = cd.append({'Command':' cd ..',
				'NL Queries':['Go back to one folder.',
							'Change current folder to previous folder.',
							'How to change directory from this one to the one before?']},ignore_index = True)

cd = cd.append({'Command':'cd /full/path/to/folder',
				'NL Queries':['Change current environment to /full/path/to/folder',
							'Make my current workspace to /full/path/to/folder',
							'Command to change directory to /full/path/to/folder']},ignore_index = True)

cd = cd.append({'Command':'cd ~/full/path/to/folder',
				'NL Queries':['Make my current workspace to ~/full/path/to/folder.',
							'Go to ~/full/path/to/folder.',
							'Change my workspace to ~/full/path/to/folder.',
							'Move to ~/full/path/to/folder.']},ignore_index = True)

cd = cd.append({'Command':'cd /relative/path/to/folder',
				'NL Queries':['Change current environment to /relative/path/to/folder.',
							'Make my current workspace to /relative/path/to/folder.',
							'Command to change directory to /relative/path/to/folder.',
							'Move to folder /relative/path/to/folder.']},ignore_index = True)

#cd = cd.append({'Command':'pushd ~/full/path/to/folder',
#				'NL Queries':['Hold ~/full/path/to/folder in a stack.',
#							'Put ~/full/path/to/folder in a stack.',
#							'Push ~/full/path/to/folder into a stack.']},ignore_index = True)

#cd = cd.append({'Command':'pushd /relative/path/to/folder',
#				'NL Queries':['Hold /relative/path/to/folder into a stack.',
#							'Put /relative/path/to/folder into a stack.',
#							'Push /relative/path/to/folder into a stack.']},ignore_index = True)

#cd = cd.append({'Command':'popd',
#				'NL Queries':['Change to the folder in stack.',
#							'Move to folder in stack.',
#							'Revome folder from stack and change current working space to that folder.']},ignore_index = True)

cd = cd.append({'Command':'cd ~',
				'NL Queries':['Change to home folder.',
							'Go to home folder.',
							'How do I go back to home folder?',
							'Single command to go to /home/username folder.']},ignore_index = True)
#cd same as cd ~ , have same NL Queries
cd = cd.append({'Command':'cd',
				'NL Queries':['Change to home folder.',
							'Go to home folder.',
							'How do I go back to home folder?',
							'Single command to go to /home/username folder.']},ignore_index = True)

cd = cd.append({'Command':'cd -',
				'NL Queries':['Change to previous working folder.',
							'How do I go back to previous working folder?',
							'Go back to previous working directory.',
							'Change my workspace to previous workspace.']},ignore_index = True)

cd = cd.append({'Command':'cd .',
				'NL Queries':['Change working directory to present working directory.',
							'How to change my working directory as present working directory?',
							'Make my working directory as present working directory.']},ignore_index = True)

#cd = cd.append({'Command':'dirs',
#				'NL Queries':['list the folders in stack.',
#							'Get me list of folders in stack.',
#							'How to get the list of folders in stack?',
#							'Display the folders in stack.']},ignore_index = True)

#cdspell used for correcting spellings during input directory structure for cd 

#cd = cd.append({'Command':'shopt -s cdspell',
#				'NL Queries':['Set autocorrect on for spelling mistakes in directory structure.',
#							'Autocorrect for directory structure.',
#							'Autocorrect \'ON\' for folder names in directory structure.']},ignore_index = True)

cd = cd.append({'Command':'cd ~/full/path/to/f*',
				'NL Queries':['Change current environment to /full/path/to/f*.',
							'Make my current workspace to /full/path/to/f*.',
							'Command to change directory to /full/path/to/f*.']},ignore_index = True)
cd = cd.append({'Command':'cd ~/full/path/to/f?',
				'NL Queries':['Change current environment to /full/path/to/f?.',
							'Make my current workspace to /full/path/to/f?.',
							'Command to change directory to /full/path/to/f?.']},ignore_index = True)

#You have said the alias is in different work, so keep them but just comment them.

#By creating a 
#alias cd1='cd ..'
#alias cd2='cd ../..'
#alias cd3='cd ../../..'
#so on in .profile or .bashrc or .bash_profile


#cd = cd.append({'Command':'cd1',
#				'NL Queries':['Go back to one folder.',
#							'Change current folder to previous folder.',
#							'How to change directory from this one to the one before?']},ignore_index = True)
#cd = cd.append({'Command':'cd2',
#				'NL Queries':['Go back to two folders.',
#							'Change working directory two levels up.',
#							'Change working directory to parents parent directory.']},ignore_index = True)
#cd = cd.append({'Command':'cd3',
#				'NL Queries':['Go back to three folders.',
#							'Change working directory three levels up.']},ignore_index = True)

#cd ~/full/path/to/f* works perfectly only if there is one folder starting with f in the parent folder, else it changes to the first one which displayed using <TAB> key

print (cd.shape)
