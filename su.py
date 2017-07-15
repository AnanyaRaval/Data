import pandas as pd 

su = pd.DataFrame(columns = ['Command','NL Queries'])

su = su.append({'Command':'su - john -c "TestProgram"','NL Queries':['Run TestProgram as user john.','How do I run TestProgram as user john?']},ignore_index=True)
su = su.append({'Command':'su guest','NL Queries':['Login as username guest.','How do I login as user guest?']},ignore_index=True)

print su


