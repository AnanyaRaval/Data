import pandas as pd 

sed = pd.DataFrame(columns = ['Command','NL Queries'])

sed = sed.append({'Command':'sed \'$d\' file.txt','NL Queries':['Remove last line of file.txt.',
						'Keep all contents of file.txt but the last line.',
						'How do I remove last line of file.txt?']},ignore_index = True)

sed = sed.append({'Command':"sed 's/^[ ^t]*//;s/[ ^]*$//' name.txt",'NL Queries':['Remove spaces in front and back of each line for name.txt',
							'How do I remove spaces before and after each line of name.txt?']},ignore_index = True)

sed = sed.append({'Command':'sed \'s/Nick/John/g\' report.txt','NL Queries':['Replace every occurance of Nick with John in file report.txt',
					'How do I replace all \'Nick\' with \'John\' in report.txt?',
						'Replace word Nick with John in report.txt. All words need to be replaced.']},ignore_index = True)

sed = sed.append({'Command':'sed -n \'5,10p\' hello.txt','NL Queries':['How to display the lines 5-10 from the file hello.txt?',
				'Display the lines 5-10 from the file hello.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'20,35d\' myfile.txt','NL Queries':['How to display all lines in the file myfile.txt excluding lines 20-35?',
					'Display lines from file myfile.txt excluding 20-35.','Show content of myfile.txt. Do not include lines 20-35.']},ignore_index=True)

sed = sed.append({'Command':'sed -n -e \'5,7p\' -e \'10,13p\' set.txt','NL Queries':['How to display the lines 5-7 and 10-13 from the file set.txt?',
					'Display the lines 5-7 10-13 in the file set.txt.','Show contents only between liens 5 and 7 and 10 and 13.']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/tom/larry/gi\' new.txt','NL Queries':['Replace every occurrence of tom with larry case insensitive in the file new.txt.',
					'How to replace \'tom\' with \'larry\' cases insensitive in the file new.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'30,40 s/old/new/g\' myfile.txt','NL Queries':['Replace the occurrence of \'old\' with \'new\' in the lines 30-40 in the file myfile.txt',
				'How to replace old with new in the lines 30-40 in the file myfile.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed -n \'/^hello/ p\' hello.txt','NL Queries':['Print the lines which start with the word \'hello\' from the file hello.txt.',
				'How to display the lines which start with the word hello from the file hello.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed G game.txt','NL Queries':['How to display the lines of the file game.txt with an empty line after every non empty line?',
							'Display the lines of the file game.txt with a blank line after every non-blank line.']},ignore_index=True)

sed = sed.append({'Command':'sed -i \'s/word1/word2/gi;s/word3/word4/gi\' myfile.txt','NL Queries':['How to replace \'word1\' with \'word2\' and \'word3\' with \'word34\' in the file myfile.txt?',
					'Replace word1 with word2 and word3 with word4 in the file myfile.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/unix/linux/3g\' file.txt','NL Queries':['How to replace the word unix with the word linux from the 3rd occurrence of linux in the line file.txt?',
					'Replace the word unix with the word linux from the 3rd occurrence of linux in the line of file.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed -n \'s/unix/linux/p\' jokes.txt','NL Queries':['How to print only the replaced lines after replacing unix with linux in the file jokes.txt?',
					'Print only the replaced lines after replacing unix with linux in the file jokes.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'1 d\' new1.txt','NL Queries':['How to delete the first line from the file new1.txt?',
					'Delete the first line from the file new1.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'p\' new1.txt','NL Queries':['How to print all the lines twice in the file new1.txt?'
							,'Display all the lines twice in the file new1.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed --version','NL Queries':['How to check the version of the command sed?',
							'Check the version of the commmand sed.']},ignore_index=True)

sed = sed.append({'Command':'sed --help','NL Queries':['How do I get the description of various flags for the sed command?',
					'Display the various options available with the sed command along with description.']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/Nick|nick/John/g\' report.txt > report_new.txt','NL Queres':['How to change Nick or nick in the file report to John and save it in a file report_new.txt',
								'Change Nick or nick to John. Save it as report_new.txt.','Change every occurrence of Nick/nick to John from report.txt and save it as report_new.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/^/ /\' file.txt >file_new.txt','NL Queries':['Add a space at the beginning  of each line in file.txt and save it as file_new.txt.',
					'How do I add a space to the beginning of each line from file.txt and save it as file_new.txt',
							'Add space for each line in file.txt. Save it as file_new.txt']},ignore_index=True)

sed = sed.append({'Command':'sed -n \'/Of course/,/attention you \pay/p\' myfile','NL Queries':['Display only one paragraph starting with \'Of course\' and ending with \'attention you pay\' from file myfile.',
						'How do I get only one paragraph starting with \'Of coursee and ending with \'attention you pay in the file myfile\'?']},ignore_index=True)

sed = sed.append({'Command':'sed \'5!s/ham/cheese/\' file.txt','NL Queries':['Replace ham with cheese except the occurrence in fifth line in the file file.txt.',
					'How do I replace \'ham\' with \'cheese\' excluding the 5th line in th e file file.txt?',
						'Replace \'ham\' with \'cheese\' from the file file.tx leaving the 5th line as it is.']},ignore_index=True)

sed = sed.append({'Command':'sed \'/[0-9]\{3\}/p\' file.txt','NL Queries':['Print only lines with three consecutive digits from the file file.txt',
				'How do I print lines with three consecutive digits from the file file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'/boom/!s/aaa/bb/\' file.txt','NL Queries':['Unless boom is found, replace aaa with bb in the file \'file.txt\'',
					'How do I replace aaa with bb in the file \'file.txt\' if boom is not found?',
							'Replace every occurrence of \'aaa\' with \'boom\' in the file \'file.txt\' if \'boom\' is not found.']},ignore_index=True)

sed = sed.append({'Command':'sed \'17,/disk/d\' file.txt','NL Queries':['Delete all lines from line 17 to \'disk\' in file.txt.',
					'How to delete all lines from line 17 to disk in file file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/one/unos/I\' game.txt','NL Queries':['Replace case insensitive occurrence of one with unos in game.txt',
					'How do I replace case insensitive occurrence of \'one\' with \'unos\' in game.txt']},ignore_index=True)

sed = sed.append({'Command':'sed \'G;G\' new.txt','NL Queries':['Leave 2 lines gap between each line in new.txt.',
					'How do I space every line in new.txt with two blank lines?',
						'Space every line with two blank lines in new.txt']},ignore_index=True)
sed = sed.append({'Command':'sed \'s/^[ ^t]*//\' file.txt','NL Queries':['Delete all spaces in front of every line in \'file.txt\'',
				'Remove all spaces before every line in file.txt.',
					'How do I remove all unnecessary spaces in front of each line in file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/[ ^t]*$//\' file.txt','NL Queries':['Delete all spaces in the end of every line in \'file.txt\'',
				'Remove all spaces in the end of every line in file.txt.',
					'How do I remove all unnecessary spaces in end of each line in file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/foo/bar/\' file.txt','NL Queries':['Replace first occurrence of foo with bar in \'file.txt\' in a line',
					'How do I replace the first occurrence of foo with bar in file.txt in a line?']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/foo/bar/4\' file.txt','NL Queries':['Replace foo with bar only for the 4th instance in a line in the file file.txt.',
				'How do I replace foo with bar only in the fourth occurrence in a line in file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'/baz/s/foo/bar/g\' file.txt','NL Queries':['Only if line contains baz, substitute foo with bar in file.txt.',
			'Substitue foo with bar in file.txt if the line contains \'baz\'',
				'How do I replace foo with bar in a line only if contains baz in file.txt']},ignore_index=True)

sed = sed.append({'Command':'sed \'/./,/^$/!d\' file.txt','NL Queries':['Delete all consecutive blank line except EOL in file.txt.',
	'How do I delete all consecutive blank lines in file.txt except the EOL?']},ignore_index=True)

sed = sed.append({'Command':'sed \'/^$/N;/\n$/D\' file.txt','NL Queries':['Delete all consecutive blank lines, but allow top line in file.txt.',
				'How do I delete consecutive blank lines except the top line in file.txt?',
						'Leave the top line and delete all other blank lines in file.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'/./,$!d\' file.txt','NL Queries':['Delete all leading blank lines in file.txt.',
			'How do I delete all leading blank lines in file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed -e :a -e \'/^\n*$/{$d;N;};/\n$/ba\' file.txt','NL Queries':['Delete all trailing blank lines in file.txt.',
			'How do I delete all trailing blank lines in file.txt']},ignore_index=True)

sed = sed.append({'Command':'sed \'1~3d\' file.txt','NL Queries':['Delete every third line, starting with the first in file.txt'
				,'How do I delete lines which are multiples of 3 in file.txt?','Delete lines which are multiples of 3 in file.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed -n \'2~5p\' file.txt','NL Queries':['Print every 5th line starting with the second in file.txt',
			'How to print every fifth line starting with the second in file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/^[^,]*,/9999,/\' file.csv','NL Queries':['Change first field to 9999 in a CSV file \'file.csv\'',
				'How to change the first field to 9999 in a CSV file file.csv?']},ignore_index=True)

sed = sed.append({'Command':'sed -r \'s/\<(reg|exp)[a-z]+/\U&/g\' file.txt','NL Queries':['Convert any word starting with reg or exp to uppercase',
					'How do I convert any word starting with reg or exp to uppercase?']},ignore_index=True)

sed = sed.append({'Command':'sed \'1,20 s/Johnson/White/g\' file.txt','NL Queries':['Do replacement of Johnson with White in lines 1-20 in file.txt',
				'How do I change Johnson to White in lines 1-20 of file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'1,20 !s/Johnson/White/g\' file.txt','NL Queries':['Do replacement of Johnson with White in all lines excluding 1-20 in file.txt.',
				'How do I replace Johnson with White in every occurence excluding lines 1-20 in file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/[a-g]//g\' jokes.txt','NL Queries':['Remove all characters from a to g in jokes.txt.',
				'How do I remove characters a-g in jokes.txt?','Delete characters which are characters between a to g inclusive in jokes.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed \'s/\(.*\)foo/bar/\' file.txt','NL Queries':['Remove only the last match of foo with bar in file.txt.',
				'How do I remove the last match of foo with bar in file.txt?','Find the last occurrence of foo in file.txt and replace it with bar.']},ignore_index=True)

sed = sed.append({'Command':'sed \'/./!d\' file.txt','NL Queries':['Delete all blank lines from file file.txt.',
				'How do I remove all blank lines in file.txt?','Remove blank lines in file.txt.']},ignore_index=True)

sed = sed.append({'Command':'sed -n \'/^$/{p;h;};/./{x;/./p;}\' file.txt','NL Queries':['Delete the last line of every paragraph in file.txt.',
				'How do I delete the last line of every paragraph in file.txt?',
					'Remove last line of ever paragraph in file.txt']},ignore_index=True)

sed = sed.append({'Command':'sed -e :a -e \'s/<[^>]*>//g;/</N;//ba\' play.txt','NL Queries':['Remove all HTML tags in play.txt.',
					'How do I remove all HTML tags from play.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed \'/./{H;d;};x;s/\n/={NL}=/g\' file.txt | sort | sed \'1s/={NL}=//;s/={NL}=/\n/g\'','NL Queries':['Sort the paragraphs of file.txt alphabetically.',
				'How do I sort the paragraphs in file.txt alphabetically?']},ignore_index=True)

sed = sed.append({'Command':'sed -n \'/^.\{65\}/p\' printer.txt','NL Queries':['Print lines which are 65 characters or more in printer.txt.',
				'How do I print the lines which contain more than equal to 65 characters from the file printer.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed -n \'/^.\{65\}/!p\' file.txt','NL Queries':['How do I print the lines which contain 65 characters or less in file.txt?',
				'Print the lines which contain less than equal to 65 characters in file.txt,']},ignore_index=True)

sed = sed.append({'Command':'sed = file.txt | sed \'N;s/\n/\t/\'','NL Queries':['Number all the lines in file.txt.',
			'How do I number all the lines in file.txt?']},ignore_index=True)

sed = sed.append({'Command':'sed -e :a -e \'s/^.\{1,77\}$/ &/;ta\' -e ','NL Queries':['Align all text entered in terminal to center and output it.',
				'How do I align standard input in terminal to the center and output it?']},ignore_index=True)


print sed.shape