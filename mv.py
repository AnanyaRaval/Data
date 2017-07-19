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
                                        'How do I transfer test1.cpp present in this folder to destination folder dir1 and rename it to test2.cpp along with making backup in dir1.?',
                                        'Change location of test1.cpp to dir/ and rename it to test2.cpp and create a backup.']}, ignore_index = True)

#2
mv = mv.append({'Command':        'mv --backup=existing test1.cpp dir1/test2.cpp',
                'NL Queries':     ['Move test1.cpp into directory dir1 under the name test2.cpp . Create backup at the destination using existing option.',
                                'Shift test1.cpp to dir1. Rename it to test2.cpp. Take numbered backup of all files in dir1 if numbered backup already exists, otherwise take simple backup.',
                                        'How do I transfer test1.cpp to dir1/test2.cpp? Take backup of all files in destination folder using existing backup strategy of the folder.']}, ignore_index = True)
#3
mv = mv.append({'Command':        'mv --backup=t test1.cpp dir1/test2.cpp',
                'NL Queries':     ['Move test1.cpp into directory dir1 under the name test2.cpp . Create numbered backup at the destination.',
                                        'Shift test1.cpp to destination folder dir1 present in the working directory. Create numbered backup of all files in dir1. Rename the file to test2.cpp.',
                                'How do I transfer test1.cpp to destination folder dir1, rename it to test2.cpp and create numbered backup?']}, ignore_index = True)

#4
mv = mv.append({'Command':        'mv -f file1.doc fold1/file2.doc',
                'NL Queries':     ['Move file1.doc inside fold1 directory as file2.doc and overwrite without asking.',
                                'How do I shift file1.doc to folder fold1? Rename file1.doc to file2.doc and overwrite file2.doc if it exists.',
                                        'Transfer file1.doc to fold1/file2.doc and overwrite if file2.doc exists.']}, ignore_index = True)

#5
mv = mv.append({'Command':        'mv -i file1.doc fold1/file2.doc',
                'NL Queries':     ['Move file1.doc inside fold1 directory as file2.doc and do not overwrite without asking.',
                                'Change location of file1.doc to fold1 in current folder and rename it to file2.doc. If file2.doc exists, prompt before overwriting.',
                                'How do I rename file1.doc to file2.doc and move it inside fold1? If file2.doc exists in fold1, confirm before replacing.',
                                'Change location of file1.doc from current directory to fold1. If file2.doc exists in fold1, prompt before replacing. Otherwise change name of file1.doc to file2.doc.']}, ignore_index = True)

#6
mv = mv.append({'Command':        'mv -n file1.doc fold1/file2.doc',
                'NL Queries':     ['Move file1.doc inside fold1 directory as file2.doc and do not overwrite.',
                                'How do I shift file1.doc to a folder named fold1.doc and rename it to file2.doc? Do not overwrite an existing file of the same name.',
                                'Shift file1.doc to fold1. Rename to file2.doc without overwriting.'
                                'How do I change location of file1.doc present in this folder to fold1 also present in  this folder. Rename to file2.doc without replacing an existing file of the same name.']}, ignore_index = True)

#7
mv = mv.append({'Command':        'mv -b -S .bk test1.cpp dir1/test2.cpp',
                'NL Queries':     ['Move test1.cpp into directory dir1 under the name test2.cpp . Create backup at the destination with .bk extension.']}, ignore_index = True)

#8
mv = mv.append({'Command':        'mv --help',
                'NL Queries':     ['Display help for mv command.']}, ignore_index = True)

#9
mv = mv.append({'Command':        'mv --version',
                'NL Queries':     ['Display details about mv command.']}, ignore_index = True)

#10
mv = mv.append({'Command':        'mv file1.txt file2.txt dest1',
                'NL Queries':     ['Move file1.txt and file2.txt to dest1 directory.']}, ignore_index = True)

#11
mv = mv.append({'Command':        'mv file1.txt file2.txt file3.txt dest1',
                'NL Queries':     ['Move file1.txt, file2.txt and file3.txt to dest1 directory.']}, ignore_index = True)

#12
mv = mv.append({'Command':        'mv -v file1.txt dest1',
                'NL Queries':     ['Move file1.txt to dest1 directory and give me a details.']}, ignore_index = True)

#13
mv = mv.append({'Command':        'mv -u file1.txt dest1',
                'NL Queries':     ['Move file1.txt to dest1 directory if it is newer than the file in dest1 or is non-existant.']}, ignore_index = True)

#14
mv = mv.append({'Command':        'mv -Z file1.txt dest1',
                'NL Queries':     ['Move file1.txt to dest1 directory and change security context to default.']}, ignore_index = True)

#15
mv = mv.append({'Command':        'mv --strip-trailing-slashes unknown// dest1',
                'NL Queries':     ['Move unknown// to dest1 directory after removing trailing slashes.']}, ignore_index = True)


print mv.shape



