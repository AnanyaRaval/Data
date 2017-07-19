import pandas as pd 

rm = pd.DataFrame(columns = ['Command','NL Queries'])

#[-dfiIrv] are the various options as per --help

# r and d generally meant for directories as per --help though work on files too.
#rm -fi takes i(same as i) and -if takes f(same as f) so f and i do not come in one command. So is applied for I and f.
#warning r and d is deleting even files not just directories.So careful while using r.
#-I option is same like -i for except it ask prompt for once if number of deleting files are more than 3.

#I have used -d and -r for folders even though they work for files, if you want do inform i will edit NL Queries.
#I have commented out few commands containing -I option because -I works best for removing more than 3 files than just a file at a time.(prompt once for all).

rm = rm.append({'Command':'rm abc.txt efg.py cdf','NL Queries':['Command to remove the following files: abc.txt,efg.py and cdf.',
	'Remove multiple files : abc.txt, efg.py, cdf.','How to remove the following files: abc.txt,efg.py and cdf?',
	'Command to delete the following files: abc.txt,efg.py and cdf.','Delete multiple files : abc.txt, efg.py, cdf.',
	'How to delete the following files: abc.txt,efg.py and cdf?','How do I delete multiple files abc.txt,efg.py and cdf?',
	'How do I remove multiple files abc.txt,efg.py and cdf?']},ignore_index=True)
rm = rm.append({'Command':'rm -f file{1..5}.txt','NL Queries':['Remove all files with names starting with file, ending with .txt and numbers 1 to 5 in between.',
	'Remove 5 files, names start with the word file, have numbers 1 to 5 after,end with .txt',
	'How to remove all files with names starting with file, ending with .txt and numbers 1 to 5 in between?',
	'Delete all files with names starting with file, ending with .txt and numbers 1 to 5 in between.',
	'Delete 5 files, names start with the word file, have numbers 1 to 5 after,end with .txt',
	'How to delete all files with names starting with file, ending with .txt and numbers 1 to 5 in between?']},ignore_index=True)
rm = rm.append({'Command':'rm -I file{1..5}.txt','NL Queries':['Remove all files with names starting with file, ending with .txt and numbers 1 to 5 in between after prompting once.',
	'Remove 5 files, names start with the word file, have numbers 1 to 5 after,end with .txt. Prompt once for all.',
	'How to remove all files with names starting with file, ending with .txt and numbers 1 to 5 in between and prompting only once?',
	'Delete all files with names starting with file, ending with .txt and numbers 1 to 5 in between with prompting once.',
	'Delete 5 files, names start with the word file, have numbers 1 to 5 after,end with .txt. Prompt once for all.',
	'How to delete all files with names starting with file, ending with .txt and numbers 1 to 5 in between and prompting only once?',
	'Delete files with name starting with \'file\', followed by numbers 1,2,3,4,5 and ending with \'.txt\' in the current folder.']},ignore_index=True)
rm = rm.append({'Command':'rm *','NL Queries':['Remove all files from the current directory.',
			'Empty folder by removing all files.','How to remove all files?',
			'How to empty folder by removing all files?','Delete all files present in the current directory.',
			'Empty this folder by deleting all files.','How to delete all files?',
			'How to empty folder by deleting all files in the current folder?']},ignore_index = True)
rm = rm.append({'Command':'rm l*','NL Queries':['Remove all files starting letter \'l\'.',
			'How to remove all files starting with \'l\'?',
			'Delete all files starting letter \'l\'.',
			'How to delete all files starting with \'l\'?',
			'Delete all files starting with letter \'l\' and which are present in the current folder.']},ignore_index = True)
rm = rm.append({'Command':'rm *.py','NL Queries':['Remove all files of type .py.','How to remove all files of type .py?',
			'Delete all files of type .py.','How to delete all files of type .py?',
			'Remove all files ending with \'.py\' from the current directory.',
			'How do I delete files ending with \'.py\' present in the current folder.']},ignore_index = True)
rm = rm.append({'Command':'rm file?','NL Queries':['Remove all files starting with \'file\' and have one more number.',
			'How to remove all files starting with \'file\' and have one more number?',
			'Delete all files starting with \'file\' and have one more number.','How to delete all files starting with \'file\' and have one more number?',
			'Remove files starting with \'file\' and followed by one number.','Delete files starting with \'file\' and followed by one number.',
			'Delete all files whose name start with \'file\', followed by exactly one number in the current folder.']},ignore_index = True)
#'rm --' for files starting with one or more '-'
rm = rm.append({'Command':'rm -- -linuxfile.log','NL Queries':['Remove a file which starts with \'-\'.',
			'Command to remove a file which starts with \'-\'.','How do I remove a file from the current folder with starting from \'-\'?',
			'Delete a file which starts with \'-\'.','Command to delete a file which starts with \'-\' followed by many characters.',
			'How do I delete a file with it\' name starting with \'-\'?']},ignore_index = True)

rm = rm.append({'Command':'rm linuxfile.log','NL Queries':['Remove file linuxfile.log.','Command to remove linuxfile.log.',
			'How to remove file linuxfile.log.','Delete file linuxfile.log from the current directory.','Command to delete linuxfile.log.',
			'How to delete file linuxfile.log.','Delete linuxfile.log from this folder.']},ignore_index = True)

rm = rm.append({'Command':'rm -d linuxfile','NL Queries':['Remove linuxfile folder if empty.','Command to remove empty folder linuxfile .',
			'How to remove empty folder linuxfile?','How do I remove linuxfile folder if empty?',
				'Delete linuxfile folder if empty.','Command to delete empty folder linuxfile from this foldeer.',
				'How to delete empty folder linuxfile?','How do I delete linuxfile folder,present in this folder, if empty?']},ignore_index = True)
rm = rm.append({'Command':'rm -f linuxfile.log','NL Queries':['Remove file linuxfile.log if present else ignore.',
			'Command to remove file linuxfile.log if present else ignore.','How to remove a file linuxfile.log if present else ignore?',
				'Delete file linuxfile.log.','Command to delete file linuxfile.log.',
					'How to delete a file linuxfile.log if present?',]},ignore_index = True)
rm = rm.append({'Command':'rm -i linuxfile.log','NL Queries':['Remove file linuxfile.log with a prompt.',
			'Remove file linuxfile.log with a confirmation before removing.','Delete file linuxfile.log with a confirmation before removing.',
			'Remove file linuxfile.log. Prompt before removing.','Delete file linuxfile.log. Prompt before deleting.',
			'Command to remove linuxfile.log  with prompting before removing the file.','Command to remove file linuxfile.log with prompt.',
			'How to remove a file linuxfile.log with a prompt before removing the file?','Delete file linuxfile.log with a prompt.',
				'Command to delete linuxfile.log  with prompting before deleting the file.','Command to delete file linuxfile.log with a prompt for confirmation.',
		'How to delete a file linuxfile.log? It should show a prompt before deletion.']},ignore_index = True)
#rm = rm.append({'Command':'rm -I linuxfile.log','NL Queries':['Remove file linuxfile.log .','remove file linuxfile.log.','Command to remove linuxfile.log .','Command to remove file linuxfile.log .']},ignore_index = True)
rm = rm.append({'Command':'rm -r linuxfile','NL Queries':['Remove linuxfile folder and it\'s contents.','Remove linuxfile folder completely.','Delete linuxfile folder completely.',
			'Command to remove linuxfile folder and it\'s content.','How to remove folder linuxfile and all files and folder present in it?',
			'Delete linuxfile folder and it\'s all of it\'s contents.','Command to delete linuxfile folder and it\'s contents.',
			'How to delete folder linuxfile and all of it\'s content?']},ignore_index = True)
rm = rm.append({'Command':'rm -v linuxfile.log','NL Queries':['Remove file linuxfile.log with an explanation of what is been removed.',
			'Command to remove linuxfile.log. Show a list of contents being removed.','How to remove a file linuxfile.log along with showing a list of what is being removed?',
			'Delete file linuxfile.log with list of what is been deleted.','Command to delete linuxfile.log , with log of what is being deleted.',
			'How to delete a file linuxfile.log? Show a list of content being deleted?','Delete \'linuxfile.log\'. Show a list of content being removed.']},ignore_index = True)

rm = rm.append({'Command':'rm -df linuxfile','NL Queries':['Remove folder linuxfile if empty else ignore.',
						'Remove folder linuxfile.','Delete folder linuxfile present in this folder.','Command to remove linuxfile folder if empty.',
						'How to remove a folder linuxfile present if empty else ignore?','Delete folder linuxfile if empty else ignore.',
						'Command to delete linuxfile folder if empty.','How to delete a folder linuxfile present in this directory? Delete only if empty.',
						'Command to delete empty folder linuxfile in this folder. Delete only if empty.']},ignore_index = True)
rm = rm.append({'Command':'rm -di linuxfile','NL Queries':['Remove folder linuxfile if empty with a prompt.',
				'Remove folder linuxfile if empty. Confirm before removing.','Delete folder linuxfile if empty. Confirm before deleting.',
				'Command to remove linuxfile folder if empty with a prompt.','How to remove a folder linuxfile if empty with a prompt?',
				'Delete folder linuxfile if empty with a prompt.','Command to delete linuxfile folder if empty with a prompt.',
					'How to delete a folder linuxfile if empty with a prompt?', 'Delete \'linuxfile\' from this directory. Delete only if empty and prompt before deletion.']},ignore_index = True)
#rm = rm.append({'Command':'rm -dI linuxfile','NL Queries':['Remove file linuxfile.','Command to remove linuxfile.log .','Command to remove file linuxfile.log .']},ignore_index = True)
rm = rm.append({'Command':'rm -dv linuxfile','NL Queries':['Remove folder linuxfile if empty with a log.',
		'Remove folder linuxfile if empty. Show log of what is being removed.','Delete folder linuxfile if empty. Show log of what is being deleted.',
		'Command to remove linuxfile folder if empty with a log.','How to remove a folder linuxfile if empty with a log of what is being removed?',
		'Delete folder linuxfile if empty with a log?','Command to delete linuxfile folder if empty with a log.',
		'How to delete an empty folder linuxfile? Show a log of what is being deleted.']},ignore_index = True)
rm = rm.append({'Command':'rm -dfv linuxfile','NL Queries':['Remove folder linuxfile  from this directory if it\'s empty. Show a log what is being deleted.',
			'Command to remove linuxfile folder if empty with a log else ignore.','How to remove a folder linuxfile if empty with a log else ignore?',
			'Delete folder linuxfile if empty with a log on command line, else ignore.','Command to delete linuxfile folder if empty with a log on display, else ignore.',
			'How to delete a folder linuxfile if empty with a log else ignore?','Delete empty folder \'linuxfile\' from this directory. If deleted, keep a log of what is being deleted.']},ignore_index = True)

rm = rm.append({'Command':'rm -fr linuxfile','NL Queries':['Remove linuxfile folder and it\'s content if present else ignore.',
			'Remove linuxfile folder completely if it is present. Ignore the command if there is no folder of that name.',
			'Delete linuxfile folder completely if it is present else ignore.','Command to remove linuxfile folder and it\'s content if present else ignore.',
			'How to remove folder linuxfile and it\'s content if it\'s present? Ignore otherwise.','Delete linuxfile folder, if it exists, and all of it\'s content.',
			'Command to delete linuxfile folder and it\'s content if present else ignore.','How to delete folder linuxfile and it\'s content if present else ignore?']},ignore_index = True)
rm = rm.append({'Command':'rm -fv linuxfile.log','NL Queries':['Remove file linuxfile.log if present with a log else ignore.',
			'Command to remove linuxfile.log if with a log present else ignore.','How to remove a file linuxfile.log from this folder. Delete only if it exists, otherwise ignore.',
			'Delete file linuxfile.log if present with a log else ignore.','Command to delete linuxfile.log if with a log present else ignore.',
			'How to delete a file linuxfile.log if present with a log else ignore.','How do I delete linuxfile.log,if present, from this directory? Ignore the command if it doesn\'t exist.']},ignore_index = True)

rm = rm.append({'Command':'rm -ri linuxfile','NL Queries':['Remove linuxfile folder and it\'s content with a prompt.',
				'Command to remove linuxfile folder and it\'s content with prompt.','How to remove folder linuxfile and it\'s content with prompt?',
				'Delete linuxfile folder and it\'s content with a prompt.','Command to delete linuxfile folder and it\'s content with prompt.',
				'How to delete folder linuxfile and it\'s content with prompt?','Delete linuxfile and all of it\'s contents. Show a prompt before deletion.']},ignore_index = True)
#rm = rm.append({'Command':'rm -rI linuxfile.log','NL Queries':['Remove file linuxfile.log.','Command to remove linuxfile.log .','Command to remove file linuxfile.log .']},ignore_index = True)
rm = rm.append({'Command':'rm -rv linuxfile','NL Queries':['Remove linuxfile folder and it\'s content. Show a log of the content along with the deletion.',
				'Remove folder linuxfile and it\'s content. Show log of what is being removed.','Delete folder linuxfile and it\'s content. Show list of what is being deleted.',
					'Command to remove linuxfile folder and it\'s content with a display of contents being deleted.','How to remove folder linuxfile and it\'s content?Show log on the command line.',
						'Delete linuxfile folder and it\'s content with log.','Command to delete linuxfile folder and it\'s content. List contents being deleted.',
						'How to delete folder linuxfile and all of it\'s contents along with a verbose explanation of what is being deleted?']},ignore_index = True)

rm = rm.append({'Command':'rm -riv linuxfile','NL Queries':['Remove linuxfile folder and it\'s content with a prompt and log.',
	'Remove linuxfile folder and it\'s content. Confirm before deleting and show log of what is being removed.',
	'Delete linuxfile folder and it\'s content. Confirm before deleting and show log of the content being deleted.',
	'Command to remove linuxfile folder and it\'s content with prompt and log.','How to remove folder linuxfile and it\'s content after a prompt and a log of contents on the command line?',
	'Delete linuxfile folder and it\'s content with a prompt and log.','Command to delete linuxfile fz,older and it\'s content with prompt and log.',
	'How to delete folder linuxfile and it\'s content with prompt and log?','Delete linuxfile from current directory. Show a prompt before deletion and list all files and folders being deleted.']},ignore_index = True)
#rm = rm.append({'Command':'rm -rIv linuxfile.log','NL Queries':['Remove file linuxfile.log.','Command to remove linuxfile.log .','Command to remove file linuxfile.log .']},ignore_index = True)

rm = rm.append({'Command':'rm -vi linuxfile.log','NL Queries':['Remove file linuxfile.log along with log of what is been removed and a prompt before removing.',
	'Remove file linuxfile.log.Show what is being removed and confirm before removing.',
	'Delete file linuxfile.log.Show the content being removed and confirm before deleting.',
	'Command to remove linuxfile.log , with log of what is being removed and prompt before removing.',
	'How to remove a file linuxfile.log with a log of what is being removed and prompting before removing?',
	'Delete file linuxfile.log with log of what is been deleted and prompt before the deletion.',
	'Command to delete linuxfile.log , with a display of list of what is being deleted and prompt before deleting.',
	'How to delete a file linuxfile.log ? Show a list of files and folders being deleted after a prompt confirming deletion?']},ignore_index = True)
#rm = rm.append({'Command':'rm -vI linuxfile.log','NL Queries':['Remove file linuxfile.log.','Command to remove linuxfile.log .','Command to remove file linuxfile.log .']},ignore_index = True)

#i am not sure whether find is allowed in rm for your project
rm = rm.append({'Command':'find foo -type f -mtime -1 -exec rm -i {} \;','NL Queries':['Remove file foo which has been modified in the last day and remove them interactively.','Command to remove file foo which has been modified in the last day and remove them interactively.','How to remove file foo which has been modified in the last day and remove them interactively?','Delete file foo which has been modified in the last day and delete them interactively.','Command to delete file foo which has been modified in the last day and delete them interactively.','How to delete file foo which has been modified in the last day and delete them interactively?']},ignore_index = True)


print rm.shape