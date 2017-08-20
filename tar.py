import pandas as pd 

tar = pd.DataFrame(columns = ['Command','NL Queries'])

tar = tar.append({'Command':'tar cvzf MyImages-14-09-12.tar.gz /home/MyImages','NL Queries':['Create a new tar archive for /home/MyImages folder in current directory. It\'s name should be MyImages-14-09-12.tar.gz. Display the progress of files.']},ignore_index = True)
tar = tar.append({'Command':'tar -xvf compressed.tar','NL Queries':['Untar compressed.tar in current directory. Show the files in the tar archive.']},ignore_index=True)
tar = tar.append({'Command':'tar -xvf Phpfiles-org.tar --wildcards \'*.php\'','NL Queries':['Extract all .php files from Phpfiles-org.tar in the current folder.','How do I extract the files ending with .php from Phpfiles-org.tar']},ignore_index = True)


#1
tar = tar.append({'Command': 'tar -cf test.tar test_folder',
                  'NL Queries': ['Create archive of test_folder directory with name test.tar .',
                                 'Make archive of the test_folder named test.tar .',
                                 'Make tar archive of the test_folder and name it as test.tar .',
                                 'Create test.tar as an archive of test_folder folder.']}, ignore_index = True)

#2
tar = tar.append({'Command': 'tar -cvf test.tar test_folder',
                  'NL Queries': ['Create archive of test_folder directory with name test.tar and display the details.',
                                 'Create tar archive of test_folder folder with name test.tar and show the files added.',
                                 'Make tar of the test_folder with name test.tar displaying the files added.',
                                 'Archive the folder test_folder with name test.tar and show the details of operations performed.']}, ignore_index = True)

#3
tar = tar.append({'Command': 'tar -czf test.tar.gz test_folder',
                  'NL Queries': ['Create compressed archive of test_folder directory in gzip format and name it test.tar.gz .',
                                 'Create gzip archive of test_folder named test.tar.gz .',
                                 'Make gzip compressed archive of test_folder with name test.tar.gz .',
                                 'Archive test_folder and compress it using Lempel-ziv coding and name it test.tar.gz .']}, ignore_index = True)

#4
tar = tar.append({'Command': 'tar -cvzf test.tar.gz test_folder',
                  'NL Queries': ['Create compressed archive of test_folder directory in gzip format and name it test.tar.gz and show the details.',
                                 'Create gzip archive of test_folder named test.tar.gz and display the files added.',
                                 'Make gzip compressed archive of test_folder with name test.tar.gz and show the progress.',
                                 'Archive test_folder and compress it using Lempel-ziv coding and name it test.tar.gz and show the files added to archive.']}, ignore_index = True)

#5
tar = tar.append({'Command': 'tar -cjf test.tar.bz2 test_folder',
                  'NL Queries': ['Create compressed archive of test_folder directory in bzip2 format and name it test.tar.bz2 .',
                                 'Make bzip2 compressed archive of test_folder and save it as test.tar.bz2 .',
                                 'Make the bz2 archive of test_folder directory and store it as test.tar.bz2 .',
                                 'Use Burrows-Wheeler algorithm to compress the tar archive of test_folder and name it as tes.tar.bz2 .']}, ignore_index = True)

#6
tar = tar.append({'Command': 'tar -cvjf test.tar.bz2 test_folder',
                  'NL Queries': ['Create compressed archive of test_folder directory in bzip2 format and name it test.tar.bz2 and show the details.',
                                 'Make bzip2 compressed archive of test_folder and save it as test.tar.bz2 and display the progress of process.',
                                 'Make the bz2 archive of test_folder directory and store it as test.tar.bz2 and show the process details.',
                                 'Use Burrows-Wheeler algorithm to compress the tar archive of test_folder and name it as tes.tar.bz2 and show the files added to archive.']}, ignore_index = True)

#7
tar = tar.append({'Command': 'tar -xf document.tar \"doc1.txt\"',
                  'NL Queries': ['Extract doc1.txt file from document.tar archive.',
                                 'Untar doc1.txt from document.tar archive.',
                                 'Untar the file doc1.txt from document.tar .']}, ignore_index = True)

#8
tar = tar.append({'Command': 'tar -xvf document.tar \"doc1.txt\"',
                  'NL Queries': ['Extract doc1.txt file from document.tar archive and display the details.',
                                 'Untar doc1.txt from document.tar archive and show the process details.',
                                 'Untar the file doc1.txt from document.tar verbosely.']}, ignore_index = True)

#9
tar = tar.append({'Command': 'tar -xzf document.tar.gz \"doc1.txt\"',
                  'NL Queries': ['Extract doc1.txt file from document.tar.gz archive.',
                                 'Untar doc1.txt file from gzip archive named document.tar.gz .',
                                 'Untar doc1.txt file from gzipped archive document.tar.gz .']}, ignore_index = True)

#10
tar = tar.append({'Command': 'tar -xzvf document.tar.gz \"doc1.txt\"',
                  'NL Queries': ['Extract doc1.txt file from document.tar.gz archive and display the details.',
                                 'Untar doc1.txt file from gzip archive named document.tar.gz verbosely.',
                                 'Untar doc1.txt file from gzipped archive document.tar.gz showing the progress.']}, ignore_index = True)

#11
tar = tar.append({'Command': 'tar -xjf document.tar.bz2 \"doc1.txt\"',
                  'NL Queries': ['Extract doc1.txt file from document.tar.bz2 archive.',
                                 'Take out the doc1.txt file from document.tat.bz2 bzip2 archive.',
                                 'From document.tar.bz2 bz2 archive, extract doc1.txt file.']}, ignore_index = True)

#12
tar = tar.append({'Command': 'tar -xjvf document.tar.bz2 \"doc1.txt\"',
                  'NL Queries': ['Extract doc1.txt file from document.tar.bz2 archive and display the details.',
                                 'Take out the doc1.txt file from document.tat.bz2 bzip2 archive and show the performed operations.',
                                 'From document.tar.bz2 bz2 archive, extract doc1.txt file giving the progress details.']}, ignore_index = True)

#13
tar = tar.append({'Command': 'tar -xf document.tar \"doc1.txt\" \"doc2.txt\"',
                  'NL Queries': ['Extract doc1.txt and doc2.txt file from document.tar archive.',
                                 'Take out the files doc1.txt and doc2.txt from document.tar archive.',
                                 'Untar the doc1.txt and doc2.txt files from document.tar archive.']}, ignore_index = True)

#14
tar = tar.append({'Command': 'tar -xvf document.tar \"doc1.txt\" \"doc2.txt\"',
                  'NL Queries': ['Extract doc1.txt and doc2.txt file from document.tar archive and display the details.',
                                 'Take out the files doc1.txt and doc2.txt from document.tar archive showing progress details.',
                                 'Untar the doc1.txt and doc2.txt files from document.tar archive showing the tasks completed.']}, ignore_index = True)

#15
tar = tar.append({'Command': 'tar -xzf document.tar.gz \"doc1.txt\" \"doc2.txt\"',
                  'NL Queries': ['Extract doc1.txt and doc2.txt file from document.tar.gz archive.',
                                 'Untar the files doc1.txt and doc2.txt files from document.tar.gz gzip compressed archive.',
                                 'Extract the files doc1.txt and doc2.txt files from gzipped archive document.tar.gz file.']}, ignore_index = True)

#16
tar = tar.append({'Command': 'tar -xzvf document.tar.gz \"doc1.txt\" \"doc2.txt\"',
                  'NL Queries': ['Extract doc1.txt and doc2.txt file from document.tar.gz archive and display the details.',
                                 'Untar the files doc1.txt and doc2.txt files from document.tar.gz gzip compressed archive and show the tasks performed.',
                                 'Extract the files doc1.txt and doc2.txt files from gzipped archive document.tar.gz file displaying the operations completed.']}, ignore_index = True)

#17
tar = tar.append({'Command': 'tar -xjf document.tar.bz2 \"doc1.txt\" \"doc2.txt\"',
                  'NL Queries': ['Extract doc1.txt and doc2.txt file from document.tar.bz2 archive.',
                                 'Extract doc1.txt and doc2.txt files from bz2 archive document.tar.bz2 .',
                                 'Untar doc1.txt and doc2.txt from the bzip2 compressed archive document.tar.bz2 .']}, ignore_index = True)

#18
tar = tar.append({'Command': 'tar -xjvf document.tar.bz2 \"doc1.txt\" \"doc2.txt\"',
                  'NL Queries': ['Extract doc1.txt and doc2.txt file from document.tar.bz2 archive and display the details.',
                                 'Untar the files doc1.txt and doc2.txt from bz2 archive document.tar.bz2 showing the files extracted.',
                                 'Extract the files doc1.txt and doc2.txt from bzipped2 archive document.tar.bz2 with the acknowledgement.']}, ignore_index = True)

#19
tar = tar.append({'Command': 'tar -tf test.tar',
                  'NL Queries': ['Show me the files in the archive named test.tar .',
                                 'List the contents of test.tar archive.',
                                 'Display the details regarding test.tar contents.',
                                 'Show the archive test.tar contents.']}, ignore_index = True)

#20
tar = tar.append({'Command': 'tar -tvf test.tar',
                  'NL Queries': ['Show me the files and its details in test.tar archive.',
                                 'Display the details of test.tar contents.',
                                 'Give the details of data in test.tar archive.']}, ignore_index = True)

#21
tar = tar.append({'Command': 'tar -tzf test.tar.gz',
                  'NL Queries': ['Show me the files under gzipped archive test.tar.gz .',
                                 'Display the archived files in test.tar.gz gzip archive.',
                                 'Show the archived files inside gzipped archive test.tar.gz .']}, ignore_index = True)

#22
tar = tar.append({'Command': 'tar -tvzf test.tar.gz',
                  'NL Queries': ['Show me the files and its details under gzipped archive test.tar.gz .',
                                 'Display the archived files and their details in test.tar.gz gzip archive.',
                                 'Display the files inside test.tar.gz gzip archive in long listing format.']}, ignore_index = True)

#23
tar = tar.append({'Command': 'tar -tjf test.tar.bz2',
                  'NL Queries': ['Show me the files under bzipped2 archive test.tar.bz2 .',
                                 'Display the contents of test.tar.bz2 archive.',
                                 'Show me the bz2 archived content in test.tar.bz2 .']}, ignore_index = True)

#24
tar = tar.append({'Command': 'tar -tvjf test.tar.bz2',
                  'NL Queries': ['Show me the files and its details under bzipped2 archive test.tar.bz2 .',
                                 'Display the files inside test.tar.bz2 bzip2 archive in long listing format.',
                                 'Show me the bz2 archived content in test.tar.bz2 in detail.']}, ignore_index = True)

#25
tar = tar.append({'Command': 'tar -cwf check.tar Music/',
                  'NL Queries': ['Create archive of Music directory named check.tar and ask for each each file or directory to be added to archive or not .',
                                 'Interactively ask for each file in Music directory to be added to check.tar archive or not.',
                                 'How do I select for each file to be added to archive check.tar in Music directory?']}, ignore_index = True)

#26
tar = tar.append({'Command': 'tar -cvwf check.tar Music/',
                  'NL Queries': ['Create archive of Music directory named check.tar and ask for each each file or directory to be added to archive or not and give me the details.',
                                 'Interactively ask for each file in Music directory to be added to check.tar archive or not. Also give the details of task done.',
                                 'How do I select for each file to be added to archive check.tar in Music directory? Show the tasks being done.']}, ignore_index = True)

#27
tar = tar.append({'Command': 'tar -czwf check.tar.gz Music/',
                  'NL Queries': ['Create gzipped archive of Music directory named check.tar.gz and ask for each each file or directory to be added to archive or not .',
                                 'Interactively ask for each file in Music directory to be added to check.tar.gz gzip archive or not.',
                                 'How do I select for each file to be added to gzipped archive check.tar.gz in Music directory?.']}, ignore_index = True)

#28
tar = tar.append({'Command': 'tar -cvzwf check.tar.gz Music/',
                  'NL Queries': ['Create gzipped archive of Music directory named check.tar.gz and ask for each each file or directory to be added to archive or not and give me the details.',
                                 'Interactively ask for each file in Music directory to be added to check.tar.gz gzip archive or not. Also give the details of task done.',
                                 'How do I select for each file to be added to gzipped archive check.tar.gz in Music directory? Show the tasks being done.']}, ignore_index = True)

#29
tar = tar.append({'Command': 'tar -cjwf check.tar.bz2 Music/',
                  'NL Queries': ['Create bzipped2 archive of Music directory named check.tar.bz2 and ask for each each file or directory to be added to archive or not .',
                                 'Interactively ask for each file in Music directory to be added to check.tar.bz2 bzip2 archive or not.',
                                 'How do I select for each file to be added to bzipped2 archive check.tar.bz2 in Music directory?']}, ignore_index = True)

#30
tar = tar.append({'Command': 'tar -cvjwf check.tar.gz Music/',
                  'NL Queries': ['Create bzipped2 archive of Music directory named check.tar.bz2 and ask for each each file or directory to be added to archive or not and give me the details.',
                                 'Interactively ask for each file in Music directory to be added to check.tar.bz2 bzip2 archive or not. Also give the details of task done.',
                                 'How do I select for each file to be added to bzipped2 archive check.tar.bz2 in Music directory? Show the tasks being done.']}, ignore_index = True)

#31
tar = tar.append({'Command': 'tar -rf check.tar another.pdf',
                  'NL Queries': ['Append another.pdf file to the check.tar archive at the end.',
                                 'Add the file another.pdf to archive check.tar .',
                                 'Archive the file another.pdf in check.tar archive, which already exists.']}, ignore_index = True)

#32
tar = tar.append({'Command': 'tar -rvf check.tar another.pdf',
                  'NL Queries': ['Append another.pdf file to the check.tar archive at the end and give me the details.',
                                 'Add the file another.pdf to archive check.tar and show the files added.',
                                 'Archive the file another.pdf in check.tar archive, which already exists. Show the details of files ']}, ignore_index = True)

#33
tar = tar.append({'Command': 'tar -cWf checked.tar monkey.dog',
                  'NL Queries': ['Create an archive of file monkey.dog and verify it.',
                                 'Verify and create checked.tar by archiving monkey.dog .',
                                 'Check the validity of archive file created by monkey.dog with name checked.tar .']}, ignore_index = True)

#34
tar = tar.append({'Command': 'tar -cvWf checked.tar monkey.dog',
                  'NL Queries': ['Create an archive of file monkey.dog , show the details and verify it.',
                                 'Verify and create checked.tar by archiving monkey.dog and display the tasks performed.',
                                 'Check the validity of archive file created by monkey.dog with name checked.tar and show the completed tasks.']}, ignore_index = True)

#35
tar = tar.append({'Command': 'tar --delete -f manga.tar \"onepiece.txt\"',
                  'NL Queries': ['Delete onepiece.txt from manga.tar archive.',
                                 'Remove onepiece.txt file from manga.tar archive.',
                                 'Erase onepiece.txt file manga.tar archive.']}, ignore_index = True)

#36
tar = tar.append({'Command': 'tar -Af arch1.tar arch2.tar',
                  'NL Queries': ['Append arch2.tar to arch1.tar archive.',
                                 'Add the contents of arch2.tar to arc1.tar archive.',
                                 'Merge the archive arch2.tar into arch1.tar file.']}, ignore_index = True)

#37
tar = tar.append({'Command': 'tar --test-label comics.tar',
                  'NL Queries': ['Check comics.tar volume label.',
                                 'Validate the volume label of comics.tar .',
                                 'Test the validity of comics.tar volume label.']}, ignore_index = True)

#38
tar = tar.append({'Command': 'tar -uf comics.tar codegeass.pdf',
                  'NL Queries': ['Add codegeass.pdf to comics.tar if the archive has older version.',
                                 'Update the codegeass.pdf in comics.tar archive with the one in present working directory(pwd).',
                                 'Add codegeass.pdf to the archive, comics.tar . If the archive has older version update it with the current one.']}, ignore_index = True)

#39
tar = tar.append({'Command': 'tar -df comics.tar naruto.pdf',
                  'NL Queries': ['Check the differences between file naruto.pdf in the archive and file system.',
                                 'Find, if there is difference between the files naruto.pdf in archive and file system.',
                                 'How to check if there is a difference between the naruto.pdf file in archive and that in file system.']}, ignore_index = True)

#40
tar = tar.append({'Command': 'tar -xf comics.tar --keep-newer-files',
                  'NL Queries': ['Extract the contents of comics.tar and keep newer files.',
                                 'Extract the contents from comics.tar archive and keep newer versions of files.',
                                 'Untar the contents of comics.tar archive and only keep those files with newer timestamps.']}, ignore_index = True)

#41
tar = tar.append({'Command': 'tar -cf comics.tar bleach.doc --remove-files',
                  'NL Queries': ['Create archive of bleach.doc as comics.tar and remove original file.',
                                 'Remove original file and create comics.tar archive from bleach.doc .',
                                 'Form archive of bleach.doc with name comics.tar and remove original copies.']}, ignore_index = True)

#42
tar = tar.append({'Command': 'tar -xOf arch.tar',
                  'NL Queries': ['Extract the files from archive arch.tar and display it on STDOUT .',
                                 'Untar the files inside arch.tar and show it on stdout .',
                                 'Extract all the files in arch.tar archive and display it as output .']}, ignore_index = True)

#43
tar = tar.append({'Command': 'tar --no-recursion -cf skew.tar /etc/',
                  'NL Queries': ['Create archive of /etc directory named skew.tar and do not descend into directories.',
                                 'Archive /etc as skew.tar and do not compress contents of subdirectories.',
                                 'Create skew.tar archive from /etc folder and do not archive sub folders.']}, ignore_index = True)

#44
tar = tar.append({'Command': 'tar --no-recursion -cvf skew.tar /etc/',
                  'NL Queries': ['Create archive of /etc directory named skew.tar and do not descend into directories. Show the list of archived entities.',
                                 'Archive /etc as skew.tar and do not compress contents of subdirectories. Show the files added to archive.',
                                 'Create skew.tar archive from /etc folder and do not archive sub folders. Display the files archived.']}, ignore_index = True)

#45
tar = tar.append({'Command': 'tar --no-recursion -czf skew.tar.gz /etc/',
                  'NL Queries': ['Create gzip archive of /etc directory named skew.tar.gz and do not descend into directories.',
                                 'Form gzip compressed archive from /etc/ directory without including subdirectories. Name the archive skew.tar.gz .',
                                 'Create gzipped archive of /etc folder and name it skew.tar.gz . Do not archive sub folders.']}, ignore_index = True)

#45
tar = tar.append({'Command': 'tar --no-recursion -cvzf skew.tar /etc/',
                  'NL Queries': ['Create gzip archive of /etc directory named skew.tar.gz and do not descend into directories. Show the list of archived entities.',
                                 'Form gzip compressed archive from /etc/ directory without including subdirectories. Name the archive skew.tar.gz and show the files added.',
                                 'Create gzipped archive of /etc folder and name it skew.tar.gz . Do not archive sub folders and display the added files.']}, ignore_index = True)

#47
tar = tar.append({'Command': 'tar --no-recursion -cjf skew.tar.bz2 /etc/',
                  'NL Queries': ['Create bzip2 archive of /etc directory named skew.tar.bz2 and do not descend into directories.',
                                 'Form bzip2 compressed archive from /etc/ directory without including subdirectories. Name the archive skew.tar.bz2 .',
                                 'Create bzipped2 archive of /etc folder and name it skew.tar.bz2 . Do not archive sub folders.']}, ignore_index = True)

#48
tar = tar.append({'Command': 'tar --no-recursion -cvjf skew.tar.bz2 /etc/',
                  'NL Queries': ['Create bzip2 archive of /etc directory named skew.tar.bz2 and do not descend into directories. Show the list of archived entities.',
                                 'Form bzip2 compressed archive from /etc/ directory without including subdirectories. Name the archive skew.tar.bz2 and show the files added.',
                                 'Create bzipped2 archive of /etc folder and name it skew.tar.bz2 . Do not archive sub folders and display the added files.']}, ignore_index = True)

#49
tar = tar.append({'Command': 'tar --xattrs -cf last.tar text.txt',
                  'NL Queries': ['Create archive, with extended attribute support, last.tar with text.txt in it.',
                                 'Create last.tar archive with extended support and add text.txt to it.',
                                 'Archive text.txt file in last.tar archive and enable extended attribute support.']}, ignore_index = True)

#50
tar = tar.append({'Command': 'tar --no-xattrs -cf last.tar text.txt',
                  'NL Queries': ['Create archive, without extended attribute support, last.tar with text.txt in it.',
                                 'Create last.tar archive without extended support and add text.txt to it.',
                                 'Archive text.txt file in last.tar archive and disable extended attribute support.']}, ignore_index = True)

#51
tar = tar.append({'Command': 'tar --xattrs -czf last.tar.gz text.txt',
                  'NL Queries': ['Create gzip archive, with extended attribute support, last.tar with text.txt in it.',
                                 'Tar the text.txt file inside last.tar.gz gzip archive with extended attribute support.',
                                 'Archive text.txt in new gzip archive last.tar.gz with extended attribute support.']}, ignore_index = True)

#52
tar = tar.append({'Command': 'tar --no-xattrs -czf last.tar.gz text.txt',
                  'NL Queries': ['Create gzip archive, without extended attribute support, last.tar with text.txt in it.',
                                 'Tar the text.txt file inside last.tar.gz gzip archive without extended attribute support.',
                                 'Archive text.txt in new gzip archive last.tar.gz without extended attribute support.']}, ignore_index = True)

#53
tar = tar.append({'Command': 'tar --xattrs -cjf last.tar.bz2 text.txt',
                  'NL Queries': ['Create bzip2 archive, with extended attribute support, last.tar with text.txt in it.',
                                 'Tar the text.txt file inside last.tar.bz2 bzip2 archive with extended attribute support.',
                                 'Archive text.txt in new bzip2 archive last.tar.bz2 with extended attribute support.']}, ignore_index = True)

#54
tar = tar.append({'Command': 'tar --no-xattrs -cjf last.tar.bz2 text.txt',
                  'NL Queries': ['Create bxip2 archive, without extended attribute support, last.tar with text.txt in it.',
                                 'Tar the text.txt file inside last.tar.bz2 bzip2 archive without extended attribute support.',
                                 'Archive text.txt in new bzip2 archive last.tar.bz2 without extended attribute support.']}, ignore_index = True)

#55
tar = tar.append({'Command': 'tar --selinux -cf suits.tar harvey.txt',
                  'NL Queries': ['Create an archive named suits.tar of harvey.txt with SELinux support.',
                                 'Archive harvey.txt with name suits.tar and selinux support.',
                                 'Tar harvey.txt in new archive, suits.tar with sel enabled.']}, ignore_index = True)

#56
tar = tar.append({'Command': 'tar --no-selinux -cf suits.tar harvey.txt',
                  'NL Queries': ['Create an archive named suits.tar of harvey.txt without SELinux support.',
                                 'Archive harvey.txt with name suits.tar and selinux support disabled.',
                                 'Tar harvey.txt in new archive, suits.tar without sel.']}, ignore_index = True)

#57
tar = tar.append({'Command': 'tar --selinux -cjf last.tar.bz2 text.txt',
                  'NL Queries': ['Create bzip2 archive, with extended selinux support, last.tar with text.txt in it.',
                                 'Create bz2 archive text.txt with name last.tar.bz2 and selinux support.',
                                 'Tar text.txt in new bzip2 archive, last.tar with sel enabled.']}, ignore_index = True)

#58
tar = tar.append({'Command': 'tar --no-selinux -cjf last.tar.bz2 text.txt',
                  'NL Queries': ['Create bxip2 archive, without selinux support, last.tar with text.txt in it.',
                                 'Create bz2 archive text.txt with name last.tar.bz2 and selinux support disabled.',
                                 'Tar text.txt in new bzip2 archive, last.tar without sel.']}, ignore_index = True)

#59
tar = tar.append({'Command': 'tar --selinux -czf suits.tar.gz harvey.txt',
                  'NL Queries': ['Create a gzip archive named suits.tar.gz of harvey.txt with SELinux support.',
                                 'gzip archive harvey.txt with name suits.tar.gz and selinux support.',
                                 'Tar harvey.txt in new gz archive, suits.tar.gz with sel enabled.']}, ignore_index = True)

#60
tar = tar.append({'Command': 'tar --no-selinux -czf suits.tar.gz harvey.txt',
                  'NL Queries': ['Create a gzip archive named suits.tar.gz of harvey.txt without SELinux support.',
                                 'gzip archive harvey.txt with name suits.tar.gz and selinux support removed.',
                                 'Tar harvey.txt in new gz archive, suits.tar.gz without sel.']}, ignore_index = True)

#61
tar = tar.append({'Command': 'tar --no-recursion -cwf anime.tar Manga/',
                  'NL Queries': ['Create an archive of directory Manga as anime.tar . Do not descend into directories and ask for each file to be added to archive or not.',
                                 'How to archive Manga directory in new archive anime.tar without archiveing subdirectories with my permission?',
                                 'Archive Manga as anime.tar without descending into sub-folders. Ask for permission for each file to be added to archive.']}, ignore_index = True)

#62
tar = tar.append({'Command': 'tar --no-recursion -cwzf anime.tar.gz Manga/',
                  'NL Queries': ['Create an gzip archive of directory Manga as anime.tar.gz . Do not descend into directories and ask for each file to be added to archive or not.',
                                 'Without descending into directories, archive Manga folder in gzip format with name anime.tar.gz . Ask for each file to be added.',
                                 'Compress Manga folder as anime.tar.gz in gzip format without traversing sub-directories. Ask for permission to add each file.']}, ignore_index = True)

#63
tar = tar.append({'Command': 'tar --no-recursion -cwjf anime.tar.bz2 Manga/',
                  'NL Queries': ['Create an bzip2 archive of directory Manga as anime.tar.gz . Do not descend into directories and ask for each file to be added to archive or not.',
                                 'Without descending into directories, archive Manga folder in bzip2 format with name anime.tar.bz2 . Ask for each file to be added.',
                                 'Compress Manga folder as anime.tar.bz2 in bzip2 format without traversing sub-directories. Ask for permission to add each file.']}, ignore_index = True)

#64
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -cf anime.tar Manga/',
                  'NL Queries': ['Create an archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar .',
                                 'Excluding .avi files, archive Manga directory as anime.tar .',
                                 'Compress Manga folder inside anime.tar without including .avi files.']}, ignore_index = True)

#65
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -cjf anime.tar.bz2 Manga/',
                  'NL Queries': ['Create a bz2 archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar .',
                                 'Excluding .avi files, archive Manga directory as anime.tar.bz2 . Compress the archive using bz2 method.',
                                 'Compress Manga folder inside anime.tar.bz without including .avi files. Use bz2 compression method.']}, ignore_index = True)

#66
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -czf anime.tar.gz Manga/',
                  'NL Queries': ['Create a gz archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar .',
                                 'Excluding .avi files, archive Manga directory as anime.tar.gz . Compress the archive using gzip method.',
                                 'Compress Manga folder inside anime.tar.gz without including .avi files. Use gz compression method.']}, ignore_index = True)

#67
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -cvf anime.tar Manga/',
                  'NL Queries': ['Create an archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar and show the archived files.',
                                 'Excluding .avi files, archive Manga directory as anime.tar and show the list of added files.',
                                 'Compress Manga folder inside anime.tar without including .avi files and display the names of files that were archived.']}, ignore_index = True)

#68
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -cjvf anime.tar.bz2 Manga/',
                  'NL Queries': ['Create a bz2 archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar.bz2 and show the archived files.',
                                 'Excluding .avi files, archive Manga directory as anime.tar.bz2 . Compress the archive using bz2 method and give acknowledgement for added files.',
                                 'Compress Manga folder inside anime.tar.bz without including .avi files. Use bz2 compression method and return names of added files for reference.']}, ignore_index = True)

#69
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -czvf anime.tar.gz Manga/',
                  'NL Queries': ['Create a gz archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar and show the archived files.',
                                 'Excluding .avi files, archive Manga directory as anime.tar.gz . Compress the archive using gzip method and display the added files.',
                                 'Compress Manga folder inside anime.tar.gz without including .avi files. Use gz compression method and show the names of added files.']}, ignore_index = True)

#70
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -cwf anime.tar Manga/',
                  'NL Queries': ['Create an archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar . Ask before adding each file.',
                                 'Excluding .avi files create archive of Manga directory as anime.tar and ask for adding each file.',
                                 'Archive Manga folder as anime.tar but do not include any file whose name ends with .avi . Ask before adding each file.']}, ignore_index = True)

#71
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -cjwf anime.tar.bz2 Manga/',
                  'NL Queries': ['Create a bz2 archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar . Ask before adding each file.',
                                 'Excluding .avi files create bzip2 archive of Manga directory as anime.tar.bz2 and ask for adding each file.',
                                 'Archive Manga folder as anime.tar but do not include any file whose name ends with .avi . Ask before adding each file and use bz2 form of compression.']}, ignore_index = True)

#72
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -cwzf anime.tar.gz Manga/',
                  'NL Queries': ['Create a gz archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar . Ask before adding each file.',
                                 'Excluding .avi files create gzip archive of Manga directory as anime.tar.gz and ask for adding each file.',
                                 'Archive Manga folder as anime.tar.gz but do not include any file whose name ends with .avi . Ask before adding each file and use gzip form of compression.']}, ignore_index = True)

#73
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -cvwf anime.tar Manga/',
                  'NL Queries': ['Create an archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar and show the archived files. Ask before adding each file.',
                                 'Excluding .avi files create archive of Manga directory as anime.tar and ask for adding each file. Give acknowledgement for added files.',
                                 'Archive Manga folder as anime.tar but do not include any file whose name ends with .avi . Ask before adding each file and show the names of added files.']}, ignore_index = True)

#74
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -czwvf anime.tar.gz Manga/',
                  'NL Queries': ['Create a gz archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar and show the archived files. Ask before adding each file.',
                                 'Excluding all files with .avi extension compress Manga directory as gz archive with name anime.tar.gz . Ask before adding each file and show the archived files.',
                                 'Archive Manga folder as gzip archive under the name anime.tar.gz and do not include .avi files. Ask before adding each file and show the name as acknowledgement for added files.']}, ignore_index = True)

#75
tar = tar.append({'Command': 'tar --exclude=\"*.avi\" -cjwvf anime.tar.bz2 Manga/',
                  'NL Queries': ['Create a bz2 archive of Manga directory after excluding all the files ending with \'.avi\' and save it as anime.tar and show the archived files. Ask before adding each file.',
                                 'Excluding all files with .avi extension compress Manga directory as bz2 archive with name anime.tar.bz2 . Ask before adding each file and show the archived files.',
                                 'Archive Manga folder as bzip2 archive under the name anime.tar.bz2 and do not include .avi files. Ask before adding each file and show the name as acknowledgement for added files.']}, ignore_index = True)

#76
tar = tar.append({'Command': 'tar -xf anime.tar --wildcards \"*.txt\"',
                  'NL Queries': ['Extract all files from anime.tar which end with \'.txt\' .',
                                 'Untar all the files ending with .txt inside anime.tar .',
                                 'Uncompress all files with .txt extension inside anime.tar archive.']}, ignore_index = True)

#77
tar = tar.append({'Command': 'tar -xvf anime.tar --wildcards \"*.txt\"',
                  'NL Queries': ['Extract all files from anime.tar which end with \'.txt\' and show the list of extracted files.',
                                 'Untar all the files ending with .txt inside anime.tar and show the list of extracted files.',
                                 'Uncompress all files with .txt extension inside anime.tar archive and display which files were extracted.']}, ignore_index = True)

#78
tar = tar.append({'Command': 'tar --help',
                  'NL Queries': ['Display summary of tar command.',
                                 'Show options available with tar command with details.',
                                 'Which options are available with tar command? Also show the details for options.']}, ignore_index = True)

#79
tar = tar.append({'Command': 'tar --usage',
                  'NL Queries': ['Display options available to use with tar command.',
                                 'How to use tar command?',
                                 'Display the options available for use with tar command.']}, ignore_index = True)

#80
tar = tar.append({'Command': 'tar --version',
                  'NL Queries': ['Display version of tar command.',
                                 'Show version number of tar command.',
                                 'Display authors of tar command.',
                                 'Display authors and version of tar command.']}, ignore_index = True)

print tar
