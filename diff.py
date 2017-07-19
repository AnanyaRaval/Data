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

#####JULY 17
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
#diff = diff.append({'Command':     'diff -c chk1.txt chk2.txt',
#                    'NL Queries':  ['Find difference between files chk1.txt and chk2.txt in context mode.']}, ignore_index = True)

#4
diff = diff.append({'Command':'diff -e chk1.txt chk2.txt',
                    'NL Queries':  ['Find difference between files chk1.txt and chk2.txt and output an ed script.'
                                        'Show difference in contents of files chk1.txt and chk2.txt. Show an ed script on screen.'
                                        'How do I distinguish between chk1.txt and chk2.txt present in current folder? Show the difference on screen in form of ed script.'
                                        'How is chk1.txt different from chk2.txt? Add differences in the form of ed script.']}, ignore_index = True)

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
                    'NL Queries':  ['Output the difference between space.txt and line.txt files ignoring trailing white spaces.']}, ignore_index = True)

#9
diff = diff.append({'Command':     'diff -w space.txt line.txt',
                    'NL Queries':  ['Output the difference between space.txt and line.txt files ignoring white space differences.']}, ignore_index = True)

#10
#diff = diff.append({'Command':     'diff -Z space.txt line.txt',
#                    'NL Queries':  ['Output the difference between space.txt and line.txt files ignoring trailing white spaces.']}, ignore_index = True)

#11
diff = diff.append({'Command':     'diff -b space.txt line.txt',
                    'NL Queries':  ['Output the difference between space.txt and line.txt files ignoring amount of white spaces.']}, ignore_index = True)

#12
diff = diff.append({'Command':     'diff -n space.txt line.txt',
                    'NL Queries':  ['Output the difference between space.txt and line.txt files in RCS format.']}, ignore_index = True)

#13
diff = diff.append({'Command':     'diff best worst',
                    'NL Queries':  ['Output the difference between best and worst directories.']}, ignore_index = True)


# 
print diff
