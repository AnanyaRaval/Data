import pandas as pd 

mkdir = pd.DataFrame(columns = ['Command','NL Queries'])

#options [-mpvZ]
#use -m 640 folder=drw-r----- instead of -m a=rw-=drw-rw-rw- and even not working correctly for various other combinations.
#Though there can be many combinations for -m with r-4,w-2,x-1 , I think 777(anyone read,write and execute),755(owner can read,write and execute and all other can only read and execute),700(owner can read,write and execute and all other do not have any rights) are the most sensible combinations.

mkdir = mkdir.append({'Command': 'mkdir ananya',
					'NL Queries':['Make folder named ananya here.',
								'Create folder ananya.',
								'Create folder named ananya with default permissions.',
								'Create directory named ananya with default permissions.',
								'How do I create a new folder ananya?',
								'Make folder ananya.',
								'Make directory named ananya here.',
								'Create directory ananya.',
								'How do I create a new directory ananya?',
								'Make directory ananya.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir ../folder',
					'NL Queries':['Create empty folder in parent directory named folder.',
								'How do I create a folder named folder in previous directory?',
								'Make empty folder in parent directory called folder.',
								'Create empty directory in parent directory named folder.',
								'How do I create a directory named folder in previous directory?',
								'Make empty directory in parent directory called folder.']},ignore_index = True)

# same as mkdir -m 777 mkdir but I perfer 777 instead of rwx.
mkdir = mkdir.append({'Command': 'mkdir -m a=rwx mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that all users may read, write and execute the contents.',
								'Make directory with name mydir. Set permissions:read,write and execute for all users.',
								'How do I create a directory called mydir and set it\'s permissions so that all users can read, execute and write to it?',
								'Create the mydir folder and set its permissions such that all users may read, write and execute the contents.',
								'Make folder with name mydir. Set permissions:read,write and execute for all users.',
								'How do I create a folder called mydir and set it\'s permissions so that all users can read, execute and write to it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 777 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that all users may read, write and execute the contents.',
								'Make directory with name mydir. Set permissions:read,write and execute for all users.',
								'How do I create a directory called mydir and set it\'s permissions so that all users can read, execute and write to it?',
								'Create the mydir folder and set its permissions such that all users may read, write and execute the contents.',
								'Make folder with name mydir. Set permissions:read,write and execute for all users.',
								'How do I create a folder called mydir and set it\'s permissions so that all users can read, execute and write to it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 755 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that owner can read, write and execute the contents but all others can only read and execute.',
								'Make directory with name mydir. Set permissions:read,write and execute for owner and read and execute for all others.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can read, execute and write to it but all others can only read and execute it?',
								'Create the mydir folder and set its permissions such that owner can read, write and execute the contents but all others can only read and execute.',
								'Make folder with name mydir. Set permissions:read,write and execute for owner and read and execute for all others.',
								'How do I create a folder called mydir and set it\'s permissions so that all users can read, execute and write to it but all others can only read and execute it?'
								'Create folder mydir in this directory. I want all permissions, read,write and execute. my group and others should have only read and execute permissions.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 700 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that only owner can read, write and execute the contents.',
								'Make directory with name mydir. Set permissions:read,write and execute for owner and no permissions for all others.',
								'Create folder mydir where only I have all permission.',
								'Create directory mydir where only I have all permission.',
								'How do I create a directory called mydir and set it\'s permissions so that only owner can read, execute and write to it but all others have no rights on it?',
								'Create the mydir folder and set its permissions such that owner can read, write and execute the contents.',
								'Make folder with name mydir. Set permissions:read,write and execute for owner and no permissions for all others.',
								'How do I create a folder called mydir and set it\'s permissions so that only owner can read, execute and write to it but all others have no rights on it?',
								'Create folder named mydir in this directory. I want permissions of read write execute. my group or any other should not have permission to read,write and execute.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 711 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that owner can read, write and execute the contents but all others can only execute.',
								'Make directory with name mydir. Set permissions:read,write and execute for owner and only execute for all others.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can read, execute and write to it but all others can only execute it?',
								'Create the mydir folder and set its permissions such that owner can read, write and execute the contents but all others can only execute.',
								'Make folder with name mydir. Set permissions:read,write and execute for owner and only execute for all others.',
								'How do I create a folder called mydir and set it\'s permissions so that all users can read, execute and write to it but all others can only execute it?',
								'Create folder mydir in this directory. I should have all permissions, read,write and execute. my group can execute. Any other can also execute.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 766 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that owner can read, write and execute the contents but all others can only read and write.',
								'Make directory with name mydir. Set permissions:read,write and execute for owner and read and write for all others.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can read, execute and write to it but all others can only read and write it?',
								'Create the mydir folder and set its permissions such that owner can read, write and execute the contents but all others can only read and write.',
								'Make folder with name mydir. Set permissions:read,write and execute for owner and read and write for all others.',
								'How do I create a folder called mydir and set it\'s permissions so that all users can read, execute and write to it but all others can only read and write it?',
								'Make folder mydir in this folder. my group can read and write to it. Any other can also read and write to it. I should be able to read,write or execute.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 744 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that owner can read, write and execute the contents but all others can only read it.',
								'Make directory with name mydir. Set permissions:read,write and execute for owner and only read for all others.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can read, execute and write to it but all others can only read it?',
								'Create the mydir folder and set its permissions such that owner can read, write and execute the contents but all others can only read it.',
								'Make folder with name mydir. Set permissions:read,write and execute for owner and only read for all others.',
								'How do I create a folder called mydir and set it\'s permissions so that all users can read, execute and write to it but all others can only read it?',
								'Make a directory mydir in this folder. Add read,write and execute permissions for me. Add read permissions for a group. Add read permissions for others.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 722 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that owner can read, write and execute the contents but all others can only write it.',
								'Make directory with name mydir. Set permissions:read,write and execute for owner and only write for all others.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can read, execute and write to it but all others can only write it?',
								'Create the mydir folder and set its permissions such that owner can read, write and execute the contents but all others can only write it.',
								'Make folder with name mydir. Set permissions:read,write and execute for owner and only write for all others.',
								'How do I create a folder called mydir and set it\'s permissions so that all users can read, execute and write to it but all others can only write it?',
								'Make folder mydir. I want permission to read,write and execute. my group or other users should only have permission to write to it.']},ignore_index = True)


mkdir = mkdir.append({'Command': 'mkdir -m 417 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that I can only read, my group can only execute and all others can read write and execute the content.',
								'Make directory with name mydir. Set permissions as only read for owner and execute for group but all others can read, write and execute the content.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can only read and group can only execute but others can read, execute and write to it?',
								'Create the mydir folder and set its permissions such that I can only read, my group can only execute all others can read write and execute the content.',
								'Make folder with name mydir. Set permissions as only read for owner and execute for group but all others can read, write and execute the content.',
								'How do I create a folder called mydir and set it\'s permissions so that owner can only read and group can only execute but others can read, execute and write to it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 740 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that owner can read, write and execute the contents, my group can only read it and all others have no permissions.',
								'Make directory with name mydir. Set permissions:read,write and execute for owner, only read for my group and no permissions for others.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can read, execute and write to it, my group can only read it and all others have no permissions on it?',
								'Create the mydir folder and set its permissions such that owner can read, write and execute the contents, my group can only read it and all others have no permissions.',
								'Make folder with name mydir. Set permissions:read,write and execute for owner, only read for my group and no permissions for others.',
								'How do I create a folder called mydir and set it\'s permissions so that owner can read, execute and write to it, my group can only read it and all others have no permissions on it?',
								'Make a directory mydir in this folder. Add read,write and execute permissions for me. Add read permissions for a group. No permissions for others.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 140 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that owner can only execute the contents, my group can only read it and all others have no permissions.',
								'Make directory with name mydir. Set permissions:only execute for owner, only read for my group and no permissions for others.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can execute it, my group can only read it and all others have no permissions on it?',
								'Create the mydir folder and set its permissions such that owner can only execute the contents, my group can only read it and all others have no permissions.',
								'Make folder with name mydir. Set permissions:only execute for owner, only read for my group and no permissions for others.',
								'How do I create a folder called mydir and set it\'s permissions so that owner can execute it, my group can only read it and all others have no permissions on it?',
								'Make a directory mydir in this folder. Add execute permissions for me. Add read permissions for a group. No permissions for others.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 571 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that I can read and write, my group have all permissions and all others can only write the content.',
								'Make directory with name mydir. Set permissions as read and write for owner and read, write and execute for group and all others can only write the content.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can read and write and group have all permissions and all others can write to it?',
								'Create the mydir folder and set its permissions such that I can read and write, my group have all permissions and all others can only write the content.',
								'Make folder with name mydir. Set permissions as read and write for owner and read, write and execute for group and all others can only write the content.',
								'How do I create a folder called mydir and set it\'s permissions so that owner can read and write and group have all permissions and all others can write to it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 007 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that I and my group cannot read, write and execute but all others can read write and execute.',
								'Make directory with name mydir. Set permissions as null for owner and group but all others can read, write and execute the content.',
								'How do I create a directory called mydir and set it\'s permissions so that owner and group cannot read, write and execute but others can read, execute and write to it?',
								'Create the mydir folder and set its permissions such that I and my group cannot read, write and execute but all others can read write and execute.',
								'Make folder with name mydir. Set permissions as null for owner and group but all others can read, write and execute the content.',
								'How do I create a folder called mydir and set it\'s permissions so that owner and group cannot read, write and execute but others can read, execute and write to it?',
								'Create folder named mydir in this directory. Me, my group and any other user should not have permission to read,write and execute.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 404 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that owner and others can only read the contents but the my group members have no permissions.',
								'Make directory with name mydir. Set permissions:only read for owner and for all others but no permissions for my group members.',
								'How do I create a directory called mydir and set it\'s permissions so that owner and others can only read it but group members no rights on it?',
								'Create the mydir folder and set its permissions such that owner and others can only read the contents but the my group members have no permissions.',
								'Make folder with name mydir. Set permissions:only read for owner and for all others but no permissions for my group members.',
								'How do I create a folder called mydir and set it\'s permissions so that only owner can read, execute and write to it but all others have no rights on it?',
								'Create folder named mydir in this directory. I want permissions of only read. My group members have no permissions. All others have only read permissions.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 000 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that no one has read, write and execute including me.',
								'Make directory with name mydir. Set permissions as null for owner, group and others.',
								'How do I create a directory called mydir and set it\'s permissions so that neither group or others nor owner can read, execute and write to it?',
								'Create the mydir folder and set its permissions such that no one has read, write and execute including me.',
								'Make folder with name mydir. Set permissions as null for owner, group and others.',
								'How do I create a folder called mydir and set it\'s permissions so that neither group or others nor owner can read, execute and write to it?',
								'Create folder named mydir in this directory. Me, my group should not have permission to read,write and execute but any other user can read,write and execute.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 124 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that I can only execute, my group can only write and all others can only read the content.',
								'Make directory with name mydir. Set permissions as only execute for owner and write for group but all others can only read the content.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can only execute and group can only write but others can only read it?',
								'Create the mydir folder and set its permissions such that I can only execute, my group can only write and all others can only read the content.',
								'Make folder with name mydir. Set permissions as only read for owner and execute for group but all others can read, write and execute the content.',
								'How do I create a directory called mydir and set it\'s permissions so that owner can only execute and group can only write but others can only read it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 227 mydir',
					'NL Queries':['Create the mydir directory and set its permissions such that owner and group can only writethe contents but all others can only read, write and execute the content.',
								'Make directory with name mydir. Set permissions:only write for owner and group. Read, write and execute for all others.',
								'How do I create a directory called mydir and set it\'s permissions so that owner and group can only write to it but all others can only read, write and execute it?',
								'Create the mydir folder and set its permissions such that owner and group can only writethe contents but all others can only read, write and execute the content.',
								'Make folder with name mydir. Set permissions:only write for owner and group. Read, write and execute for all others.',
								'How do I create a folder called mydir and set it\'s permissions so that owner and group can only write to it but all others can only read, write and execute it?',
								'Make folder mydir. I and my group have permissions to only write.All other should have permissions to read, write and execute to it.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir foo bar baz',
					'NL Queries':['Make folders named foo bar baz here.',
								'Make directories named foo bar baz here.',
								'Create folders: foo, bar, baz in this directory.',
								'How do I create multiple folders named foo, bar and baz?',
								'Make multiple folders named foo bar baz in current folder.',
								'Create directories: foo bar baz in this directory.',
								'How do I create multiple directories named foo bar baz?',
								'Make multiple directories named foo bar baz in current folder.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -p tmpdir/{trunk/{includes,docs},branches,tags}',
					'NL Queries':['Make folders trunk, branches, tags under tmpdir and folders includes, docs under trunk. Ignore if already exists.',
								'How to make folders trunk, branches, tags under tmpdir and folders includes, docs under trunk? Ignore if already exists.',
								'Create folders trunk, branches, tags under tmpdir and folders includes, docs under trunk. Ignore if already exists?',
								'Make directories trunk, branches, tags under tmpdir and directories includes, docs under trunk. Ignore if already exists.',
								'How to make directories trunk, branches, tags under tmpdir and directories includes, docs under trunk? Ignore if already exists?',
								'Create directories trunk, branches, tags under tmpdir and directories includes, docs under trunk. Ignore if already exists.',]},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -p myfolder/main/ananya',
					'NL Queries':['Make folder named ananya and create parent folders(myfolder/main) if do not exist.',
								'Create folder ananya and it\'s parent folders(myfolder/main).',
								'How do I create a new folder ananya and it\'s parent folders(myfolder/main)?',
								'Make folder ananya and it\'s parent directories(myfolder/main) if they do not exist.',
								'Create folder named ananya and it\'s parent folders(myfolder/main) if they do not exist.',
								'Make directory named ananya and create parent folders(myfolder/main), if they are not present.',
								'Create directory ananya and it\'s parent directories(myfolder/main).',
								'How do I create a new directory ananya and it\'s parent directories(myfolder/main)?',
								'Make directory ananya. Make it\'s parent directories(myfolder/main), if they do not exist.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -v ananya',
					'NL Queries':['Make folder named ananya. Show log of what is being created.',
								'Create folder ananya with a log.',
								'How do I create a new folder ananya? Display what folder is being created.',
								'Make folder ananya and log of folder created.',
								'Make directory named ananya. Show log of what is being created.',
								'Create directory ananya with a log.',
								'How do I create a new directory ananya? Display what directory is being created.',
								'Make directory ananya and log of folder created.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 777 -v mydir',
					'NL Queries':['Create the mydir directory with a log and set its permissions such that all users may read, write and execute the contents.',
								'Make directory with name mydir. Set permissions:read,write and execute for all users. Display what folder is being created.',
								'How do I create a directory called mydir with a log and set it\'s permissions so that all users can read, execute and write to it?',
								'Create the mydir folder with a log of what is being created and set its permissions such that all users may read, write and execute the contents.',
								'Make folder with name mydir. Set permissions:read,write and execute for all users. Display the log.',
								'How do I create a folder called mydir with a log and set it\'s permissions so that all users can read, execute and write to it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 755 -v mydir',
					'NL Queries':['Create the mydir directory with a log and set its permissions such that owner can read, write and execute the contents but all others can only read and execute.',
								'Make directory with name mydir. Set permissions:read,write and execute for owner and read and execute for all others. Display what folder is being created.',
								'How do I create a directory called mydir with a log and set it\'s permissions so that owner can read, execute and write to it but all others can only read and execute it?',
								'Create the mydir folder with a log of what is being created and set its permissions such that owner can read, write and execute the contents but all others can only read and execute.',
								'Make folder with name mydir. Set permissions:read,write and execute for owner and read and execute for all others. Display the log.',
								'How do I create a folder called mydir with a log and set it\'s permissions so that all users can read, execute and write to it but all others can only read and execute it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 777 -p myfolder/main/ananya',
					'NL Queries':['Create the ananya directory and set its permissions such that all users may read, write and execute the contents. Create parent directories(myfolder/main) if not present.',
								'Make directory with name ananya. Create parent directories(myfolder/main), if absent. Set permissions:read,write and execute for all users.',
								'How do I create a directory called ananya, it\'s parent directories(myfolder/main) if not present and set it\'s permissions so that all users can read, execute and write to it?',
								'Create the ananya folder and it\'s parent directories(myfolder/main) if they do not exist. Set permissions of ananya such that all users may read, write and execute the contents.',
								'Make folder with name ananya and it\'s parent directories(myfolder/main) if absent. Set permissions:read,write and execute for all users.',
								'How do I create a folder called ananya, it\'s parent directories namely myfolder and main, if not present and set it\'s permissions so that all users can read, execute and write to it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 700 -p myfolder/main/ananya',
					'NL Queries':['Create the ananya directory and set its permissions such that only owner can read, write and execute the contents. Create parent directories(myfolder/main) if not present.',
								'Make directory with name ananya. Create parent directories(myfolder/main), if absent. Set permissions:read,write and execute for owner and no permissions for all others.',
								'Create folder ananya with parent folders(myfolder/main), if absent and where only I have all permission.',
								'Create directory ananya with parent directories(myfolder/main), if absent and where only I have all permission.',
								'How do I create a directory called ananya and it\'s parent directories(myfolder/main). Set it\'s permissions so that only owner can read, execute and write to it but all others have no rights on it?',
								'Create the ananya folder and set its permissions such that owner can read, write and execute the contents. Create parent folders(myfolder/main) if not absent.',
								'Make folder with name ananya. Create parent folders(myfolder/main), if absent. Set permissions:read,write and execute for owner and no permissions for all others.',
								'How do I create a folder called ananya and it\'s parent folders(myfolder/main). Set it\'s permissions so that only owner can read, execute and write to it but all others have no rights on it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -vp myfolder/main/ananya',
					'NL Queries':['Make folder named ananya and create parent folders(myfolder/main) if do not exist. Show log of what is being created.',
								'Create folder ananya and it\'s parent directories(myfolder/main) with a log.',
								'How do I create a new folder ananya and it\'s parent folders(myfolder/main)? Display what folders are being created.',
								'Make folder ananya and it\'s parent directories(myfolder/main) if do not exist and log of folders created.',
								'Create folder named ananya and it\'s parent folders(myfolder/main) if do not exist, with list of what folders being created.',
								'Make directory named ananya and create parent folders(myfolder/main) if do not exist. Show log of what is being created.',
								'Create directory ananya and it\'s parent directories(myfolder/main) along with a log of changes displayed on the screen.',
								'How do I create a new directory ananya and it\'s parent directories(myfolder/main)? Display what directories are being created.',
								'Make directory ananya and it\'s parent directories(myfolder/main) if do not exist and log of folders created.',
								'Create directory named ananya and it\'s parent directories(myfolder/main) if do not exist, with a list of what folders being created.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 777 -vp myfolder/main/ananya',
					'NL Queries':['Make folder named ananya and create parent folders(myfolder/main) if do not exist. Show log of what is being created. Set its permissions such that all users may read, write and execute the contents.',
								'Create folder ananya and it\'s parent directories(myfolder/main) with a log. Set permissions:read,write and execute for all users.',
								'How do I create a new folder ananya and it\'s parent folders(myfolder/main)? Display what folders are being created and set folder permissions as read,write and execute for all users.',
								'Make folder ananya and it\'s parent directories(myfolder/main) if do not exist and log of folders created. Make folder permissions as read,write and execute for all users.',
								'Create folder named ananya and it\'s parent folders(myfolder/main) if do not exist, with list of what folders being created. Make ananya folder readable,writeable and executable for all users.',
								'Make directory named ananya and create parent folders(myfolder/main) if do not exist. Show log of what is being created. Set its permissions such that all users may read, write and execute the contents.',
								'Create directory ananya and it\'s parent directories(myfolder/main), namely myfolder/main with a log. Set permissions:read,write and execute for all users.',
								'How do I create a new directory ananya and it\'s parent directories(myfolder/main)? Display what directories are being created and set directory permissions as read,write and execute for all users.',
								'Make directory ananya and it\'s parent directories(myfolder/main) if do not exist and log of folders created. Make directory permissions as read,write and execute for all users.',
								'Create directory named ananya and it\'s parent directories(myfolder/main) if do not exist, with list of what folders being created. Make ananya folder readable,writeable and executable for all users.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 711 -vp myfolder/main/ananya',
					'NL Queries':['Create the ananya directory and set its permissions such that owner can read, write and execute the contents but all others can only execute. Create parent directories(myfolder/main) if absent.',
								'Make directory with name ananya and it\'s parent directories(myfolder/main) if they do not exist. Set permissions:read,write and execute for owner and only execute for all others.',
								'How do I create a directory called ananya with it\'s parent directories(myfolder/main) and set it\'s permissions so that owner can read, execute and write to it but all others can only execute it?',
								'Create the ananya folder and it\'s parent folders(myfolder/main) if absent. Set its permissions such that owner can read, write and execute the contents but all others can only execute.',
								'Make folder with name ananya and it\'s parent folders(myfolder/main) if they are not present. Set permissions:read,write and execute for owner and only execute for all others.',
								'How do I create a folder called ananya with it\'s parent folders(myfolder/main) and set it\'s permissions so that all users can read, execute and write to it but all others can only execute it?']},ignore_index = True)
#below are -Z combinations.
mkdir = mkdir.append({'Command': 'mkdir -Z ananya',
					'NL Queries':['Create folder ananya. Set default security context for ananya.',
								'Create directory named ananya. Set default security context for ananya.',
								'Make new folder ananya and set it\'s security context to be the default type.',
								'Make new directory naemd ananya and set it\'s security context to be the default type.',
								'How to create a new folder ananya with it\'s security context set to default type?',
								'How to create a new directory ananya with it\'s security context set to default type?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 777 -Z mydir',
					'NL Queries':['Create the mydir directory, set its permissions such that all users may read, write and execute the contents and it\'s security context as default.',
								'Make directory with name mydir. Set permissions:read,write and execute for all users. Set security context as default type.',
								'How do I create a directory called mydir and set it\'s permissions so that all users can read, execute and write to it? Set security context to default type.',
								'Create the mydir folder and set its permissions such that all users may read, write and execute the contents and it\'s security context as default.',
								'Make folder with name mydir. Set permissions:read,write and execute for all users. Set security context as default type.',
								'How do I create a folder called mydir and set it\'s permissions so that all users can read, execute and write to it? Set security context to default type.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -vZ ananya',
					'NL Queries':['Make folder named ananya. Show log of what is being created. Set security context as default type.',
								'Create folder ananya with a log and security context to default type.',
								'How do I create a new folder ananya with security context as default type? Display what folder is being created.',
								'Make folder ananya and log of folder created. Set security context as default type.',
								'Make directory named ananya. Show log of what is being created. Set security context as default type.',
								'Create directory ananya with a log and security context to default type.',
								'How do I create a new directory ananya with security context as default type? Display what directory is being created.',
								'Make directory ananya and log of folder created. Set security context as default type.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -pZ myfolder/main/ananya',
					'NL Queries':['Make folder named ananya and create parent folders(myfolder/main) if do not exist. Set security context as default type.',
								'Create folder ananya and it\'s parent folders(myfolder/main) with security context set to default type.',
								'How do I create a new folder ananya and it\'s parent folders(myfolder/main) and set security context to default type?',
								'Make folder ananya and it\'s parent directories(myfolder/main) if they do not exist with security context set to default.',
								'Make directory named ananya and create parent folders(myfolder/main), if they are not present. Set security context as default type.',
								'Create directory ananya and it\'s parent directories(myfolder/main) with security context set to default type.',
								'How do I create a new directory ananya and it\'s parent directories(myfolder/main) and set security context to default type?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 777 -vZ mydir',
					'NL Queries':['Create the mydir directory with a log and set its permissions such that all users may read, write and execute the contents. Set security context as default type. Show log of what is being created.',
								'Make directory with name mydir with security context as default type. Set permissions:read,write and execute for all users. Display what folder is being created.',
								'How do I create a directory called mydir with a log and security context as default type and set it\'s permissions so that all users can read, execute and write to it?',
								'Create the mydir folder with a log and set its permissions such that all users may read, write and execute the contents. Set security context as default type. Show log of what is being created.',
								'Make folder with name mydir with security context as default type. Set permissions:read,write and execute for all users. Display the log.',
								'How do I create a folder called mydir with a log and security context as default type and set it\'s permissions so that all users can read, execute and write to it?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 777 -pZ myfolder/main/ananya',
					'NL Queries':['Create the ananya directory and set its permissions such that all users may read, write and execute the contents. Create parent directories(myfolder/main) if not present. Set security context as default type.',
								'Make directory with name ananya. Create parent directories(myfolder/main) if absent. Set permissions:read,write and execute for all users. Set security context as default type.',
								'How do I create a directory called ananya, it\'s parent directories(myfolder/main) if not present and set it\'s permissions so that all users can read, execute and write to it with security context set to default type?',
								'Create the ananya folder and it\'s parent if they do not exist. Set permissions of ananya such that all users may read, write and execute the contents and make security context set to default.',
								'Make folder with name ananya and it\'s parent folders(myfolder/main) if absent. Set permissions:read,write and execute for all users. Set security context as default type.',
								'How do I create a folder called ananya, it\'s parent folders namely myfolder and main, if not present and set it\'s permissions so that all users can read, execute and write to it? Set security context as default type?']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -pvZ myfolder/main/ananya',
					'NL Queries':['Make folder named ananya and create parent folders(myfolder/main) if do not exist. Show log of what is being created. Set security context as default type.',
								'Create folder ananya and it\'s parent directories(myfolder/main) with a log and set security context to default type.',
								'How do I create a new folder ananya and it\'s parent folders? Display what folders are being created. Set security context as default type.',
								'Make folder ananya and it\'s parent directories(myfolder/main) if do not exist and log of folders created with security context set to default type.',
								'Create folder named ananya and it\'s parent folders(myfolder/main) if do not exist, with list of what folders being created and security context set to default.',
								'Make directory named ananya and create parent folders(myfolder/main) if do not exist. Show log of what is being created. Set security context as default type.',
								'Create directory ananya and it\'s parent directories(myfolder/main) along with a log of changes displayed on the screen and it\'s security context set to default type.',
								'How do I create a new directory ananya and it\'s parent directories(myfolder/main)? Display what directories are being created. Set security context as default type.',
								'Make directory ananya and it\'s parent directories(myfolder/main) if do not exist and log of folders created. Set security context as default type.',
								'Create directory named ananya and it\'s parent directories(myfolder/main) if do not exist, with a list of what folders being created and it\'s security context set to default type.']},ignore_index = True)

mkdir = mkdir.append({'Command': 'mkdir -m 777 -vpZ myfolder/main/ananya',
					'NL Queries':['Make folder named ananya and create parent folders(myfolder/main) if do not exist. Show log of what is being created. Set its permissions such that all users may read, write and execute the contents.',
								'Create folder ananya and it\'s parent directories(myfolder/main) with a log. Set permissions:read,write and execute for all users. Set security context as default type.',
								'How do I create a new folder ananya with security context set to default type and it\'s parent folders(myfolder/main)? Display what folders are being created and set folder permissions as read,write and execute for all users. Set security context as default type.',
								'Make folder ananya with security context set to default type and it\'s parent directories(myfolder/main) if do not exist and log of folders created. Make folder permissions as read,write and execute for all users.',
								'Create folder named ananya with security context set to default type and it\'s parent folders(myfolder/main) if do not exist, with list of what folders being created. Make ananya folder readable,writeable and executable for all users.',
								'Make directory named ananya with security context set to default type and create parent folders(myfolder/main) if do not exist. Show log of what is being created. Set its permissions such that all users may read, write and execute the contents.',
								'Create directory ananya with security context set to default type and it\'s parent directories(myfolder/main), namely myfolder/main with a log. Set permissions:read,write and execute for all users.',
								'How do I create a new directory ananya with security context set to default type and it\'s parent? Display what directories are being created and set directory permissions as read,write and execute for all users.',
								'Make directory ananya with security context set to default type and it\'s parent directories(myfolder/main) if do not exist and log of folders created. Make directory permissions as read,write and execute for all users.',
								'Create directory named ananya with security context set to default type and it\'s parent directories(myfolder/main) if do not exist, with list of what folders being created. Make ananya folder readable,writeable and executable for all users.']},ignore_index = True)


#mkdir.to_csv('/home/ananyaraval/Documents/Thesis/Data/UNIX/csv_files/mkdir.csv',index=False)
print (mkdir.shape)