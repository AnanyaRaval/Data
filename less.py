import pandas as pd 

less = pd.DataFrame(columns = ['Command','NL Queries'])

less = less.append({'Command':'less instructions.txt',
					'NL Queries':['Show contents of instructions.txt enough to fit the teminal.', 
								'Display on command line, content of instructions.txt. Do not show complete file, only the amount which fits the command line.']},ignore_index=True)

less = less.append({'Command':'less +4 instructions.txt',
					'NL Queries':['Show contents of instructions.txt. Skip the first 4 lines though.',
								'Show contents of instructions.txt starting from 5th line.',
								'How do I see content of instructions.txt without the first four lines?']},ignore_index=True)

less = less.append({'Command':'less general.py ananya.py',
					'NL Queries':['Show content of general.py and ananya.py.',
								'Display lines of the files general.py and ananya.py.',
								'Show contents of general.py and ananya.py.']},ignore_index=True)

less = less.append({'Command':'less --help',
					'NL Queries':['Show help for less command.',
								'Man page for less in command line.',
								'What are the options available for less command?']},ignore_index = True)

less = less.append({'Command':'less -a new.txt',
					'NL Queries':['Open file with name new.txt. Start forward search from bottom of screen and backward search from top of screen.',
								'Open file new.txt to search for a pattern in the file skipping all lines displayed on the screen.',
								'How to search in lines of the file new.txt not displayed on screen ,while using?',
								'Search for pattern in new.txt in this folder. Do not search in lines displayed on the screen.']},ignore_index = True)

less = less.append({'Command':'less -b3 new.txt',
					'NL Queries':['Open file new.txt.Allow only a buffer space of 3Kb.',
								'Allocate 3kb buffer space while opening file new.txt.',
								'How do I allocate only 3kb of buffer space to new.txt while opening it?']},ignore_index = True)

less = less.append({'Command':'less -E ~/hi.txt',
					'NL Queries':['Open ~/hi.txt and exit the file after reaching the end.',
								'Open file hi.txt in home directory and close it once it\'s last line is reached.',
								'Display contents of hi.txt using less command. Exit once end of file has reached.',
								'Show contents on hi.txt present in home folder. Close file once end has reached.']},ignore_index = True)

less = less.append({'Command':'less -f new.txt',
					'NL Queries':['Open a non-regular file new.txt. Suppress any warning messages.',
								'How to open a non-regular file new.txt and suppress any warning messages in command line.',
								'Display contents of a non-regular file new.txt.']},ignore_index = True)

less = less.append({'Command':'less -F new.txt',
					'NL Queries':['Open new.txt in command prompt and exit automatically if content fits in one page.',
								'Display new.txt and exit automatically if the content of new.txt completely fits in the screen.',
								'How to automatically quit if the content of new.txt completely fits in the screen.']},ignore_index = True)

less = less.append({'Command':'less -g list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the query was found in that pageful.',
								'Open list.txt. Highlight only the last locations that match the query.',
								'How to highlight only the last matching items found while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -G list.txt',
					'NL Queries':['Open list.txt in command line,one pageful at a time. While searching, go to the location where the query is matched in that pageful without highlighting the match.',
								'Open list.txt. Display the location where the query was matched, without highlighting the query word.',
								'How to supress highlighting, while searching the file => list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -K instructions.txt',
					'NL Queries':['Show contents of instructions.txt. Exit when pressed control + c.',
								'Show contents of instructions.txt starting and exit if pressed control + c.',
								'How do I see content of instructions.txt and exit on pressing control + c?']},ignore_index=True)

less = less.append({'Command':'less -i list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, ignore case if the searching word does not contain uppercase.',
								'Open list.txt. Ignore alphabetic case if the searched word does not contain capital alphabets.',
								'How to search the file = list.txt in command line and treat uppercase and lowercase as identical if the searching word does not contain uppercase?']},ignore_index = True)

less = less.append({'Command':'less -I list.txt',
					'NL Queries':['Open list.txt in command line,one pageful at a time. While searching, ignore case.',
								'Open list.txt. consider small and capital as identical.',
								'How to search the file = list.txt in command line treating uppercase and lowercase as identical?']},ignore_index = True)

less = less.append({'Command':'less -j5p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the query was found in that pageful and place the first found location at number 5 line.',
								'Open list.txt.Highlight only the last locations that match the query and display the first found location at number 5 line.',
								'How to highlight only the last matching items found while searching the file = list.txt in command line and display the first found location at number 5 line?']},ignore_index = True)

less = less.append({'Command':'less -J new.txt',
					'NL Queries':['Open new.txt and show status of each line.',
								'Display content of new.txt with status on left side of each line.',
								'How to see content and status of each line in new.txt?']},ignore_index = True)

less = less.append({'Command':'less -m new.txt',
					'NL Queries':['Open new.txt with and show short explanation of output.',
								'Open new.txt with and show percentage of output displayed.',
								'Display content of new.txt with percentage of file displayed.',
								'How to see content and short explanation of the displayed content of new.txt?',
								'How to see content and percentage of the displayed content of new.txt?']},ignore_index = True)

less = less.append({'Command':'less -M new.txt',
					'NL Queries':['Open new.txt and show verbose of output.',
								'Open new.txt and show percentage, line numbers of output displayed.',
								'Display content of new.txt with percentage , line numbers of file displayed.',
								'How to see verbose content of the file new.txt?',
								'How to see content and percentage, line numbers of the displayed content of new.txt?']},ignore_index = True)

#-n not nesseccarily need(its default)
less = less.append({'Command':'less -n new.txt',
					'NL Queries':['Open new.txt and do not show line numbers.',
								'Display content of new.txt without line numbering.',
								'How to see content of new.txt without numbering lines?']},ignore_index = True)

less = less.append({'Command':'less -N new.txt',
					'NL Queries':['Open new.txt and show line numbers for lines.',
								'Display content of new.txt with line numbering.',
								'How to see content of new.txt with numbering of lines?']},ignore_index = True)

less = less.append({'Command':'less -r new.txt',
					'NL Queries':['Open new.txt along with control characters.',
								'Display content of new.txt with control characters.',
								'How to see content of new.txt along with control characters?']},ignore_index = True)

less = less.append({'Command':'less -s new.txt',
					'NL Queries':['Open new.txt and squeeze any multiple blank lines.',
								'Display content of new.txt with squeezing multiple empty lines.',
								'How to see content of new.txt with squeezing multiple blank lines?']},ignore_index = True)

less = less.append({'Command':'less -S new.txt',
					'NL Queries':['Open new.txt and do not wrap longer lines.',
								'Display content of new.txt without displaying the portion of the line that does not fit in the screen.',
								'Display content of new.txt without cutting long lines into multiple lines.',
								'Open new.txt without cutting long lines into multiple lines.',
								'How to see content of new.txt with displaying long lines as one line?',
								'How to see content of new.txt without breaking long lines?']},ignore_index = True)

less = less.append({'Command':'less -u new.txt',
					'NL Queries':['Open new.txt and display backsapce, tabs and carriage returns as control characters.',
								'Display content of new.txt with backsapce, tabs and carriage returns as control characters.',
								'How to see content of new.txt with backsapce, tabs and carriage returns displayed as control character?']},ignore_index = True)

less = less.append({'Command':'less -~ new.txt',
					'NL Queries':['Open new.txt and do not end with tilda after end of file.',
								'Display content of new.txt without ~ after end of file.',
								'How to see content of new.txt without tilda at the end?']},ignore_index = True)


#--- Add commands for -g, -G, -h, -i, -I, -j, -t, -T, -y. For -p, add about 10 queries with different patterns for searching. Also, add as many combinations of these as you can.


#-p
less = less.append({'Command':'less -p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the hello word.',
								'Open list.txt.Highlight all locations that match the hello word.',
								'How to highlight matching word hello while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -p \"hello world\" list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \"hello world\" word.',
								'Open list.txt. Highlight all locations that match the \"hello world\" word.',
								'How to highlight matching words \"hello world\" while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -p h+ello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'ello\' word is preceded by one or more \'h\'.',
								'Open list.txt.Highlight all locations that match \'ello\' preceded word by one or more \'h\'.',
								'How to highlight matching words \'ello\' preceded by one or more \'h\' while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -p hello? list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where zero or one \'o\' occurs after \'hell\'.',
								'Open list.txt.Highlight all locations that match \'hell\' and follows zero or one \'o\'.',
								'How to highlight matching words \'hell\' followed by zero or one \'o\' while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -p he*llo list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'h\' is followed by zero or more occurences of \'e\' and again followed by \'llo\'.',
								'Open list.txt.Highlight all locations that match \'h\' followed by zero or more \'e\' and again followed by \'llo\'.',
								'How to highlight matching words \'h\' followed by zero or more \'e\' again follwed by \'llo\' while searching the file list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -p ^hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the locations where the hello word was at the beginning of string or line.',
								'Open list.txt.Highlight the locations that match the hello word at the starting of line or string.',
								'How to highlight matching words hello at starting for line or string while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -p hello$ list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the locations where the hello word was at the end of string or line.',
								'Open list.txt.Highlight the locations that match the hello word at the ending of line or string.',
								'How to highlight matching words hello at ending for line or string while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -p [CT]all list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'Call\' or \'Tall\' word was found in that pageful.',
								'Open list.txt.Highlight all locations that match the \'Call\' or \'Tall\' word.',
								'How to highlight matching words \'Call\' or \'Tall\' while searching the file = list.txt in command line?']},ignore_index = True)

#-gp
less = less.append({'Command':'less -gp hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the hello word.',
								'Open list.txt. Highlight the last locations that match the hello word.',
								'How to highlight last matching word hello while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -gp \"hello world\" list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the \"hello world\" word.',
								'Open list.txt. Highlight the last locations that match the \"hello world\" word.',
								'How to highlight last matching words \"hello world\" while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -gp h+ello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the \'ello\' word is preceded by one or more \'h\'.',
								'Open list.txt. Highlight the last locations that match \'ello\' preceded word by one or more \'h\'.',
								'How to highlight last matching words \'ello\' preceded by one or more \'h\' while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -gp hello? list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where zero or one \'o\' occurs after \'hell\'.',
								'Open list.txt.Highlight the last locations that match \'hell\' and follows zero or one \'o\'.',
								'How to highlight last matching words \'hell\' followed by zero or one \'o\' while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -gp he*llo list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the \'h\' is followed by zero or more occurences of \'e\' and again followed by \'llo\'.',
								'Open list.txt.Highlight last locations that match \'h\' followed by zero or more \'e\' and again followed by \'llo\'.',
								'How to highlight last matching words \'h\' followed by zero or more \'e\' again follwed by \'llo\' while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -gp ^hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the hello word was at the beginning of string or line.',
								'Open list.txt. Highlight the last locations that match the hello word at the starting of line or string.',
								'How to highlight last matching words hello at starting for line or string while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -gp hello$ list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the hello word was at the end of string or line.',
								'Open list.txt. Highlight the last locations that match the hello word at the ending of line or string.',
								'How to highlight last matching words hello at ending for line or string while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -gp [CT]all list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the \'Call\' or \'Tall\' word was found in that pageful.',
								'Open list.txt. Highlight the last locations that match the \'Call\' or \'Tall\' word.',
								'How to highlight last matching words \'Call\' or \'Tall\' while searching the file = list.txt in command line?']},ignore_index = True)

#-Gp
less = less.append({'Command':'less -Gp hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the locations where the hello word is present.',
								'Open list.txt. Do not highlight locations that match the hello word.',
								'Do not highlight matching word hello while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -Gp \"hello world\" list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the locations where the \"hello world\" word.',
								'Open list.txt. Do not highlight locations that match the \"hello world\" word.',
								'Do not highlight matching words \"hello world\" while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -Gp h+ello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the locations where the \'ello\' word is preceded by one or more \'h\'.',
								'Open list.txt. Do not highlight locations that match \'ello\' preceded word by one or more \'h\'.',
								'Do not highlight matching words \'ello\' preceded by one or more \'h\' while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -Gp hello? list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the locations where zero or one \'o\' occurs after \'hell\'.',
								'Open list.txt. Do not highlight locations that match \'hell\' and follows zero or one \'o\'.',
								'Do not highlight matching words \'hell\' followed by zero or one \'o\' while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -Gp he*llo list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the locations where the \'h\' is followed by zero or more occurences of \'e\' and again followed by \'llo\'.',
								'Open list.txt. Do not highlight locations that match \'h\' followed by zero or more \'e\' and again followed by \'llo\'.',
								'Do not highlight matching words \'h\' followed by zero or more \'e\' again follwed by \'llo\' while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -Gp ^hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the locations where the hello word was at the beginning of string or line.',
								'Open list.txt. Do not highlight the locations that match the hello word at the starting of line or string.',
								'Do not highlight matching words hello at starting for line or string while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -Gp hello$ list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the locations where the hello word was at the end of string or line.',
								'Open list.txt. Do not highlight the locations that match the hello word at the ending of line or string.',
								'Do not highlight matching words hello at ending for line or string while searching the file = list.txt in command line?']},ignore_index = True)

less = less.append({'Command':'less -Gp [CT]all list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the locations where the \'Call\' or \'Tall\' word was found in that pageful.',
								'Open list.txt. Do not highlight locations that match the \'Call\' or \'Tall\' word.',
								'Do not highlight matching words \'Call\' or \'Tall\' while searching the file = list.txt in command line?']},ignore_index = True)

#-Ip
less = less.append({'Command':'less -Ip hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the hello word. Ignore case while searching.',
								'Open list.txt. Highlight all locations that match the hello word. Consider small and capital letters as identical.',
								'How to highlight matching word hello while searching the file = list.txt in command line? Do not differentiate upper and lower case as different.']},ignore_index = True)

less = less.append({'Command':'less -Ip \"hello world\" list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \"hello world\" word. Ignore case while searching.',
								'Open list.txt.Highlight all locations that match the \"hello world\" word. Consider small and capital letters as identical.',
								'How to highlight matching words \"hello world\" while searching the file = list.txt in command line? Do not differentiate upper and lower case as different.']},ignore_index = True)

less = less.append({'Command':'less -Ip h+ello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'ello\' word is preceded by one or more \'h\'. Ignore case while searching.',
								'Open list.txt. Highlight all locations that match \'ello\' preceded word by one or more \'h\'. Consider small and capital letters as identical.',
								'How to highlight matching words \'ello\' preceded by one or more \'h\' while searching the file = list.txt in command line? Do not differentiate upper and lower case.']},ignore_index = True)

less = less.append({'Command':'less -Ip hello? list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where zero or one \'o\' occurs after \'hell\'. Ignore case while searching.',
								'Open list.txt. Highlight all locations that match \'hell\' and follows zero or one \'o\'. Consider small and capital letters as identical.',
								'How to highlight matching words \'hell\' followed by zero or one \'o\' while searching the file = list.txt in command line? Do not differentiate upper and lower case as different.']},ignore_index = True)

less = less.append({'Command':'less -Ip he*llo list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'h\' is followed by zero or more occurences of \'e\' and again followed by \'llo\'. Ignore case while searching.',
								'Open list.txt. Highlight all locations that match \'h\' followed by zero or more \'e\' and again followed by \'llo\'. Consider small and capital letters as identical.',
								'How to highlight matching words \'h\' followed by zero or more \'e\' again follwed by \'llo\' while searching the file = list.txt in command line? Do not differentiate upper and lower case.']},ignore_index = True)

less = less.append({'Command':'less -Ip ^hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the locations where the hello word was at the beginning of string or line. Ignore case while searching.',
								'Open list.txt.Highlight the locations that match the hello word at the starting of line or string. Consider small and capital letters as identical.',
								'How to highlight matching words hello at starting for line or string while searching the file = list.txt in command line? Do not differentiate upper and lower case.']},ignore_index = True)

less = less.append({'Command':'less -Ip hello$ list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the locations where the hello word was at the end of string or line. Ignore case while searching.',
								'Open list.txt. Highlight the locations that match the hello word at the ending of line or string. Consider small and capital letters as identical.',
								'How to highlight matching words hello at ending for line or string while searching the file = list.txt in command line? Do not differentiate upper and lower case.']},ignore_index = True)

less = less.append({'Command':'less -Ip [CT]all list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'Call\' or \'Tall\' word was found in that pageful. Ignore case while searching.',
								'Open list.txt.Highlight all locations that match the \'Call\' or \'Tall\' word. Consider small and capital letters as identical.',
								'How to highlight matching words \'Call\' or \'Tall\' while searching the file = list.txt in command line? Do not differentiate upper and lower case as different.']},ignore_index = True)

#-ip
less = less.append({'Command':'less -ip hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the hello word. Ignore case while searching if the word to be searched does not contain uppercase.',
								'Open list.txt.Highlight all locations that match the hello word. Consider small and capital letters as identical if the word to be searched does not contain capital letters.',
								'How to highlight matching word hello while searching the file = list.txt in command line? Do not differentiate upper and lower case as different if the word to be searched does not contain uppercase.']},ignore_index = True)

less = less.append({'Command':'less -ip \"hello world\" list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \"hello world\" word. Ignore case while searching if the word to be searched does not contain uppercase.',
								'Open list.txt.Highlight all locations that match the \"hello world\" word. Consider small and capital letters as identical if the word to be searched does not contain capital letters.',
								'How to highlight matching words \"hello world\" while searching the file = list.txt in command line? Do not differentiate upper and lower case as different if the word to be searched does not contain uppercase.']},ignore_index = True)

less = less.append({'Command':'less -ip h+ello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'ello\' word is preceded by one or more \'h\'. Ignore case while searching if the word to be searched does not contain uppercase.',
								'Open list.txt.Highlight all locations that match \'ello\' preceded word by one or more \'h\'. Consider small and capital letters as identical if the word to be searched does not contain capital letters.',
								'How to highlight matching words \'ello\' preceded by one or more \'h\' while searching the file = list.txt in command line? Do not differentiate upper and lower case as different if the word to be searched does not contain uppercase.']},ignore_index = True)

less = less.append({'Command':'less -ip hello? list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where zero or one \'o\' occurs after \'hell\'. Ignore case while searching if the word to be searched does not contain uppercase.',
								'Open list.txt.Highlight all locations that match \'hell\' and follows zero or one \'o\'. Consider small and capital letters as identical if the word to be searched does not contain capital letters.',
								'How to highlight matching words \'hell\' followed by zero or one \'o\' while searching the file = list.txt in command line? Do not differentiate upper and lower case as different if the word to be searched does not contain uppercase.']},ignore_index = True)

less = less.append({'Command':'less -ip he*llo list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'h\' is followed by zero or more occurences of \'e\' and again followed by \'llo\'. Ignore case while searching if the word to be searched does not contain uppercase.',
								'Open list.txt.Highlight all locations that match \'h\' followed by zero or more \'e\' and again followed by \'llo\'. Consider small and capital letters as identical if the word to be searched does not contain capital letters.',
								'How to highlight matching words \'h\' followed by zero or more \'e\' again follwed by \'llo\' while searching the file = list.txt in command line? Do not differentiate upper and lower case as different if the word to be searched does not contain uppercase.']},ignore_index = True)

less = less.append({'Command':'less -ip ^hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the locations where the hello word was at the beginning of string or line. Ignore case while searching if the word to be searched does not contain uppercase.',
								'Open list.txt. Highlight the locations that match the hello word at the starting of line or string. Consider small and capital letters as identical if the word to be searched does not contain capital letters.',
								'How to highlight matching words hello at starting for line or string while searching the file = list.txt in command line? Do not differentiate upper and lower case as different if the word to be searched does not contain uppercase.']},ignore_index = True)

less = less.append({'Command':'less -ip hello$ list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the locations where the hello word was at the end of string or line. Ignore case while searching if the word to be searched does not contain uppercase.',
								'Open list.txt.Highlight the locations that match the hello word at the ending of line or string. Consider small and capital letters as identical if the word to be searched does not contain capital letters.',
								'How to highlight matching words hello at ending for line or string while searching the file = list.txt in command line? Do not differentiate upper and lower case as different if the word to be searched does not contain uppercase.']},ignore_index = True)

less = less.append({'Command':'less -ip [CT]all list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'Call\' or \'Tall\' word was found in that pageful. Ignore case while searching if the word to be searched does not contain uppercase.',
								'Open list.txt.Highlight all locations that match the \'Call\' or \'Tall\' word. Consider small and capital letters as identical if the word to be searched does not contain capital letters.',
								'How to highlight matching words \'Call\' or \'Tall\' while searching the file = list.txt in command line? Do not differentiate upper and lower case as different if the word to be searched does not contain uppercase.']},ignore_index = True)

#-jp
less = less.append({'Command':'less -j5p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the hello word. Display the first found location at line 5.',
								'Open list.txt. Highlight all locations that match the hello word. Display the first found location at line 5.',
								'How to highlight matching word hello while searching the file = list.txt in command line? Display the first found location at line 5.']},ignore_index = True)

less = less.append({'Command':'less -j5p \"hello world\" list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \"hello world\" word. Display the first found location at line 5.',
								'Open list.txt.Highlight all locations that match the \"hello world\" word. Display the first found location at line 5.',
								'How to highlight matching words \"hello world\" while searching the file = list.txt in command line? Display the first found location at line 5.']},ignore_index = True)

less = less.append({'Command':'less -j5p h+ello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'ello\' word is preceded by one or more \'h\'. Display the first found location at line 5.',
								'Open list.txt.Highlight all locations that match \'ello\' preceded word by one or more \'h\'. Display the first found location at line 5.',
								'How to highlight matching words \'ello\' preceded by one or more \'h\' while searching the file = list.txt in command line? Display the first found location at line 5.']},ignore_index = True)

less = less.append({'Command':'less -j5p hello? list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where zero or one \'o\' occurs after \'hell\'. Display the first found location at line 5.',
								'Open list.txt. Highlight all locations that match \'hell\' and follows zero or one \'o\'. Display the first found location at line 5.',
								'How to highlight matching words \'hell\' followed by zero or one \'o\' while searching the file = list.txt in command line? Display the first found location at line 5.']},ignore_index = True)

less = less.append({'Command':'less -j5p he*llo list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'h\' is followed by zero or more occurences of \'e\' and again followed by \'llo\'. Display the first found location at line 5.',
								'Open list.txt.Highlight all locations that match \'h\' followed by zero or more \'e\' and again followed by \'llo\'. Display the first found location at line 5.',
								'How to highlight matching words \'h\' followed by zero or more \'e\' again follwed by \'llo\' while searching the file = list.txt in command line? Display the first found location at line 5.']},ignore_index = True)

less = less.append({'Command':'less -j5p ^hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the locations where the hello word was at the beginning of string or line. Display the first found location at line 5.',
								'Open list.txt.Highlight the locations that match the hello word at the starting of line or string. Display the first found location at line 5.',
								'How to highlight matching words hello at starting for line or string while searching the file = list.txt in command line? Display the first found location at line 5.']},ignore_index = True)

less = less.append({'Command':'less -j5p hello$ list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the locations where the hello word was at the end of string or line. Display the first found location at line 5.',
								'Open list.txt. Highlight the locations that match the hello word at the ending of line or string. Display the first found location at line 5.',
								'How to highlight matching words hello at ending for line or string while searching the file = list.txt in command line? Display the first found location at line 5.']},ignore_index = True)

less = less.append({'Command':'less -j5p [CT]all list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the \'Call\' or \'Tall\' word was found in that pageful. Display the first found location at line 5.',
								'Open list.txt. Highlight all locations that match the \'Call\' or \'Tall\' word. Display the first found location at line 5.',
								'How to highlight matching words \'Call\' or \'Tall\' while searching the file = list.txt in command line? Display the first found location at line 5.']},ignore_index = True)

#######
less = less.append({'Command':'less -gIp hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the hello word. Ignore case while searching.',
								'Open list.txt. Highlight the last locations that match the hello word. Do not differentiate uppercase with lowercase.',
								'How to highlight last matching word hello while searching the file = list.txt in command line? Consider lowercase and uppercase as one.']},ignore_index = True)

less = less.append({'Command':'less -gip hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the hello word. Ignore case while searching if the searched word does not contain upper case.',
								'Open list.txt. Highlight the last locations that match the hello word. Do not differentiate uppercase with lowercase if the word to be searched does not contain upper case.',
								'How to highlight last matching word hello while searching the file = list.txt in command line? Consider lowercase and uppercase as one if searching word does not contain uppercase.']},ignore_index = True)

less = less.append({'Command':'less -GIp hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the last locations where the hello word. Ignore case while searching.',
								'Open list.txt in "less" mode. Do not highlight the last locations that match the hello word. Do not differentiate uppercase with lowercase.',
								'Do not highlight last matching word hello while searching the file = list.txt in command line? Consider lowercase and uppercase letters the same.']},ignore_index = True)

less = less.append({'Command':'less -Gip hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, do not highlight the last locations where the hello word. Ignore case while searching if the searched word does not contain upper case.',
								'Open list.txt. Do not highlight the last locations that match the hello word. Do not differentiate uppercase with lowercase if the word to be searched does not contain upper case.',
								'Do not highlight last matching word hello while searching the file = list.txt in command line? Consider lowercase and uppercase as one if searching word does not contain uppercase.']},ignore_index = True)

less = less.append({'Command':'less -i~p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the hello word. Ignore case while searching if the word to be searched does not contain uppercase and do not show tilda at end of file.',
								'Open list.txt.Highlight all locations that match the hello word. Consider small and capital letters as identical if the word to be searched does not contain capital letters and do not show tilda at end.',
								'How to highlight matching word hello while searching the file = list.txt in command line? Do not differentiate upper and lower case as different if the word to be searched does not contain uppercase and do not show tilda at end of file.']},ignore_index = True)

less = less.append({'Command':'less -IJ~p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations and respective lines where the hello word. Ignore case while searching and do not show tilda at end of file.',
								'Open list.txt. Highlight all locations and respective lines of highlighted locations that match the hello word. Consider small and capital letters as identical and do not show tilda at end of file.',
								'How to highlight matching word hello and respective lines of highlighted locations while searching the file = list.txt in command line? Do not differentiate upper and lower case as different and do not show tilda at end of file.']},ignore_index = True)

less = less.append({'Command':'less +5 -IJp hello list.txt',
					'NL Queries':['Open list.txt in command line from 5th line, one pageful at a time. While searching, highlight the all locations and respective lines of highlighted locations where the hello word. Ignore case while searching.',
								'Open list.txt. Skip first 4 lines. Highlight all locations and respective lines of highlighted locations that match the hello word. Consider small and capital letters as identical.',
								'How to highlight matching word hello and respective lines of highlighted locations while searching the file = list.txt in command line? Do not differentiate upper and lower case as different. Skip the first 4 lines.']},ignore_index = True)

less = less.append({'Command':'less +5 -gIJp hello list.txt',
					'NL Queries':['Open list.txt in command line from 5th line, one pageful at a time. While searching, highlight the last locations and respective line of highlighted location where the hello word. Ignore case while searching.',
								'Open list.txt. Skip first 4 lines. Highlight last locations that match the hello word and respective line of highlighted location. Consider small and capital letters as identical.',
								'How to highlight last matching word hello and respective line of highlighted location while searching the file = list.txt in command line? Do not differentiate upper and lower case as different. Skip the first 4 lines.']},ignore_index = True)

less = less.append({'Command':'less -gJj4p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the hello word and display the highlighted location at line 4. Display status of each line.',
								'Open list.txt. Highlight the last locations that match the hello word. Display the highlighted location at line 4. Display status of each line.',
								'How to highlight last matching word hello while searching the file = list.txt in command line? Display the highlighted location at line 4. Display status of each line.']},ignore_index = True)

less = less.append({'Command':'less -gJj4~p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the hello word and display the highlighted location at line 4. Do not show tilda at start or end of file. Display status of each line.',
								'Open list.txt. Highlight the last locations that match the hello word. Display the highlighted location at line 4 Do not show tilda at start or end of file. Display status of each line.',
								'How to highlight last matching word hello while searching the file = list.txt in command line? Display the highlighted location at line 4. Do not show tilda at start or end of file. Display status of each line.']},ignore_index = True)

less = less.append({'Command':'less -gJIj4~p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching ignore case, highlight the last locations where the hello word and display the highlighted location at line 4. Do not show tilda at start or end of file. Display status of each line.',
								'Open list.txt.Highlight the last locations that match the hello word. Ignore case while searching. Display the highlighted location at line 4 Do not show tilda at start or end of file. Display status of each line.',
								'How to highlight last matching word hello while searching the file = list.txt case insensitively in command line? Display the highlighted location at line 4. Do not show tilda at start or end of file. Display status of each line.']},ignore_index = True)

less = less.append({'Command':'less -I~p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the all locations where the hello word. Ignore case while searching and do not show tilda at end of file.',
								'Open list.txt.Highlight all locations that match the hello word. Consider small and capital letters as identical and do not show tilda at end of file.',
								'How to highlight matching word hello while searching the file = list.txt in command line? Do not differentiate upper and lower case as different and do not show tilda at end of file.']},ignore_index = True)

less = less.append({'Command':'less +5 -Ip hello list.txt',
					'NL Queries':['Open list.txt in command line from 5th line, one pageful at a time. While searching, highlight the all locations where the hello word. Ignore case while searching.',
								'Open list.txt. Skip first 4 lines. Highlight all locations that match the hello word. Consider small and capital letters as identical.',
								'How to highlight matching word hello while searching the file = list.txt in command line? Do not differentiate upper and lower case as different. Skip the first 4 lines.']},ignore_index = True)

less = less.append({'Command':'less +5 -gIp hello list.txt',
					'NL Queries':['Open list.txt in command line from 5th line, one pageful at a time. While searching, highlight the last locations where the hello word. Ignore case while searching.',
								'Open list.txt. Skip first 4 lines. Highlight last locations that match the hello word. Consider small and capital letters as identical.',
								'How to highlight last matching word hello while searching the file = list.txt in command line? Do not differentiate upper and lower case as different. Skip the first 4 lines.']},ignore_index = True)

less = less.append({'Command':'less -gj4p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the hello word and display the highlighted location at line 4.',
								'Open list.txt.Highlight the last locations that match the hello word. Display the highlighted location at line 4.',
								'How to highlight last matching word hello while searching the file = list.txt in command line? Display the highlighted location at line 4.']},ignore_index = True)

less = less.append({'Command':'less -gj4~p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching, highlight the last locations where the hello word and display the highlighted location at line 4. Do not show tilda at start or end of file.',
								'Open list.txt.Highlight the last locations that match the hello word. Display the highlighted location at line 4 Do not show tilda at start or end of file..',
								'How to highlight last matching word hello while searching the file = list.txt in command line? Display the highlighted location at line 4. Do not show tilda at start or end of file.']},ignore_index = True)

less = less.append({'Command':'less -gIj4~p hello list.txt',
					'NL Queries':['Open list.txt in command line, one pageful at a time. While searching ignore case, highlight the last locations where the hello word and display the highlighted location at line 4. Do not show tilda at start or end of file.',
								'Open list.txt.Highlight the last locations that match the hello word. Ignore case while searching. Display the highlighted location at line 4. Do not show tilda at start or end of file..',
								'How to highlight last matching word hello while searching the file = list.txt in command line with ignoring case? Display the highlighted location at line 4. Do not show tilda at start or end of file.']},ignore_index = True)


#less.to_csv('/home/ananyaraval/Documents/Thesis/Data/UNIX/Model/csv_files/less.csv',index=False)
print less.shape


