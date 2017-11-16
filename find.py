import pandas as pd 

find = pd.DataFrame(columns = ['Command','NL Queries'])

find = find.append({'Command':'find . -name tecmint.txt','NL Queries':['Find all the files whose name is tecmint.txt in a current working directory.',
                                                                        'How do I list all files named techmint.txt in this folder?']},ignore_index = True)

find = find.append({'Command':'find /home -iname tecmint.txt','NL Queries':['Find all the files whose name is tecmint.txt and contains both capital and small letters in /home directory.',
                                                                            'List all techmint.txt irrespective of their case in /home folder.']},ignore_index=True)
find = find.append({'Command':'find /home/Documents -type d -name Data','NL Queries':['Find all directories whose name is Data in /home/Documents directory.',
                                                                                        'How do I list all folders named Data in /home/Documents?']},ignore_index=True)


#1
find = find.append({'Command':      'find .',
                    'NL Queries':   ['Find all the files in current directory.',
                                     'List all the files in present working directory.',
                                     'Show the files inside current folder.',
                                     'how to display all the files under current folder?']}, ignore_index = True)

#2
find = find.append({'Command':      'find /tmp/',
                    'NL Queries':   ['Find all the files in /tmp directory.',
                                     'Search for all the files inside /tmp/ folder.',
                                     'List all the files under /tmp directory.',
                                     'How to display all the files under current folder?']}, ignore_index = True)

#3
find = find.append({'Command':      'find /tmp/ -maxdepth 2 -name xyz0509',
                    'NL Queries':   ['Find the file named xyz0509 in /tmp directory. Search only till depth of 2.',
                                     'Search for file named xyz0509 in /tmp/ directory only till the depth of two.',
                                     'List all the files in /tmp/ directory whose names match with xyz0509 and at a maximum depth of 2 from /tmp directory.',
                                     'How to display all the files whose names match with xyz0509 and are maximum 2 levels deep?']}, ignore_index = True)

#4
find = find.append({'Command':      'find /tmp/ -not -name \'*.cpp\'',
                    'NL Queries':   ['Find all the files in /tmp directory not ending with .cpp extension.',
                                     'Search for all the files in /tmp folder not ending with .cpp .',
                                     'Find all such files whose name do not end with .cpp in /tmp directory.',
                                     'How to list all those files which do not end with .cpp file name?']}, ignore_index = True)

#5
find = find.append({'Command':      'find /tmp/ -name \'abc*\' -not -name \'*.cpp\'',
                    'NL Queries':   ['Find all the files in /tmp directory whose name starts with abc and does not end with .cpp .',
                                     'List all such files under /tmp folder whose name start with abc but do not end with .cpp .',
                                     'Search for all the files inside /tmp directory whose name start with abc but do not end with .cpp .']}, ignore_index = True)

#6
find = find.append({'Command':      'find /tmp/ -name \'abc*\' -o -name \'*.cpp\'',
                    'NL Queries':   ['Find all the files in /tmp directory whose name starts with abc or end with .cpp .',
                                     'Search for all those files inside /tmp folder whose name either starts with abc or ends with .cpp .',
                                     'List all those files inside /tmp/ with string abc in beginning of their names or .cpp at the end of their names.']}, ignore_index = True)

#7
find = find.append({'Command':      'find /tmp/ -type f -name pratik*\'',
                    'NL Queries':   ['Search for all the regular files starting with pratik in /tmp directory.',
                                     'List the regular files in /tmp directory with pratik as the starting string in name.',
                                     'Search for all simple files in /tmp folder whose name begin with substring pratik .']}, ignore_index = True)

#8
find = find.append({'Command':      'find /dev/ -type b -name \'mem*\'',
                    'NL Queries':   ['Find all the block device special files in /dev directory with name starting with mem .',
                                     'List the block device files in /dev directory with mem as the starting string in name.',
                                     'Search for all block special files in /dev folder whose name begin with substring mem .']}, ignore_index = True)

#9
find = find.append({'Command':      'find /dev/ -type c -name \'mem*\'',
                    'NL Queries':   ['Find all the char device special files in /dev directory with name starting with mem .',
                                     'Search for all char device files in /dev folder whose name begin with substring mem .',
                                     'List the special char files in /dev directory with mem as the starting string in name.']}, ignore_index = True)

#10
find = find.append({'Command':      'find /dev/ -type p -name \'mem*\'',
                    'NL Queries':   ['Find all the name pipe special files in /dev directory with name starting with mem .',
                                     'List the pipe files in /dev directory with mem as the starting string in name.',
                                     'Search for all pipe files in /dev folder whose name begin with substring mem .']}, ignore_index = True)

#11
find = find.append({'Command':      'find /dev/ -type l -name \'mem*\'',
                    'NL Queries':   ['Find all the symlink in /dev directory with name starting with mem .',
                                     'How do I search for all the symbolic links with names starting with mem ?',
                                     'Search for all soft links in /dev folder whose name begin with substring mem .']}, ignore_index = True)

#12
find = find.append({'Command':      'find /dev/ -type s -name \'mem*\'',
                    'NL Queries':   ['Find all the socket files in /dev directory with name starting with mem .',
                                     'Search for all socket files in /dev folder whose name begin with substring mem .',
                                     'How do I search for all the sockets in /dev/ with names starting with mem ?']}, ignore_index = True)

#13
find = find.append({'Command':      'find /tmp/ /dev/ -name \'abc*\'',
                    'NL Queries':   ['Find all the files starting with abc in directories /tmp and /dev .',
                                     'Search for all the files in /tmp and /abc directories for files whose name start with abc .',
                                     'Show the files whose name start with abc in /tmp and /dev folders.']}, ignore_index = True)

#14
find = find.append({'Command':      'find /boot/ -perm 0777',
                    'NL Queries':   ['Find all the files in /boot directory which has 0777 permission.',
                                     'List all the files in /boot/ folder with permission bits set as 0777 .',
                                     'Give a list of all those files under /boot directory with 777 as permission and no sticky bit.',
                                     'How to search for all the files in /boot directory with 0777 as permission ?']}, ignore_index = True)

#15
find = find.append({'Command':     'find /home/ -user zara',
                    'NL Queries':  ['Search for all the files in /home directory belonging to user zara .',
                                    'Show all the files in /home belonging to user zara .',
                                    'List the files in filder /home whose owner is user named zara .']}, ignore_index = True)

#16
find = find.append({'Command':     'find /etc/ -group wheel',
                    'NL Queries':  ['Search for all the files in /etc directory which belong to the group named wheel .',
                                    'Show all the files belonging to group wheel in /etc directory.',
                                    'Which files belong to group wheel in /etc/ directory?']}, ignore_index = True)

#17
find = find.append({'Command':     'find /lib/ -mtime 10',
                    'NL Queries':  ['Find all the files in /lib directory which was modified 10 days back.',
                                    'List for all the files in /lib/ folder with modification time 10 days ago.',
                                    'Search for the files under /lib directory with last modified time 10 days back.']}, ignore_index = True)

#18
find = find.append({'Command':     'find /lib/ -atime 10',
                    'NL Queries':  ['Find all the files in /lib directory which was accessed 10 days back.',
                                    'List for all the files in /lib/ folder with access time 10 days ago.',
                                    'Search for the files under /lib directory with last access time 10 days back.']}, ignore_index = True)

#19
find = find.append({'Command':     'find . -cmin -60',
                    'NL Queries':  ['Search for all the files in current directory which were changed within 60 minutes.',
                                    'Enumerate the files inside the current directory with change time less than 60 minutes.',
                                    'List all the files in present working directory with change time less than 60 minutes.',
                                    'Show the files in pwd which were changed less than 60 minutes ago.']}, ignore_index = True)

#20
find = find.append({'Command':     'find . -ctime +5 -ctime -10',
                    'NL Queries':  ['Search for all the files in current directory which were changed 5 to 10 days back.',
                                    'Display all such files in pwd with change time within 5 to 10 days ago.',
                                    'Show me all the files which were changed in an interval of 5 to 10 days ago.']}, ignore_index = True)

#21
find = find.append({'Command':     'find . -mtime +5 -mtime -10',
                    'NL Queries':  ['Search for all the files which were modified 5 to 10 days back.',
                                    'List all the files in current directory whose modification time is in between 5 to 10 days back from now.',
                                    'Display all the files in pwd which were last modified 5 through 10 days ago.']}, ignore_index = True)

#22
find = find.append({'Command':     'find . -atime +5 -atime -10',
                    'NL Queries':  ['Search for all the files which were accessed 5 to 10 days back.',
                                    'List all the files in current directory whose access time is in between 5 to 10 days back from now.',
                                    'Show me all the files which were accessed in an interval of 5 to 10 days ago in present directory.']}, ignore_index = True)

#23
find = find.append({'Command':     'find . -amin +5 -amin -10',
                    'NL Queries':  ['Search for all the files which were accessed 5 to 10 minutes back.',
                                    'Display the files which have their access timestamp set around 5 to 10 minutes ago.',
                                    'List the files which were read about 5 to 10 minutes back from now in current workspace.']}, ignore_index = True)

#24
find = find.append({'Command':     'find . -mmin +5 -mmin -10',
                    'NL Queries':  ['Search for all the files which were modified 5 to 10 minutes back.',
                                    'List all the files in current directory whose modification time is in between 5 to 10 minutes back from now.',
                                    'Show me all the files which were modified in an interval of 5 to 10 minutes ago in current working folder.']}, ignore_index = True)

#25
find = find.append({'Command':     'find . -cmin +5 -cmin -10',
                    'NL Queries':  ['Search for all the files which were changed 5 to 10 minutes back.',
                                    'In a time interval of 5 to 10 minutes, show all the files which were changed in current directory.',
                                    'In present working directory, show all the files that were changed about 5 to 10 minutes back.']}, ignore_index = True)

#26
find = find.append({'Command':     'find /lib/ -ctime 10',
                    'NL Queries':  ['Find all the files in /lib directory which was changed 10 days back.',
                                    'Search for all the files in /lib/ which were changed 10 days ago.',
                                    'Display the files in /lib/ which were changed 10 days back from now.']}, ignore_index = True)

#27
find = find.append({'Command':     'find . -amin -60',
                    'NL Queries':  ['Search for all the files in current directory which were accessed within 60 minutes.',
                                    'In current directory, which all files were accessed within 60 minutes?',
                                    'Show all the files that have been read from within 60 minutes in pwd .']}, ignore_index = True)

#28
find = find.append({'Command':     'find . -mmin -60',
                    'NL Queries':  ['Search for all the files in current directory which were modified within 60 minutes.',
                                    'In current directory, which all files were modified within 60 minutes?',
                                    'Show all the files that have been modified from within 60 minutes in pwd .']}, ignore_index = True)

#29
find = find.append({'Command':     'find . -size 10M',
                    'NL Queries':  ['Find all the files in current directory which occupy 10MB space.',
                                    'Show all 10MB files in current directory.',
                                    'Which files in present working directory have 10MB size?']}, ignore_index = True)

#30
find = find.append({'Command':     'find . -size -10M',
                    'NL Queries':  ['Find all the files in current directory which occupy less than 10MB space.',
                                    'Show all files in pwd which occupy less than 10 MB space.',
                                    'Which files in present working directory have less than 10MB size?']}, ignore_index = True)

#31
find = find.append({'Command':     'find . -size +10M',
                    'NL Queries':  ['Find all the files in current directory which occupy more than 10MB space.',
                                    'Show all files in pwd which occupy more than 10 MB space.',
                                    'Which files in present working directory have more than 10MB size?']}, ignore_index = True)

#32
find = find.append({'Command':     'find . -size -15M -size +10M',
                    'NL Queries':  ['Search for all the files which are greater than 10MB and less than 15MB in size.',
                                    'List all the files in pwd whose size is in between 10 to 15 MB.',
                                    'Show all the files in current directory whose size is in between 10 and 15 MB.']}, ignore_index = True)

#33
find = find.append({'Command':     'find . -empty',
                    'NL Queries':  ['Search for all the files which are empty.',
                                    'List all the empty files in pwd.',
                                    'Display all the files in current workspace which are empty.']}, ignore_index = True)

#34
find = find.append({'Command':      'find /tmp/ -maxdepth 2 -iname xyz0509',
                    'NL Queries':   ['Find the file named xyz0509 in /tmp directory. Search only till depth of 2 and perform case insensitive match.',
                                     'Search for all the files in /tmp directory with name matching with xyz0509 case insensitively. Do not go more than 2 directory levels deep.',
                                     'Ignoring case, list all the files whose name is xyz0509 in /tmp and are at maximum 2 levels inside.']}, ignore_index = True)

#35
find = find.append({'Command':      'find /tmp/ -not -iname \'*.cpp\'',
                    'NL Queries':   ['Find all the files in /tmp directory not ending with .cpp extension. Perform case-insensitive match.',
                                     'Show all the files in /tmp whose names do not end with .cpp , case insensitively.',
                                     'Do not display any such file whose name matches with .cpp at the end, ignoring case, in /tmp/ .']}, ignore_index = True)

#36
find = find.append({'Command':      'find /tmp/ -iname \'abc*\' -not -iname \'*.cpp\'',
                    'NL Queries':   ['Find all the files in /tmp directory whose name starts with abc and does not end with .cpp . Perform case-insensitive match.',
                                     'Perform all matching, case insensitively. Find all such files inside /tmp starting with abc and not ending with .cpp .',
                                     'Treat upper and lower case as same. List all the files under /tmp such that its name starts with abc but does not end with cpp.']}, ignore_index = True)

#37
find = find.append({'Command':      'find /tmp/ -iname \'abc*\' -o -iname \'*.cpp\'',
                    'NL Queries':   ['Find all the files in /tmp directory whose name starts with abc or end with .cpp . Perform case-insensitive match.',
                                     'Perform all matching, case insensitively. Find all such files inside /tmp starting with abc or ending with .cpp .',
                                     'Treat upper and lower case as same. List all the files under /tmp such that its name starts with abc or ends with .cpp .']}, ignore_index = True)

#38
find = find.append({'Command':      'find /tmp/ -type f -iname pratik*\'',
                    'NL Queries':   ['Search for all the regular files starting with pratik in /tmp directory. Perform case-insensitive match.',
                                     'Do all comparison ignoring case and list all the regular files which start with pratik name and in /tmp/ .',
                                     'Find all regular files inside /tmp with their name starting with pratik . Do case insensitive matching.']}, ignore_index = True)

#39
find = find.append({'Command':      'find /dev/ -type b -iname \'mem*\'',
                    'NL Queries':   ['Find all the block device special files in /dev directory with name starting with mem . Perform case-insensitive match.',
                                     'Do all comparison ignorinng case and list all the block device files which start with pratik name and in /tmp/ .',
                                     'Find all block files inside /tmp with their name starting with pratik . Do case insensitive matching.']}, ignore_index = True)

#40
find = find.append({'Command':      'find /dev/ -type c -iname \'mem*\'',
                    'NL Queries':   ['Find all the char device special files in /dev directory with name starting with mem . Perform case-insensitive matching.',
                                     'Do all comparison ignoring case and list all the char files which start with pratik name and in /dev/ .',
                                     'Find all char device files inside /dev with their name starting with pratik . Do case insensitive matching.']}, ignore_index = True)

#41
find = find.append({'Command':      'find /dev/ -type p -iname \'mem*\'',
                    'NL Queries':   ['Find all the name pipe special files in /dev directory with name starting with mem . Perform case-insensitive matching.',
                                     'Do all comparison ignoring case and list all the pipes which start with pratik name and in /dev/ .',
                                     'Find all pipe files inside /dev with their name starting with pratik . Do case insensitive matching.']}, ignore_index = True)

#42
find = find.append({'Command':      'find /dev/ -type l -iname \'mem*\'',
                    'NL Queries':   ['Find all the symlink in /dev directory with name starting with mem . Perform case-insensitive matching.',
                                     'Do all comparison ignoring case and list all the symbolic links which start with pratik name and in /dev/ .',
                                     'Find all soft links inside /dev with their name starting with pratik . Do case insensitive matching.']}, ignore_index = True)

#43
find = find.append({'Command':      'find /dev/ -type s -iname \'mem*\'',
                    'NL Queries':   ['Find all the socket files in /dev directory with name starting with mem . Perform case-insensitive matching.',
                                     'Do all comparison ignoring case and list all the socket files which start with pratik name and in /tmp/ .',
                                     'Find all socket files inside /tmp with their name starting with pratik . Do case insensitive matching.']}, ignore_index = True)

#44
find = find.append({'Command':      'find /tmp/ /dev/ -iname \'abc*\'',
                    'NL Queries':   ['Find all the files starting with abc in directories /tmp and /dev . Perform case-insensitive matching.',
                                     'List all the files in /tmp and /dev whose name start with abc and treat upper and lowercase the same.',
                                     'Display all the files that start with abc, not considering case, inside /tmp and /dev directory.']}, ignore_index = True)

#45
find = find.append({'Command':      'find . -newer unknown.txt',
                    'NL Queries':   ['Search for all the files which are newer than unknown.txt file.',
                                     'List all the files with modification time newer than unknown.txt in pwd .',
                                     'Display the files inside current workspace which is newer than the modification time of unknown.txt .']}, ignore_index = True)

#46
find = find.append({'Command':      'find . -mindepth 2 -name rcc.txt',
                    'NL Queries':   ['Search for all the files whose name match with rcc.txt and at least 2 levels deep from current directory.',
                                     'List all such files, at directory depth of at least 2, and name rcc.txt .',
                                     'Display all the files with name rcc.txt and at the minimum directory depth of 2 level.']}, ignore_index = True)

#47
find = find.append({'Command':      'find . -mindepth 2 -iname rcc.txt',
                    'NL Queries':   ['Search for all the files whose name match with rcc.txt case-insensitively and are at least 2 levels deep from current directory.',
                                     'List all such files, at directory depth of at least 2, and name rcc.txt , ignoring case difference.',
                                     'Display all the files with name rcc.txt and at the minimum directory depth of 2 level. Do not perform case sensitive comparison.']}, ignore_index = True)

#48
find = find.append({'Command':      'find . -inum 05091998',
                    'NL Queries':   ['Search for all the files in current directory with inode number 05091998 .',
                                     'Display all the files in current directory with inode number 05091998 .',
                                     'List the files with inode number 05091998 in pwd .']}, ignore_index = True)

#49
find = find.append({'Command':      'find . -anewer test.txt',
                    'NL Queries':   ['Search for all the files in current directory which have access time greater than the modification time of test.txt file.',
                                     'Display all the files in current directory with access time newer than modification time of test.txt file.',
                                     'List all such files which were accessed more recently than test.txt was modified in current directory.']}, ignore_index = True)

#50
find = find.append({'Command':      'find . -cnewer test.txt',
                    'NL Queries':   ['Search for all the files in current directory which have change time greater than the modification time of test.txt file.',
                                     'Display all the files in current directory with change time newer than modification time of test.txt file.',
                                     'List all such files which were changed more recently than test.txt was modified in current directory.']}, ignore_index = True)

#51
find = find.append({'Command':      'find / -xdev -name \'*.log\'',
                    'NL Queries':   ['Search for the file names ending with .log in root directory. Do not descend into directories of other file system.',
                                     'In the current file system, search for all files with names ending with .log .',
                                     'List all the files in current file system with names ending with .log .']}, ignore_index = True)

#52
find = find.append({'Command':      'find . -exec ls -l \'{}\' \\;',
                    'NL Queries':   ['Search for all the files in current directory and run the command \'ls -l\' on all of them.',
                                     'Execute the command \'ls -l\' on all the files in current directory.',
                                     'Run command \'ls -l\' on all the files in pwd .']}, ignore_index = True)

#53
find = find.append({'Command':      'find / -xdev -iname \'*.log\'',
                    'NL Queries':   ['Search for the file names ending with .log in root directory. Do not descend into directories of other file system. Do case-insensitive comparison.',
                                     'In the root file system, search for all files with names ending with .log . Compare them case insensitively.',
                                     'List all the files in root file system with names ending with .log without considering case.']}, ignore_index = True)

#54
find = find.append({'Command':      'find / -maxdepth 5 -mindepth 2 -name pratik.txt',
                    'NL Queries':   ['Search for the file named pratik.txt in root directory between levels 2 and 5.',
                                     'List all the files with name pratik.txt in / which are at maximum depth of 5 and minimum depth of 2.',
                                     'Display all the files in between directory levels 2 to 5 from / whose name is pratik.txt .']}, ignore_index = True)

#55
find = find.append({'Command':      'find / -maxdepth 5 -mindepth 2 -iname pratik.txt',
                    'NL Queries':   ['Search for the file named pratik.txt in root directory between levels 2 and 5, both inclusive. Perform case-insensitive search.',
                                     'List all the files with name pratik.txt , irrespective of case, in / which are at maximum depth of 5 and minimum depth of 2.',
                                     'Display all the files in between directory levels 2 to 5 from / whose name is pratik.txt , not considering case.']}, ignore_index = True)

#56
find = find.append({'Command':      'find / -maxdepth 4 -not -name \'*.log\'',
                    'NL Queries':   ['Search for all the files in / directory at a maximum depth of 4 so that the name does not end with .log .',
                                     'Find all such files in root directory with name not ending with .log and maximum depth 4.',
                                     'List all the files in root directory which are at a maximum directory depth of 4 and do not end with .log .']}, ignore_index = True)

#57
find = find.append({'Command':      'find / -maxdepth 4 -not -iname \'*.log\'',
                    'NL Queries':   ['Search for all the files in / directory at a maximum depth of 4 so that the name does not end with .log , case-insensitively.',
                                     'Find all such files in root directory with name not ending with .log and maximum depth 4. Do case insensitive comparison.',
                                     'List all the files in root directory which are at a maximum directory depth of 4 and do not end with .log . Names should be compared without case separation.']}, ignore_index = True)

#58
find = find.append({'Command':      'find / -maxdepth 6 -name \'*.cpp\' -o -name \'*.cc\'',
                    'NL Queries':   ['Search for all the files in root directory at maximum depth of 6 whose name either end with .cpp or .cc .',
                                     'Find all such files in root directory with name ending with .cpp or .cc and maximum depth 6.',
                                     'List all the files in root directory which are at a maximum directory depth of 6 and end with .cpp or .cc .']}, ignore_index = True)

#59
find = find.append({'Command':      'find / -maxdepth 6 -iname \'*.cpp\' -o -iname \'*.cc\'',
                    'NL Queries':   ['Search for all the files in root directory at maximum depth of 6 whose name either end with .cpp or .cc .',
                                     'Find all such files in root directory with name ending with .cpp or .cc and maximum depth 6. Do case insensitive comparison.',
                                     'List all the files in root directory which are at a maximum directory depth of 6 and end with .cpp or .cc . Names should be considered without considering case.']}, ignore_index = True)

#60
find = find.append({'Command':      'find / -maxdepth 2 -type f -name \'*.pl\'',
                    'NL Queries':   ['Search for all those files at a maximum depth of 2 from root directory whose name ends with .pl and are regular files.',
                                     'List all those regular files which end with .pl in / directory. Search only till the directory depth of 2.',
                                     'How to list all those regular files in / folder which end with .pl and are located at the maximum depth of 2?']}, ignore_index = True)

#61
find = find.append({'Command':      'find / -maxdepth 2 -type f -iname \'*.pl\'',
                    'NL Queries':   ['Search for all those files at a maximum depth of 2 from root directory whose name ends with .pl , case insensitively, and are regular files.',
                                     'List all those regular files which end with .pl in / directory. While matching names do not consider case of alphabets. Search only till the directory depth of 2.',
                                     'How to list all those regular files in / folder which end with .pl and are located at the maximum depth of 2? Treat upper and lower case as same.']}, ignore_index = True)

#62
find = find.append({'Command':      'find / -maxdepth 2 -type d -name \'*.pl\'',
                    'NL Queries':   ['Search for all those files at a maximum depth of 2 from root directory whose name ends with .pl and are directories.',
                                     'List all those directories which end with .pl in / directory. Search only till the directory depth of 2.',
                                     'How to list all those directories in / folder which end with .pl and are located at the maximum depth of 2?']}, ignore_index = True)

#63
find = find.append({'Command':      'find / -maxdepth 2 -type d -iname \'*.pl\'',
                    'NL Queries':   ['Search for all those files at a maximum depth of 2 from root directory whose name ends with .pl , case insensitively, and are directories.',
                                     'List all those directories which end with .pl in / directory. While matching names do not consider case of alphabets. Search only till the directory depth of 2.',
                                     'How to list all those directories in / folder which end with .pl and are located at the maximum depth of 2? Treat upper and lower case as same.']}, ignore_index = True)

#64
find = find.append({'Command':      'find / -maxdepth 3 -perm 0777',
                    'NL Queries':   ['Search for all those files which are at maximum depth 3 from root directory and has permission 0777 .',
                                     'List all the files with 777 permission bits and are at a maximum depth of 3 starting from / directory.',
                                     'Find all such files which have all the permission bits set and are at most 3 directories deep from root directory.']}, ignore_index = True)

#65
find = find.append({'Command':      'find / -maxdepth 4 -user pratik',
                    'NL Queries':   ['Search for all the files at a maximum depth of 4 from root directory whose owner is pratik .',
                                     'Display all the files which are owned by pratik and are at a maximum depth of 4.',
                                     'How to list all such files whose user owner is pratik and are located at most 4 directories deep?']}, ignore_index = True)

#66
find = find.append({'Command':      'find / -maxdepth 4 -group pratik',
                    'NL Queries':   ['Search for all the files at a maximum depth of 4 from root directory belonging to group pratik .',
                                     'Display all the files which are owned by group pratik and are at a maximum depth of 4.',
                                     'How to list all such files whose group owner is pratik and are located at most 4 directories deep?']}, ignore_index = True)

#67
find = find.append({'Command':      'find / -maxdepth 3 -atime 1',
                    'NL Queries':   ['Find all such files at the maximum depth of 3 from root directory which was accessed 1 day back.',
                                     'List all such files under root directory which were accessed one day ago and at most 3 directories deep.',
                                     'How to display all such files under / which have access time stamp of 1 day back and at most 3 levels of directories deep?']}, ignore_index = True)

#68
find = find.append({'Command':      'find / -maxdepth 3 -ctime 1',
                    'NL Queries':   ['Find all such files at the maximum depth of 3 from root directory which was changed 1 day back.',
                                     'List all such files under root directory which were changed one day ago and at most 3 directories deep.',
                                     'How to display all such files under / which have change time stamp of 1 day back and at most 3 levels of directories deep?']}, ignore_index = True)

#69
find = find.append({'Command':      'find / -maxdepth 3 -mtime 1',
                    'NL Queries':   ['Find all such files at the maximum depth of 3 from root directory which was modified 1 day back.',
                                     'List all such files under root directory which were modified one day ago and at most 3 directories deep.',
                                     'How to display all such files under / which have modification time stamp of 1 day back and at most 3 levels of directories deep?']}, ignore_index = True)

#70
find = find.append({'Command':      'find / -maxdepth 3 -amin 100',
                    'NL Queries':   ['Find all such files at the maximum depth of 3 from root directory which was accessed 100 minutes back.',
                                     'List all such files under root directory which were accessed 100 minutes ago and at most 3 directories deep.',
                                     'How to display all such files under / which have access time stamp of 100 minutes back and at most 3 levels of directories deep?']}, ignore_index = True)

#71
find = find.append({'Command':      'find / -maxdepth 3 -cmin 100',
                    'NL Queries':   ['Find all such files at the maximum depth of 3 from root directory which was changed 100 minutes back.',
                                     'List all such files under root directory which were changed 100 minutes ago and at most 3 directories deep.',
                                     'How to display all such files under / which have change time stamp of 100 minutes back and at most 3 levels of directories deep?']}, ignore_index = True)

#72
find = find.append({'Command':      'find / -maxdepth 3 -mmin 1',
                    'NL Queries':   ['Find all such files at the maximum depth of 3 from root directory which was modified 100 minutes back.',
                                     'List all such files under root directory which were modified 100 minutes ago and at most 3 directories deep.',
                                     'How to display all such files under / which have modification time stamp of 100 minutes back and at most 3 levels of directories deep?']}, ignore_index = True)

#73
find = find.append({'Command':      'find / -maxdepth 4 -size 10M',
                    'NL Queries':   ['Find all such files at the maximum depth of 4 from root directory which has size 10MB .',
                                     'Show all the files in / with size 10 MB and are at most 4 levels deep from the root.',
                                     'How to list all the files under root with size 10 MB and less than or equal to 4 directories deep.']}, ignore_index = True)

#74
find = find.append({'Command':      'find / -maxdepth 3 -empty',
                    'NL Queries':   ['Search for all such files at the maximum depth of 3 from root such that it is empty.',
                                     'Which are the empty files in / and are <= 3 directory level deep?',
                                     'Display the files which are under / and are empty. Do not display the files which are > 3 directories deep.']}, ignore_index = True)

#75
find = find.append({'Command':      'find / -maxdepth 3 -newer a.txt',
                    'NL Queries':   ['Search for all such files at the maximum depth of 3 from root such that its modification time is newer than a.txt file.',
                                     'Show all those files in / which have modification time newer than a.txt and have maximum depth of 3.',
                                     'How to list the files in root with modification time later than that of a.txt and <= 3 levels directory depth?']}, ignore_index = True)

#76
find = find.append({'Command':      'find / -maxdepth 3 -inum 13021970',
                    'NL Queries':   ['Search for all such files at the maximum depth of 3 from root such that its inode number is 13021970.',
                                     'Show the files with inode number 13021970 and <= 3 levels deep.',
                                     'How to find the files with inode number 13021970 inside / directory? Search only till 3 levels.']}, ignore_index = True)

#77
find = find.append({'Command':      'find / -maxdepth 3 -xdev -name \'pratik.txt\'',
                    'NL Queries':   ['Search for all such files at the maximum depth of 3 from root such that its name is pratik.txt . Do not descend into directories of other file systems.',
                                     'Without descending into other FS, starting from root search for all files with name pratik and search only till the depth of 3.',
                                     'Search for all the files with name pratik.txt in root directory. Do not go beyond directory level 3.']}, ignore_index = True)

#78
find = find.append({'Command':      'find / -maxdepth 3 -anewer a.txt',
                    'NL Queries':   ['Search for all such files at the maximum depth of 3 from root such that its access time is newer than modification time of a.txt file.',
                                     'Show all those files in / which have access time newer than modification time of a.txt and have maximum depth of 3.',
                                     'How to list the files in root with access time later than the modification time of a.txt and <= 3 levels directory depth?']}, ignore_index = True)

#79
find = find.append({'Command':      'find / -maxdepth 3 -cnewer a.txt',
                    'NL Queries':   ['Search for all such files at the maximum depth of 3 from root such that its change time is newer than modification time of a.txt file.',
                                     'Show all those files in / which have change time newer than modification time of a.txt and have maximum depth of 3.',
                                     'How to list the files in root with change time later than modification time of a.txt and <= 3 levels directory depth?']}, ignore_index = True)

#80
find = find.append({'Command':      'find / -mindepth 4 -not -name \'*.log\'',
                    'NL Queries':   ['Search for all the files in / directory at a minimum depth of 4 so that the name does not end with .log .',
                                     'Display all the files with name not ending with .log in root folder. Do not search in less than 4 directories deep.',
                                     'How to find all the files in / whose names do not end with .log and do not list files < 4 directories deep?']}, ignore_index = True)

#81
find = find.append({'Command':      'find / -mindepth 4 -not -iname \'*.log\'',
                    'NL Queries':   ['Search for all the files in / directory at a minimum depth of 4 so that the name does not end with .log , case-insensitively.',
                                     'Display all the files with name not ending with .log in root folder. Do not search in less than 4 directories deep. While matching do not consider case.',
                                     'How to find all the files in / whose names do not end with .log and do not list files < 4 directories deep? Consider upper and lower case as same.']}, ignore_index = True)

#82
find = find.append({'Command':      'find / -mindepth 6 -name \'*.cpp\' -o -name \'*.cc\'',
                    'NL Queries':   ['Search for all the files in root directory at minimum depth of 6 whose name either end with .cpp or .cc .',
                                     'Show all the files under root which have either .cpp or .cc extension and are at least 6 level deeper from / .',
                                     'How to list all the files in / which end with .cpp or .cc and are >= 6 levels deep?']}, ignore_index = True)

#83
find = find.append({'Command':      'find / -mindepth 6 -iname \'*.cpp\' -o -iname \'*.cc\'',
                    'NL Queries':   ['Search for all the files in root directory at minimum depth of 6 whose name either end with .cpp or .cc .',
                                     'Show all the files under root which have either .cpp or .cc extension and are at least 6 level deeper from / . Compare names case-insensitively.',
                                     'How to list all the files in / which end with .cpp or .cc and are >= 6 levels deep? Do case insensitive comparison.']}, ignore_index = True)

#84
find = find.append({'Command':      'find / -mindepth 2 -type f -name \'*.pl\'',
                    'NL Queries':   ['Search for all those files at a minimum depth of 2 from root directory whose name ends with .pl and are regular files.',
                                     'Display all the regular files with extension .pl and at least 2 directories deep.',
                                     'How to list the regular files which are at least 2 directories deep and have .pl extension?']}, ignore_index = True)

#85
find = find.append({'Command':      'find / -mindepth 2 -type f -iname \'*.pl\'',
                    'NL Queries':   ['Search for all those files at a minimum depth of 2 from root directory whose name ends with .pl , case insensitively, and are regular files.',
                                     'Display all the regular files with extension .pl and at least 2 directories deep. While checking names do not consider case sensitivity.',
                                     'How to list the regular files which are at least 2 directories deep and have .pl extension? Treat upper and lower case as same.']}, ignore_index = True)

#86
find = find.append({'Command':      'find / -mindepth 2 -type d -name \'*.pl\'',
                    'NL Queries':   ['Search for all those files at a minimum depth of 2 from root directory whose name ends with .pl and are directories.',
                                     'Display all the directories with extension .pl and at least 2 directories deep.',
                                     'How to list the directories which are at least 2 directories deep and have .pl extension?']}, ignore_index = True)

#87
find = find.append({'Command':      'find / -mindepth 2 -type d -iname \'*.pl\'',
                    'NL Queries':   ['Search for all those files at a minimum depth of 2 from root directory whose name ends with .pl , case insensitively, and are directories.',
                                     'Display all the directories with extension .pl and at least 2 directories deep. While checking names do not consider case sensitivity.',
                                     'How to list the directories which are at least 2 directories deep and have .pl extension? Treat upper and lower case as same.']}, ignore_index = True)

#88
find = find.append({'Command':      'find / -mindepth 3 -perm 0777',
                    'NL Queries':   ['Search for all those files which are at minimum depth 3 from root directory and has permission 0777 .',
                                     'How to locate all the files under root with permission 777 and at minimum directory depth of 3?',
                                     'List the files in / directory with all permission bits on and at least 3 directories deep.']}, ignore_index = True)

#89
find = find.append({'Command':      'find / -mindepth 4 -user pratik',
                    'NL Queries':   ['Search for all the files at a minimum depth of 4 from root directory whose owner is pratik .',
                                     'Which files are owned by pratik and are at least 4 directories inside root ?',
                                     'Show the files inside / with owner pratik and minimum depth of 4 folders.']}, ignore_index = True)

#90
find = find.append({'Command':      'find / -mindepth 4 -group pratik',
                    'NL Queries':   ['Search for all the files at a minimum depth of 4 from root directory belonging to group pratik .',
                                     'Which files are owned by group named pratik and are at least 4 directories inside root ?',
                                     'Show the files inside / with group owner pratik and minimum depth of 4 folders.']}, ignore_index = True)

#91
find = find.append({'Command':      'find / -mindepth 3 -atime 1',
                    'NL Queries':   ['Find all such files at the minimum depth of 3 from root directory which was accessed 1 day back.',
                                     'List all such files under root directory which were accessed one day ago and at least 3 directories deep.',
                                     'How to display all such files under / which have access time stamp of 1 day back and at least 3 levels of directories deep?']}, ignore_index = True)

#92
find = find.append({'Command':      'find / -mindepth 3 -ctime 1',
                    'NL Queries':   ['Find all such files at the minimum depth of 3 from root directory which was changed 1 day back.',
                                     'List all such files under root directory which were changed one day ago and at least 3 directories deep.',
                                     'How to display all such files under / which have change time stamp of 1 day back and at least 3 levels of directories deep?']}, ignore_index = True)

#93
find = find.append({'Command':      'find / -mindepth 3 -mtime 1',
                    'NL Queries':   ['Find all such files at the minimum depth of 3 from root directory which was modified 1 day back.',
                                     'List all such files under root directory which were modified one day ago and at least 3 directories deep.',
                                     'How to display all such files under / which have modification time stamp of 1 day back and at least 3 levels of directories deep?']}, ignore_index = True)

#94
find = find.append({'Command':      'find / -mindepth 3 -amin 100',
                    'NL Queries':   ['Find all such files at the minimum depth of 3 from root directory which was accessed 100 minutes back.',
                                     'List all such files under root directory which were accessed 100 minutes ago and at least 3 directories deep.',
                                     'How to display all such files under / which have access time stamp of 100 minutes back and at least 3 levels of directories deep?']}, ignore_index = True)

#95
find = find.append({'Command':      'find / -mindepth 3 -cmin 100',
                    'NL Queries':   ['Find all such files at the minimum depth of 3 from root directory which was changed 100 minutes back.',
                                     'List all such files under root directory which were changed 100 minutes ago and at least 3 directories deep.',
                                     'How to display all such files under / which have change time stamp of 100 minutes back and at least 3 levels of directories deep?']}, ignore_index = True)

#96
find = find.append({'Command':      'find / -mindepth 3 -mmin 1',
                    'NL Queries':   ['Find all such files at the minimum depth of 3 from root directory which was modified 100 minutes back.',
                                     'List all such files under root directory which were modified 100 minutes ago and at least 3 directories deep.',
                                     'How to display all such files under / which have modification time stamp of 100 minutes back and at least 3 levels of directories deep?']}, ignore_index = True)

#97
find = find.append({'Command':      'find / -mindepth 4 -size 10M',
                    'NL Queries':   ['Find all such files at the minimum depth of 4 from root directory which has size 10MB .',
                                     'Show all the files in / with size 10 MB and are at least 4 levels deep from the root.',
                                     'How to list all the files under root with size 10 MB and more than or equal to 4 directories deep.']}, ignore_index = True)

#98
find = find.append({'Command':      'find / -mindepth 3 -empty',
                    'NL Queries':   ['Search for all such files at the minimum depth of 3 from root such that it is empty.',
                                     'Which files are empty inside / directory and at minimum depth of 3 levels?',
                                     'Show the empty files which are at least 3 directories in depth.']}, ignore_index = True)

#99
find = find.append({'Command':      'find / -mindepth 3 -newer a.txt',
                    'NL Queries':   ['Search for all such files at the minimum depth of 3 from root such that its modification time is newer than a.txt file.',
                                     'Show all the files inside / with modification time newer than that of a.txt file.',
                                     'How to list the files inside / directory which are at least 3 directory level deep and are modified later than a.txt ?']}, ignore_index = True)

#100
find = find.append({'Command':      'find / -mindepth 3 -inum 13021970',
                    'NL Queries':   ['Search for all such files at the minimum depth of 3 from root such that its inode number is 13021970.',
                                     'Show all the files hardlinked to inode number 13021970 and are at minimum 3 directories inside.',
                                     'How can I locate all the files with 13021970 as inode number? Display only those which are three directory levels deep.']}, ignore_index = True)

#101
find = find.append({'Command':      'find / -mindepth 3 -xdev -name \'pratik.txt\'',
                    'NL Queries':   ['Search for all such files at the minimum depth of 3 from root such that its name is pratik.txt . Do not descend into directories of other file systems.',
                                     'Without descending into other FS, starting from root search for all files with name pratik and search only after or on the depth of 3.',
                                     'Search for all the files with name pratik.txt in root directory. Do not search below directory level 3.']}, ignore_index = True)

#102
find = find.append({'Command':      'find / -mindepth 3 -anewer a.txt',
                    'NL Queries':   ['Search for all such files at the minimum depth of 3 from root such that its access time is newer than modification time of a.txt file.',
                                     'Show all those files in / which have access time newer than modification time of a.txt and have mainimum depth of 3.',
                                     'How to list the files in root with access time later than the modification time of a.txt and >= 3 levels directory depth?']}, ignore_index = True)

#103
find = find.append({'Command':      'find / -mindepth 3 -cnewer a.txt',
                    'NL Queries':   ['Search for all such files at the minimum depth of 3 from root such that its change time is newer than modification time of a.txt file.',
                                     'Show all those files in / which have change time newer than modification time of a.txt and have minimum depth of 3.',
                                     'How to list the files in root with change time later than modification time of a.txt and = 3 levels directory depth?']}, ignore_index = True)

#104
find = find.append({'Command':      'find . -not -name \'*.cpp\' -not -name \'*.pl\'',
                    'NL Queries':   ['Search for all those files in current directory whose name does not end with .cpp or .pl .',
                                     'List all the files which do not end with .cpp or .pl under pwd.',
                                     'Except for the files ending with .cpp or .pl , show each files inside current folder.']}, ignore_index = True)

#105
find = find.append({'Command':      'find . -not -iname \'*.cpp\' -not -iname \'*.pl\'',
                    'NL Queries':   ['Search for all those files in current directory whose name does not end with .cpp or .pl when compared case-insensitively.',
                                     'List all the files which do not end with .cpp or .pl under pwd. Match names of files using case insensitive comparison.',
                                     'Except for the files ending with .cpp or .pl , show each files inside current folder. Use case insensitive matching.']}, ignore_index = True)

#106
find = find.append({'Command':      'find . -type f -not -name \'*.py\'',
                    'NL Queries':   ['Search for all those files in current directory whose names do not end with .py and are regular files.',
                                     'List all the regular files with names not ending with .py in current working directory.',
                                     'Show all the regular files in pwd which do not have .py extension.']}, ignore_index = True)

#107
find = find.append({'Command':      'find . -type f -not -iname \'*.py\'',
                    'NL Queries':   ['Search for all those files in current directory whose names do not end with .py , case-insensitively, and are regular files.',
                                     'List all the regular files with names not ending with .py in current working directory. Use case-insensitive comparison for file names.',
                                     'Show all the regular files in pwd which do not have .py extension. Perform case insensitive file name checking.']}, ignore_index = True)

#108
find = find.append({'Command':      'find . -type d -not -name \'*py\'',
                    'NL Queries':   ['Search for all those files in current directory whose names do not end with py and are directories.',
                                     'List all the directories with names not ending with .py in current working directory.',
                                     'Show all the directories in pwd which do not have .py extension.']}, ignore_index = True)

#109
find = find.append({'Command':      'find . -type d -not -iname \'*py\'',
                    'NL Queries':   ['Search for all those files in current directory whose names do not end with py , case-insensitively, and are directories.',
                                     'List all the directories with names not ending with .py in current working directory. Use case-insensitive comparison for file names.',
                                     'Show all the directories in pwd which do not have .py extension. Perform case insensitive file name checking.']}, ignore_index = True)

#110
find = find.append({'Command':      'find . -not -perm 0755',
                    'NL Queries':   ['Search for all those files in current directory whose permission is not 0755 .',
                                     'List all the files under current directory which do not have permission as 755 .',
                                     'Display all the files in pwd with permission bits not set as 755 .']}, ignore_index = True)

#111
find = find.append({'Command':      'find . -not -user pratik',
                    'NL Queries':   ['Search for all those files in current directory whose owner in not pratik .',
                                     'list all the files not owned by pratik.',
                                     'Which files are not owned by user pratik ?']}, ignore_index = True)

#112
find = find.append({'Command':      'find . -not -group pratik',
                    'NL Queries':   ['Search for all those files in current directory whose group owner in not pratik .',
                                     'list all the files not owned by group pratik.',
                                     'Which files are not owned by group pratik ?']}, ignore_index = True)

#113
find = find.append({'Command':      'find . -not -atime 1',
                    'NL Queries':   ['Search for all those files in current directory whose access time is not 1 day back.',
                                     'Show all the files in pwd which were not accessed one day back.',
                                     'Which files were not accessed 1 day ago in current directory?']}, ignore_index = True)

#114
find = find.append({'Command':      'find . -not -ctime 1',
                    'NL Queries':   ['Search for all those files in current directory whose change time is not 1 day back.',
                                     'Show all the files in pwd which were not changed one day back.',
                                     'Which files were not changed 1 day ago in current directory?']}, ignore_index = True)

#115
find = find.append({'Command':      'find . -not -mtime 1',
                    'NL Queries':   ['Search for all those files in current directory whose modification time is not 1 day back.',
                                     'Show all the files in pwd which were not modified one day back.',
                                     'Which files were not modified 1 day ago in current directory?']}, ignore_index = True)

#116
find = find.append({'Command':      'find . -not -amin 10',
                    'NL Queries':   ['Search for all those files in current directory whose access time is not 10 minutes back.',
                                     'Which are the files which were not accessed 10 minutes back in present working directory?',
                                     'Show me the files which do not have access time stamp of ten minutes back?']}, ignore_index = True)

#117
find = find.append({'Command':      'find . -not -cmin 10',
                    'NL Queries':   ['Search for all those files in current directory whose change time is not 10 minutes back.',
                                     'Which are the files which were not changed 10 minutes back in present working directory?',
                                     'Show me the files which do not have change time stamp of ten minutes back?']}, ignore_index = True)

#118
find = find.append({'Command':      'find . -not -mmin 10',
                    'NL Queries':   ['Search for all those files in current directory whose modification time is not 10 minutes back.',
                                     'Which are the files which were not modified 10 minutes back in present working directory?',
                                     'Show me the files which do not have modification time stamp of ten minutes back?']}, ignore_index = True)

#119
find = find.append({'Command':      'find . -not -size 1M',
                    'NL Queries':   ['Search for all those files in current directory whose size is not 1MB .',
                                     'List the files with size not equal to 1 MB and present in current directory.',
                                     'Display all the files except those with size 1 megabyte.']}, ignore_index = True)

#120
find = find.append({'Command':      'find . -not -empty',
                    'NL Queries':   ['Search for all those files in current directory which are not empty.',
                                     'List all the non empty files in pwd.',
                                     'Which files in current workspace are not empty?']}, ignore_index = True)

#121
find = find.append({'Command':      'find . -not -newer b.txt',
                    'NL Queries':   ['Search for all those files in current directory whose modification time is not newer than b.txt file.',
                                     'List all the files in pwd which were not modified after b.txt was modified.',
                                     'How to locate all the files which were modified earlier than b.txt was modified? Show files from only present working directory.']}, ignore_index = True)

#122
find = find.append({'Command':      'find . -not -anewer b.txt',
                    'NL Queries':   ['Search for all those files in current directory whose access time is not newer than modification time of b.txt file.',
                                     'List all the files in pwd which were not accessed after b.txt was modified.',
                                     'How to locate all the files which were accessed earlier than b.txt was modified? Show files from only present working directory.']}, ignore_index = True)

#123
find = find.append({'Command':      'find . -not -cnewer b.txt',
                    'NL Queries':   ['Search for all those files in current directory whose change time is not newer than modification time of b.txt file.',
                                     'List all the files in pwd which were not changed after b.txt was modified.',
                                     'How to locate all the files which were changed earlier than b.txt was modified? Show files from only present working directory.']}, ignore_index = True)

#124
find = find.append({'Command':      'find . -not -inum 06091994',
                    'NL Queries':   ['Search for all those files in current directory whose inode number is not 06091994 .',
                                     'How to show the files which do not have inode number equal to 06091994 and are inside current folder?',
                                     'List all such files inside pwd and inode number 06091994 .']}, ignore_index = True)

#125
find = find.append({'Command':      'find /dev/ -type c -o -type b',
                    'NL Queries':   ['Find all the special char and block files in /dev directory.',
                                     'Show all the files inside /dev which are either char or block device files.',
                                     'How to list all the char and block device files inside /dev ?']}, ignore_index = True)

#126
find = find.append({'Command':      'find /dev/ -perm 0755 -o -perm 0765',
                    'NL Queries':   ['Find all the files in /dev/ directory whose permission is either 0755 or 0765 .',
                                     'Locate all the files in /dev with 755 or 765 permission bits.',
                                     'How to locate files in /dev/ with either permission bits set to 765 or 755 ?']}, ignore_index = True)

#127
find = find.append({'Command':      'find /dev/ -user miranda -o -user kerr',
                    'NL Queries':   ['Find all the files in /dev/ belonging to user miranda or kerr directory.',
                                     'List all the files inside /dev/ belonging to the user miranda or kerr .',
                                     'How to display the files owned by miranda or kerr in /dev ?']}, ignore_index = True)

#128
find = find.append({'Command':      'find /dev/ -group miranda -o -group kerr',
                    'NL Queries':   ['Find all the files in /dev/ belonging to group miranda or kerr directory.',
                                     'List all the files inside /dev/ belonging to the group miranda or kerr .',
                                     'How to display the files owned by group miranda or group kerr in /dev ?']}, ignore_index = True)

#129
find = find.append({'Command':      'find /dev/ -atime 1 -o -atime 8',
                    'NL Queries':   ['Find all the files in /dev/ which was last accessed 1 or 8 days back.',
                                     'Display the files in /dev/ which were accessed either 1 day or 8 days back.',
                                     'How to find the files with access timestamp set to 1 or 8 days back?']}, ignore_index = True)

#130
find = find.append({'Command':      'find /dev/ -mtime 1 -o -mtime 8',
                    'NL Queries':   ['Find all the files in /dev/ which was last modified 1 or 8 days back.',
                                     'Display the files in /dev/ which were modified either 1 day or 8 days back.',
                                     'How to find the files with modified timestamp set to 1 or 8 days back?']}, ignore_index = True)

#131
find = find.append({'Command':      'find /dev/ -ctime 1 -o -ctime 8',
                    'NL Queries':   ['Find all the files in /dev/ which was last changed 1 or 8 days back.',
                                     'Display the files in /dev/ which were changed either 1 day or 8 days back.',
                                     'How to find the files with change timestamp set to 1 or 8 days back?']}, ignore_index = True)

#132
find = find.append({'Command':      'find /dev/ -amin 1 -o -amin 8',
                    'NL Queries':   ['Find all the files in /dev/ which was last accessed 1 or 8 minutes back.',
                                     'Display the files in /dev/ which were accessed either 1 minute or 8 minutes back.',
                                     'How to find the files with access timestamp set to 1 or 8 minutes back?']}, ignore_index = True)

#133
find = find.append({'Command':      'find /dev/ -mmin 1 -o -mmin 8',
                    'NL Queries':   ['Find all the files in /dev/ which was last modified 1 or 8 minutes back.',
                                     'Display the files in /dev/ which were modified either 1 minute or 8 minutes back.',
                                     'How to find the files with modification timestamp set to 1 or 8 minutes back?']}, ignore_index = True)

#134
find = find.append({'Command':      'find /dev/ -cmin 1 -o -cmin 8',
                    'NL Queries':   ['Find all the files in /dev/ which was last changed 1 or 8 minutes back.',
                                     'Display the files in /dev/ which were changed either 1 minute or 8 minutes back.',
                                     'How to find the files with change timestamp set to 1 or 8 minutes back?']}, ignore_index = True)

#135
find = find.append({'Command':      'find /etc/ -size 1M -o -size 10M',
                    'NL Queries':   ['Find all the files in /etc/ directory with size either 1MB or 10MB .',
                                     'List all the files in /etc/ which are 1MB or 10MB in size.',
                                     'How to display all the files with size 1 or 10 megabyte ?']}, ignore_index = True)

#136
find = find.append({'Command':      'find /home/ -newer a.txt -o -anewer a.txt',
                    'NL Queries':   ['Search for all the files in /home/ such that either access or modification time is newer than a.txt file.',
                                     'Show the files in /home/ which were accessed or modified after a.txt was modified.',
                                     'How to display the files in /home with access or modification timestamp later than modification time of a.txt .']}, ignore_index = True)

#137
find = find.append({'Command':      'find /home/ -cnewer a.txt -o -anewer a.txt',
                    'NL Queries':   ['Search for all the files in /home/ such that either change or access time is newer than a.txt file.',
                                     'Show the files in /home/ which were accessed or changed after a.txt was modified.',
                                     'How to display the files in /home with access or change timestamp later than modification time of a.txt .']}, ignore_index = True)

#138
find = find.append({'Command':      'find /home/ -cnewer a.txt -o -newer a.txt',
                    'NL Queries':   ['Search for all the files in /home/ such that either change or modification time is newer than a.txt file.',
                                     'Show the files in /home/ which were changed or modified after a.txt was modified.',
                                     'How to display the files in /home with change or modification timestamp later than modification time of a.txt .']}, ignore_index = True)

#139
find = find.append({'Command':      'find . -inum 12345678 -o -inum 23456789',
                    'NL Queries':   ['Search for all the files in current directory whose inode number is either 12345678 or 23456789 .',
                                     'Find the files with inode number 12345678 or 2345678 in PWD.',
                                     'How to locate all the files with inode number either equal to 12345678 or 23456789 in current workspace?']}, ignore_index = True)

#140
find = find.append({'Command':      'find . -type f -perm 0765',
                    'NL Queries':   ['Search for all those regular files in current directory whose permissions are 0765 .',
                                     'List all the regular files with permission 765 in current directory.',
                                     'Which regular files in current workspace have 765 permission?']}, ignore_index = True)

#141
find = find.append({'Command':      'find . -type f -user snyder',
                    'NL Queries':   ['Search for all those regular files in current directory whose owner is snyder .',
                                     'How to find all the regular files owned by snyder in pwd?',
                                     'List all the regular files in present working folder which are owned by snyder.']}, ignore_index = True)

#142
find = find.append({'Command':      'find /home/model/ -type f -group sarah',
                    'NL Queries':   ['Search for all the regular files in /home/model/ directory whose group owner is sarah .',
                                     'How to list the regular files with group sarah and present inside /home/model ?',
                                     'Enumerate all the regular files in /home/model/ with group owner sarah .']}, ignore_index = True)

#143
find = find.append({'Command':      'find /home/projects/ -type f -atime 1',
                    'NL Queries':   ['Search for all those regular files in /home/projects/ directory which were accessed 1 day back.',
                                     'How to locate all the regular files with access timestamp of 1 day back? Show file inside /home/projects/ .',
                                     'Display the regular files in /home/projects which were accessed 1 day ago.']}, ignore_index = True)

#144
find = find.append({'Command':      'find /home/projects/ -type f -mtime 1',
                    'NL Queries':   ['Search for all those regular files in /home/projects/ directory which were modified 1 day back.',
                                     'How to locate all the regular files with modification timestamp of 1 day back? Show file inside /home/projects/ .',
                                     'Display the regular files in /home/projects which were modified 1 day ago.']}, ignore_index = True)

#145
find = find.append({'Command':      'find /home/projects/ -type f -ctime 1',
                    'NL Queries':   ['Search for all those regular files in /home/projects/ directory which were modified 1 day back.',
                                     'How to locate all the regular files with change timestamp of 1 day back? Show file inside /home/projects/ .',
                                     'Display the regular files in /home/projects which were changed 1 day ago.']}, ignore_index = True)

#146
find = find.append({'Command':      'find /home/projects/ -type f -amin 1',
                    'NL Queries':   ['Search for all those regular files in /home/projects/ directory which were accessed 1 minute back.',
                                     'How to locate all the regular files with access timestamp of 1 minute back? Show file inside /home/projects/ .',
                                     'Display the regular files in /home/projects which were accessed 1 minute ago.']}, ignore_index = True)

#147
find = find.append({'Command':      'find /home/projects/ -type f -cmin 1',
                    'NL Queries':   ['Search for all those regular files in /home/projects/ directory which were changed 1 minute back.',
                                     'How to locate all the regular files with change timestamp of 1 minute back? Show file inside /home/projects/ .',
                                     'Display the regular files in /home/projects which were changed 1 minute ago.']}, ignore_index = True)

#148
find = find.append({'Command':      'find /home/projects/ -type f -mmin 1',
                    'NL Queries':   ['Search for all those regular files in /home/projects/ directory which were modified 1 minute back.',
                                     'How to locate all the regular files with modification timestamp of 1 minute back? Show file inside /home/projects/ .',
                                     'Display the regular files in /home/projects which were modified 1 minute ago.']}, ignore_index = True)

#149
find = find.append({'Command':      'find /home/ -type f -size 1k',
                    'NL Queries':   ['Search for all the regular files in /home/ directory whose size on disk is 1KB .',
                                     'How to find the regular files with size exceeding 1 KB in home ?',
                                     'Show all the regular files inside /home/ which have size >= 1 KB.']}, ignore_index = True)

#150
find = find.append({'Command':      'find . -type f -empty',
                    'NL Queries':   ['Search for all the empty regular files in current directory.',
                                     'List all the empty regular files of current folder.',
                                     'How to locate all the empty regular files in pwd ?']}, ignore_index = True)

#151
find = find.append({'Command':      'find . -type f -newer abc.txt',
                    'NL Queries':   ['Search for all the regular files in current directory which have modification time newer than abc.txt .',
                                     'Show all the regular files which were modified later than abc.txt was modified in pwd.',
                                     'How to display the files which were modified after abc.txt was modified? Show files from only present directory.']}, ignore_index = True)

#152
find = find.append({'Command':      'find . -type f -cnewer abc.txt',
                    'NL Queries':   ['Search for all the regular files in current directory which have change time newer than modification time of abc.txt .',
                                     'Show all the regular files which were changed later than abc.txt was modified in pwd.',
                                     'How to display the regular files which were changed after abc.txt was modified? Show files from only present directory.']}, ignore_index = True)

#153
find = find.append({'Command':      'find . -type d -user snyder',
                    'NL Queries':   ['Search for all those directories in current directory whose owner is snyder .',
                                     'How to find all the directories owned by snyder in pwd?',
                                     'List all the directories in present working folder which are owned by snyder.']}, ignore_index = True)

#154
find = find.append({'Command':      'find /home/model/ -type d -group sarah',
                    'NL Queries':   ['Search for all the directories in /home/model/ directory whose group owner is sarah .',
                                     'How to list the directories with group sarah and present inside /home/model ?',
                                     'Enumerate all the directories in /home/model/ with group owner sarah .']}, ignore_index = True)

#155
find = find.append({'Command':      'find /home/projects/ -type d -atime 1',
                    'NL Queries':   ['Search for all those directories in /home/projects/ directory which were accessed 1 day back.',
                                     'How to locate all the directories with access timestamp of 1 day back? Show file inside /home/projects/ .',
                                     'Display the directories in /home/projects which were accessed 1 day ago.']}, ignore_index = True)

#156
find = find.append({'Command':      'find /home/projects/ -type d -mtime 1',
                    'NL Queries':   ['Search for all those directories in /home/projects/ directory which were modified 1 day back.',
                                     'How to locate all the directories with modification timestamp of 1 day back? Show file inside /home/projects/ .',
                                     'Display the directories in /home/projects which were modified 1 day ago.']}, ignore_index = True)

#157
find = find.append({'Command':      'find /home/projects/ -type d -ctime 1',
                    'NL Queries':   ['Search for all those directories in /home/projects/ directory which were modified 1 day back.',
                                     'How to locate all the directories with change timestamp of 1 day back? Show file inside /home/projects/ .',
                                     'Display the directories in /home/projects which were changed 1 day ago.']}, ignore_index = True)

#158
find = find.append({'Command':      'find /home/projects/ -type d -amin 1',
                    'NL Queries':   ['Search for all those directories in /home/projects/ directory which were accessed 1 minute back.',
                                     'How to locate all the directories with access timestamp of 1 minute back? Show file inside /home/projects/ .',
                                     'Display the directories in /home/projects which were accessed 1 minute ago.']}, ignore_index = True)

#159
find = find.append({'Command':      'find /home/projects/ -type d -cmin 1',
                    'NL Queries':   ['Search for all those directories in /home/projects/ directory which were changed 1 minute back.',
                                     'How to locate all the directories with change timestamp of 1 minute back? Show file inside /home/projects/ .',
                                     'Display the directories in /home/projects which were changed 1 minute ago.']}, ignore_index = True)

#160
find = find.append({'Command':      'find /home/projects/ -type d -mmin 1',
                    'NL Queries':   ['Search for all those directories in /home/projects/ directory which were modified 1 minute back.',
                                     'How to locate all the directories with modification timestamp of 1 minute back? Show file inside /home/projects/ .',
                                     'Display the directories in /home/projects which were modified 1 minute ago.']}, ignore_index = True)

#161
find = find.append({'Command':      'find /home/ -type d -size +1k',
                    'NL Queries':   ['Search for all the directories in /home/ directory whose size on disk is greater than 1KB .',
                                     'How to find the directories with size exceeding 1 KB in home ?',
                                     'Show all the directories inside /home/ which have size >= 1 KB.']}, ignore_index = True)

#162
find = find.append({'Command':      'find . -type d -empty',
                    'NL Queries':   ['Search for all the empty directories in current directory.',
                                     'List all the empty directories of current folder.',
                                     'How to locate all the empty folders in pwd ?']}, ignore_index = True)

#163
find = find.append({'Command':      'find . -type d -newer abc.txt',
                    'NL Queries':   ['Search for all the directories in current directory which have modification time newer than abc.txt .',
                                     'Show all the directories which were modified later than abc.txt was modified in pwd.',
                                     'How to display the files which were modified after abc.txt was modified? Show files from only present directory.']}, ignore_index = True)

#164
find = find.append({'Command':      'find . -type d -cnewer abc.txt',
                    'NL Queries':   ['Search for all the directories in current directory which have change time newer than modification time of abc.txt .',
                                     'Show all the directories which were changed later than abc.txt was modified in pwd.',
                                     'How to display the directories which were changed after abc.txt was modified? Show files from only present directory.']}, ignore_index = True)

#165
find = find.append({'Command':      'find . -type d -anewer abc.txt',
                    'NL Queries':   ['Search for all the directories in current directory which have access time newer than modification time of abc.txt .',
                                     'Show all the directories which were accessed later than abc.txt was modified in pwd.',
                                     'How to display the files which were accessed after abc.txt was modified? Show files from only present directory.']}, ignore_index = True)

#166
find = find.append({'Command':      'find /dev/ -perm 0712 -user guddu',
                    'NL Queries':   ['Search for all the files in /dev/ directory whose permission is 0712 and owner is guddu .',
                                     'Show the files whose user owner is wheel and has permission 555 in /dev directory.',
                                     'How to find all the files in /dev folder with file permissions set as 0555 ? Owner should be guddu .']}, ignore_index = True)

#167
find = find.append({'Command':      'find /dev/ -perm 0555 -group wheel',
                    'NL Queries':   ['Search for all the files in /dev/ directory with permission 0555 and group owner is wheel .',
                                     'Show the files whose group owner is wheel and has permission 555 in /dev directory.',
                                     'How to find all the files in /dev folder with file permissions set as 0555 ? Group owner should be wheel.']}, ignore_index = True)

#168
find = find.append({'Command':      'find . -perm 0755 -atime 1',
                    'NL Queries':   ['Search for all the files in current directory with permission 0755 and was accessed 1 day ago.',
                                     'List the files in pwd which were accessed 1 day ago and have permission bits as 755.',
                                     'How to locate all the files with default permissions for a directory in current directory? Show only those files which were accessed 1 day back.']}, ignore_index = True)

#169
find = find.append({'Command':      'find . -perm 0755 -mtime 1',
                    'NL Queries':   ['Search for all the files in current directory with permission 0755 and was modified 1 day ago.',
                                     'List the files in pwd which were modified 1 day ago and have permission bits as 755.',
                                     'How to locate all the files with default permissions for a directory in current directory? Show only those files which were modified 1 day back.']}, ignore_index = True)

#170
find = find.append({'Command':      'find . -perm 0755 -ctime 1',
                    'NL Queries':   ['Search for all the files in current directory with permission 0755 and was changed 1 day ago.',
                                     'List the files in pwd which were changed 1 day ago and have permission bits as 755.',
                                     'How to locate all the files with default permissions for a directory in current directory? Show only those files which were changed 1 day back.']}, ignore_index = True)

#171
find = find.append({'Command':      'find . -perm 0755 -amin 1',
                    'NL Queries':   ['Search for all the files in current directory with permission 0755 and was accessed 1 minute ago.',
                                     'List the files in pwd which were changed 1 minute ago and have permission bits as 755.',
                                     'How to locate all the files with default permissions for a directory in current directory? Show only those files which were accessed 1 minute back.']}, ignore_index = True)

#172
find = find.append({'Command':      'find . -perm 0755 -mmin 1',
                    'NL Queries':   ['Search for all the files in current directory with permission 0755 and was modified 1 minute ago.',
                                     'List the files in pwd which were modified 1 minute ago and have permission bits as 755.',
                                     'How to locate all the files with default permissions for a directory in current directory? Show only those files which were modified 1 minute back.']}, ignore_index = True)

#173
find = find.append({'Command':      'find . -perm 0755 -cmin 1',
                    'NL Queries':   ['Search for all the files in current directory with permission 0755 and was changed 1 minute ago.',
                                     'List the files in pwd which were changed 1 minute ago and have permission bits as 755.',
                                     'How to locate all the files with default permissions for a directory in current directory? Show only those files which were changed 1 minute back.']}, ignore_index = True)

#174
find = find.append({'Command':      'find . -perm 0765 -size 10k',
                    'NL Queries':   ['Search for all the files whose size is 10KB and has permission set as 0765 .',
                                     'How to display all 10 KB files with 765 permission?',
                                     'Show the files having 765 as permission bits and size of 10 kilobytes.']}, ignore_index = True)

#175
find = find.append({'Command':      'find . -perm 0777 -empty',
                    'NL Queries':      ['Search for all the files having permission 777 and is empty.',
                                     'How to search for empty files with permission 777 in pwd?',
                                     'List all the files with 777 permission bits and present inside current workplace.']}, ignore_index = True)

#176
find = find.append({'Command':      'find . -perm 0756 -newer termin',
                    'NL Queries':   ['Search for all the files with permission 0756 and modification time newer than that of termin in current workspace.',
                                     'List the files with permission 756 and modified later than termin in pwd.',
                                     'How to display the files in current folder with 756 as permission bits and modified later than termin ?']}, ignore_index = True)

#177
find = find.append({'Command':      'find . -perm 0756 -anewer termin',
                    'NL Queries':   ['Search for all the files with permission 0756 and access time newer than access time of termin in present directory.',
                                     'List the files with permission 756 and access time after modification time of termin in pwd.',
                                     'How to display the files in current folder with 756 as permission bits and accessed later than termin was modified?']}, ignore_index = True)

#178
find = find.append({'Command':      'find . -perm 0756 -cnewer termin',
                    'NL Queries':   ['Search for all the files with permission 0756 and change time newer than access time of termin in current workplace.',
                                     'List the files with permission 756 and change time after modification time of termin in pwd.',
                                     'How to display the files in current folder with 756 as permission bits and changed later than termin was modified?']}, ignore_index = True)

#179
find = find.append({'Command':      'find . -perm 0666 -size 1G',
                    'NL Queries':   ['Search for all the files whose permission is 0666 and size is 1GB .',
                                     'Find the files with size 1 gigabyte and permission 666 in pwd.',
                                     'How to locate files in current directory with permission bits 666 and size 1 GB?']}, ignore_index = True)

#180
find = find.append({'Command':      'find . -perm 0775 -empty',
                    'NL Queries':   ['Search for all the files whose permission is 0775 and are empty in pwd.',
                                     'How to find all the 775 permission files in current working folder and are empty?',
                                     'Find the files with permission bits 775 and are empty. Search for only those files in current folder.']}, ignore_index = True)

#181
find = find.append({'Command':      'find . -perm 0745 -newer tilda.txt',
                    'NL Queries':   ['Search for all the files whose permission is 0745 and has modification time newer than tilda.txt file.',
                                     'How to list all the files in present working workplace with modification time newer than that of tilda.txt and permission 745 ?',
                                     'Show the files with 745 permission and modification timestamp later than modification time of tilda.txt in present directory.']}, ignore_index = True)

#182
find = find.append({'Command':      'find . -perm 0745 -cnewer tilda.txt',
                    'NL Queries':   ['Search for all the files whose permission is 0745 and has change time newer than the modification time of tilda.txt file.',
                                     'How to list all the files in present working workplace with change time newer than modification time of tilda.txt and permission 745 ?',
                                     'Show the files with 745 permission and change timestamp later than modification time of tilda.txt in present directory.']}, ignore_index = True)

#183
find = find.append({'Command':      'find . -perm 0745 -anewer tilda.txt',
                    'NL Queries':   ['Search for all the files whose permission is 0745 and has access time newer than the modification time of tilda.txt file.',
                                     'How to list all the files in present working workplace with access time newer than modification time of tilda.txt and permission 745 ?',
                                     'Show the files with 745 permission and access timestamp later than modification time of tilda.txt in present directory.']}, ignore_index = True)

#184
find = find.append({'Command':      'find . -user pratik -group wheel',
                    'NL Queries':   ['Search for all the files in current directory with owner pratik and group owner wheel .',
                                     'List all the files with owner pratik and group owner wheel in PWD.',
                                     'How to list the files which are owned by pratik and the group is wheel in current working directory?']}, ignore_index = True)

#185
find = find.append({'Command':      'find /manga/ -user soul -atime 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose owner is soul and access time was 5 days back.',
                                     'Which files were accessed 5 days ago in /manga/ folder? Only show those files owned by user named soul.',
                                     'Locate all files with access timestamp of nearly 5 days ago and the user owner is soul in /manga/ .']}, ignore_index = True)

#186
find = find.append({'Command':      'find /manga/ -user soul -ctime 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose owner is soul and change time was 5 days back.',
                                     'Which files were changed 5 days ago in /manga/ folder? Only show those files owned by user named soul.',
                                     'Locate all files with change timestamp of nearly 5 days ago and the user owner is soul in /manga folder.']}, ignore_index = True)

#187
find = find.append({'Command':      'find /manga/ -user soul -mtime 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose owner is soul and modification time was 5 days back.',
                                     'Which files were modified 5 days ago in /manga/ folder? Only show those files owned by user named soul.',
                                     'Locate all files with modification timestamp of nearly 5 days ago and the user owner is soul in /manga directory.']}, ignore_index = True)

#188
find = find.append({'Command':      'find /manga/ -user soul -mmin 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose owner is soul and access time was 5 minutes back.',
                                     'Which files were modified 5 minutes ago in /manga/ folder? Only show those files owned by user named soul.',
                                     'Locate all files with modification timestamp of nearly 5 minutes ago and the user owner is soul in /manga folder.']}, ignore_index = True)

#189
find = find.append({'Command':      'find /manga/ -user soul -cmin 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose owner is soul and change time was 5 minutes back.',
                                     'Which files were changed 5 minutes ago in /manga/ folder? Only show those files owned by user named soul.',
                                     'Locate all files with change timestamp of nearly 5 minutes ago and the user owner is soul in /manga folder.']}, ignore_index = True)

#190
find = find.append({'Command':      'find /manga/ -user soul -amin 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose owner is soul and access time was 5 minutes back.',
                                     'Which files were accessed 5 minutes ago in /manga/ folder? Only show those files owned by user named soul.',
                                     'Locate all files with access timestamp of nearly 5 minutes ago and the user owner is soul in /manga/ .']}, ignore_index = True)

#191
find = find.append({'Command':      'find /manga/ -user soul -newer xyz.txt',
                    'NL Queries':   ['Search for all those files in /manga/ directory whose owner is soul and has modification time newer than xyz.txt file.',
                                     'How to search for the files in /manga folder which were modified after xyz.txt and owned by user, soul ?',
                                     'List all the files which are owned by user named soul and have modification timestamp later than that of xyz.txt file. Search in /manga folder .']}, ignore_index = True)

#192
find = find.append({'Command':      'find /manga/ -user soul -anewer xyz.txt',
                    'NL Queries':   ['Search for all those files in /manga/ directory whose owner is soul and has access time newer than modification time of xyz.txt file.',
                                     'How to search for the files in /manga folder with access time later than modification time of xyz.txt and owned by user, soul ?',
                                     'List all the files which are owned by user named soul and have access timestamp later than the modification timestamp of xyz.txt file. Search in /manga .']}, ignore_index = True)

#193
find = find.append({'Command':      'find /manga/ -user soul -cnewer xyz.txt',
                    'NL Queries':   ['Search for all those files in /manga/ directory whose owner is soul and has change time newer than modification time of xyz.txt file.',
                                     'How to search for the files in /manga folder with change time later than modification time of xyz.txt and owned by user, soul ?',
                                     'List all the files which are owned by user named soul and have change timestamp later than the modification timestamp of xyz.txt file. Find in /manga/ .']}, ignore_index = True)

#194
find = find.append({'Command':      'find . -user soul -inum 87654321',
                    'NL Queries':   ['Search for all the files in current directory with user owner soul and inode number 87654321 .',
                                     'List the files with inode number 87654321 and belonging to user soul in pwd.',
                                     'How to find the files which belong to user named soul and has inode number 87654321 in current workspace?']}, ignore_index = True)

#195
find = find.append({'Command':      'find /manga/ -group soul -atime 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose group owner is soul and access time was 5 days back.',
                                     'Which files were accessed 5 days ago in /manga/ folder? Only show those files owned by group named soul.',
                                     'Locate all files with access timestamp of nearly 5 days ago and the group owner is soul in /manga/ .']}, ignore_index = True)

#196
find = find.append({'Command':      'find /manga/ -group soul -ctime 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose group owner is soul and change time was 5 days back.',
                                     'Which files were changed 5 days ago in /manga/ folder? Only show those files owned by group named soul.',
                                     'Locate all files with change timestamp of nearly 5 days ago and the group owner is soul in /manga folder.']}, ignore_index = True)

#197
find = find.append({'Command':      'find /manga/ -group soul -mtime 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose group owner is soul and modification time was 5 days back.',
                                     'Which files were modified 5 days ago in /manga/ folder? Only show those files owned by group named soul.',
                                     'Locate all files with modification timestamp of nearly 5 days ago and the group owner is soul in /manga directory.']}, ignore_index = True)

#198
find = find.append({'Command':      'find /manga/ -group soul -mmin 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose group owner is soul and modification time was 5 minutes back.',
                                     'Which files were modified 5 minutes ago in /manga/ folder? Only show those files owned by group named soul.',
                                     'Locate all files with modification timestamp of nearly 5 minutes ago and the group owner is soul in /manga folder.']}, ignore_index = True)

#199
find = find.append({'Command':      'find /manga/ -group soul -cmin 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose group owner is soul and change time was 5 minutes back.',
                                     'Which files were changed 5 minutes ago in /manga/ folder? Only show those files owned by group named soul.',
                                     'Locate all files with change timestamp of nearly 5 minutes ago and the group owner is soul in /manga folder.']}, ignore_index = True)

#200
find = find.append({'Command':      'find /manga/ -group soul -amin 5',
                    'NL Queries':   ['Search for all the files in /manga/ directory whose group owner is soul and access time was 5 minutes back.',
                                     'Which files were accessed 5 minutes ago in /manga/ folder? Only show those files owned by group named soul.',
                                     'Locate all files with access timestamp of nearly 5 minutes ago and the group owner is soul in /manga/ .']}, ignore_index = True)

#201
find = find.append({'Command':      'find /manga/ -group soul -newer xyz.txt',
                    'NL Queries':   ['Search for all those files in /manga/ directory whose group owner is soul and has modification time newer than xyz.txt file.',
                                     'How to search for the files in /manga folder which were modified after xyz.txt and owned by group, soul ?',
                                     'List all the files which are owned by group named soul and have modification timestamp later than that of xyz.txt file. Search in /manga folder .']}, ignore_index = True)

#202
find = find.append({'Command':      'find /manga/ -group soul -anewer xyz.txt',
                    'NL Queries':   ['Search for all those files in /manga/ directory whose group owner is soul and has access time newer than modification time of xyz.txt file.',
                                     'How to search for the files in /manga folder with access time later than modification time of xyz.txt and owned by group, soul ?',
                                     'List all the files which are owned by group named soul and have access timestamp later than the modification timestamp of xyz.txt file. Search in /manga .']}, ignore_index = True)

#203
find = find.append({'Command':      'find /manga/ -group soul -cnewer xyz.txt',
                    'NL Queries':   ['Search for all those files in /manga/ directory whose group owner is soul and has change time newer than modification time of xyz.txt file.',
                                     'How to search for the files in /manga folder with change time later than modification time of xyz.txt and owned by group, soul ?',
                                     'List all the files which are owned by group named soul and have change timestamp later than the modification timestamp of xyz.txt file. Find in /manga/ .']}, ignore_index = True)

#204
find = find.append({'Command':      'find . -group soul -inum 87654321',
                    'NL Queries':   ['Search for all the files in current directory with group owner soul and inode number 87654321 .',
                                     'List the files with inode number 87654321 and belonging to group soul in pwd.',
                                     'How to find the files which belong to group named soul and has inode number 87654321 in current workspace?']}, ignore_index = True)

#205
find = find.append({'Command':      'find . -atime 5 -size 1M',
                    'NL Queries':   ['Search for all the files in current directory whose access time was 5 days ago and is 1MB in size.',
                                     'Show all 1M files with access time stamp of 5 days ago in current folder.',
                                     'How to list all the files in pwd with size 1 megabytes and was accessed 5 days back?']}, ignore_index = True)

#206
find = find.append({'Command':      'find . -atime 5 -empty',
                    'NL Queries':   ['Search for all the files in current directory whose access time was 5 days ago and is empty.',
                                     'Enumerate the empty files in current folder which were accessed 5 days ago.',
                                     'Output the names of files which are empty and have been accessed 5 days ago.']}, ignore_index = True)

#207
find = find.append({'Command':      'find . -ctime 5 -size 1M',
                    'NL Queries':   ['Search for all the files in current directory whose change time was 5 days ago and is 1MB in size.',
                                     'Show all 1M files with change time stamp of 5 days ago in current folder.',
                                     'How to list all the files in pwd with size 1 megabytes and was changed 5 days back?']}, ignore_index = True)

#208
find = find.append({'Command':      'find . -ctime 5 -empty',
                    'NL Queries':   ['Search for all the files in current directory whose change time was 5 days ago and is empty.',
                                     'Enumerate the empty files in current folder which were changed 5 days ago.',
                                     'Output the names of files which are empty and have been changed 5 days ago.']}, ignore_index = True)

#209
find = find.append({'Command':      'find . -mtime 5 -size 1M',
                    'NL Queries':   ['Search for all the files in current directory whose modification time was 5 days ago and is 1MB in size.',
                                     'Show all 1M files with modification time stamp of 5 days ago in current folder.',
                                     'How to list all the files in pwd with size 1 megabytes and was modified 5 days back?']}, ignore_index = True)

#210
find = find.append({'Command':      'find . -mtime 5 -empty',
                    'NL Queries':   ['Search for all the files in current directory whose modification time was 5 days ago and is empty.',
                                     'List all empty files in pwd which were modified 5 days back.',
                                     'Show the empty files with modification time stamp of 5 days back in current directory.']}, ignore_index = True)

#211
find = find.append({'Command':      'find . -empty -newer tick.txt',
                    'NL Queries':   ['Search for all the files in current directory which are empty and have modification time newer than tick.txt file.',
                                     'Show all the empty files in pwd with modification time newer than that of tick.txt file.',
                                     'How to find the empty files with newer modification time than tick.txt file in current workspace?']}, ignore_index = True)

#212
find = find.append({'Command':      'find . -empty -cnewer tick.txt',
                    'NL Queries':   ['Search for all the files in current directory which are empty and have change time newer than modification time of tick.txt file.',
                                     'Show all the empty files in pwd with change time newer than modification time of tick.txt file.',
                                     'How to find the empty files with change time later than the modification time of tick.txt file in present working folder?']}, ignore_index = True)

#213
find = find.append({'Command':      'find . -empty -anewer tick.txt',
                    'NL Queries':   ['Search for all the files in current directory which are empty and have access time newer than modification time of tick.txt file.',
                                     'Show all the empty files in pwd with access time newer than modification time of tick.txt file.',
                                     'How to find the empty files with access time later than the modification time of tick.txt file in current directory?']}, ignore_index = True)

#214
find = find.append({'Command':      'find . -type f -anewer abc.txt',
                    'NL Queries':   ['Search for all the regular files in current directory which have access time newer than modification time of abc.txt .',
                                     'Display the regular files which are in current folder and have access time newer than modification time of abc.txt file.',
                                     'Which regular files in pwd have access timestamp later than the modification time of abc.txt ?']}, ignore_index = True)

#215
find = find.append({'Command':      'find . -type d -perm 0765',
                    'NL Queries':   ['Search for all those directories in current directory whose permissions are 0765 .',
                                     'List all the directories with permission 765 in current directory.',
                                     'Which directories in current workspace have 765 permission?']}, ignore_index = True)

#216
find = find.append({'Command':      'find --version',
                    'NL Queries':   ['Show version number of find command.',
                                     'Show authors of find command.',
                                     'Which version of find am I using?']}, ignore_index = True)

#find.to_csv('/home/ananyaraval/Documents/Thesis/Data/UNIX/csv_files/find.csv',index=False)
print find.shape
