import pandas as pd 

'''
	-a, --all
              include pseudo, duplicate, inaccessible file systems

       -B, --block-size=SIZE
              scale sizes by SIZE before printing them; e.g., '-BM' prints sizes in units of 1,048,576 bytes; see SIZE format below

       -h, --human-readable
              print sizes in powers of 1024 (e.g., 1023M)

       -H, --si
              print sizes in powers of 1000 (e.g., 1.1G)

       -i, --inodes
              list inode information instead of block usage

       -k     like --block-size=1K

       -l, --local
              limit listing to local file systems

       --no-sync
              do not invoke sync before getting usage info (default)

       --output[=FIELD_LIST]
              use the output format defined by FIELD_LIST, or print all fields if FIELD_LIST is omitted.

       -P, --portability
              use the POSIX output format

       --sync invoke sync before getting usage info

       --total
              elide all entries insignificant to available space, and produce a grand total

       -t, --type=TYPE
              limit listing to file systems of type TYPE

       -T, --print-type
              print file system type
	
		-x, --exclude-type=TYPE
              limit listing to file systems not of type TYPE

       -v     (ignored)
       
       SIZE Units are K,M,G,T,P,E,Z,Y
       
       FIELD_LIST  is  a  comma-separated list of columns to be included.  Valid field names are: 'source', 'fstype', 'itotal', 'iused', 'iavail', 'ipcent', 'size', 'used', 'avail', 'pcent', 'file' and 'target'
'''

#Note that POSIX stands for Portable Operating System Interface and will be used only as POSIX

df = pd.DataFrame(columns = ['Command','NL Queries'])

df = df.append({'Command':'df','NL Queries':['Display file system usage.',
																				'Show the statistics of file system.',
																				'How can I display the file system usage?',
																				'How can I show the statistics of the file system?']},ignore_index=True)

df = df.append({'Command':'df -a','NL Queries':['Show statistics of all file systems. Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system, along with those of dummy file system?']},ignore_index=True)
'''																			
df = df.append({'Command':'df --all','NL Queries':['Show statistics of all file systems. Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -T','NL Queries':['Display file system type and other statistics of file system.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system.',
																				'How do I display file system type and other statistics of file system?',
																				'How do I display device name, total blocks, total disk space, available disk space,file system type and mount points of the system?']},ignore_index=True)

'''																				
df = df.append({'Command':'df --print-type','NL Queries':['Display file system type and other statistics of file system.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system.',
																				'How do I display file system type and other statistics of file system?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system?']},ignore_index=True)
'''
df = df.append({'Command':'df -h','NL Queries':['Display statistics of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format.',
																				'How do I display statistics of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df --human-readable','NL Queries':['Display statistics of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format.',
																				'How do I display statistics of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -H','NL Queries':['Display statistics of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000.',
																				'How do I display statistics of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df --si','NL Queries':['Display statistics of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000.',
																				'How do I display statistics of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BG','NL Queries':['Display statistics of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Gigabytes.',
																				'How do I display statistics of file system in Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df -BK','NL Queries':['Display statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Kilobytes.',
																				'How do I display file system type and other statistics of file system in Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -BM','NL Queries':['Display file system type and other statistics of file system in Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes.',
																				'How do I display file system type and other statistics of file system in Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -BT','NL Queries':['Display statistics of file system in Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Terabytes.',
																				'How do I display statistics of file system in Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -BP','NL Queries':['Display statistics of file system in Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Petabytes.',
																				'How do I Display statistics of file system in Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -BY','NL Queries':['Display statistics of file system in Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Yottabytes.',
																				'How do I display statistics of file system in Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -BZ','NL Queries':['Display statistics of file system in Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Zettabytes.',
																				'How do I display statistics of file system in Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df -BE','NL Queries':['Display statistics of file system in Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Exabytes.',
																				'How do I display statistics of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Exabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df --block-size=G','NL Queries':['Display statistics of file system in Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Gigabytes.',
																				'How do I display statistics of file system in Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Gigabytes?']},ignore_index=True)
#
df = df.append({'Command':'df --block-size=E','NL Queries':['Display statistics of file system in Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Exabytes.',
																				'How do I display statistics of file system in Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Exabytes?']},ignore_index=True)
#
df = df.append({'Command':'df --block-size=K','NL Queries':['Display statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes.',
																				'How do I Display statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)
#
df = df.append({'Command':'df --block-size=M','NL Queries':['Display statistics of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes.',
																				'How do I Display statistics of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes?']},ignore_index=True)
#
df = df.append({'Command':'df --block-size=T','NL Queries':['Display statistics of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes.',
																				'How do I Display statistics of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes?']},ignore_index=True)
#
df = df.append({'Command':'df --block-size=P','NL Queries':['Display statistics of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes.',
																				'How do I Display statistics of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes?']},ignore_index=True)
#
df = df.append({'Command':'df --block-size=Y','NL Queries':['Display fstatistics of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes.',
																				'How do I Display statistics of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes?']},ignore_index=True)
#
df = df.append({'Command':'df --block-size=Z','NL Queries':['Display statistics of file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zettabytes.',
																				'How do I Display statistics of file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zettabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'ext4\'','NL Queries':['Display statistics of file system of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of file system type ext4.',
																				'How do I Display statistics of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of filesystem type ext4?']},ignore_index=True)
'''
df = df.append({'Command':'df --type=\'filesystemtype\'','NL Queries':['Display statistics of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype.',
																				'How do I Display statistics of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -P','NL Queries':['Display statistics of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX Format.',
																				'How do I display statistics of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df --portability','NL Queries':['Display statistics of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX Format.',
																				'How do I Display statistics of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -i','NL Queries':['Display statistics of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes.',
																				'How do I display statistics of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df --inodes','NL Queries':['Display statistics of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in terms of inodes.',
																				'How do I display statistics of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in terms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext4\'','NL Queries':['Display statistics of all file systems except ext4.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all file systems except of type ext4.',
																				'How do I display statistics of file system not of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all file system and not of type ext4?']},ignore_index=True)
'''
df = df.append({'Command':'df --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype.',
																				'How do I display statistics of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -k','NL Queries':['Display statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes.',
																				'How do I display file system type and other statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df --total','NL Queries':['Display statistics of file system along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system along with the total disk usage.',
																				'How do I display file system type and other statistics of file system along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system along with the total disk usage?']},ignore_index=True)

#This ends all Vanilla Combinations
'''
df = df.append({'Command':'df -v','NL Queries':['Display file system usage.',
																				'Show the usage statistics of file system.',
																				'How can I display the file system usage?',
																				'How can I see the statistics of the file system?']},ignore_index=True)

df = df.append({'Command':'df -v -a','NL Queries':['Show statistics of all file systems, along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of all file systems, along with those of dummy file system.',
																				'How can I see the statistics of all file systems and of the dummy ones also?',
																				'How can I see device name,total blocks, total disk space,available disk space and mount points of the file systems, along with those of dummy file system?']},ignore_index=True)
#																		
df = df.append({'Command':'df -v --all','NL Queries':['Show statistics of all file systems. Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df -v -T','NL Queries':['Display file system type and other statistics of file system.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system.',
																				'How do I display file system type and other statistics of file system?',
																				'How do I display device name, total blocks, total disk space, available disk space, filesystem type and mount points of the file system?']},ignore_index=True)
#																				
df = df.append({'Command':'df -v --print-type','NL Queries':['Display file system type and other statistics of file system.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system.',
																				'How do I Display file system type and other statistics of file system?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system?']},ignore_index=True)

df = df.append({'Command':'df -v -h','NL Queries':['Display statistics of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format.',
																				'How do I display statistics of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df -v --human-readable','NL Queries':['Display statistics of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format.',
																				'How do I display statistics of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df -v -H','NL Queries':['Display statistics of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000.',
																				'How do I display statistics of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df -v --si','NL Queries':['Display statistics of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000.',
																				'How do I Display statistics of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000?']},ignore_index=True)
																				
df = df.append({'Command':'df -v -BG','NL Queries':['Display statistics of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes.',
																				'How do I Display statistics of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df -v -BK','NL Queries':['Display statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -v -BM','NL Queries':['Display file system type and other statistics of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -v -BT','NL Queries':['Display statistics of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes.',
																				'How do I Display statistics of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -v -BP','NL Queries':['Display statistics of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes.',
																				'How do I Display statistics of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -v -BY','NL Queries':['Display statistics of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes.',
																				'How do I display statistics of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -v -BZ','NL Queries':['Display statistics of file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zettabytes.',
																				'How do I display statistics of file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df -v -BE','NL Queries':['Display statistics of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes.',
																				'How do I display statistics of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -v --block-size=G','NL Queries':['Display statistics of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes.',
																				'How do I display statistics of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df -v --block-size=E','NL Queries':['Display statistics of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes.',
																				'How do I display statistics of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -v --block-size=K','NL Queries':['Display statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes.',
																				'How do I Display statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -v --block-size=M','NL Queries':['Display statistics of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes.',
																				'How do I Display statistics of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -v --block-size=T','NL Queries':['Display statistics of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes.',
																				'How do I Display statistics of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -v --block-size=P','NL Queries':['Display statistics of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes.',
																				'How do I Display statistics of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -v --block-size=Y','NL Queries':['Display fstatistics of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes.',
																				'How do I Display statistics of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -v --block-size=Z','NL Queries':['Display statistics of file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zettabytes.',
																				'How do I Display statistics of file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df -v -t\'filesystemtype\'','NL Queries':['Display statistics of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype.',
																				'How do I Display statistics of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -v --type=\'filesystemtype\'','NL Queries':['Display statistics of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype.',
																				'How do I Display statistics of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -v -P','NL Queries':['Display statistics of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX Format.',
																				'How do I Display statistics of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df -v --portability','NL Queries':['Display statistics of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX Format.',
																				'How do I Display statistics of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df -v -i','NL Queries':['Display statistics of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system interms of inodes.',
																				'How do I Display statistics of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df -v --inodes','NL Queries':['Display statistics of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system interms of inodes.',
																				'How do I Display statistics of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df -v -x\'filesystemtype\'','NL Queries':['Display statistics of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype.',
																				'How do I Display statistics of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -v --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype.',
																				'How do I Display statistics of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -v -k','NL Queries':['Display statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -v --total','NL Queries':['Display statistics of file system along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system along with the total disk usage?']},ignore_index=True)
'''
#This ends all combinations for -v

df = df.append({'Command':'df -a -T','NL Queries':['Display all file systems type and other statistics of all  file systems including the dummy ones.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of all the file systems along with the dummy ones.',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones.?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -a --print-type','NL Queries':['Display all file systems type and other statistics of all  file systems including the dummy ones.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of all the file systems including the dummy ones..',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones and dummy file systems?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones.?']},ignore_index=True)
'''
df = df.append({'Command':'df -a -h','NL Queries':['Display statistics of all  file systems including the dummy ones in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in Human Readable Format.',
																				'How do I display statistics of all  file systems and dummy file systems in Human Readable Format ?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -a --human-readable','NL Queries':['Display statistics of all  file systems including the dummy ones in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in Human Readable Format.',
																				'How do I display statistics of all  file systems including the dummy ones and dummy file systems in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -a -H','NL Queries':['Display statistics of all file systems including the dummy ones in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in powers of 1000.',
																				'How do I display statistics of all  file systems along with the dummy ones in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems with the dummy ones in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -a --si','NL Queries':['Display statistics of all  file systems including the dummy ones in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in powers of 1000.',
																				'How do I Display statistics of all  file systems including the dummy ones in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in powers of 1000?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -a -BG','NL Queries':['Display statistics of all  file systems including the dummy ones in Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones Gigabytes.',
																				'How do I display statistics of all  file systems along with the dummy ones in Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems with the dummy ones in Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df -a -BK','NL Queries':['Display statistics of all  file systems including the dummy ones Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems along with the dummy ones in Kilobytes.',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones in Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems with the dummy ones in Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -a -BM','NL Queries':['Display all file systems type and other statistics of all  file systems including the dummy ones in Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems along with the dummy ones in Megabytes.',
																				'How do I Display all file systems type and other statistics of all  file systems with the dummy ones in Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems with the dummy ones in Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -a -BT','NL Queries':['Display statistics of all  file systems including the dummy ones in Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems along with the dummy ones in Terabytes.',
																				'How do I Display statistics of all  file systems with the dummy ones in Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems along with the dummy ones in Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -a -BP','NL Queries':['Display statistics of all  file systems including the dummy ones in Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems with the dummy ones in Petabytes.',
																				'How do I Display statistics of all  file systems along with the dummy ones in Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -a -BY','NL Queries':['Display statistics of all  file systems including the dummy ones in Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems and the dummy ones in Yottabytes.',
																				'How do I display statistics of all  file systems including the dummy ones in Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems along with the dummy ones in Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -a -BZ','NL Queries':['Display statistics of all  file systems including the dummy ones in Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in Zettabytes.',
																				'How do I display statistics of all  file systems along with the dummy ones in Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems and the dummy ones in Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df -a -BE','NL Queries':['Display statistics of all  file systems including the dummy ones in Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in Exabytes.',
																				'How do I display statistics of all  file systems along with the dummy ones in Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems withs the dummy ones in Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -a --block-size=G','NL Queries':['Display statistics of all  file systems including the dummy ones in Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems and the dummy ones in terms o Gigabytes.',
																				'How do I display statistics of all  file systems including the dummy ones in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Gigabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -a --block-size=E','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Exabytes.',
																				'How do I display statistics of all  file systems including the dummy ones in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -a --block-size=K','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -a --block-size=M','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Megabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -a --block-size=T','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Terabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -a --block-size=P','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Petabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -a --block-size=Y','NL Queries':['Display fstatistics of all  file systems including the dummy ones in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Yottabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -a --block-size=Z','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Zettabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Zettabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -a -t\'ext4\'','NL Queries':['Display statistics of all  file systems including the dummy ones of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones of type ext4.',
																				'How do I display statistics of all  file systems along with the dummy ones of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems with the dummy ones of type ext4?']},ignore_index=True)
'''
df = df.append({'Command':'df -a --type=\'filesystemtype\'','NL Queries':['Display statistics of all  file systems including the dummy ones of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones. of type filesystemtype.',
																				'How do I Display statistics of all  file systems including the dummy ones of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones. of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -a -P','NL Queries':['Display statistics of all  file systems including the dummy ones in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems and the dummy ones in POSIX Format.',
																				'How do I display statistics of all  file systems along with the dummy ones in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems with the dummy ones in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -a --portability','NL Queries':['Display statistics of all  file systems including the dummy ones in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in POSIX Format.',
																				'How do I Display statistics of all  file systems including the dummy ones in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -a -i','NL Queries':['Display statistics of all file systems including the dummy ones in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems with the dummy ones in terms of inodes.',
																				'How do I display statistics of all  file systems along with the dummy ones in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems and the dummy ones in terms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -a --inodes','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones interms of inodes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -a -x\'ext4\'','NL Queries':['Display statistics of all file systems including the dummy ones and not of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones, but not of type ext4.',
																				'How do I display statistics of all  file systems with the dummy ones also and without type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems with the dummy ones but not type ext4?']},ignore_index=True)
'''
df = df.append({'Command':'df -a --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of all  file systems including the dummy ones not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones. not of type filesystemtype.',
																				'How do I Display statistics of all  file systems including the dummy ones not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones. not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -a -k','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes.',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -a --total','NL Queries':['Display statistics of all file systems including the dummy ones along with their total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems and the dummy ones along with their total disk usage.',
																				'How do I display all file systems type and other statistics of all file systems with the dummy ones and their total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems with the dummy ones and their total disk usage?']},ignore_index=True)
# This ends all possible working combinations of -a
'''
df = df.append({'Command':'df --all -T','NL Queries':['Display all file systems type and other statistics of all  file systems including the dummy ones includes the dummy file systems also.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of all the file systems including the dummy ones. and dummy file systems.',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones and dummy file systems?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones.?']},ignore_index=True)
																				
df = df.append({'Command':'df --all --print-type','NL Queries':['Display all file systems type and other statistics of all file systems including the dummy ones.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of all the file systems including the dummy ones..',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones and dummy file systems?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones.?']},ignore_index=True)

df = df.append({'Command':'df --all -h','NL Queries':['Display statistics of all  file systems including the dummy ones in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in Human Readable Format.',
																				'How do I display statistics of all  file systems including the dummy ones and dummy file systems in Human Readable Format ?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --all --human-readable','NL Queries':['Display statistics of all  file systems including the dummy ones in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in Human Readable Format.',
																				'How do I display statistics of all  file systems including the dummy ones and dummy file systems in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --all -H','NL Queries':['Display statistics of all  file systems including the dummy ones in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in powers of 1000.',
																				'How do I display statistics of all  file systems including the dummy ones in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --all --si','NL Queries':['Display statistics of all  file systems including the dummy ones in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in powers of 1000.',
																				'How do I Display statistics of all  file systems including the dummy ones in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in powers of 1000?']},ignore_index=True)
																				
df = df.append({'Command':'df --all -BG','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Gigabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --all -BK','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes.',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --all -BM','NL Queries':['Display all file systems type and other statistics of all  file systems including the dummy ones in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Megabytes.',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --all -BT','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Terabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --all -BP','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Petabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --all -BY','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Yottabytes.',
																				'How do I display statistics of all  file systems including the dummy ones in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --all -BZ','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Zettabytes.',
																				'How do I display statistics of all  file systems including the dummy ones in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --all -BE','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Exabytes.',
																				'How do I display statistics of all  file systems including the dummy ones in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --all --block-size=G','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Gigabytes.',
																				'How do I display statistics of all  file systems including the dummy ones in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df --all --block-size=E','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Exabytes.',
																				'How do I display statistics of all  file systems including the dummy ones in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --all --block-size=K','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --all --block-size=M','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Megabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --all --block-size=T','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Terabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --all --block-size=P','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Petabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --all --block-size=Y','NL Queries':['Display fstatistics of all  file systems including the dummy ones in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Yottabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --all --block-size=Z','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Zettabytes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --all -t\'filesystemtype\'','NL Queries':['Display statistics of all  file systems including the dummy ones of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones. of type filesystemtype.',
																				'How do I Display statistics of all  file systems including the dummy ones of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones. of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --all --type=\'filesystemtype\'','NL Queries':['Display statistics of all  file systems including the dummy ones of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones. of type filesystemtype.',
																				'How do I Display statistics of all  file systems including the dummy ones of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones. of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --all -P','NL Queries':['Display statistics of all  file systems including the dummy ones in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in POSIX Format.',
																				'How do I Display statistics of all  file systems including the dummy ones in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --all --portability','NL Queries':['Display statistics of all  file systems including the dummy ones in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in POSIX Format.',
																				'How do I Display statistics of all  file systems including the dummy ones in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --all -i','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones interms of inodes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --all --inodes','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones interms of inodes.',
																				'How do I Display statistics of all  file systems including the dummy ones in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --all -x\'filesystemtype\'','NL Queries':['Display statistics of all  file systems including the dummy ones not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones. not of type filesystemtype.',
																				'How do I Display statistics of all  file systems including the dummy ones not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones. not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --all --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of all  file systems including the dummy ones not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones. not of type filesystemtype.',
																				'How do I Display statistics of all  file systems including the dummy ones not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones. not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --all -k','NL Queries':['Display statistics of all  file systems including the dummy ones in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes.',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --all --total','NL Queries':['Display statistics of all  file systems including the dummy ones along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of all the file systems including the dummy ones. along with the total disk usage.',
																				'How do I Display all file systems type and other statistics of all  file systems including the dummy ones along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of all the file systems including the dummy ones. along with the total disk usage?']},ignore_index=True)
'''
# This ends all possible working combinations of --all

df = df.append({'Command':'df -BG -a','NL Queries':['Show statistics of all file systems in terms of Gigabytes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Gigabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Gigabytes, along with those of dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BG --all','NL Queries':['Show statistics of all file systems in terms of Gigabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Gigabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Gigabytes, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG -T','NL Queries':['Display file system type and other statistics of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Gigabytes.',
																				'How do I display file system type and other statistics of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space,file system type and mount points of the system in terms of Gigabytes?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BG --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Gigabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG -h','NL Queries':['Display statistics of file system in terms of Gigabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Gigabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG --human-readable','NL Queries':['Display statistics of file system in terms of Gigabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Gigabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG -H','NL Queries':['Display statistics of file system in terms of Gigabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the  file system in terms of Gigabytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Gigabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG --si','NL Queries':['Display statistics of file system in terms of Gigabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Gigabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG -t\'ext4\'','NL Queries':['Display statistics of file system  of type ext4 in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of type ext4file system in terms of Gigabytes.',
																				'How do I display statistics of file system, in terms of Gigabytes, of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system ext4 in terms of Gigabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Gigabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Gigabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG -P','NL Queries':['Display statistics of file system in terms of Gigabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes and in  POSIX Format.',
																				'How do I display statistics of file system in Gigabytes and in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX Format with Gigabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG --portability','NL Queries':['Display statistics of file system in terms of Gigabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Gigabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG -x\'ext4\'','NL Queries':['Display statistics of file system in Gigabytes except of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the all file systems except ext4 in Gigabytes.',
																				'How do I display statistics of file system in Gigabytes? Do not include type ext4.',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Gigabytes without including type ext4?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Gigabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Gigabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BG --total','NL Queries':['Display statistics of file system in terms of Gigabytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in terms of Gigabytes along with the total disk usage.',
																				'How do I display file system type and other statistics of file system in terms of Gigabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in terms of Gigabytes along with the total disk usage?']},ignore_index=True)
#This ends all possible working combinations of -BG
'''
df = df.append({'Command':'df --block-size=G -a','NL Queries':['Show statistics of all file systems in terms of Gigabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Gigabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Gigabytes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=G --all','NL Queries':['Show statistics of all file systems in terms of Gigabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Gigabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Gigabytes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G -T','NL Queries':['Display file system type and other statistics of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Gigabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=G --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Gigabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G -h','NL Queries':['Display statistics of file system in terms of Gigabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Gigabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G --human-readable','NL Queries':['Display statistics of file system in terms of Gigabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Gigabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G -H','NL Queries':['Display statistics of file system in terms of Gigabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Gigabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G --si','NL Queries':['Display statistics of file system in terms of Gigabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Gigabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Gigabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Gigabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Gigabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Gigabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G -P','NL Queries':['Display statistics of file system in terms of Gigabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Gigabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G --portability','NL Queries':['Display statistics of file system in terms of Gigabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Gigabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Gigabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Gigabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Gigabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Gigabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=G --total','NL Queries':['Display statistics of file system in terms of Gigabytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Gigabytes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of Gigabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Gigabytes along with the total disk usage?']},ignore_index=True)
'''
# This ends all possible working combinations of --block-size=G

df = df.append({'Command':'df -BY -a','NL Queries':['Show statistics of all file systems in Yottabytes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system with dummy ones in Yottabytes.',
																				'How can I see the statistics of all file systems and the dummy ones in terms of Yottabytes?',
																				'How can I view device name,total blocks, total disk space,available disk space and mount points of the file system in Yottabytes, including the dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BY --all','NL Queries':['Show statistics of all file systems in terms of Yottabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Yottabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Yottabytes, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY -T','NL Queries':['Display file system type and other statistics of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system in Yottabytes.',
																				'How do I display file system type and other statistics of file system with Yottabytes as the unit?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Yottabytes?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BY --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Yottabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes?']},ignore_index=True)
'''

df = df.append({'Command':'df -BY -h','NL Queries':['Display statistics of file system in terms of Yottabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Yottabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY --human-readable','NL Queries':['Display statistics of file system in terms of Yottabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Yottabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY -H','NL Queries':['Display statistics of file system in terms of Yottabytes and in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 and unit as Yottabytes.',
																				'How do I display statistics of file system in terms of Yottabytes and in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in terms of Yottabytes and in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY --si','NL Queries':['Display statistics of file system in terms of Yottabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Yottabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY -t\'ext4\'','NL Queries':['Display statistics of file system in terms of Yottabytes of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in terms of Yottabytes of type ext4.',
																				'How do I display statistics of file system in terms of Yottabytes of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes of type ext4?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Yottabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Yottabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY -P','NL Queries':['Display statistics of file system in Yottabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in POSIX Format.',
																				'How do I display statistics of file system in POSIX Format with Yottabytes as unit?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY --portability','NL Queries':['Display statistics of file system in terms of Yottabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Yottabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY -x\'ext3\'','NL Queries':['Display statistics of file system in terms of Yottabytes but not of type ext3.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Yottabytes except for ext3.',
																				'How do I display statistics of file system ,apart from ext3, in Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Yottabytes, excluding type ext3?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Yottabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Yottabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BY --total','NL Queries':['Display statistics of file system in terms of Yottabytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes along with the total disk usage.',
																				'How do I display file system type and other statistics of file system in terms of Yottabytes with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space, mount points  and the total disk usage of the file system in terms of Yottabytes?']},ignore_index=True)

# This ends all combinations for -BY
'''
df = df.append({'Command':'df --block-size=Y -a','NL Queries':['Show statistics of all file systems in terms of Yottabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Yottabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Yottabytes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=Y --all','NL Queries':['Show statistics of all file systems in terms of Yottabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Yottabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Yottabytes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y -T','NL Queries':['Display file system type and other statistics of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Yottabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=Y --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Yottabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y -h','NL Queries':['Display statistics of file system in terms of Yottabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Yottabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y --human-readable','NL Queries':['Display statistics of file system in terms of Yottabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Yottabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y -H','NL Queries':['Display statistics of file system in terms of Yottabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Yottabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y --si','NL Queries':['Display statistics of file system in terms of Yottabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Yottabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Yottabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Yottabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Yottabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Yottabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y -P','NL Queries':['Display statistics of file system in terms of Yottabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Yottabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y --portability','NL Queries':['Display statistics of file system in terms of Yottabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Yottabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Yottabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Yottabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Yottabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Yottabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Y --total','NL Queries':['Display statistics of file system in terms of Yottabytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Yottabytes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of Yottabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Yottabytes along with the total disk usage?']},ignore_index=True)
'''
# This ends all combinations for --block-size=Y

df = df.append({'Command':'df -BK -a','NL Queries':['Show statistics of all file systems in terms of Kilobytes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems and dummy ones also in Kilobytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Kilobytes, including those of dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BK --all','NL Queries':['Show statistics of all file systems in terms of Kilobytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Kilobytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK -T','NL Queries':['Display file system type and other statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system in terms of Kilobytes.',
																				'How do I display file system type and other statistics of file system with Kilobytes as units?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Kilobytes?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BK --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK -h','NL Queries':['Display statistics of file system in terms of Kilobytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Kilobytes and in Human Readable Format.',
																				'How do I display statistics of file system in Kilobytes and in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format and Kilobytes as unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK --human-readable','NL Queries':['Display statistics of file system in terms of Kilobytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Kilobytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK -H','NL Queries':['Display statistics of file system in terms of Kilobytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 and Kilobytes as unit.',
																				'How do I display statistics of file system in Kilobytes with values in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in powers of 1000 and Kilobytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK --si','NL Queries':['Display statistics of file system in terms of Kilobytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Kilobytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK -t\'NTFS\'','NL Queries':['Display statistics of file system of type NTFS in Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system of type NTFS in terms of Kilobytes .',
																				'How do I display statistics of file system type NTFS in Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of NTFS system in Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK -P','NL Queries':['Display statistics of file system in terms of Kilobytes and POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in POSIX Format with Kilobytes as unit.',
																				'How do I display statistics of file system in terms of Kilobytes and in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in POSIX Format and Kilobytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK --portability','NL Queries':['Display statistics of file system in terms of Kilobytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Kilobytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK -x\'ext3\'','NL Queries':['Display statistics of file system in terms of Kilobytes but not of type ext3.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system except of type ext3 in Kilobytes.',
																				'How do I display statistics of file system in terms of Kilobytes not of type ext3?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes not of type ext3?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BK --total','NL Queries':['Display statistics of file system in terms of Kilobytes along with their total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space,total disk usage and mount points of the file system in Kilobytes.',
																				'How do I display file system type and other statistics of file system in terms of Kilobytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Kilobytes along with their total disk usage?']},ignore_index=True)

# This ends all working combinations of -BK
'''
df = df.append({'Command':'df --block-size=K -a','NL Queries':['Show statistics of all file systems in terms of Kilobytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Kilobytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=K --all','NL Queries':['Show statistics of all file systems in terms of Kilobytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Kilobytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K -T','NL Queries':['Display file system type and other statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=K --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K -h','NL Queries':['Display statistics of file system in terms of Kilobytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Kilobytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K --human-readable','NL Queries':['Display statistics of file system in terms of Kilobytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Kilobytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K -H','NL Queries':['Display statistics of file system in terms of Kilobytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Kilobytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K --si','NL Queries':['Display statistics of file system in terms of Kilobytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Kilobytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K -P','NL Queries':['Display statistics of file system in terms of Kilobytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Kilobytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K --portability','NL Queries':['Display statistics of file system in terms of Kilobytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Kilobytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=K --total','NL Queries':['Display statistics of file system in terms of Kilobytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of Kilobytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes along with the total disk usage?']},ignore_index=True)
'''
# This ends all working combinations of --block-size=K
df = df.append({'Command':'df -BM -a','NL Queries':['Show statistics of all file systems in terms of Megabytes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems and dummy ones also in Megabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Megabytes, including those of dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BM --all','NL Queries':['Show statistics of all file systems in terms of Megabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Megabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Megabytes, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM -T','NL Queries':['Display file system type and other statistics of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system in terms of Megabytes.',
																				'How do I display file system type and other statistics of file system with Megabytes as units?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Megabytes?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BM --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Megabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM -h','NL Queries':['Display statistics of file system in terms of Megabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Megabytes and in Human Readable Format.',
																				'How do I display statistics of file system in Megabytes and in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format and Megabytes as unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM --human-readable','NL Queries':['Display statistics of file system in terms of Megabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Megabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM -H','NL Queries':['Display statistics of file system in terms of Megabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 and Megabytes as unit.',
																				'How do I display statistics of file system in Megabytes with values in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in powers of 1000 and Megabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM --si','NL Queries':['Display statistics of file system in terms of Megabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Megabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM -t\'NTFS\'','NL Queries':['Display statistics of file system of type NTFS in Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system of type NTFS in terms of Megabytes .',
																				'How do I display statistics of file system type NTFS in Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of NTFS system in Megabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Megabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Megabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM -P','NL Queries':['Display statistics of file system in terms of Megabytes and POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in POSIX Format with Megabytes as unit.',
																				'How do I display statistics of file system in terms of Megabytes and in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in POSIX Format and Megabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM --portability','NL Queries':['Display statistics of file system in terms of Megabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Megabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM -x\'ext3\'','NL Queries':['Display statistics of file system in terms of Megabytes but not of type ext3.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system except of type ext3 in Megabytes.',
																				'How do I display statistics of file system in terms of Megabytes not of type ext3?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes not of type ext3?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Megabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Megabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BM --total','NL Queries':['Display statistics of file system in terms of Megabytes along with their total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space,total disk usage and mount points of the file system in Megabytes.',
																				'How do I display file system type and other statistics of file system in terms of Megabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Megabytes along with their total disk usage?']},ignore_index=True)


# This ends all combinations for -BM
'''
df = df.append({'Command':'df --block-size=M -a','NL Queries':['Show statistics of all file systems in terms of Megabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Megabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Megabytes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=M --all','NL Queries':['Show statistics of all file systems in terms of Megabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Megabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Megabytes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M -T','NL Queries':['Display file system type and other statistics of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Megabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=M --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Megabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M -h','NL Queries':['Display statistics of file system in terms of Megabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Megabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M --human-readable','NL Queries':['Display statistics of file system in terms of Megabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Megabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M -H','NL Queries':['Display statistics of file system in terms of Megabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Megabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M --si','NL Queries':['Display statistics of file system in terms of Megabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Megabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Megabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Megabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Megabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Megabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M -P','NL Queries':['Display statistics of file system in terms of Megabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Megabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M --portability','NL Queries':['Display statistics of file system in terms of Megabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Megabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Megabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Megabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=M --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Megabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Megabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes not of type filesystemtype?']},ignore_index=True)


df = df.append({'Command':'df --block-size=M --total','NL Queries':['Display statistics of file system in terms of Megabytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Megabytes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of Megabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Megabytes along with the total disk usage?']},ignore_index=True)
'''
# This ends all combinations for --block-size=M

df = df.append({'Command':'df -BT -a','NL Queries':['Show statistics of all file systems in terms of Terabytes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems and dummy ones also in Terabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Terabytes, including those of dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BT --all','NL Queries':['Show statistics of all file systems in terms of Terabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Terabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Terabytes, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT -T','NL Queries':['Display file system type and other statistics of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system in terms of Terabytes.',
																				'How do I display file system type and other statistics of file system with Terabytes as units?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Terabytes?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BT --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Terabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT -h','NL Queries':['Display statistics of file system in terms of Terabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Terabytes and in Human Readable Format.',
																				'How do I display statistics of file system in Terabytes and in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format and Terabytes as unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT --human-readable','NL Queries':['Display statistics of file system in terms of Terabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Terabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT -H','NL Queries':['Display statistics of file system in terms of Terabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 and Terabytes as unit.',
																				'How do I display statistics of file system in Terabytes with values in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in powers of 1000 and Terabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT --si','NL Queries':['Display statistics of file system in terms of Terabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Terabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT -t\'NTFS\'','NL Queries':['Display statistics of file system of type NTFS in Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system of type NTFS in terms of Terabytes .',
																				'How do I display statistics of file system type NTFS in Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of NTFS system in Terabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Terabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Terabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT -P','NL Queries':['Display statistics of file system in terms of Terabytes and POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in POSIX Format with Terabytes as unit.',
																				'How do I display statistics of file system in terms of Terabytes and in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in POSIX Format and Terabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT --portability','NL Queries':['Display statistics of file system in terms of Terabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Terabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT -x\'ext3\'','NL Queries':['Display statistics of file system in terms of Terabytes but not of type ext3.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system except of type ext3 in Terabytes.',
																				'How do I display statistics of file system in terms of Terabytes not of type ext3?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes not of type ext3?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Terabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Terabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BT --total','NL Queries':['Display statistics of file system in terms of Terabytes along with their total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space,total disk usage and mount points of the file system in Terabytes.',
																				'How do I display file system type and other statistics of file system in terms of Terabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Terabytes along with their total disk usage?']},ignore_index=True)


#This ends all combinations for -BT
'''																				
df = df.append({'Command':'df --block-size=T -a','NL Queries':['Show statistics of all file systems in terms of Terabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Terabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Terabytes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=T --all','NL Queries':['Show statistics of all file systems in terms of Terabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Terabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Terabytes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T -T','NL Queries':['Display file system type and other statistics of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Terabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=T --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Terabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T -h','NL Queries':['Display statistics of file system in terms of Terabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Terabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T --human-readable','NL Queries':['Display statistics of file system in terms of Terabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Terabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T -H','NL Queries':['Display statistics of file system in terms of Terabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Terabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T --si','NL Queries':['Display statistics of file system in terms of Terabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Terabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Terabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Terabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Terabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Terabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T -P','NL Queries':['Display statistics of file system in terms of Terabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Terabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T --portability','NL Queries':['Display statistics of file system in terms of Terabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Terabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Terabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Terabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=T --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Terabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Terabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes not of type filesystemtype?']},ignore_index=True)


df = df.append({'Command':'df --block-size=T --total','NL Queries':['Display statistics of file system in terms of Terabytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Terabytes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of Terabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Terabytes along with the total disk usage?']},ignore_index=True)
'''
#This ends all working combinations of --block-size=T

df = df.append({'Command':'df -BP -a','NL Queries':['Show statistics of all file systems in terms of Petabytes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems and dummy ones also in Petabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Petabytes, including those of dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BP --all','NL Queries':['Show statistics of all file systems in terms of Petabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Petabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Petabytes, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP -T','NL Queries':['Display file system type and other statistics of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system in terms of Petabytes.',
																				'How do I display file system type and other statistics of file system with Petabytes as units?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Petabytes?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BP --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Petabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP -h','NL Queries':['Display statistics of file system in terms of Petabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Petabytes and in Human Readable Format.',
																				'How do I display statistics of file system in Petabytes and in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format and Petabytes as unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP --human-readable','NL Queries':['Display statistics of file system in terms of Petabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Petabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP -H','NL Queries':['Display statistics of file system in terms of Petabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 and Petabytes as unit.',
																				'How do I display statistics of file system in Petabytes with values in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in powers of 1000 and Petabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP --si','NL Queries':['Display statistics of file system in terms of Petabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Petabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP -t\'NTFS\'','NL Queries':['Display statistics of file system of type NTFS in Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system of type NTFS in terms of Petabytes .',
																				'How do I display statistics of file system type NTFS in Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of NTFS system in Petabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Petabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Petabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP -P','NL Queries':['Display statistics of file system in terms of Petabytes and POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in POSIX Format with Petabytes as unit.',
																				'How do I display statistics of file system in terms of Petabytes and in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in POSIX Format and Petabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP --portability','NL Queries':['Display statistics of file system in terms of Petabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Petabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP -x\'ext3\'','NL Queries':['Display statistics of file system in terms of Petabytes but not of type ext3.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system except of type ext3 in Petabytes.',
																				'How do I display statistics of file system in terms of Petabytes not of type ext3?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes not of type ext3?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Petabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Petabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BP --total','NL Queries':['Display statistics of file system in terms of Petabytes along with their total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space,total disk usage and mount points of the file system in Petabytes.',
																				'How do I display file system type and other statistics of file system in terms of Petabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Petabytes along with their total disk usage?']},ignore_index=True)


# This ends all working combinations for -BP
'''
df = df.append({'Command':'df --block-size=P -a','NL Queries':['Show statistics of all file systems in terms of Petabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Petabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Petabytes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=P --all','NL Queries':['Show statistics of all file systems in terms of Petabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Petabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Petabytes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P -T','NL Queries':['Display file system type and other statistics of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Petabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=P --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Petabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P -h','NL Queries':['Display statistics of file system in terms of Petabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Petabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P --human-readable','NL Queries':['Display statistics of file system in terms of Petabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Petabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P -H','NL Queries':['Display statistics of file system in terms of Petabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Petabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P --si','NL Queries':['Display statistics of file system in terms of Petabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Petabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Petabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Petabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Petabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Petabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P -P','NL Queries':['Display statistics of file system in terms of Petabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Petabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P --portability','NL Queries':['Display statistics of file system in terms of Petabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Petabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Petabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Petabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=P --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Petabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Petabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes not of type filesystemtype?']},ignore_index=True)


df = df.append({'Command':'df --block-size=P --total','NL Queries':['Display statistics of file system in terms of Petabytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Petabytes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of Petabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Petabytes along with the total disk usage?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE -a','NL Queries':['Show statistics of all file systems in terms of Exabytes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems and dummy ones also in Exabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Exabytes, including those of dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BE --all','NL Queries':['Show statistics of all file systems in terms of Exabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Exabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Exabytes, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE -T','NL Queries':['Display file system type and other statistics of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system in terms of Exabytes.',
																				'How do I display file system type and other statistics of file system with Exabytes as units?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Exabytes?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BE --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Exabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE -h','NL Queries':['Display statistics of file system in terms of Exabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Exabytes and in Human Readable Format.',
																				'How do I display statistics of file system in Exabytes and in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format and Exabytes as unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE --human-readable','NL Queries':['Display statistics of file system in terms of Exabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Exabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE -H','NL Queries':['Display statistics of file system in terms of Exabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 and Exabytes as unit.',
																				'How do I display statistics of file system in Exabytes with values in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in powers of 1000 and Exabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE --si','NL Queries':['Display statistics of file system in terms of Exabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Exabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE -t\'NTFS\'','NL Queries':['Display statistics of file system of type NTFS in Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system of type NTFS in terms of Exabytes .',
																				'How do I display statistics of file system type NTFS in Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of NTFS system in Exabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Exabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Exabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE -P','NL Queries':['Display statistics of file system in terms of Exabytes and POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in POSIX Format with Exabytes as unit.',
																				'How do I display statistics of file system in terms of Exabytes and in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in POSIX Format and Exabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE --portability','NL Queries':['Display statistics of file system in terms of Exabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Exabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE -x\'ext3\'','NL Queries':['Display statistics of file system in terms of Exabytes but not of type ext3.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system except of type ext3 in Exabytes.',
																				'How do I display statistics of file system in terms of Exabytes not of type ext3?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes not of type ext3?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Exabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Exabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BE --total','NL Queries':['Display statistics of file system in terms of Exabytes along with their total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space,total disk usage and mount points of the file system in Exabytes.',
																				'How do I display file system type and other statistics of file system in terms of Exabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Exabytes along with their total disk usage?']},ignore_index=True)


'''
df = df.append({'Command':'df --block-size=E -a','NL Queries':['Show statistics of all file systems in terms of Exabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Exabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Exabytes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=E --all','NL Queries':['Show statistics of all file systems in terms of Exabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Exabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Exabytes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E -T','NL Queries':['Display file system type and other statistics of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Exabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=E --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Exabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E -h','NL Queries':['Display statistics of file system in terms of Exabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Exabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E --human-readable','NL Queries':['Display statistics of file system in terms of Exabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Exabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E -H','NL Queries':['Display statistics of file system in terms of Exabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Exabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E --si','NL Queries':['Display statistics of file system in terms of Exabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Exabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Exabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Exabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Exabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Exabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E -P','NL Queries':['Display statistics of file system in terms of Exabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Exabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E --portability','NL Queries':['Display statistics of file system in terms of Exabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Exabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Exabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Exabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=E --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Exabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Exabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes not of type filesystemtype?']},ignore_index=True)


df = df.append({'Command':'df --block-size=E --total','NL Queries':['Display statistics of file system in terms of Exabytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Exabytes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of Exabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Exabytes along with the total disk usage?']},ignore_index=True)
'''
# This ends all combinations for --block-size=E

df = df.append({'Command':'df -BZ -a','NL Queries':['Show statistics of all file systems in terms of Zetabytes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems and dummy ones also in Zetabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Zetabytes, including those of dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BZ --all','NL Queries':['Show statistics of all file systems in terms of Zetabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Zetabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Zetabytes, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ -T','NL Queries':['Display file system type and other statistics of file system in terms of Zetabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system in terms of Zetabytes.',
																				'How do I display file system type and other statistics of file system with Zetabytes as units?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Zetabytes?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -BZ --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Zetabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Zetabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Zetabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ -h','NL Queries':['Display statistics of file system in terms of Zetabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Zetabytes and in Human Readable Format.',
																				'How do I display statistics of file system in Zetabytes and in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format and Zetabytes as unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ --human-readable','NL Queries':['Display statistics of file system in terms of Zetabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Zetabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ -H','NL Queries':['Display statistics of file system in terms of Zetabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 and Zetabytes as unit.',
																				'How do I display statistics of file system in Zetabytes with values in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in powers of 1000 and Zetabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ --si','NL Queries':['Display statistics of file system in terms of Zetabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Zetabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ -t\'NTFS\'','NL Queries':['Display statistics of file system of type NTFS in Zetabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system of type NTFS in terms of Zetabytes .',
																				'How do I display statistics of file system type NTFS in Zetabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of NTFS system in Zetabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Zetabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Zetabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ -P','NL Queries':['Display statistics of file system in terms of Zetabytes and POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in POSIX Format with Zetabytes as unit.',
																				'How do I display statistics of file system in terms of Zetabytes and in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in POSIX Format and Zetabytes unit?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ --portability','NL Queries':['Display statistics of file system in terms of Zetabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Zetabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ -x\'ext3\'','NL Queries':['Display statistics of file system in terms of Zetabytes but not of type ext3.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system except of type ext3 in Zetabytes.',
																				'How do I display statistics of file system in terms of Zetabytes not of type ext3?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes and not of type ext3?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Zetabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Zetabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -BZ --total','NL Queries':['Display statistics of file system in terms of Zetabytes along with their total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space,total disk usage and mount points of the file system in Zetabytes.',
																				'How do I display file system type and other statistics of file system in terms of Zetabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Zetabytes along with their total disk usage?']},ignore_index=True)
# This ends all combinations for -BZ
'''																				
df = df.append({'Command':'df --block-size=Z -a','NL Queries':['Show statistics of all file systems in terms of Zetabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Zetabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Zetabytes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=Z --all','NL Queries':['Show statistics of all file systems in terms of Zetabytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Zetabytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Zetabytes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z -T','NL Queries':['Display file system type and other statistics of file system in terms of Zetabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Zetabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Zetabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --block-size=Z --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Zetabytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Zetabytes.',
																				'How do I Display file system type and other statistics of file system in terms of Zetabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z -h','NL Queries':['Display statistics of file system in terms of Zetabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Zetabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z --human-readable','NL Queries':['Display statistics of file system in terms of Zetabytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Zetabytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z -H','NL Queries':['Display statistics of file system in terms of Zetabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Zetabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z --si','NL Queries':['Display statistics of file system in terms of Zetabytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Zetabytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Zetabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Zetabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Zetabytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Zetabytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z -P','NL Queries':['Display statistics of file system in terms of Zetabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Zetabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z --portability','NL Queries':['Display statistics of file system in terms of Zetabytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Zetabytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Zetabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Zetabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --block-size=Z --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Zetabytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Zetabytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes not of type filesystemtype?']},ignore_index=True)


df = df.append({'Command':'df --block-size=Z --total','NL Queries':['Display statistics of file system in terms of Zetabytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Zetabytes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of Zetabytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Zetabytes along with the total disk usage?']},ignore_index=True)

# This ends all combinations for --block-size=Z

df = df.append({'Command':'df -k -a','NL Queries':['Show statistics of all file systems in terms of Kilobytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Kilobytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df -k --all','NL Queries':['Show statistics of all file systems in terms of Kilobytes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of Kilobytes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of Kilobytes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df -k -T','NL Queries':['Display file system type and other statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)
																				
df = df.append({'Command':'df -k --print-type','NL Queries':['Display file system type and other statistics of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -k -h','NL Queries':['Display statistics of file system in terms of Kilobytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Kilobytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df -k --human-readable','NL Queries':['Display statistics of file system in terms of Kilobytes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in Human Readable Format.',
																				'How do I display statistics of file system in terms of Kilobytes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df -k -H','NL Queries':['Display statistics of file system in terms of Kilobytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in powers of 1000.',
																				'How do I display statistics of file system in terms of Kilobytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df -k --si','NL Queries':['Display statistics of file system in terms of Kilobytes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in powers of 1000.',
																				'How do I Display statistics of file system in terms of Kilobytes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df -k -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -k --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -k -P','NL Queries':['Display statistics of file system in terms of Kilobytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Kilobytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df -k --portability','NL Queries':['Display statistics of file system in terms of Kilobytes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes in POSIX Format.',
																				'How do I Display statistics of file system in terms of Kilobytes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df -k -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -k --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of Kilobytes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of Kilobytes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes not of type filesystemtype?']},ignore_index=True)


df = df.append({'Command':'df -k --total','NL Queries':['Display statistics of file system in terms of Kilobytes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of Kilobytes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of Kilobytes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of Kilobytes along with the total disk usage?']},ignore_index=True)
'''
# This ends all combinations for -k

df = df.append({'Command':'df -i -a','NL Queries':['Show statistics of all file systems in terms of inodes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system and the dummy file system in terms of inodes.',
																				'How can I show the statistics of all file systems with dummy ones also included, in terms of inodes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of inodes, including the dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -i --all','NL Queries':['Show statistics of all file systems in terms of inodes along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of inodes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of inodes, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -i -T','NL Queries':['Display file system type and other statistics of file systems in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of inodes.',
																				'How do I view file system type and other statistics of file system in terms of inodes?',
																				'How do I see the device name, total blocks, total disk space, available disk space,file system type and mount points of the system in terms of inodes?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -i --print-type','NL Queries':['Display file system type and other statistics of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of inodes.',
																				'How do I Display file system type and other statistics of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -i -h','NL Queries':['Display statistics of file system in terms of inodes and in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes and in Human Readable Format.',
																				'How do I display statistics of file system in terms of inodes and in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes, in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -i --human-readable','NL Queries':['Display statistics of file system in terms of inodes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in Human Readable Format.',
																				'How do I display statistics of file system in terms of inodes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -i -H','NL Queries':['Display statistics of file system in terms of inodes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes and powers of 1000.',
																				'How do I display statistics of file system in terms of inodes and powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -i --si','NL Queries':['Display statistics of file system in terms of inodes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in powers of 1000.',
																				'How do I Display statistics of file system in terms of inodes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -i -t\'ext4\'','NL Queries':['Display statistics of file system of type ext4 in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the  of type ext4 file system in terms of inodes.',
																				'How do I display statistics of file system in terms of inodes of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system of type ext4 in terms of inodes ?']},ignore_index=True)
'''
df = df.append({'Command':'df -i --type=\'ext4\'','NL Queries':['Display statistics of file system in terms of inodes of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes of type ext4.',
																				'How do I Display statistics of file system in terms of inodes of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes of type ext4?']},ignore_index=True)
'''
df = df.append({'Command':'df -i -P','NL Queries':['Display statistics of file system in terms of inodes in POSIX Format.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in POSIX Format.',
																				'How do I display statistics of file system in terms of inodes in POSIX Format?',
																				'How do I see device name, total blocks, total disk space, available disk space and mount points of the file system in terms of inodes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -i --portability','NL Queries':['Display statistics of file system in terms of inodes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in POSIX Format.',
																				'How do I Display statistics of file system in terms of inodes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -i -x\'ext4\'','NL Queries':['Display statistics of file system in terms of inodes but not of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes except of type ext4.',
																				'How do I see the statistics of file system without type ext4 in terms of inodes?',
																				'How do I view device name, total blocks, total disk space, available disk space and mount points of the file system, not of ext4, in terms of inodes ?']},ignore_index=True)
'''
df = df.append({'Command':'df -i --exclude-type=\'ext4\'','NL Queries':['Display statistics of file system in terms of inodes not of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes not of type ext4.',
																				'How do I Display statistics of file system in terms of inodes not of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes not of type ext4?']},ignore_index=True)
'''

df = df.append({'Command':'df -i --total','NL Queries':['Show statistics of file system in terms of inodes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space,total disk usage and mount points of the system in terms of inodes.',
																				'How do I display disk usage and other statistics of file system in terms of inodes?',
																				'How do I see the device name, total blocks, total disk space, available disk space,disk usage and mount points of the file system in terms of inodes?']},ignore_index=True)

# This ends all combinations for -i
'''
df = df.append({'Command':'df --inodes -a','NL Queries':['Show statistics of all file systems in terms of inodes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of inodes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of inodes, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --inodes --all','NL Queries':['Show statistics of all file systems in terms of inodes Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in terms of inodes?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in terms of inodes, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --inodes -T','NL Queries':['Display file system type and other statistics of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of inodes.',
																				'How do I Display file system type and other statistics of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes?']},ignore_index=True)
																				
df = df.append({'Command':'df --inodes --print-type','NL Queries':['Display file system type and other statistics of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in terms of inodes.',
																				'How do I Display file system type and other statistics of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --inodes -h','NL Queries':['Display statistics of file system in terms of inodes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in Human Readable Format.',
																				'How do I display statistics of file system in terms of inodes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --inodes --human-readable','NL Queries':['Display statistics of file system in terms of inodes in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in Human Readable Format.',
																				'How do I display statistics of file system in terms of inodes in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --inodes -H','NL Queries':['Display statistics of file system in terms of inodes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in powers of 1000.',
																				'How do I display statistics of file system in terms of inodes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --inodes --si','NL Queries':['Display statistics of file system in terms of inodes in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in powers of 1000.',
																				'How do I Display statistics of file system in terms of inodes in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --inodes -t\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of inodes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of inodes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --inodes --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of inodes of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes of type filesystemtype.',
																				'How do I Display statistics of file system in terms of inodes of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --inodes -P','NL Queries':['Display statistics of file system in terms of inodes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in POSIX Format.',
																				'How do I Display statistics of file system in terms of inodes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --inodes --portability','NL Queries':['Display statistics of file system in terms of inodes in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes in POSIX Format.',
																				'How do I Display statistics of file system in terms of inodes in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --inodes -x\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of inodes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of inodes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --inodes --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in terms of inodes not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes not of type filesystemtype.',
																				'How do I Display statistics of file system in terms of inodes not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes not of type filesystemtype?']},ignore_index=True)


df = df.append({'Command':'df --inodes --total','NL Queries':['Display statistics of file system in terms of inodes along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in terms of inodes along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in terms of inodes along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes along with the total disk usage?']},ignore_index=True)
'''
# This ends all combinations for --inodes

df = df.append({'Command':'df -H -a','NL Queries':['Show statistics of all file systems in powers of 1000 along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000, along with those of dummy file system.',
																				'How can I show the statistics of all file systems and the dummy ones in powers of 1000?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of  all the file systems including dummy ones in powers of 1000, ?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -H --all','NL Queries':['Show statistics of all file systems in powers of 1000 Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in powers of 1000?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in powers of 1000, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -H -T','NL Queries':['Display file system type and other statistics of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system in powers of 1000.',
																				'How do I display file system type and other statistics of file system in powers of 1000?',
																				'How do I display device name, total blocks, file system type, total disk space, available disk space and mount points of the file system in powers of 1000?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -H --print-type','NL Queries':['Display file system type and other statistics of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in powers of 1000.',
																				'How do I Display file system type and other statistics of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -H -t\'NTFS\'','NL Queries':['Display statistics of file system in powers of 1000 of type NTFS.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 of type NTFS.',
																				'How do I display statistics of file system  of type NTFS in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the  NTFS file system in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -H --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in powers of 1000 of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 of type filesystemtype.',
																				'How do I Display statistics of file system in powers of 1000 of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -H -P','NL Queries':['Show statistics of file system in powers of 1000 in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 in POSIX Format.',
																				'How do I display statistics of file system in powers of 1000 in POSIX Format?',
																				'How do I see the device name, total blocks, total disk space, available disk space and mount points of the file system in powers of 1000 in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -H --portability','NL Queries':['Display statistics of file system in powers of 1000 in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 in POSIX Format.',
																				'How do I Display statistics of file system in powers of 1000 in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -H -x\'NTFS\'','NL Queries':['Display statistics of file system except of type NTFS in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in powers of 1000 except of type NTFS.',
																				'How do I see statistics of all file systems in powers of 1000 but not of type NTFS?',
																				'How do I view the device name, total blocks, total disk space, available disk space and mount points of the file system  except for NTFS in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -H --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in powers of 1000 not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 not of type filesystemtype.',
																				'How do I Display statistics of file system in powers of 1000 not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 not of type filesystemtype?']},ignore_index=True)
'''

df = df.append({'Command':'df -H --total','NL Queries':['Display statistics of file system in powers of 1000 along with the total disk usage.',
																				'Show device name,total blocks, total disk usage total disk space,available disk space and mount points of the system in powers of 1000.',
																				'How do I view total disk usage and other statistics of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space and usage, available disk space and mount points of the system in powers of 1000?']},ignore_index=True)

# This ends all combinations for -H
'''
df = df.append({'Command':'df --si -a','NL Queries':['Show statistics of all file systems in powers of 1000 Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in powers of 1000?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in powers of 1000, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --si --all','NL Queries':['Show statistics of all file systems in powers of 1000 Along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in powers of 1000?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in powers of 1000, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --si -T','NL Queries':['Display file system type and other statistics of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in powers of 1000.',
																				'How do I Display file system type and other statistics of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000?']},ignore_index=True)
																				
df = df.append({'Command':'df --si --print-type','NL Queries':['Display file system type and other statistics of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in powers of 1000.',
																				'How do I Display file system type and other statistics of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --si -t\'filesystemtype\'','NL Queries':['Display statistics of file system in powers of 1000 of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 of type filesystemtype.',
																				'How do I Display statistics of file system in powers of 1000 of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --si --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in powers of 1000 of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 of type filesystemtype.',
																				'How do I Display statistics of file system in powers of 1000 of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --si -P','NL Queries':['Display statistics of file system in powers of 1000 in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 in POSIX Format.',
																				'How do I Display statistics of file system in powers of 1000 in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --si --portability','NL Queries':['Display statistics of file system in powers of 1000 in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 in POSIX Format.',
																				'How do I Display statistics of file system in powers of 1000 in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --si -x\'filesystemtype\'','NL Queries':['Display statistics of file system in powers of 1000 not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 not of type filesystemtype.',
																				'How do I Display statistics of file system in powers of 1000 not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --si --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in powers of 1000 not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 not of type filesystemtype.',
																				'How do I Display statistics of file system in powers of 1000 not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 not of type filesystemtype?']},ignore_index=True)


df = df.append({'Command':'df --si --total','NL Queries':['Display statistics of file system in powers of 1000 along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in powers of 1000 along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in powers of 1000 along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in powers of 1000 along with the total disk usage?']},ignore_index=True)
'''
# This ends all combinations for --si

df = df.append({'Command':'df -h -a','NL Queries':['Show statistics of all file systems and the dummy ones in Human Readable Format.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format, along with those of dummy file system.',
																				'How can I see the statistics of all file systems including the dummy ones in Human Readable Format?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the file system in Human Readable Format, along with those of the dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -h --all','NL Queries':['Show statistics of all file systems along with dummy ones in Human Readable Format.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in Human Readable Format?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in Human Readable Format, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -h -T','NL Queries':['Display file system type and other statistics of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the file system in Human Readable Format.',
																				'How do I see file system type and other statistics of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -h --print-type','NL Queries':['Display file system type and other statistics of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in Human Readable Format.',
																				'How do I Display file system type and other statistics of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format?']},ignore_index=True)
'''	

df = df.append({'Command':'df -h -BG','NL Queries':['Display statistics of file system in Human Readable Format in Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in Gigabytes.',
																				'How do I see statistics of file system in Human Readable Format in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format in Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df -h -BK','NL Queries':['Display statistics of file system in Human Readable Format in Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in Kilobytes.',
																				'How do I see file system type and other statistics of file system in Human Readable Format in Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format in Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -h -BM','NL Queries':['Display file system type and other statistics of file system in Human Readable Format in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in Megabytes.',
																				'How do I display statistics of file system in Human Readable Format in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format in Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -h -BT','NL Queries':['Display statistics of file system in Human Readable Format in Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in Terabytes.',
																				'How do I see statistics of file system in Human Readable Format in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format in Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -h -BP','NL Queries':['Display statistics of file system in Human Readable Format in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in Petabytes.',
																				'How do I view statistics of file system in Human Readable Format in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format in Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -h -BY','NL Queries':['Display statistics of file system in Human Readable Format in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in Yottabytes.',
																				'How do I see statistics of file system in Human Readable Format in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format in Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -h -BZ','NL Queries':['Display statistics of file system in Human Readable Format in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in Zettabytes.',
																				'How do I display statistics of file system in Human Readable Format in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format in Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df -h -BZ','NL Queries':['Display statistics of file system in Human Readable Format in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in Exabytes.',
																				'How do I display statistics of file system in Human Readable Format in Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format in Exabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -h --block-size=G','NL Queries':['Display statistics of file system in Human Readable Format in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Gigabytes.',
																				'How do I display statistics of file system in Human Readable Format in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df -h --block-size=E','NL Queries':['Display statistics of file system in Human Readable Format in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Exabytes.',
																				'How do I display statistics of file system in Human Readable Format in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -h --block-size=K','NL Queries':['Display statistics of file system in Human Readable Format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Kilobytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -h --block-size=M','NL Queries':['Display statistics of file system in Human Readable Format in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Megabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -h --block-size=T','NL Queries':['Display statistics of file system in Human Readable Format in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Terabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -h --block-size=P','NL Queries':['Display statistics of file system in Human Readable Format in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Petabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -h --block-size=Y','NL Queries':['Display fstatistics of file system in Human Readable Format in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Yottabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -h --block-size=Z','NL Queries':['Display statistics of file system in Human Readable Format in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Zettabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Zettabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -h -t\'ext3\'','NL Queries':['Display statistics of file system in Human Readable Format of type ext3.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the ext3 file system in Human Readable Format.',
																				'How do I see statistics of file system in Human Readable Format of type ext3?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the ext3 file system in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -h --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in Human Readable Format of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format of type filesystemtype.',
																				'How do I Display statistics of file system in Human Readable Format of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -h -P','NL Queries':['Display statistics of file system in Human Readable Format in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in POSIX Format.',
																				'How do I see statistics of file system in Human Readable Format in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -h --portability','NL Queries':['Display statistics of file system in Human Readable Format in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in POSIX Format.',
																				'How do I Display statistics of file system in Human Readable Format in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -h -i','NL Queries':['Display statistics of file system in Human Readable Format in inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format in terms of inodes.',
																				'How do I see statistics of file system in Human Readable Format in terms of inodes?',
																				'How do I view device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -h --inodes','NL Queries':['Display statistics of file system in Human Readable Format in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format interms of inodes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -h -x\'NTFS\'','NL Queries':['Display statistics of file system in Human Readable Format except that of NTFS.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Human Readable Format excluding type NTFS.',
																				'How do I see statistics of file system apart from NTFS in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Human Readable Format except of type NTFS?']},ignore_index=True)
'''
df = df.append({'Command':'df -h --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in Human Readable Format not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format not of type filesystemtype.',
																				'How do I Display statistics of file system in Human Readable Format not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -h -k','NL Queries':['Display statistics of file system in Human Readable Format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in Human Readable Format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -h --total','NL Queries':['Display statistics of file system in Human Readable Format along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space,total disk usage and mount points of the file system in Human Readable Format.',
																				'How do I see all statistics of file system in Human Readable Format including the total disk usage?',
																				'How do I display device name, total blocks, total disk space and usage, available disk space and mount points of the file system in Human Readable Format?']},ignore_index=True)

# This ends all combinations for -h
'''
df = df.append({'Command':'df --human-readable -a','NL Queries':['Show statistics of all file systems along with dummy ones in Human Readable Format.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in Human Readable Format?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in Human Readable Format, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --human-readable --all','NL Queries':['Show statistics of all file systems along with dummy ones in Human Readable Format.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in Human Readable Format?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in Human Readable Format, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -T','NL Queries':['Display file system type and other statistics of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in Human Readable Format.',
																				'How do I Display file system type and other statistics of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format?']},ignore_index=True)
																				
df = df.append({'Command':'df --human-readable --print-type','NL Queries':['Display file system type and other statistics of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in Human Readable Format.',
																				'How do I Display file system type and other statistics of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format?']},ignore_index=True)
																			
df = df.append({'Command':'df --human-readable -BG','NL Queries':['Display statistics of file system in Human Readable Format in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Gigabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --human-readable -BK','NL Queries':['Display statistics of file system in Human Readable Format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in Human Readable Format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -BM','NL Queries':['Display file system type and other statistics of file system in Human Readable Format in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Megabytes.',
																				'How do I Display file system type and other statistics of file system in Human Readable Format in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -BT','NL Queries':['Display statistics of file system in Human Readable Format in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Terabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -BP','NL Queries':['Display statistics of file system in Human Readable Format in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Petabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -BY','NL Queries':['Display statistics of file system in Human Readable Format in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Yottabytes.',
																				'How do I display statistics of file system in Human Readable Format in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -BZ','NL Queries':['Display statistics of file system in Human Readable Format in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Zettabytes.',
																				'How do I display statistics of file system in Human Readable Format in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -BE','NL Queries':['Display statistics of file system in Human Readable Format in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Exabytes.',
																				'How do I display statistics of file system in Human Readable Format in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --block-size=G','NL Queries':['Display statistics of file system in Human Readable Format in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Gigabytes.',
																				'How do I display statistics of file system in Human Readable Format in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --block-size=E','NL Queries':['Display statistics of file system in Human Readable Format in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Exabytes.',
																				'How do I display statistics of file system in Human Readable Format in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --block-size=K','NL Queries':['Display statistics of file system in Human Readable Format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Kilobytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --block-size=M','NL Queries':['Display statistics of file system in Human Readable Format in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Megabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --block-size=T','NL Queries':['Display statistics of file system in Human Readable Format in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Terabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --block-size=P','NL Queries':['Display statistics of file system in Human Readable Format in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Petabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --block-size=Y','NL Queries':['Display fstatistics of file system in Human Readable Format in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Yottabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --block-size=Z','NL Queries':['Display statistics of file system in Human Readable Format in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Zettabytes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -t\'filesystemtype\'','NL Queries':['Display statistics of file system in Human Readable Format of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format of type filesystemtype.',
																				'How do I Display statistics of file system in Human Readable Format of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in Human Readable Format of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format of type filesystemtype.',
																				'How do I Display statistics of file system in Human Readable Format of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -P','NL Queries':['Display statistics of file system in Human Readable Format in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in POSIX Format.',
																				'How do I Display statistics of file system in Human Readable Format in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --portability','NL Queries':['Display statistics of file system in Human Readable Format in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in POSIX Format.',
																				'How do I Display statistics of file system in Human Readable Format in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -i','NL Queries':['Display statistics of file system in Human Readable Format in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format interms of inodes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --inodes','NL Queries':['Display statistics of file system in Human Readable Format in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format interms of inodes.',
																				'How do I Display statistics of file system in Human Readable Format in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -x\'filesystemtype\'','NL Queries':['Display statistics of file system in Human Readable Format not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format not of type filesystemtype.',
																				'How do I Display statistics of file system in Human Readable Format not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in Human Readable Format not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format not of type filesystemtype.',
																				'How do I Display statistics of file system in Human Readable Format not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --human-readable -k','NL Queries':['Display statistics of file system in Human Readable Format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in Human Readable Format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --human-readable --total','NL Queries':['Display statistics of file system in Human Readable Format along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in Human Readable Format along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in Human Readable Format along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in Human Readable Format along with the total disk usage?']},ignore_index=True)
'''
# This ends all combinations for --human-readable


df = df.append({'Command':'df -t\'ext4\' -a','NL Queries':['Show statistics of all file systems along with dummy ones of type ext4.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system of type ext4 and the dummy file system.',
																				'How can I show the statistics of all ext4 file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the file system of type ext4 and dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -t\'filesystemtype\' --all','NL Queries':['Show statistics of all file systems along with dummy ones of type filesystemtype.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones of type filesystemtype?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system of type filesystemtype, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'ext3\' -T','NL Queries':['Display file system type and other statistics of file system of type ext3.',
																				'Display device name,total blocks,total disk space,available disk space,file system type and mount points of the file system of type ext3.',
																				'How do I show file system type and other statistics of file system of type ext3?',
																				'How do I display device name, total blocks, total disk space,file system type, available disk space and mount points of the system of type ext3?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -t\'filesystemtype\' --print-type','NL Queries':['Display file system type and other statistics of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system of type filesystemtype.',
																				'How do I Display file system type and other statistics of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -t\'filesystemtype\' -h','NL Queries':['Display statistics of file system of type filesystemtype in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in Human Readable Format.',
																				'How do I display statistics of file system of type filesystemtype in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df -t\'filesystemtype\' --human-readable','NL Queries':['Display statistics of file system of type filesystemtype in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in Human Readable Format.',
																				'How do I display statistics of file system of type filesystemtype in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'NTFS\' -H','NL Queries':['Display statistics of file system of type NTFS in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system of type NTFS in powers of 1000.',
																				'How do I see statistics of file system of type NTFS in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system of type NTFS in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'NTFS\' --si','NL Queries':['Display statistics of file system of type NTFS in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type NTFS in powers of 1000.',
																				'How do I Display statistics of file system of type NTFS in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type NTFS in powers of 1000?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -t\'NTFS\' -BG','NL Queries':['Display statistics of file system of type NTFS in Gigabytes.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system of type NTFS in Gigabytes.',
																				'How do I show statistics of file system of type NTFS in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system of type NTFS in Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'ext3\' -BK','NL Queries':['Display statistics of file system of type ext3 in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type ext3 in Kilobytes.',
																				'How do I see all statistics of file system of type ext3 in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the ext3 file system in Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'ext3\' -BM','NL Queries':['Display all statistics of file system of type ext3 in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system of type ext3 in Megabytes.',
																				'How do I see file system type and other statistics of file system of type ext3 in Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system of type ext3 in Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'ext3\' -BT','NL Queries':['Display statistics of file system of type ext3 in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system of type ext3 in Terabytes.',
																				'How do I view statistics of file system of type ext3 in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system of type ext3 in Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'ext3\' -BP','NL Queries':['Display statistics of file system of type ext3 in terms of Petabytes.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the ext3 file system in Petabytes.',
																				'How do I Display statistics of file system of type ext3 in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system of type ext3 in Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'NTFS\' -BY','NL Queries':['Show statistics of file system of type NTFS in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the NTFS file system in Yottabytes.',
																				'How do I see statistics of file system of type NTFS in Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system of type NTFS in Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'NTFS\' -BZ','NL Queries':['Show statistics of file system of type NTFS in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of NTFS file system in Zettabytes.',
																				'How do I see statistics of file system of type NTFS in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system of type NTFS in Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'ext4\' -BE','NL Queries':['Display statistics of file system of type ext4 in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the ext4 file system in Exabytes.',
																				'How do I see statistics of file system of type ext4 in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the ext4 file system in Exabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'ext4\' --block-size=G','NL Queries':['Display statistics of file system of type ext4 in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type ext4 in terms of Gigabytes.',
																				'How do I display statistics of file system of type ext4 in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type ext4 in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'filesystemtype\' --block-size=E','NL Queries':['Display statistics of file system of type filesystemtype in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Exabytes.',
																				'How do I display statistics of file system of type filesystemtype in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'filesystemtype\' --block-size=K','NL Queries':['Display statistics of file system of type filesystemtype in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Kilobytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'filesystemtype\' --block-size=M','NL Queries':['Display statistics of file system of type filesystemtype in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Megabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'filesystemtype\' --block-size=T','NL Queries':['Display statistics of file system of type filesystemtype in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Terabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'filesystemtype\' --block-size=P','NL Queries':['Display statistics of file system of type filesystemtype in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Petabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'filesystemtype\' --block-size=Y','NL Queries':['Display fstatistics of file system of type filesystemtype in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Yottabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -t\'filesystemtype\' --block-size=Z','NL Queries':['Display statistics of file system of type filesystemtype in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Zettabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Zettabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'NTFS\' -P','NL Queries':['Show statistics of file system of type NTFS in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type NTFS in POSIX Format.',
																				'How do I see statistics of file system of type NTFS in POSIX Format?',
																				'How do I see device name, total blocks, total disk space, available disk space and mount points of the system of type NTFS in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'filesystemtype\' --portability','NL Queries':['Display statistics of file system of type filesystemtype in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in POSIX Format.',
																				'How do I Display statistics of file system of type filesystemtype in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'NTFS\' -i','NL Queries':['Show statistics of file system of type NTFS in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type NTFS in terms of inodes.',
																				'How do I see statistics of file system of type NTFS in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type NTFS in terms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'NTFS\' --inodes','NL Queries':['Display statistics of file system of type NTFS in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type NTFS interms of inodes.',
																				'How do I Display statistics of file system of type NTFS in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type NTFS interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df -t\'NTFS\' -k','NL Queries':['Display statistics of file system of type NTFS in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type NTFS in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system of type NTFS in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type NTFS in terms of Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -t\'ext4\' --total','NL Queries':['Display statistics of file system of type ext4 along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system of type ext4.',
																				'How do I see all statistics of file system of type ext4 along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space and usage, available disk space and mount points of the system of type ext4?']},ignore_index=True)

# This ends all working possible combinations for -t

'''
df = df.append({'Command':'df --type=\'ext4\' -a','NL Queries':['Show statistics of all file systems along with dummy ones of type ext4.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system of type ext4, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones of type ext4?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system of type ext4, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --type=\'filesystemtype\' --all','NL Queries':['Show statistics of all file systems along with dummy ones of type filesystemtype.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones of type filesystemtype?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system of type filesystemtype, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -T','NL Queries':['Display file system type and other statistics of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system of type filesystemtype.',
																				'How do I Display file system type and other statistics of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype?']},ignore_index=True)
																				
df = df.append({'Command':'df --type=\'filesystemtype\' --print-type','NL Queries':['Display file system type and other statistics of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system of type filesystemtype.',
																				'How do I Display file system type and other statistics of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -h','NL Queries':['Display statistics of file system of type filesystemtype in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in Human Readable Format.',
																				'How do I display statistics of file system of type filesystemtype in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --human-readable','NL Queries':['Display statistics of file system of type filesystemtype in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in Human Readable Format.',
																				'How do I display statistics of file system of type filesystemtype in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -H','NL Queries':['Display statistics of file system of type filesystemtype in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in powers of 1000.',
																				'How do I display statistics of file system of type filesystemtype in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --si','NL Queries':['Display statistics of file system of type filesystemtype in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in powers of 1000.',
																				'How do I Display statistics of file system of type filesystemtype in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in powers of 1000?']},ignore_index=True)
																				
df = df.append({'Command':'df --type=\'filesystemtype\' -BG','NL Queries':['Display statistics of file system of type filesystemtype in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Gigabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --type=\'filesystemtype\' -BK','NL Queries':['Display statistics of file system of type filesystemtype in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system of type filesystemtype in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -BM','NL Queries':['Display file system type and other statistics of file system of type filesystemtype in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Megabytes.',
																				'How do I Display file system type and other statistics of file system of type filesystemtype in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -BT','NL Queries':['Display statistics of file system of type filesystemtype in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Terabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -BP','NL Queries':['Display statistics of file system of type filesystemtype in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Petabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -BY','NL Queries':['Display statistics of file system of type filesystemtype in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Yottabytes.',
																				'How do I display statistics of file system of type filesystemtype in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -BZ','NL Queries':['Display statistics of file system of type filesystemtype in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Zettabytes.',
																				'How do I display statistics of file system of type filesystemtype in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -BE','NL Queries':['Display statistics of file system of type filesystemtype in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Exabytes.',
																				'How do I display statistics of file system of type filesystemtype in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --block-size=G','NL Queries':['Display statistics of file system of type filesystemtype in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Gigabytes.',
																				'How do I display statistics of file system of type filesystemtype in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --block-size=E','NL Queries':['Display statistics of file system of type filesystemtype in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Exabytes.',
																				'How do I display statistics of file system of type filesystemtype in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --block-size=K','NL Queries':['Display statistics of file system of type filesystemtype in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Kilobytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --block-size=M','NL Queries':['Display statistics of file system of type filesystemtype in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Megabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --block-size=T','NL Queries':['Display statistics of file system of type filesystemtype in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Terabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --block-size=P','NL Queries':['Display statistics of file system of type filesystemtype in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Petabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --block-size=Y','NL Queries':['Display fstatistics of file system of type filesystemtype in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Yottabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --block-size=Z','NL Queries':['Display statistics of file system of type filesystemtype in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Zettabytes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -P','NL Queries':['Display statistics of file system of type filesystemtype in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in POSIX Format.',
																				'How do I Display statistics of file system of type filesystemtype in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --portability','NL Queries':['Display statistics of file system of type filesystemtype in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in POSIX Format.',
																				'How do I Display statistics of file system of type filesystemtype in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -i','NL Queries':['Display statistics of file system of type filesystemtype in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype interms of inodes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --inodes','NL Queries':['Display statistics of file system of type filesystemtype in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype interms of inodes.',
																				'How do I Display statistics of file system of type filesystemtype in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' -k','NL Queries':['Display statistics of file system of type filesystemtype in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system of type filesystemtype in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --type=\'filesystemtype\' --total','NL Queries':['Display statistics of file system of type filesystemtype along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system of type filesystemtype along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system of type filesystemtype along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system of type filesystemtype along with the total disk usage?']},ignore_index=True)
'''
# This ends all combinations for --type


df = df.append({'Command':'df -x\'ext4\' -a','NL Queries':['Show statistics of all file systems along with dummy ones except of type ext4.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system including dummy ones except type ext4.',
																				'How can I see the statistics of all file systems along with dummy ones but not of type ext4?',
																				'How can I view device name,total blocks, total disk space,available disk space and mount points of the file system, including the dummy ones, not of type ext4?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -x\'ext4\' --all','NL Queries':['Show statistics of all file systems along with dummy ones not of type ext4.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system not of type ext4, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones not of type ext4?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system not of type ext4, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext4\' -T','NL Queries':['Display file system type and other statistics of file system except of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system except type ext4.',
																				'How do I see file system type and other statistics of file system but not of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the file system, not of type ext4?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -x\'ext4\' --print-type','NL Queries':['Display file system type and other statistics of file system not of type ext4.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system not of type ext4.',
																				'How do I Display file system type and other statistics of file system not of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type ext4?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext3\' -h','NL Queries':['Display statistics of file system not of type ext3 in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system, except type ext3, in Human Readable Format.',
																				'How do I see statistics of file system not of type ext3 in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system, not of type ext3, in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext3\' --human-readable','NL Queries':['Display statistics of file system not of type ext3 in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type ext3 in Human Readable Format.',
																				'How do I display statistics of file system not of type ext3 in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type ext3 in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext3\' -H','NL Queries':['Display statistics of file system except of type ext3 in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system, not of type ext3, in powers of 1000.',
																				'How do I display statistics of file system in powers of 1000, except of type ext3?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system, not of type ext3, in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext3\' --si','NL Queries':['Display statistics of file system not of type ext3 in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type ext3 in powers of 1000.',
																				'How do I Display statistics of file system not of type ext3 in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type ext3 in powers of 1000?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -x\'NTFS\' -BG','NL Queries':['Display statistics of file system,not of type NTFS, in Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Gigabytes, except for NTFS file system type.',
																				'How do I see statistics of file system, not of type NTFS, in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system, not of type NTFS, in Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df -x\'NTFS\' -BK','NL Queries':['Display statistics of file system, not of type NTFS, in terms of Kilobytes.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system except that of type NTFS, in Kilobytes.',
																				'How do I see statistics of file system, not of type NTFS, in Kilobytes?',
																				'How do I view device name, total blocks, total disk space, available disk space and mount points of the file system, not of type NTFS, in Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'ext3\' -BM','NL Queries':['Display file system type and other statistics of file system except of type ext3 in Megabytes.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the  file system, except of type ext3, in Megabytes.',
																				'How do I see statistics of file system, not of type ext3, in Megabytes?',
																				'How do I view device name, total blocks, total disk space, available disk space and mount points of the file system, not of type ext3, in Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'ext3\' -BT','NL Queries':['Display statistics of file system except of type ext3 in Terabytes.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system, not of type ext3, in Terabytes.',
																				'How do I see statistics of file system, not of type ext3, in terms of Terabytes?',
																				'How do I view device name, total blocks, total disk space, available disk space and mount points of the file system, not of type ext3, in Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'NTFS\' -BP','NL Queries':['Display statistics of file system except of type NTFS in Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system in Petabytes but not of type NTFS.',
																				'How do I see statistics of file system, not of type NTFS, in Petabytes?',
																				'How do I view device name, total blocks, total disk space, available disk space and mount points of the file system, not of type NTFS, in Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'NTFS\' -BY','NL Queries':['Display statistics of file system except of type NTFS in Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system, not of type NTFS, in Yottabytes.',
																				'How do I see statistics of file system, not of type NTFS, in terms of Yottabytes?',
																				'How do I view device name, total blocks, total disk space, available disk space and mount points of the file system in Yottabytes except that of type NTFS?']},ignore_index=True)

df = df.append({'Command':'df -x\'ext3\' -BZ','NL Queries':['Display statistics of file system except of type ext3 in Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system not of type ext3 in Zettabytes.',
																				'How do I see statistics of file system, not of type ext3, in Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Zettabytes except that of type ext3?']},ignore_index=True)

df = df.append({'Command':'df -x\'ext3\' -BE','NL Queries':['Display statistics of file system except of type ext3 in Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system not of type ext3 in terms of Exabytes.',
																				'How do I see statistics of file system, not of type ext3, in Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the file system in Exabytes except of type ext3?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'filesystemtype\' --block-size=G','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Gigabytes.',
																				'How do I display statistics of file system not of type filesystemtype in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'filesystemtype\' --block-size=E','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Exabytes.',
																				'How do I display statistics of file system not of type filesystemtype in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'filesystemtype\' --block-size=K','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'filesystemtype\' --block-size=M','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Megabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'filesystemtype\' --block-size=T','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Terabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'filesystemtype\' --block-size=P','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Petabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'filesystemtype\' --block-size=Y','NL Queries':['Display fstatistics of file system not of type filesystemtype in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Yottabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -x\'filesystemtype\' --block-size=Z','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Zettabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Zettabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext3\' -P','NL Queries':['Display statistics of file system except of type ext3 in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the file system, not of type ext3, in POSIX Format.',
																				'How do I see statistics of file system in POSIX Format except of ext3 type?',
																				'How do I view device name, total blocks, total disk space, available disk space and mount points of the file system in POSIX Format except that of type ext3?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext3\' --portability','NL Queries':['Display statistics of file system not of type ext3 in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type ext3 in POSIX Format.',
																				'How do I Display statistics of file system not of type ext3 in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type ext3 in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext4\' -i','NL Queries':['Display statistics of file system except of type ext4 in terms of inodes.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the file system, not of type ext4, in terms of inodes.',
																				'How do I see statistics of file system in terms of inodes except of type ext4?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in terms of inodes except ext4 type?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'filesystemtype\' --inodes','NL Queries':['Display statistics of file system not of type filesystemtype in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype interms of inodes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df -x\'filesystemtype\' -k','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system not of type filesystemtype in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -x\'ext4\' --total','NL Queries':['Display statistics of file system, not of type ext4, along with the total disk usage.',
																				'Show device name,total blocks,total disk space,available disk space,total disk usage and mount points of the file system except of type ext4.',
																				'How do I see total disk usage and other statistics of file system except of type ext4?',
																				'How do I view device name, total blocks, total disk space and usage, available disk space and mount points of the file system but not of type ext4?']},ignore_index=True)

# This ends all combinations for -x

'''
df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -a','NL Queries':['Show statistics of all file systems along with dummy ones not of type filesystemtype.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones not of type filesystemtype?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system not of type filesystemtype, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --all','NL Queries':['Show statistics of all file systems along with dummy ones not of type filesystemtype.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones not of type filesystemtype?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system not of type filesystemtype, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -T','NL Queries':['Display file system type and other statistics of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system not of type filesystemtype.',
																				'How do I Display file system type and other statistics of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype?']},ignore_index=True)
																				
df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --print-type','NL Queries':['Display file system type and other statistics of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system not of type filesystemtype.',
																				'How do I Display file system type and other statistics of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -h','NL Queries':['Display statistics of file system not of type filesystemtype in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in Human Readable Format.',
																				'How do I display statistics of file system not of type filesystemtype in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --human-readable','NL Queries':['Display statistics of file system not of type filesystemtype in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in Human Readable Format.',
																				'How do I display statistics of file system not of type filesystemtype in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -H','NL Queries':['Display statistics of file system not of type filesystemtype in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in powers of 1000.',
																				'How do I display statistics of file system not of type filesystemtype in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --si','NL Queries':['Display statistics of file system not of type filesystemtype in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in powers of 1000.',
																				'How do I Display statistics of file system not of type filesystemtype in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in powers of 1000?']},ignore_index=True)
																				
df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -BG','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Gigabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -BK','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system not of type filesystemtype in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -BM','NL Queries':['Display file system type and other statistics of file system not of type filesystemtype in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Megabytes.',
																				'How do I Display file system type and other statistics of file system not of type filesystemtype in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -BT','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Terabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -BP','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Petabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -BY','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Yottabytes.',
																				'How do I display statistics of file system not of type filesystemtype in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -BZ','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Zettabytes.',
																				'How do I display statistics of file system not of type filesystemtype in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -BE','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Exabytes.',
																				'How do I display statistics of file system not of type filesystemtype in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --block-size=G','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Gigabytes.',
																				'How do I display statistics of file system not of type filesystemtype in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --block-size=E','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Exabytes.',
																				'How do I display statistics of file system not of type filesystemtype in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --block-size=K','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --block-size=M','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Megabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --block-size=T','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Terabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --block-size=P','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Petabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --block-size=Y','NL Queries':['Display fstatistics of file system not of type filesystemtype in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Yottabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --block-size=Z','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Zettabytes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -P','NL Queries':['Display statistics of file system not of type filesystemtype in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in POSIX Format.',
																				'How do I Display statistics of file system not of type filesystemtype in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --portability','NL Queries':['Display statistics of file system not of type filesystemtype in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in POSIX Format.',
																				'How do I Display statistics of file system not of type filesystemtype in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -i','NL Queries':['Display statistics of file system not of type filesystemtype in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype interms of inodes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --inodes','NL Queries':['Display statistics of file system not of type filesystemtype in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype interms of inodes.',
																				'How do I Display statistics of file system not of type filesystemtype in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' -k','NL Queries':['Display statistics of file system not of type filesystemtype in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system not of type filesystemtype in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --exclude-type=\'filesystemtype\' --total','NL Queries':['Display statistics of file system not of type filesystemtype along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system not of type filesystemtype along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system not of type filesystemtype along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system not of type filesystemtype along with the total disk usage?']},ignore_index=True)
'''																				
# This ends all combinations for --exclude-type


df = df.append({'Command':'df -P -a','NL Queries':['Show statistics of all file systems along with dummy ones in POSIX format.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in POSIX format?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in POSIX format, along with those of dummy file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -P --all','NL Queries':['Show statistics of all file systems along with dummy ones in POSIX format.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in POSIX format?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in POSIX format, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -P -T','NL Queries':['Display file system type and other statistics of file system in POSIX format.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in POSIX format.',
																				'How do I Display file system type and other statistics of file system in POSIX format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format?']},ignore_index=True)
'''																	
df = df.append({'Command':'df -P --print-type','NL Queries':['Display file system type and other statistics of file system in POSIX format.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in POSIX format.',
																				'How do I Display file system type and other statistics of file system in POSIX format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format?']},ignore_index=True)
'''
df = df.append({'Command':'df -P -H','NL Queries':['Display statistics of file system in POSIX format in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in powers of 1000.',
																				'How do I display statistics of file system in POSIX format in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -P --si','NL Queries':['Display statistics of file system in POSIX format in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in powers of 1000.',
																				'How do I Display statistics of file system in POSIX format in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in powers of 1000?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -P -BG','NL Queries':['Display statistics of file system in POSIX format in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Gigabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df -P -BK','NL Queries':['Display statistics of file system in POSIX format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in POSIX format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -P -BM','NL Queries':['Display file system type and other statistics of file system in POSIX format in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Megabytes.',
																				'How do I Display file system type and other statistics of file system in POSIX format in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -P -BT','NL Queries':['Display statistics of file system in POSIX format in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Terabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -P -BP','NL Queries':['Display statistics of file system in POSIX format in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Petabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -P -BY','NL Queries':['Display statistics of file system in POSIX format in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Yottabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -P -BZ','NL Queries':['Display statistics of file system in POSIX format in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Zettabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df -P -BE','NL Queries':['Display statistics of file system in POSIX format in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Exabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Exabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -P --block-size=G','NL Queries':['Display statistics of file system in POSIX format in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Gigabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df -P --block-size=E','NL Queries':['Display statistics of file system in POSIX format in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Exabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -P --block-size=K','NL Queries':['Display statistics of file system in POSIX format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Kilobytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -P --block-size=M','NL Queries':['Display statistics of file system in POSIX format in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Megabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -P --block-size=T','NL Queries':['Display statistics of file system in POSIX format in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Terabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -P --block-size=P','NL Queries':['Display statistics of file system in POSIX format in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Petabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -P --block-size=Y','NL Queries':['Display fstatistics of file system in POSIX format in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Yottabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -P --block-size=Z','NL Queries':['Display statistics of file system in POSIX format in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Zettabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Zettabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -P -t\'filesystemtype\'','NL Queries':['Display statistics of file system in POSIX format of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format of type filesystemtype.',
																				'How do I Display statistics of file system in POSIX format of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -P --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in POSIX format of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format of type filesystemtype.',
																				'How do I Display statistics of file system in POSIX format of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -P -i','NL Queries':['Display statistics of file system in POSIX format in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format interms of inodes.',
																				'How do I Display statistics of file system in POSIX format in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -P --inodes','NL Queries':['Display statistics of file system in POSIX format in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format interms of inodes.',
																				'How do I Display statistics of file system in POSIX format in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -P -x\'filesystemtype\'','NL Queries':['Display statistics of file system in POSIX format not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format not of type filesystemtype.',
																				'How do I Display statistics of file system in POSIX format not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -P --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in POSIX format not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format not of type filesystemtype.',
																				'How do I Display statistics of file system in POSIX format not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -P -k','NL Queries':['Display statistics of file system in POSIX format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in POSIX format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -P --total','NL Queries':['Display statistics of file system in POSIX format along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in POSIX format along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format along with the total disk usage?']},ignore_index=True)

# This ends all combinations for -P

'''
df = df.append({'Command':'df --portability -a','NL Queries':['Show statistics of all file systems along with dummy ones in POSIX format.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in POSIX format?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in POSIX format, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --portability --all','NL Queries':['Show statistics of all file systems along with dummy ones in POSIX format.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format, along with those of dummy file system.',
																				'How can I show the statistics of all file systems along with dummy ones in POSIX format?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the system in POSIX format, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --portability -T','NL Queries':['Display file system type and other statistics of file system in POSIX format.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in POSIX format.',
																				'How do I Display file system type and other statistics of file system in POSIX format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format?']},ignore_index=True)
																				
df = df.append({'Command':'df --portability --print-type','NL Queries':['Display file system type and other statistics of file system in POSIX format.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the system in POSIX format.',
																				'How do I Display file system type and other statistics of file system in POSIX format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format?']},ignore_index=True)

df = df.append({'Command':'df --portability -H','NL Queries':['Display statistics of file system in POSIX format in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in powers of 1000.',
																				'How do I display statistics of file system in POSIX format in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --portability --si','NL Queries':['Display statistics of file system in POSIX format in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in powers of 1000.',
																				'How do I Display statistics of file system in POSIX format in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in powers of 1000?']},ignore_index=True)
																				
df = df.append({'Command':'df --portability -BG','NL Queries':['Display statistics of file system in POSIX format in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Gigabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --portability -BK','NL Queries':['Display statistics of file system in POSIX format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in POSIX format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --portability -BM','NL Queries':['Display file system type and other statistics of file system in POSIX format in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Megabytes.',
																				'How do I Display file system type and other statistics of file system in POSIX format in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability -BT','NL Queries':['Display statistics of file system in POSIX format in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Terabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability -BP','NL Queries':['Display statistics of file system in POSIX format in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Petabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability -BY','NL Queries':['Display statistics of file system in POSIX format in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Yottabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability -BZ','NL Queries':['Display statistics of file system in POSIX format in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Zettabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability -BE','NL Queries':['Display statistics of file system in POSIX format in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Exabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability --block-size=G','NL Queries':['Display statistics of file system in POSIX format in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Gigabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability --block-size=E','NL Queries':['Display statistics of file system in POSIX format in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Exabytes.',
																				'How do I display statistics of file system in POSIX format in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability --block-size=K','NL Queries':['Display statistics of file system in POSIX format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Kilobytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --portability --block-size=M','NL Queries':['Display statistics of file system in POSIX format in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Megabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability --block-size=T','NL Queries':['Display statistics of file system in POSIX format in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Terabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability --block-size=P','NL Queries':['Display statistics of file system in POSIX format in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Petabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability --block-size=Y','NL Queries':['Display fstatistics of file system in POSIX format in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Yottabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability --block-size=Z','NL Queries':['Display statistics of file system in POSIX format in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Zettabytes.',
																				'How do I Display statistics of file system in POSIX format in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --portability -t\'filesystemtype\'','NL Queries':['Display statistics of file system in POSIX format of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format of type filesystemtype.',
																				'How do I Display statistics of file system in POSIX format of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --portability --type=\'filesystemtype\'','NL Queries':['Display statistics of file system in POSIX format of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format of type filesystemtype.',
																				'How do I Display statistics of file system in POSIX format of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --portability -i','NL Queries':['Display statistics of file system in POSIX format in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format interms of inodes.',
																				'How do I Display statistics of file system in POSIX format in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --portability --inodes','NL Queries':['Display statistics of file system in POSIX format in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format interms of inodes.',
																				'How do I Display statistics of file system in POSIX format in terms of inodes?',
																		 		'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --portability -x\'filesystemtype\'','NL Queries':['Display statistics of file system in POSIX format not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format not of type filesystemtype.',
																				'How do I Display statistics of file system in POSIX format not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --portability --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of file system in POSIX format not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format not of type filesystemtype.',
																				'How do I Display statistics of file system in POSIX format not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --portability -k','NL Queries':['Display statistics of file system in POSIX format in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format in terms of Kilobytes.',
																				'How do I Display file system type and other statistics of file system in POSIX format in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --portability --total','NL Queries':['Display statistics of file system in POSIX format along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the system in POSIX format along with the total disk usage.',
																				'How do I Display file system type and other statistics of file system in POSIX format along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the system in POSIX format along with the total disk usage?']},ignore_index=True)
'''
# This ends all combinations for --portability

df = df.append({'Command':'df --total -a','NL Queries':['Show statistics, total disk usage of all file systems and the total disk usage along with that of dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system, along with those of dummy file system.',
																				'How can I show the statistics, total disk usage of all file systems and the total disk usage along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space, total disk usage and mount points of the system, along with those of dummy file system?']},ignore_index=True)
'''																			
df = df.append({'Command':'df --total --all','NL Queries':['Show statistics, total disk usage of all file systems and the total disk usage along with that of dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system, along with those of dummy file system.',
																				'How can I show the statistics, total disk usage of all file systems and the total disk usage along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space, total disk usage and mount points of the system, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df --total -T','NL Queries':['Display file system type and other statistics, total disk usage of file system.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage,filesystem type and mount points of the system.',
																				'How do I Display file system type and other statistics, total disk usage of file system?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df --total --print-type','NL Queries':['Display file system type and other statistics, total disk usage of file system.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage,filesystem type and mount points of the system.',
																				'How do I Display file system type and other statistics, total disk usage of file system?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system?']},ignore_index=True)
'''
df = df.append({'Command':'df --total -h','NL Queries':['Display statistics, total disk usage of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in Human Readable Format.',
																				'How do I display statistics, total disk usage of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df --total --human-readable','NL Queries':['Display statistics, total disk usage of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in Human Readable Format.',
																				'How do I display statistics, total disk usage of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df --total -H','NL Queries':['Display statistics, total disk usage of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in powers of 1000.',
																				'How do I display statistics, total disk usage of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df --total --si','NL Queries':['Display statistics, total disk usage of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in powers of 1000.',
																				'How do I Display statistics, total disk usage of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in powers of 1000?']},ignore_index=True)
'''																			
df = df.append({'Command':'df --total -BG','NL Queries':['Display statistics, total disk usage of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Gigabytes.',
																				'How do I Display statistics, total disk usage of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --total -BK','NL Queries':['Display statistics, total disk usage of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Kilobytes.',
																				'How do I Display file system type and other statistics, total disk usage of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --total -BM','NL Queries':['Display file system type and other statistics, total disk usage of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Megabytes.',
																				'How do I Display file system type and other statistics, total disk usage of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --total -BT','NL Queries':['Display statistics, total disk usage of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Terabytes.',
																				'How do I Display statistics, total disk usage of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --total -BP','NL Queries':['Display statistics, total disk usage of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Petabytes.',
																				'How do I Display statistics, total disk usage of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --total -BY','NL Queries':['Display statistics, total disk usage of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Yottabytes.',
																				'How do I display statistics, total disk usage of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --total -BZ','NL Queries':['Display statistics, total disk usage of file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Zettabytes.',
																				'How do I display statistics, total disk usage of file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --total -BE','NL Queries':['Display statistics, total disk usage of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Exabytes.',
																				'How do I display statistics, total disk usage of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Exabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df --total --block-size=G','NL Queries':['Display statistics, total disk usage of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Gigabytes.',
																				'How do I display statistics, total disk usage of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df --total --block-size=E','NL Queries':['Display statistics, total disk usage of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Exabytes.',
																				'How do I display statistics, total disk usage of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --total --block-size=K','NL Queries':['Display statistics, total disk usage of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Kilobytes.',
																				'How do I Display statistics, total disk usage of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --total --block-size=M','NL Queries':['Display statistics, total disk usage of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Megabytes.',
																				'How do I Display statistics, total disk usage of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --total --block-size=T','NL Queries':['Display statistics, total disk usage of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Terabytes.',
																				'How do I Display statistics, total disk usage of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --total --block-size=P','NL Queries':['Display statistics, total disk usage of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Petabytes.',
																				'How do I Display statistics, total disk usage of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --total --block-size=Y','NL Queries':['Display fstatistics, total disk usage of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Yottabytes.',
																				'How do I Display statistics, total disk usage of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --total --block-size=Z','NL Queries':['Display statistics, total disk usage of file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Zettabytes.',
																				'How do I Display statistics, total disk usage of file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Zettabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df --total -t\'filesystemtype\'','NL Queries':['Display statistics, total disk usage of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system of type filesystemtype.',
																				'How do I Display statistics, total disk usage of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df --total --type=\'filesystemtype\'','NL Queries':['Display statistics, total disk usage of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system of type filesystemtype.',
																				'How do I Display statistics, total disk usage of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df --total -P','NL Queries':['Display statistics, total disk usage of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in POSIX Format.',
																				'How do I Display statistics, total disk usage of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df --total --portability','NL Queries':['Display statistics, total disk usage of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in POSIX Format.',
																				'How do I Display statistics, total disk usage of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df --total -i','NL Queries':['Display statistics, total disk usage of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system interms of inodes.',
																				'How do I Display statistics, total disk usage of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df --total --inodes','NL Queries':['Display statistics, total disk usage of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system interms of inodes.',
																				'How do I Display statistics, total disk usage of file system in terms of inodes?',
																		 		'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df --total -x\'filesystemtype\'','NL Queries':['Display statistics, total disk usage of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system not of type filesystemtype.',
																				'How do I Display statistics, total disk usage of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df --total --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics, total disk usage of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system not of type filesystemtype.',
																				'How do I Display statistics, total disk usage of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --total -k','NL Queries':['Display statistics, total disk usage of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space, total disk usage and mount points of the system in terms of Kilobytes.',
																				'How do I Display file system type and other statistics, total disk usage of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, total disk usage and mount points of the system in terms of Kilobytes?']},ignore_index=True)
'''
# This ends all combinations for --total

# The following are useful when non local disks are mounted. This is not included as a part of Vanilla combinations or other combinations in the beginning
df = df.append({'Command':'df -l -a','NL Queries':['Show statistics of all local file systems along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the local file system, along with those of dummy local file system.',
																				'How can I show the statistics of all local file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the local file system, along with those of dummy local file system?']},ignore_index=True)
'''																			
df = df.append({'Command':'df -l --all','NL Queries':['Show statistics of all local file systems along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the local file system, along with those of dummy local file system.',
																				'How can I show the statistics of all local file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the local file system, along with those of dummy local file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -l -T','NL Queries':['Display local file system type and other statistics of local file system.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the local file system.',
																				'How do I Display local file system type and other statistics of local file system?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -l --print-type','NL Queries':['Display local file system type and other statistics of local file system.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the local file system.',
																				'How do I Display local file system type and other statistics of local file system?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -l -h','NL Queries':['Display statistics of local file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in Human Readable Format.',
																				'How do I display statistics of local file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -l --human-readable','NL Queries':['Display statistics of local file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in Human Readable Format.',
																				'How do I display statistics of local file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -l -H','NL Queries':['Display statistics of local file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in powers of 1000.',
																				'How do I display statistics of local file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -l --si','NL Queries':['Display statistics of local file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in powers of 1000.',
																				'How do I Display statistics of local file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in powers of 1000?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -l -BG','NL Queries':['Display statistics of local file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Gigabytes.',
																				'How do I Display statistics of local file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df -l -BK','NL Queries':['Display statistics of local file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Kilobytes.',
																				'How do I Display statistics of local file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -l -BM','NL Queries':['Display local file system type and other statistics of local file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Megabytes.',
																				'How do I Display statistics of local file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -l -BT','NL Queries':['Display statistics of local file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Terabytes.',
																				'How do I Display statistics of local file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -l -BP','NL Queries':['Display statistics of local file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Petabytes.',
																				'How do I Display statistics of local file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -l -BY','NL Queries':['Display statistics of local file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Yottabytes.',
																				'How do I display statistics of local file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -l -BZ','NL Queries':['Display statistics of local file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Zettabytes.',
																				'How do I display statistics of local file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df -l -BE','NL Queries':['Display statistics of local file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Exabytes.',
																				'How do I display statistics of local file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Exabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -l --block-size=G','NL Queries':['Display statistics of local file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Gigabytes.',
																				'How do I display statistics of local file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df -l --block-size=E','NL Queries':['Display statistics of local file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Exabytes.',
																				'How do I display statistics of local file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -l --block-size=K','NL Queries':['Display statistics of local file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Kilobytes.',
																				'How do I Display statistics of local file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -l --block-size=M','NL Queries':['Display statistics of local file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Megabytes.',
																				'How do I Display statistics of local file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -l --block-size=T','NL Queries':['Display statistics of local file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Terabytes.',
																				'How do I Display statistics of local file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -l --block-size=P','NL Queries':['Display statistics of local file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Petabytes.',
																				'How do I Display statistics of local file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -l --block-size=Y','NL Queries':['Display statistics of local file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Yottabytes.',
																				'How do I Display statistics of local file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -l --block-size=Z','NL Queries':['Display statistics of local file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Zettabytes.',
																				'How do I Display statistics of local file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Zettabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -l -t\'filesystemtype\'','NL Queries':['Display statistics of local file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system of type filesystemtype.',
																				'How do I Display statistics of local file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -l --type=\'filesystemtype\'','NL Queries':['Display statistics of local file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system of type filesystemtype.',
																				'How do I Display statistics of local file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -l -P','NL Queries':['Display statistics of local file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in POSIX Format.',
																				'How do I Display statistics of local file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -l --portability','NL Queries':['Display statistics of local file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in POSIX Format.',
																				'How do I Display statistics of local file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -l -i','NL Queries':['Display statistics of local file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system interms of inodes.',
																				'How do I display statistics of local file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -l --inodes','NL Queries':['Display statistics of local file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system interms of inodes.',
																				'How do I Display statistics of local file system in terms of inodes?',
																		 		'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -l -x\'filesystemtype\'','NL Queries':['Display statistics of local file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system not of type filesystemtype.',
																				'How do I Display statistics of local file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -l --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of local file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system not of type filesystemtype.',
																				'How do I Display statistics of local file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -l -k','NL Queries':['Display statistics of local file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Kilobytes.',
																				'How do I Display statistics of local file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -l --total','NL Queries':['Display statistics of local file system along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system along with the total disk usage.',
																				'How do I Display statistics of local file system along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system along with the total disk usage?']},ignore_index=True)

# This ends all working combinations of -l

'''
df = df.append({'Command':'df --local -a','NL Queries':['Show statistics of all local file systems along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the local file system, along with those of dummy local file system.',
																				'How can I show the statistics of all local file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the local file system, along with those of dummy local file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --local --all','NL Queries':['Show statistics of all local file systems along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space and mount points of the local file system, along with those of dummy local file system.',
																				'How can I show the statistics of all local file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space and mount points of the local file system, along with those of dummy local file system?']},ignore_index=True)

df = df.append({'Command':'df --local -T','NL Queries':['Display local file system type and other statistics of local file system.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the local file system.',
																				'How do I Display local file system type and other statistics of local file system?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --local --print-type','NL Queries':['Display local file system type and other statistics of local file system.',
																				'Display device name,total blocks,total disk space,available disk space,filesystem type and mount points of the local file system.',
																				'How do I Display local file system type and other statistics of local file system?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system?']},ignore_index=True)

df = df.append({'Command':'df --local -h','NL Queries':['Display statistics of local file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in Human Readable Format.',
																				'How do I display statistics of local file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --local --human-readable','NL Queries':['Display statistics of local file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in Human Readable Format.',
																				'How do I display statistics of local file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --local -H','NL Queries':['Display statistics of local file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in powers of 1000.',
																				'How do I display statistics of local file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --local --si','NL Queries':['Display statistics of local file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in powers of 1000.',
																				'How do I Display statistics of local file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in powers of 1000?']},ignore_index=True)
																				
df = df.append({'Command':'df --local -BG','NL Queries':['Display statistics of local file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Gigabytes.',
																				'How do I Display statistics of local file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --local -BK','NL Queries':['Display statistics of local file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Kilobytes.',
																				'How do I Display statistics of local file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --local -BM','NL Queries':['Display local file system type and other statistics of local file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Megabytes.',
																				'How do I Display statistics of local file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --local -BT','NL Queries':['Display statistics of local file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Terabytes.',
																				'How do I Display statistics of local file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --local -BP','NL Queries':['Display statistics of local file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Petabytes.',
																				'How do I Display statistics of local file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --local -BY','NL Queries':['Display statistics of local file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Yottabytes.',
																				'How do I display statistics of local file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --local -BZ','NL Queries':['Display statistics of local file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Zettabytes.',
																				'How do I display statistics of local file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --local -BE','NL Queries':['Display statistics of local file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Exabytes.',
																				'How do I display statistics of local file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --local --block-size=G','NL Queries':['Display statistics of local file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Gigabytes.',
																				'How do I display statistics of local file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df --local --block-size=E','NL Queries':['Display statistics of local file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Exabytes.',
																				'How do I display statistics of local file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --local --block-size=K','NL Queries':['Display statistics of local file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Kilobytes.',
																				'How do I Display statistics of local file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --local --block-size=M','NL Queries':['Display statistics of local file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Megabytes.',
																				'How do I Display statistics of local file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --local --block-size=T','NL Queries':['Display statistics of local file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Terabytes.',
																				'How do I Display statistics of local file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --local --block-size=P','NL Queries':['Display statistics of local file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Petabytes.',
																				'How do I Display statistics of local file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --local --block-size=Y','NL Queries':['Display fstatistics of local file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Yottabytes.',
																				'How do I Display statistics of local file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --local --block-size=Z','NL Queries':['Display statistics of local file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Zettabytes.',
																				'How do I Display statistics of local file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --local -t\'filesystemtype\'','NL Queries':['Display statistics of local file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system of type filesystemtype.',
																				'How do I Display statistics of local file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --local --type=\'filesystemtype\'','NL Queries':['Display statistics of local file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system of type filesystemtype.',
																				'How do I Display statistics of local file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --local -P','NL Queries':['Display statistics of local file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in POSIX Format.',
																				'How do I Display statistics of local file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --local --portability','NL Queries':['Display statistics of local file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in POSIX Format.',
																				'How do I Display statistics of local file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --local -i','NL Queries':['Display statistics of local file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system interms of inodes.',
																				'How do I Display statistics of local file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --local --inodes','NL Queries':['Display statistics of local file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system interms of inodes.',
																				'How do I Display statistics of local file system in terms of inodes?',
																		 		'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --local -x\'filesystemtype\'','NL Queries':['Display statistics of local file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system not of type filesystemtype.',
																				'How do I Display statistics of local file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --local --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics of local file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system not of type filesystemtype.',
																				'How do I Display statistics of local file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --local -k','NL Queries':['Display statistics of local file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system in terms of Kilobytes.',
																				'How do I Display statistics of local file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --local --total','NL Queries':['Display statistics of local file system along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space and mount points of the local file system along with the total disk usage.',
																				'How do I Display statistics of local file system along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space and mount points of the local file system along with the total disk usage?']},ignore_index=True)
'''
# This ends all working combinations of --local


df = df.append({'Command':'df -T -a','NL Queries':['Show statistics and file system type of all file systems along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space, file system type and mount points of the system, along with those of dummy file system.',
																				'How can I show the statistics and file system type of all file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space, file system type and mount points of the system, along with those of dummy file system?']},ignore_index=True)
'''																			
df = df.append({'Command':'df -T --all','NL Queries':['Show statistics and file system type of all file systems along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space, file system type and mount points of the system, along with those of dummy file system.',
																				'How can I show the statistics and file system type of all file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space, file system type and mount points of the system, along with those of dummy file system?']},ignore_index=True)
'''
df = df.append({'Command':'df -T -h','NL Queries':['Display statistics and file system type of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in Human Readable Format.',
																				'How do I display statistics and file system type of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -T --human-readable','NL Queries':['Display other statistics and file system type of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in Human Readable Format.',
																				'How do I display statistics and file system type of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in Human Readable Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -T -H','NL Queries':['Display statistics and file system type of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in powers of 1000.',
																				'How do I display statistics and file system type of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in powers of 1000?']},ignore_index=True)
'''
df = df.append({'Command':'df -T --si','NL Queries':['Display other statistics and file system type of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in powers of 1000.',
																				'How do I Display other statistics and file system type of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in powers of 1000?']},ignore_index=True)
'''																				
df = df.append({'Command':'df -T -BG','NL Queries':['Display statistics and file system type of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Gigabytes.',
																				'How do I Display statistics and file system type of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df -T -BK','NL Queries':['Display statistics and file system type of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Kilobytes.',
																				'How do I Display statistics and file system type of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -T -BM','NL Queries':['Display statistics and file system type of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Megabytes.',
																				'How do I Display statistics and file system type of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -T -BT','NL Queries':['Display statistics and file system type of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Terabytes.',
																				'How do I Display statistics and file system type of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -T -BP','NL Queries':['Display statistics and file system type of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Petabytes.',
																				'How do I Display other statistics and file system type of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -T -BY','NL Queries':['Display statistics and file system type of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Yottabytes.',
																				'How do I display statistics and file system type of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -T -BZ','NL Queries':['Display statistics and file system type of file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Zettabytes.',
																				'How do I display statistics and file system type of file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df -T -BE','NL Queries':['Display statistics and file system type of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Exabytes.',
																				'How do I display statistics and file system type of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Exabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -T --block-size=G','NL Queries':['Display statistics and file system type of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Gigabytes.',
																				'How do I display statistics and file system type of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df -T --block-size=E','NL Queries':['Display statistics and file system type of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Exabytes.',
																				'How do I display statistics and file system type of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df -T --block-size=K','NL Queries':['Display statistics and file system type of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Kilobytes.',
																				'How do I Display statistics and file system type of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df -T --block-size=M','NL Queries':['Display statistics and file system type of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Megabytes.',
																				'How do I Display statistics and file system type of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df -T --block-size=T','NL Queries':['Display statistics and file system type of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Terabytes.',
																				'How do I Display statistics and file system type of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df -T --block-size=P','NL Queries':['Display statistics and file system type of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Petabytes.',
																				'How do I Display statistics and file system type of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df -T --block-size=Y','NL Queries':['Display fstatistics and file system type of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Yottabytes.',
																				'How do I Display statistics and file system type of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df -T --block-size=Z','NL Queries':['Display statistics and file system type of file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Zettabytes.',
																				'How do I Display statistics and file system type of file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Zettabytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -T -t\'filesystemtype\'','NL Queries':['Display statistics and file system type of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system of type filesystemtype.',
																				'How do I Display statistics and file system type of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -T --type=\'filesystemtype\'','NL Queries':['Display statistics and file system type of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system of type filesystemtype.',
																				'How do I Display statistics and file system type of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -T -P','NL Queries':['Display statistics and file system type of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in POSIX Format.',
																				'How do I Display statistics and file system type of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -T --portability','NL Queries':['Display statistics and file system type of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in POSIX Format.',
																				'How do I Display statistics and file system type of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in POSIX Format?']},ignore_index=True)
'''
df = df.append({'Command':'df -T -i','NL Queries':['Display statistics and file system type of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system interms of inodes.',
																				'How do I Display statistics and file system type of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -T --inodes','NL Queries':['Display statistics and file system type of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system interms of inodes.',
																				'How do I Display statistics and file system type of file system in terms of inodes?',
                                                                         		'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system interms of inodes?']},ignore_index=True)
'''
df = df.append({'Command':'df -T -x\'filesystemtype\'','NL Queries':['Display statistics and file system type of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system not of type filesystemtype.',
																				'How do I Display statistics and file system type of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system not of type filesystemtype?']},ignore_index=True)
'''
df = df.append({'Command':'df -T --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics and file system type of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system not of type filesystemtype.',
																				'How do I Display statistics and file system type of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df -T -k','NL Queries':['Display statistics and file system type of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Kilobytes.',
																				'How do I Display statistics and file system type of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Kilobytes?']},ignore_index=True)
'''
df = df.append({'Command':'df -T --total','NL Queries':['Display statistics and file system type of file system along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system along with the total disk usage.',
																				'How do I Display statistics and file system type of file system along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system along with the total disk usage?']},ignore_index=True)

# This ends all combinations for -T

'''
df = df.append({'Command':'df --print-type -a','NL Queries':['Show statistics and file system type of all file systems along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space, file system type and mount points of the system, along with those of dummy file system.',
																				'How can I show the statistics and file system type of all file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space, file system type and mount points of the system, along with those of dummy file system?']},ignore_index=True)
																				
df = df.append({'Command':'df --print-type --all','NL Queries':['Show statistics and file system type of all file systems along with dummy ones.',
																				'Show device name,total blocks,total disk space,available disk space, file system type and mount points of the system, along with those of dummy file system.',
																				'How can I show the statistics and file system type of all file systems along with dummy ones?',
																				'How can I show device name,total blocks, total disk space,available disk space, file system type and mount points of the system, along with those of dummy file system?']},ignore_index=True)

df = df.append({'Command':'df --print-type -h','NL Queries':['Display statistics and file system type of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in Human Readable Format.',
																				'How do I display statistics and file system type of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --print-type --human-readable','NL Queries':['Display other statistics and file system type of file system in Human Readable Format.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in Human Readable Format.',
																				'How do I display statistics and file system type of file system in Human Readable Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in Human Readable Format?']},ignore_index=True)

df = df.append({'Command':'df --print-type -H','NL Queries':['Display statistics and file system type of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in powers of 1000.',
																				'How do I display statistics and file system type of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in powers of 1000?']},ignore_index=True)

df = df.append({'Command':'df --print-type --si','NL Queries':['Display other statistics and file system type of file system in powers of 1000.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in powers of 1000.',
																				'How do I Display other statistics and file system type of file system in powers of 1000?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in powers of 1000?']},ignore_index=True)
																				
df = df.append({'Command':'df --print-type -BG','NL Queries':['Display statistics and file system type of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Gigabytes.',
																				'How do I Display statistics and file system type of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Gigabytes?']},ignore_index=True)
																				
df = df.append({'Command':'df --print-type -BK','NL Queries':['Display statistics and file system type of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Kilobytes.',
																				'How do I Display statistics and file system type of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type -BM','NL Queries':['Display statistics and file system type of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Megabytes.',
																				'How do I Display statistics and file system type of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type -BT','NL Queries':['Display statistics and file system type of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Terabytes.',
																				'How do I Display statistics and file system type of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type -BP','NL Queries':['Display statistics and file system type of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Petabytes.',
																				'How do I Display other statistics and file system type of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type -BY','NL Queries':['Display statistics and file system type of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Yottabytes.',
																				'How do I display statistics and file system type of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type -BZ','NL Queries':['Display statistics and file system type of file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Zettabytes.',
																				'How do I display statistics and file system type of file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type -BE','NL Queries':['Display statistics and file system type of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Exabytes.',
																				'How do I display statistics and file system type of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --block-size=G','NL Queries':['Display statistics and file system type of file system in terms of Gigabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Gigabytes.',
																				'How do I display statistics and file system type of file system in terms of Gigabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Gigabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --block-size=E','NL Queries':['Display statistics and file system type of file system in terms of Exabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Exabytes.',
																				'How do I display statistics and file system type of file system in terms of Exabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Exabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --block-size=K','NL Queries':['Display statistics and file system type of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Kilobytes.',
																				'How do I Display statistics and file system type of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --block-size=M','NL Queries':['Display statistics and file system type of file system in terms of Megabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Megabytes.',
																				'How do I Display statistics and file system type of file system in terms of Megabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Megabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --block-size=T','NL Queries':['Display statistics and file system type of file system in terms of Terabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Terabytes.',
																				'How do I Display statistics and file system type of file system in terms of Terabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Terabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --block-size=P','NL Queries':['Display statistics and file system type of file system in terms of Petabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Petabytes.',
																				'How do I Display statistics and file system type of file system in terms of Petabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Petabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --block-size=Y','NL Queries':['Display fstatistics and file system type of file system in terms of Yottabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Yottabytes.',
																				'How do I Display statistics and file system type of file system in terms of Yottabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Yottabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --block-size=Z','NL Queries':['Display statistics and file system type of file system in terms of Zettabytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Zettabytes.',
																				'How do I Display statistics and file system type of file system in terms of Zettabytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Zettabytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type -t\'filesystemtype\'','NL Queries':['Display statistics and file system type of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system of type filesystemtype.',
																				'How do I Display statistics and file system type of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --print-type --type=\'filesystemtype\'','NL Queries':['Display statistics and file system type of file system of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system of type filesystemtype.',
																				'How do I Display statistics and file system type of file system of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --print-type -P','NL Queries':['Display statistics and file system type of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in POSIX Format.',
																				'How do I Display statistics and file system type of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --print-type --portability','NL Queries':['Display statistics and file system type of file system in POSIX Format.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in POSIX Format.',
																				'How do I Display statistics and file system type of file system in POSIX Format?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in POSIX Format?']},ignore_index=True)

df = df.append({'Command':'df --print-type -i','NL Queries':['Display statistics and file system type of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system interms of inodes.',
																				'How do I Display statistics and file system type of file system in terms of inodes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --inodes','NL Queries':['Display statistics and file system type of file system in terms of inodes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system interms of inodes.',
																				'How do I Display statistics and file system type of file system in terms of inodes?',
                                                                         		'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system interms of inodes?']},ignore_index=True)

df = df.append({'Command':'df --print-type -x\'filesystemtype\'','NL Queries':['Display statistics and file system type of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system not of type filesystemtype.',
																				'How do I Display statistics and file system type of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --print-type --exclude-type=\'filesystemtype\'','NL Queries':['Display statistics and file system type of file system not of type filesystemtype.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system not of type filesystemtype.',
																				'How do I Display statistics and file system type of file system not of type filesystemtype?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system not of type filesystemtype?']},ignore_index=True)

df = df.append({'Command':'df --print-type -k','NL Queries':['Display statistics and file system type of file system in terms of Kilobytes.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system in terms of Kilobytes.',
																				'How do I Display statistics and file system type of file system in terms of Kilobytes?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system in terms of Kilobytes?']},ignore_index=True)

df = df.append({'Command':'df --print-type --total','NL Queries':['Display statistics and file system type of file system along with the total disk usage.',
																				'Display device name,total blocks,total disk space,available disk space, file system type and mount points of the system along with the total disk usage.',
																				'How do I Display statistics and file system type of file system along with the total disk usage?',
																				'How do I display device name, total blocks, total disk space, available disk space, file system type and mount points of the system along with the total disk usage?']},ignore_index=True)
'''
# This ends all working combinations for --print-type

print (df.shape)