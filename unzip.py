import pandas as pd 

unzip = pd.DataFrame(columns = ['Command','NL Queries'])

unzip = unzip.append({'Command':'unzip letters.zip',
					'NL Queries':['Extract all files and sub directories in the archive named letters.',
								'Uncompress the letters archive and store all the files in current folder and sub directories below the current folder.',
								'How do I extract all files of letters.zip to this directory and subdirectories in corresponding subdirectories ?']},ignore_index=True)

unzip = unzip.append({'Command':'unzip letters.zip template.zip music.zip',
					'NL Queries':['Extract all files and sub directories in the archive named letters , template and music.',
								'Uncompress the letters , template and music archive and store all the files in current folder and sub directories below the current folder.',
								'How do I extract all files of letters.zip , template.zip and music.zip to this directory and subdirectories in corresponding subdirectories ?']},ignore_index=True)


unzip = unzip.append({'Command':'unzip Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash.',
								'How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash ?',
								'Extract Trash.zip in this directory to /home/music/Alice/Cooper/Trash.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip Trash.zip -d /home/music/Alice Cooper/Trash /home/music/ALL/Trash',
					'NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash and /home/music/ALL/Trash.',
								'How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash and /home/music/ALL/Trash?',
								'Extract Trash.zip in this directory to /home/music/Alice/Cooper/Trash and /home/music/ALL/Trash.']},ignore_index=True)


unzip = unzip.append({'Command':'unzip letters.zip -x file1',
					'NL Queries':['How do I extract all contents of letters.zip except file1 ?',
								'Uncompress letters.zip except file1 from letters.zip.',
								'Extract letters.zip. Do not extract file1.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip letters.zip -x file1 file2',
					'NL Queries':['How do I extract all contents of letters.zip except file1 and file2 ?',
								'Uncompress letters.zip except file1 and file2 from letters.zip.',
								'Extract letters.zip. Do not extract file1 and file2.']},ignore_index=True)


unzip = unzip.append({'Command':'unzip -p letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip to a pipe?',
								'Uncompress letters.zip and place them in pipe.',
								'Extract archive letters.zip files to a pipe without any messages.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -f letters.zip',
					'NL Queries':['How do I extract newer version of files in letters.zip to it\'s current directory itself?',
								'Uncompress newer version of files in letters.zip and store all files and folders in current folder.',
								'Extract newer version of files from letters.zip into current directory. Do not create any new files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -u letters.zip',
					'NL Queries':['How do I update extracted contents of letters.zip?',
								'Update extracted contents of letters.zip and create any files if nessesary.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -v letters.zip',
					'NL Queries':['How do I see complete information of letters.zip?',
								'Display complete information of letters.zip.',]},ignore_index=True)

unzip = unzip.append({'Command':'unzip -l letters.zip',
					'NL Queries':['How do I see brief information of letters.zip?',
								'Display brief information of letters.zip.',]},ignore_index=True)

unzip = unzip.append({'Command':'unzip -t letters.zip',
					'NL Queries':['How do I test compressed archive data of letters.zip?',
								'Test compressed archive data of letters.zip.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -z letters.zip',
					'NL Queries':['How do I display archive comment only of letters.zip?',
								'Display archive comment only of letters.zip.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -T letters.zip',
					'NL Queries':['How do I change timestamp to latest for letters.zip?',
								'Change timestamp archive to latest for letters.zip.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -n letters.zip',
					'NL Queries':['How do I extract contents of letters.zip? Do not overwrite existing extracted content.',
								'Uncompress letters.zip and do not overwrite existing extracted content.',
								'Extract letters.zip , while extracting do not overwrite extracting extracted content.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -o letters.zip',
					'NL Queries':['How do I extract contents of letters.zip? Overwrite existing extracted content.',
								'Uncompress letters.zip and overwrite existing extracted content.',
								'Extract archive letters.zip , while extracting overwrite extracting extracted content.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -j letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip to this directory itself?',
								'Uncompress letters.zip and store all files and folders in this folder.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -U letters.zip',
					'NL Queries':['How do I extract contents of letters.zip and use escapes for all non-ASCII unicode characters?',
								'Uncompress letters.zip and use escapes for all non-ASCII unicode characters.',
								'Extract letters.zip and use escapes for all non-ASCII unicode characters.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -C letters',
					'NL Queries':['How do I extract contents of files named letters ? Search file names with case-insensitively.',
								'Uncompress all files named letters and do not consider case while searching files.',
								'Extract all files named as letters , match files names case-insensitively.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -K letters.zip',
					'NL Queries':['How do I extract contents of letters.zip and keep setuid or setgid or tacky permissions?',
								'Uncompress letters.zip and set setuid or setgid or tacky permissions.',
								'Extract archive letters.zip and keep setuid or setgid or tacky permissions.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -X letters.zip',
					'NL Queries':['How do I extract contents of letters.zip and restore UID or GID info?',
								'Uncompress letters.zip and restore UID or GID info.',
								'Extract archive letters.zip and restore UID or GID info.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -q letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip quietly?',
								'Uncompress letters.zip in quiet mode.',
								'Extract letters.zip in quiet mode.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -a letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip and auto convert nessesary extracted files to text files?',
								'Uncompress letters.zip and auto convert nessesary extracted files to text files.',
								'Extract letters.zip and auto convert nessesary extracted files to text files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -aa letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip and convert all extracted files to text files?',
								'Uncompress letters.zip and convert all extracted files to text files.',
								'Extract letters.zip and convert all extracted files to text files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -UU letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip and ignore any unicode named file names?',
								'Uncompress letters.zip and ignore any unicode named file names.',
								'Extract letters.zip and ignore any unicode named file names.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -L letters.zip',
					'NL Queries':['How do I extract contents of letters.zip ? How do i convert uppercase names to lowercase names ?',
								'Uncompress letters.zip . Convert uppercase names to lowercase names.',
								'Extract archive letters.zip. Convert uppercase names to lowercase names.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -V letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip and retain VMS version number?',
								'Uncompress letters.zip and retain VMS version number.',
								'Extract letters.zip and retain VMS version number.']},ignore_index=True)


unzip = unzip.append({'Command':'unzip -tq letters.zip',
					'NL Queries':['How do I test archive letters.zip quietly?',
								'Test letters.zip quietly.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -j -aa letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip to this directory itself ? How to convert all extracted files to text files.',
								'Uncompress letters.zip , store all files and folders in this folder and convert all extracted files to text files.',
								'Extract letters.zip , store all files and folders in this folder. Convert all extracted files to text files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -Ca letters',
					'NL Queries':['How do I extract contents of all files named letters and auto convert nessesary extracted files to text files? Search file names with case-insensitively.',
								'Uncompress all files named letters , auto convert nessesary extracted files to text files and do not consider case while searching files.',
								'Extract all files named as letters , match files names case-insensitively. Auto convert nessesary extracted files to text files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -uo letters.zip',
					'NL Queries':['How do I extract newer version of files of letters.zip in current directory and create any files if any required ?',
								'Extract newer version of files of letters.zip in current directory and create any files if any required .']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -jU letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip to this directory itself and use escapes for all non-ASCII unicode characters?',
								'Uncompress letters.zip and store all files and folders in this folder and use escapes for all non-ASCII unicode characters.',
								'Extract archive letters.zip and store all files and folders in this folder and use escapes for all non-ASCII unicode characters.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -Kq letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip quietly and keep setuid or setgid or tacky permissions?',
								'Uncompress letters.zip quietly and set setuid or setgid or tacky permissions.',
								'Extract archive letters.zip quietly and keep setuid or setgid or tacky permissions.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -o -UU letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip , ignore any unicode named file names and overwrite existing files?',
								'Uncompress letters.zip , ignore any unicode named file names and overwrite existing files.',
								'Extract letters.zip , ignore any unicode named file names and overwrite existing files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -CL letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip and convert uppercase names to lowercase names ? Do not consider case while searching files.',
								'Uncompress letters.zip . Convert uppercase names to lowercase names. Match files names case-insensitively.',
								'Extract archive letters.zip. Convert uppercase names to lowercase names. Do not consider case while searching files.']},ignore_index=True)


unzip = unzip.append({'Command':'unzip -jn letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip to this directory itself and never overwrite existing files?',
								'Uncompress letters.zip , store all files and folders in this folder and never overwrite existing files.',
								'Extract letters.zip , store all files and folders in this folder and never overwrite existing files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -Xn letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip and restore UID or GID info and do not overwrite existing files?',
								'Uncompress letters.zip , restore UID or GID info and do not overwrite existing files.',
								'Extract archive letters.zip , restore UID or GID info and do not overwrite existing files.']},ignore_index=True)



unzip = unzip.append({'Command':'unzip -jo letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip to this directory itself and overwrite existing files?',
								'Uncompress letters.zip , store all files and folders in this folder and overwrite existing files.',
								'Extract letters.zip , store all files and folders in this folder and overwrite existing files.']},ignore_index=True)


unzip = unzip.append({'Command':'unzip -Xo letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip and restore UID or GID info and overwrite existing files?',
								'Uncompress letters.zip , restore UID or GID info and overwrite existing files.',
								'Extract archive letters.zip , restore UID or GID info and overwrite existing files.']},ignore_index=True)




unzip = unzip.append({'Command':'unzip -Cn letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip? Do not overwrite existing files and match file names case-insensitively.',
								'Uncompress letters.zip. Do not overwrite existing files. Do not consider case while searching files.',
								'Extract letters.zip. Do not overwrite existing files. Do not consider case while searching files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -C -aa letters',
					'NL Queries':['How do I extract contents of all files named letters? Search file names with case-insensitively. Convert all extracted files info text files.',
								'Uncompress all files named letters and do not consider case while searching files. Convert all extracted files info text files.',
								'Extract all files named as letters , match files names case-insensitively. Convert all extracted files info text files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -KqL letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip quietly and keep setuid or setgid or tacky permissions? Convert uppercase names to lowercase names.',
								'Uncompress letters.zip quietly , convert uppercase names to lowercase names and set setuid or setgid or tacky permissions.',
								'Extract archive letters.zip quietly , convert uppercase names to lowercase names and keep setuid or setgid or tacky permissions.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -oq -UU letters.zip',
					'NL Queries':['How do I extract all contents of letters.zip quietly, ignore any unicode named file names and overwrite existing files?',
								'Uncompress letters.zip quietly , ignore any unicode named file names and overwrite existing files.',
								'Extract letters.zip quietly, ignore any unicode named file names and overwrite existing files.']},ignore_index=True)


unzip = unzip.append({'Command':'unzip -q Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress Trash.zip quietly in this directory to /home/music/Alice/Cooper/Trash.',
								'Uncompress Trash.zip quietly in this directory to /home/music/Alice/Cooper/Trash.',
								'How do I decompress archive Trash.zip quietly and store them to /home/music/Alice Cooper/Trash ?',
								'How do I extract content of Trash.zip quietly and store them to /home/music/Alice Cooper/Trash ?',
								'Extract Trash.zip quietly in this directory to /home/music/Alice/Cooper/Trash.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -o Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Overwrite existing files.',
								'Uncompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Overwrite existing files.',
								'How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash and overwrite existing files?',
								'How do I extract content of Trash.zip and store them to /home/music/Alice Cooper/Trash and overwrite existing files?',
								'Extract Trash.zip in this directory to /home/music/Alice/Cooper/Trash and overwrite existing files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -n Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not overwrite existing files.',
								'Uncompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not overwrite existing files.',
								'How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash and do not overwrite existing files?',
								'How do I extract content of Trash.zip and store them to /home/music/Alice Cooper/Trash and do not overwrite existing files?',
								'Extract Trash.zip in this directory to /home/music/Alice/Cooper/Trash and do not overwrite existing files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -j Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress all contents of Trash.zip in this directory to /home/music/Alice/Cooper/Trash.',
								'Uncompress all contents of Trash.zip in this directory to /home/music/Alice/Cooper/Trash.',
								'How do I decompress all contents of archive Trash.zip and store them to /home/music/Alice Cooper/Trash?',
								'How do I extract all contents of Trash.zip and store them to /home/music/Alice Cooper/Trash?',
								'Extract all contents of Trash.zip in this directory to /home/music/Alice/Cooper/Trash.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -C Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not consider case while searching files.',
								'Uncompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Match file names case-insensitively.',
								'How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash and do not consider case while searching files?',
								'How do I extract content of Trash.zip and store them to /home/music/Alice Cooper/Trash and match file names case-insensitively?',
								'Extract Trash.zip in this directory to /home/music/Alice/Cooper/Trash and do not consider case while searching file names.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -jn Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress all contents of Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not overwrite existing files.',
								'Uncompress all contents of Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not overwrite existing files.',
								'How do I decompress all contents of archive Trash.zip and store them to /home/music/Alice Cooper/Trash ? Do not overwrite existing files.',
								'How do I extract all contents of Trash.zip and store them to /home/music/Alice Cooper/Trash? Do not overwrite existing files.',
								'Extract all contents of Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not overwrite existing files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -jo Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress all contents of Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Overwrite existing files.',
								'Uncompress all contents of Trash.zip in this directory to /home/music/Alice/Cooper/Trash . Overwrite existing files.',
								'How do I decompress all contents of archive Trash.zip and store them to /home/music/Alice Cooper/Trash ? Overwrite existing files.',
								'How do I extract all contents of Trash.zip with and store them to /home/music/Alice Cooper/Trash? Overwrite existing files.',
								'Extract all contents of Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Overwrite existing files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -Co Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not consider case while searching files. Overwrite existing files.',
								'Uncompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Match file names case-insensitively. Overwrite existing files.',
								'How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash and do not consider case while searching files? Overwrite existing files.',
								'How do I extract content of Trash.zip and store them to /home/music/Alice Cooper/Trash and match file names case-insensitively? Overwrite existing files.',
								'Extract Trash.zip in this directory to /home/music/Alice/Cooper/Trash and do not consider case while searching file names. Overwrite existing files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -Cn Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not consider case while searching files. Do not overwrite existing files.',
								'Uncompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Match file names case-insensitively. Do not overwrite existing files.',
								'How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash and do not consider case while searching files? Do not overwrite existing files.',
								'How do I extract content of Trash.zip and store them to /home/music/Alice Cooper/Trash and match file names case-insensitively? Do not overwrite existing files.',
								'Extract Trash.zip in this directory to /home/music/Alice/Cooper/Trash and do not consider case while searching file names. Do not overwrite existing files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -CnL Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not consider case while searching files. Do not overwrite existing files. Convert uppercase names to lowercase names.',
								'Uncompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Match file names case-insensitively. Do not overwrite existing files. Convert uppercase names to lowercase names.',
								'How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash and do not consider case while searching files? Do not overwrite existing files. Convert uppercase names to lowercase names.',
								'How do I extract content of Trash.zip and store them to /home/music/Alice Cooper/Trash and match file names case-insensitively? Do not overwrite existing files. Convert uppercase names to lowercase names.',
								'Extract Trash.zip in this directory to /home/music/Alice/Cooper/Trash and do not consider case while searching file names. Do not overwrite existing files. Convert uppercase names to lowercase names.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -CoL Trash.zip -d /home/music/Alice Cooper/Trash',
					'NL Queries':['Decompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Do not consider case while searching files. Overwrite existing files. Convert uppercase names to lowercase names.',
								'Uncompress Trash.zip in this directory to /home/music/Alice/Cooper/Trash. Match file names case-insensitively. Overwrite existing files. Convert uppercase names to lowercase names.',
								'How do I decompress archive Trash.zip and store them to /home/music/Alice Cooper/Trash and do not consider case while searching files? Overwrite existing files. Convert uppercase names to lowercase names.',
								'How do I extract content of Trash.zip and store them to /home/music/Alice Cooper/Trash and match file names case-insensitively? Overwrite existing files. Convert uppercase names to lowercase names.',
								'Extract Trash.zip in this directory to /home/music/Alice/Cooper/Trash and do not consider case while searching file names. Overwrite existing files. Convert uppercase names to lowercase names.']},ignore_index=True)


unzip = unzip.append({'Command':'unzip -n letters.zip -x file1',
					'NL Queries':['How do I extract all contents of letters.zip except file1 ? Do not overwrite existing files.',
								'Uncompress letters.zip except file1 from letters.zip and do not overwrite any existing files.',
								'Extract letters.zip. Do not extract file1. Do not overwrite existing files.']},ignore_index=True)

unzip = unzip.append({'Command':'unzip -o letters.zip -x file1',
					'NL Queries':['How do I extract all contents of letters.zip except file1 ? Overwrite existing files.',
								'Uncompress letters.zip except file1 from letters.zip and Overwrite any existing files.',
								'Extract letters.zip. Do not extract file1. Overwrite existing files.']},ignore_index=True)




print unzip.shape


