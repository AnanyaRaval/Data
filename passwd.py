import pandas as pd 

passwd = pd.DataFrame(columns = ['Command','NL Queries'])

passwd = passwd.append({'Command':'sudo passwd ted','NL Queries':['Change passwd for username ted.',
																'How do I change password for account name ted?',
																'I want to change password of account with username ted. What is the command for that?']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -S -a','NL Queries':['Show password information of all user accounts, system-wide.',
																	'How do I check password usability, last date of password change, minimum and maximum age password etc. for all users in the system?',
																	'Show status information of all user accounts in the system.']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -u jane','NL Queries':['Unlock password for account with username jane.',
																	'How do I unlock password for username jane?',
																	'How do I open access to the account jane so that she can log in?']},ignore_index=True)

passwd = passwd.append({'Command':'passwd sally','NL Queries':['Change password of user sally via root user.',
																'What if I forget password for username sally?',
																'How do I open access to the account sally so that it can change password of it?']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -l jane','NL Queries':['Lock account with username jane until system administrator unlocks it.',
																		'How do I lock password of username jane?',
																		'How do I stop access to the account jane, by locking the password, so that she cannot log in?']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -S jane','NL Queries':['Check the status of the password of user jane',
																	'How do I check status of password for username jane?',
																	'How do I can see status of the account jane?']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -e jane','NL Queries':['Expire password of username jane.',
																	'How do I expire password account jane?',
																	'How can we expire the password of account jane?',
																	'Command to immediately expire password of account jane.']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -d jane','NL Queries':['Delete password of jane\'s account.',
																		'How do I delete password of jane?',
																		'How can we delete password of username jane?']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -n 5 jane','NL Queries':['Set minimum no. of days between password changes to 5 days of username jane.',
																		'How do I set minimum no. of days between password changes to 5 days for account with username jane?',
																		'Set minimum number of days between password changes of account with username jane to 5.']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -x 999 jane','NL Queries':['Set maximum no. of days for validity of password to 999 days of username jane.',
																			'How do I set maximum no. of days for validity of password to 999 days of account jane?',
																			'Set 999 days as maximum number of days of validity of password of account with username jane.']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -w 9 jane','NL Queries':['Set no. of days of warning before a password change is required to 9 days of username jane.',
																		'How do I set no. of days of warning before a password change is required to 9 days of account jane?'
																		'Set 9 days as warning period of password change for account with username jane.']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -qe jane','NL Queries':['Expire password of username jane quietly.',
																		'How do I expire password account jane quietly?',
																		'Without any messages on command prompt, expire password of account with username jane.']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -qd jane','NL Queries':['Delete password of jane\'s account quietly.',
																		'How do I delete password of jane quietly?',
																		'Without any messages on command prompt, delete the password of account with username jane.']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -nq 0 jane','NL Queries':['Set minimum no. of days between password change to 0 days of username jane quietly.',
																		'How do I set minimum no. of days between password change to 0 days of account jane quietly?',
																		'Without any messages on command prompt, make number of days between password changes to 0 for username jane?']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -xq 999 jane','NL Queries':['Set maximum no. of days for validity of password to 999 days of username jane quietly.',
																			'How do I set maximum no. of days for validity of password to 999 days of account jane quietly?',
																			'Without any messages on command prompt, make 999 the maximum number of days for validity of password of account jane.']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -qw 9 jane','NL Queries':['Set no. of days of warning before a password change is required to 9 days of username jane quietly.',
																		'How do I Set no. of days of warning before a password change is required to 9 days of account jane quietly?',
																		'Without any mesages on command prompt, make 9 days as warning period before a password change is require for account jane.']},ignore_index=True)

#passwd = passwd.append({'Command':'man passwd','NL Queries':['How do I know what the command passwd could do?',
#															'Get complete details of passwd command.',
#															'How do I see all options of passwd command in linux?']},ignore_index=True)




'''

passwd = passwd.append({'Command':'whatis passwd','NL Queries':['How do I know what the command passwd does?','Get one line description of passwd command.','How do I see what passwd command in linux does?']},ignore_index=True)

passwd = passwd.append({'Command':'whereis passwd','NL Queries':['How do I find all paths containing passwd?','Locate python.','List folders where passwd source files, documentaion and binaries are stored.','How can i know where are the files of passwd are stored?']},ignore_index=True)

passwd = passwd.append({'Command':'chage --list jane','NL Queries':['List the password\'s related details of jane.','How do I get password related detail\'s of jane?','How can we find details of password for an account?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -M 10 jane','NL Queries':['Expire password of jane\'s account after 10 days.','How do I set no. of days of expiry for password of jane?','How can we change the new no. of days of expiry date of password?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -E "2009-05-31" jane','NL Queries':['Expire password of jane\'s account on 2009-05-31.','How do I set date of expiry for password of jane?','How can we change the date of expiry of password?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -I 10 jane','NL Queries':['Force the jane\'s account to be locked after 10 number of inactivity days.','How do I lock jane\'s account after certain no. of inactive days?','How can we lock an account after certain no. of inactivity days?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -m 0 jane','NL Queries':['Set minimum no. of days between password change to 0 of jane.','How do I set minimum no. days between password change of account of jane?','How can we set minimum number of days between password change of an account?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -M 99999 jane','NL Queries':['Set maximum no. of days between password change to 99999 of jane.','How do I set maximum no. days between password change of account of jane?','How can we set maximum number of days between password change of an account?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -I -1 jane','NL Queries':['Set password inactive to never of jane.','How do I set password inactive to never of jane?','How can we set password inactive to never of an account?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -E -1 jane','NL Queries':['Set Account expires to never of jane.','How do I set Account expires to never of jane?','How can we set Account expires to never of an account?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -W -10 jane','NL Queries':['Set password expiry warning message of jane to 10 days.','How do I set password expiry warning message of jane to 10 days?','How can we set password expiry warning message of an account to some days?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -d 0 jane','NL Queries':['Force the user jane to change the password on next logon.','How can we Force the user jane to change the password on next logon?','How can we Force the users to change the password on next logon?']},ignore_index=True)

passwd = passwd.append({'Command':'chage -m 0 -M 99999 -I -1 -E -1 jane','NL Queries':['Disable password aging for jane\'s account.','How to disable password aging for jane\'s account?','How to disable password aging for an user account?']},ignore_index=True)

passwd = passwd.append({'Command':'sudo passwd -e jane','NL Queries':['Expire account of jane.','How do I expire account of jane?','How can we expires an account?']},ignore_index=True)

'''
print (passwd.shape)


