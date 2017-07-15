import pandas as pd 

sed = pd.DataFrame(columns = ['Command','NL Queries'])

sed = sed.append({'Command':'sed \'$d\' file.txt','NL Queries':['Remove last line of file.txt.','Keep all contents of file.txt but the last line.','How do I remove last line of file.txt?']},ignore_index = True)
sed = sed.append({'Command':"sed 's/^[ ^t]*//;s/[ ^]*$//' name.txt",'NL Queries':['Remove spaces in fromt and back of each line for name.txt','How do i remove spaces before and after each line of name.txt?']},ignore_index = True)
sed = sed.append({'Command':'sed \'s/Nick/John/g\' report.txt','NL Queries':['Replace every occurance of Nick with John in file report.txt','How do I replace all \'Nick\' with \'John\' in report.txt?','Replace word Nick with John in report.txt. All words need to be replaced.']},ignore_index = True)

print sed