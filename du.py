import pandas as pd 
# coding=utf-8

'''
		-0, --null
              end each output line with NUL, not newline

       -a, --all
              write counts for all files, not just directories

       --apparent-size
              print apparent sizes, rather than disk usage; although the apparent size is usually smaller, it may be larger due to
              holes in ('sparse') files, internal fragmentation, indirect blocks, and the like

       -B, --block-size=SIZE
              scale sizes by SIZE before printing them; e.g., '-BM' prints sizes in units of  1,048,576  bytes;  see  SIZE  format
              below

       -b, --bytes
              equivalent to '--apparent-size --block-size=1'

       -c, --total
              produce a grand total

       -D, --dereference-args
              dereference only symlinks that are listed on the command line

       -d, --max-depth=N
              print  the  total for a directory (or file, with --all) only if it is N or fewer levels below the command line argu‐
              ment;  --max-depth=0 is the same as --summarize

       --files0-from=F
              summarize disk usage of the NUL-terminated file names specified in file F; if F is -, then read names from  standard
              input

       -H     equivalent to --dereference-args (-D)

       -h, --human-readable
              print sizes in human readable format (e.g., 1K 234M 2G)

       --inodes
              list inode usage information instead of block usage

       -k     like --block-size=1K

       -L, --dereference
              dereference all symbolic links

       -l, --count-links
              count sizes many times if hard linked

       -m     like --block-size=1M

       -P, --no-dereference
              don't follow any symbolic links (this is the default)

       -S, --separate-dirs
              for directories do not include size of subdirectories

       --si   like -h, but use powers of 1000 not 1024

       -s, --summarize
              display only a total for each argument

       -t, --threshold=SIZE
              exclude entries smaller than SIZE if positive, or entries greater than SIZE if negative

       --time show time of the last modification of any file in the directory, or any of its subdirectories

       --time=WORD
              show time as WORD instead of modification time: atime, access, use, ctime or status

       --time-style=STYLE
              show times using STYLE, which can be: full-iso, long-iso, iso, or +FORMAT; FORMAT is interpreted like in 'date'

       -X, --exclude-from=FILE
              exclude files that match any pattern in FILE

       --exclude=PATTERN
              exclude files that match PATTERN

       -x, --one-file-system
              skip directories on different file systems
'''

du = pd.DataFrame(columns = ['Command','NL Queries'])

'''du = du.append({'Command':'du -s *.txt','NL Queries':['Display file size of all files in this folder with extension txt.',
													'How do I check file sizes of all .txt files in this folder?']},ignore_index=True)

du = du.append({'Command':'du  -h /home/ananyaraval','NL Queries':['Show amount of memory occupied by all folders in /home/ananyaraval. Show the memory with units I understand.',
																	'Display the amount of memory occupied by each folder in /home/ananyaraval, using KiloBytes, MegaBytes as units.']},ignore_index=True)

du = du.append({'Command':'du -c /home/ananyaraval','NL Queries':['Display memory usage of each folder in /home/ananyaraval along with total memory usage of /home/ananyaraval.',
																	'Show individual and cumulative diska usage of folders in /home/ananyaraval.']},ignore_index=True)

du = du.append({'Command':'du -sh /home/user','NL Queries':['Displays the total memory occupied by the folder /home/user in Megabytes', 'How do I check total memory occupied by the folder?']},ignore_index=True)'''

du = du.append({'Command':'du -a /home/user/','NL Queries':['Display the memory occupied by each file in the folder and the sub-folders in /home/user/.', 
															'How do I check total memory occupied by the files in the folder and the sub-folder in /home/user/?',
															'View the memory occupied by each file in the folder and the sub-folders in /home/user/.',
															'How do I show the memory occupied by the files in the folders and sub-folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du -b /home/user/','NL Queries':['Display the memory occupied by the folders in /home/user/ in terms of bytes ignoring the folders which have 0 bytes.', 
															'How do I check the memory occupied by the folder in /home/user/ in terms of bytes and ignore the folders which have zero byte size?',
															'View the memory occupied by the folder in /home/user/ in terms of bytes. Ignore the folders which donot have any folders or files in them.',
															'How do I show the memory occupied by the folders in /home/user/ in terms of bytes and ignore the folders which occupy zero bytes memory?']},ignore_index=True)

du = du.append({'Command':'du -BG /home/user/','NL Queries':['Display the memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes.', 
															'How do I check the memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes?']},ignore_index=True)
																				
du = du.append({'Command':'du -BK /home/user/','NL Queries':['Display the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I check the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -BM /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -BT /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes.',
															'How do I check the memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du -BP /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du -BY /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes.', 
															'How do I check the memory occupied by the folder and the sub-folders\ in /home/user/ in terms of Yottabytes?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du -BZ /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes?']},ignore_index=True)

du = du.append({'Command':'du -BE /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes.', 
															'How do I check memory occupied by the folder in /home/user/ in terms of Exabytes?',
															'View the memory occupied by the folder in /home/user/ in terms of Exabytes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes?']},ignore_index=True)

du = du.append({'Command':'du -c /home/user/','NL Queries':['Display memory usage of each folder along with total memory usage of /home/user/.',
															'Show individual and cumulative disk usage of the folders in /home/user/.',
															'How do I view the memory usage of each folder along with the total memory usage of /home/user/?',
															'How do I view the individual and cumulative disk usage of the folders in /home/user/?']},ignore_index=True)
														
du = du.append({'Command':'du -d1 /home/user/','NL Queries':['Display memory usage of the folders in /home/user/.',
															'Check the individual disk usage of each of the folders in /home/user/.',
															'How do I show the memory usage of each folder in /home/user/?',
															'How do I check the individual disk usage of the folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du -d0 /home/user/','NL Queries':['Display total memory usage of the folders in /home/user/.',
															'Check the total disk usage of the folders in /home/user/.',
															'How do I show the total memory usage of all the folders in /home/user/?',
															'How do I check the cumulative disk usage of the folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du -d2 /home/user/','NL Queries':['Display memory usage of the folders and sub-folders in /home/user/.',
															'Check the individual disk usage of each of the folders and sub-folders in /home/user/.',
															'How do I show the memory usage of each folder and sub-folder in /home/user/?',
															'How do I check the individual disk usage of the folders and sub-folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du --inodes /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Inodes.', 
															'How do I check memory occupied by the folder in /home/user/ in terms of Inodes?',
															'View the memory occupied by the folder in /home/user/ in terms of Inodes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Inodes?']},ignore_index=True)

du = du.append({'Command':'du -k /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I check the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -m /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the folders and sub-folders in /home/user/.',
															'Check the individual disk usage and last modified date, time of each of the folders and sub-folders in /home/user/.',
															'How do I show the memory usage and last modified date, time of each folder and sub-folder in /home/user/?',
															'How do I check the individual disk usage and last modified date, time of the folders and sub-folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the folders and sub-folders in /home/user/.',
															'Check the individual disk usage and last modified date, time of each of the folders and sub-folders in /home/user/.',
															'How do I show the memory usage and last modified date, time of each folder and sub-folder in /home/user/?',
															'How do I check the individual disk usage and last modified date, time of the folders and sub-folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the folders and sub-folders in /home/user/.',
															'Check the individual disk usage and last modified date of each of the folders and sub-folders in /home/user/.',
															'How do I show the memory usage and last modified date of each folder and sub-folder in /home/user/?',
															'How do I check the individual disk usage and last modified date of the folders and sub-folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -s *.out','NL Queries':['Display total file size of all files in this folder with extension .out.',
															'How do I check total file size of all .out files in this folder?',
															'Check the total file size of the files in the folder containing the file extension .out.',
															'How do I show the total file size of all the files in the folder having the extension .out.']},ignore_index=True)

# This ends all Chocolate Combinations :P

du = du.append({'Command':'du -a -b /home/user/','NL Queries':['Displays the memory occupied by each file in the folders in /home/user/ in terms of bytes ignoring the folders which have 0 bytes.', 
															'How do I check the memory occupied by each file in the folder in /home/user/ in terms of bytes and ignore the folders which have zero byte size?',
															'View the memory occupied by each file in the folder in /home/user/ in terms of bytes. Ignore the folders which donot have any folders or files in them.',
															'How do I show the memory occupied by each file in the folders in /home/user/ in terms of bytes and ignore the folders which occupy zero bytes memory?']},ignore_index=True)

du = du.append({'Command':'du -a -BG /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Gigabytes.', 
															'How do I check the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Gigabytes?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Gigabytes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Gigabytes?']},ignore_index=True)
																				
du = du.append({'Command':'du -a -BK /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I check the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -a -BM /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Megabytes.', 
															'How do I view the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Megabytes?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Megabytes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -a -BT /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Terabytes.', 
															'How do I view the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Terabytes?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Terabytes.',
															'How do I check the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du -a -BP /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Petabytes.', 
															'How do I view the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Petabytes?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Petabytes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du -a -BY /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Yottabytes.', 
															'How do I check the memory occupied by each file in the folder and the sub-folders\ in /home/user/ in terms of Yottabytes?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Yottabytes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du -a -BZ /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Zetabytes.', 
															'How do I view the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Zetabytes?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Zetabytes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Zetabytes?']},ignore_index=True)

du = du.append({'Command':'du -a -BE /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Exabytes.', 
															'How do I check memory occupied by each file in the folder in /home/user/ in terms of Exabytes?',
															'View the memory occupied by each file in the folder in /home/user/ in terms of Exabytes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Exabytes?']},ignore_index=True)

du = du.append({'Command':'du -a -h /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in Human Readable Format.', 
															'How do I view the memory occupied by each file in the folder and the sub-folder in /home/user/ in Human Readable Format?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in Human Readable Format.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -a --inodes /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Inodes.', 
															'How do I check memory occupied by each file in the folder in /home/user/ in terms of Inodes?',
															'View the memory occupied by each file in the folder in /home/user/ in terms of Inodes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Inodes?']},ignore_index=True)

du = du.append({'Command':'du -a -k /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I check the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -a -m /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Megabytes.', 
															'How do I view the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Megabytes?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in terms of Megabytes.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -a --si /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ in powers of 1000.', 
															'How do I view the memory occupied by each file in the folder and the sub-folder in /home/user/ in powers of 1000?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/ in powers of 1000.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -a -t10K /home/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /home/user/ by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by each file in the folder and the sub-folder in /home/user/ and ignore the folders having size less than 10K?',
															'View the memory occupied by each file in the folder and the sub-folder in /home/user/. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /home/user/ by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -a --time /home/user/','NL Queries':['Display memory usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du -a --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/?',
															'How do I check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du -a --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of each of the files in the folders and sub-folders in /home/user/.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/.',
															'How do I show the memory usage and last modified date of each of the files in the folder and sub-folder in /home/user/?',
															'How do I check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/?']},ignore_index=True)

du = du.append({'Command':'du -a -x /media/user/','NL Queries':['Displays the memory occupied by each file in the folders and sub-folders in /media/user/ by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by each file in the folder and the sub-folder in /media/user/ and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by each file in the folder and the sub-folder in /media/user/. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by each file in the folders and sub-folders in /media/user/ by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -a -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/.', 
															'How do I view the total file size of all the files in /home/user/?',
															'View the total file size of all the files in /home/user/.',
															'How do I show the total file size of all the files in /home/user/?']},ignore_index=True)


# This ends all combinations for -a

du = du.append({'Command':'du -c -BG /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes.', 
															'How do I check the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes?',
															'View the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes.',
															'How do I show the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes?']},ignore_index=True)
																				
du = du.append({'Command':'du -c -BK /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I check the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -c -BM /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes.', 
															'How do I view the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes?',
															'View the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes.',
															'How do I show the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -c -BT /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes.', 
															'How do I view the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes?',
															'View the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes.',
															'How do I check the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du -c -BP /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes.', 
															'How do I view the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes?',
															'View the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes.',
															'How do I show the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du -c -BY /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes.', 
															'How do I check the individual and cumulative memory occupied by the folder and the sub-folders\ in /home/user/ in terms of Yottabytes?',
															'View the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes.',
															'How do I show the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du -c -BZ /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes.', 
															'How do I view the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes?',
															'View the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes.',
															'How do I show the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes?']},ignore_index=True)

du = du.append({'Command':'du -c -BE /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes.', 
															'How do I check memory occupied by the folder in /home/user/ in terms of Exabytes?',
															'View the individual and cumulative memory occupied by the folder in /home/user/ in terms of Exabytes.',
															'How do I show the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes?']},ignore_index=True)

du = du.append({'Command':'du -c -k /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I check the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -c -m /home/user/','NL Queries':['Displays the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes.', 
															'How do I view the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes?',
															'View the individual and cumulative memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes.',
															'How do I show the individual and cumulative memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

# This ends all combinations for -c

du = du.append({'Command':'du -h -a /home/user/','NL Queries':['Displays the memory occupied by each file in the folder and the sub-folders in /home/user/ in human readable format.', 
															'How do I check total memory occupied by the files in the folder and the sub-folder in /home/user/ in human readable format?',
															'View the memory occupied by each file in the folder and the sub-folders in /home/user/ in human readable format.',
															'How do I show the total memory occupied by the files in the folders and sub-folders in /home/user/ in human readable format?']},ignore_index=True)

du = du.append({'Command':'du -h -b /home/user/','NL Queries':['Displays the memory occupied by the folders in /home/user/ in human readable format in terms of bytes ignoring the folders which have 0 bytes.', 
															'How do I check the memory occupied by the folder in /home/user/ in human readable format in terms of bytes and ignore the folders which have zero byte size?',
															'View the memory occupied by the folder in /home/user/ in human readable format in terms of bytes. Ignore the folders which donot have any folders or files in them.',
															'How do I show the memory occupied by the folders in /home/user/ in human readable format in terms of bytes and ignore the folders which occupy zero bytes memory?']},ignore_index=True)

du = du.append({'Command':'du -h --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in human readable format in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in human readable format in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in human readable format in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in human readable format in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -h -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in human readable format by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in human readable format and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in human readable format. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in human readable format by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -h --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in human readable format.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in human readable format.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in human readable format?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in human readable format?']},ignore_index=True)

du = du.append({'Command':'du -h --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in human readable format.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in human readable format.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in human readable format?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in human readable format?']},ignore_index=True)

du = du.append({'Command':'du -h --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in human readable format.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in human readable format.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in human readable format?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in human readable format?']},ignore_index=True)

du = du.append({'Command':'du -h -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in human readable format by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in human readable format and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in human readable format. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in human readable format by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -h -s /home/user/','NL Queries':['Displays the total file size of files in /home/user/ in human readable format.', 
															'How do I view the total file size of files in /home/user/ in human readable format?',
															'View the total file size of files in /home/user/ in human readable format.',
															'How do I show the total file size of files in /home/user/ in human readable format?']},ignore_index=True)

# This ends all combinations for -h

du = du.append({'Command':'du -s -BG /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Gigabytes.', 
															'How do I check the total file size of the files in in /home/user/ in terms of Gigabytes?',
															'View the total file size of the files in in /home/user/ in terms of Gigabytes.',
															'How do I show the total file size of the files in in /home/user/ in terms of Gigabytes?']},ignore_index=True)
																				
du = du.append({'Command':'du -s -BK /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Kilobytes.', 
															'How do I check the total file size of the files in in /home/user/ in terms of Kilobytes?',
															'View the total file size of the files in in /home/user/ in terms of Kilobytes.',
															'How do I show the total file size of the files in in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -s -BM /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Megabytes.', 
															'How do I view the total file size of the files in in /home/user/ in terms of Megabytes?',
															'View the total file size of the files in in /home/user/ in terms of Megabytes.',
															'How do I show the total file size of the files in in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -s -BT /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Terabytes.', 
															'How do I view the total file size of the files in in /home/user/ in terms of Terabytes?',
															'View the total file size of the files in in /home/user/ in terms of Terabytes.',
															'How do I check the total file size of the files in in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du -s -BP /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Petabytes.', 
															'How do I view the total file size of the files in in /home/user/ in terms of Petabytes?',
															'View the total file size of the files in in /home/user/ in terms of Petabytes.',
															'How do I show the total file size of the files in in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du -s -BY /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Yottabytes.', 
															'How do I check the total file size of the files ins\ in /home/user/ in terms of Yottabytes?',
															'View the total file size of the files in in /home/user/ in terms of Yottabytes.',
															'How do I show the total file size of the files in in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du -s -BZ /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Zetabytes.', 
															'How do I view the total file size of the files in in /home/user/ in terms of Zetabytes?',
															'View the total file size of the files in in /home/user/ in terms of Zetabytes.',
															'How do I show the total file size of the files in in /home/user/ in terms of Zetabytes?']},ignore_index=True)

du = du.append({'Command':'du -s -BE /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Exabytes.', 
															'How do I check memory occupied by the folder in /home/user/ in terms of Exabytes?',
															'View the individual and cumulative memory occupied by the folder in /home/user/ in terms of Exabytes.',
															'How do I show the total file size of the files in in /home/user/ in terms of Exabytes?']},ignore_index=True)

du = du.append({'Command':'du -s -k /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Kilobytes.', 
															'How do I check the total file size of the files in in /home/user/ in terms of Kilobytes?',
															'View the total file size of the files in in /home/user/ in terms of Kilobytes.',
															'How do I show the total file size of the files in in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -s -m /home/user/','NL Queries':['Displays the total file size of the files in in /home/user/ in terms of Megabytes.', 
															'How do I view the total file size of the files in in /home/user/ in terms of Megabytes?',
															'View the total file size of the files in in /home/user/ in terms of Megabytes.',
															'How do I show the total file size of the files in in /home/user/ in terms of Megabytes?']},ignore_index=True)

# This ends all combinations for -s

du = du.append({'Command':'du --inodes -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of inodes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of inodes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of inodes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of inodes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du --inodes --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of inodes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of inodes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of inodes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of inodes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du --inodes -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of inodes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of inodes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of inodes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of inodes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du --inodes --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of inodes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of inodes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of inodes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of inodes?']},ignore_index=True)

du = du.append({'Command':'du --inodes --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of inodes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of inodes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of inodes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of inodes?']},ignore_index=True)

du = du.append({'Command':'du --inodes --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of inodes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of inodes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of inodes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of inodes?']},ignore_index=True)

du = du.append({'Command':'du --inodes -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of inodes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of inodes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of inodes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of inodes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du --inodes -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of inodes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of inodes?',
															'View the total file size of all the files in /home/user/ in terms of inodes.',
															'How do I show the total file size of all the files in /home/user/ in terms of inodes?']},ignore_index=True)

# This ends all combinations for --inodes

du = du.append({'Command':'du -BG -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -BG --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -BG -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -BG --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Gigabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Gigabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Gigabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Gigabytes?']},ignore_index=True)

du = du.append({'Command':'du -BG --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Gigabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Gigabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Gigabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Gigabytes?']},ignore_index=True)

du = du.append({'Command':'du -BG --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Gigabytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Gigabytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Gigabytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Gigabytes?']},ignore_index=True)

du = du.append({'Command':'du -BG -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Gigabytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Gigabytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Gigabytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Gigabytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -BG -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Gigabytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Gigabytes?',
															'View the total file size of all the files in /home/user/ in terms of Gigabytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Gigabytes?']},ignore_index=True)


#This ends all combinations for -BG

du = du.append({'Command':'du -BK -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -BK --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -BK -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -BK --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Kilobytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -BK --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Kilobytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -BK --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Kilobytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -BK -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Kilobytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Kilobytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Kilobytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Kilobytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -BK -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Kilobytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Kilobytes?',
															'View the total file size of all the files in /home/user/ in terms of Kilobytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Kilobytes?']},ignore_index=True)


#This ends all combinations for -BK

du = du.append({'Command':'du -BM -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -BM --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -BM -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -BM --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Megabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -BM --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Megabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -BM --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Megabytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -BM -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Megabytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Megabytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Megabytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Megabytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -BM -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Megabytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Megabytes?',
															'View the total file size of all the files in /home/user/ in terms of Megabytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Megabytes?']},ignore_index=True)


#This ends all combinations for -BM

du = du.append({'Command':'du -BT -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -BT --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -BT -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -BT --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Terabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Terabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Terabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du -BT --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Terabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Terabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Terabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du -BT --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Terabytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Terabytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Terabytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du -BT -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Terabytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Terabytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Terabytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Terabytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -BT -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Terabytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Terabytes?',
															'View the total file size of all the files in /home/user/ in terms of Terabytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Terabytes?']},ignore_index=True)


#This ends combinations for -BT

du = du.append({'Command':'du -BP -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -BP --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -BP -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -BP --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Petabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Petabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Petabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du -BP --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Petabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Petabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Petabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du -BP --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Petabytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Petabytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Petabytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du -BP -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Petabytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Petabytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Petabytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Petabytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -BP -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Petabytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Petabytes?',
															'View the total file size of all the files in /home/user/ in terms of Petabytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Petabytes?']},ignore_index=True)


#This ends all combinations for -BP

du = du.append({'Command':'du -BY -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -BY --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -BY -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -BY --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Yottabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Yottabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Yottabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du -BY --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Yottabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Yottabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Yottabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du -BY --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Yottabytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Yottabytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Yottabytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du -BY -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Yottabytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Yottabytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Yottabytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Yottabytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -BY -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Yottabytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Yottabytes?',
															'View the total file size of all the files in /home/user/ in terms of Yottabytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Yottabytes?']},ignore_index=True)


#This ends all combinations for -BY

du = du.append({'Command':'du -BZ -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -BZ --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -BZ -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Zetabytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Zetabytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -BZ --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Zetabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Zetabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Zetabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Zetabytes?']},ignore_index=True)

du = du.append({'Command':'du -BZ --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Zetabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Zetabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Zetabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Zetabytes?']},ignore_index=True)

du = du.append({'Command':'du -BZ --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Zetabytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Zetabytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Zetabytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Zetabytes?']},ignore_index=True)

du = du.append({'Command':'du -BZ -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Zetabytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Zetabytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Zetabytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Zetabytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -BZ -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Zetabytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Zetabytes?',
															'View the total file size of all the files in /home/user/ in terms of Zetabytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Zetabytes?']},ignore_index=True)


#This ends all combinations for -BZ

du = du.append({'Command':'du -BE -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Exabytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Exabytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -BE --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Exabytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Exabytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -BE -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Exabytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Exabytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -BE --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Exabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Exabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Exabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Exabytes?']},ignore_index=True)

du = du.append({'Command':'du -BE --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Exabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Exabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Exabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Exabytes?']},ignore_index=True)

du = du.append({'Command':'du -BE --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Exabytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Exabytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Exabytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Exabytes?']},ignore_index=True)

du = du.append({'Command':'du -BE -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Exabytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Exabytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Exabytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Exabytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -BE -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Exabytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Exabytes?',
															'View the total file size of all the files in /home/user/ in terms of Exabytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Exabytes?']},ignore_index=True)

#This ends all combinations for -BE

du = du.append({'Command':'du -m -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -m --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -m -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -m --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Megabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -m --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Megabytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -m --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Megabytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Megabytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du -m -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Megabytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Megabytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Megabytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Megabytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -m -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Megabytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Megabytes?',
															'View the total file size of all the files in /home/user/ in terms of Megabytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Megabytes?']},ignore_index=True)


#This ends all combinations for -m

du = du.append({'Command':'du -k -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -k --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -k -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -k --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Kilobytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -k --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of Kilobytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -k --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of Kilobytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du -k -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of Kilobytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of Kilobytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of Kilobytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of Kilobytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -k -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of Kilobytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of Kilobytes?',
															'View the total file size of all the files in /home/user/ in terms of Kilobytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of Kilobytes?']},ignore_index=True)


#This ends all combinations for -k

du = du.append({'Command':'du -b -h /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of bytes in Human Readable Format.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of bytes in Human Readable Format?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of bytes in Human Readable Format.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of bytes in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du -b --si /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of bytes in powers of 1000.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of bytes in powers of 1000?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of bytes in powers of 1000.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of bytes in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du -b -t10K /home/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /home/user/ in terms of bytes by ignoring the folders having size less than 10K.', 
															'How do I view the memory occupied by the folder and the sub-folder in /home/user/ in terms of bytes and ignore the folders having size less than 10K?',
															'View the memory occupied by the folder and the sub-folder in /home/user/ in terms of bytes. Ignore the folders which have size less than 10K.',
															'How do I show the memory occupied by the folders and sub-folders in /home/user/ in terms of bytes by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du -b --time /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of bytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of bytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of bytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of bytes?']},ignore_index=True)

du = du.append({'Command':'du -b --time --time-style=long-iso /home/user/','NL Queries':['Display memory usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of bytes.',
															'Check the individual disk usage and last modified date, time of each of the files in the folders and sub-folders in /home/user/ in terms of bytes.',
															'How do I show the memory usage and last modified date, time of each of the files in the folder and sub-folder in /home/user/ in terms of bytes?',
															'How do I check the individual disk usage and last modified date, time of the files in the folders and sub-folders in /home/user/ in terms of bytes?']},ignore_index=True)

du = du.append({'Command':'du -b --time --time-style=iso /home/user/','NL Queries':['Display memory usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of bytes.',
															'Check the individual disk usage and last modified date of each of the files in the folders and sub-folders in /home/user/ in terms of bytes.',
															'How do I show the memory usage and last modified date of each of thefiles in the folder and sub-folder in /home/user/ in terms of bytes?',
															'How do I check the individual disk usage and last modified date of the files in the folders and sub-folders in /home/user/ in terms of bytes?']},ignore_index=True)

du = du.append({'Command':'du -b -x /media/user/','NL Queries':['Displays the memory occupied by the folders and sub-folders in /media/user/ in terms of bytes by ignoring the folders of different filesystem.', 
															'How do I view the memory occupied by the folder and the sub-folder in /media/user/ in terms of bytes and ignore the folders mounted from a different filesystem?',
															'View the memory occupied by the folder and the sub-folder in /media/user/ in terms of bytes. Ignore the folders which are of a different filesystem.',
															'How do I show the memory occupied by the folders and sub-folders in /media/user/ in terms of bytes by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du -b -s /home/user/','NL Queries':['Displays the total file size of all the files in /home/user/ in terms of bytes.', 
															'How do I view the total file size of all the files in /home/user/ in terms of bytes?',
															'View the total file size of all the files in /home/user/ in terms of bytes.',
															'How do I show the total file size of all the files in /home/user/ in terms of bytes?']},ignore_index=True)


#This ends all combinations for -b

du = du.append({'Command':'du --time -h /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in Human Readable Format.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in Human Readable Format?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in Human Readable Format.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du --time -BG /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes.', 
															'How do I check the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes?']},ignore_index=True)
																				
du = du.append({'Command':'du --time -BK /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I check the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du --time -BM /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du --time -BT /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes.',
															'How do I check the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du --time -BP /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du --time -BY /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes.', 
															'How do I check the last modification date, time and memory occupied by the folder and the sub-folders\ in /home/user/ in terms of Yottabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du --time -BZ /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du --time -BE /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes.', 
															'How do I check last modification date, time and memory occupied by the folder in /home/user/ in terms of Exabytes?',
															'View the last modification date, time and memory occupied by the folder in /home/user/ in terms of Exabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes?']},ignore_index=True)


du = du.append({'Command':'du --time --si /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in powers of 1000.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in powers of 1000?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in powers of 1000.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du --time -t10K /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ by ignoring the folders having size less than 10K.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ and ignore the folders having size less than 10K?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/. Ignore the folders which have size less than 10K.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du --time -x /media/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /media/user/ by ignoring the folders of different filesystem.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /media/user/ and ignore the folders mounted from a different filesystem?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /media/user/. Ignore the folders which are of a different filesystem.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /media/user/ by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du --time -s /home/user/','NL Queries':['Displays the last modification date, time and total file size of all the files in /home/user/.', 
															'How do I view the last modification date, time and total file size of all the files in /home/user/?',
															'View the last modification date, time and total file size of all the files in /home/user/.',
															'How do I show the last modification date, time and total file size of all the files in /home/user/?']},ignore_index=True)


#This ends all combinations for --time

du = du.append({'Command':'du --time --time-style=iso -h /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in Human Readable Format.', 
															'How do I view the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in Human Readable Format?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in Human Readable Format.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -BG /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes.', 
															'How do I check the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes?']},ignore_index=True)
																				
du = du.append({'Command':'du --time --time-style=iso -BK /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I check the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -BM /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes.', 
															'How do I view the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -BT /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes.', 
															'How do I view the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes.',
															'How do I check the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -BP /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes.', 
															'How do I view the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -BY /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes.', 
															'How do I check the last modification date and memory occupied by the folder and the sub-folders\ in /home/user/ in terms of Yottabytes?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -BZ /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I view the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -BE /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes.', 
															'How do I check last modification date and memory occupied by the folder in /home/user/ in terms of Exabytes?',
															'View the last modification date and memory occupied by the folder in /home/user/ in terms of Exabytes.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso --si /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ in powers of 1000.', 
															'How do I view the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in powers of 1000?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/ in powers of 1000.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -t10K /home/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /home/user/ by ignoring the folders having size less than 10K.', 
															'How do I view the last modification date and memory occupied by the folder and the sub-folder in /home/user/ and ignore the folders having size less than 10K?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /home/user/. Ignore the folders which have size less than 10K.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /home/user/ by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -x /media/user/','NL Queries':['Displays the last modification date and memory occupied by the folders and sub-folders in /media/user/ by ignoring the folders of different filesystem.', 
															'How do I view the last modification date and memory occupied by the folder and the sub-folder in /media/user/ and ignore the folders mounted from a different filesystem?',
															'View the last modification date and memory occupied by the folder and the sub-folder in /media/user/. Ignore the folders which are of a different filesystem.',
															'How do I show the last modification date and memory occupied by the folders and sub-folders in /media/user/ by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=iso -s /home/user/','NL Queries':['Displays the last modification date and total file size of all the files in /home/user/.', 
															'How do I view the last modification date and total file size of all the files in /home/user/?',
															'View the last modification date and total file size of all the files in /home/user/.',
															'How do I show the last modification date and total file size of all the files in /home/user/?']},ignore_index=True)

#This ends all combinations for --time --time-style=iso

du = du.append({'Command':'du --time --time-style=long-iso -h /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in Human Readable Format.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in Human Readable Format?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in Human Readable Format.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in Human Readable Format?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -BG /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes.', 
															'How do I check the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Gigabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Gigabytes?']},ignore_index=True)
																				
du = du.append({'Command':'du --time --time-style=long-iso -BK /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I check the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -BM /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Megabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Megabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -BT /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Terabytes.',
															'How do I check the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Terabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -BP /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Petabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Petabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -BY /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes.', 
															'How do I check the last modification date, time and memory occupied by the folder and the sub-folders\ in /home/user/ in terms of Yottabytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Yottabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Yottabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -BZ /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in terms of Kilobytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Kilobytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -BE /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes.', 
															'How do I check last modification date, time and memory occupied by the folder in /home/user/ in terms of Exabytes?',
															'View the last modification date, time and memory occupied by the folder in /home/user/ in terms of Exabytes.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in terms of Exabytes?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso --si /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in powers of 1000.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in powers of 1000?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ in powers of 1000.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ in powers of 1000?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -t10K /home/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ by ignoring the folders having size less than 10K.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/ and ignore the folders having size less than 10K?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /home/user/. Ignore the folders which have size less than 10K.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /home/user/ by ignoring the folders which have size less than 10K?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -x /media/user/','NL Queries':['Displays the last modification date, time and memory occupied by the folders and sub-folders in /media/user/ by ignoring the folders of different filesystem.', 
															'How do I view the last modification date, time and memory occupied by the folder and the sub-folder in /media/user/ and ignore the folders mounted from a different filesystem?',
															'View the last modification date, time and memory occupied by the folder and the sub-folder in /media/user/. Ignore the folders which are of a different filesystem.',
															'How do I show the last modification date, time and memory occupied by the folders and sub-folders in /media/user/ by ignoring the folders which are of a different filesystem?']},ignore_index=True)

du = du.append({'Command':'du --time --time-style=long-iso -s /home/user/','NL Queries':['Displays the last modification date, time and total file size of all the files in /home/user/.', 
															'How do I view the last modification date, time and total file size of all the files in /home/user/?',
															'View the last modification date, time and total file size of all the files in /home/user/.',
															'How do I show the last modification date, time and total file size of all the files in /home/user/?']},ignore_index=True)


#This ends all combinations for --time --time-style=long-iso

print (du.shape)