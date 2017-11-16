import pandas as pd 

cp = pd.DataFrame(columns = ['Command','NL Queries'])

cp = cp.append({'Command':'cp main.c bak','NL Queries':['Copy main.c in curent folder to bak in the same folder.',
'How do I copy main.c to bak?',
'Command to copy contents of main.c to bak.']},ignore_index = True)

cp = cp.append({'Command':'cp *.py backup','NL Queries':['Copy all .py files to backup folder.',
'How do I copy all .py files to folder backup?',
'Command to replicate all files to folder backup in this directory.']},ignore_index=True)

cp = cp.append({'Command':'cp file1.txt file2.txt dir1','NL Queries':['How do I copy file1.txt and file2.txt to directory dir1?',
'How do I copy two files file1.txt and file2.txt to folder dir1 at the same time?',
'Copy two files file1.txt and file2.txt to a given directory dir1.']},ignore_index=True)

cp = cp.append({'Command':'cp ../file1.txt .','NL Queries':['How do I copy a file file1.txt from from parent directory to the current folder?',
'Copy file file1.txt from previous folder to current folder.',
'How do I copy file1.txt from parent folder to current directory?']},ignore_index=True)

cp = cp.append({'Command':'cp new1.txt /','NL Queries':['How do I copy new1.txt to the root directory?',
'Copies new1.txt to root directory.',
'How do I copy file new1.txt to root folder?']},ignore_index=True)

cp = cp.append({'Command':'cp best.txt ~','NL Queries':['How do I copy best.txt to the home directory?',
'Copies best.txt to home directory.',
'Copy best.txt to /home/']},ignore_index=True)

cp = cp.append({'Command':'cp main.c def.h /home/usr/rapid/','NL Queries':['Copy 2 files main.c and def.h to destination absolute path /home/usr/rapid/',
'How do I copy main.c and def.h to a given absolute path /home/usr/rapid/?',
'How do I copy two files main.c and def.h to the folder present in /home/usr/rapid/?']},ignore_index=True)

cp = cp.append({'Command':'cp file* /directory/subdirectory','NL Queries':['Copy all files with filename beginning with file into /directory/subdirectory.',
	'How do I copy files beginning with \'file\' into /directory/subdirectory?','Command to copy files beginning with \'file\' into /directory/subdirectory.']},ignore_index=True)

cp = cp.append({'Command':'cp -a directory_1/ /home/pungki/office','NL Queries':['How do I copy all files including symbolic links in directory_1 to absolute path /home/pungki/office?',
'Copy files and folders including symbolic links in directory_1 to office folder in /home/pungki.',
'How do I copy all symbolic links, files and folders from directory_1 to /home/pungki/office?']},ignore_index=True)

cp = cp.append({'Command':'cp --attributes-only file1.txt file2.txt','NL Queries':['How do I copy only the attributes of file1 to file2?',
'Get the file attributes of file1 and copy it to file2.',
'How do I copy ownership and timestamp from file1 to file2?']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt.',
'How to copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office?',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory?']},ignore_index=True)

cp = cp.append({'Command':'cp -b *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt.',
'How to copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office?',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory?']},ignore_index=True)

cp = cp.append({'Command':'cp -f new1.txt new2.txt','NL Queries':['How do I forcefully copy new1.txt to new2.txt?',
'Copy new1.txt to new2.txt by removing new2.txt and trying again if it cannot be opened.',
'Copy new1.txt to new2.txt. If destination file new2.txt cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -i game1.txt dir1','NL Queries':['How do I copy file game1.txt to dir1 with a prompt?',
'How do I ensure that the file game.txt get copied to dir1 only after asking me?',
'How do I ensure that I am asked for confirmation before the file game.txt gets copied to directory dir1?']},ignore_index=True)

cp = cp.append({'Command':'cp -l file fileshortcut','NL Queries':['How do I create a shortcut of file under the name fileshortcut?',
'Create a shortcut of a file \'fileshortcut\' in the same directory.',
'Command to create shortcut fileshortcut of file.',
'Single command to create a hard link fileshortcut of the file named file in the current folder.']},ignore_index=True)

cp = cp.append({'Command':'cp -l file_4.txt /home/pungki/office','NL Queries':['How do I create a hard link of file file4.txt to /home/pungki/office directory?',
'How do I create a shortcut for a file file4.txt in /home/pungki/office?',
'Command to create shortcut for a file file4.txt and place it in a directory /home/pungki/office.']},ignore_index=True)

cp = cp.append({'Command':'cp -L file_6.txt ./movie','NL Queries':['How do I get the original source file file_6.txt from symbolic link in ./movie?',
'Command to get the source file file_6.txt from symbolic link in ./movie.']},ignore_index=True)

cp = cp.append({'Command':'cp -n instructions.txt backup','NL Queries':['Create a copy of instructions.txt named backup. Copy only if backup not present in current folder.',
'How do I copy instructions.txt to backup without overwriting it.',
'Copy instructions.txt and name it backup. Do not overwrite if backup exists.']},ignore_index=True)

cp = cp.append({'Command':'cp -P file_6.txt ./movie','NL Queries':['How do I copy file file_6.txt with symbolic link as it is to ./movie?',
'Copy file file_6.txt with symbolic link as it is into another file ./movie.',
'Copy file file_6.txt to ./movie. Copy symbolic links as they are.']},ignore_index=True)

cp = cp.append({'Command':'cp -r dir1 dir2','NL Queries':['Copy entire directory structure dir1 to dir2.',
'How do I copy the files and folders inside dir1 recursively into dir2?',
'Copy all files and folders inside dir1 to dir2','Command to copy files and folders in dir1 to dir2 recursively.']},ignore_index=True)

cp = cp.append({'Command':'cp --remove-destination file1.txt file2.txt','NL Queries':['How do I overwrite an existing file2.txt with contents from file1.txt?',
'Remove the file2.txt. Recreate it with contents from file1.txt.',
'How do I delete file2.txt and replace it with contents from file1.txt?']},ignore_index=True)

cp = cp.append({'Command':'cp -s file.txt file2.txt','NL Queries':['Create symbolic link file2.txt to point to file1.txt.',
'How to create symbolic link for file1.txt with the name file1.txt?',
'Create symbolic link file2.txt for file1.txt.']},ignore_index=True)

cp = cp.append({'Command':'cp -s ~/myfiles/file*.txt ~/myfiles2','NL Queries':['Create a symbolic link of multiple files starting with \'file\' in ~/myfiles directory as ~/myfiles2.',
'How to create symbolic links for multiple files starting with \'file\' in ~/myfiles folder as ~/myfiles2?',
'Command to create a symbolic links for files starting with \'file\' in ~/myfiles folder with name ~/myfiles2.']},ignore_index=True)

cp = cp.append({'Command':'cp -u * ananya','NL Queries':['Copy all files in this folder to ananya only if they are not present in ananya or if they are newer than source file.',
'Update folder ananya by copying files from this directory. Update only if file not present in ananya and if the file is newer than source file.',
'How do I copy all files from this folder to ananya making sure only the files which need to be updated or hich don\'t exist are copied.']},ignore_index=True)

cp = cp.append({'Command':'cp -v joke1 joke2','NL Queries':['How do I copy joke1 to joke2 along with details on what is being done?',
'Copy joke1 to joke2 and show information on what is being done.',
'How do I see details of joke1 being copied to joke2?']},ignore_index=True)

##### -i

cp = cp.append({'Command':'cp -i -a directory_1/ /home/pungki/office','NL Queries':['How do I copy all files including symbolic links in directory_1 to absolute path /home/pungki/office in interactive mode?',
'Copy files and folders including symbolic links in directory_1 to office folder in /home/pungki. Prompt before overwriting existing destination files.',
'How do I copy all symbolic links, files and folders from directory_1 to /home/pungki/office? Prompt before overwriting any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i --attributes-only file1.txt file2.txt','NL Queries':['How do I copy only the attributes of file1 to file2 in interactive mode?',
'Get the file attributes of file1 and copy it to file2. Prompt before overwriting any existing destination files.',
'How do I copy ownership and timestamp from file1 to file2? Prompt before overwriting any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i --backup=simple *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt in interactive mode.',
'How to copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office? Prompt before overwriting any existing destination files.',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory? Prompt before overwriting any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -b *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt in interactive mode.',
'How to copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office? Prompt before overwriting any existing destination files.',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory? Prompt before overwriting any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -i new1.txt new2.txt','NL Queries':['How do I forcefully copy new1.txt to new2.txt? Prompt before the operation in interactive mode.',
'Copy new1.txt to new2.txt by removing new2.txt and trying again if it cannot be opened after asking me.',
'Copy new1.txt to new2.txt. If destination file new2.txt cannot be opened, remove it and try again. Ensure I am asked for confirmation.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -l file fileshortcut','NL Queries':['How do I create a shortcut of file under the name fileshortcut in interactive mode?',
'Create a shortcut of a file \'fileshortcut\' in the same directory. Prompt before overwriting any existing destination files.',
'Command to create shortcut fileshortcut of file. Ensure I am asked for confirmation before removing any existing destination files.',
'Single command to create a hard link fileshortcut of the file named file in the current folder. Prompt before overwriting any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -l file_4.txt /home/pungki/office','NL Queries':['How do I create a hard link of file file4.txt to /home/pungki/office directory in interactive mode?',
'How do I create a shortcut for a file file4.txt in /home/pungki/office? Prompt before overwriting any existing destination files.',
'Command to create shortcut for a file file4.txt and place it in a directory /home/pungki/office. Ensure I am asked for confirmation before removing any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -L file_6.txt ./movie','NL Queries':['How do I get the original source file file_6.txt from symbolic link in ./movie in interactive mode?',
'Command to get the source file file_6.txt from symbolic link in ./movie. Prompt before overwriting any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -P file_6.txt ./movie','NL Queries':['How do I copy file file_6.txt with symbolic link as it is to ./movie in interactive mode?',
'Copy file file_6.txt with symbolic link as it is into another file ./movie. Prompt before overwriting any existing destination files.',
'Copy file file_6.txt to ./movie. Copy symbolic links as they are. Ensure I am asked for confirmation before removing any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -r dir1 dir2','NL Queries':['Copy entire directory structure dir1 to dir2 in interactive mode.',
'How do I copy the files and folders inside dir1 recursively into dir2? Prompt before overwriting any existing destination files.',
'Copy all files and folders inside dir1 to dir2.  Ensure I am asked for confirmation before removing any existing destination files.',
'Command to copy files and folders in dir1 to dir2 recursively. Prompt before overwriting any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i --remove-destination file1.txt file2.txt','NL Queries':['How do I overwrite an existing file2.txt with contents from file1.txt in interactive mode?',
'Remove the file2.txt. Recreate it with contents from file1.txt. Prompt before overwriting any existing destination files.',
'How do I delete file2.txt and replace it with contents from file1.txt? Ensure I am asked for confirmation before removing any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -s file.txt file2.txt','NL Queries':['Create symbolic link file2.txt to point to file1.txt in interactive mode.',
'How to create symbolic link for file1.txt with the name file1.txt with cp command? Prompt before overwriting any existing destination files.',
'Create symbolic link file2.txt for file1.txt with cp command. Ensure I am asked for confirmation before removing any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -s ~/myfiles/file*.txt ~/myfiles2','NL Queries':['Create a symbolic link of multiple files starting with \'file\' in ~/myfiles directory as ~/myfiles2 in interactive mode.',
'How to create symbolic links for multiple files starting with \'file\' in ~/myfiles folder as ~/myfiles2? Prompt before overwriting any existing destination files.',
'Command to create a symbolic links for files starting with \'file\' in ~/myfiles folder with name ~/myfiles2. Ensure I am asked for confirmation before removing any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -u * ananya','NL Queries':['Copy all files in this folder to ananya only if they are not present in ananya or if they are newer than source file in interactive mode.',
'Update folder ananya by copying files from this directory. Update only if file not present in ananya and if the file is newer than source file. Prompt before overwriting any existing destination files.',
'How do I copy all files from this folder to ananya making sure only the files which need to be updated or which don\'t exist are copied. Ensure I am asked for confirmation before removing any existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -v joke1 joke2','NL Queries':['How do I copy joke1 to joke2 along with details on what is being done in interactive mode?',
'Copy joke1 to joke2 and show information on what is being done. Ensure I am asked for confirmation before removing any existing destination files.',
'How do I see details of joke1 being copied to joke2? Prompt before overwriting any existing destination files.']},ignore_index=True)

####

cp = cp.append({'Command':'cp -R -s ~/myfiles ~/myfiles2','NL Queries':['Create a symbolic link for all files and folders in ~/myfiles recursively as ~/myfiles2.',
'How do I create a symbolic link ~/myfiles2 to an entire directory structure  ~/myfiles?',
'Command to create symbolic link recursively for the folder ~/myfiles with the name ~/myfiles2.']},ignore_index=True)

#### -v

cp = cp.append({'Command':'cp -a -v directory_1/ /home/pungki/office','NL Queries':['How do I copy all files including symbolic links in directory_1 to absolute path /home/pungki/office with details of what is being done?',
'Copy files and folders including symbolic links in directory_1 to office folder in /home/pungki. Show all details of what is being done',
'How do I copy all symbolic links, files and folders from directory_1 to /home/pungki/office? Also, give information about what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp --attributes-only -v file1.txt file2.txt','NL Queries':['How do I copy only the attributes of file1 to file2 in verbose mode?',
'Get the file attributes of file1 and copy it to file2 in verbose mode.',
'How do I copy ownership and timestamp from file1 to file2? Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -v *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt in verbose mode.',
'How to copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office in verbose mode?',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory? Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -b -v *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt in verbose mode.',
'How to copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office in verbose mode?',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory? Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -v new1.txt new2.txt','NL Queries':['How do I forcefully copy new1.txt to new2.txt in verbose mode?',
'Copy new1.txt to new2.txt by removing new2.txt and trying again if it cannot be opened in verbose mode.',
'Copy new1.txt to new2.txt. If destination file new2.txt cannot be opened, remove it and try again. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -l -v file fileshortcut','NL Queries':['How do I create a shortcut of file under the name fileshortcut in verbose mode?',
'Create a shortcut of a file \'fileshortcut\' in the same directory in verbose mode.',
'Command to create shortcut fileshortcut of file in verbose mode.',
'Single command to create a hard link fileshortcut of the file named file in the current folder. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -l -v file_4.txt /home/pungki/office','NL Queries':['How do I create a hard link of file file4.txt to /home/pungki/office directory in verbose mode?',
'How do I create a shortcut for a file file4.txt in /home/pungki/office in verbose mode?',
'Command to create shortcut for a file file4.txt and place it in a directory /home/pungki/office. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -L -v file_6.txt ./movie','NL Queries':['How do I get the original source file file_6.txt from symbolic link in ./movie in verbose mode?',
'Command to get the source file file_6.txt from symbolic link in ./movie. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -n -v instructions.txt backup','NL Queries':['Create a copy of instructions.txt named backup. Copy only if backup not present in current folder in verbose mode.',
'How do I copy instructions.txt to backup without overwriting it in verbose mode.',
'Copy instructions.txt and name it backup. Do not overwrite if backup exists. Explain what is being done.']},ignore_index=True)


cp = cp.append({'Command':'cp -p -v /etc/resolv.conf $HOME','NL Queries':['Copy all attributes along with the file /etc/resolv.conf to home. Show the files copied',
'How do I copy /etc/resolve.conf file to home directory along with attributes and display the files copied?',
'Command to copy /etc/resolv.conf to home along with the attributes and list the files copied.']},ignore_index=True)

cp = cp.append({'Command':'cp -r -v dir1 dir2','NL Queries':['How do I copy recursively from dir1 to dir2 and get to know what is being copied?',
'Copies all files and folders from dir1 to dir2. Display information on what is being copied.',
'How do I copy all files and folders from dir1 to dir2 and get information on what is being copied?']},ignore_index=True)

cp = cp.append({'Command':'cp --remove-destination -v file1.txt file2.txt','NL Queries':['How do I overwrite an existing file2.txt with contents from file1.txt in verbose mode?',
'Remove the file2.txt. Recreate it with contents from file1.txt in verbose mode.',
'How do I delete file2.txt and replace it with contents from file1.txt? Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -s -v file.txt file2.txt','NL Queries':['Create symbolic link file2.txt to point to file1.txt in verbose mode.',
'How to create symbolic link for file1.txt with the name file1.txt with cp command in verbose mode?',
'Create symbolic link file2.txt for file1.txt with cp command. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -s -v ~/myfiles/file*.txt ~/myfiles2','NL Queries':['Create a symbolic link of multiple files starting with \'file\' in ~/myfiles directory as ~/myfiles2 in verbose mode.',
'How to create symbolic links for multiple files starting with \'file\' in ~/myfiles folder as ~/myfiles2 in verbose mode?',
'Command to create a symbolic links for files starting with \'file\' in ~/myfiles folder with name ~/myfiles2. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -u -v * ananya','NL Queries':['Copy all files in this folder to ananya only if they are not present in ananya or if they are newer than source file in verbose mode.',
'Update folder ananya by copying files from this directory in verbose mode. Update only if file not present in ananya and if the file is newer than source file.',
'How do I copy all files from this folder to ananya making sure only the files which need to be updated or which don\'t exist are copied. Explain what is being done.']},ignore_index=True)

#### --backup=simple 

cp = cp.append({'Command':'cp --backup=simple -a directory_1/ /home/pungki/office','NL Queries':['How do I create a copy of existing destination files and copy all files including symbolic links in directory_1 to absolute path /home/pungki/office?',
'Copy files and folders including symbolic links in directory_1 to office folder in /home/pungki. Instead of overwriting existing files, create their backup.',
'How do I create a backup of exisitng destination files and copy all symbolic links, files and folders from directory_1 to /home/pungki/office?']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple --attributes-only file1.txt file2.txt','NL Queries':['How do I create a backup of existing destination files and copy only the attributes of file1 to file2?',
'Get the file attributes of file1 and copy it to file2. Instead of overwriting existing files, create their backup.',
'How do I create a backup of any existing file titled file2.txt and copy ownership and timestamp from file1 to file2?']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -b *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt.',
'How to copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office?',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory?']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -f new1.txt new2.txt','NL Queries':['How do I forcefully copy new1.txt to new2.txt? Create a backup of existing destination files.',
'Copy new1.txt to new2.txt by removing new2.txt and trying again if it cannot be opened. Instead of overwriting the exisitng destination file, create its backup.',
'Copy new1.txt to new2.txt. If destination file new2.txt cannot be opened, remove it and try again. Also, create a backup of existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -l file fileshortcut','NL Queries':['How do I create a shortcut of file under the name fileshortcut? Create a backup of any existing file titled fileshortcut.',
'Create a shortcut of a file \'fileshortcut\' in the same directory. Instead of overwriting any existing destination files, create their backup.',
'Command to create shortcut fileshortcut of file. Create a backup of existing file named fileshortcut.',
'Single command to create a hard link fileshortcut of the file named file in the current folder. Instead of overwriting any existing file titled fileshortcut, create its backup.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -l file_4.txt /home/pungki/office','NL Queries':['How do I create a hard link of file file4.txt to /home/pungki/office directory? Create a backup of any existing destination files.',
'How do I create a shortcut for a file file4.txt in /home/pungki/office? Instead of overwriting any existing destination files, create their backup.',
'Command to create shortcut for a file file4.txt and place it in a directory /home/pungki/office. Do not overwrite any existing files, instead create their backup.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -L file_6.txt ./movie','NL Queries':['How do I get the original source file file_6.txt from symbolic link in ./movie? Create a backup of any existing destination files.',
'Command to get the source file file_6.txt from symbolic link in ./movie. Instead of overwriting any existing destination files, create their backup.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -n instructions.txt backup','NL Queries':['Create a copy of instructions.txt named backup. Copy only if backup not present in current folder. Create a backup of any existing destination files.',
'How do I copy instructions.txt to backup without overwriting it. Instead of overwriting any existing destination files, create their backup.',
'Copy instructions.txt and name it backup. Do not overwrite if backup exists. Do not overwrite any existing files, instead create their backup.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -P file_6.txt ./movie','NL Queries':['How do I copy file file_6.txt with symbolic link as it is to ./movie? Create a backup of any existing destination files.',
'Copy file file_6.txt with symbolic link as it is into another file ./movie. Instead of overwriting any existing destination files, create their backup.',
'Copy file file_6.txt to ./movie. Copy symbolic links as they are. Do not overwrite any existing files, instead create their backup.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -r dir1 dir2','NL Queries':['Copy entire directory structure dir1 to dir2. Create a backup of any existing destination files.',
'How do I copy the files and folders inside dir1 recursively into dir2? Instead of overwriting any existing destination files, create their backup.',
'Copy all files and folders inside dir1 to dir2','Command to copy files and folders in dir1 to dir2 recursively. Do not overwrite any existing files, instead create their backup.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple --remove-destination file1.txt file2.txt','NL Queries':['How do I overwrite an existing file2.txt with contents from file1.txt? Create a backup of any existing destination files.',
'Remove the file2.txt. Recreate it with contents from file1.txt. Instead of overwriting any existing destination files, create their backup.',
'How do I delete file2.txt and replace it with contents from file1.txt? Do not overwrite any existing files, instead create their backup.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -s file.txt file2.txt','NL Queries':['Create symbolic link file2.txt to point to file1.txt. Create a backup of any existing destination files.',
'How to create symbolic link for file1.txt with the name file1.txt? Instead of overwriting any existing destination files, create their backup.',
'Create symbolic link file2.txt for file1.txt. Do not overwrite any existing files, instead create their backup.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -s ~/myfiles/file*.txt ~/myfiles2','NL Queries':['Create a symbolic link of multiple files starting with \'file\' in ~/myfiles directory as ~/myfiles2. Create a backup of any existing destination files.',
'How to create symbolic links for multiple files starting with \'file\' in ~/myfiles folder as ~/myfiles2? Instead of overwriting any existing destination files, create their backup.',
'Command to create a symbolic links for files starting with \'file\' in ~/myfiles folder with name ~/myfiles2. Do not overwrite any existing files, instead create their backup.']},ignore_index=True)

cp = cp.append({'Command':'cp --backup=simple -u * ananya','NL Queries':['Copy all files in this folder to ananya only if they are not present in ananya or if they are newer than source file. Create a backup of any existing destination files.',
'Update folder ananya by copying files from this directory. Update only if file not present in ananya and if the file is newer than source file. Instead of overwriting any existing destination files, create their backup.',
'How do I copy all files from this folder to ananya making sure only the files which need to be updated or which don\'t exist are copied. Do not overwrite any existing files, instead create their backup.']},ignore_index=True)

### -f 

cp = cp.append({'Command':'cp -f -a directory_1/ /home/pungki/office','NL Queries':['How do I copy all files including symbolic links in directory_1 to absolute path /home/pungki/office? If an existing destination file cannot be opened, remove it and try again.',
'Forcefully copy files and folders including symbolic links in directory_1 to office folder in /home/pungki.',
'How do I copy all symbolic links, files and folders from directory_1 to /home/pungki/office? If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -f --attributes-only file1.txt file2.txt','NL Queries':['How do I copy only the attributes of file1 to file2? If an existing destination file cannot be opened, remove it and try again.',
'Forcefully Get the file attributes of file1 and copy it to file2.',
'How do I copy ownership and timestamp from file1 to file2? If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -b *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt. If an existing destination file cannot be opened, remove it and try again.',
'How to forcefully copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office?',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory? If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -l file fileshortcut','NL Queries':['How do I create a shortcut of file under the name fileshortcut?',
'Create a shortcut of a file \'fileshortcut\' in the same directory. If an existing destination file cannot be opened, remove it and try again.',
'Command to forcefully create shortcut fileshortcut of file.',
'Single command to create a hard link fileshortcut of the file named file in the current folder. If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -l file_4.txt /home/pungki/office','NL Queries':['How do I create a hard link of file file4.txt to /home/pungki/office directory? If an existing destination file cannot be opened, remove it and try again.',
'How do I forcefully create a shortcut for a file file4.txt in /home/pungki/office?',
'Command to create shortcut for a file file4.txt and place it in a directory /home/pungki/office. If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -L file_6.txt ./movie','NL Queries':['How do I get the original source file file_6.txt from symbolic link in ./movie? If an existing destination file cannot be opened, remove it and try again.',
'Command to forcefully get the source file file_6.txt from symbolic link in ./movie. If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -P file_6.txt ./movie','NL Queries':['How do I copy file file_6.txt with symbolic link as it is to ./movie? If an existing destination file cannot be opened, remove it and try again.',
'Forcefully Copy file file_6.txt with symbolic link as it is into another file ./movie.',
'Copy file file_6.txt to ./movie. Copy symbolic links as they are. If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -r dir1 dir2','NL Queries':['Copy entire directory structure dir1 to dir2. If an existing destination file cannot be opened, remove it and try again.',
'How do I forcefully copy the files and folders inside dir1 recursively into dir2?',
'Copy all files and folders inside dir1 to dir2. If an existing destination file cannot be opened, remove it and try again.',
'Command to forcefully copy files and folders in dir1 to dir2 recursively.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -s file.txt file2.txt','NL Queries':['Create symbolic link file2.txt to point to file1.txt. If an existing destination file cannot be opened, remove it and try again.',
'How to forcefully create symbolic link for file1.txt with the name file1.txt with cp command?',
'Create symbolic link file2.txt for file1.txt with cp command. If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -s ~/myfiles/file*.txt ~/myfiles2','NL Queries':['Create a symbolic link of multiple files starting with \'file\' in ~/myfiles directory as ~/myfiles2. If an existing destination file cannot be opened, remove it and try again.',
'How to forcefully create symbolic links for multiple files starting with \'file\' in ~/myfiles folder as ~/myfiles2?',
'Command to create a symbolic links for files starting with \'file\' in ~/myfiles folder with name ~/myfiles2. If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

cp = cp.append({'Command':'cp -f -u * ananya','NL Queries':['Copy all files in this folder to ananya only if they are not present in ananya or if they are newer than source file. If an existing destination file cannot be opened, remove it and try again.',
'Forcefully Update folder ananya by copying files from this directory. Update only if file not present in ananya and if the file is newer than source file.',
'How do I copy all files from this folder to ananya making sure only the files which need to be updated or which don\'t exist are copied. If an existing destination file cannot be opened, remove it and try again.']},ignore_index=True)

### -i -v

cp = cp.append({'Command':'cp -i -a -v directory_1/ /home/pungki/office','NL Queries':['How do I copy all files including symbolic links in directory_1 to absolute path /home/pungki/office with details of what is being done? Prompt before overwriting existing destination files.',
'Copy files and folders including symbolic links in directory_1 to office folder in /home/pungki. Show all details of what is being done.  Prompt before overwriting existing destination files.',
'How do I copy all symbolic links, files and folders from directory_1 to /home/pungki/office in interactive mode? Also, give information about what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i --attributes-only -v file1.txt file2.txt','NL Queries':['How do I copy only the attributes of file1 to file2 in verbose mode? Prompt before overwriting existing destination files.',
'Get the file attributes of file1 and copy it to file2 in verbose mode. Prompt before overwriting existing destination files.',
'How do I copy ownership and timestamp from file1 to file2 in interactive mode? Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i --backup=simple -v *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt in verbose mode. Prompt before overwriting existing destination files.',
'How to copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office in verbose mode? Prompt before overwriting existing destination files.',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory in interactive mode? Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -b -v *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt in verbose mode. Prompt before overwriting existing destination files.',
'How to copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office in verbose mode? Prompt before overwriting existing destination files.',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory in interactive mode? Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -v new1.txt new2.txt','NL Queries':['How do I forcefully copy new1.txt to new2.txt in verbose mode? Prompt before overwriting existing destination files.',
'Copy new1.txt to new2.txt by removing new2.txt and trying again if it cannot be opened in verbose mode. Prompt before overwriting existing destination files.',
'Copy new1.txt to new2.txt in interactive mode. If destination file new2.txt cannot be opened, remove it and try again. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -l -v file fileshortcut','NL Queries':['How do I create a shortcut of file under the name fileshortcut in verbose mode? Prompt before overwriting existing destination files.',
'Create a shortcut of a file \'fileshortcut\' in the same directory in verbose mode. Prompt before overwriting existing destination files.',
'Command to create shortcut fileshortcut of file in verbose mode. Prompt before overwriting existing destination files.',
'Single command to create a hard link fileshortcut of the file named file in the current folder in interactive mode. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -l -v file_4.txt /home/pungki/office','NL Queries':['How do I create a hard link of file file4.txt to /home/pungki/office directory in verbose mode? Prompt before overwriting existing destination files.',
'How do I create a shortcut for a file file4.txt in /home/pungki/office in verbose mode? Prompt before overwriting existing destination files.',
'Command to create shortcut for a file file4.txt and place it in a directory /home/pungki/office in interactive mode. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -L -v file_6.txt ./movie','NL Queries':['How do I get the original source file file_6.txt from symbolic link in ./movie in verbose mode? Prompt before overwriting existing destination files.',
'Command to get the source file file_6.txt from symbolic link in ./movie in interactive mode. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -p -v /etc/resolv.conf $HOME','NL Queries':['Copy all attributes along with the file /etc/resolv.conf to home. Show the files copied. Prompt before overwriting existing destination files.',
'How do I copy /etc/resolve.conf file to home directory along with attributes and display the files copied? Prompt before overwriting existing destination files.',
'Command to copy /etc/resolv.conf to home along with the attributes in interactive mode and list the files copied.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -r -v dir1 dir2','NL Queries':['How do I copy recursively from dir1 to dir2 and get to know what is being copied? Prompt before overwriting existing destination files.',
'Copies all files and folders from dir1 to dir2. Display information on what is being copied. Prompt before overwriting existing destination files.',
'How do I copy all files and folders from dir1 to dir2 in interactive mode and get information on what is being copied?']},ignore_index=True)

cp = cp.append({'Command':'cp -i --remove-destination -v file1.txt file2.txt','NL Queries':['How do I overwrite an existing file2.txt with contents from file1.txt in verbose mode? Prompt before overwriting existing destination files.',
'Remove the file2.txt. Recreate it with contents from file1.txt in verbose mode. Prompt before overwriting existing destination files.',
'How do I delete file2.txt and replace it with contents from file1.txt in interactive mode? Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -s -v file.txt file2.txt','NL Queries':['Create symbolic link file2.txt to point to file1.txt in verbose mode. Prompt before overwriting existing destination files.',
'How to create symbolic link for file1.txt with the name file1.txt in verbose mode? Prompt before overwriting existing destination files.',
'Create symbolic link file2.txt for file1.txt with cp command in interactive mode. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -s -v ~/myfiles/file*.txt ~/myfiles2','NL Queries':['Create a symbolic link of multiple files starting with \'file\' in ~/myfiles directory as ~/myfiles2 in verbose mode. Prompt before overwriting existing destination files.',
'How to create symbolic links for multiple files starting with \'file\' in ~/myfiles folder as ~/myfiles2 in verbose mode? Prompt before overwriting existing destination files.',
'Command to create a symbolic links for files starting with \'file\' in ~/myfiles folder with name ~/myfiles2 in interactive mode. Explain what is being done.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -u -v * ananya','NL Queries':['Copy all files in this folder to ananya only if they are not present in ananya or if they are newer than source file in verbose mode. Prompt before overwriting existing destination files.',
'Update folder ananya by copying files from this directory in verbose mode. Update only if file not present in ananya and if the file is newer than source file. Prompt before overwriting existing destination files.',
'How do I copy all files from this folder to ananya in interactive mode making sure only the files which need to be updated or which don\'t exist are copied. Explain what is being done.']},ignore_index=True)

### -i -f 

cp = cp.append({'Command':'cp -i -f -a directory_1/ /home/pungki/office','NL Queries':['How do I copy all files including symbolic links in directory_1 to absolute path /home/pungki/office? If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'Forcefully copy files and folders including symbolic links in directory_1 to office folder in /home/pungki. Do this in interactive mode.',
'How do I copy all symbolic links, files and folders from directory_1 to /home/pungki/office? If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f --attributes-only file1.txt file2.txt','NL Queries':['How do I copy only the attributes of file1 to file2? If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'Forcefully Get the file attributes of file1 and copy it to file2. Do this in interactive mode.',
'How do I copy ownership and timestamp from file1 to file2? If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -b *.txt ../office','NL Queries':['Create a backup of each existing destination file in office folder in parent directory while copying all files ending with .txt. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'How to forcefully copy all files ending with .txt to ../office and create a backup for existing destination files in relative path ../office? Do this in interactive mode.',
'How to keep the existing files instead of overwriting while copying all .txt files to office folder in parent directory? If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -l file fileshortcut','NL Queries':['How do I create a shortcut of file under the name fileshortcut?',
'Create a shortcut of a file \'fileshortcut\' in the same directory. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'Command to forcefully create shortcut fileshortcut of file. Do this in interactive mode.',
'Single command to create a hard link fileshortcut of the file named file in the current folder. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -l file_4.txt /home/pungki/office','NL Queries':['How do I create a hard link of file file4.txt to /home/pungki/office directory? If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'How do I forcefully create a shortcut for a file file4.txt in /home/pungki/office? Do this in interactive mode.',
'Command to create shortcut for a file file4.txt and place it in a directory /home/pungki/office. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -L file_6.txt ./movie','NL Queries':['How do I get the original source file file_6.txt from symbolic link in ./movie? If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'Command to forcefully get the source file file_6.txt from symbolic link in ./movie. If an existing destination file cannot be opened, remove it and try again. Do this in interactive mode.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -P file_6.txt ./movie','NL Queries':['How do I copy file file_6.txt with symbolic link as it is to ./movie? If an existing destination file cannot be opened, remove it and try again.',
'Forcefully Copy file file_6.txt with symbolic link as it is into another file ./movie. Do this in interactive mode.',
'Copy file file_6.txt to ./movie. Copy symbolic links as they are. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -r dir1 dir2','NL Queries':['Copy entire directory structure dir1 to dir2. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'How do I forcefully copy the files and folders inside dir1 recursively into dir2? Do this in interactive mode.',
'Copy all files and folders inside dir1 to dir2. If an existing destination file cannot be opened, remove it and try again. Do this in interactive mode.',
'Command to forcefully copy files and folders in dir1 to dir2 recursively. Prompt before overwriting existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -s file.txt file2.txt','NL Queries':['Create symbolic link file2.txt to point to file1.txt. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'How to forcefully create symbolic link for file1.txt with the name file1.txt? Do this in interactive mode.',
'Create symbolic link file2.txt for file1.txt. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -s ~/myfiles/file*.txt ~/myfiles2','NL Queries':['Create a symbolic link of multiple files starting with \'file\' in ~/myfiles directory as ~/myfiles2. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'How to forcefully create symbolic links for multiple files starting with \'file\' in ~/myfiles folder as ~/myfiles2? Do this in interactive mode.',
'Command to create a symbolic links for files starting with \'file\' in ~/myfiles folder with name ~/myfiles2. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.']},ignore_index=True)

cp = cp.append({'Command':'cp -i -f -u * ananya','NL Queries':['Copy all files in this folder to ananya only if they are not present in ananya or if they are newer than source file. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.',
'Forcefully update folder ananya by copying files from this directory. Update only if file not present in ananya and if the file is newer than source file. Do this in interactive mode.',
'How do I copy all files from this folder to ananya making sure only the files which need to be updated or which don\'t exist are copied. If an existing destination file cannot be opened, remove it and try again. Prompt before overwriting existing destination files.']},ignore_index=True)

#####

cp = cp.append({'Command':'cp --help','NL Queries':['How to get help with information on cp command?','Display all the option available with cp command.','List all the flags available with cp command.','Where can I find help with cp command?']},ignore_index=True)

cp = cp.append({'Command':'cp --version','NL Queries':['How do I get to know the version of cp command?','List the version of the cp command.','How to get the version and license of the cp command?','Where to find version,author,license regarding cp command?']},ignore_index=True)

#cp = cp.append({'Command':'cp file*.jpg /directory/subdirectory','NL Queries':['Copy all files beginning with \'file\' and having .jpg destination to given absolute path.',
#				'How do I copy .jpg files beginning with \'file\' to given absolute path?',
#					'Command to copy files like file1.jpg, file2.jpg, etc to given destination']},ignore_index=True)

#cp = cp.append({'Command':'cp /home/chuck/pictures/picture.jpg /home/chuck/backup/picture.jpg','NL Queries':['How to copy file when source /home/chuck/pictures/picture.jpg and destination /home/chuck/backup/picture.jpg exist in different directories?',
#			'How do I copy file from absolute path /home/chuck/pictures/picture.jpg to /home/chuck/backup/picture.jpg',
#				'Copy files when source /home/chuck/pictures/picture.jpg and destination /home/chuck/backup/picture.jpg is different.']},ignore_index=True)

#cp = cp.append({'Command':'cp ~/pictures/picture-*.jpg ~/picture-backup','NL Queries':['How to backup pictures \'picture(x).jpg\' from ~/pictures to ~/picture-backup?',
#			'Copy pictures starting with \'picture\' with extension.jpg from source to destination']},ignore_index=True)

#cp = cp.append({'Command':'cp * ../dir1','NL Queries':['Copy all the files in the current directory to dir1 in the parent directory.',
#			'How do I copy all the files in the current directory to dir1 in the parent directory?']},ignore_index=True)

#cp = cp.append({'Command':'cp src /home/usr/rapid/','NL Queries':['Copy directory src to absolute path directory /home/usr/rapid/',
#				'How do I copy a directory src in the current folder to a given absolute path /home/usr/rapid/?',
#					'How do I copy src folder to the folder present in /home/usr/rapid/?']},ignore_index=True)


print cp.shape
