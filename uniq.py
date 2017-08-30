import pandas as pd 

uniq = pd.DataFrame(columns = ['Command','NL Queries'])

uniq = uniq.append({'Command':'uniq myfile.txt','NL Queries':['Display all unique lines in the file myfile.txt.',
															'Filter all unique lines from myfile.txt.',
															'Command to check all distinct lines in myfile.txt.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -d documents.txt','NL Queries':['Show only repeated lines from documents.txt.',
																	'Display contents of documents.txt. Show lines, which have count more than 1, of file documents.txt.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq samplefile.txt','NL Queries':['Show samplefile.txt without consecutive duplicate lines.',
																	'From samplefile.txt display all unique lines.',
																	'How to see only unique lines from the file samplefile.txt?',
																	'Single command to filter unique lines from samplefile.txt']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c sample.txt','NL Queries':['Prefix each line with its number of consecutive occurences in the file sample.txt.',
																'Display the number of instances of each line in the file sample.txt.',
																'How to see how many times each line occurs in the file sample.txt?',
																'Show each line in the file sample.txt with the number of times it occurs consecutively.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -d test','NL Queries':['Print only the lines that have multiple consecutive occurences in the file test.',
															'Display only continuous repeated lines from the file test.',
															'How to filter out only continuous repeated lines from the file test?',
															'Single command to see only continuous repeated lines in the file test.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -D samarth.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file samarth.txt as many times as they occur in the file.',
																'Display only continuous repeated lines from the file samarth.txt as many times as they repeat.',
																'How to filter out only repeated lines from the file samarth.txt? Print each line as many times as it occurs in the file.',
																'Single command to see only repeated lines in the file samarth.txt as many times as they occur in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -f 3 ananya.txt','NL Queries':['Show ananya.txt without consecutive duplicate lines. Ignore first 3 fields when comparing lines.',
																'Ignore first 3 fields while comparing lines and display only unique lines from the file ananya.txt on the command line.',
																'How to see unique lines from ananya.txt irrespective of the first 3 fields?',
																'Single command to see only unique lines from ananya.txt while ignoring first 3 fields when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -i tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines. Ignore case when comparing lines.',
																'Ignore case while comparing lines and display only unique lines from the file tutorial.txt on the command line.',
																'How to see unique lines from tutorial.txt irrespective of case?',
																'Single command to see only unique lines from tutorial.txt while ignoring case when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -s 8 tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines. Don\'t consider the first 8 characters of each line when comparing them.',
																	'Don\'t consider the first 8 characters while comparing lines and display only unique lines from the file tutorial.txt on the command line.',
																	'How to see unique lines from tutorial.txt? Ignore first 8 characters when comparing the lines.',
																	'Single command to see only unique lines from tutorial.txt while avoiding first 8 characters when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -u instructions.txt','NL Queries':['Print only non-repeating lines in the file instructions.txt on command line.',
																		'Show lines of instructions.txt which have count = 1.',
																		'Show only those lines that do not have multiple consecutive occurences in textfile.txt.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -w 8 tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines. Consider only the first 8 characters of each line when comparing them.',
																	'Consider first 8 characters while comparing lines and display only unique lines from the file tutorial.txt on the command line.',
																	'How to see unique lines from tutorial.txt? Only consider first 8 characters when comparing the lines.',
																	'Single command to see only unique lines from tutorial.txt while taking first 8 characters into account when comparing lines.']},ignore_index=True)

###

uniq = uniq.append({'Command':'uniq --help','NL Queries':['Show all options of uniq command.',
														'What all can be done using uniq command?',
														'What are the options available with uniq command?',
														'Display all the additions that can be made to the uniq command.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq --version','NL Queries':['Show version of uniq command.',
															'Who wrote uniq command?',
															'What is the version of uniq command?',
															'Who is the author of uniq command?']},ignore_index=True)

###

uniq = uniq.append({'Command':'uniq -c -d myfile.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file myfile.txt along with the number of occurences.',
																'Display only continuous repeated lines from the file myfile.txt. Prefix each line with it\'s number of occurences.',
																'How to filter out only continuous repeated lines from the file myfile.txt along with the number of times they repeat?',
																'Single command to see only continuous repeated lines in the file myfile.txt and the number of repetitions.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -f 4 start.txt','NL Queries':['Show start.txt without consecutive duplicate lines along with the number of occurences. Ignore first 4 fields when comparing lines.',
																	'Ignore first 4 fields while comparing lines and display only unique lines from the file start.txt on the command line. Prefix the number of times each line repeats.',
																	'How to see unique lines from start.txt irrespective of first 4 fields along with the number of consecutive repetitions in the file?',
																	'Single command to see only unique lines from start.txt while ignoring first 4 fields when comparing lines. Also display the number of times each line repeats in the file consecutively.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -i tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines along with the number of occurences. Ignore case when comparing lines.',
																	'Ignore case while comparing lines and display only unique lines from the file tutorial.txt on the command line. Prefix the number of times each line repeats.',
																	'How to see unique lines from tutorial.txt irrespective of case along with the number of consecutive repetitions in the file?',
																	'Single command to see only unique lines from tutorial.txt while ignoring case when comparing lines. Also display the number of times each line repeats in the file consecutively.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -s 8 tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines. Don\'t consider the first 8 characters of each line when comparing them. Prefix each line with the number of times it consecutively repeats in the file.',
																		'Don\'t consider the first 8 characters while comparing lines and display only unique lines from the file tutorial.txt on the command line along with it\'s number of occurences.',
																		'How to see unique lines from tutorial.txt? Ignore first 8 characters when comparing the lines and print the number of times each line repeats consecutively in the file.',
																		'Single command to see only unique lines from tutorial.txt while avoiding first 8 characters when comparing lines. The output should also include the number of times each line repeats consecutively in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -w 8 tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines. Consider only the first 8 characters of each line when comparing them. The output should also include the number of times each line repeats consecutively in the file.',
																		'Consider first 8 characters while comparing lines and display only unique lines from the file tutorial.txt on the command line along with it\'s number of occurences in the file.',
																		'How to see unique lines from tutorial.txt? Only consider first 8 characters when comparing the lines and print the number of times each line repeats consecutively in the file.',
																		'Single command to see only unique lines from tutorial.txt while taking first 8 characters into account when comparing lines. Prefix each line with the number of times it consecutively repeats in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -d -f 2 sample.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file sample.txt. Ignore first 2 fields when comparing lines.',
																		'Ignore first 2 fields when comparing lines and display only continuous srepeated lines from the file sample.txt.',
																		'How to filter out only continuous repeated lines from the file sample.txt while ignoring first 2 fields during comparison?',
																		'Single command to see only continuous repeated lines in the file sample.txt irrespective of first 2 fields.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -d -i sample.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file sample.txt. Ignore case when comparing lines.',
																	'Ignore case when comparing lines and display only continuous repeated lines from the file sample.txt.',
																	'How to filter out only continuous repeated lines from the file sample.txt while ignoring case during comparison?',
																	'Single command to see only  continuous repeated lines in the file sample.txt irrespective of case.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -d -s 10 tutorial.txt','NL Queries':['Show tutorial.txt with lines that have multiple consecutive occurences. Don\'t consider the first 10 characters of each line when comparing them.',
																		'Don\'t consider the first 10 characters while comparing lines and display only those lines that repeat consecutively in the file tutorial.txt on the command line.',
																		'How to see only repeated lines from tutorial.txt? Ignore first 10 characters when comparing the lines.',
																		'Single command to see only repeated lines from tutorial.txt while avoiding first 10 characters when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -d -w 10 tutorial.txt','NL Queries':['From tutorial.txt, only show lines that have multiple consecutive occurences. Consider only the first 10 characters of each line when comparing them.',
																		'Consider first 10 characters while comparing lines and display only consecutive repeated lines from the file tutorial.txt on the command line.',
																		'How to see lines with multiple consecutive occurences from tutorial.txt? Only consider first 10 characters when comparing the lines.',
																		'Single command to see only consecutive repeated lines from tutorial.txt while taking only first 10 characters into account when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -D -f 5 moons.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file moons.txt as many times as they occur in the file. Ignore first 5 fields when comparing lines.',
																	'Display only repeated lines from the file moons.txt as many times as they repeat irrespective of first 5 fields.',
																	'How to filter out only repeated lines from the file moons.txt without considering first 5 fields when comparing lines? Print each line as many times as it occurs in the file.',
																	'Single command to see only repeated lines in the file moons.txt as many times as they occur in the file irrespective of first 5 fields.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -D -i scrolls.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file scrolls.txt as many times as they occur in the file. Ignore case when comparing lines.',
																	'Display only repeated lines from the file scrolls.txt as many times as they repeat irrespective of case.',
																	'How to filter out only repeated lines from the file scrolls.txt without considering case when comparing lines? Print each line as many times as it occurs in the file.',
																	'Single command to see only repeated lines in the file scrolls.txt as many times as they occur in the file irrespective of case.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -D -s 7 sides.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file sides.txt as many times as they occur in the file. Don\'t consider the first 7 characters of each line when comparing them.',
																	'Don\'t consider the first 10 characters while comparing lines and display only repeated lines from the file sides.txt as many times as they repeat.',
																	'How to filter out only repeated lines from the file sides.txt? Print each line as many times as it occurs in the file and ignore first 7 characters when comparing the lines.',
																	'Single command to see only repeated lines in the file sides.txt as many times as they occur in the file while avoiding first 7 characters when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -D -w 7 developer.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file developer.txt as many times as they occur in the file. Consider only the first 7 characters of each line when comparing them.',
																		'Consider first 7 characters while comparing lines and display only repeated lines from the file developer.txt as many times as they repeat.',
																		'How to filter out only repeated lines from the file developer.txt? Print each line as many times as it occurs in the file. Only consider first 7 characters when comparing the lines.',
																		'Single command to see only repeated lines in the file developer.txt as many times as they occur in the file while taking only first 7 characters into account when comparing lines.']},ignore_index=True)

####
uniq = uniq.append({'Command':'uniq -f 3 -i ananya.txt','NL Queries':['Show ananya.txt without consecutive duplicate lines. Ignore first 3 fields and case when comparing lines.',
																		'Ignore first 3 fields as well as case while comparing lines and display only unique lines from the file ananya.txt on the command line.',
																		'How to see unique lines from ananya.txt irrespective of the first 3 fields and the case?',
																		'Single command to see only unique lines from ananya.txt while ignoring first 3 fields as well as case when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -s 8 -i tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines. Don\'t consider the first 8 characters of each line or the case when comparing them.',
																		'Don\'t consider the first 8 characters as well as the case while comparing lines and display only unique lines from the file tutorial.txt on the command line.',
																		'How to see unique lines from tutorial.txt? Ignore first 8 characters and the case when comparing the lines.',
																		'Single command to see only unique lines from tutorial.txt while avoiding first 8 characters as well as the case when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -w 8 -i tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines. Consider only the first 8 characters of each line and ignore case when comparing them.',
																		'Consider first 8 characters and ignore the case while comparing lines and display only unique lines from the file tutorial.txt on the command line.',
																		'How to see unique lines from tutorial.txt? Only consider first 8 characters irrespective of case when comparing the lines.',
																		'Single command to see only unique lines from tutorial.txt while taking first 8 characters into account and ignoring the case when comparing lines.']},ignore_index=True)

####

uniq = uniq.append({'Command':'uniq -u -f 3 summer.txt','NL Queries':['In summer.txt show only those lines that do not have multiple consecutive occurences. Ignore first 3 fields when comparing lines.',
																	'Ignore first 3 fields when comparing lines and filter out the ones that appear only once in summer.txt.',
																	'What all lines have only one instance in summer.txt irrespective of first 3 fields?']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -u -i course.txt','NL Queries':['In course.txt show only those lines that do not have multiple consecutive occurences. Ignore case when comparing lines.',
																	'Ignore case when comparing lines and filter out the ones that appear only once in course.txt.',
																	'What all lines have only one instance in course.txt irrespective of case?']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -u -s 8 tutorial.txt','NL Queries':['From tutorial.txt, show only non-repeating lines. Don\'t consider the first 8 characters of each line when comparing them.',
																		'Don\'t consider the first 8 characters while comparing lines and display only non-repeating lines from the file tutorial.txt on the command line.',
																		'How to see non-repeating lines from tutorial.txt? Ignore first 8 characters when comparing the lines.',
																		'Single command to see only non-repeating lines from tutorial.txt while avoiding first 8 characters when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -u -w 8 tutorial.txt','NL Queries':['From tutorial.txt, show only non-repeating lines. Consider only the first 8 characters of each line when comparing them.',
																		'Consider first 8 characters while comparing lines and display only non-repeating lines from the file tutorial.txt on the command line.',
																		'How to see non-repeating lines from tutorial.txt? Only consider first 8 characters when comparing the lines.',
																		'Single command to see only non-repeating lines from tutorial.txt while taking first 8 characters into account when comparing lines.']},ignore_index=True)

####
uniq = uniq.append({'Command':'uniq -c -d -i myfile.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file myfile.txt along with the number of occurences. Ignore case when comparing lines.',
																		'Display only repeated lines from the file myfile.txt irrespective of case. Prefix each line with it\'s number of occurences.',
																		'How to filter out only repeated lines from the file myfile.txt along with the number of times they repeat? Don\'t consider case when comparing lines.',
																		'Single command to see only repeated lines in the file myfile.txt and the number of repetitions. Compare lines without considering case.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -d -f 5 tutorial.txt','NL Queries':['From tutorial.txt, only show lines that have multiple consecutive occurences. Don\'t consider the first 5 fields of each line when comparing them. Prefix each line with the number of times it consecutively repeats in the file.',
																		'Don\'t consider the first 5 fields while comparing lines and display only consecutively repeating lines from the file tutorial.txt on the command line along with it\'s number of occurences.',
																		'How to see repeating lines from tutorial.txt? Ignore first 5 fields when comparing the lines and print the number of times each line repeats consecutively in the file.',
																		'Single command to see only the lines from tutorial.txt that have multiple consecutive occurences while avoiding first 5 fields when comparing lines. The output should also include the number of times each line repeats consecutively in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -d -s 8 tutorial.txt','NL Queries':['From tutorial.txt, only show lines that have multiple consecutive occurences. Don\'t consider the first 8 characters of each line when comparing them. Prefix each line with the number of times it consecutively repeats in the file.',
																			'Don\'t consider the first 8 characters while comparing lines and display only consecutively repeating lines from the file tutorial.txt on the command line along with it\'s number of occurences.',
																			'How to see repeating lines from tutorial.txt? Ignore first 8 characters when comparing the lines and print the number of times each line repeats consecutively in the file.',
																			'Single command to see only the lines from tutorial.txt that have multiple consecutive occurences while avoiding first 8 characters when comparing lines. The output should also include the number of times each line repeats consecutively in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -d -w 8 tutorial.txt','NL Queries':['Show tutorial.txt with lines that repeat consecutively multiple times. Consider only the first 8 characters of each line when comparing them. The output should also include the number of times each line repeats consecutively in the file.',
																		'Consider first 8 characters while comparing lines and display only repeating lines from the file tutorial.txt on the command line along with it\'s number of occurences in the file.',
																		'How to see lines from tutorial.txt that have multiple consecutive occurences? Only consider first 8 characters when comparing the lines and print the number of times each line repeats consecutively in the file.',
																		'Single command to see only consecutively repeating lines from tutorial.txt while taking first 8 characters into account when comparing lines. Prefix each line with the number of times it consecutively repeats in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -s 8 -i tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines. Don\'t consider the first 8 characters of each line as well as case when comparing them. Prefix each line with the number of times it consecutively repeats in the file.',
																			'Don\'t consider the first 8 characters and the case while comparing lines and display only unique lines from the file tutorial.txt on the command line along with it\'s number of occurences.',
																			'How to see unique lines from tutorial.txt? Ignore first 8 characters as well as the case when comparing the lines and print the number of times each line repeats consecutively in the file.',
																			'Single command to see only unique lines from tutorial.txt while avoiding first 8 characters and the case when comparing lines. The output should also include the number of times each line repeats consecutively in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -w 8 -i tutorial.txt','NL Queries':['Show tutorial.txt without consecutive duplicate lines irrespective of case. Consider only the first 8 characters of each line when comparing them. The output should also include the number of times each line repeats consecutively in the file.',
																			'Consider first 8 characters and ignore case while comparing lines and display only unique lines from the file tutorial.txt on the command line along with it\'s number of occurences in the file.',
																			'How to see unique lines from tutorial.txt? Only consider first 8 characters and ignore case when comparing the lines and print the number of times each line repeats consecutively in the file.',
																			'Single command to see only unique lines from tutorial.txt while taking first 8 characters into account when comparing lines irrespective of case. Prefix each line with the number of times it consecutively repeats in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -f 4 -i start.txt','NL Queries':['Show start.txt without consecutive duplicate lines along with the number of occurences. Ignore first 4 fields and case when comparing lines.',
																		'Ignore first 4 fields as well as the case while comparing lines and display only unique lines from the file start.txt on the command line. Prefix the number of times each line repeats.',
																		'How to see unique lines from start.txt irrespective of first 4 fields and the case along with the number of consecutive repetitions in the file?',
																		'Single command to see only unique lines from start.txt while ignoring first 4 fields and the case when comparing lines. Also display the number of times each line repeats in the file consecutively.']},ignore_index=True)

###
uniq = uniq.append({'Command':'uniq -d -f 2 -i sample.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file sample.txt. Ignore first 2 fields and the case when comparing lines.',
																		'Ignore first 2 fields as well as the case when comparing lines and display only continuous repeated lines from the file sample.txt.',
																		'How to filter out only continuous repeated lines from the file sample.txt while ignoring first 2 fields and the case during comparison?',
																		'Single command to see only continuous repeated lines in the file sample.txt irrespective of first 2 fields and the case.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -d -s 10 -i tutorial.txt','NL Queries':['Show tutorial.txt with lines that have multiple consecutive occurences. Don\'t consider the first 10 characters of each line or the case when comparing them.',
																			'Don\'t consider the first 10 characters as well as the case while comparing lines and display only those lines that repeat consecutively in the file tutorial.txt on the command line.',
																			'How to see only continuous repeated lines from tutorial.txt? Ignore first 10 characters and the case when comparing the lines.',
																			'Single command to see only continuous repeated lines from tutorial.txt while avoiding first 10 characters and the case when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -d -w 10 -i tutorial.txt','NL Queries':['From tutorial.txt, only show lines that have multiple consecutive occurences. Consider only the first 10 characters of each line and ignore the case when comparing them.',
																		'Consider first 10 characters and ignore case while comparing lines and display only continuous repeated lines from the file tutorial.txt on the command line.',
																		'How to see lines with multiple consecutive occurences from tutorial.txt? Only consider first 10 characters irrespective of case when comparing the lines.',
																		'Single command to see only continuous repeated lines from tutorial.txt while taking only first 10 characters into account and ignoring the case when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -D -f 5 -i moons.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file moons.txt as many times as they occur in the file. Ignore first 5 fields and the case when comparing lines.',
																		'Display only repeated lines from the file moons.txt as many times as they repeat irrespective of first 5 fields or the case.',
																		'How to filter out only repeated lines from the file moons.txt without considering first 5 fields and the case when comparing lines? Print each line as many times as it occurs in the file.',
																		'Single command to see only repeated lines in the file moons.txt as many times as they occur in the file irrespective of first 5 fields or the case.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -D -s 7 -i sides.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file sides.txt as many times as they occur in the file. Don\'t consider the first 7 characters of each line or the case when comparing them.',
																	'Don\'t consider the first 10 characters as well as the case while comparing lines and display only repeated lines from the file sides.txt as many times as they repeat.',
																	'How to filter out only repeated lines from the file sides.txt? Print each line as many times as it occurs in the file and ignore first 7 characters or the case when comparing the lines.',
																	'Single command to see only repeated lines in the file sides.txt as many times as they occur in the file while avoiding first 7 characters and the case when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -D -w 7 -i developer.txt','NL Queries':['Print only the lines that have multiple consecutive occurences in the file developer.txt as many times as they occur in the file. Consider only the first 7 characters of each line and ignore the case when comparing them.',
																		'Consider first 7 characters and ignore the case while comparing lines and display only repeated lines from the file developer.txt as many times as they repeat.',
																		'How to filter out only repeated lines from the file developer.txt? Print each line as many times as it occurs in the file. Only consider first 7 characters and ignore the case when comparing the lines.',
																		'Single command to see only repeated lines in the file developer.txt as many times as they occur in the file while taking only first 7 characters into account and ignoring the case when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -u -f 3 -i summer.txt','NL Queries':['In summer.txt show only those lines that do not have multiple consecutive occurences. Ignore first 3 fields and the case when comparing lines.',
																		'Ignore first 3 fields and the case when comparing lines and filter out the ones that appear only once in summer.txt.',
																		'What all lines have only one instance in summer.txt irrespective of first 3 fields or the case?']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -u -s 8 -i tutorial.txt','NL Queries':['From tutorial.txt, show only non-repeating lines. Don\'t consider the first 8 characters of each line or the case when comparing them.',
																		'Don\'t consider the first 8 characters and the case while comparing lines and display only non-repeating lines from the file tutorial.txt on the command line.',
																		'How to see non-repeating lines from tutorial.txt? Ignore first 8 characters as well as the case when comparing the lines.',
																		'Single command to see only non-repeating lines from tutorial.txt while avoiding first 8 characters and the case when comparing lines.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -u -w 8 -i tutorial.txt','NL Queries':['From tutorial.txt, show only non-repeating lines. Consider only the first 8 characters of each line and ignore the case when comparing them.',
																		'Consider first 8 characters while comparing lines, ignore the case and display only non-repeating lines from the file tutorial.txt on the command line.',
																		'How to see non-repeating lines from tutorial.txt? Only consider first 8 characters and ignore the case when comparing the lines.',
																		'Single command to see only non-repeating lines from tutorial.txt while taking first 8 characters into account and ignoring case when comparing lines.']},ignore_index=True)

###
uniq = uniq.append({'Command':'uniq -c -d -f 5 -i tutorial.txt','NL Queries':['From tutorial.txt, only show lines that have multiple consecutive occurences. Don\'t consider the first 5 fields of each line or the case when comparing them. Prefix each line with the number of times it consecutively repeats in the file.',
																			'Don\'t consider the first 5 fields and the case while comparing lines and display only consecutively repeating lines from the file tutorial.txt on the command line along with it\'s number of occurences.',
																			'How to see repeating lines from tutorial.txt? Ignore first 5 fields or the case when comparing the lines and print the number of times each line repeats consecutively in the file.',
																			'Single command to see only the lines from tutorial.txt that have multiple consecutive occurences while avoiding first 5 fields or the case when comparing lines. The output should also include the number of times each line repeats consecutively in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -d -s 8 -i tutorial.txt','NL Queries':['From tutorial.txt, only show lines that have multiple consecutive occurences. Don\'t consider the first 8 characters of each line or the case when comparing them. Prefix each line with the number of times it consecutively repeats in the file.',
																			'Don\'t consider the first 8 characters and the case while comparing lines and display only consecutively repeating lines from the file tutorial.txt on the command line along with it\'s number of occurences.',
																			'How to see  continuous repeating lines from tutorial.txt? Ignore first 8 characters and the case when comparing the lines and print the number of times each line repeats consecutively in the file.',
																			'Single command to see only the lines from tutorial.txt that have multiple consecutive occurences while avoiding first 8 characters and the case when comparing lines. The output should also include the number of times each line repeats consecutively in the file.']},ignore_index=True)

uniq = uniq.append({'Command':'uniq -c -d -w 8 -i tutorial.txt','NL Queries':['Show tutorial.txt with lines that repeat consecutively multiple times. Consider only the first 8 characters of each line and ignore the case when comparing them. The output should also include the number of times each line repeats consecutively in the file.',
																			'Consider first 8 characters and ignore the case while comparing lines and display only continuous repeating lines from the file tutorial.txt on the command line along with it\'s number of occurences in the file.',
																			'How to see lines from tutorial.txt that have multiple consecutive occurences? Only consider first 8 characters and ignore the case when comparing the lines and print the number of times each line repeats consecutively in the file.',
																			'Single command to see only consecutively repeating lines from tutorial.txt while taking first 8 characters into account and ignoring the case when comparing lines. Prefix each line with the number of times it consecutively repeats in the file.']},ignore_index=True)

print uniq
