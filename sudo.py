import pandas as pd 

sudo = pd.DataFrame(columns = ['Command','NL Queries'])

sudo = sudo.append({'Command':'sudo -u comphope ls /home/comphope/hope',
					'NL Queries':['List the contents of the /home/comphope/hope directory as the comphope user.',
								'See contents of /home/comphope/hope as user comphope.']},ignore_index=True)

sudo = sudo.append({'Command':'sudo -g comphope ls /home/comphope/hope',
					'NL Queries':['List the contents of the /home/comphope/hope directory as the comphope group.',
								'See contents of /home/comphope/hope as group comphope.']},ignore_index=True)

sudo = sudo.append({'Command':'sudo -k',
					'NL Queries':['Invalidate timestamp of current user.',
								'How do I invalidate timestamp of active user?',
								'Kill timestamp of current user.']},ignore_index=True)

sudo = sudo.append({'Command':'sudo -V',
					'NL Queries':['Display sudo version information and exit.',
								'How do I know version of sudo?',
								'How do I know version information of sudo?']},ignore_index=True)

sudo = sudo.append({'Command':'sudo -K',
					'NL Queries':['Remove timestamp of current user completely.',
								'How do I remove timestamp of active user?',
								'Surely kill timestamp of current user.']},ignore_index=True)

sudo = sudo.append({'Command':'sudo -h',
					'NL Queries':['Show help of sudo command.',
								'How do see the help of sudo command?',
								'How do I get the various options of sudo command?',
								'Display various options of sudo command?']},ignore_index=True)

sudo = sudo.append({'Command':'sudo -v',
					'NL Queries':['Update timestamp of current user.',
								'How do I update timestamp of active user?']},ignore_index=True)

sudo = sudo.append({'Command':'sudo -b rm file.txt',
					'NL Queries':['Remove file.txt in background.',
								'How do I remove file.txt in background?']},ignore_index=True)


print sudo.shape


