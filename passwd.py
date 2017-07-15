import pandas as pd 

gnu = pd.DataFrame(columns = ['Command','NL Queries'])

gnu = gnu.append({'Command':'sudo passwd ted','NL Queries':['Change passwd for username ted.','How do I change password for account name ted?','I want to change password of account with username ted. What is the command for that?']},ignore_index=True)
gnu = gnu.append({'Command':'sudo passwd -S -a','NL Queries':['Show password information of all user accounts, system-wide.','How do I check password usability, last date of password change, minimum and maximum age password etc. for all users in the system?']},ignore_index=True)
gnu = gnu.append({'Command':'sudo passwd -u jane','NL Queries':[' Unlock password for account with username jane.','How do I unlock password for username jane?','How do I open access to the account jane so that she can log in?']},ignore_index=True)

print gnu


