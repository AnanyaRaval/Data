import pandas as pd 

chown = pd.DataFrame(columns = ['Command','NL Queries'])

chown = chown.append({'Command':'chown root tmpfile','NL Queries':['Change ownership of tmpfile to root.','How do I make root owner of tmpfile?','How do I change ownership of file tmpfile to root?']},ignore_index=True)
chown = chown.append({'Command':'chown --from=guest root tmpfile','NL Queries':['Change ownership of tmpfile from guest to root.','How do make root the owner of tmpfile instead of root?','How do I replace root as owner of tmpfile instead of guest?']},ignore_index=True)
chown = chown.append({'Command':'chown -R mark:sales /path/to/directory','NL Queries':['Changer owner of path/to/directory and it\'s contents from mark to sales.',' How do I replace ownership of /path/to/directory from mark to sales? Change ownership of all files and folders inside /path/to/directory to mark']},ignore_index=True)

print chown
