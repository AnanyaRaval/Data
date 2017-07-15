import pandas as pd 

which = pd.DataFrame(columns = ['Command','NL Queries'])

which = which.append({'Command':'which programname','NL Queries':['What is the location of programname?','Where is programname?','How do I find programname?','Path of programname.']},ignore_index = True)
which = which.append({'Command':'which firefox gimp banshee','NL Queries':['Where are the firefox, gimp, banshee located?',' What are the paths of firefox, gimp, banshee?','How do I get the folders of banshee, gimp and firefox?']}, ignore_index = True)
which = which.append({'Command': 'which -a command','NL Queries':['All paths of command','Find all locations of command','Find more than one location of command.','In what palces is command installed?']},ignore_index = True)

print which