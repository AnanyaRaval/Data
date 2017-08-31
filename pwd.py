import pandas as pd 

pwd = pd.DataFrame(columns = ['Command','NL Queries'])

pwd = pwd.append({'Command': 'pwd','NL Queries' :['Current Directory',
												"What is my current path?",
												"What is the path till current directory?",
												"Show Working Directory.",
												'Print the current working directory',
												'Command to find current folder full path.',
												'How do I find the absolute path of the working directory?',
												'Command to find the present working directory path from root directory.',
												'How do I know my current working path?']},ignore_index = True)

pwd = pwd.append({'Command': 'pwd -L','NL Queries' :['Print working directory from environment.',
													'What is my logical working directory?',
													'Show working Directory with symbolic links.',
													'How do I know the present folder full path with symbolic links?']},ignore_index = True)
pwd = pwd.append({'Command': 'pwd -P', 'NL Queries': ['Print current physical directory without considering symbolic links.',
													 'What is current physical location? Don\'t consider symbolic links.',
													 'Print current directory. Ignore symbolic links',]},ignore_index = True)

pwd = pwd.append({'Command': 'pwd --help','NL Queries':['What are the options of pwd command?',
														'Show pwd command description',
														'Show all options of pwd command.',
														'what are the options of pwd command?']},ignore_index = True)
pwd = pwd.append({'Command':'pwd --version','NL Queries':['How do I know the current version of the pwd command?',
															'Show pwd command installation info.',
															'Display pwd command version details.']},ignore_index = True)


#pwd.to_csv('pwd.csv',index = False)

print pwd.shape