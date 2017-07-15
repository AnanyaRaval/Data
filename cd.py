import pandas as pd 

cd = pd.DataFrame(columns = ['Command','NL Queries'])

cd = cd.append({'Command':' cd ..','NL Queries':['Go back one folder.','Change current folder to previous folder.',\
										'How to change directory from this one to one before?']},ignore_index = True)
cd = cd.append({'Command': 'cd /full/path/to/folder','NL Queries':['Change current environment to /full/path/to/folder',\
					'Make my current workspace to /full/path/to/folder',\
					'Command to change directory to /full/path/to/folder']},ignore_index = True)
cd = cd.append({'Command':'cd ~','NL Queries':['Change to home folder.',\
					'Go to home folder.','Hwo do I go back to home folder?',\
						'Single command to go to /home/username folder.']},ignore_index = True)

print cd
