import pandas as pd 

diff = pd.DataFrame(columns = ['Command','NL Queries'])

diff = diff.append({'Command':'diff file1.txt file2.txt','NL Queries':['How do I find the difference between files file1.txt and file2.txt?',
                              'What is the difference between file1.txt and file2.txt? Both files are in this folder.',
                                   'How do I display lines which are different from each other in file1.txt and file2.txt?']},ignore_index = True)

diff = diff.append({'Command':'diff -u file1.txt file2.txt','NL Queries':['How do I find the difference between file1.txt and file2.txt? Print all unique rows from both files.'
                                   'How do I print a unified set of all distinct rows in file1.txt and file2.txt?', 'How do I print unique rows from both file1.txt and file2.txt combined?'
                                        ]},ignore_index=True)

diff = diff.append({'Command':'diff -i file1.txt file2.txt','NL Queries':['How do I perform a case insensitive comparision of file1.txt and file2.txt? Print the difference on Command Line.',
                    'Command to print case insensitive difference between file1.txt and file2.txt in this folder.'
                         'Display differences between file1.txt and file2.txt. Take case insensitive differences.']},ignore_index=True)


#1
diff = diff.append({'Command':'diff -q chk1.txt chk2.txt',
                    'NL Queries':  ['Check if there is difference between file chk1.txt and chk2.txt or not.',
                         'Output whether there is a difference between chk1.txt and chk2.txt or not. Do not display the difference.',
                         'How do I check whether there is a difference between chk1.txt and chk2.txt present in this folder.',
                              'Check if chk1.txt is different than chk2.txt. If not, do not display the difference.',
                              'Are the contents of chk1.txt and chk2.txt different?']}, ignore_index = True)

#2
diff = diff.append({'Command':'diff -s chk1.txt chk2.txt',
                    'NL Queries':  ['Find difference between files chk1.txt and chk2.txt and report if they are same.',
                                   'Are the contents of chk1.txt and chk2.txt same? If not, display the difference.',
                                   'Check if chk1.txt is same as chk2.txt. If not,display the difference.'
                                   'Output whether there is similarity between chk1.txt and chk2.txt or not. If not, display the difference.',
                                        'How do I check whether the contents of chk1.txt and chk2.txt are the same.']}, ignore_index = True)

#3
diff = diff.append({'Command':     'diff -c chk1.txt chk2.txt',
                    'NL Queries':  ['Find difference between files chk1.txt and chk2.txt in context mode.',
                                    'Show the distinctions between chk1.txt and chk2.txt showing a few lines for context around the change.',
                                    'Display the difference between the files chk1.txt and chk2.txt with few lines around the change for reference.',
                                    'Distinguish between the files chk1.txt and chk2.txt in context mode.']}, ignore_index = True)

#4
diff = diff.append({'Command':'diff -e chk1.txt chk2.txt',
                    'NL Queries':  ['Find difference between files chk1.txt and chk2.txt and output an ed script.'
                                        'Show difference in contents of files chk1.txt and chk2.txt. Show an ed script on screen.'
                                        'How do I distinguish between chk1.txt and chk2.txt present in current folder? Show the difference on screen in form of ed script.']}, ignore_index = True)
                 
#5
diff = diff.append({'Command':     'diff -y chk1.txt chk2.txt',
                    'NL Queries':  ['Find difference between files chk1.txt and chk2.txt and output the differences side by side.',
                                        'Show distinction between chk1.txt and chk2.txt on adjacent columns on command line.',
                                        'How do I show the distinction between chk1.txt and chk2.txt side by side?',
                                        'Display difference in content between chk1.txt and chk2.txt linewise in two columns.']}, ignore_index = True)

#6
diff = diff.append({'Command':     'diff --width=5 chk1.txt chk2.txt',
                    'NL Queries':  ['Find difference between files chk1.txt and chk2.txt and restrict the number of columns of output to 5.',
                                        'Show distinction between chk1.txt and chk2.txt and output maximum 5 columns of screen.',
                                        'How do I show distinction between chk1.txt and chk2.txt? Show at most 5 columns.',
                                             'Display the difference between chk1.txt and chk2.txt. Output at most 5 columns.']}, ignore_index = True)

#7
diff = diff.append({'Command':     'diff -B space.txt line.txt',
                    'NL Queries':  ['Output the difference between space.txt and line.txt files ignoring blank lines.',
                                        'Show difference between space.txt and line.txt present in this folder. Do not include blank lines.',
                                   'How do I get the difference in contents between space.txt and line.txt? I do not want to include blank lines as a difference.',
                                        'Distinguish between line.txt and space.txt ignoring the blank lines.']}, ignore_index = True)

#8
diff = diff.append({'Command':     'diff -Z space.txt line.txt',
                    'NL Queries':  ['Output the difference between space.txt and line.txt files ignoring trailing white spaces.',
                                    'Distinguish between space.txt and line.txt files without considering the trailing white spaces.',
                                    'Show the differences between space.txt and line.txt without taking white spaces at the end of line into account.',
                                    'Display the differences between space.txt and line.txt files ignoring white spaces at the end of line.']}, ignore_index = True)

#9
diff = diff.append({'Command':     'diff -w space.txt line.txt',
                    'NL Queries':  ['Output the difference between space.txt and line.txt files ignoring white space differences.',
                                    'How to find the difference between space.txt and line.txt files without taking any white space difference into account?',
                                    'Distinguish between space.txt and line.txt ignoring white space differences.',
                                    'Show me the distinctions between space.txt and line.txt files without considering white space differences.']}, ignore_index = True)

#10
diff = diff.append({'Command':     'diff -b space.txt line.txt',
                    'NL Queries':  ['Output the difference between space.txt and line.txt files ignoring amount of white spaces.',
                                    'Show the distinctions between space.txt and line.txt without taking amount of spaces into account.',
                                    'Display the difference between space.txt and line.txt which do not involve amount of space as a change.',
                                    'How to check difference between the files space.txt and line.txt without considering white space amount.']}, ignore_index = True)

#11
diff = diff.append({'Command':     'diff -n space.txt line.txt',
                    'NL Queries':  ['Output the difference between space.txt and line.txt files in RCS format.',
                                    'Show the difference between the files space.txt and line.txt in revision control format.',
                                    'Distinguish between the files space.txt and line.txt files in version control form.']}, ignore_index = True)

#12
diff = diff.append({'Command':     'diff best worst',
                    'NL Queries':  ['Output the difference between best and worst directories.',
                                    'Display the difference between the directories named best and worst .',
                                    'What is the difference between best and worst directories?']}, ignore_index = True)

#13
diff = diff.append({'Command':     'diff -qi aa.txt AA.txt',
                    'NL Queries':  ['Output if there is difference between aa.txt and AA.txt not involving case differences.',
                                    'Check if there is a difference in files aa.txt and AA.txt files if upper and lower case are treated as same.',
                                    'Is there any point of distinction between aa.txt and AA.txt files without case sensitivity?']}, ignore_index = True)

#14
diff = diff.append({'Command':     'diff -yi aa.txt AA.txt',
                    'NL Queries':  ['Output the difference between aa.txt and AA.txt not involving case differences in side-by-side format.',
                                    'Ignoring case differences, show the differences between aa.txt and AA.txt in side by side format.',
                                    'Show the differences between aa.txt and AA.txt files placed next to each other. Do not involve case differences.']}, ignore_index = True)

#15
diff = diff.append({'Command':     'diff -ci aa.txt AA.txt',
                    'NL Queries':  ['Output the difference between aa.txt and AA.txt not involving case differences in context mode.',
                                    'Show the differences between aa.txt and AA.txt files without taking case of alphabets into account. Display the output in context format.',
                                    'Dispaly the lines in in files aa.txt and AA.txt which differ from each other ignoring case differences. Show some lines for reference around the changed lines.']}, ignore_index = True)

#16
diff = diff.append({'Command':     'diff -ui aa.txt AA.txt',
                    'NL Queries':  ['Show the differences in files aa.txt and AA.txt in unified format not involving case differences.',
                                    'Display the differences between files aa.txt and AA.txt in unified format. Do not consider case related differences.',
                                    'Show the lines which differ in the files aa.txt and AA.txt in unified format. Ignore case differences.']}, ignore_index = True)

#17
diff = diff.append({'Command':     'diff -nZ aa.txt AA.txt',
                    'NL Queries':  ['Show the differences in files aa.txt and AA.txt in RCS format not involving trailing white space differences.',
                                    'Do not consider trailing white space differences in comparing aa.txt and AA.tt files. Output the differences in RCS format.',
                                    'Display the distinctions between aa.txt and AA.txt files in version control format ignoring trailing white space differences.']}, ignore_index = True)

#18
diff = diff.append({'Command':     'diff -pw aa.c AA.c',
                    'NL Queries':  ['Show the differences in C source files aa.c and AA.c ignoring white space differences.',
                                    'Show any difference between C files aa.c and AA.c without considering white spaces.',
                                    'Display the distinctions between the C source files aa.c and AA.c . Do not show white space differences.']}, ignore_index = True)

#19
diff = diff.append({'Command':     'diff -pi aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp ignoring case-sensitive differences.',
                                    'Ignoring case differences, show the difference between the C source files aa.cpp and AA.cpp .',
                                    'Compare the C files aa.cpp and AA.cpp line by line and show the differences. Use case-insensitive comparison.']}, ignore_index = True)

#20
diff = diff.append({'Command':     'diff -pZ aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp ignoring trailing white space differences.',
                                    'Ignore trailing white spaces, show the distinctions between aa.cpp and AA.cpp C files.',
                                    'Distinguish between aa.cpp and AA.cpp considering them C files and ignoring trailing white spaces.']}, ignore_index = True)

#21
diff = diff.append({'Command':     'diff -pb aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp ignoring the amount of white space differences.',
                                    'List all the line by line differences in C files aa.cpp and AA.cpp . Do not consider amount of spaces as differences.',
                                    'Treating aa.cpp and AA.cpp as C files show the distinctions between aa.cpp and AA.cpp files. Amount of white spaces do not matter.']}, ignore_index = True)

#22
diff = diff.append({'Command':     'diff -pZ --speed-large-files aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp ignoring trailing white space differences. Use hueristics to speed up processing of the file.',
                                    'Quickly find out the distinctions between the C files aa.cpp and AA.cpp ignoring the trailing spaces.',
                                    'Using tricks to speed up the process, find differences between aa.cpp and AA.cpp files not including trailing spaces. Treat them as C source codes.',
                                    'Compare the big C source files aa.cpp and AA.cpp files, if trailing white spaces is not an issue.']}, ignore_index = True)

#23
diff = diff.append({'Command':     'diff -p --speed-large-files aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp using speedup heuristics.',
                                    'Compare the big C source files aa.cpp and AA.cpp files.',
                                    'Using tricks to speed up the process, find differences between aa.cpp and AA.cpp files.',
                                    'Quickly find out the distinctions between the C files aa.cpp and AA.cpp .']}, ignore_index = True)

#24
diff = diff.append({'Command':     'diff  --speed-large-files os1.txt os2.txt',
                    'NL Queries':  ['Show the differences in os1.txt and os2.txt files using speedup heuristics.',
                                    'Using heuristics for speed up, show the differences between os1.txt and os2.txt files.',
                                    'Quickly find out the distinctions between os1.txt and os2.txt files.']}, ignore_index = True)

#25
diff = diff.append({'Command':     'diff -pi --speed-large-files aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp using speedup heuristics. Do not perform case-sensitive comparisons.',
                                    'Compare the big C source files aa.cpp and AA.cpp files ignoring case sensitivity.',
                                    'Quickly find out the distinctions between the C files aa.cpp and AA.cpp treating upper and lower case alphabets as same.']}, ignore_index = True)

#26
diff = diff.append({'Command':     'diff -p --strip-trailing-cr aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp after removing trailing carriage return characters.',
                                    'Compare the C files aa.cpp and AA.cpp after removing trailing carriage return .',
                                    'Display the distinctions between aa.cpp and AA.cpp C files after stripping trailing carriage returns .']}, ignore_index = True)

#27
diff = diff.append({'Command':     'diff --strip-trailing-cr src1.txt src2.txt',
                    'NL Queries':  ['Show the differences between src1.txt and src2.txt file after stripping trailing carriage returns.',
                                    'Strip the trailing carriage returns from source files src1.txt and src2.txt and show distinctions between them.',
                                    'Remove the trailing cr from the files src1.txt and src2.txt and show the comparision.']}, ignore_index = True)

#28
diff = diff.append({'Command':     'diff -D BSD src1.cpp src2.cpp',
                    'NL Queries':  ['Merge the source files src1.cpp and src2.cpp using BSD preprocessor directive condition.',
                                    'Make merged \'#ifdef\' format output, conditional on the preprocessor macro BSD using the files src1.cpp and src2.cpp .',
                                    'Merge different versions of src1.cpp and src2.cpp using preprocessor identifier BSD.']}, ignore_index = True)

#29
diff = diff.append({'Command':     'diff -D BSD --strip-trailing-cr src1.cpp src2.cpp',
                    'NL Queries':  ['Merge the C source files src1.cpp and src2.cpp, after stripping trailing carriage returns, using BSD preprocessor directive condition.',
                                    'Make merged \'#ifdef\' format output, conditional on the preprocessor macro BSD using the files src1.cpp and src2.cpp after stripping trailing carriage returns.',
                                    'Merge different versions of src1.cpp and src2.cpp using preprocessor macro identifier BSD. Remove the trailing carriage returns before comparison.']}, ignore_index = True)

#30
diff = diff.append({'Command':     'diff -a a.out b.out',
                    'NL Queries':  ['Output the differences between files a.out and b.out treating them as text files.',
                                    'Treat a.out and b.out as text files and show the distinctions between them.',
                                    'Show the difference between the contents of a.out and b.out if they are treated as normal text files.']}, ignore_index = True)

#31
diff = diff.append({'Command':     'diff --color black.txt white.txt',
                    'NL Queries':  ['Show differences between texts black.txt and white.txt using color to show context.',
                                    'Show the differences between black.txt and white.txt in color.',
                                    'Using color, show the distinctions between black.txt and white.txt files.']}, ignore_index = True)

#32
diff = diff.append({'Command':     'diff -E undo.txt redo.txt',
                    'NL Queries':  ['Show the differences between undo.txt and redo.txt ignoring TAB expansions.',
                                    'Display the distinctions between undo.txt and redo.txt without considering tab expansion.',
                                    'Show the lines which differ in file undo.txt from redo.txt . Do not show tab expansion changes.']}, ignore_index = True)

#33
diff = diff.append({'Command':     'diff -B --strip-trailing-cr src1.txt src2.txt',
                    'NL Queries':  ['Show the differences between src1.txt and src2.txt file after stripping trailing carriage returns and removing empty line differences.',
                                    'Ignoring empty lines and trailing carriage returns, distinguish between src1.txt and src2.txt .',
                                    'After removing trailing CR, compare the files src1.txt and src2.txt . Do not show empty line differences.']}, ignore_index = True)

#34
diff = diff.append({'Command':     'diff -pB aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp ignoring blank line differences.',
                                    'Compare the C files aa.cpp and AA.cpp and remove blank line differences.',
                                    'Show the lines which differ when comparing C files aa.cpp and AA.cpp . Do not consider blank lines.']}, ignore_index = True)

#35
diff = diff.append({'Command':     'diff -N aa.doc AA.doc',
                    'NL Queries':  ['Show the differences files aa.doc and AA.doc . If any file is absent treat it as blank file.',
                                    'Treating the non existent file as empty, show the distinctions between aa.doc and AA.doc .',
                                    'Show the differences between the files aa.doc and AA.doc . Interpret absent file as empty.']}, ignore_index = True)

#36
diff = diff.append({'Command':     'diff -pN aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp . If any file is absent treat it as blank file.',
                                    'Treating the non existent file as empty, show the distinctions between aa.cpp and AA.cpp C source files.',
                                    'Show the differences between the C files aa.cpp and AA.cpp . Interpret absent file as empty.']}, ignore_index = True)

#37
diff = diff.append({'Command':     'diff -pE aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp ignoring TAB expansion changes.',
                                    'Display the distinctions between C files aa.cpp and AA.cpp without considering tab expansion as a change.',
                                    'Output the differences between aa.cpp and AA.cpp . Ignore any changes caused by TAB expansion.']}, ignore_index = True)

#38
diff = diff.append({'Command':     'diff -pl aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp and paginate the output.',
                                    'Paginate the difference between aa.cpp and AA.cpp C files.',
                                    'Output the distinctions between aa.cpp and AA.cpp C files and ready the output for printout.']}, ignore_index = True)

#39
diff = diff.append({'Command':     'diff -l aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences aa.cpp and AA.cpp and paginate the output.',
                                    'Paginate the difference between aa.cpp and AA.cpp .',
                                    'Output the distinctions between aa.cpp and AA.cpp and ready the output for printout.']}, ignore_index = True)

#40
diff = diff.append({'Command':     'diff -pBd aa.cpp AA.cpp',
                    'NL Queries':  ['Show the minimal differences in C source files aa.cpp and AA.cpp ignoring blank line differences.',
                                    'Compare the C files aa.cpp and AA.cpp and remove blank line differences. Output minimal differences between them.',
                                    'Show the lines which differ when comparing C files aa.cpp and AA.cpp . Do not consider blank lines. Output minimum difference between them.']}, ignore_index = True)

#41
diff = diff.append({'Command':     'diff -pBE aa.cpp AA.cpp',
                    'NL Queries':  ['Show the differences in C source files aa.cpp and AA.cpp ignoring blank line and tab expansion differences.',
                                    'Compare the C files aa.cpp and AA.cpp and remove blank line differences. Remove any tab expansion differences from output.',
                                    'Show the lines which differ when comparing C files aa.cpp and AA.cpp . Do not consider blank lines and tab expansion.']}, ignore_index = True)

#42
diff = diff.append({'Command':     'diff -I \'[0-9]\' num1.txt num2.txt',
                    'NL Queries':  ['Show the differences in files num1.txt num2.txt except number differences.',
                                    'Show all the differences between files num1.txt and num2.txt except those which match with regex \'[0-9]\' .',
                                    'Except the differences which match with \'[0-9]\' show differences between num1.txt and num2.txt .']}, ignore_index = True)

#43
diff = diff.append({'Command':     'diff -y --suppress-common-lines com1.txt com2.txt',
                    'NL Queries':  ['Show only the differences between com1.txt and com2.txt files in side-by-side format.',
                                    'Comapre the files com1.txt and com2.txt side by side ,and do not display common lines.',
                                    'Distinguish between com1.txt and com2.txt placing them next to each other. Hide common lines.']}, ignore_index = True)

#44
diff = diff.append({'Command':     'diff -y --left-column com1.txt com2.txt',
                    'NL Queries':  ['Show the differences between com1.txt and com2.txt files in side-by-side format and only left column for common lines.',
                                    'Compare com1.txt and com2.txt in side by side format, showing only left column for the common lines.',
                                    'Distinguish between com1.txt and com2.txt with both of them being displayed. Do not show identical lines more than once.']}, ignore_index = True)

#45
diff = diff.append({'Command':     'diff -y --width=50 com1.txt com2.txt',
                    'NL Queries':  ['Show the differences between com1.txt and com2.txt files in side-by-side format and width of 50 columns.',
                                    'In a window of 50 columns output the differences highlight com1.txt and com2.txt in side-by-side format.',
                                    'Show the contents of com1.txt and com2.txt next to each other and highlight the different lines.']}, ignore_index = True)

#46
diff = diff.append({'Command':     'diff --ignore-file-name-case sarah mcdaniel',
                    'NL Queries':  ['Compare the directories sarah and mcdaniel and output the differences. Do not consider file names to be case sensitive.',
                                    'Compare the directories sarah and mcdaniel . Compare the files without taking their names to be case sensitive.',
                                    'Find the difference between the directories sarah and mcdaniel . Comapre the files names considering lower and upper case to be same.']}, ignore_index = True)

#47
diff = diff.append({'Command':     'diff --from-file=model.txt sarah mcdaniel',
                    'NL Queries':  ['Compare the model.txt file with model.txt files in sarah and mcdaniel directories.',
                                    'Compare model.txt in pwd against sarah/model.txt and mcdaniel/model.txt files.',
                                    'Show distinctions between ./model.txt and sarah/model.txt, and ./model.txt and mcdaniel/model.txt .']}, ignore_index = True)

#48
diff = diff.append({'Command':     'diff --to-file=model.txt sarah mcdaniel',
                    'NL Queries':  ['Compare  with model.txt files in sarah and mcdaniel directories to model.txt in current directory.',
                                    'Compare sarah/model.txt and mcdaniel/model.txt files against model.txt in pwd.',
                                    'Show distinctions between sarah/model.txt and ./model.txt, and mcdaniel/model.txt and ./model.txt .']}, ignore_index = True)

#49
diff = diff.append({'Command':     'diff -r selena gomez',
                    'NL Queries':  ['Recursively compare directories selena and gomez .',
                                    'Show differences between selena and gomez directories recursively.',
                                    'Display the differences between selena and gomez directories. Also compare underlying directories.']}, ignore_index = True)

#50
diff = diff.append({'Command':     'diff -S singer selena gomez',
                    'NL Queries':  ['Compare directories selena and gomez starting from file named singer .',
                                    'Show the differences between selena and gomez and start comparing from file singer .',
                                    'Display the distinctions between directories selena and gomez and begin comparing from singer file.']}, ignore_index = True)

#51
diff = diff.append({'Command':     'diff -x \'*.c\' BSD LINUX',
                    'NL Queries':   ['Compare the directories BSD and LINUX except the files which ends with .c extension.',
                                     'Show differences between BSD and LINUX , but do not compare files ending with .c .',
                                     'Display the distinctiona between BSD and LINUX . Do not compare files with .c at end.']}, ignore_index = True)

#52
diff = diff.append({'Command':     'diff -X exc.txt BSD LINUX',
                    'NL Queries':   ['Compare the directories BSD and LINUX except the file names which match with those mentioned in exc.txt .',
                                     'Show differences between BSD and LINUX , but do not compare files matching with those stated in exc.txt .',
                                     'Display the distinctiona between BSD and LINUX . Do not compare whose name matches with pattern in exc.txt file.']}, ignore_index = True)

#53
diff = diff.append({'Command':     'diff --tabsize=10 monkey.txt king.txt',
                    'NL Queries':  ['Show the differences between monkey.txt and king.txt files using tabstop every 10 columns.',
                                    'Set tabstops every 10 columns. Compare monkey.txt and king.txt files.',
                                    'Show distinctions between monkey.txt and king.txt . Use tabstop every 10 columns.']}, ignore_index = True)

#54
diff = diff.append({'Command':     'diff --ignore-file-name-case -r WINDOWS BSD',
                    'NL Queries':  ['Output the differences between WINDOWS and BSD directories recursively and ignoring file name case.',
                                    'Treating upper and lower case file names as same, compare WINDOWS and BSD recursively.',
                                    'Show distinctions between WINDOWS and BSD recursively, and turn off case sensitivity for file names.']}, ignore_index = True)

#55
diff = diff.append({'Command':     'diff -rs BSD LINUX',
                    'NL Queries':   ['Compare the directories BSD and LINUX recursively and report identical files.',
                                     'Reporting identical files, recursively compare BSD and LINUX directories.',
                                     'Compare everything inside BSD and LINUX and report if some files are identical.']}, ignore_index = True)

#56
diff = diff.append({'Command':     'diff -r --starting-file=resume.txt BSD LINUX',
                    'NL Queries':   ['Compare the directories BSD and LINUX recursively starting from resume.txt file.',
                                     'Starting from file resume.txt , begin comparing BSD and LINUX directories recursively.',
                                     'Recursively compare BSD and LINUX starting from file resume.txt .']}, ignore_index = True)

#57
diff = diff.append({'Command':     'diff -rn BSD LINUX',
                    'NL Queries':   ['Compare the directories BSD and LINUX recursively and report differences in RCS format.',
                                     'Recursively compare and display differences between BSD and LINUX in RCS format.',
                                     'Compare and show points of distinctions between BSD and LINUX in version control format.']}, ignore_index = True)

#58
diff = diff.append({'Command':     'diff -ry BSD LINUX',
                    'NL Queries':   ['Compare the directories BSD and LINUX recursively and report differences in side by side format.',
                                     'Recursively compare and display differences between BSD and LINUX in side by side format.',
                                     'Compare and show points of distinctions between BSD and LINUX next to each other.']}, ignore_index = True)

#59
diff = diff.append({'Command':     'diff -rnx \'*.cpp\' BSD LINUX',
                    'NL Queries':   ['Compare the directories BSD and LINUX recursively and report differences in RCS format except the file names ending with .cpp .',
                                     'Recursively compare and display differences between BSD and LINUX in RCS format. Do not compare files with .cpp ending.',
                                     'Compare and show points of distinctions between BSD and LINUX in version control format. Exempt files with .cpp at end of their names.']}, ignore_index = True)

#60
diff = diff.append({'Command':     'diff -ru BSD LINUX',
                    'NL Queries':   ['Compare the directories BSD and LINUX recursively and report differences in unified format.',
                                     'How do I display differences in BSD and LINUX directories in unified form?',
                                     'How to show differences between BSD and LINUX with unique lines of context?']}, ignore_index = True)

#61
diff = diff.append({'Command':     'diff -rc BSD LINUX',
                    'NL Queries':   ['Compare the directories BSD and LINUX recursively and report differences in context format.',
                                     'How do I display differences in BSD and LINUX directories in context form?',
                                     'How to show differences between BSD and LINUX with lines for context around the change?']}, ignore_index = True)

#62
diff = diff.append({'Command':      'diff -C 2 facebook.txt twitter.txt',
                    'NL Queries':   ['Show the difference between facebook.txt and twitter.txt in context format with 2 lines of context.',
                                     'Use 2 lines of context for showing differences between facebook.txt and twitter.txt .',
                                     'Showing 2 lines of context, display differences between facebook.txt and twitter.txt files.']}, ignore_index = True)

#63
diff = diff.append({'Command':      'diff -U 2 facebook.txt twitter.txt',
                    'NL Queries':   ['Show the difference between facebook.txt and twitter.txt in unified format with 2 lines of unified context.',
                                     'Use 2 lines of unified context for showing differences between facebook.txt and twitter.txt .',
                                     'Showing 2 lines of unified context, display differences between facebook.txt and twitter.txt files.']}, ignore_index = True)

#64
diff = diff.append({'Command':      'diff -wc goku.txt vegeta.txt',
                    'NL Queries':   ['Output the differences between goku.txt and vegeta.txt files ignoring white spaces, in context format.',
                                     'Not considering white spaces, display differences between goku.txt and vegeta.txt in context form.',
                                     'Without taking white space into account, show distinctions between goku.txt and vegeta.txt , with lines of context around change.']}, ignore_index = True)

#65
diff = diff.append({'Command':      'diff -wu goku.txt vegeta.txt',
                    'NL Queries':   ['Output the differences between goku.txt and vegeta.txt files ignoring white spaces, in unified format.',
                                     'Not considering white spaces, display differences between goku.txt and vegeta.txt in unified context form.',
                                     'Without taking white space into account, show distinctions between goku.txt and vegeta.txt , with lines of unified context around change.']}, ignore_index = True)

#66
diff = diff.append({'Command':      'diff -wy goku.txt vegeta.txt',
                    'NL Queries':   ['Output the differences between goku.txt and vegeta.txt files ignoring white spaces, in side by side format.',
                                     'Not considering white spaces, display differences between goku.txt and vegeta.txt in side by side form.',
                                     'Without taking white space into account, show distinctions between goku.txt and vegeta.txt , placing them next to each other.']}, ignore_index = True)

#67
diff = diff.append({'Command':      'diff -Zc goku.txt vegeta.txt',
                    'NL Queries':   ['Output the differences between goku.txt and vegeta.txt files ignoring trailing white spaces, in context format.',
                                     'Not considering trailing white spaces, display differences between goku.txt and vegeta.txt in context form.',
                                     'Without taking ending white space into account, show distinctions between goku.txt and vegeta.txt , with lines of context around change.']}, ignore_index = True)

#68
diff = diff.append({'Command':      'diff -Zu goku.txt vegeta.txt',
                    'NL Queries':   ['Output the differences between goku.txt and vegeta.txt files ignoring trailing white spaces, in unified format.',
                                     'Not considering white spaces at the end of lines, display differences between goku.txt and vegeta.txt in unified context form.',
                                     'Without taking trailing white spaces into account, show distinctions between goku.txt and vegeta.txt , with lines of unified context around change.']}, ignore_index = True)

#69
diff = diff.append({'Command':      'diff -Zy goku.txt vegeta.txt',
                    'NL Queries':   ['Output the differences between goku.txt and vegeta.txt files ignoring trailing white spaces, in side by side format.',
                                     'Not considering white spaces at line endings, display differences between goku.txt and vegeta.txt in side by side form.',
                                     'Without taking ending white spaces into account, show distinctions between goku.txt and vegeta.txt , placing them next to each other.']}, ignore_index = True)

#70
diff = diff.append({'Command':      'diff --strip-trailing-cr -y naruto.txt sasuke.txt',
                    'NL Queries':   ['Output the differences between naruto.txt file and sasuke.txt file in side by side format. Before comparing the lines remove the trailing carriage return.',
                                     'After removing trailing carriage returns, compare naruto.txt and sasuke.txt side by side.',
                                     'How to compare naruto.txt and sasuke.txt side by side after removing trailing carriage returns.']}, ignore_index = True)

#71
diff = diff.append({'Command':      'diff --strip-trailing-cr -u naruto.txt sasuke.txt',
                    'NL Queries':   ['Output the differences between naruto.txt file and sasuke.txt file in unified format. Before comparing the lines remove the trailing carriage return.',
                                     'Remove the ending carriage returns from the files and then compare naruto.txt and sasuke.txt files. Display the differernces in unified format.',
                                     'Show lines which differ in files, naruto.txt and sasuke.txt in unified format. Before checking remove trailing carriage returns.']}, ignore_index = True)

#72
diff = diff.append({'Command':      'diff --strip-trailing-cr -c naruto.txt sasuke.txt',
                    'NL Queries':   ['Output the differences between naruto.txt file and sasuke.txt file in context format. Before comparing the lines remove the trailing carriage return.',
                                     'How do the data in naruto.txt and sasuke.txt differ? Show in context format and do not consider trailing carriage returns.',
                                     'Show differences between naruto.txt and sasuke.txt . Show some lines around the differences for reference. Compare after removing trailing cr.']}, ignore_index = True)

#73
diff = diff.append({'Command':      'diff -u --speed-large-files Big.txt Data.txt',
                    'NL Queries':   ['Show the differences between two large files Big.txt and Data.txt in unified format.',
                                     'In compact context form, show differences between Big.txt and Data.txt files. Use hueristics to speed up comparison.',
                                     'Show output for patching Big.txt into Data.txt and speed up the process.']}, ignore_index = True)

#74
diff = diff.append({'Command':      'diff -y --speed-large-files Big.txt Data.txt',
                    'NL Queries':   ['Show the differences between two large files Big.txt and Data.txt in side by side format.',
                                     'Show the files, Big.txt and Data.txt next to each other and highlight different lines. Accelerate the process.',
                                     'Highlight the differences between Big.txt and Data.txt placing them side by side and perform this as quickly as possible.']}, ignore_index = True)

#75
diff = diff.append({'Command':      'diff -c --speed-large-files Big.txt Data.txt',
                    'NL Queries':   ['Show the differences between two large files Big.txt and Data.txt in context format.',
                                     'Quickly show the differing lines of Big.txt and Data.txt with few lines of context around them.',
                                     'Show the differences between Big.txt and Data.txt in reference format and use hueristics to boost the process.']}, ignore_index = True)

#76
diff = diff.append({'Command':      'diff -e undo.txt redo.txt',
                    'NL Queries':   ['Output the forward ed script that shows the difference between undo.txt and redo.txt files.',
                                     'How to create an ed script which changes undo.txt to redo.txt ?',
                                     'Display the ed script which can change undo.txt to redo.txt .',
                                     'Output an ed script which can convert undo.txt to redo.txt .']}, ignore_index = True)

#77
diff = diff.append({'Command':      'diff -d long.txt file.txt',
                    'NL Queries':   ['Output minimal differences between long.txt and file.txt files.',
                                     'Show minimum amount of difference between long.txt and file.txt .',
                                     'Differentiate between long.txt and file.txt . Show minimum lines in which they differ.',
                                     'How to find minimum differences between long.txt and file.txt ?']}, ignore_index = True)

#78
diff = diff.append({'Command':      'diff -du long.txt file.txt',
                    'NL Queries':   ['Output minimal differences between long.txt and file.txt files in unified format.',
                                     'Create a file for patching long.txt to file.txt with minimum differences to be changed.',
                                     'How to create a patchfile for file.txt from long.txt with minimum changes to be covered?']}, ignore_index = True)

#79
diff = diff.append({'Command':      'diff -dy long.txt file.txt',
                    'NL Queries':   ['Output minimal differences between long.txt and file.txt files in side by side format.',
                                     'Show the minimum differences between long.txt and file.txt placing them next to each other.',
                                     'How to compare the files long.txt and file.txt line by line and highlight minimum differences between them?']}, ignore_index = True)

#80
diff = diff.append({'Command':      'diff -dc long.txt file.txt',
                    'NL Queries':   ['Output minimal differences between long.txt and file.txt files in context format.',
                                     'Display as less as possible differences between long.txt and file.txt with lines for references around changes.',
                                     'Differentiate between long.txt and file.txt showing as less as possible differences. Also show lines around differences for reference purposes.']}, ignore_index = True)

#81
diff = diff.append({'Command':      'diff -u --color lts.txt main.txt',
                    'NL Queries':   ['Show the difference between lts.txt main.txt files in unified format using color to show context.',
                                     'Display differences between lts,txt and main.txt in unified format with color indicating context.',
                                     'Show variations between lts.txt and main.txt files with unique lines for reference around changes, combining both files as one. Use color for context.']}, ignore_index = True)

#82
diff = diff.append({'Command':      'diff -c --color lts.txt main.txt',
                    'NL Queries':   ['Show the difference between lts.txt main.txt files in context format using color to show context.',
                                     'Display the differences between lts.txt and main.txt with references surrounding the changes. Show context in color.',
                                     'How to find differing lines between lts.txt and main.txt ? Use color to show context and show some lines for reference purposes.']}, ignore_index = True)

#83
diff = diff.append({'Command':      'diff --color --palette=\'de=33\' color.txt one.txt',
                    'NL Queries':   ['Output the difference between color.txt and one.txt files with deleted lines shown in yellow color and others with their default color values.',
                                     'Use color to show differences between color.txt and one.txt files. Show deleted lines in yellow.',
                                     'Differentiate between color.txt and one.txt files. Use color to show context of change. Instead of default, show deleted lines in yellow.']}, ignore_index = True)

#84
diff = diff.append({'Command':      'diff --color --palette=\'de=33\' -u color.txt one.txt',
                    'NL Queries':   ['Output the difference in unified format between color.txt and one.txt files with deleted lines shown in yellow color and others with their default color values.',
                                     'Use color to show differences between color.txt and one.txt files in unified format. Show deleted lines in yellow.',
                                     'Differentiate between color.txt and one.txt files. Use color to show context of change. Instead of default, show deleted lines in yellow. Show the output in unified context format.']}, ignore_index = True)

#85
diff = diff.append({'Command':      'diff --color --palette=\'de=33\' -c color.txt one.txt',
                    'NL Queries':   ['Output the difference in context format between color.txt and one.txt files with deleted lines shown in yellow color and others with their default color values.',
                                     'Use color to show differences between color.txt and one.txt files with lines for reference around the change. Show deleted lines in yellow.',
                                     'Differentiate between color.txt and one.txt files. Use color to show context of change. Instead of default, show deleted lines in yellow. Also display some lines around the different lines for reference purposes.']}, ignore_index = True)

#86
diff = diff.append({'Command':      'diff --color --palette=\'de=33\' -b color.txt one.txt',
                    'NL Queries':   ['Output the difference between color.txt and one.txt files with deleted lines shown in yellow color and others with their default color values. Do not consider changes in amount of spaces as a difference.',
                                     'Show differences between color.txt and one.txt in color with deleted lines shown in yellow. Ignore the number of spaces to count as difference.',
                                     'Number of white spaces do not matter. Show the differences between color.txt and one.txt using color. Removed lines are to be shown in color value 33.']}, ignore_index = True)

#87
diff = diff.append({'Command':      'diff -ub one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in unified format. Do not distinguish lines on the basis of number of white space characters.',
                                     'In unified format, display differences between one.txt and two.txt without considering amount of blanks to be a change.',
                                     'How to differentiate between one.txt and two.txt , showing unified lines of context, without taking number of spaces as a change?']}, ignore_index = True)

#88
diff = diff.append({'Command':      'diff -yb one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in side by side format. Do not distinguish lines on the basis of number of white space characters.',
                                     'Place the contents of one.txt and two.txt and highlight the different lines. Number of blanks do not matter.',
                                     'Not considering number of blanks, show differences between one.txt and two.txt in side-by-side form.']}, ignore_index = True)

#89
diff = diff.append({'Command':      'diff -cb one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in context format. Do not distinguish lines on the basis of number of white space characters.',
                                     'In context format, display the lines of one.txt and two.txt which differ.',
                                     'Using lines for context around the change, show differences between one.txt and two.txt files.']}, ignore_index = True)

#90
diff = diff.append({'Command':      'diff -uB one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in unified format. Do not include blank lines in difference.',
                                     'Using unified lines for context, show differences between one.txt and two.txt files.',
                                     'Using context lines, show differences between one.txt and two.txt . Remove repeated lines of context.']}, ignore_index = True)

#91
diff = diff.append({'Command':      'diff -yB one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in side by side format. Do not include blank lines in difference.',
                                     'Ignoring blank lines, highlight differing lines of one.txt and two.txt placing them next to each other.',
                                     'Not considering blank line differences, show the lines which differ in one.txt and two.txt in side-by-side format.']}, ignore_index = True)

#92
diff = diff.append({'Command':      'diff -cB one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in context format. Do not include blank lines in difference.',
                                     'Ignoring blank lines, show differing lines of one.txt and two.txt with lines for context around the change.',
                                     'Not considering blank line differences, show the lines which differ in one.txt and two.txt in context format.']}, ignore_index = True)

#93
diff = diff.append({'Command':      'diff -ui one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in unified format ignoring case difference.',
                                     'Ignoring blank lines, highlight differing lines of one.txt and two.txt with unified lines for context.',
                                     'Not considering blank line differences, show the lines which differ in one.txt and two.txt in advanced context format.']}, ignore_index = True)

#94
diff = diff.append({'Command':      'diff -yiZ one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in side by side format ignoring case differences and trailing white spaces.',
                                     'Ignoring trailing white spaces and case of alphabets, show the differing lines of one.txt and two.txt showing them next to each other.',
                                     'Placing the files one.txt and two.txt next to each other, highlight differences between them. Ignore case and trailing space differences.']}, ignore_index = True)

#95
diff = diff.append({'Command':      'diff -ci one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in context format ignoring case differences.',
                                     'In context mode, display the differing lines between one.txt and two.txt files if comparison is case insensitive.',
                                     'Display the lines which differ in files one.txt and two.txt and show line of context around the change. Do not consider case differences.']}, ignore_index = True)

#96
diff = diff.append({'Command':      'diff --no-dereference emma watson',
                    'NL Queries':   ['Compare the directories emma and watson . Do not follow symlinks.',
                                     'Without following symbolic links, show differences between emma and watson .',
                                     'While displaying differences between emma and watson , do not resolve soft links.']}, ignore_index = True)

#97
diff = diff.append({'Command':      'diff -ni one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in RCS format ignoring case differences.',
                                     'Ignoring case differences, show the distinctions between one.txt and two.txt in RCS format.',
                                     'What are the differences between one.txt and two.txt contents? Output in rcs format.']}, ignore_index = True)

#98
diff = diff.append({'Command':      'diff -nB one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in RCS format. Do not include blank lines in difference.',
                                     'Without considering blank line differences, compare one.txt and two.txt and show the output in rcs format.',
                                     'Display the distinctions between one.txt and two.txt in revision control form. Do not display blank line differences.']}, ignore_index = True)

#99
diff = diff.append({'Command':      'diff -nb one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in RCS format. Do not distinguish lines on the basis of number of white space characters.',
                                     'Ignoring blank spaces, show differences between one.txt and two.txt in version control format.',
                                     'What are the differences between one.txt and two.txt if blanks are neglected? Show the result in RCS format.']}, ignore_index = True)

#100
diff = diff.append({'Command':      'diff -nt dead.txt pool.txt',
                    'NL Queries':   ['Show the differences between files dead.txt pool.txt in RCS format. In output expand TAB to spaces.',
                                     'How the files dead.txt and pool.txt differ? Show the output in revision control format and expand tabs to spaces.',
                                     'Display the distinctions between dead.txt and pool.txt files. Show the output in RCS format expanding tabs to spaces.']}, ignore_index = True)

#101
diff = diff.append({'Command':      'diff -ct dead.txt pool.txt',
                    'NL Queries':   ['Show the differences between files dead.txt pool.txt in context format. In output expand TAB to spaces.',
                                     'How to show differences between dead.txt and pool.txt in context format expanding tabs to spaces?',
                                     'Distinguish between dead.txt and pool.txt files and show lines for context around the change. Expand tabs to spaces in output.']}, ignore_index = True)

#102
diff = diff.append({'Command':      'diff -ut dead.txt pool.txt',
                    'NL Queries':   ['Show the differences between files dead.txt pool.txt in unified format. In output expand TAB to spaces.',
                                     'How to show differences between dead.txt and pool.txt in unified context format expanding tabs to spaces?',
                                     'Distinguish between dead.txt and pool.txt files and show unique lines for context around the change. Expand tabs to spaces in output.']}, ignore_index = True)

#103
diff = diff.append({'Command':      'diff -yt dead.txt pool.txt',
                    'NL Queries':   ['Show the differences between files dead.txt pool.txt in side by side format. In output expand TAB to spaces.',
                                     'How to show differences between dead.txt and pool.txt in side-by-side format expanding tabs to spaces?',
                                     'Distinguish between dead.txt and pool.txt files and compare them line by line placing them next to each other. Expand tabs to spaces in output.']}, ignore_index = True)

#104
diff = diff.append({'Command':      'diff -qE victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving TAB expansion.',
                                     'Report if the files victoria.txt and justice.txt differ. Do not consider tab expansion changes.',
                                     'Neglecting tab expansion changes, indicate if files are different. Do nothing if files are same.']}, ignore_index = True)

#105
diff = diff.append({'Command':      'diff -qb victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving amount of white spaces.',
                                     'Report if the files victoria.txt and justice.txt differ. Do not consider amount of whote space changes.',
                                     'Neglecting amount of blank space changes, indicate if files are different. Do nothing if files are same.']}, ignore_index = True)

#106
diff = diff.append({'Command':      'diff -qB victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving insertion or deletion of blank lines.',
                                     'Report if the files victoria.txt and justice.txt differ. Do not blank line changes.',
                                     'Neglecting changes due to empty lines, indicate if files are different. Do nothing if files are same.']}, ignore_index = True)

#107
diff = diff.append({'Command':      'diff -qw victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving white spaces.',
                                     'Report if the files victoria.txt and justice.txt differ. Do not consider white space changes.',
                                     'Neglecting white space changes, indicate if files are different. Do nothing if files are same.']}, ignore_index = True)

#108
diff = diff.append({'Command':      'diff -qZ victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving trailing white spaces.',
                                     'Report if the files victoria.txt and justice.txt differ. Do not consider ending blank space changes.',
                                     'Neglecting blank space at the end of line changes, indicate if files are different. Do nothing if files are same.']}, ignore_index = True)

#109
diff = diff.append({'Command':      'diff -ya victoria bonya',
                    'NL Queries':   ['Find the differences between victoria and bonya in side by side format and treat them as text files.',
                                     'Compare victoria and bonya next to each other as if they are text files and highlight differong lines.',
                                     'Show the differences between victoria and bonya treating them as text. Place them side by side and show differences.']}, ignore_index = True)

#110
diff = diff.append({'Command':      'diff -y --binary victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt files in side by side format and read-write in binary mode.',
                                     'Compare victoria.txt and bonya.txt next to each other and highlight differong lines. R/W in binary mode.',
                                     'Show the differences between victoria.txt and bonya.txt . Place them side by side and show differences. Output in binary mode.']}, ignore_index = True)

#111
diff = diff.append({'Command':      'diff -yE victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in side by side format and ignore changes due to tab expansion.',
                                     'Compare victoria.txt and bonya.txt files line by line next to each other and highlight different lines. Do not highlight changes due to tab expansion.',
                                     'Not including changes due to tab expansion, show differences between victoria.txt and bonya.txt files in side by side format.']}, ignore_index = True)

#112
diff = diff.append({'Command':      'diff -y --from-file=model.txt victoria bonya',
                    'NL Queries':   ['Find how the files model.txt in victoria and bonya directories differ from model.txt in current directory in side by side format.',
                                     'Compare model.txt in victoria and bonya directories from model.txt file in side by side format.',
                                     'Highlight differing lines of model.txt in victoria and bonya from model.txt in current directory placing them next to each other.']}, ignore_index = True)

#113
diff = diff.append({'Command':      'diff -yI \'[0-9]\' victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in side by side format and ignore changes due to regex \'[0-9]\' .',
                                     'Ignore all changes involving numerals and highlight the differences between victoria.txt and bonya.txt placing them next to each other.',
                                     'Distinguish between victoria.txt and bonya.txt in side by side format excluding the changes which include numbers in side by side format.']}, ignore_index = True)

#114
diff = diff.append({'Command':      'diff -yl victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in side by side format and paginate the output.',
                                     'Show the distinctions between victoria.txt and bonya.txt showing them side by side and highlighting the differing lines. Format the output for printout.',
                                     'How to paginate the differences between victoria.txt and bonya.txt files? Output should be in the form such that lines from both the files are placed correspondingly and differing lines are marked.']}, ignore_index = True)

#115
diff = diff.append({'Command':      'diff -yN victoria.txt bonya.txt',
                    'NL Queries':   ['Show the differences between the files victoria.txt and bonya.txt in side by side format. Treat the file as empty if it is not present.',
                                     'Treating empty files as absent, show differences between victoria.txt and bonya.txt side by side.',
                                     'How to differentiate between victoria.txt and bonya.txt files in side by side format? Non existent file should be treated as empty.']}, ignore_index = True)

#116
diff = diff.append({'Command':      'diff -yr mad grace',
                    'NL Queries':   ['Output the difference between directories mad and grace in side by side format recursively.',
                                     'Recursively compare mad grace directories in side by side format.',
                                     'Show distinctions between mad and grace directories in side by side form. Also compare subdirectories for differences.']}, ignore_index = True)

#117
diff = diff.append({'Command':      'diff -yS holla.txt UK Switz',
                    'NL Queries':   ['Show the differences between directories UK and Switz in side by side format and start comparing from file holla.txt .',
                                     'In side by side format, show distinctions between UK and Switz directory. Start comparing from holla.txt file.',
                                     'Starting from holla.txt, compare UK and Switz by placing the contents of files next to each other.']}, ignore_index = True)

#118
diff = diff.append({'Command':      'diff -cT UK.txt US.txt',
                    'NL Queries':   ['Show the difference between files UK.txt and US.txt and append a leading TAB to the output lines in context format.',
                                     'Display the distinctions between UK.txt and US.txt files in context mode. Prepend a tab to each output line.',
                                     'Prepending a tab character to each output line, show the differences between US.txt and UK.txt files in context format.']}, ignore_index = True)

#119
diff = diff.append({'Command':      'diff -y --to-file=currency.txt US UK IND',
                    'NL Queries':   ['Output the differences between the file currency.txt in directories US , UK and IND to currency.txt in current directory in side by side format.',
                                     'In side by side format, show differences between currency.txt file in US , UK , IND directories to current.txt in pwd.',
                                     'Placing the contents of files next to each other, compare currency.txt in US, UK, IND folders to currency.txt in current folder.']}, ignore_index = True)

#120
diff = diff.append({'Command':      'diff -yx \'*.cpp\' US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in side by side format. Do not compare files or directories whose names end with .cpp .',
                                     'Except .cpp files, compare the directories US and Russia inn side by side format.',
                                     'How to compare US and Russia folders in side by side form? Do not compare files ending with .cpp .']}, ignore_index = True)

#121
diff = diff.append({'Command':      'diff -yX exc.txt US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in side by side format. Do not compare files or directories whose names match with the pattern mentioned in file exc.txt .',
                                     'Except file name patterns matching with those in exc.txt file, compare each file of directory US and Russia using side by side format.',
                                     'Compare the directories US and Russia in side by side format. Do not compare files mentioned in exc.txt .']}, ignore_index = True)

#122
diff = diff.append({'Command':      'diff -na a.out b.out',
                    'NL Queries':   ['Show the differences between a.out and b.out treating them as text files in RCS format.',
                                     'Compare files a.out and b.out as if they were text files. Show the distinctions in version control format.',
                                     'Using revision control format, show the differing lines of a.out and b.out .']}, ignore_index = True)
#123
diff = diff.append({'Command':      'diff -nd aa.txt bb.txt',
                    'NL Queries':   ['Show minimal differences between files aa.txt and bb.txt in RCS format.',
                                     'What are the differing lines in aa.txt and bb.txt ? Show the output in RCS format and find minimal differences.',
                                     'Display the lines in aa.txt which differ from corresponding line in bb.txt . Show minimal difference in revision control format.']}, ignore_index = True)

#124
diff = diff.append({'Command':      'diff -nE one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in RCS format. Ignore any changes due to tab expansion.',
                                     'Compare victoria.txt and bonya.txt files line by line in revision control format. Do not highlight changes due to tab expansion.',
                                     'Not including changes due to tab expansion, show differences between victoria.txt and bonya.txt files in rcs format.']}, ignore_index = True)

#125
diff = diff.append({'Command':      'diff -n --from-file=currency.txt US UK',
                    'NL Queries':   ['Show the lines where US/currency.txt and UK/currency.txt differ from currency.txt in current directory in RCS format.',
                                     'Compare model.txt in victoria and bonya directories from model.txt file in rcs format.',
                                     'Highlight differing lines of model.txt in victoria and bonya from model.txt in current directory i revision control form.']}, ignore_index = True)

#126
diff = diff.append({'Command':      'diff -nI \'[0-9]\' victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in RCS format and ignore changes due to regex \'[0-9]\' .',
                                     'Ignore all changes involving numerals and highlight the differences between victoria.txt and bonya.txt in version control form.',
                                     'Distinguish between victoria.txt and bonya.txt in side by side format excluding the changes which include numbers in rcs format.']}, ignore_index = True)

#127
diff = diff.append({'Command':      'diff -nl victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in RCS format and paginate the output.',
                                     'Show the distinctions between victoria.txt and bonya.txt showing them in revision control. Format the output for printout.',
                                     'How to paginate the differences between victoria.txt and bonya.txt files? Output should be in the form such that lines from both the files are placed correspondingly and differing lines are marked.']}, ignore_index = True)

#128
diff = diff.append({'Command':      'diff -nN victoria.txt bonya.txt',
                    'NL Queries':   ['Show the differences between the files victoria.txt and bonya.txt in RCS format. Treat the file as empty if it is not present.',
                                     'Treating the absent files as empty, display the differences between victoria.txt and bonya.txt files in revision control format.',
                                     'Showing differences as in revision control, distinguish between victoria.txt and bonya.txt files. Consider non existent files as absent.']}, ignore_index = True)

#129
diff = diff.append({'Command':      'diff -nS model.txt mad grace',
                    'NL Queries':   ['Output the difference between directories mad and grace in RCS format. Start from file named model.txt .',
                                     'Starting from the file named model.txt , compare the directories mad and grace in RCS format.',
                                     'Show the distinctions between mad and grace directories. Begin comparing from model.txt file.']}, ignore_index = True)

#130
diff = diff.append({'Command':      'diff -nx \'*.cpp\' US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in RCS format. Do not compare files or directories whose names end with .cpp .',
                                     'Excluding .cpp files in directories, compare US and Russia directories and show the differences in RCS mode.',
                                     'Compare the directories US and Russia and output the difference in revision control format. Do not compare files whose names end with .cpp .']}, ignore_index = True)

#131
diff = diff.append({'Command':      'diff -nX exc.txt US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in RCS format. Do not compare files or directories whose names end match with the pattern mentioned in file exc.txt .',
                                     'Compare US and Russia directories. Show the output in RCS mode. Do not compare the files whose names match with patterns mentioned in exc.txt .',
                                     'Show differences between US and Russia directories in Revision Control mode. Do not consider differences of files which match with patterns stated in exc.txt file.']}, ignore_index = True)

#132
diff = diff.append({'Command':      'diff -nw abc.txt xyz.txt',
                    'NL Queries':   ['Show the differences between abc.txt and xyz.txt in RCS format and ignore the differences involving white spaces.',
                                     'Not considering white spaces, display differences between goku.txt and vegeta.txt in RCS form.',
                                     'Without taking white space into account, show distinctions between goku.txt and vegeta.txt in version control mode.']}, ignore_index = True)

#133
diff = diff.append({'Command':      'diff -ca tic.txt tac.txt',
                    'NL Queries':   ['Show the differences between tic.txt and tac.txt files in context format treating them as text files. ',
                                     'Distinguish between tic.txt and tac.txt text files. Show lines of context around the change.',
                                     'Show distinctions between tic.txt and tac.txt files as if they were text files. Show lines around the differences for reference purposes.']}, ignore_index = True)

#134
diff = diff.append({'Command':      'diff -c --binary tic.txt tac.txt',
                    'NL Queries':   ['Show the differences between the files tic.txt and tac.txt in context format. Read and write in binary mode.',
                                     'Perform IO in binary mode. Show the differences between tic.txt and tac.txt files in context mode.',
                                     'Using context mode of displaying the differences, show distinctions between tic.txt and tac.txt files. Write and read in binary mode.']}, ignore_index = True)

#135
diff = diff.append({'Command':      'diff -cE tic.txt tac.txt',
                    'NL Queries':   ['Show the differences between tic.txt and tac.txt files in context mode and ignore changes due to tab expansion.',
                                     'Not taking changes occuring due to tab expansion into account, show differences between tic.txt and tac.txt files in context format.',
                                     'How to find differences between tic.txt and tac.txt files with lines of context around the change? Do not consider tab expansion changes as a difference.']}, ignore_index = True)

#136
diff = diff.append({'Command':      'diff -c --from-file=currency.txt US UK',
                    'NL Queries':   ['Show the lines where US/currency.txt and UK/currency.txt differ from currency.txt in current directory in context format.',
                                     'Compare US/currency.txt and UK/currency.txt from ./currency.txt in context mode.',
                                     'Showing the distinctions in context mode, compare currency.txt in US and UK folders to currency.txt in current folder.']}, ignore_index = True)

#137
diff = diff.append({'Command':      'diff -cI \'[0-9]\' victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in context format and ignore changes due to regex \'[0-9]\' .',
                                     'Ignore all changes involving numerals and highlight the differences between victoria.txt and bonya.txt in context mode.',
                                     'Distinguish between victoria.txt and bonya.txt in side by side format excluding the changes which include numbers with few lines of context around the differences.']}, ignore_index = True)

#138
diff = diff.append({'Command':      'diff -cl victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in context format and paginate the output.',
                                     'Show the distinctions between victoria.txt and bonya.txt showing the differing lines with some reference lines. Format the output for printout.',
                                     'How to paginate the differences between victoria.txt and bonya.txt files? Output should be in the context form.']}, ignore_index = True)

#139
diff = diff.append({'Command':      'diff -cN victoria.txt bonya.txt',
                    'NL Queries':   ['Show the differences between the files victoria.txt and bonya.txt in context format. Treat the file as empty if it is not present.',
                                     'Absent files should be treated as empty. Show the distinctions between victoria.txt and boya.txt files in context mode.',
                                     'Using lines of context for referring to changes, show differences between victoria.txt and bonya.txt files.']}, ignore_index = True)

#140
diff = diff.append({'Command':      'diff -cS model.txt mad grace',
                    'NL Queries':   ['Output the difference between directories mad and grace in context format. Start from file named model.txt .',
                                     'Beginning from model.txt file compare mad and grace directories. Show the differences in context mode.',
                                     'Start comparing the folders named mad and grace from model.txt onwards. Output the distinctions in context format.']}, ignore_index = True)

#141
diff = diff.append({'Command':      'diff -cx \'*.cpp\' US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in context format. Do not compare files or sub-directories whose names end with .cpp .',
                                     'Show the distinctions between US and Russia folders in context mode. Do not compare .cpp files.',
                                     'Without considering files with names ending with .cpp , compare US and Russia in context mode.']}, ignore_index = True)

#142
diff = diff.append({'Command':      'diff -cX exc.txt US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in context format. Do not compare files or directories whose names end match with the pattern mentioned in file exc.txt .',
                                     'Excluding the file names which match with patterns mentioned in exc.txt , distinguish between US and Russia in context mode.',
                                     'How to show differences between US and Russia directories with context lines around the change? Ignore files whose names match with the patterns stated in exc.txt file.']}, ignore_index = True)

#143
diff = diff.append({'Command':      'diff -c --to-file=currency.txt US UK IND',
                    'NL Queries':   ['Output the differences between the file currency.txt in directories US , UK and IND to currency.txt in current directory in context format.',
                                     'Compare US/currency.txt , UK/currency.txt , IND/currency.txt to ./currency.txt . Show lines around the change for reference purposes.',
                                     'Compare currency.txt in US , UK and IND folders to that in current folder. Show the output in context mode.']}, ignore_index = True)

#144
diff = diff.append({'Command':      'diff -c --suppress-blank-empty tt.txt txt.txt',
                    'NL Queries':   ['Show the differences between tt.txt and txt.txt files in context mode. Suppress any blanks before newlines when printing the representation of an empty line.',
                                     'Compare tt.txt and txt.txt files. Show the result in context form. Do not output any white space in empty lines.',
                                     'Distinguish between tt.txt and txt.txt files in context mode and remove any space in empty line representation.']}, ignore_index = True)

#145
diff = diff.append({'Command':      'diff -ua a.out b.out',
                    'NL Queries':   ['Show the differences between a.out and b.out treating them as text files in unified format.',
                                     'Distinguish between tic.txt and tac.txt text files. Show unified lines of context around the change.',
                                     'Show distinctions between tic.txt and tac.txt files as if they were text files. Show unique lines around the differences for reference purposes.']}, ignore_index = True)

#146
diff = diff.append({'Command':      'diff -uS model.txt mad grace',
                    'NL Queries':   ['Output the difference between directories mad and grace in unified format. Start from file named model.txt .',
                                     'Beginning from model.txt file compare mad and grace directories. Show the differences in unified context mode.',
                                     'Start comparing the folders named mad and grace from model.txt onwards. Output the distinctions in unified format.']}, ignore_index = True)

#147
diff = diff.append({'Command':      'diff -uE one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in unified format. Ignore any changes due to tab expansion.',
                                     'Not taking changes occuring due to tab expansion into account, show differences between tic.txt and tac.txt files in unified context format.',
                                     'How to find differences between tic.txt and tac.txt files with unique lines of context around the change? Do not consider tab expansion changes as a difference.']}, ignore_index = True)

#148
diff = diff.append({'Command':      'diff -u --from-file=currency.txt US UK',
                    'NL Queries':   ['Show the lines where US/currency.txt and UK/currency.txt differ from currency.txt in current directory in unified format.',
                                     'Compare US/currency.txt and UK/currency.txt from ./currency.txt in unified context mode.',
                                     'Showing the distinctions in unified mode, compare currency.txt in US and UK folders to currency.txt in current folder.']}, ignore_index = True)

#149
diff = diff.append({'Command':      'diff -uI \'[0-9]\' victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in unified format and ignore changes due to regex \'[0-9]\' .',
                                     'Ignore all changes involving numerals and highlight the differences between victoria.txt and bonya.txt in unified context mode.',
                                     'Distinguish between victoria.txt and bonya.txt in side by side format excluding the changes which include numbers with few lines of context around the differences. Show only unique context lines.']}, ignore_index = True)

#150
diff = diff.append({'Command':      'diff -ul victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in unified format and paginate the output.',
                                     'Show the distinctions between victoria.txt and bonya.txt showing the differing lines with some reference lines. Format the output for printout. Show only unique lines of reference.',
                                     'How to paginate the differences between victoria.txt and bonya.txt files? Output should be in the unified context form.']}, ignore_index = True)

#151
diff = diff.append({'Command':      'diff -uN victoria.txt bonya.txt',
                    'NL Queries':   ['Show the differences between the files victoria.txt and bonya.txt in unified format. Treat the file as empty if it is not present.',
                                     'Absent files should be treated as empty. Show the distinctions between victoria.txt and boya.txt files in unique context mode.',
                                     'Using unnified lines of context for referring to changes, show differences between victoria.txt and bonya.txt files.']}, ignore_index = True)

#152
diff = diff.append({'Command':      'diff -ux \'*.cpp\' US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in unified format. Do not compare files or directories whose names end with .cpp .',
                                     'Show the distinctions between US and Russia folders in unified mode. Do not compare .cpp files.',
                                     'Without considering files with names ending with .cpp , compare US and Russia in unified mode.']}, ignore_index = True)

#153
diff = diff.append({'Command':      'diff -uX exc.txt US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in unified format. Do not compare files or directories whose names end match with the pattern mentioned in file exc.txt .',
                                     'Excluding the file names which match with patterns mentioned in exc.txt , distinguish between US and Russia in unified mode.',
                                     'How to show differences between US and Russia directories with unique context lines around the change? Ignore files whose names match with the patterns stated in exc.txt file.']}, ignore_index = True)

#154
diff = diff.append({'Command':      'diff -u --to-file=currency.txt US UK IND',
                    'NL Queries':   ['Output the differences between the file currency.txt in directories US , UK and IND to currency.txt in current directory in unified format.',
                                     'Compare US/currency.txt , UK/currency.txt , IND/currency.txt to ./currency.txt . Show unique lines around the change for reference purposes.',
                                     'Compare currency.txt in US , UK and IND folders to that in current folder. Show the output in unified mode.']}, ignore_index = True)

#155
diff = diff.append({'Command':      'diff -u --suppress-blank-empty tt.txt txt.txt',
                    'NL Queries':   ['Show the differences between tt.txt and txt.txt files in unified mode. Suppress any blanks before newlines when printing the representation of an empty line.',
                                     'Compare tt.txt and txt.txt files. Show the result in unified form. Do not output any white space in empty lines.',
                                     'Distinguish between tt.txt and txt.txt files in unique context mode and remove any space in empty line representation.']}, ignore_index = True)

#156
diff = diff.append({'Command':     'diff -uZ aa.txt AA.txt',
                    'NL Queries':  ['Show the differences in files aa.txt and AA.txt in unified format not involving trailing white space differences.',
                                    'Do not consider trailing white space differences in comparing aa.txt and AA.tt files. Output the differences in unified format.',
                                    'Display the distinctions between aa.txt and AA.txt files in unified context format ignoring trailing white space differences.']}, ignore_index = True)

#157
diff = diff.append({'Command':     'diff -bB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change.',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files.']}, ignore_index = True)

#158
diff = diff.append({'Command':     'diff -ubB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in unified format.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change. Show the output in unified format.',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files and display the result in unique context format.']}, ignore_index = True)

#159
diff = diff.append({'Command':     'diff -cbB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in context format.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change. Show lines of context around the change.',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files. Show the output in context mode.']}, ignore_index = True)

#160
diff = diff.append({'Command':     'diff -ybB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in side by side format.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change. Display the output in side-by-side mode.',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files. Output the differences in side-by-side format.']}, ignore_index = True)

#161
diff = diff.append({'Command':     'diff -nbB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in RCS format.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change. Show the differences in RCS format.',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files. Display the differences in revision control form.']}, ignore_index = True)

#162
diff = diff.append({'Command':     'diff -dbB abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change. Output minimal differences.',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files. Show minimum amount of changes.']}, ignore_index = True)

#163
diff = diff.append({'Command':     'diff -ubBd abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in unified format.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change. Output minimal differences in unified context form.',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files. Show minimum amount of changes in unified mode.']}, ignore_index = True)

#164
diff = diff.append({'Command':     'diff -cdbB abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in context format.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change. Output minimal differences in unified mode.',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files. Show minimum amount of changes in unified context mode.']}, ignore_index = True)

#165
diff = diff.append({'Command':     'diff -ybBd abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in side by side format.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change. Output minimal differences in side-by-side format.',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files. Show minimum amount of changes showing the files next to each other.']}, ignore_index = True)

#166
diff = diff.append({'Command':     'diff -nbBd abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in RCS format.',
                                    'Distinguish between abc.txt and xyz.txt files. Do not include empty lines and quantity of spaces as change. Output minimal differences in RCS format..',
                                    'Ignoring empty lines and amount of space as a change, distinguish between abc.txt and xyz.txt files. Show minimum amount of changes in version control format.']}, ignore_index = True)

#167
diff = diff.append({'Command':     'diff -bBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes , tab expansion changes and amount of white space.',
                                    'Output the differences between abc.txt and xyz.txt files. Exclude empty lines, tab expansion and amount of white spaces as change.',
                                    'Distinguish between abc.txt and xyz.txt files without considering blank linnes and amount of spaces as change. Also ignore TAB expansion changes.']}, ignore_index = True)

#168
diff = diff.append({'Command':     'diff -ubBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in unified format.',
                                    'Output the differences between abc.txt and xyz.txt files. Exclude empty lines, tab expansion and amount of white spaces as change. Output should be in unified context format.',
                                    'Distinguish between abc.txt and xyz.txt files without considering blank linnes and amount of spaces as change. Also ignore TAB expansion changes. Display the result in unified format.']}, ignore_index = True)

#169
diff = diff.append({'Command':     'diff -cbBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in context format.',
                                    'Output the differences between abc.txt and xyz.txt files. Exclude empty lines, tab expansion and amount of white spaces as change. Show the lines around differing lines for reference.',
                                    'Distinguish between abc.txt and xyz.txt files without considering blank linnes and amount of spaces as change. Also ignore TAB expansion changes. Display context lines around changes.']}, ignore_index = True)

#170
diff = diff.append({'Command':     'diff -ybBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in side by side format.',
                                    'Output the differences between abc.txt and xyz.txt files. Exclude empty lines, tab expansion and amount of white spaces as change. Output should be in side by side mode.',
                                    'Distinguish between abc.txt and xyz.txt files without considering blank linnes and amount of spaces as change. Also ignore TAB expansion changes. Show the output in side by side format.']}, ignore_index = True)

#171
diff = diff.append({'Command':     'diff -nbBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in RCS format.',
                                    'Output the differences between abc.txt and xyz.txt files. Exclude empty lines, tab expansion and amount of white spaces as change. Output difference should be in rcs format.',
                                    'Distinguish between abc.txt and xyz.txt files without considering blank linnes and amount of spaces as change. Also ignore TAB expansion changes. Display the differences in rcs format.']}, ignore_index = True)

#172
diff = diff.append({'Command':     'diff -bBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space. Paginate the output.',
                                    'Paginate the distinctions between abc.txt and xyz.txt files. Do not include empty line and white space amount in difference.',
                                    'Show the distinctions between the contents of abc.txt and xyz.txt files. Empty lines and changes in white space should not be treated as difference. Paginate the final result.']}, ignore_index = True)

#173
diff = diff.append({'Command':     'diff -ubBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in unified format. Paginate the output.',
                                    'Paginate the distinctions between abc.txt and xyz.txt files. Do not include empty line and white space amount in difference. Output should be in unified format.',
                                    'Show the distinctions between the contents of abc.txt and xyz.txt files. Empty lines and changes in white space should not be treated as difference. Paginate the unified mode output.']}, ignore_index = True)

#174
diff = diff.append({'Command':     'diff -cbBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in context format. Paginate the output.',
                                    'Paginate the distinctions between abc.txt and xyz.txt files. Do not include empty line and white space amount in difference. Display the differences in context mode.',
                                    'Show the distinctions between the contents of abc.txt and xyz.txt files. Empty lines and changes in white space should not be treated as difference. Show lines of context around the change and paginate the result.']}, ignore_index = True)

#175
diff = diff.append({'Command':     'diff -ybBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in side by side format. Paginate the output.',
                                    'Paginate the distinctions between abc.txt and xyz.txt files. Do not include empty line and white space amount in difference. Show the contents of files next to each other and highlight different lines.',
                                    'Show the distinctions between the contents of abc.txt and xyz.txt files. Empty lines and changes in white space should not be treated as difference. Paginate the side by side difference format output shown.']}, ignore_index = True)

#176
diff = diff.append({'Command':     'diff -nbBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in RCS format. Paginate the output.',
                                    'Paginate the distinctions between abc.txt and xyz.txt files. Do not include empty line and white space amount in difference. Use revision control format for showing the output.',
                                    'Show the distinctions between the contents of abc.txt and xyz.txt files. Empty lines and changes in white space should not be treated as difference. Paginate the final output generated by showing the differences in RCS format.']}, ignore_index = True)

#177
diff = diff.append({'Command':     'diff -dbBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space. Paginate the output.',
                                    'Distinguish between abc.txt and xyz.txt files showing minimum differences. Ignore changes due to blank lines and amount of white spaces. Show the paginated output.',
                                    'Show differences between abc.txt and xyz.txt . Show only minimal differences not considering empty lines and quantity of white spaces. Final output should be paginated.']}, ignore_index = True)

#178
diff = diff.append({'Command':     'diff -ubBdl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in unified format. Paginate the output.',
                                    'Distinguish between abc.txt and xyz.txt files showing minimum differences. Ignore changes due to blank lines and amount of white spaces. Show the output in unified format and paginate it.',
                                    'Show differences between abc.txt and xyz.txt in unified context format. Show only minimal differences not considering empty lines and quantity of white spaces. Final output should be paginated.']}, ignore_index = True)

#179
diff = diff.append({'Command':     'diff -cdbBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in context format. Paginate the output.',
                                    'Distinguish between abc.txt and xyz.txt files showing minimum differences. Ignore changes due to blank lines and amount of white spaces. Show the output in context format and paginate it.',
                                    'Show differences between abc.txt and xyz.txt in context mode. Show only minimal differences not considering empty lines and quantity of white spaces. Final output should be paginated.']}, ignore_index = True)

#180
diff = diff.append({'Command':     'diff -ybBdl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in side by side format. Paginate the output.',
                                    'Distinguish between abc.txt and xyz.txt files showing minimum differences. Ignore changes due to blank lines and amount of white spaces. Show the output in side-by-side format and paginate it.',
                                    'Show differences between abc.txt and xyz.txt in side by side format. Show only minimal differences not considering empty lines and quantity of white spaces. Final output should be paginated.']}, ignore_index = True)

#181
diff = diff.append({'Command':     'diff -nbBdl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in RCS format. Paginate the output.',
                                    'Distinguish between abc.txt and xyz.txt files showing minimum differences. Ignore changes due to blank lines and amount of white spaces. Show the output in revision control format and paginate it.',
                                    'Show differences between abc.txt and xyz.txt in rcs format. Show only minimal differences not considering empty lines and quantity of white spaces. Final output should be paginated.']}, ignore_index = True)

#182
diff = diff.append({'Command':     'diff -bBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes , tab expansion changes and amount of white space. Paginate the output.',
                                    'Paginate the difference between abc.txt and xyz.txt files. While comparing ignore blank line, tab expansion and amount of white space changes. Show the output.',
                                    'Display the distinctions between abc.txt and xyz.txt files. Do not consider tab expansion, amount of spaces and blank lines as changes. Finally, paginate the output.']}, ignore_index = True)

#183
diff = diff.append({'Command':     'diff -ubBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in unified format. Paginate the output.',
                                    'Paginate the difference between abc.txt and xyz.txt files. While comparing ignore blank line, tab expansion and amount of white space changes. Show the output in unified format.',
                                    'Display the distinctions between abc.txt and xyz.txt in unified context format. Do not consider tab expansion, amount of spaces and blank lines as changes. Finally, paginate the output.']}, ignore_index = True)

#184
diff = diff.append({'Command':     'diff -cbBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in context format. Paginate the output.',
                                    'Paginate the difference between abc.txt and xyz.txt files. While comparing ignore blank line, tab expansion and amount of white space changes. Show the output in context format.',
                                    'Display the distinctions between abc.txt and xyz.txt in reference format. Do not consider tab expansion, amount of spaces and blank lines as changes. Finally, paginate the output.']}, ignore_index = True)

#185
diff = diff.append({'Command':     'diff -ybBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in side by side format. Paginate the output.',
                                    'Paginate the difference between abc.txt and xyz.txt files. While comparing ignore blank line, tab expansion and amount of white space changes. Show the output in side by side format.',
                                    'Display the distinctions between abc.txt and xyz.txt in side-by-side format. Do not consider tab expansion, amount of spaces and blank lines as changes. Finally, paginate the output.']}, ignore_index = True)

#186
diff = diff.append({'Command':     'diff -nbBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in RCS format. Paginate the output.',
                                    'Paginate the difference between abc.txt and xyz.txt files. While comparing ignore blank line, tab expansion and amount of white space changes. Show the output in rcs format.',
                                    'Display the distinctions between abc.txt and xyz.txt in revision control format. Do not consider tab expansion, amount of spaces and blank lines as changes. Finally, paginate the output.']}, ignore_index = True)

#187
diff = diff.append({'Command':     'diff --ignore-file-name-case -ru kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in unified format.',
                                    'Recursively compare kate and upton. Show the difference output in unified context format. While comparing treat upper and lowercase alphabets in name as identical.',
                                    'Names should be considered case insensitive and compare kate and upton recursively showing the output in unified context mode.']}, ignore_index = True)

#188
diff = diff.append({'Command':     'diff --ignore-file-name-case -ry kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in side by side format.',
                                    'Recursively compare kate and upton. Show the difference output in side-by-side format. While comparing treat upper and lowercase alphabets in name as identical.',
                                    'Names should be considered case insensitive and compare kate and upton recursively in side by side mode.']}, ignore_index = True)

#189
diff = diff.append({'Command':     'diff --ignore-file-name-case -rc kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in context format.',
                                    'Recursively compare kate and upton. Show the difference output in context format. While comparing treat upper and lowercase alphabets in name as identical.',
                                    'Names should be considered case insensitive and compare kate and upton recursively showing the output in context mode.']}, ignore_index = True)

#190
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -ru kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in unified format. Do not follow symlinks.',
                                    'Without dereferencing the symbolic links, recursively compare kate and upton. Show the difference output in unified context format. While comparing treat upper and lowercase alphabets in name as identical.',
                                    'Names should be considered case insensitive and compare kate and upton recursively showing the output in unified context mode. Do not resolve soft links.']}, ignore_index = True)

#191
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -ry kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in side by side format. Do not follow symlinks.',
                                    'Without dereferencing the symbolic links, recursively compare kate and upton. Show the difference output in side-by-side format. While comparing treat upper and lowercase alphabets in name as identical.',
                                    'Names should be considered case insensitive and compare kate and upton recursively in side by side mode. Do not resolve soft links.']}, ignore_index = True)

#192
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -rc kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in context format. Do not follow symlinks.',
                                    'Without dereferencing the symbolic links, recursively compare kate and upton. Show the difference output in context format. While comparing treat upper and lowercase alphabets in name as identical.',
                                    'Names should be considered case insensitive and compare kate and upton recursively showing the result in context mode. Do not resolve soft links.']}, ignore_index = True)

#193
diff = diff.append({'Command':     'diff -rsq kate upton',
                    'NL Queries':  ['Compare the directories recursively and check if the files are identical or different.',
                                    'Recursively compare kate and upton to check if they are same or different.',
                                    'Are the contents of kate and upton same or different?',
                                    'For each file inside kate and upton, show whether they are same or different from the corresponding file in other folder.']}, ignore_index = True)

#194
diff = diff.append({'Command':     'diff --ignore-file-name-case -ruw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in unified format. Ignore any white space difference.',
                                    'Recursively compare kate and upton folders. Use unified format for showing differences. While comparing ignore white space differences and case differences in file names.',
                                    'Compare contents of kate and upton and show the differences with unified lines of context near the changes. Treat upper and lower case as same in file names and ignore white spaces.']}, ignore_index = True)

#195
diff = diff.append({'Command':     'diff --ignore-file-name-case -ryw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in side by side format. Ignore any white space difference.',
                                    'Recursively compare kate and upton folders. Use side by side format for showing differences. While comparing ignore white space differences and case differences in file names.',
                                    'Placing the contents of kate and upton next to each other highlight the differences. Treat upper and lower case as same in file names and ignore white spaces.']}, ignore_index = True)

#196
diff = diff.append({'Command':     'diff --ignore-file-name-case -rcw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in context format. Ignore any white space difference.',
                                    'Recursively compare kate and upton directories. Do not consider file names to be case sensitive. Output the differences in context mode ignoring white spaces.',
                                    'Ignoring white space differences, recursively differentiate between kate and upton folders in context format. Treat upper and lower case as same in file names.']}, ignore_index = True)

#197
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -ruw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in unified format. Do not follow symlinks. Ignore any white space difference.',
                                    'Without resolving symbolic links, recursively compare kate and upton folders. Use unified format for showing differences. While comparing ignore white space differences and case differences in file names.',
                                    'Compare contents of kate and upton and show the differences with unified lines of context near the changes. Treat upper and lower case as same in file names and ignore white spaces. Do not resolve soft links.']}, ignore_index = True)

#198
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -ryw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in side by side format. Do not follow symlinks. Ignore any white space difference.',
                                    'Without resolving symbolic links, recursively compare kate and upton folders. Use side by side format for showing differences. While comparing ignore white space differences and case differences in file names.',
                                    'Placing the contents of kate and upton next to each other highlight the differences. Treat upper and lower case as same in file names and ignore white spaces. Do not try to reference soft links.']}, ignore_index = True)

#199
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -rcw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in context format. Do not follow symlinks. Ignore any white space difference.',
                                    'Recursively compare kate and upton directories. Do not consider file names to be case sensitive and do not follow soft links. Output the differences in context mode ignoring white spaces.',
                                    'Ignoring white space differences, recursively differentiate between kate and upton folders in context format. Treat upper and lower case as same in file names and do not resolve symbolic links.']}, ignore_index = True)

#200
diff = diff.append({'Command':     'diff -rsqw kate upton',
                    'NL Queries':  ['Compare the directories recursively and check if the files are identical or different. Ignore any white space difference.',
                                    'Determine if directories kate and upton are same or not. Compare each file and subdirectory recursively.',
                                    'Are kate and upton different? Compare each file and sub folder.']}, ignore_index = True)

#201
diff = diff.append({'Command':     'diff --version',
                    'NL Queries':   ['Show the version of diff command.',
                                     'Display the authors of diff command.',
                                     'How to find out the authors and version number of diff command?']}, ignore_index = True)

#202
diff = diff.append({'Command':     'diff --help',
                    'NL Queries':  ['Show quick summary of diff command.',
                                    'Show options available with diff command for use.',
                                    'How to use diff command?']}, ignore_index = True)
                                    
print diff
