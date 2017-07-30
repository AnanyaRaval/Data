import pandas as pd 

diff = pd.DataFrame(columns = ['Command','NL Queries'])

diff = diff.append({'Command':'diff file1.txt file2.txt','NL Queries':['How do I find the difference between files file1.txt and file2.txt?',
                              'What is the difference between file1.txt and file2.txt? Both files are in this folder.',
                                   'How do I display lines which are different from each other in file1.txt and file2.txt?']},ignore_index = True)

diff = diff.append({'Command':'diff -u file1.txt file2.txt','NL Queries':['How do I find the difference between file1.txt and file2.txt? Print all unique rows from both files.'
                                   'How do I print a unified set of all distinct rows in file1.txt and file2.txt?', 'How do I print unique rows from both file1.txt and file2.txt combined?']},ignore_index=True)

diff = diff.append({'Command':'diff -i file1.txt file2.txt','NL Queries':['How do I perform a case insensitive comparision of file1.txt and file2.txt? Print the difference on Command Line.',
                    'Command to print case insensitive difference between file1.txt and file2.txt in this folder.'
                         'Display differences between file1.txt and file2.txt. Take case insensitive differences.']},ignore_index=True)


#1
diff = diff.append({'Command':'diff -q chk1.txt chk2.txt',
                    'NL Queries':  ['Check if there is difference between file chk1.txt and chk2.txt or not.',
                         'Output whether there is a difference between chk1.txt and chk2.txt or not. Do not display the difference.',
                         'How do I check whether there is a difference between chk1.txt and chk2.txt present in this folder.',
                              'Check if chk1.txt is different than chk2.txt. If there is a difference, do not display.',
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
                                    'How do I distinguish between chk1.txt and chk2.txt present in current folder? Show the difference on screen in form of ed script.']},ignore_index=True)

                 
#49                                                                                                                                                                  
diff = diff.append({'Command':'diff -r selena gomez',                                                                                                              
                    'NL Queries':  ['Recursively compare directories selena and gomez .',                                                                               
                                    'Show differences between selena and gomez directories recursively.',                                                                                      
                                    'How is selena different from gomez? Find differences between them including differences between all files and folders they contain.']}, ignore_index = True)

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
                                    'Display the distinctions between the C source files aa.c and AA.c. Do not show white space differences.']}, ignore_index = True)

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
                                    'Display the distinctions between C files aa.cpp and AA.cpp without considering TAB expansion as a change.',
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

#diff = diff.append({'Command':     'diff -r selena gomez',
#                    'NL Queries':  ['Recursively compare directories selena and gomez .',
#                                    'Show differences between selena and gomez directories recursively.',
#                                    'Display the differences between selena and gomez directories. Also compare underlying directories.']}, ignore_index = True)

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
                    'NL Queries':   ['Output the differences between naruto.txt file and sasuke.txt file in unified format. Before comparing the lines remove the trailing carriage return.']}, ignore_index = True)

#72
diff = diff.append({'Command':      'diff --strip-trailing-cr -c naruto.txt sasuke.txt',
                    'NL Queries':   ['Output the differences between naruto.txt file and sasuke.txt file in context format. Before comparing the lines remove the trailing carriage return.']}, ignore_index = True)

#73
diff = diff.append({'Command':      'diff -u --speed-large-files Big.txt Data.txt',
                    'NL Queries':   ['Show the differences between two large files Big.txt and Data.txt in unified format using speedup heuristics.']}, ignore_index = True)

#74
diff = diff.append({'Command':      'diff -y --speed-large-files Big.txt Data.txt',
                    'NL Queries':   ['Show the differences between two large files Big.txt and Data.txt in side by side format using speedup heuristics.']}, ignore_index = True)

#75
diff = diff.append({'Command':      'diff -c --speed-large-files Big.txt Data.txt',
                    'NL Queries':   ['Show the differences between two large files Big.txt and Data.txt in context format using speedup heuristics.']}, ignore_index = True)

#76
diff = diff.append({'Command':      'diff -e undo.txt redo.txt',
                    'NL Queries':   ['Output the forward ed script that shows the difference between undo.txt and redo.txt files.']}, ignore_index = True)

#77
diff = diff.append({'Command':      'diff -d long.txt file.txt',
                    'NL Queries':   ['Output minimal differences between long.txt and file.txt files.']}, ignore_index = True)

#78
diff = diff.append({'Command':      'diff -du long.txt file.txt',
                    'NL Queries':   ['Output minimal differences between long.txt and file.txt files in unified format.']}, ignore_index = True)

#79
diff = diff.append({'Command':      'diff -dy long.txt file.txt',
                    'NL Queries':   ['Output minimal differences between long.txt and file.txt files in side by side format.']}, ignore_index = True)

#80
diff = diff.append({'Command':      'diff -dc long.txt file.txt',
                    'NL Queries':   ['Output minimal differences between long.txt and file.txt files in context format.']}, ignore_index = True)

#81
diff = diff.append({'Command':      'diff -u --color lets.txt meet.txt',
                    'NL Queries':   ['Show the difference between lets.txt meet.txt files in unified format using color to show context.']}, ignore_index = True)

#82
diff = diff.append({'Command':      'diff -c --color lets.txt meet.txt',
                    'NL Queries':   ['Show the difference between lets.txt meet.txt files in context format using color to show context.']}, ignore_index = True)

#83
diff = diff.append({'Command':      'diff --color --palette=\'de=33\' color.txt one.txt',
                    'NL Queries':   ['Output the difference between color.txt and one.txt files with deleted lines shown in yellow color and others with their default color values.']}, ignore_index = True)

#84
diff = diff.append({'Command':      'diff --color --palette=\'de=33\' -u color.txt one.txt',
                    'NL Queries':   ['Output the difference in unified format between color.txt and one.txt files with deleted lines shown in yellow color and others with their default color values.']}, ignore_index = True)

#85
diff = diff.append({'Command':      'diff --color --palette=\'de=33\' -c color.txt one.txt',
                    'NL Queries':   ['Output the difference in context format between color.txt and one.txt files with deleted lines shown in yellow color and others with their default color values.']}, ignore_index = True)

#86
#diff = diff.append({'Command':      'diff --color --palette=\'de=33\' color.txt one.txt',
#                    'NL Queries':   ['Output the difference between color.txt and one.txt files with deleted lines shown in yellow color and others with their default color values.']}, ignore_index = True)

#87
diff = diff.append({'Command':      'diff -ub one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in unified format. Do not distinguish lines on the basis of number of white space characters.']}, ignore_index = True)

#88
diff = diff.append({'Command':      'diff -yb one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in side by side format. Do not distinguish lines on the basis of number of white space characters.']}, ignore_index = True)

#89
diff = diff.append({'Command':      'diff -cb one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in context format. Do not distinguish lines on the basis of number of white space characters.']}, ignore_index = True)

#90
diff = diff.append({'Command':      'diff -uB one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in unified format. Do not include blank lines in difference.']}, ignore_index = True)

#91
diff = diff.append({'Command':      'diff -yB one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in side by side format. Do not include blank lines in difference.']}, ignore_index = True)

#92
diff = diff.append({'Command':      'diff -cB one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in context format. Do not include blank lines in difference.']}, ignore_index = True)

#93
diff = diff.append({'Command':      'diff -ui one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in unified format ignoring case difference.']}, ignore_index = True)

#94
diff = diff.append({'Command':      'diff -yiZ one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in side by side format ignoring case differences and trailing white spaces.']}, ignore_index = True)

#95
diff = diff.append({'Command':      'diff -ci one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in context format ignoring case differences.']}, ignore_index = True)

#96
diff = diff.append({'Command':      'diff --no-dereference emma watson',
                    'NL Queries':   ['Compare the directories emma and watson . Do not follow symlinks.']}, ignore_index = True)

#97
diff = diff.append({'Command':      'diff -ni one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in RCS format ignoring case differences.']}, ignore_index = True)

#98
diff = diff.append({'Command':      'diff -nB one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in RCS format. Do not include blank lines in difference.']}, ignore_index = True)

#99
diff = diff.append({'Command':      'diff -nb one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in RCS format. Do not distinguish lines on the basis of number of white space characters.']}, ignore_index = True)

#100
diff = diff.append({'Command':      'diff -nt dead.txt pool.txt',
                    'NL Queries':   ['Show the differences between files dead.txt pool.txt in RCS format. In output expand TAB to spaces.']}, ignore_index = True)

#101
diff = diff.append({'Command':      'diff -ct dead.txt pool.txt',
                    'NL Queries':   ['Show the differences between files dead.txt pool.txt in context format. In output expand TAB to spaces.']}, ignore_index = True)

#102
diff = diff.append({'Command':      'diff -ut dead.txt pool.txt',
                    'NL Queries':   ['Show the differences between files dead.txt pool.txt in unified format. In output expand TAB to spaces.']}, ignore_index = True)

#103
diff = diff.append({'Command':      'diff -yt dead.txt pool.txt',
                    'NL Queries':   ['Show the differences between files dead.txt pool.txt in side by side format. In output expand TAB to spaces.']}, ignore_index = True)

#104
diff = diff.append({'Command':      'diff -qE victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving TAB expansion.']}, ignore_index = True)

#105
diff = diff.append({'Command':      'diff -qb victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving amount of white spaces.']}, ignore_index = True)

#106
diff = diff.append({'Command':      'diff -qB victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving insertion or deletion of blank lines.']}, ignore_index = True)

#107
diff = diff.append({'Command':      'diff -qw victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving white spaces.']}, ignore_index = True)

#108
diff = diff.append({'Command':      'diff -qZ victoria.txt justice.txt',
                    'NL Queries':   ['Check if there is any difference between files victoria.txt and justice.txt except those involving trailing white spaces.']}, ignore_index = True)

#109
diff = diff.append({'Command':      'diff -ya victoria bonya',
                    'NL Queries':   ['Find the differences between victoria and bonya in side by side format and treat them as text files.']}, ignore_index = True)

#110
diff = diff.append({'Command':      'diff -y --binary victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt files in side by side format and read-write in binary mode.']}, ignore_index = True)

#111
diff = diff.append({'Command':      'diff -yE victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in side by side format and ignore changes due to tab expansion.']}, ignore_index = True)

#112
diff = diff.append({'Command':      'diff -y --from-file=model.txt victoria bonya',
                    'NL Queries':   ['Find how the files model.txt in victoria and bonya directories differ from model.txt in current directory in side by side format.']}, ignore_index = True)

#113
diff = diff.append({'Command':      'diff -yI \'[0-9]\' victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in side by side format and ignore changes due to regex \'[0-9]\' .']}, ignore_index = True)

#114
diff = diff.append({'Command':      'diff -yl victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in side by side format and paginate the output.']}, ignore_index = True)

#115
diff = diff.append({'Command':      'diff -yN victoria.txt bonya.txt',
                    'NL Queries':   ['Show the differences between the files victoria.txt and bonya.txt in side by side format. Treat the file as empty if it is not present.']}, ignore_index = True)

#116
diff = diff.append({'Command':      'diff -yr mad grace',
                    'NL Queries':   ['Output the difference between directories mad and grace in side by side format recursively.']}, ignore_index = True)

#117
diff = diff.append({'Command':      'diff -yS holla.txt UK Switz',
                    'NL Queries':   ['Show the differences between directories UK and Switz in side by side format and start comparing from file holla.txt .']}, ignore_index = True)

#118
diff = diff.append({'Command':      'diff -cT UK.txt US.txt',
                    'NL Queries':   ['Show the difference between files UK.txt and US.txt and append a leading TAB to the output lines in context format.']}, ignore_index = True)

#119
diff = diff.append({'Command':      'diff -y --to-file=currency.txt US UK IND',
                    'NL Queries':   ['Output the differences between the file currency.txt in directories US , UK and IND to currency.txt in current directory in side by side format.']}, ignore_index = True)

#120
diff = diff.append({'Command':      'diff -yx \'*.cpp\' US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in side by side format. Do not compare files or directories whose names end with .cpp .']}, ignore_index = True)

#121
diff = diff.append({'Command':      'diff -yX exc.txt US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in side by side format. Do not compare files or directories whose names end match with the pattern mentioned in file exc.txt .']}, ignore_index = True)

#122
diff = diff.append({'Command':      'diff -na a.out b.out',
                    'NL Queries':   ['Show the differences between a.out and b.out treating them as text files in RCS format.']}, ignore_index = True)

#123
diff = diff.append({'Command':      'diff -nd aa.txt bb.txt',
                    'NL Queries':   ['Show minimal differences between files aa.txt and bb.txt in RCS format.']}, ignore_index = True)

#124
diff = diff.append({'Command':      'diff -nE one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in RCS format. Ignore any changes due to tab expansion.']}, ignore_index = True)

#125
diff = diff.append({'Command':      'diff -n --from-file=currency.txt US UK',
                    'NL Queries':   ['Show the lines where US/currency.txt and UK/currency.txt differ from currency.txt in current directory in RCS format.']}, ignore_index = True)

#126
diff = diff.append({'Command':      'diff -nI \'[0-9]\' victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in RCS format and ignore changes due to regex \'[0-9]\' .']}, ignore_index = True)

#127
diff = diff.append({'Command':      'diff -nl victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in RCS format and paginate the output.']}, ignore_index = True)

#128
diff = diff.append({'Command':      'diff -nN victoria.txt bonya.txt',
                    'NL Queries':   ['Show the differences between the files victoria.txt and bonya.txt in RCS format. Treat the file as empty if it is not present.']}, ignore_index = True)

#129
diff = diff.append({'Command':      'diff -nS model.txt mad grace',
                    'NL Queries':   ['Output the difference between directories mad and grace in RCS format. Start from file named model.txt .']}, ignore_index = True)

#130
diff = diff.append({'Command':      'diff -nx \'*.cpp\' US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in RCS format. Do not compare files or directories whose names end with .cpp .']}, ignore_index = True)

#131
diff = diff.append({'Command':      'diff -nX exc.txt US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in RCS format. Do not compare files or directories whose names end match with the pattern mentioned in file exc.txt .']}, ignore_index = True)

#132
diff = diff.append({'Command':      'diff -nw abc.txt xyz.txt',
                    'NL Queries':   ['Show the differences between abc.txt and xyz.txt in RCS format and ignore the differences involving white spaces.']}, ignore_index = True)

#133
diff = diff.append({'Command':      'diff -ca tic.txt tac.txt',
                    'NL Queries':   ['Show the differences between tic.txt and tac.txt files in context format treating them as text files. ']}, ignore_index = True)

#134
diff = diff.append({'Command':      'diff -c --binary tic.txt tac.txt',
                    'NL Queries':   ['Show the differences between the files tic.txt and tac.txt in context format. Read and write in binary mode.']}, ignore_index = True)

#135
diff = diff.append({'Command':      'diff -cE tic.txt tac.txt',
                    'NL Queries':   ['Show the differences between tic.txt and tac.txt files in context mode and ignore changes due to tab expansion.']}, ignore_index = True)

#136
diff = diff.append({'Command':      'diff -c --from-file=currency.txt US UK',
                    'NL Queries':   ['Show the lines where US/currency.txt and UK/currency.txt differ from currency.txt in current directory in context format.']}, ignore_index = True)

#137
diff = diff.append({'Command':      'diff -cI \'[0-9]\' victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in context format and ignore changes due to regex \'[0-9]\' .']}, ignore_index = True)

#138
diff = diff.append({'Command':      'diff -cl victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in context format and paginate the output.']}, ignore_index = True)

#139
diff = diff.append({'Command':      'diff -cN victoria.txt bonya.txt',
                    'NL Queries':   ['Show the differences between the files victoria.txt and bonya.txt in context format. Treat the file as empty if it is not present.']}, ignore_index = True)

#140
diff = diff.append({'Command':      'diff -cS model.txt mad grace',
                    'NL Queries':   ['Output the difference between directories mad and grace in context format. Start from file named model.txt .']}, ignore_index = True)

#141
diff = diff.append({'Command':      'diff -cx \'*.cpp\' US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in context format. Do not compare files or directories whose names end with .cpp .']}, ignore_index = True)

#142
diff = diff.append({'Command':      'diff -cX exc.txt US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in context format. Do not compare files or directories whose names end match with the pattern mentioned in file exc.txt .']}, ignore_index = True)

#143
diff = diff.append({'Command':      'diff -c --to-file=currency.txt US UK IND',
                    'NL Queries':   ['Output the differences between the file currency.txt in directories US , UK and IND to currency.txt in current directory in context format.']}, ignore_index = True)

#144
diff = diff.append({'Command':      'diff -c --suppress-blank-empty tt.txt txt.txt',
                    'NL Queries':   ['Show the differences between tt.txt and txt.txt files in context mode. Suppress any blanks before newlines when printing the representation of an empty line.']}, ignore_index = True)

#145
diff = diff.append({'Command':      'diff -ua a.out b.out',
                    'NL Queries':   ['Show the differences between a.out and b.out treating them as text files in unified format.']}, ignore_index = True)

#146
diff = diff.append({'Command':      'diff -uS model.txt mad grace',
                    'NL Queries':   ['Output the difference between directories mad and grace in unified format. Start from file named model.txt .']}, ignore_index = True)

#147
diff = diff.append({'Command':      'diff -uE one.txt two.txt',
                    'NL Queries':   ['Show the differences between one.txt and two.txt files in unified format. Ignore any changes due to tab expansion.']}, ignore_index = True)

#148
diff = diff.append({'Command':      'diff -u --from-file=currency.txt US UK',
                    'NL Queries':   ['Show the lines where US/currency.txt and UK/currency.txt differ from currency.txt in current directory in unified format.']}, ignore_index = True)

#149
diff = diff.append({'Command':      'diff -uI \'[0-9]\' victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in unified format and ignore changes due to regex \'[0-9]\' .']}, ignore_index = True)

#150
diff = diff.append({'Command':      'diff -ul victoria.txt bonya.txt',
                    'NL Queries':   ['Find the differences between victoria.txt and bonya.txt in unified format and paginate the output.']}, ignore_index = True)

#151
diff = diff.append({'Command':      'diff -uN victoria.txt bonya.txt',
                    'NL Queries':   ['Show the differences between the files victoria.txt and bonya.txt in unified format. Treat the file as empty if it is not present.']}, ignore_index = True)

#152
diff = diff.append({'Command':      'diff -ux \'*.cpp\' US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in unified format. Do not compare files or directories whose names end with .cpp .']}, ignore_index = True)

#153
diff = diff.append({'Command':      'diff -uX exc.txt US Russia',
                    'NL Queries':   ['Output the differences between directories US and Russia in unified format. Do not compare files or directories whose names end match with the pattern mentioned in file exc.txt .']}, ignore_index = True)

#154
diff = diff.append({'Command':      'diff -u --to-file=currency.txt US UK IND',
                    'NL Queries':   ['Output the differences between the file currency.txt in directories US , UK and IND to currency.txt in current directory in unified format.']}, ignore_index = True)

#155
diff = diff.append({'Command':      'diff -u --suppress-blank-empty tt.txt txt.txt',
                    'NL Queries':   ['Show the differences between tt.txt and txt.txt files in unified mode. Suppress any blanks before newlines when printing the representation of an empty line.']}, ignore_index = True)

#156
diff = diff.append({'Command':     'diff -uZ aa.txt AA.txt',
                    'NL Queries':  ['Show the differences in files aa.txt and AA.txt in unified format not involving trailing white space differences.']}, ignore_index = True)

#157
diff = diff.append({'Command':     'diff -bB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space.']}, ignore_index = True)

#158
diff = diff.append({'Command':     'diff -ubB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in unified format.']}, ignore_index = True)

#159
diff = diff.append({'Command':     'diff -cbB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in context format.']}, ignore_index = True)

#160
diff = diff.append({'Command':     'diff -ybB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in side by side format.']}, ignore_index = True)

#161
diff = diff.append({'Command':     'diff -nbB abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in RCS format.']}, ignore_index = True)

#162
diff = diff.append({'Command':     'diff -dbB abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space.']}, ignore_index = True)

#163
diff = diff.append({'Command':     'diff -ubBd abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in unified format.']}, ignore_index = True)

#164
diff = diff.append({'Command':     'diff -cdbB abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in context format.']}, ignore_index = True)

#165
diff = diff.append({'Command':     'diff -ybBd abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in side by side format.']}, ignore_index = True)

#166
diff = diff.append({'Command':     'diff -nbBd abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in RCS format.']}, ignore_index = True)

#167
diff = diff.append({'Command':     'diff -bBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes , tab expansion changes and amount of white space.']}, ignore_index = True)

#168
diff = diff.append({'Command':     'diff -ubBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in unified format.']}, ignore_index = True)

#169
diff = diff.append({'Command':     'diff -cbBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in context format.']}, ignore_index = True)

#170
diff = diff.append({'Command':     'diff -ybBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in side by side format.']}, ignore_index = True)

#171
diff = diff.append({'Command':     'diff -nbBE abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in RCS format.']}, ignore_index = True)

#172
diff = diff.append({'Command':     'diff -bBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space. Paginate the output.']}, ignore_index = True)

#173
diff = diff.append({'Command':     'diff -ubBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in unified format. Paginate the output.']}, ignore_index = True)

#174
diff = diff.append({'Command':     'diff -cbBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in context format. Paginate the output.']}, ignore_index = True)

#175
diff = diff.append({'Command':     'diff -ybBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in side by side format. Paginate the output.']}, ignore_index = True)

#176
diff = diff.append({'Command':     'diff -nbBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in RCS format. Paginate the output.']}, ignore_index = True)

#177
diff = diff.append({'Command':     'diff -dbBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space. Paginate the output.']}, ignore_index = True)

#178
diff = diff.append({'Command':     'diff -ubBdl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in unified format. Paginate the output.']}, ignore_index = True)

#179
diff = diff.append({'Command':     'diff -cdbBl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in context format. Paginate the output.']}, ignore_index = True)

#180
diff = diff.append({'Command':     'diff -ybBdl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in side by side format. Paginate the output.']}, ignore_index = True)

#181
diff = diff.append({'Command':     'diff -nbBdl abc.txt xyz.txt',
                    'NL Queries':  ['Show the minimal differences between abc.txt and xyz.txt ignoring blank line changes and amount of white space in RCS format. Paginate the output.']}, ignore_index = True)

#182
diff = diff.append({'Command':     'diff -bBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes , tab expansion changes and amount of white space. Paginate the output.']}, ignore_index = True)

#183
diff = diff.append({'Command':     'diff -ubBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in unified format. Paginate the output.']}, ignore_index = True)

#184
diff = diff.append({'Command':     'diff -cbBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in context format. Paginate the output.']}, ignore_index = True)

#185
diff = diff.append({'Command':     'diff -ybBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in side by side format. Paginate the output.']}, ignore_index = True)

#186
diff = diff.append({'Command':     'diff -nbBEl abc.txt xyz.txt',
                    'NL Queries':  ['Show the differences between abc.txt and xyz.txt ignoring blank line changes, tab expansion changes and amount of white space in RCS format. Paginate the output.']}, ignore_index = True)

#187
diff = diff.append({'Command':     'diff --ignore-file-name-case -ru kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in unified format.']}, ignore_index = True)

#188
diff = diff.append({'Command':     'diff --ignore-file-name-case -ry kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in side by side format.']}, ignore_index = True)

#189
diff = diff.append({'Command':     'diff --ignore-file-name-case -rc kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in context format.']}, ignore_index = True)

#190
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -ru kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in unified format. Do not follow symlinks.']}, ignore_index = True)

#191
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -ry kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in side by side format. Do not follow symlinks.']}, ignore_index = True)

#192
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -rc kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in context format. Do not follow symlinks.']}, ignore_index = True)

#193
diff = diff.append({'Command':     'diff -rsq kate upton',
                    'NL Queries':  ['Compare the directories recursively and check if the files are identical or different.']}, ignore_index = True)

#194
diff = diff.append({'Command':     'diff --ignore-file-name-case -ruw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in unified format. Ignore any white space difference.']}, ignore_index = True)

#195
diff = diff.append({'Command':     'diff --ignore-file-name-case -ryw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in side by side format. Ignore any white space difference.']}, ignore_index = True)

#196
diff = diff.append({'Command':     'diff --ignore-file-name-case -rcw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in context format. Ignore any white space difference.']}, ignore_index = True)

#197
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -ruw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in unified format. Do not follow symlinks. Ignore any white space difference.']}, ignore_index = True)

#198
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -ryw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in side by side format. Do not follow symlinks. Ignore any white space difference.']}, ignore_index = True)

#199
diff = diff.append({'Command':     'diff --no-dereference --ignore-file-name-case -rcw kate upton',
                    'NL Queries':  ['Compare the directories kate and upton recursively. Treat file names to be case-insensitive. Show the output in context format. Do not follow symlinks. Ignore any white space difference.']}, ignore_index = True)

#200
diff = diff.append({'Command':     'diff -rsqw kate upton',
                    'NL Queries':  ['Compare the directories recursively and check if the files are identical or different. Ignore any white space difference.']}, ignore_index = True)



print diff.shape
