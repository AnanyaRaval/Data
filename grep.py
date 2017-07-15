import pandas as pd 

grep = pd.DataFrame(columns = ['Command','NL Queries'])

grep = grep.append({'Command':'grep "gmail" ananya.txt','NL Queries':['Search if the string \'gmail\' is present in the file ananya.txt.',\
		'How do I find the pattern \'gmail\' in ananya.txt?',\
		'Command to search a string in ananya.txt. The string to be searched is \'gmail\'.']},ignore_index=True)
grep = grep.append({'Command':'grep -i "gmail" ananya.txt','NL Queries':['Command to search for string \'gmail\' in ananya.txt without being case sensitive.',\
		'Find string \'gmail\' in ananya.txt. Find string containing letters in any case.',\
			'How do I search for string \'gmail\' in current folder case insensitively?']},ignore_index=True)
grep = grep.append({'Command':'grep -r "string" *','NL Queries':['Command to search for the phrase "string" in all files of this directory and sub-directories.',\
		'How do I search for "string" in all files in current folder and all folders in this folder?']},ignore_index=True)

print grep

