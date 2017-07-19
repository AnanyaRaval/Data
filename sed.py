import pandas as pd 

sed = pd.DataFrame(columns = ['Command','NL Queries'])

sed = sed.append({'Command':'sed \'$d\' file.txt','NL Queries':['Remove last line of file.txt.','Keep all contents of file.txt but the last line.',
													'How do I remove last line of file.txt?']},ignore_index = True)

sed = sed.append({'Command':"sed 's/^[ ^t]*//;s/[ ^]*$//' name.txt",'NL Queries':['Remove spaces in front and back of each line for name.txt',
													'How do I remove spaces before and after each line of name.txt?']},ignore_index = True)

sed = sed.append({'Command':'sed \'s/Nick/John/g\' report.txt','NL Queries':['Replace every occurance of Nick with John in file report.txt','How do I replace all \'Nick\' with \'John\' in report.txt?',
														'Replace word Nick with John in report.txt. All words need to be replaced.',
														'Change every occurance of Nick with the word John in report.txt.']},ignore_index = True)

sed = sed.append({'Command':'sed -n \'5,10p\' hello.txt','NL Queries':['How to display the lines 5-10 from the file hello.txt?',
															'Display the lines 5-10 from the file hello.txt.',
															'Show contents of hello.txt from line 5 to line 10.']},ignore_index=True)

sed = sed.append({'Command':'sed \'20,35d\' myfile.txt','NL Queries':['How to display all lines in the file myfile.txt excluding lines 20-35?',
														'Display lines from file myfile.txt excluding lines 20-35.',
														'Show all contents of myfile.txt except between lines 20 and 35.']},ignore_index=True)

sed = sed.append({'Command':'sed -n -e \'5,7p\' -e \'10,13p\' set.txt','NL Queries':['How to display the lines 5-7 and 10-13 from the file set.txt?',
								'Display the lines 5-7 and 10-13 in the file set.txt.','Show content of set.txt between lines 5 and 7 and lines 10 and 13.']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/tom/larry/gi\' new.txt','NL Queries':['Replace every occurence of tom with larry case insensitive in the file new.txt.','How to replace \'tom\' with \'larry\' cases insensitive in the file new.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'30,40 s/old/new/g\' myfile.txt','NL Queries':['Replace the occurence of \'old\' with \'new\' in the lines 30-40 in the file myfile.txt','How to replace old with new in the lines 30-40 in the file myfile.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed -n \'/^hello/ p\' hello.txt','NL Queries':['Print the lines which start with the word \'hello\' from the file hello.txt.','How to display the lines which start with the word hello from the file hello.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed G game.txt','NL Queries':['How to display the lines of the file game.txt with an empty line after every non empty line?','Displays the lines of the file game.txt with a blank line after every non-blank line.']},ignore_index=True)

sed = sed.append({'Command':'sed -i \'s/word1/word2/gi;s/word3/word4/gi\' myfile.txt','NL Queries':['How to replace \'word1\' with \'word2\' and \'word3\' with \'word3\' in the file myfile.txt?','Replace word1 with word2 and word3 with word4 in the file myfile.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/unix/linux/3g\' file.txt','NL Queries':['How to replace the word unix with the word linux from the 3rd occurence of linux in the line?','Replace the qord unix with the word linux from the 3rd occurence of linux in the line.']},ignore_index=True)

sed = sed.append({'Command':'sed -n \'s/unix/linux/p\' jokes.txt','NL Queries':['How to print only the replaced lines after replacing unix with linux in the file jokes.txt?','Print only the replaced lines after replacing unix with linux in the file jokes.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'1 d\' new1.txt','NL Queries':['How to delete the first line from the file new1.txt?','Deletes the first line from the file new1.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'p\' new1.txt','NL Queries':['How to print all the lines twice in the file new1.txt?','Display all the lines twice in the file new1.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed --version','NL Queries':['How to check the version of the command sed?','Checks the version of the commmand sed.']},ignore_index=True)

sed = sed.append({'Command':'sed --help','NL Queries':['How do I get the description of various flags for the sed command?','Displays the various options available with the sed command along with description.']},ignore_index=True)


print sed.shape