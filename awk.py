import pandas as pd 

awk = pd.DataFrame(columns = ['Command','NL Queries'])



awk = awk.append({'Command':'awk \'{print}\' marks.txt',
				'NL Queries':['Print contents of marks.txt.',
							'Display contents of marks.txt.',
							'Show the contents of marks.txt.',
							'How do I print marks.txt?']},ignore_index=True)

awk = awk.append({'Command':'awk \'/a/ {print $4 "\t" $3}\' marks.txt',
				'NL Queries':['Print tab-separated columns 4 and 3 of marks.txt containing string "a".',
							'How do I see the columns 4 and 3 of table in marks.txt? I need to see only those which have "a" in their value.',
							'Display column 4 then followed by tab space then by column 3 of marks.txt. Display only those which contain "a" in records.']},ignore_index=True)

awk = awk.append({'Command':'awk -F, \'{print $2}\' table.csv',
				'NL Queries':['Print second column of comma separated table in table.csv.',
							'How do I print second column from table.csv which has , as their separator?',
							'Show the second column from table.csv. Take , as separator.']},ignore_index=True)

awk = awk.append({'Command':'awk -F: \'{print $2}\' table.csv',
				'NL Queries':['Print second and third column of colon separated table in table.csv.',
							'How do I print second and third column from table.csv which has : as their separator?',
							'Show the second and third column from table.csv. Take : as separator.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{print $2,$3}\' table.csv',
				'NL Queries':['Print second and third column of table in table.csv.',
							'How do I print second and third column from table.csv?',
							'Display the second and third column content from table.csv.']},ignore_index=True)

awk = awk.append({'Command':'awk \'/hello/\' marks.txt',
				'NL Queries':['Print lines of marks.txt containing \'hello\' word.',
							'How do I print records containing word \'hello\' from marks.txt?',
							'How to display lines from marks.txt containing \'hello\'?',
							'Show records from marks.txt containing \'hello\' word.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{print NR, $0}\' table.csv',
				'NL Queries':['Print contents of table.csv with line number for each record.',
							'How do I print table.csv along with number of records?',
							'Display table.csv records with numbering for each line.']},ignore_index=True)

awk = awk.append({'Command':'awk \'NR==3 {print NR, $0}\' table.csv',
				'NL Queries':['Print contents of record from table.csv having line number 3.',
							'How do I print values of record from table.csv having line number as 3?',
							'Display table.csv record content having line number 3.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{print NF, $0}\' table.csv',
				'NL Queries':['Print contents of table.csv with number of fields in each record.',
							'How do I print table.csv along with number of fields in each records?',
							'Display table.csv with number of fields in each record.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{print NR, $3}\' table.csv',
				'NL Queries':['Print column 3 contents of table.csv with line number for each record.',
							'How do I print column 3 from table.csv along with number of records?',
							'Display third column of all records of table.csv with numbering for each line.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{print NF, $3}\' table.csv',
				'NL Queries':['Print column 3 contents of table.csv with number of fields in each record.',
							'How do I print column 3 from table.csv along with number of fields in each record?',
							'Display third column records of table.csv with number of fields in each record.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{print NR, $1, $3}\' table.csv',
				'NL Queries':['Print column 1 and 3 contents of table.csv with line number for each record.',
							'How do I print column 1 and 3 from table.csv along with number of records?',
							'Display first and third column records of table.csv with numbering for each line.']},ignore_index=True)

awk = awk.append({'Command':'awk \'$1 ~/hello/\' marks.txt',
				'NL Queries':['Print lines of marks.txt containing \'hello\' word in column 1.',
							'How do I print records containing word \'hello\' in column 1 from marks.txt?',
							'How to display lines from marks.txt containing \'hello\' in column 1?',
							'Show records from marks.txt containing \'hello\' word in column 1.']},ignore_index=True)

awk = awk.append({'Command':'awk \'$0 !~/hello/\' marks.txt',
				'NL Queries':['Print lines of marks.txt which do not contain \'hello\' word.',
							'How do I print records which do not contain word \'hello\' from marks.txt?',
							'How to display lines from marks.txt which do not contain \'hello\' word?',
							'Show records from marks.txt which do not contain \'hello\' word.']},ignore_index=True)

awk = awk.append({'Command':'awk \'$4 !~/E/{print $1, $2}\' marks.txt',
				'NL Queries':['Print columns 1 and 2 from marks.txt which do not contain \'E\' letter in column 4.',
							'How do I print column 1 and 2 which do not contain letter \'E\' in column 4 from marks.txt?',
							'How to display columns 1 and 2 from marks.txt which do not contain \'E\' letter in column 4?',
							'Show columns 1 and 2 from marks.txt which do not contain \'E\' letter in column 4.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{ print $2> \"file1\" }\' marks.txt',
				'NL Queries':['Copy column 2 from marks.txt into file1.',
							'How do copy column 2 of marks.txt into a file named file1?',
							'I want to copy column 2 of marks.txt into file1.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{ print $2>> \"file1\" }\' marks.txt',
				'NL Queries':['Append column 2 from marks.txt into file1.',
							'How do append column 2 of marks.txt into a file named file1?',
							'I want to append column 2 of marks.txt into file1.',
							'Concatenate column 2 of marks.txt with file1.',
							'Join column 2 of marks.txt after file1 content and save it in file1.']},ignore_index=True)

awk = awk.append({'Command':'awk \'$1 == \"hello\", $1 == \"world\"\' marks.txt',
				'NL Queries':['Print the content between \'hello\' and \'world\' from every record of marks.txt.',
							'How do I print the content between \'hello\' and \'world\' from every record of marks.txt.',
							'Display the content of marks.txt which is between \'hello\' and \'world\' from every record.',
							'Show the content of marks.txt between \'hello\' and \'world\' from every record.']},ignore_index=True)

#original file doesnot change
awk = awk.append({'Command':'awk \'$1 == \"hello\" {$2 = \"world\";print $0}\' table.csv',
				'NL Queries':['Display table.csv with replacing column 2 value with \'world\' for records having column 1 value as \'hello\'.',
							'Print table.csv with replacing column 2 value with \'world\' for records having column 1 value as \'hello\'.',
							'How do I see table.csv after replacing column 2 value with \'world\' for records having column 1 value as \'hello\'?']},ignore_index=True)

awk = awk.append({'Command':'awk \'{OFS=\",\";print $1, $2}\' table.csv',
				'NL Queries':['Print column 1 and 2 contents of table.csv with \',\' as a field separator.',
							'How do I print column 1 and 2 from table.csv having comma as OFS?',
							'Display first and second column records of table.csv with comma as field separator.']},ignore_index=True)

#alternative better way
awk = awk.append({'Command':'awk \'{print $1 \",\" $2 \":\" $3}\' table.csv',
				'NL Queries':['Print column 1 and 2 with \',\' as a field separator and $2 and $3 with \':\' as a field separator from table.csv .',
							'How do I print column 1 and 2 having comma as OFS and column 2 and 3 having colon as OFS from table.csv?',
							'Display first and second column with comma as field separator and second and third column with colon as field separator from table.csv.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{ORS=\",\";print $1, $2}\' table.csv',
				'NL Queries':['Print column 1 and 2 contents of table.csv with \',\' as a record separator.',
							'How do I print column 1 and 2 from table.csv having comma as ORS?',
							'Display first and second column records of table.csv with comma as record separator.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{print $1 | \"sort\"}\' table.csv',
				'NL Queries':['Print column 1 contents of table.csv and sort them.',
							'How do I print sorted column 1 content from table.csv?',
							'Display sorted first column content from table.csv.']},ignore_index=True)

awk = awk.append({'Command':'awk \'{print NF>2, $0}\' table.csv',
				'NL Queries':['Print records from table.csv having number of fields greater than 2.',
							'How do I print records from table.csv having number of fields greater than 2?',
							'Display records having number of fields greater than 2 from table.csv.']},ignore_index=True)

awk = awk.append({'Command':'awk \'/hello/\' {print $1} \' marks.txt',
				'NL Queries':['Print column 1 of marks.txt containing \'hello\' word in that record.',
							'How do I print column 1 containing word \'hello\' in that record from marks.txt?',
							'How to display column 1 from marks.txt containing \'hello\' in that record?']},ignore_index=True)

awk = awk.append({'Command':'awk -f script.awk table.csv',
				'NL Queries':['Run script.awk on table.csv.',
							'How do run external awk script script.awk on table.csv?',
							'Run external awk script script.awk on table.csv.']},ignore_index=True)

print (awk.shape)
