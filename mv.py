import pandas as pd 

mv = pd.DataFrame(columns = ['Command','NL Queries'])

mv = mv.append({'Command':'mv ananya.py ananya_new.py','NL Queries':['Copy ananya.py. Rename ananya.py to ananya_new.py.',
                        'Change name to ananya.py to ananya_new.py and copy the file.',
                                'How do I create a copy of ananya.py named ananya_new.py?']},ignore_index=True)

mv = mv.append({'Command':'mv *.c backup','NL Queries':['Move all .c files from current folder to folder backup.',
                'How do I shift all .c files from this folder to a different folder named backup?',
                        'Command to move all .c files to backup folder.']},ignore_index=True)

mv = mv.append({'Command':'mv bak/* .','NL Queries':['Shift all files from back folder in this directory to this folder.',
                                        'How do I move all files from folder bak/ to this folder?',
                                        'Move all content of back folder to current directory.',
                                        'How do I shift all files and folder from bak directory to this directory?']},ignore_index=True)

#1
mv = mv.append({'Command':        'mv --backup test1.cpp dir1/test2.cpp',
                'NL Queries':     ['Move test1.cpp into directory dir1 under the name test2.cpp . Create backup at the destination.',
                                        'Shift test1.cpp to dir1 folder. Change name to test2.cpp. Make a backup in dir1.',
                                        'How do I transfer test1.cpp present in this folder to destination folder dir1 and rename it to test2.cpp along with making backup in dir1?',
                                        'Change location of test1.cpp to dir/ and rename it to test2.cpp and create a backup.']}, ignore_index = True)

#2
mv = mv.append({'Command':        'mv --backup=existing test1.cpp dir1/test2.cpp',
                'NL Queries':     ['Move test1.cpp into directory dir1 under the name test2.cpp . Create backup at the destination using existing option.',
                                'Shift test1.cpp to dir1. Rename it to test2.cpp. Take numbered backup of all files in dir1 if numbered backup already exists, otherwise take simple backup.',
                                        'How do I transfer test1.cpp to dir1/test2.cpp? Take backup of all files in destination folder using existing backup strategy of the folder?']}, ignore_index = True)

#3
mv = mv.append({'Command':        'mv --backup=t test1.cpp dir1/test2.cpp',
                'NL Queries':     ['Move test1.cpp into directory dir1 under the name test2.cpp . Create numbered backup at the destination.',
                                        'Shift test1.cpp to destination folder dir1 present in the working directory. Create numbered backup of all files in dir1. Rename the file to test2.cpp.',
                                'How do I transfer test1.cpp to destination folder dir1, rename it to test2.cpp and create numbered backup?']}, ignore_index = True)

#4
mv = mv.append({'Command':        'mv -f file1.doc fold1/file2.doc',
                'NL Queries':     ['Move file1.doc inside fold1 directory as file2.doc and overwrite without asking.',
                                'How do I shift file1.doc to folder fold1? Rename file1.doc to file2.doc and overwrite file2.doc if it exists?',
                                        'Transfer file1.doc to fold1/file2.doc and overwrite if file2.doc exists.']}, ignore_index = True)

#5
mv = mv.append({'Command':        'mv -i file1.doc fold1/file2.doc',
                'NL Queries':     ['Move file1.doc inside fold1 directory as file2.doc and do not overwrite without asking.',
                                'Change location of file1.doc to fold1 in current folder and rename it to file2.doc. If file2.doc exists, prompt before overwriting.',
                                'How do I rename file1.doc to file2.doc and move it inside fold1? If file2.doc exists in fold1, confirm before replacing?',
                                'Change location of file1.doc from current directory to fold1. If file2.doc exists in fold1, prompt before replacing. Otherwise change name of file1.doc to file2.doc.']}, ignore_index = True)

#6
mv = mv.append({'Command':        'mv -n file1.doc fold1/file2.doc',
                'NL Queries':     ['Move file1.doc inside fold1 directory as file2.doc and do not overwrite.',
                                'How do I shift file1.doc to a folder named fold1.doc and rename it to file2.doc? Do not overwrite an existing file of the same name.',
                                'Shift file1.doc to fold1. Rename to file2.doc without overwriting.'
                                'How do I change location of file1.doc present in this folder to fold1 also present in  this folder? Rename to file2.doc without replacing an existing file of the same name.']}, ignore_index = True)

#7
mv = mv.append({'Command':        'mv -b -S .bk test1.cpp dir1/test2.cpp',
                'NL Queries':     ['Move test1.cpp into directory dir1 under the name test2.cpp . Create backup at the destination with .bk extension.',
                                   'Cut test1.cpp file and paste it in dir1 folder with name test2.cpp . Create backup, if necessary, with .bk appended to the file name.',
                                   'Change the location of file test1.cpp to dir1 with name test2.cpp and create backup with .bk extension.']}, ignore_index = True)

#8
mv = mv.append({'Command':        'mv --help',
                'NL Queries':     ['Display help for mv command.',
                                   'Show help menu for mv command.',
                                   'Show usage of mv command.',
                                   'How to use mv command?',
                                   'Which options are available for mv command?']}, ignore_index = True)

#9
mv = mv.append({'Command':        'mv --version',
                'NL Queries':     ['Display details about mv command.',
                                   'Show version and author details for mv .',
                                   'Which version of mv am I using?',
                                   'Who are the authors of mv command?']}, ignore_index = True)

#10
mv = mv.append({'Command':        'mv file1.txt file2.txt dest1',
                'NL Queries':     ['Move file1.txt and file2.txt to dest1 directory.',
                                   'Shift file1.txt and file2.txt to dest1 folder.',
                                   'Change the location of files file1.txt and file2.txt to dest1 directory.']}, ignore_index = True)

#11
mv = mv.append({'Command':        'mv file1.txt file2.txt file3.txt dest1',
                'NL Queries':     ['Move file1.txt, file2.txt and file3.txt to dest1 directory.',
                                   'Cut the files file1.txt , file2.txt and file3.txt and paste it in dest1 folder.',
                                   'Transfer the files file1.txt , file2.txt and file3.txt into dest1 folder.',
                                   'Shift the files file1.txt , file2.txt and file3.txt to dest1 directory.']}, ignore_index = True)

#12
mv = mv.append({'Command':        'mv -v file1.txt dest1',
                'NL Queries':     ['Move file1.txt to dest1 directory and give me a details.',
                                   'Shift file1.txt -> dest1/file1.txt and show the progress.',
                                   'Shift the location of file1.txt from current directory to dest1 directory, which is in current directory. Also give acknowledgement of operations.',
                                   'Showing the progress of operation, transfer the file file1.txt to dest1 directory.']}, ignore_index = True)

#13
mv = mv.append({'Command':        'mv -u file1.txt dest1',
                'NL Queries':     ['Move file1.txt to dest1 directory if it is newer than the file in dest1 or is non-existant.',
                                   'If file1.txt in dest1 is older than file1.txt in pwd , file1.txt -> dest1/file1.txt .',
                                   'Shift the file file1.txt to dest1 directory if it is newer.']}, ignore_index = True)

#14
mv = mv.append({'Command':        'mv -Z file1.txt dest1',
                'NL Queries':     ['Move file1.txt to dest1 directory and change security context to default.',
                                   'Shift file1.txt -> dest1/file1.txt and update the SELinux security to default.',
                                   'Shift the location of file1.txt to dest1 folder and set SELinux security to default.']}, ignore_index = True)

#15
mv = mv.append({'Command':        'mv --strip-trailing-slashes unknown// dest1',
                'NL Queries':     ['Move unknown// to dest1 directory after removing trailing slashes.',
                                   'Shift unknown// to dest1 after removing following slashes from the unknown// .',
                                   'Change the location of unknown// to dest1/unknown// after removing trailing slashes from the source.']}, ignore_index = True)

#16
mv = mv.append({'Command':        'mv -t youtube flv',
                'NL Queries':     ['Move the flv to the directory youtube .',
                                   'Change the location of flv to youtube/flv .',
                                   'Move flv -> youtube/flv',
                                   'Shift the file flv into youtube directory.']}, ignore_index = True)

#17
mv = mv.append({'Command':        'mv -T flv ogg',
                'NL Queries':     ['Rename the file ogg to flv .',
                                   'Change the name of ogg to file flv .',
                                   'Treat flv as file. Change the file ogg to flv .']}, ignore_index = True)

#18
mv = mv.append({'Command':        'mv -bv duplicate.txt original/',
                'NL Queries':     ['Move the file duplicate.txt to directory original and create backup. Show me the details of work done.',
                                   'Move duplicate.txt -> original/duplicate.txt and create backup. Show the which were moved.',
                                   'Shift the file duplicate.txt into original directory. Create backup, if required, and show the tasks performed.']}, ignore_index = True)

#19
mv = mv.append({'Command':        'mv -v --backup=off duplicate.txt original/',
                'NL Queries':     ['Move the file duplicate.txt to directory original and do not create backup. Show me the details of work done.',
                                   'Move duplicate.txt -> original/duplicate.txt and show the operations performed. Do not create backup.',
                                   'Without creating backup move the file duplicate.txt inside original directory and display the tasks performed.']}, ignore_index = True)

#20
mv = mv.append({'Command':        'mv -v --backup=t  duplicate.txt original/',
                'NL Queries':     ['Move the file duplicate.txt to directory original and create numbered backup. Show me the details of work done.',
                                   'Creating numbered backup, move duplicate.txt file into original directory and show the tasks performed.',
                                   'Shift duplicate.txt -> original/duplicate.txt creating numbered backups and give the details of operations performed.']}, ignore_index = True)

#21
mv = mv.append({'Command':        'mv -v --backup=existing  duplicate.txt original/',
                'NL Queries':     ['Move the file duplicate.txt to directory original and create existing backup. Show me the details of work done.',
                                   'Use the existing form of backup and move duplicate.txt to original .',
                                   'Shift ./duplicate.txt -> ./original/duplicate.txt and keep the backup in existing format.']}, ignore_index = True)

#22
mv = mv.append({'Command':        'mv -buv duplicate.txt original/',
                'NL Queries':     ['Move the file duplicate.txt to directory original, if it is newer than the one in destination, and create backup. Show me the details of work done.',
                                   'If the file in destination is older then, duplicate.txt -> original/duplicate.txt and make the backup of old duplicate.txt giving the acknowledgement of tasks done.',
                                   'Shift the file duplicate.txt into original directory, if the destination file is older and make backup of the old file. Show the tasks performed.']}, ignore_index = True)

#23
mv = mv.append({'Command':        'mv -uv --backup=off duplicate.txt original/',
                'NL Queries':     ['Move the file duplicate.txt to directory original, if the destination has older file, and do not create backup. Show me the details of work done.',
                                   'Without creating backup, move the file duplicate.txt to original folder and give the account of operations done. Perform this only when destination has older version of file.',
                                   'Move duplicate.txt -> original/duplicate.txt , if the destination has older file, without maintaining a backup and display the tasks performed.']}, ignore_index = True)

#24
mv = mv.append({'Command':        'mv -uv --backup=t  duplicate.txt original/',
                'NL Queries':     ['Move the file duplicate.txt to directory original, if the destination has older file, and create numbered backup. Show me the details of work done.',
                                   'Creating numbered backups, move duplicate.txt to original folder, if the destination has an older one and display the tasks done.',
                                   'Move duplicate.txt -> original/duplicate.txt and create backup by numbering files. Perform the operations only if duplicate.txt is newer than the duplicate.txt in original directory or is absent. Give the summary of tasks performed.']}, ignore_index = True)

#25
mv = mv.append({'Command':        'mv -uv --backup=existing  duplicate.txt original/',
                'NL Queries':     ['Move the file duplicate.txt to directory original, if the destination has older file, and create existing backup. Show me the details of work done.',
                                   'If the destination file is older then, shift the file duplicate.txt to original folder and make existing style of backups. Perform tasks verbosely.',
                                   'Shift duplicate.txt -> original/duplicate.txt if the source file is newer and use existing backup format. Verbosely do the tasks.']}, ignore_index = True)

#26
mv = mv.append({'Command':         'mv -nv undo.txt redo/',
                'NL Queries':      ['Move the file undo.txt to redo directory and do not overwrite the existing file. Give me the details of operation.',
                                    'Shift the file undo.txt to redo directory without replacing any file in destination. Show the tasks performed.',
                                    'Shift undo.txt -> redo/undo.txt and do not replace any file. Display the operations performed.']}, ignore_index = True)

#27
mv = mv.append({'Command':         'mv -nZ bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Do not overwrite existing files and set SELinux security context to default settings.',
                                    'Move bleach.txt -> anime/bleach.txt and do not overwrite the destination files. Set SELinux security to default.',
                                    'Shift bleach.txt into anime folder, if no other file of same name is present in destination. Configure SELinux security to default value.']}, ignore_index = True)

#28
mv = mv.append({'Command':         'mv -iZ bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default.',
                                    'Shift bleach.txt -> anime/bleach.txt and ask to overwrite the destination files. Set SELinux security to default.',
                                    'Shift bleach.txt into anime folder, if other file of same name is present in destination ask for overwrite permission. Configure SELinux security to default value.']}, ignore_index = True)

#29
mv = mv.append({'Command':         'mv -fZ bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default.',
                                    'Move bleach.txt -> anime/bleach.txt and set SELinux security context to default. Overwrite, if required.',
                                    'Shift bleach.txt into anime folder, if other file of same name is present in destination then overwrite. Configure SELinux security to default value.']}, ignore_index = True)

#30
mv = mv.append({'Command':         'mv -iv bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Ask before overwriting files and show me the operations performed.',
                                    'Shift bleach.txt -> anime/bleach.txt and ask before overwriting. Display the tasks executed.',
                                    'Change the location of bleach.txt to anime/bleach.txt and ask for permission to overwrite files in destination. Show operations performed.']}, ignore_index = True)

#31
mv = mv.append({'Command':         'mv -fv naruto.txt anime/',
                'NL Queries':      ['Move the file naruto.txt to anime directory. Overwrite the files and show the operations performed.',
                                    'Move naruto.txt -> anime/naruto.txt overwriting the existing file and showing the completed tasks.',
                                    'Shift the file naruto.txt into anime and overwrite any existing file with same name. Display the progress.']}, ignore_index = True)

#32
mv = mv.append({'Command':         'mv -Z --backup bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Set SELinux security context to default settings. Create simple backup.',
                                    'Shift bleach.txt -> anime/bleach.txt setting SELinux security to default and creating backup.',
                                    'Change location of bleach.txt to anime and set SELinux security context to default. Create backup at destination.']}, ignore_index = True)

#33
mv = mv.append({'Command':         'mv -iZ --backup bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default. Create simple backup.',
                                    'Move bleach.txt -> anime/bleach.txt and ask to overwrite the destination files. Set SELinux security to default. Make backup of destination file.',
                                    'Shift bleach.txt into anime folder, if other file of same name is present in destination ask for overwrite permission. Configure SELinux security to default value. Make backup.']}, ignore_index = True)

#34
mv = mv.append({'Command':         'mv -fZ --backup bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default. Create simple backup.',
                                    'Move naruto.txt -> anime/bleach.txt overwriting the existing file. Take backup of destination files being overwritten.',
                                    'Shift the file bleach.txt into anime and overwrite any existing file with same name. Create backup of existing files in destination.']}, ignore_index = True)

#35
mv = mv.append({'Command':         'mv -iv --backup bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Ask before overwriting files and show me the operations performed. Create simple backup.',
                                    'Shift bleach.txt -> anime/bleach.txt and ask before overwriting. Display the tasks executed. Make backups.',
                                    'Change the location of bleach.txt to anime/bleach.txt and ask for permission to overwrite files in destination. Show operations performed. Create backup of files being overwritten.']}, ignore_index = True)

#36
mv = mv.append({'Command':         'mv -fv --backup naruto.txt anime/',
                'NL Queries':      ['Move the file naruto.txt to anime directory. Overwrite the files and show the operations performed. Create simple backup.',
                                    'Move naruto.txt -> anime/naruto.txt overwriting the existing file and showing the completed tasks. Make simple backups.',
                                    'Shift the file naruto.txt into anime and overwrite any existing file with same name. Display the progress. Save the files before overwriting.']}, ignore_index = True)

#37
mv = mv.append({'Command':         'mv -Z --strip-trailing-slashes undo//// redo/',
                'NL Queries':      ['Move undo//// to redo directory after stripping trailing slashes from source and set SElinux security context to default.',
                                    'Shift undo//// into redo/ directory after the trailing slashes have been stripped and change the SELinux security to default.',
                                    'Change the location of undo//// to redo/ after removing trailing slashes from source name. Set Security Enhanced Linux context to default.']}, ignore_index = True)

#38
mv = mv.append({'Command':         'mv -iZ --backup=existing bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default. Create existing backup.',
                                    'Move bleach.txt -> anime/bleach.txt and ask before over-writing. Use existing style of backup and set SEL security context to default.',
                                    'Change the location of bleach.txt to anime/bleach.txt and use the existing style of backup. Ask before over-writing and make SEL security context to its recommended value.']}, ignore_index = True)

#39
mv = mv.append({'Command':         'mv -fZ --backup=existing bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default. Create existing backup.',
                                    'Shift bleach.txt -> anime/bleach.txt and set SELinux security context to default. Overwrite, if required. Make existing backup format.',
                                    'Shift bleach.txt into anime folder, if other file of same name is present in destination then overwrite. Configure SELinux security to default value. Create backup of existing style.']}, ignore_index = True)

#40
mv = mv.append({'Command':         'mv -iv --backup=existing bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Ask before overwriting files and show me the operations performed. Create existing backup.',
                                    'bleach.txt -> anime/bleach.txt and ask before overwriting. Display the tasks executed. Make backups of existing type.',
                                    'Change the location of bleach.txt to anime/bleach.txt and ask for permission to overwrite files in destination. Show operations performed. Create backup of files being overwritten in the present style.']}, ignore_index = True)

#41
mv = mv.append({'Command':         'mv -fv --backup=existing naruto.txt anime/',
                'NL Queries':      ['Move the file naruto.txt to anime directory. Overwrite the files and show the operations performed. Create existing backup.',
                                    'Move naruto.txt -> anime/naruto.txt overwriting the existing file and showing the completed tasks. Make backups of already present style.',
                                    'Shift the file naruto.txt into anime and overwrite any existing file with same name. Display the progress. Save the files before overwriting with name in the same format as present previously.']}, ignore_index = True)

#42
mv = mv.append({'Command':         'mv -v --strip-trailing-slashes undo/// redo/',
                'NL Queries':      ['Move undo/// into redo/ after removing trailing slashes and show the tasks performed.',
                                    'After removing trailing slashes, shift undo/// into redo and display the jobs completed.',
                                    'Remove trailing slashes from source name. Move undo/// into redo. Give the details of accomplished jobs.']}, ignore_index = True)

#43
mv = mv.append({'Command':         'mv -iZ --backup=t bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default. Create numbered backup.',
                                    'Shift bleach.txt -> anime/bleach.txt and ask before over-writing. Use numbered style of backup and set SEL security context to default.',
                                    'Change the location of bleach.txt to anime/bleach.txt and use the numeric format of backup. Ask before over-writing and make SEL security context to its recommended value.']}, ignore_index = True)

#44
mv = mv.append({'Command':         'mv -fZ --backup=t bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default. Create numbered backup.',
                                    'Move bleach.txt -> anime/bleach.txt and set SELinux security context to default. Overwrite, if required. Make numeric backup format.',
                                    'Shift bleach.txt into anime folder, if other file of same name is present in destination then over-write. Configure SELinux security to default value. Create backup of numeric style.']}, ignore_index = True)

#45
mv = mv.append({'Command':         'mv -iv --backup=t bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Ask before overwriting files and show me the operations performed. Create numbered backup.',
                                    'Shift bleach.txt -> anime/bleach.txt and ask before overwriting. Display the tasks executed. Make numbered backups.',
                                    'Change the location of bleach.txt to anime/bleach.txt and ask for permission to overwrite files in destination. Show operations performed. Create backup of files being overwritten in the number style.']}, ignore_index = True)

#46
mv = mv.append({'Command':         'mv -fv --backup=t naruto.txt anime/',
                'NL Queries':      ['Move the file naruto.txt to anime directory. Overwrite the files and show the operations performed. Create numbered backup.',
                                    'naruto.txt -> anime/naruto.txt overwriting the existing file and showing the completed tasks. Make backups in numeric style.',
                                    'Shift the file naruto.txt into anime and overwrite any existing file with same name. Display the progress. Save the files before overwriting with name in the numbered format.']}, ignore_index = True)

#47
mv = mv.append({'Command':         'mv -buvZS .bk --strip-trailing-slashes code.txt anime/',
                'NL Queries':      ['Move the file code.txt to anime directory after stripping any trailing slashes from source code.txt and show the details of operations performed. Use .bk extension for creating backup files. Set SELinux security context to default.',
                                    'Showing the progress, move code.txt into anime folder after removing any trailing slashes and create backup using .bk as the extension. Move the source file only if the destination one has older modification or change time and set SELinux security context to normal.',
                                    'Shift code.txt into anime directory, only if source has newer file, after removing following slashes from source. Set SELinux security to default value and make backups using .bk extension.']}, ignore_index = True)

#48
mv = mv.append({'Command':         'mv -iZS .bk --backup bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default. Create backup with suffix .bk .',
                                    'Move bleach.txt -> anime/bleach.txt and ask before over-writing. Append .bk to the names of backup files and set SEL security context to default.',
                                    'Change the location of bleach.txt to anime/bleach.txt and use .bk at the end of backup files. Ask before over-writing and make SEL security context to its recommended value.']}, ignore_index = True)

#49
mv = mv.append({'Command':         'mv -fZS .bk --backup bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default. Create backup with suffix .bk .',
                                    'Shift bleach.txt -> anime/bleach.txt and set SELinux security context to default. Overwrite, if required. Make backups with .bk appended to backup files.',
                                    'Shift bleach.txt into anime folder, if other file of same name is present in destination then over-write. Configure SELinux security to default value. Create backup with .bk extension.']}, ignore_index = True)

#50
mv = mv.append({'Command':         'mv -ivS .bk --backup bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Ask before overwriting files and show me the operations performed. Create backup with suffix .bk.',
                                    'Move bleach.txt -> anime/bleach.txt and ask before overwriting. Display the tasks executed. Make backups whose names end with .bk .',
                                    'Change the location of bleach.txt to anime/bleach.txt and ask for permission to overwrite files in destination. Show operations performed. Create backup of files being overwritten with the original names appended with .bk .']}, ignore_index = True)

#51
mv = mv.append({'Command':         'mv -fvS .bk --backup naruto.txt anime/',
                'NL Queries':      ['Move the file naruto.txt to anime directory. Overwrite the files and show the operations performed. Create backup with suffix .bk .',
                                    'Shift naruto.txt -> anime/naruto.txt overwriting the existing file and showing the completed tasks. Make backups with names ending in .bk .',
                                    'Shift the file naruto.txt into anime and overwrite any existing file with same name. Display the progress. Save the files before overwriting with name appended with .bk .']}, ignore_index = True)

#52
mv = mv.append({'Command':         'mv -bvS .bk code.txt anime/',
                'NL Queries':      ['Move the file code.txt to directoy anime and create backup with extension, .bk . Show the operations performed.',
                                   'duplicate.txt -> original/duplicate.txt and create backup with .bk extension. Show the which were moved.',
                                   'Shift the file duplicate.txt into original directory. Create backup with .bk extension, if required, and show the tasks performed.']}, ignore_index = True)

#53
mv = mv.append({'Command':         'mv -buvS .bk code.txt anime/',
                'NL Queries':      ['Move the file code.txt to anime directory, only if the source code.txt file is newer, and show the details of operations performed. Use .bk extension for creating backup files.',
                                    'Showing the progress, move code.txt into anime folder after removing any trailing slashes and create backup using .bk as the extension. Move the source file only if the destination one has older modification or change time.',
                                    'Shift code.txt into anime directory, only if source has newer file, after removing following slashes from source. Make backups using .bk extension.']}, ignore_index = True)

#54
mv = mv.append({'Command':         'mv -nvZ bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Do not overwrite existing files and set SELinux security context to default settings. Show the operations performed.',
                                    'Shift bleach.txt into anime directory and do not overwrite existing files. Make SEL security context to default and show the tasks completed.',
                                    'Move bleach.txt -> anime/bleach.txt and do not over-write. Set SEL security context to default and show the jobs completed.']}, ignore_index = True)

#55
mv = mv.append({'Command':         'mv -ivZ bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default. Show the operations performed.',
                                    'Shift bleach.txt -> anime/bleach.txt showing progress. Ask before overwriting. Set SEL security context to default value.',
                                    'Shift bleach.txt into anime folder. Show the progress of process and ask before overwriting. Set SEL security context to default.']}, ignore_index = True)

#56
mv = mv.append({'Command':         'mv -fvZ bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default. Show the operations performed.',
                                    'Shift bleach.txt into anime folder. Overwrite files without asking. Set SEL security to default. Show task progress.',
                                    'Overwriting files, if needed, move bleach.txt to anime and show the tasks completed. Configure SEL security context to defaukt value.']}, ignore_index = True)

#57
mv = mv.append({'Command':         'mv -fvZS .bk --backup --strip-trailing-slashes bleach/ anime/',
                'NL Queries':      ['Move bleach/ to anime directory after removing any trailing slashes from source bleach/ . Overwrite files and set SELinux security context to default. Create backup with suffix .bk . Show the operations performed.',
                                    'Move bleach/ -> anime/bleach . Strip trailing slashes from source. Overwrite files, if needed and set SEL security context to default. Create backup with .bk extension.',
                                    'Shift bleach/ into anime after removing following slashes from source name. Set SEL security to default and overwrite, if needed. Create backup with name ending with .bk .']}, ignore_index = True)

#58
mv = mv.append({'Command':         'mv -ivZ --backup bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default. Create simple backup. Show the operations performed.',
                                    'Shift bleach.txt -> anime/bleach.txt showing progress. Ask before overwriting and create backup of overwritten files. Set SEL security context to default value.',
                                    'Shift bleach.txt into anime folder. Show the progress of process and ask before overwriting and take backup of those files. Set SEL security context to default.']}, ignore_index = True)

#59
mv = mv.append({'Command':         'mv -fvZ --backup bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default. Create simple backup. Show the operations performed.',
                                    'Move bleach.txt -> anime/bleach.txt showing progress. Overwrite files after making their backup files. Set SEL security context to default value.',
                                    'Shift bleach.txt into anime folder. Show the progress of process and do not ask before overwriting. Create backup. Set SEL security context to default.']}, ignore_index = True)

#60
mv = mv.append({'Command':         'mv -nv --strip-trailing-slashes undo/// redo/',
                'NL Queries':      ['Move undo/// into redo directory after stripping following slashes. Do not overwrite any file. Show the progress of the process.',
                                    'Truncate trailing slashes from source undo/// and transfer it into redo folder. Do not overwrite existing files and give the list of tasks performed.',
                                    'Shift undo/// into redo after stripping trailing forward slashes from source name. Do not overwrite any files in destination. Display the jobs completed.']}, ignore_index = True)

#61
mv = mv.append({'Command':         'mv -ivZ --backup=existing bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default. Create existing backup. Show the operations performed.',
                                    'Shift bleach.txt -> anime/bleach.txt showing progress. Ask before overwriting and take backup of those files in existing format. Set SEL security context to default value.',
                                    'Shift bleach.txt into anime folder. Show the progress of process and ask before overwriting. Create backup for overwritten files in the format used before. Set SEL security context to default.']}, ignore_index = True)

#62
mv = mv.append({'Command':         'mv -fvZ --backup=existing bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default. Create existing backup. Show the operations performed.',
                                    'Shift bleach.txt -> anime/bleach.txt showing progress. Overwrite files after making their backup files in existing format. Set SEL security context to default value.',
                                    'Shift bleach.txt into anime folder. Show the progress of process and do not ask before overwriting. Create backup in existing format for such files. Set SEL security context to default.']}, ignore_index = True)

#63
mv = mv.append({'Command':         'mv -ivZS .bk --strip-trailing-slashes --backup bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory after removing any trailing slashes from source bleach.txt . Ask for overwriting files. Set the SELinux security context to default. Create backup with suffix .bk . Show the operations performed.',
                                    'How do I move bleach.txt inside anime folder after removing following slashes from name and creatinng backup of overwritten files with .bk extension? I also want to display the tasks done, ask before overwriting files and set SELinux security context to default value?',
                                    'Setting SEL security context to default, shift bleach.txt into anime folder after stripping trailing slashes from source name. Ask for permission to overwrite files and display the tasks completed.']}, ignore_index = True)

#64
mv = mv.append({'Command':         'mv -ivZ --backup=t bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default. Create numbered backup. Show the operations performed.',
                                    'Transfer bleach.txt into anime folder. Set sel security context to normal value and create numbered backup. Do not over-write files without asking and show the operations performed.',
                                    'Shift the file, bleach.txt into anime folder and make the sel security context default. Ask for permission to overwrite files and take numbered backup of overwritten files.']}, ignore_index = True)

#65
mv = mv.append({'Command':         'mv -fvZ --backup=t bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default. Create numbered backup. Show the operations performed.']}, ignore_index = True)

#66
mv = mv.append({'Command':         'mv -fvZ --strip-trailing-slashes --backup=t bleach.txt// anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory after removing trailing slashes fromm source bleach.txt// . Overwrite files and set SELinux security context to default. Create numbered backup. Show the operations performed.',
                                    'Transfer bleach.txt into anime folder. Set sel security context to normal value and create numbered backup. Over-write files without asking and show the operations performed.',
                                    'Shift the file, bleach.txt into anime folder and make the sel security context default.Do not ask for permission to overwrite files and take numbered backup of overwritten files.']}, ignore_index = True)

#67
mv = mv.append({'Command':         'mv -ivZS .bk --backup bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory. Ask for overwriting files. Set the SELinux security context to default. Create backup with suffix .bk . Show the operations performed.',
                                    'Setting SELinux security context to default, move bleach.txt inside anime folder and create backup with .bk extension. Show the progress of tasks. Do not over-write without permission.',
                                    'Shift bleach.txt into anime folder with sel security context set to default and make backup with .bk appended to name before overwriting them. Ask before overwriting.']}, ignore_index = True)

#68
mv = mv.append({'Command':         'mv -fvZS .bk --backup bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory. Overwrite files and set SELinux security context to default. Create backup with suffix .bk . Show the operations performed.',
                                    'Setting SELinux security context to default, move bleach.txt inside anime folder and create backup with .bk extension. Show the progress of tasks. Over-write without permission.',
                                    'Shift bleach.txt into anime folder with sel security context set to default and make backup with .bk appended to name before overwriting them. Do not ask before overwriting.']}, ignore_index = True)

#69
mv = mv.append({'Command':         'mv -buvZS .bk code.txt anime/',
                'NL Queries':      ['Move the file code.txt to anime directory, only if the source file code.txt is newer, and show the details of operations performed. Use .bk extension for creating backup files. Set SELinux security context to default.',
                                    'Creating backup with .bk extension, shift code.txt into anime folder. Perform this operation only when destination has older file. Also set sel security to default. Show the progress of the tasks.',
                                    'Showing the progress of the tasks, transfer code.txt into anime folder, if there is old file in destination. Display the operations completed and set SELinux security to default setting.']}, ignore_index = True)

#70
mv = mv.append({'Command':         'mv -nvZ --strip-trailing-slashes bleach/// anime/',
                'NL Queries':      ['Move bleach/// to anime directory after stripping trailing slashes from source bleach/// . Do not overwrite existing files and set SELinux security context to default settings. Show the operations performed.',
                                    'Removing the trailing slashes from source bleach/// , transfer it inside anime folder if no file of same name exists already. Set SEL context to default value. Show the jobs completed.',
                                    'Showing the tasks fulfilled, move bleach/// into anmie . Remove following slashes from source before transferring. Do not transfer if the file with same name is present.']}, ignore_index = True)

#71
mv = mv.append({'Command':         'mv -ivZ --strip-trailing-slashes bleach/// anime/',
                'NL Queries':      ['Move bleach/// to anime directory after stripping trailing slashes from source bleach/// . Ask for overwriting files. Set the SELinux security context to default. Show the operations performed.',
                                    'Remove the ending slashes from bleach/// . Shift it inside anime folder, if a file with same name overwrite only after asking. Set the SEL to normal value. Show the tasks completed.',
                                    'Giving the acknowledgement of the jobs performed, move bleach/// into anime folder after removing ending slashes. Set SEL security to default. Overwrite any file with my permission.']}, ignore_index = True)

#72
mv = mv.append({'Command':         'mv -fvZ --strip-trailing-slashes bleach/// anime/',
                'NL Queries':      ['Move bleach/// to anime directory after stripping all the trailing slashes from source bleach/// . Overwrite files and set SELinux security context to default. Show the operations performed.',
                                    'Remove the ending slashes from bleach/// . Shift it inside anime folder, if a file with same name exists overwrite. Set the SEL to normal value. Show the tasks completed.',
                                    'Giving the acknowledgement of the jobs performed, move bleach/// into anime folder after removing ending slashes. Set SEL security to default. Overwrite any file.']}, ignore_index = True)

#73
mv = mv.append({'Command':         'mv -ivZ --strip-trailing-slashes --backup=t bleach.txt anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory after removing any trailing slashes from source bleach.txt . Ask for overwriting files. Set the SELinux security context to default. Create numbered backup. Show the operations performed.',
                                    'Remove the ending slashes from bleach.txt . Shift it inside anime folder, if a file with same name exists create numbered backup only after asking. Set the SEL to normal value. Show the tasks completed.',
                                    'Giving the acknowledgement of the jobs performed, move bleach.txt into anime folder after removing ending slashes. Set SEL security to default. Take backup of numbering style if overwriting any file with my permission.']}, ignore_index = True)

#74
mv = mv.append({'Command':         'mv -ivZ --backup --strip-trailing-slashes bleach// anime/',
                'NL Queries':      ['Move bleach// to anime directory after removing the trailing slashes from source bleach// . Ask for overwriting files. Set the SELinux security context to default. Create simple backup. Show the operations performed.',
                                    'Remove the ending slashes from bleach.txt// . Shift it inside anime folder, if a file with same name exists create backup only after asking. Set the SEL to normal value. Show the tasks completed.',
                                    'Giving the acknowledgement of the jobs performed, move bleach.txt// into anime folder after removing ending slashes. Set SEL security to default. Take backup of existing style if overwriting any file with my permission.']}, ignore_index = True)

#75
mv = mv.append({'Command':         'mv -fvZ --backup --strip-trailing-slashes bleach//// anime/',
                'NL Queries':      ['Move bleach//// to anime directory after removing the trailing slashes from source bleach//// . Overwrite files and set SELinux security context to default. Create simple backup. Show the operations performed.',
                                    'Remove the ending slashes from bleach.txt//// . Shift it inside anime folder, if a file with same name exists create backup. Set the SEL to normal value. Show the tasks completed.',
                                    'Giving the acknowledgement of the jobs performed, move bleach.txt//// into anime folder after removing ending slashes. Set SEL security to default. Take backup of existing style if overwriting any file.']}, ignore_index = True)

#76
mv = mv.append({'Command':         'mv -fvZ --strip-trailing-slashes --backup=existing bleach.txt anime/',
                'NL Queries':      ['Move the file bleach.txt to anime directory after removing any trailing slashes from source bleach.txt . Overwrite files and set SELinux security context to default. Create existing backup. Show the operations performed.',
                                    'Remove the ending slashes from bleach.txt . Shift it inside anime folder, if a file with same name exists create backup of existing style. Set the SEL to normal value. Show the tasks completed.',
                                    'Giving the acknowledgement of the jobs performed, move bleach.txt into anime folder after removing ending slashes. Set SEL security to default. Take backup of existing style if overwriting any file.']}, ignore_index = True)

#77
mv = mv.append({'Command':         'mv -ivZ --backup=existing --strip-trailing-slashes bleach.txt/ anime/',
                'NL Queries':      ['Move bleach.txt file to anime directory after removing any trailing slashes from source bleach.txt/ . Ask for overwriting files. Set the SELinux security context to default. Create existing backup. Show the operations performed.',
                                    'Remove the ending slashes from bleach.txt/ . Shift it inside anime folder, if a file with same name exists create backup of existing only after asking. Set the SEL to normal value. Show the tasks completed.',
                                    'Giving the acknowledgement of the jobs performed, move bleach.txt/ into anime folder after removing ending slashes. Set SEL security to default. Take backup of existing style if overwriting any file with my permission.']}, ignore_index = True)

#78
mv = mv.append({'Command':         'mv -n --strip-trailing-slashes undo/// redo/',
                'NL Queries':      ['Without over-writing existing files, shift undo/// into redo directory after stripping trailing slashes from source.',
                                    'Move undo/// inside redo directory. Remove trailing slashes from source before performing the operation. Do not over write.',
                                    'Remove following slashes from undo/// . Move it inside redo folder, if no file with same name id present.']}, ignore_index = True)



#mv.to_csv('/home/ananyaraval/Documents/Thesis/Data/UNIX/csv_files/mv.csv',index=False)
print mv.shape



