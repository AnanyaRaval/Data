import pandas as pd 

echo = pd.DataFrame(columns = ['Command','NL Queries'])

echo = echo.append({'Command':' echo My name is Ananya','NL Queries':['Print My name is Ananya','Output this string: \'My name is Ananya.\'','How do I print My name is Ananya in command line?']},ignore_index = True)
echo = echo.append({'Command':'echo -e Column1 \t Column2','NL Queries':['Print Column1 Column2 with a tab in between them.' 'How do I print tab separated \'Column1 Column2\'?']},ignore_index =  True)
echo = echo.append({'Command':'echo $X','NL Queries':['Print value of variable x.','What is the value of shell variable x?','How do I output the value of variable x?']},ignore_index = True)
echo = echo.append({'Command':'echo *','NL Queries':['Print all file names in current folder.','What files are present in this folder?','How do I find out the files present in this folder?','List all files in this folder.']},ignore_index = True)

print echo