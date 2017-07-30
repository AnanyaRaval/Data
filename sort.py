import pandas as pd 

sort = pd.DataFrame(columns = ['Command','NL Queries'])

sort = sort.append({'Command':'sort data.txt','NL Queries':['Sort the file data.txt in this directory.',
                                'What is the command to sort file data.txt in alphabetical order?',
                                'How do I sort contents of file data.txt present in this directory, in ascending order?']},ignore_index = True)

sort = sort.append({'Command':'sort -f data.txt','NL Queries':['Sort the file data.txt in alphabetical order. Ignore the case of the words.',
                                    'How do I sort the contents of file data.txt in this folder with being case sensitive?']},ignore_index=True)

sort = sort.append({'Command':'sort -k2 test.txt','NL Queries':['Sort contents of text.txt using values in second column.',
                                'How do I sort test.txt using contents of second column?']},ignore_index=True)

#1
sort = sort.append({'Command':     'sort -r another.txt',
                    'NL Queries':  ['Sort the file another.txt in reverse order.',
                                    'Reverse sort the file another.txt .',
                                    'Arrange the lines in file another.txt in reverse order.',
                                    'How do I sort the lines of file another.txt in reverse order?']}, ignore_index = True)

#2
sort = sort.append({'Command':     'sort -r another.txt -o sanother.txt',
                    'NL Queries':  ['Reverse sort the lines of file another.txt and save it in sanother.txt file.',
                                    'Arrange the lines of file another.txt in reverse order and save the output to sanother.txt file.',
                                    'Order the lines of file another.txt in reverse and save it to sanother.txt file.',
                                    'How to arrange the lines in file another.txt in reverse order and save it to sanother.txt file?']}, ignore_index = True)

#3
sort = sort.append({'Command':     'sort -n another.txt',
                    'NL Queries':  ['Numerically sort another.txt file.',
                                    'Order the lines of the file another.txt on numerical basis.',
                                    'How do I sort the contents of another.txt numerically?',
                                    'Show the contents of file another.txt after sorting them numerically.']}, ignore_index = True)

#4
sort = sort.append({'Command':     'sort -n another.txt -o sorted.txt',
                    'NL Queries':  ['Numerically sort another.txt file and save it as sorted.txt file.',
                                    'How do I sort the contents of another.txt , numerically, and store it in another file sorted.txt ?',
                                    'Save the contents of file another.txt, after sorting them numerically, in sorted.txt .',
                                    'Sort the contents of file another.txt numerically and save it in sorted.txt file.']}, ignore_index = True)

#5
sort = sort.append({'Command':     'sort -rn one.txt',
                    'NL Queries':  ['Reverse numerically sort one.txt file.',
                                    'Sort the file one.txt numerically in reverse order.',
                                    'How to sort the contents of file one.txt numerically in reverse order?',
                                    'Show the contents of file one.txt after reverse sorting it numerically.']}, ignore_index = True)

#6
sort = sort.append({'Command':     'sort -rn one.txt -o sortedone.txt',
                    'NL Queries':  ['Reverse numerically sort one.txt file and save it as sortedone.txt file.',
                                    'Save the contents of fileone.txt in sortedone.txt after reverse sorting it numerically.',
                                    'How to sort the data in the file one.txt in the reverse order of numbers and save it in sortedone.txt file?',
                                    'Reverse sort the data in the file one.txt treating them as numbers and save the output as sortedone.txt .']}, ignore_index = True)

#7
sort = sort.append({'Command':     'sort -rf one.txt -o sortedone.txt',
                    'NL Queries':  ['Reverse sort one.txt file and save it as sortedone.txt file. Do case-insensitive comparison.',
                                    'Sort the data in the file one.txt in reverse order and save it as sortedone.txt file. Perform case-insensitive conparison.',
                                    'How to sort the lines in one.txt file in reverse alphanumeric order while doing case insensitive comparison and save it as sortedone.txt file?',
                                    'I want to reverse sort the data in file one.txt in alphanumeric order irrespective of case difference.']}, ignore_index = True)

#8
sort = sort.append({'Command':     'sort -rf one.txt',
                    'NL Queries':  ['Reverse sort one.txt file. Treat uppercase and lowercase alphabets as same.',
                                    'Not considering case of alphabets, reverse sort the content of file one.txt and show the output.',
                                    'How do I sort the contents of file one.txt ignoring case differences in reverse order?',
                                    'Display the result of reverse sorting one.txt if uppercase and lowercase alphabets are treated the same.']}, ignore_index = True)

#9
sort = sort.append({'Command':     'sort -u dupl.txt',
                    'NL Queries':  ['Sort the lines in dupl.txt file and remove the duplicate lines.',
                                    'Sort the contents of file dupl.txt . Display only unique lines.',
                                    'How do I get the content of file dupl.txt sorted and only unique lines to be shown?',
                                    'Show only the unique lines in the file dupl.txt and in sorted order.']}, ignore_index = True)

#10
sort = sort.append({'Command':     'sort -ur dupl.txt',
                    'NL Queries':  ['Reverse sort the lines in dupl.txt file and remove the duplicate lines.',
                                    'Reverse sort the contents of file dupl.txt . Display only unique lines.',
                                    'How do I get the content of file dupl.txt reverse sorted and only unique lines to be shown?',
                                    'Show only the unique lines in the file dupl.txt and in reverse sorted order.']}, ignore_index = True)

#11
sort = sort.append({'Command':     'sort -u dupl.txt -o out.txt',
                    'NL Queries':  ['Sort the lines in dupl.txt file and remove the duplicate lines and save the output as out.txt file.',
                                    'Save the contents of file dupl.txt in out.txt after sorting and removing duplicate lines.',
                                    'How to sort the contents of file dupl.txt and save it in out.txt after removing duplicate lines?',
                                    'Sort the contents of file dupl.txt . Remove repeated lines. Save the final output as out.txt file.']}, ignore_index = True)

#12
sort = sort.append({'Command':     'sort -ur dupl.txt -o chk.txt',
                    'NL Queries':  ['Reverse sort the lines in dupl.txt file and remove the duplicate lines and save the output as chk.txt file.',
                                    'Sort the contents of file dupl.txt in reverse order and remove the repeating lines. Save the output in file chk.txt .',
                                    'Save the contents of file dupl.txt in out.txt after reverse sorting and removing duplicate lines.',
                                    'How to reverse sort the contents of file dupl.txt and save it in out.txt after removing duplicate lines?']}, ignore_index = True)

#13
sort = sort.append({'Command':     'sort -u linux.txt unix.txt -o os.txt',
                    'NL Queries':  ['Sort the lines in files linux.txt and unix.txt, merge them and save the output in os.txt file. Remove duplicates.',
                                    'Save the output of sorting and merging linux.txt and unix.txt files in os.txt file. Save only the unique lines.',
                                    'Merge the contents of files linux.txt and unix.txt files after sorting them. Remove the repeating lines and save it as os.txt file.',
                                    'Create a file os.txt consisting of only unique lines from linux.txt and unix.txt files in sorted order.']}, ignore_index = True)

#14
sort = sort.append({'Command':     'sort -nu dupl.txt -o out.txt',
                    'NL Queries':  ['Numerically sort the lines in dupl.txt file and remove the duplicate lines and save the output as out.txt file.',
                                    'Create the file out.txt which contains the contents of file dupl.txt file sorted numerically and has unique lines.',
                                    'Save the output of sorting the file dupl.txt numerically in out.txt file. Save only the unique lines.',
                                    'How to numerically sort the contents of file dupl.txt and save only the unique lines in file out.txt ?']}, ignore_index = True)

#15
sort = sort.append({'Command':     'sort -unr dupl.txt -o chk.txt',
                    'NL Queries':  ['Reverse numerically sort the lines in dupl.txt file and remove the duplicate lines and save the output as chk.txt file.',
                                    'Create the file chk.txt which contains the contents of file dupl.txt file sorted numerically in reverse order and has unique lines.',
                                    'Save the output of sorting the file dupl.txt in numerically reverse order in chk.txt file. Save only the unique lines.',
                                    'How to numerically reverse sort the contents of file dupl.txt and save only the unique lines in file chk.txt ?']}, ignore_index = True)

#16
sort = sort.append({'Command':     'sort -nu dupl.txt',
                    'NL Queries':  ['Numerically sort the lines in dupl.txt file and remove the duplicate lines.',
                                    'Show me the output of sorting dupl.txt file numerically and do not display the repeating lines.',
                                    'Sort the contents of file dupl.txt numerically and remove repeating lines.',
                                    'Display the data in file dupl.txt in numerically sorted format. Do not display identical lines more than once.']}, ignore_index = True)

#17
sort = sort.append({'Command':     'sort -unr dupl.txt',
                    'NL Queries':  ['Reverse numerically sort the lines in dupl.txt file and remove the duplicate lines.',
                                    'Display the data in file dupl.txt in numerically reverse sorted format. Do not display identical lines more than once.',
                                    'Show me the output of reverse sorting dupl.txt file numerically and do not display the repeating lines.',
                                    'How to numerically reverse sort the contents of file dupl.txt and show only the unique lines?']}, ignore_index = True)

#18
sort = sort.append({'Command':     'sort linux.txt unix.txt',
                    'NL Queries':  ['Sort the lines in files linux.txt and unix.txt, merge them and display the output.',
                                    'Show the contents of files linux.txt and unix.txt after sorting and merging them.',
                                    'Display the data in linux.txt and unix.txt files after sorting and merging them.',
                                    'How do I get the contents of both the files, linux.txt and unix.txt , sorted together?']}, ignore_index = True)

#19
sort = sort.append({'Command':     'sort -r linux.txt unix.txt',
                    'NL Queries':  ['Reverse sort the lines in files linux.txt and unix.txt, merge them and display the output.',
                                    'Show the contents of files linux.txt and unix.txt after reverse sorting and merging them.',
                                    'Display the data in linux.txt and unix.txt files after sorting in reverse order and merging them.',
                                    'How do I get the contents of both the files, linux.txt and unix.txt , sorted together in reverse order?']}, ignore_index = True)

#20
sort = sort.append({'Command':     'sort -r linux.txt unix.txt -o os.txt',
                    'NL Queries':  ['Reverse sort the lines in files linux.txt and unix.txt, merge them and save the output in os.txt file.',
                                    'Merge the contents of files linux.txt and unix.txt files after sorting them in reverse order and save it as os.txt file.',
                                    'How to sort the content of both the files, linux.txt and unix.txt, together in reverse order and save it as os.txt file?',
                                    'Show me the output of reverse sorting linux.txt and unix.txt files, together, and save it as os.txt .']}, ignore_index = True)

#21
sort = sort.append({'Command':     'sort linux.txt unix.txt -o os.txt',
                    'NL Queries':  ['Sort the lines in files linux.txt and unix.txt, merge them and save the output in os.txt file.',
                                    'Save the contents of files linux.txt and unix.txt after sorting and merging them in os.txt .',
                                    'How to sort the content of both the files, linux.txt and unix.txt, together and save it as os.txt file?',
                                    'Merge the contents of files linux.txt and unix.txt files after sorting them and save it as os.txt file.']}, ignore_index = True)

#22
sort = sort.append({'Command':     'sort -u linux.txt unix.txt',
                    'NL Queries':  ['Sort the lines in files linux.txt and unix.txt, merge them and display the output. Remove duplicates.',
                                    'Merge the unique liness from linux.txt and unix.txt after sorting them.',
                                    'How to sort the contents of linux.txt and unix.txt files as one and retain only unique lines?',
                                    'Display the lines from file linux.txt and unix.txt files in sorted order. Show only unique lines.']}, ignore_index = True)

#23
sort = sort.append({'Command':     'sort -ru linux.txt unix.txt',
                    'NL Queries':  ['Reverse sort the lines in files linux.txt and unix.txt, merge them and display the output. Remove duplicates.',
                                    'Merge the unique liness from linux.txt and unix.txt after sorting them in reverse order.',
                                    'How to sort the contents of linux.txt and unix.txt files in reverse order as one file and retain only unique lines?',
                                    'Display the lines from file linux.txt and unix.txt files in reverse sorted order. Show only unique lines.']}, ignore_index = True)

#24
sort = sort.append({'Command':     'sort -ru linux.txt unix.txt -o os.txt',
                    'NL Queries':  ['Reverse sort the lines in files linux.txt and unix.txt, merge them and save the output in os.txt file. Remove duplicates.',
                                    'Merge the unique liness from linux.txt and unix.txt after sorting them in reverse order. Save the result as os.txt .',
                                    'How to sort the contents of linux.txt and unix.txt files in reverse order as one file and save result as os.txt retaining only unique lines?',
                                    'Save the lines from file linux.txt and unix.txt files in reverse sorted order and only unique lines in the file os.txt .']}, ignore_index = True)

#25
sort = sort.append({'Command':     'sort -hf num.txt',
                    'NL Queries':  ['Sort the file num.txt and interpret human readable numbers ignoring case.',
                                    'Sort the file num.txt interpreting the lines as human readable numbers and ignoring case differences.',
                                    'Interpret the contents of file num.txt as human friendly numbers and sort them without taking case of alphabets into account.',
                                    'How to sort the file num.txt which contains human readable numbers and not so strict case following?']}, ignore_index = True)

#26
sort = sort.append({'Command':     'sort -hf num.txt -o sortnum.txt',
                    'NL Queries':  ['Sort the file num.txt and interpret human readable numbers ignoring case. Save the output in sortnum.txt file.',
                                    'How to sort the file num.txt which contains human readable numbers with not so strict case following and save it as sortnum.txt file?',
                                    'Interpret the contents of file num.txt as human friendly numbers and sort them without taking case of alphabets into account. Save the result as sortnum.txt file.']}, ignore_index = True)

#27
sort = sort.append({'Command':     'sort -i spaces.txt',
                    'NL Queries':  ['Sort spaces.txt file and consider only printable characters.',
                                    'While sorting spaces.txt contents do not take non graphic characters into account.',
                                    'Do not consider non printable characters and sort the data in file spaces.txt .']}, ignore_index = True)

#28
sort = sort.append({'Command':     'sort -i spaces.txt -o sorted.txt',
                    'NL Queries':  ['Sort spaces.txt file and consider only printable characters and save it as sorted.txt file.',
                                    'Do not consider non printable characters and sort the data in file spaces.txt saving the output as sorted.txt file.',
                                    'Save the output generated by sorting spaces.txt file in sorted.txt file. While sorting do not consider non printable characters.']}, ignore_index = True)

#29
sort = sort.append({'Command':     'sort -m snippet1.txt snippet2.txt',
                    'NL Queries':  ['Merge , already sorted, snippet1.txt and snippet2.txt and show the result.',
                                    'How to merge the files snippet1.txt and snippet2.txt which are already sorted?',
                                    'Show the output generated by merging snippet1.txt and snippet2.txt if they are considered sorted.']}, ignore_index = True)

#30
sort = sort.append({'Command':     'sort -m snippet1.txt snippet2.txt -o merged.txt',
                    'NL Queries':  ['Merge , already sorted, snippet1.txt and snippet2.txt and save the result as merged.txt .',
                                    'How to merge the files snippet1.txt and snippet2.txt which are already sorted and save the result as merged.txt file?',
                                    'Create the file merged.txt which contains merged content from files snippet1.txt and snippet2.txt which were sorted beforehand.']}, ignore_index = True)

#31
sort = sort.append({'Command':     'sort -z blag.doc',
                    'NL Queries':  ['Sort lines in blag.doc and treat NULL as line delimiter.',
                                    'Treating NULL as line delimiter sort the file blag.doc .',
                                    'Show the output of sorting contents of file blag.doc , if NULL is the line delimiter.']}, ignore_index = True)

#32
sort = sort.append({'Command':     'sort -z blag.doc -o output',
                    'NL Queries':  ['Sort lines in blag.doc and treat NUL as line delimiter. Save it in file named output .',
                                    'Treating NULL as delimiter sort the file blag.doc and save the output as output file.',
                                    'Save the output of sorting blag.doc file, if NULL is treated as line delimiter, in file output .']}, ignore_index = True)

#33
sort = sort.append({'Command':     'sort -M months.txt',
                    'NL Queries':  ['Sort, in the order of months, the file months.txt .',
                                    'Sort the contents of file months.txt treating them as months of the calendar year.',
                                    'Show the output of sorting months.txt file as if it were months of the year.']}, ignore_index = True)

#34
sort = sort.append({'Command':     'sort -M months.txt -o jhakaas.txt',
                    'NL Queries':  ['Sort, in the order of months, the file months.txt . Save the output in file jhakaas.txt .',
                                    'Sort the contents of file months.txt treating them as months of the calendar year and save it as jhakaas.txt .',
                                    'Save the output of sorting months.txt file as if it were months of the year in jhakaas.txt file.']}, ignore_index = True)

#35
sort = sort.append({'Command':     'sort -c testsort.txt',
                    'NL Queries':  ['Check if the file testsort.txt is sorted or not.',
                                    'Report if the file testsort.txt is sorted or not.',
                                    'Is the file sorted.txt sorted?']}, ignore_index = True)

#36
sort = sort.append({'Command':     'sort -k2 sec.txt',
                    'NL Queries':  ['Sort lines in sec.txt according to second word in each line.',
                                    'Sort the contents of file sec.txt using second word as key.',
                                    'Use the second word as key to sort the lines of sec.txt file. For a tie break use entire line.']}, ignore_index = True)

#37
sort = sort.append({'Command':     'sort -k2 sec.txt -o sorted.pxp',
                    'NL Queries':  ['Sort lines in sec.txt according to second word in each line and save the output as sorted.pxp file.',
                                    'Sort the contents of file sec.txt using second word as key and save it as sorted.pxp file.',
                                    'Use the second word as key to sort the lines of sec.txt file. For a tie break use entire line. Save the output as sorted.pxp .']}, ignore_index = True)

#38
sort = sort.append({'Command':     'sort -t\'|\' sign.pdf',
                    'NL Queries':  ['Sort the file sign.pdf and use | as word delimiter.',
                                    'Using | as word delimiter sort the data in sign.pdf file.',
                                    'Sort the contents of file sign.pdf . Use | as delimiter.']}, ignore_index = True)

#39
sort = sort.append({'Command':     'sort -t\'|\' sign.pdf -o sort.pl',
                    'NL Queries':  ['Sort the file sign.pdf and use | as delimiter. Save the output as sort.pl file.',
                                    'Set | as symbol to separate words. Sort the sign.pdf file contents and save it as sort.pl file.',
                                    'Using | as key delimiter sort the data in sign.pdf file. Save the output as sort.pl .']}, ignore_index = True)

#40
sort = sort.append({'Command':     'sort -d dict.py',
                    'NL Queries':  ['Sort dict.py in dictionary order.',
                                    'Arrange the contents of file dict.py in dictionary order.',
                                    'Order the contents of file dict.py as in a dictionary.']}, ignore_index = True)

#41
sort = sort.append({'Command':     'sort -d dict.py -o scrambled.txt',
                    'NL Queries':  ['Sort dict.py in dictionary order and save the output in scrambled.txt file.',
                                    'Arrange the contents of file dict.py in dictionary order and save it as scrambled.txt .',
                                    'Order the contents of file dict.py as in a dictionary and store it in scrambled.txt .']}, ignore_index = True)

#42
sort = sort.append({'Command':     'sort -V ver.doc',
                    'NL Queries':  ['Sort file verdoc.txt containing version numbers in natural order.',
                                    'Reorder the file containing version numbers, ver.doc .',
                                    'Arrange the contents of ver.doc file as if they were version numbers.']}, ignore_index = True)

#43
sort = sort.append({'Command':     'sort -V ver.doc -o sortver.doc',
                    'NL Queries':  ['Sort file verdoc.txt containing version numbers in natural order. Save the output in sortver.doc file.',
                                    'Reorder the file containing version numbers, ver.doc and store it as sortver.doc file.',
                                    'Arrange the contents of ver.doc file as if they were version numbers and save it as sortver.doc .']}, ignore_index = True)

#44
sort = sort.append({'Command':     'sort -',
                    'NL Queries':  ['Sort the lines read from stdin.',
                                    'Read the lines from STDIN and sort them when end of input signal is received.',
                                    'Take input from stdin and sort the lines.',
                                    'Sort the content received from stdin .']}, ignore_index = True)

#45
sort = sort.append({'Command':     'sort - -o serial.txt',
                    'NL Queries':  ['Sort the lines read from stdin and save it in file serial.txt .',
                                    'Read the lines from STDIN and sort them when end of input signal is received. Save the output as serial.txt .',
                                    'Take input from stdin and sort the lines. Store the output in serial.txt file.',
                                    'Sort the content received from stdin and save the result as serial.txt file.']}, ignore_index = True)

#46
sort = sort.append({'Command':     'sort -hrf num.txt',
                    'NL Queries':  ['Reverse sort the file num.txt and interpret human readable numbers ignoring case.',
                                    'Sort the contents of file num.txt treating them as human readable numbers and ignoring case in reverse order.',
                                    'How to sort the file num.txt interpreting the lines as human friendly numbers in reverse order without case checking?']}, ignore_index = True)

#47
sort = sort.append({'Command':     'sort -hrf num.txt -o sortnum.txt',
                    'NL Queries':  ['Reverse sort the file num.txt and interpret human readable numbers ignoring case. Save the output in sortnum.txt file.',
                                    'Sort the contents of file num.txt treating them as human readable numbers and ignoring case in reverse order. Save the output as sortnum.txt file.',
                                    'How to sort the file num.txt interpreting the lines as human friendly numbers in reverse order without case checking and save it as sortnum.txt ?']}, ignore_index = True)

#48
sort = sort.append({'Command':     'sort -ri spaces.txt',
                    'NL Queries':  ['Reverse sort spaces.txt file and consider only printable characters.',
                                    'Ignoring non printable characters sort the file spaces.txt in reverse order.',
                                    'Sort the contents of file spaces.txt in reverse order ignoring non printable characters.']}, ignore_index = True)

#49
sort = sort.append({'Command':     'sort -ri spaces.txt -o sorted.txt',
                    'NL Queries':  ['Reverse sort spaces.txt file and consider only printable characters and save it as sorted.txt file.',
                                    'Ignoring non printable characters sort the file spaces.txt in reverse order and save it as sorted.txt .',
                                    'Sort the contents of file spaces.txt in reverse order ignoring non printable characters. Store the file as sorted.txt .']}, ignore_index = True)

#50
sort = sort.append({'Command':     'sort -rm snippet1.txt snippet2.txt',
                    'NL Queries':  ['Merge , already sorted in reverse order, snippet1.txt and snippet2.txt and show the result.',
                                    'Combine the files snippet1.txt and snippet2.txt which are sorted in reverse order.',
                                    'Merge snippet1.txt and snippet.txt files which are sorted in reverse order.']}, ignore_index = True)

#51
sort = sort.append({'Command':     'sort -rm snippet1.txt snippet2.txt -o merged.txt',
                    'NL Queries':  ['Merge , already sorted in reverse order, snippet1.txt and snippet2.txt and save the result as merged.txt .',
                                    'Combine the files snippet1.txt and snippet2.txt which are sorted in reverse order. Save the output as merged.txt file.',
                                    'Merge snippet1.txt and snippet.txt files which are sorted in reverse order. Store the file as merged.txt file.']}, ignore_index = True)

#52
sort = sort.append({'Command':     'sort -rz blag.doc',
                    'NL Queries':  ['Reverse sort lines in blag.doc and treat NULL as line delimiter.',
                                    'Sort the file blag.doc in reverse order treating NULL as line delimiter.',
                                    'Arrange the content of file blag.doc in reverse order and NULL is the line terminator.']}, ignore_index = True)

#53
sort = sort.append({'Command':     'sort -rz blag.doc -o output',
                    'NL Queries':  ['Reverse sort lines in blag.doc and treat NULL as line delimiter. Save it in file named output .',
                                    'Sort the file blag.doc in reverse order treating NULL as line delimiter. Save the result as output file.',
                                    'Arrange the content of file blag.doc in reverse order and NUL is the line terminator. Store the result in file output .']}, ignore_index = True)

#54
sort = sort.append({'Command':     'sort -rM months.txt',
                    'NL Queries':  ['Reverse sort, in the order of months, the file months.txt .',
                                    'Sort the contents of file months.txt in reverse order of months in a year.',
                                    'Arrange the lines in months.txt in the reverse order of the months.']}, ignore_index = True)

#55
sort = sort.append({'Command':     'sort -rM months.txt -o jhakaas.txt',
                    'NL Queries':  ['Revere sort, in the order of months, the file months.txt . Save the output in file jhakaas.txt .',
                                    'Sort the contents of file months.txt in reverse order of months in a year and save the ouput as jhakaas.txt .',
                                    'Arrange the lines in months.txt in the reverse order of the months. Store the output as jhakaas.txt file.']}, ignore_index = True)

#56
sort = sort.append({'Command':     'sort -rc testsort.txt',
                    'NL Queries':  ['Check if the file testsort.txt is reverse sorted or not.',
                                    'Tell if the file testsort.txt is sorted in reverse order or not.',
                                    'How to check if file testsort.txt is reverse sorted?',
                                    'Is the file testsorted.txt reverse sorted?']}, ignore_index = True)

#57
sort = sort.append({'Command':     'sort -rk2 sec.txt',
                    'NL Queries':  ['Reverse sort lines in sec.txt according to second word in each line.',
                                    'Sort the file sec.txt using second word as key in reverse order.',
                                    'Arrange the file sec.txt in reverse order using second word of each line as key.',
                                    'Order the file sec.txt in reverse according to second word in each line.']}, ignore_index = True)

#58
sort = sort.append({'Command':     'sort -rk2 sec.txt -o sorted.pxp',
                    'NL Queries':  ['Reverse sort lines in sec.txt according to second word in each line and save the output as sorted.pxp file.',
                                    'Sort the file sec.txt using second word as key in reverse order and save the output as sorted.pxp .',
                                    'Arrange the file sec.txt in reverse order using second word of each line as key and store it as sorted.pxp file.',
                                    'Order the file sec.txt in reverse according to second word in each line and save the result as sorted.pxp .']}, ignore_index = True)

#59
sort = sort.append({'Command':     'sort -rt\'|\' sign.pdf',
                    'NL Queries':  ['Reverse sort the file sign.pdf and use | as delimiter.',
                                    'Sort the file sign.pdf in reverse order and use | as word separator.',
                                    'Arrange the contents of file sign.pdf in reverse order using | as key separator.']}, ignore_index = True)

#60
sort = sort.append({'Command':     'sort -rt\'|\' sign.pdf -o sort.pl',
                    'NL Queries':  ['Reverse sort the file sign.pdf and use | as delimiter. Save the output as sort.pl file.',
                                    'Sort the file sign.pdf in reverse order and use | as word separator, saving the output as sort.pl .',
                                    'Arrange the contents of file sign.pdf in reverse order using | as key separator and save it as sort.pl .']}, ignore_index = True)

#61
sort = sort.append({'Command':     'sort -rd dict.py',
                    'NL Queries':  ['Sort dict.py in reverse dictionary order.',
                                    'Sort the contents of file dict.py in reverse order as they are arranged in a dictionary.',
                                    'Arrange the lines in file dict.py in the opposite dictionary order.',
                                    'Order the contents of file dict.py in the reverse order of dictionary sorting.']}, ignore_index = True)

#62
sort = sort.append({'Command':     'sort -rd dict.py -o scrambled.txt',
                    'NL Queries':  ['Sort dict.py in reverse dictionary order and save the output in scrambled.txt file.',
                                    'Sort the contents of file dict.py in reverse order as they are arranged in a dictionary. Save the output as scrambled.txt .',
                                    'Arrange the lines in file dict.py in the opposite dictionary order storing it in scrambled.txt file.',
                                    'Order the contents of file dict.py in the reverse order of dictionary sorting and save it in scrambled.txt file.']}, ignore_index = True)

#63
sort = sort.append({'Command':     'sort -rV ver.doc',
                    'NL Queries':  ['Reverse sort file ver.doc containing version numbers in natural order.',
                                    'Arrange the version numbers in ver.doc file with latest in top and oldest in bottom.',
                                    'Sort the contents of file ver.doc treating them as version numbers and in reverse order.']}, ignore_index = True)

#64
sort = sort.append({'Command':     'sort -rV ver.doc -o sortver.doc',
                    'NL Queries':  ['Reverse sort file ver.doc containing version numbers in natural order. Save the output in sortver.doc file.',
                                    'Arrange the version numbers in ver.doc file with latest in top and oldest in bottom. Store the output in sortver.doc file.',
                                    'Sort the contents of file ver.doc treating them as version numbers and in reverse order, saving the result in sortver.doc file.']}, ignore_index = True)

#65
sort = sort.append({'Command':     'sort -r -',
                    'NL Queries':  ['Reverse sort the lines read from stdin.',
                                    'Sort the lines read from stdin in reverse order.',
                                    'Arrange the lines taken input from STDIN in reverse order.',
                                    'Order the input lines in opposite order.']}, ignore_index = True)

#66
sort = sort.append({'Command':     'sort - -ro serial.txt',
                    'NL Queries':  ['Reverse sort the lines read from stdin and save it in file serial.txt .',
                                    'Sort the lines read from stdin in reverse order and save it as serial.txt .',
                                    'Arrange the lines taken input from STDIN in reverse order and use serial.txt file to save it.',
                                    'Order the input lines in opposite order and save it in serial.txt file.']}, ignore_index = True)

#67
sort = sort.append({'Command':     'sort -s marks.txt',
                    'NL Queries':  ['Stable sort the file marks.txt .',
                                    'Sort the file marks.txt without using last resort comparison.',
                                    'Perform stable sort on the contents of marks.txt .']}, ignore_index = True)

#68
sort = sort.append({'Command':     'sort -s marks.txt -o ranks.txt',
                    'NL Queries':  ['Stable sort the file marks.txt and save the output in ranks.txt file.',
                                    'Sort the file marks.txt without using last resort comparison and save it in ranks.txt file.',
                                    'Perform stable sort on the contents of marks.txt and save the result as ranks.txt .']}, ignore_index = True)

#69
sort = sort.append({'Command':     'sort --files0-from=files.txt',
                    'NL Queries':  ['Sort the files with names mentioned in files.txt file and separated by NULL character.',
                                    'Sort all the files with names mentioned in files.txt . Use file name separator to be NULL character.',
                                    'Sort the contents of file whose names are mentioned in files.txt . NULL is to be used as name separator.']}, ignore_index = True)

#70
sort = sort.append({'Command':     'sort --files0-from=files.txt -o hehe.txt',
                    'NL Queries':  ['Sort the files with names mentioned in files.txt file and separated by NULL character. Save the output in hehe.txt file.',
                                    'Sort all the files with names mentioned in files.txt . Use file name separator to be NULL character. Store the output in hehe.txt file.',
                                    'Arrange the contents of files whose names are stated in files.txt and are separated by NULL . Save the result in hehe.txt .']}, ignore_index = True)

#71
sort = sort.append({'Command':     'sort check.txt --debug',
                    'NL Queries':  ['Sort the file check.txt and display the part of line used to order them.',
                                    'Arrange the contents of file check.txt and show the part of string used for comparison.',
                                    'Order the content of the file check.txt and display what part of line was used for comparing.']}, ignore_index = True)

#72
sort = sort.append({'Command':     'sort -r check.txt --debug',
                    'NL Queries':  ['Reverse sort the file check.txt and display the part of line used to order them.',
                                    'Sort the contents of check.txt in opposite order and also show the part used for comparison.',
                                    'Arrange the contents of check.txt in reverse order and tell me the part of key used for sorting.']}, ignore_index = True)

#73
sort = sort.append({'Command':     'sort -T\"~/exec/\" check.txt -o test.txt',
                    'NL Queries':  ['Sort the file check.txt using ~/ecec/ as temporary directory save it in test.txt file.',
                                    'Using ~/exec/ as a temporary folder, sort check.txt and save the output in test.txt file.',
                                    'Save the sorted content of check.txt to test.txt and use ~/exec for temporary directory.']}, ignore_index = True)

#74
sort = sort.append({'Command':     'sort big.txt --compress-program=gzip',
                    'NL Queries':  ['Sort the file big.txt and use gzip command for compressing temporary files.',
                                    'Use gzip for compressing temporary files, sort big.txt file.',
                                    'Order the contents of big.txt and use gzip for compressing temporary files.']}, ignore_index = True)

#75
sort = sort.append({'Command':     'sort big.txt --compress-program=gzip -o sortedbig.txt',
                    'NL Queries':  ['Sort the file big.txt and use gzip command for compressing temporary files. Save the output in sortedbig.txt file.',
                                    'Use gzip for compressing temporary files, sort big.txt file. Store the output in sortedbig.txt file.',
                                    'Order the contents of big.txt and use gzip for compressing temporary files and saving the result in sortedbig.txt .']}, ignore_index = True)

#76
sort = sort.append({'Command':     'sort big.txt --compress-program=bzip2',
                    'NL Queries':  ['Sort the file big.txt and use bzip2 command for compressing temporary files.',
                                    'Use bzip2 for compressing temporary files, sort big.txt file.',
                                    'Order the contents of big.txt and use bzip2 for compressing temporary files.']}, ignore_index = True)

#77
sort = sort.append({'Command':     'sort big.txt --compress-program=bzip2 -o sortedbig.txt',
                    'NL Queries':  ['Sort the file big.txt and use bzip2 command for compressing temporary files. Save the output in sortedbig.txt file.',
                                    'Use bzip2 for compressing temporary files, sort big.txt file. Store the output in sortedbig.txt file.',
                                    'Order the contents of big.txt and use bzip2 for compressing temporary files and saving the result in sortedbig.txt .']}, ignore_index = True)

#78
sort = sort.append({'Command':     'sort big.txt --compress-program=zip',
                    'NL Queries':  ['Sort the file big.txt and use zip command for compressing temporary files.',
                                    'Order the contents of big.txt and use zip for compressing temporary files.',
                                    'Use zip for compressing temporary files, sort big.txt file.']}, ignore_index = True)

#79
#sort = sort.append({'Command':     'sort big.txt --compress-program=zip -o sortedbig.txt',
#                    'NL Queries':  ['Sort the file big.txt and use zip command for compressing temporary files. Save the output in sortedbig.txt file.',
#                                    'Use zip for compressing temporary files, sort big.txt file. Store the output in sortedbig.txt file.',
#                                    'Order the contents of big.txt and use zip for compressing temporary files and saving the result in sortedbig.txt .']}, ignore_index = True)

#80
sort = sort.append({'Command':     'sort -r big.txt --compress-program=gzip',
                    'NL Queries':  ['Reverse sort the file big.txt and use gzip command for compressing temporary files.',
                                    'Using gzip to compress temporary files, reverse sort the contents of big.txt .',
                                    'Compressing the temporary files by gzip, sort big.txt in reverse order.']}, ignore_index = True)

#81
sort = sort.append({'Command':     'sort -r big.txt --compress-program=gzip -o sortedbig.txt',
                    'NL Queries':  ['Reverse sort the file big.txt and use gzip command for compressing temporary files. Save the output in sortedbig.txt file.',
                                    'Using gzip to compress temporary files, reverse sort the contents of big.txt . Store the result in sortedbig.txt .',
                                    'Compressing the temporary files by gzip, sort big.txt in reverse order and save the output in sortedbig.txt .']}, ignore_index = True)

#82
sort = sort.append({'Command':     'sort -r big.txt --compress-program=bzip2',
                    'NL Queries':  ['Reverse sort the file big.txt and use bzip2 command for compressing temporary files.',
                                    'Using bzip2 to compress temporary files, reverse sort the contents of big.txt .',
                                    'Compressing the temporary files by bzip2, sort big.txt in reverse order.']}, ignore_index = True)

#83
sort = sort.append({'Command':     'sort -r big.txt --compress-program=bzip2 -o sortedbig.txt',
                    'NL Queries':  ['Reverse sort the file big.txt and use bzip2 command for compressing temporary files. Save the output in sortedbig.txt file.',
                                    'Using bzip2 to compress temporary files, reverse sort the contents of big.txt . Store the result in sortedbig.txt .',
                                    'Compressing the temporary files by bzip2, sort big.txt in reverse order and save the output in sortedbig.txt .']}, ignore_index = True)

#84
sort = sort.append({'Command':     'sort -r big.txt --compress-program=zip',
                    'NL Queries':  ['Reverse sort the file big.txt and use zip command for compressing temporary files.',
                                    'Using zip to compress temporary files, reverse sort the contents of big.txt .',
                                    'Compressing the temporary files by zip, sort big.txt in reverse order.']}, ignore_index = True)

#85
sort = sort.append({'Command':     'sort -r big.txt --compress-program=zip -o sortedbig.txt',
                    'NL Queries':  ['Reverse sort the file big.txt and use zip command for compressing temporary files. Save the output in sortedbig.txt file.',
                                    'Using zip to compress temporary files, reverse sort the contents of big.txt . Store the result in sortedbig.txt .',
                                    'Compressing the temporary files by zip, sort big.txt in reverse order and save the output in sortedbig.txt .']}, ignore_index = True)

#86
sort = sort.append({'Command':     'sort -R lhead.txt',
                    'NL Queries':   ['Sort the lines in lhead.txt randomly.',
                                     'Randomly permute the lines of lhead.txt .',
                                     'Reorder the contents of lhead.txt in random order.']}, ignore_index = True)

#87
sort = sort.append({'Command':     'sort -R lhead.txt -o randout.txt',
                    'NL Queries':   ['Sort the lines in lhead.txt randomly and save the output in randout.txt file.',
                                     'Reorder the contents of lhead.txt in random order and save it in randout.txt file.',
                                     'Save the randomly permuted lines of lhead.txt in randout.txt .']}, ignore_index = True)

#88
sort = sort.append({'Command':     'sort -b spaces.txt',
                    'NL Queries':  ['Sort the lines in file spaces.txt ignoring leading blanks.',
                                    'Ignore the leading blanks while sorting spaces.txt file.',
                                    'Do not consider starting white spaces and sort spaces.txt file.']}, ignore_index = True)

#89
sort = sort.append({'Command':     'sort -br spaces.txt',
                    'NL Queries':  ['Reverse sort the lines in file spaces.txt ignoring leading blanks.',
                                    'Ignore the leading blanks while sorting spaces.txt file in reverse order.',
                                    'Do not consider starting white spaces and reverse sort spaces.txt file.']}, ignore_index = True)

#90
sort = sort.append({'Command':     'sort -b spaces.txt -o ss.txt',
                    'NL Queries':  ['Sort the lines in file spaces.txt ignoring leading blanks and save it in ss.txt file.',
                                    'Ignore the leading blanks while sorting spaces.txt file and save the result to ss.txt .',
                                    'Do not consider starting white spaces and sort spaces.txt file. Save the output in ss.txt file.']}, ignore_index = True)

#91
sort = sort.append({'Command':     'sort -br spaces.txt -o ss.txt',
                    'NL Queries':  ['Reverse sort the lines in file spaces.txt ignoring leading blanks and save it in ss.txt file.',
                                    'Ignore the leading blanks while sorting spaces.txt file in reverse order. Save the output in ss.txt file.',
                                    'Do not consider starting white spaces and reverse sort spaces.txt file. Store the output in ss.txt .']}, ignore_index = True)

#92
sort = sort.append({'Command':     'sort -R --random-source=rand.txt text.txt',
                    'NL Queries':  ['Sort the lines of text.txt randomly using seed from rand.txt file.',
                                    'Using seeds from rand.txt sort text.txt .',
                                    'Randomly sort text.txt . Use random seeding from rand.txt file.']}, ignore_index = True)

#93
sort = sort.append({'Command':     'sort -R --random-source=rand.txt text.txt -o randomize.txt',
                    'NL Queries':  ['Sort the lines of text.txt randomly using seed from rand.txt file and save the output in randomize.txt file.',
                                    'Using seeds from rand.txt sort text.txt . Store the output in randomize.txt file.',
                                    'Randomly sort text.txt . Use random seeding from rand.txt file. Save the result as randomize.txt .']}, ignore_index = True)

#94
sort = sort.append({'Command':     'sort --parallel=24 bigdata.txt',
                    'NL Queries':  ['Sort the file bigdata.txt by parallelizing it over 24 threads.',
                                    'Parallely processing the data over 24 threads, sort bigdata.txt .',
                                    'Order the contents of bigdata.txt by processing it in 24 threads.']}, ignore_index = True)

#95
sort = sort.append({'Command':     'sort --parallel=24 bigdata.txt -o sorteddata.txt',
                    'NL Queries':  ['Sort the file bigdata.txt by parallelizing it over 24 threads. Save the output as sorteddata.txt file.',
                                    'Parallely processing the data over 24 threads, sort bigdata.txt and save the result as sorteddata.txt .',
                                    'Order the contents of bigdata.txt by processing it in 24 threads. Save the data as sorteddata.txt file.']}, ignore_index = True)

#96
sort = sort.append({'Command':     'sort -f --parallel=24 bigdata.txt',
                    'NL Queries':  ['Reverse sort the file bigdata.txt by parallelizing it over 24 threads. Do not perform case-sensitive sorting.',
                                    'Parallely processing the data over 24 threads, sort bigdata.txt . Perform case-insensitive sort.',
                                    'Order the contents of bigdata.txt by processing it in 24 threads and treat upper and lower case the same.']}, ignore_index = True)

#97
sort = sort.append({'Command':     'sort -n --parallel=24 bigdata.txt -o sorteddata.txt',
                    'NL Queries':  ['Sort the file bigdata.txt by parallelizing it over 24 threads. Perform numeric sorting. Save the output as sorteddata.txt file.',
                                    'Parallely processing the data over 24 threads, numerically sort bigdata.txt and save the result as sorteddata.txt .',
                                    'Numerically order the contents of bigdata.txt by processing it in 24 threads and treat upper and lower case the same.']}, ignore_index = True)

#98
sort = sort.append({'Command':     'sort -S1M smalldata.txt',
                    'NL Queries':  ['Sort the file smalldata.txt using buffer size of 1M .',
                                    'Order the file smalldata.txt using buffer of 1MB size.',
                                    'Arrange the contents of smalldata.txt in order by using 1 MB of buffer.']}, ignore_index = True)

#99
sort = sort.append({'Command':     'sort -S1M smalldata.txt -o sortsmall.txt',
                    'NL Queries':  ['Sort the file smalldata.txt using buffer size of 1M and save the output as sortsmall.txt file.',
                                    'Order the file smalldata.txt using buffer of 1MB size and store the output as sortsmall.txt file.',
                                    'Arrange the contents of smalldata.txt in order by using 1 MB of buffer. Save the result as sortsmall.txt file.']}, ignore_index = True)

#100
sort = sort.append({'Command':     'sort -rS1M smalldata.txt',
                    'NL Queries':  ['Reverse sort the file smalldata.txt using buffer size of 1M .',
                                    'Order the file smalldata.txt in reverse using buffer of 1MB size.',
                                    'Arrange the contents of smalldata.txt in reverse order by using 1 MB of buffer.']}, ignore_index = True)

#101
sort = sort.append({'Command':     'sort -rS1M smalldata.txt -o sortsmall.txt',
                    'NL Queries':  ['Reverse sort the file smalldata.txt using buffer size of 1M and save the output as sortsmall.txt file.',
                                    'Order the file smalldata.txt in reverse using buffer of 1MB size and store the output as sortsmall.txt file.',
                                    'Arrange the contents of smalldata.txt in reverse order by using 1 MB of buffer. Save the result as sortsmall.txt file.']}, ignore_index = True)

#102
sort = sort.append({'Command':     'sort -T~/exec/ check.txt',
                    'NL Queries':  ['Sort the file check.txt using ~/exec/ as temporary directory.',
                                    'Order the contents of file check.txt using ~/exec/ as temporary directory.',
                                    'Use ~/exec as temporary folder and sort the data in check.txt .']}, ignore_index = True)

#103
sort = sort.append({'Command':     'sort -bd random.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces and in dictionary order.',
                                     'Arrange the contents of random.txt in dictionary order ignoring the leading blanks.',
                                     'Order the contents of file random.txt in dictionary style and do not consider leading blanks.']}, ignore_index = True)

#104
sort = sort.append({'Command':     'sort -bf random.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces and case of alphabets.',
                                     'Arrange the data in file random.txt without considering leading blanks and case of alphabets.',
                                     'Ignoring case and leading blanks, sort random.txt file.']}, ignore_index = True)

#105
sort = sort.append({'Command':     'sort -bM random.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces and sort the months in year.',
                                     'Arrange the contents of random.txt in order of months ignoring the leading blanks.',
                                     'Order the contents of file random.txt in month style and do not consider leading blanks.']}, ignore_index = True)

#106
sort = sort.append({'Command':     'sort -bn random.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces. Use numeric sorting.',
                                     'Use numeric sorting to arrange the content of random.txt and ignore leading white spaces.',
                                     'Order the contents of random.txt in numeric order ignoring spaces at the start.']}, ignore_index = True)

#107
sort = sort.append({'Command':     'sort -bu random.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces. Suppress duplicate lines.',
                                     'Sort the contents of random.txt ignoring leading spaces. Remove repeating lines.',
                                     'Remove redundant lines and sort random.txt ignoring leading spaces.']}, ignore_index = True)

#108
sort = sort.append({'Command':     'sort -bt\';\' random.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces. Use ; as field separator.',
                                     'Using ; as word delimiter, sort random.txt without considering leading blanks.',
                                     'Arrange the contents of random.txt . Ignore starting spaces of each line and treat ; as word separator.']}, ignore_index = True)

#109
sort = sort.append({'Command':     'sort -dk2,2 random.txt',
                    'NL Queries':  ['Sort the lines in file random.txt according to the second word in the lines in dictionary order.',
                                    'Arrange the data in random.txt using second word as key for dictionary sorting.',
                                    'Order the lines of random.txt in dictionary style using 2nd word as key.']}, ignore_index = True)

#110
sort = sort.append({'Command':     'sort -du dup.txt',
                    'NL Queries':  ['Sort the lines in dup.txt in dictionary order and remove duplicate lines.',
                                    'Order the contents of dup.txt in dictionary style and remove duplicates.',
                                    'Removing duplicate lines, arrange the data in dup.txt in dictionary format.']}, ignore_index = True)

#111
sort = sort.append({'Command':     'sort -dt\'-\' manga.txt',
                    'NL Queries':  ['Sort the lines in manga.txt file in dictionary order using - as field separator.',
                                    'Order the contents of dup.txt in dictionary style and remove duplicates using - as field separator.',
                                    'Removing duplicate lines, arrange the data in dup.txt in dictionary format using - as a field separator.']}, ignore_index = True)

#112
sort = sort.append({'Command':     'sort -Mk3,3 reg.txt',
                    'NL Queries':  ['Sort the file reg.txt using third word as the only key. Do month sorting.',
                                    'Do month sort on content of reg.txt using 3rd word as key.',
                                    'Perform month sorting on reg.txt using third word as key.']}, ignore_index = True)

#113
sort = sort.append({'Command':     'sort -Mk3,3 -t\';\' rendom.txt',
                    'NL Queries':  ['Sort the file rendom.txt using third key as the only key. Do month sorting. Use ; as word delimiter.',
                                    'Do month sort on content of rendom.txt using 3rd word as key. Use ; as separator.',
                                    'Perform month sorting on rendom.txt using third word as key. For separating keys use ; .']}, ignore_index = True)

#114
sort = sort.append({'Command':     'sort -nk2,2 nums.txt',
                    'NL Queries':  ['Do numeric sort on the lines of file nums.txt base on second key.',
                                    'Perform numeric sort on nums.txt and use second word as key.',
                                    'Order the lines of nums.txt treating them as numbers and use 2nd word for sorting.']}, ignore_index = True)

#115
sort = sort.append({'Command':     'sort -nk2,2 -t\',\' nums.txt',
                    'NL Queries':  ['Do numeric sort on the lines of file nums.txt base on second key. Use , as delimiter.',
                                    'Use , as field separator. Perform numeric sort on nums.txt and use second word as key.',
                                    'Use , as word separator. Order the lines of nums.txt treating them as numbers and use 2nd word for sorting.']}, ignore_index = True)

#116
sort = sort.append({'Command':     'sort -nt\';\' nums.txt',
                    'NL Queries':  ['Do numeric sort on the lines of file nums.txt base on second key. Use ; as delimiter.',
                                    'Use , as field separator. Perform numeric sort on nums.txt .',
                                    'Use , as word separator. Order the lines of nums.txt treating them as numbers .']}, ignore_index = True)

#117
sort = sort.append({'Command':     'sort -h readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers.',
                                    'Sort readme.txt treating the contents as human friendly numbers.',
                                    'Arrange the contents of readme.txt considering them as human readable.']}, ignore_index = True)

#118
sort = sort.append({'Command':     'sort -hb readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Ignore the spaces at the starting of line.',
                                    'Ignoring leading blanks , sort readme.txt treating the contents as human friendly numbers.',
                                    'Arrange the contents of readme.txt considering them as human readable. Do not consider starting white spaces.']}, ignore_index = True)

#119
sort = sort.append({'Command':     'sort -hk2,2 readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use second key to sort.',
                                    '']}, ignore_index = True)

#120
sort = sort.append({'Command':     'sort -ht\';\' readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use ; as delimiter for keys.']}, ignore_index = True)

#121
sort = sort.append({'Command':     'sort -hu readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Remove duplicate lines.']}, ignore_index = True)

#122
sort = sort.append({'Command':     'sort -hut\'-\' readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Remove duplicate lines and use - as delimiter between keys.']}, ignore_index = True)

#123
sort = sort.append({'Command':     'sort -hbt\'-\' readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Ignore starting spaces and use - as delimiter.']}, ignore_index = True)

#124
sort = sort.append({'Command':     'sort -hk5,5 -t\':\' readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Using : as delimiter and 5th key as the only key.']}, ignore_index = True)

#125
sort = sort.append({'Command':     'sort -hft\',\' readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use , as delimiter and do case-insensitive comparison.']}, ignore_index = True)

#126
sort = sort.append({'Command':     'sort -huk4,7  readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Remove duplicate lines and use columns 4 through 7 as keys.']}, ignore_index = True)

#127
sort = sort.append({'Command':     'sort -hbk2,5 readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Ignore starting blank spaces and use keys 2 through 5.']}, ignore_index = True)

#128
sort = sort.append({'Command':     'sort -huk5,8 -t\'.\' readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use . as delimiter and columns 5 through 8 as keys. Remove duplicate lines.']}, ignore_index = True)

#129
sort = sort.append({'Command':     'sort -hbuk3,6 readme.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use columns 3 to 6 for comparison. Ignore starting white spaces and remove duplicate lines.']}, ignore_index = True)

#130
sort = sort.append({'Command':     'sort -bdr random.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces and in dictionary order.']}, ignore_index = True)

#131
sort = sort.append({'Command':     'sort -bfr random.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces and case of alphabets.']}, ignore_index = True)

#132
sort = sort.append({'Command':     'sort -bMr random.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces and sort the months in year.']}, ignore_index = True)

#133
sort = sort.append({'Command':     'sort -bnr random.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces. Use numeric sorting.']}, ignore_index = True)

#134
sort = sort.append({'Command':     'sort -bru random.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces. Suppress duplicate lines.']}, ignore_index = True)

#135
sort = sort.append({'Command':     'sort -brt\';\' random.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces. Use ; as field separator.']}, ignore_index = True)

#136
sort = sort.append({'Command':     'sort -drk2,2 random.txt',
                    'NL Queries':  ['Reverse sort the lines in file random.txt according to the second word in the lines in dictionary order.']}, ignore_index = True)

#137
sort = sort.append({'Command':     'sort -dru dup.txt',
                    'NL Queries':  ['Reverse sort the lines in dup.txt in dictionary order and remove duplicate lines.']}, ignore_index = True)

#138
sort = sort.append({'Command':     'sort -drt\'-\' manga.txt',
                    'NL Queries':  ['Reverse sort the lines in manga.txt file in dictionary order using - as field separator.']}, ignore_index = True)

#139
sort = sort.append({'Command':     'sort -rMk3,3 reg.txt',
                    'NL Queries':  ['Reverse sort the file reg.txt using third key as the only key. Do month sorting.']}, ignore_index = True)

#140
sort = sort.append({'Command':     'sort -rMk3,3 -t\';\' rendom.txt',
                    'NL Queries':  ['Reverse sort the file rendom.txt using third key as the only key. Do month sorting. Use ; as delimiter.']}, ignore_index = True)

#141
sort = sort.append({'Command':     'sort -rnk2,2 nums.txt',
                    'NL Queries':  ['Do reverse numeric sort on the lines of file nums.txt base on second key.']}, ignore_index = True)

#142
sort = sort.append({'Command':     'sort -rnk2,2 -t\',\' nums.txt',
                    'NL Queries':  ['Do reverse numeric sort on the lines of file nums.txt base on second key. Use , as delimiter.']}, ignore_index = True)

#143
sort = sort.append({'Command':     'sort -rnt\';\' nums.txt',
                    'NL Queries':  ['Do reverse numeric sort on the lines of file nums.txt base on second key. Use ; as delimiter.']}, ignore_index = True)

#144
sort = sort.append({'Command':     'sort -rh readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers.']}, ignore_index = True)

#145
sort = sort.append({'Command':     'sort -hrb readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Ignore the spaces at the starting of line.']}, ignore_index = True)

#146
sort = sort.append({'Command':     'sort -hrk2,2 readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use second key as the only key to sort.']}, ignore_index = True)

#147
sort = sort.append({'Command':     'sort -rht\';\' readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use ; as delimiter for keys.']}, ignore_index = True)

#148
sort = sort.append({'Command':     'sort -hru readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Remove duplicate lines.']}, ignore_index = True)

#149
sort = sort.append({'Command':     'sort -hrut\'-\' readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Remove duplicate lines and use - as delimiter between keys.']}, ignore_index = True)

#150
sort = sort.append({'Command':     'sort -rhbt\'-\' readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Ignore starting spaces and use - as delimiter.']}, ignore_index = True)

#151
sort = sort.append({'Command':     'sort -rhk5,5 -t\':\' readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Using : as delimiter and 5th key as the only key.']}, ignore_index = True)

#152
sort = sort.append({'Command':     'sort -rhft\',\' readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use , as delimiter and do case-insensitive comparison.']}, ignore_index = True)

#153
sort = sort.append({'Command':     'sort -rhuk4,7  readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Remove duplicate lines and use columns 4 through 7 as keys.']}, ignore_index = True)

#154
sort = sort.append({'Command':     'sort -rhbk2,5 readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Ignore starting blank spaces and use keys 2 through 5.']}, ignore_index = True)

#155
sort = sort.append({'Command':     'sort -rhuk5,8 -t\'.\' readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use . as delimiter and columns 5 through 8 as keys. Remove duplicate lines.']}, ignore_index = True)

#156
sort = sort.append({'Command':     'sort -rhbuk3,6 readme.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use columns 3 to 6 for comparison. Ignore starting blank spaces and remove duplicate lines.']}, ignore_index = True)

#157
sort = sort.append({'Command':     'sort -bd random.txt -o sorted.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces and in dictionary order. Save the output as sorted.txt .']}, ignore_index = True)

#158
sort = sort.append({'Command':     'sort -bf random.txt -o sorted.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces and case of alphabets. Save the output as sorted.txt .']}, ignore_index = True)

#159
sort = sort.append({'Command':     'sort -bM random.txt -o sorted.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces and sort the months in year. Save the output as sorted.txt .']}, ignore_index = True)

#160
sort = sort.append({'Command':     'sort -bn random.txt -o sad.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces. Use numeric sorting. Save the output as sad.txt file.']}, ignore_index = True)

#161
sort = sort.append({'Command':     'sort -bu random.txt -o mad.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces. Suppress duplicate lines. Save the output as mad.txt file.']}, ignore_index = True)

#162
sort = sort.append({'Command':     'sort -bt\';\' random.txt -o tank.txt',
                    'NL Queries':   ['Sort the lines in the file random.txt ignoring starting white spaces. Use ; as field separator. Save the output as tank.txt file.']}, ignore_index = True)

#163
sort = sort.append({'Command':     'sort -dk2,2 random.txt -o pratik.txt',
                    'NL Queries':  ['Sort the lines in file random.txt according to the second word in the lines in dictionary order. Save the output as tank.txt file.']}, ignore_index = True)

#164
sort = sort.append({'Command':     'sort -du dup.txt -o pratik.txt',
                    'NL Queries':  ['Sort the lines in dup.txt in dictionary order and remove duplicate lines. Save the output as pratik.txt file.']}, ignore_index = True)

#165
sort = sort.append({'Command':     'sort -dt\'-\' manga.txt -o holla.txt',
                    'NL Queries':  ['Sort the lines in manga.txt file in dictionary order using - as field separator. Save the output as holla.txt file.']}, ignore_index = True)

#166
sort = sort.append({'Command':     'sort -Mk3,3 reg.txt -o ~/ink.txt',
                    'NL Queries':  ['Sort the file reg.txt using third key as the only key. Do month sorting. Save the output as ink.txt in home directory.']}, ignore_index = True)

#167
sort = sort.append({'Command':     'sort -Mk3,3 -t\';\' rendom.txt -o ~/waka.txt',
                    'NL Queries':  ['Sort the file rendom.txt using third key as the only key. Do month sorting. Use ; as delimiter. Save the output as waka.txt in home directory.']}, ignore_index = True)

#168
sort = sort.append({'Command':     'sort -nk2,2 nums.txt -o ~/anthrax.txt',
                    'NL Queries':  ['Do numeric sort on the lines of file nums.txt base on second key. Save the output as anthrax.txt in home directory.']}, ignore_index = True)

#169
sort = sort.append({'Command':     'sort -nk2,2 -t\',\' nums.txt -o ~/numb.txt',
                    'NL Queries':  ['Do numeric sort on the lines of file nums.txt base on second key. Use , as delimiter. Save the output as ~/numb.txt file.']}, ignore_index = True)

#170
sort = sort.append({'Command':     'sort -nt\';\' nums.txt -o ~/tower.txt',
                    'NL Queries':  ['Do numeric sort on the lines of file nums.txt base on second key. Use ; as delimiter. Save the output as tower.txt in home directory.']}, ignore_index = True)

#171
sort = sort.append({'Command':     'sort -h readme.txt -o ~/texas.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Save the output as texas.txt file in home.']}, ignore_index = True)

#172
sort = sort.append({'Command':     'sort -hb readme.txt -o ~/otter.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Ignore the spaces at the starting of line. Save the output as ~/otter.txt file.']}, ignore_index = True)

#173
sort = sort.append({'Command':     'sort -hk2,2 readme.txt -o ~/kettle.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use second key as the only key to sort. Save the file as kettle.txt in home directory.']}, ignore_index = True)

#174
sort = sort.append({'Command':     'sort -ht\';\' readme.txt -o ~/nevada.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use ; as delimiter for keys. Save the file as nevada.txt in home directory.']}, ignore_index = True)

#175
sort = sort.append({'Command':     'sort -hu readme.txt -o ~/ostrich.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Remove duplicate lines. Save the file as ostritch.txt in home directory.']}, ignore_index = True)

#176
sort = sort.append({'Command':     'sort -hut\'-\' readme.txt -o ~/water.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Remove duplicate lines and use - as delimiter between keys. Save the file as water.txt in home directory.']}, ignore_index = True)

#177
sort = sort.append({'Command':     'sort -hbt\'-\' readme.txt -o ~/yak.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Ignore starting spaces and use - as delimiter. Save the file as yak.txt in home directory.']}, ignore_index = True)

#178
sort = sort.append({'Command':     'sort -hk5,5 -t\':\' readme.txt -o ~/orange.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Using : as delimiter and 5th key as the only key. Save the file as orange.txt in home directory.']}, ignore_index = True)

#179
sort = sort.append({'Command':     'sort -huk4,7  readme.txt -o check.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Remove duplicate lines and use columns 4 through 7 as keys. Save the output as check.txt file.']}, ignore_index = True)

#180
sort = sort.append({'Command':     'sort -hbk2,5 readme.txt -o another.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Ignore starting blank spaces and use keys 2 through 5. Save the output as another.txt named file.']}, ignore_index = True)

#181
sort = sort.append({'Command':     'sort -huk5,8 -t\'.\' readme.txt -o stand.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use . as delimiter and columns 5 through 8 as keys. Remove duplicate lines. Save the output as stand.txt file.']}, ignore_index = True)

#182
sort = sort.append({'Command':     'sort -hbuk3,6 readme.txt -o miranda.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use columns 3 to 6 for comparison. Ignore starting white spaces and remove duplicate lines. Save the output as miranda.txt file.']}, ignore_index = True)

#183
sort = sort.append({'Command':     'sort -brd random.txt -o sorted.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces and in dictionary order. Save the output as sorted.txt .']}, ignore_index = True)

#184
sort = sort.append({'Command':     'sort -rbf random.txt -o sorted.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces and case of alphabets. Save the output as sorted.txt .']}, ignore_index = True)

#185
sort = sort.append({'Command':     'sort -rbM random.txt -o sorted.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces and sort the months in year. Save the output as sorted.txt .']}, ignore_index = True)

#186
sort = sort.append({'Command':     'sort -rbn random.txt -o sad.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces. Use numeric sorting. Save the output as sad.txt file.']}, ignore_index = True)

#187
sort = sort.append({'Command':     'sort -rbu random.txt -o mad.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces. Suppress duplicate lines. Save the output as mad.txt file.']}, ignore_index = True)

#188
sort = sort.append({'Command':     'sort -rbt\';\' random.txt -o tank.txt',
                    'NL Queries':   ['Reverse sort the lines in the file random.txt ignoring starting white spaces. Use ; as field separator. Save the output as tank.txt file.']}, ignore_index = True)

#189
sort = sort.append({'Command':     'sort -rdk2,2 random.txt -o pratik.txt',
                    'NL Queries':  ['Reverse sort the lines in file random.txt according to the second word in the lines in dictionary order. Save the output as tank.txt file.']}, ignore_index = True)

#190
sort = sort.append({'Command':     'sort -rdu dup.txt -o pratik.txt',
                    'NL Queries':  ['Reverse sort the lines in dup.txt in dictionary order and remove duplicate lines. Save the output as pratik.txt file.']}, ignore_index = True)

#191
sort = sort.append({'Command':     'sort -rdt\'-\' manga.txt -o holla.txt',
                    'NL Queries':  ['Sort the lines in manga.txt file in reverse dictionary order using - as field separator. Save the output as holla.txt file.']}, ignore_index = True)

#192
sort = sort.append({'Command':     'sort -rMk3,3 reg.txt -o ~/ink.txt',
                    'NL Queries':  ['Revevrse sort the file reg.txt using third key as the only key. Do month sorting. Save the output as ink.txt in home directory.']}, ignore_index = True)

#193
sort = sort.append({'Command':     'sort -rMk3,3 -t\';\' rendom.txt -o ~/waka.txt',
                    'NL Queries':  ['Sort the file rendom.txt using third key as the only key. Do reverse month sorting. Use ; as delimiter. Save the output as waka.txt in home directory.']}, ignore_index = True)

#194
sort = sort.append({'Command':     'sort -rnk2,2 nums.txt -o ~/anthrax.txt',
                    'NL Queries':  ['Do reverse numeric sort on the lines of file nums.txt base on second key. Save the output as anthrax.txt in home directory.']}, ignore_index = True)

#195
sort = sort.append({'Command':     'sort -rnk2,2 -t\',\' nums.txt -o ~/numb.txt',
                    'NL Queries':  ['Do reverse numeric sort on the lines of file nums.txt base on second key. Use , as delimiter. Save the output as ~/numb.txt file.']}, ignore_index = True)

#196
sort = sort.append({'Command':     'sort -rnt\';\' nums.txt -o ~/tower.txt',
                    'NL Queries':  ['Do reverse numeric sort on the lines of file nums.txt base on second key. Use ; as delimiter. Save the output as tower.txt in home directory.']}, ignore_index = True)

#197
sort = sort.append({'Command':     'sort -rh readme.txt -o ~/texas.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Save the output as texas.txt file in home.']}, ignore_index = True)

#198
sort = sort.append({'Command':     'sort -rhb readme.txt -o ~/otter.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Ignore the spaces at the starting of line. Save the output as ~/otter.txt file.']}, ignore_index = True)

#199
sort = sort.append({'Command':     'sort -rhk2,2 readme.txt -o ~/kettle.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use second key as the only key to sort. Save the file as kettle.txt in home directory.']}, ignore_index = True)

#200
sort = sort.append({'Command':     'sort -rht\';\' readme.txt -o ~/nevada.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use ; as delimiter for keys. Save the file as nevada.txt in home directory.']}, ignore_index = True)

#201
sort = sort.append({'Command':     'sort -rhu readme.txt -o ~/ostrich.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Remove duplicate lines. Save the file as ostritch.txt in home directory.']}, ignore_index = True)

#202
sort = sort.append({'Command':     'sort -rhut\'-\' readme.txt -o ~/water.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Remove duplicate lines and use - as delimiter between keys. Save the file as water.txt in home directory.']}, ignore_index = True)

#203
sort = sort.append({'Command':     'sort -rhbt\'-\' readme.txt -o ~/yak.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Ignore starting spaces and use - as delimiter. Save the file as yak.txt in home directory.']}, ignore_index = True)

#204
sort = sort.append({'Command':     'sort -rhk5,5 -t\':\' readme.txt -o ~/orange.txt',
                    'NL Queries':  ['Revevrse sort the readme.txt file as human readable numbers. Using : as delimiter and 5th key as the only key. Save the file as orange.txt in home directory.']}, ignore_index = True)

#205
sort = sort.append({'Command':     'sort -rhft\',\' readme.txt -o ~/ukraine.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use , as delimiter and do case-insensitive comparison. Save the output as ~/ukraine.txt file.']}, ignore_index = True)

#206
sort = sort.append({'Command':     'sort -rhuk4,7  readme.txt -o check.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Remove duplicate lines and use columns 4 through 7 as keys. Save the output as check.txt file.']}, ignore_index = True)

#207
sort = sort.append({'Command':     'sort -rhbk2,5 readme.txt -o another.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Ignore starting blank spaces and use keys 2 through 5. Save the output as another.txt named file.']}, ignore_index = True)

#208
sort = sort.append({'Command':     'sort -rhuk5,8 -t\'.\' readme.txt -o stand.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use . as delimiter and columns 5 through 8 as keys. Remove duplicate lines. Save the output as stand.txt file.']}, ignore_index = True)

#209
sort = sort.append({'Command':     'sort -rhbuk3,6 readme.txt -o miranda.txt',
                    'NL Queries':  ['Reverse sort the readme.txt file as human readable numbers. Use columns 3 to 6 for comparison. Ignore starting white spaces and remove duplicate lines. Save the output as miranda.txt file.']}, ignore_index = True)

#210
sort = sort.append({'Command':     'sort -hft\',\' readme.txt -o ~/ukraine.txt',
                    'NL Queries':  ['Sort the readme.txt file as human readable numbers. Use , as delimiter and do case-insensitive comparison. Save the output as ~/ukraine.txt file.']}, ignore_index = True)


print sort.shape
