import pandas as pd 

free = pd.DataFrame(columns = ['Command','NL Queries'])

free = free.append({'Command':'free','NL Queries':['How much free memory do I have on my disk?',
'Show the amount of free memory on my computer.',
'Get statistics of available memory.']},ignore_index=True)

free = free.append({'Command':'free -m','NL Queries':['Show the amount of memory in Megabytes.',
'Display free RAM memory in MB.',
'How do I check the statistics of available RAM in MB?']},ignore_index=True)

free = free.append({'Command':'free -b','NL Queries':['How much free memory, in bytes, do I have on my disk?',
'Show the amount of free memory on my computer in bytes.',
'Get statistics of available memory in bytes.',
'Display free RAM memory in bytes.']},ignore_index=True)

free = free.append({'Command':'free -k','NL Queries':['How much free memory, in kilobytes, do I have on my disk?',
'Show the amount of free memory on my computer in kilobytes.',
'Get statistics of available memory in kilobytes.',
'Display free RAM memory in KB.']},ignore_index=True)

free = free.append({'Command':'free -m','NL Queries':['How much free memory, in megabytes, do I have on my disk?',
'Show the amount of free memory on my computer in megabytes.',
'Get statistics of available memory in megabytes.',
'Display free RAM memory in MB.']},ignore_index=True)

free = free.append({'Command':'free -g','NL Queries':['How much free memory, in gigabytes, do I have on my disk?',
'Show the amount of free memory on my computer in gigabytes.',
'Get statistics of available memory in gigabytes.',
'Display free RAM memory in GB.']},ignore_index=True)

free = free.append({'Command':'free --tera','NL Queries':['How much free memory, in terabytes, do I have on my disk?',
'Show the amount of free memory on my computer in terabytes.',
'Get statistics of available memory in terabytes.',
'Display free RAM memory in TB.']},ignore_index=True)

free = free.append({'Command':'free -h','NL Queries':['How much free memory, in human readable format, do I have on my disk?',
'Show the amount of free memory on my computer in human readable format.',
'Get statistics of available memory in human readable format.',
'Display free RAM memory in human readable format.']},ignore_index=True)

free = free.append({'Command':'free --si','NL Queries':['How much free memory do I have on my disk? Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer. Divide by 1000 not 1024.',
'Get statistics of available memory. Use powers of 1000 not 1024.',
'Display free RAM memory. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics.',
'Show the amount of free memory on my computer with detailed low and high memory statistics.',
'Get statistics of available memory including low and high memory details.',
'Display free RAM memory. Also include low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -o','NL Queries':['How much free memory do I have on my disk? Give the result in old format.',
'Show the amount of free memory on my computer without -/+buffers/cache line.',
'Get statistics of available memory without -/+buffers/cache line.',
'Display free RAM memory in old format.']},ignore_index=True)

free = free.append({'Command':'free -t','NL Queries':['How much free memory do I have on my disk? Show total of RAM and Swap.',
'Show the amount of free memory on my computer with total of RAM plus Swap.',
'Get statistics of available memory including total of RAM and Swap.',
'Display free RAM memory. Also include total of RAM plus Swap.']},ignore_index=True)

free = free.append({'Command':'free -s 1','NL Queries':['Display usage of RAM every 1 second.',
'How do I check the usage of my RAM every second?',
'Get statistics of available memory every 1 second.',
'Display free RAM memory every 1 second.']},ignore_index=True)

free = free.append({'Command':'free -c 5','NL Queries':['Display usage of RAM every 1 second for 5 seconds.',
'How do I check the usage of my RAM every second for 5 seconds?',
'Get statistics of available memory for the next 5 seconds.',
'Display free RAM memory for the next 5 seconds.']},ignore_index=True)

######
free = free.append({'Command':'free -b --si','NL Queries':['How much free memory, in bytes, do I have on my disk? Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in bytes. Divide by 1000 not 1024.',
'Get statistics of available memory in bytes. Use powers of 1000 not 1024.',
'Display free RAM memory in bytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -k --si','NL Queries':['How much free memory, in kilobytes, do I have on my disk? Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in kilobytes. Divide by 1000 not 1024.',
'Get statistics of available memory in kilobytes. Use powers of 1000 not 1024.',
'Display free RAM memory in KB. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -m --si','NL Queries':['How much free memory, in megabytes, do I have on my disk? Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in megabytes. Divide by 1000 not 1024.',
'Get statistics of available memory in megabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in MB. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -g --si','NL Queries':['How much free memory, in gigabytes, do I have on my disk? Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in gigabytes. Divide by 1000 not 1024.',
'Get statistics of available memory in gigabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in GB. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free --tera --si','NL Queries':['How much free memory, in terabytes, do I have on my disk? Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in terabytes. Divide by 1000 not 1024.',
'Get statistics of available memory in terabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in TB. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -h --si','NL Queries':['How much free memory, in human readable format, do I have on my disk? Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in human readable format. Divide by 1000 not 1024.',
'Get statistics of available memory in human readable format. Use powers of 1000 not 1024.',
'Display free RAM memory in human readable format. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l --si','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics.  Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o --si','NL Queries':['How much free memory do I have on my disk? Give the result in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -t --si','NL Queries':['How much free memory do I have on my disk? Show total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with total of RAM plus Swap. Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include total of RAM plus Swap. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -s 1 --si','NL Queries':['Display usage of RAM every 1 second. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second? Divide by 1000 not 1024.',
'Get statistics of available memory every 1 second. Use powers of 1000 not 1024.',
'Display free RAM memory every 1 second. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -c 5 --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory for the next 5 seconds. Divide by 1000 not 1024.']},ignore_index=True)

####
free = free.append({'Command':'free -l -b','NL Queries':['How much free memory do I have on my disk in bytes? Show detailed low and high memory statistics.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in bytes.',
'Get statistics of available memory including low and high memory details in bytes.',
'Display free RAM memory in bytes. Also include low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -k','NL Queries':['How much free memory do I have on my disk in kilobytes? Show detailed low and high memory statistics.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in kilobytes.',
'Get statistics of available memory including low and high memory details in kilobytes.',
'Display free RAM memory in kilobytes. Also include low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -m','NL Queries':['How much free memory do I have on my disk in megabytes? Show detailed low and high memory statistics.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in megabytes.',
'Get statistics of available memory including low and high memory details in megabytes.',
'Display free RAM memory in megabytes. Also include low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -g','NL Queries':['How much free memory do I have on my disk in gigabytes? Show detailed low and high memory statistics.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in gigabytes.',
'Get statistics of available memory including low and high memory details in gigabytes.',
'Display free RAM memory in gigabytes. Also include low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l --tera','NL Queries':['How much free memory do I have on my disk in terabytes? Show detailed low and high memory statistics.',
'Show the amount of free memory on my computer with detailed low and high memory statistics  in terabytes.',
'Get statistics of available memory including low and high memory details  in terabytes.',
'Display free RAM memory  in terabytes. Also include low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -h','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics in human readable format.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in human readable format.',
'Get statistics of available memory including low and high memory details in human readable format.',
'Display free RAM memory in human readable format. Also include low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -o','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics in old format.',
'Show the amount of free memory on my computer with detailed low and high memory statistics without -/+buffers/cache line.',
'Get statistics of available memory including low and high memory details without -/+buffers/cache line.',
'Display free RAM memory in old format. Also include low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -t','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics and total of RAM and Swap.',
'Show the amount of free memory on my computer with detailed low and high memory statistics and total of RAM plus Swap.',
'Get statistics of available memory including low and high memory details and total of RAM and Swap.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics.',
'Get statistics of available memory including low and high memory details every 1 second.',
'Display free RAM memory every 1 second. Results should inlcude detailed low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics.',
'How do I check the usage of my RAM every second including low and high memory statistics for 5 seconds?',
'Get statistics of available memory including low and high memory details for the next 5 seconds.',
'Display free RAM memory for the next 5 seconds. Also include low and high memory statistics.']},ignore_index=True)

####
free = free.append({'Command':'free -o -b','NL Queries':['How much free memory do I have on my disk in bytes? Give the result in old format.',
'Show the amount of free memory on my computer in bytes, without -/+buffers/cache line.',
'Get statistics of available memory in bytes, without -/+buffers/cache line.',
'Display free RAM memory in old format. Give the output in bytes.']},ignore_index=True)

free = free.append({'Command':'free -o -k','NL Queries':['How much free memory do I have on my disk in kilobytes? Give the result in old format.',
'Show the amount of free memory on my computer in kilobytes, without -/+buffers/cache line.',
'Get statistics of available memory in kilobytes, without -/+buffers/cache line.',
'Display free RAM memory in old format. Give the output in kilobytes.']},ignore_index=True)

free = free.append({'Command':'free -o -m','NL Queries':['How much free memory do I have on my disk in megabytes? Give the result in old format.',
'Show the amount of free memory on my computer in megabytes, without -/+buffers/cache line.',
'Get statistics of available memory in megabytes, without -/+buffers/cache line.',
'Display free RAM memory in old format. Give the output in megabytes.']},ignore_index=True)

free = free.append({'Command':'free -o -g','NL Queries':['How much free memory do I have on my disk in gigabytes? Give the result in old format.',
'Show the amount of free memory on my computer in gigabytes, without -/+buffers/cache line.',
'Get statistics of available memory in gigabytes, without -/+buffers/cache line.',
'Display free RAM memory in old format. Give the output in gigabytes.']},ignore_index=True)

free = free.append({'Command':'free -o --tera','NL Queries':['How much free memory do I have on my disk in terabytes? Give the result in old format.',
'Show the amount of free memory on my computer in terabytes, without -/+buffers/cache line.',
'Get statistics of available memory in terabytes, without -/+buffers/cache line.',
'Display free RAM memory in old format. Give the output in terabytes.']},ignore_index=True)

free = free.append({'Command':'free -o -h','NL Queries':['How much free memory do I have on my disk? Give the result in old format with human readable numbers.',
'Show the amount of free memory on my computer in human readable format, without -/+buffers/cache line.',
'Get statistics of available memory in human readable format, without -/+buffers/cache line.',
'Display free RAM memory in old format with human readable numbers.']},ignore_index=True)

free = free.append({'Command':'free -o -t','NL Queries':['How much free memory do I have on my disk? Show total of RAM and Swap in old format.',
'Show the amount of free memory on my computer with total of RAM plus Swap and without -/+buffers/cache line.',
'Get statistics of available memory including total of RAM and Swap but excluding -/+buffers/cache line.',
'Display free RAM memory in old format. Also include total of RAM plus Swap.']},ignore_index=True)

free = free.append({'Command':'free -o -s 1','NL Queries':['Display usage of RAM in old format every 1 second.',
'How do I check the usage of my RAM without -/+buffers/cache line every second?',
'Get statistics of available memory without -/+buffers/cache line every 1 second.',
'Display free RAM memory every in old format 1 second.']},ignore_index=True)

free = free.append({'Command':'free -o -c 5','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Output should be in old format.',
'How do I check the usage of my RAM without -/+buffers/cache line, every second for 5 seconds?',
'Get statistics of available memory without -/+buffers/cache line for the next 5 seconds.',
'Display free RAM memory for the next 5 seconds. The result should be in old format.']},ignore_index=True)

####
free = free.append({'Command':'free -t -b','NL Queries':['How much free memory, in bytes, do I have on my disk? Show total of RAM and Swap.',
'Show the amount of free memory on my computer with total of RAM plus Swap in bytes.',
'Get statistics of available memory including total of RAM and Swap in bytes.',
'Display free RAM memory in bytes. Also include total of RAM plus Swap.']},ignore_index=True)

free = free.append({'Command':'free -t -k','NL Queries':['How much free memory, in kilobytes, do I have on my disk? Show total of RAM and Swap.',
'Show the amount of free memory on my computer with total of RAM plus Swap in kilobytes.',
'Get statistics of available memory including total of RAM and Swap in kilobytes.',
'Display free RAM memory in KB. Also include total of RAM plus Swap.']},ignore_index=True)

free = free.append({'Command':'free -t -m','NL Queries':['How much free memory, in megabytes, do I have on my disk? Show total of RAM and Swap.',
'Show the amount of free memory on my computer with total of RAM plus Swap in megabytes.',
'Get statistics of available memory including total of RAM and Swap in megabytes.',
'Display free RAM memory. Also include total of RAM plus Swap in MB.']},ignore_index=True)

free = free.append({'Command':'free -t -g','NL Queries':['How much free memory, in gigabytes, do I have on my disk? Show total of RAM and Swap.',
'Show the amount of free memory on my computer with total of RAM plus Swap in gigabytes.',
'Get statistics of available memory including total of RAM and Swap in gigabytes.',
'Display free RAM memory in GB. Also include total of RAM plus Swap.']},ignore_index=True)

free = free.append({'Command':'free -t --tera','NL Queries':['How much free memory, in terabytes, do I have on my disk? Show total of RAM and Swap.',
'Show the amount of free memory on my computer with total of RAM plus Swap in terabytes.',
'Get statistics of available memory including total of RAM and Swap in terabytes.',
'Display free RAM memory in TB. Also include total of RAM plus Swap.']},ignore_index=True)

free = free.append({'Command':'free -t -h','NL Queries':['How much free memory do I have on my disk? Show total of RAM and Swap in human readable format.',
'Show the amount of free memory on my computer with total of RAM plus Swap in human readable format.',
'Get statistics of available memory including total of RAM and Swap in human readable format.',
'Display free RAM memory in human readable format. Also include total of RAM plus Swap.']},ignore_index=True)

free = free.append({'Command':'free -t -s 1','NL Queries':['Display usage of RAM every 1 second. Also show total of RAM and Swap.',
'How do I check the usage of my RAM including total of RAM plus Swap every second?',
'Get statistics of available memory including total of RAM and Swap every 1 second.',
'Display free RAM memory including total of RAM plus Swap every 1 second.']},ignore_index=True)

free = free.append({'Command':'free -t -c 5','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Also show total of RAM and Swap.',
'How do I check the usage of my RAM including total of RAM plus Swap every second for 5 seconds?',
'Get statistics of available memory including total of RAM and Swap for the next 5 seconds.',
'Display free RAM memory including total of RAM plus Swap for the next 5 seconds.']},ignore_index=True)

#####
free = free.append({'Command':'free -s 1 -b','NL Queries':['Display usage of RAM every 1 second in bytes.',
'How do I check the usage of my RAM every second in bytes?',
'Get statistics of available memory in bytes every 1 second.',
'Display free RAM memory in bytes every 1 second.']},ignore_index=True)

free = free.append({'Command':'free -s 1 -k','NL Queries':['Display usage of RAM every 1 second in kilobytes.',
'How do I check the usage of my RAM every second in kilobytes?',
'Get statistics of available memory in kilobytes every 1 second.',
'Display free RAM memory in kilobytes every 1 second.']},ignore_index=True)

free = free.append({'Command':'free -s 1 -m','NL Queries':['Display usage of RAM every 1 second in megabytes.',
'How do I check the usage of my RAM every second in megabytes?',
'Get statistics of available memory in megabytes every 1 second.',
'Display free RAM memory in megabytes every 1 second.']},ignore_index=True)

free = free.append({'Command':'free -s 1 -g','NL Queries':['Display usage of RAM every 1 second in gigabytes.',
'How do I check the usage of my RAM every second in gigabytes?',
'Get statistics of available memory in gigabytes every 1 second.',
'Display free RAM memory in gigabytes every 1 second.']},ignore_index=True)

free = free.append({'Command':'free -s 1 --tera','NL Queries':['Display usage of RAM every 1 second in terabytes.',
'How do I check the usage of my RAM every second in terabytes?',
'Get statistics of available memory in terabytes every 1 second.',
'Display free RAM memory in terabytes every 1 second.']},ignore_index=True)

free = free.append({'Command':'free -s 1 -h','NL Queries':['Display usage of RAM every 1 second in human readable format.',
'How do I check the usage of my RAM every second in human readable format?',
'Get statistics of available memory every 1 second in human readable format.',
'Display free RAM memory every 1 second in human readable format.']},ignore_index=True)

####
free = free.append({'Command':'free -c 5 -b','NL Queries':['Display usage of RAM every 1 second for 5 seconds in bytes.',
'How do I check the usage of my RAM every second for 5 seconds in bytes?',
'Get statistics of available memory in bytes for the next 5 seconds.',
'Display free RAM memory in bytes for the next 5 seconds.']},ignore_index=True)

free = free.append({'Command':'free -c 5 -k','NL Queries':['Display usage of RAM every 1 second for 5 seconds in kilobytes.',
'How do I check the usage of my RAM every second for 5 seconds in kilobytes?',
'Get statistics of available memory in kilobytes for the next 5 seconds.',
'Display free RAM memory in kilobytes for the next 5 seconds.']},ignore_index=True)

free = free.append({'Command':'free -c 5 -m','NL Queries':['Display usage of RAM every 1 second for 5 seconds in megabytes.',
'How do I check the usage of my RAM every second for 5 seconds in megabytes?',
'Get statistics of available memory in megabytes for the next 5 seconds.',
'Display free RAM memory in megabytes for the next 5 seconds.']},ignore_index=True)

free = free.append({'Command':'free -c 5 -g','NL Queries':['Display usage of RAM every 1 second for 5 seconds in gigabytes.',
'How do I check the usage of my RAM every second for 5 seconds in gigabytes?',
'Get statistics of available memory in gigabytes for the next 5 seconds.',
'Display free RAM memory in gigabytes for the next 5 seconds.']},ignore_index=True)

free = free.append({'Command':'free -c 5 --tera','NL Queries':['Display usage of RAM every 1 second for 5 seconds in terabytes.',
'How do I check the usage of my RAM every second for 5 seconds in terabytes?',
'Get statistics of available memory in terabytes for the next 5 seconds.',
'Display free RAM memory in terabytes for the next 5 seconds.']},ignore_index=True)

free = free.append({'Command':'free -c 5 -h','NL Queries':['Display usage of RAM every 1 second for 5 seconds in human readable format.',
'How do I check the usage of my RAM in human readable format every second for 5 seconds?',
'Get statistics of available memory for the next 5 seconds in human readable format.',
'Display free RAM memory in human readable format for the next 5 seconds.']},ignore_index=True)

#### 
free = free.append({'Command':'free -l -b --si','NL Queries':['How much free memory do I have on my disk in bytes? Show detailed low and high memory statistics. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in bytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details in bytes. Use powers of 1000 not 1024.',
'Display free RAM memory in bytes. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -k --si','NL Queries':['How much free memory do I have on my disk in kilobytes? Show detailed low and high memory statistics. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in kilobytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details in kilobytes. Use powers of 1000 not 1024.',
'Display free RAM memory in kilobytes. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -m --si','NL Queries':['How much free memory do I have on my disk in megabytes? Show detailed low and high memory statistics. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in megabytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details in megabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in megabytes. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -g --si','NL Queries':['How much free memory do I have on my disk in gigabytes? Show detailed low and high memory statistics. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in gigabytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details in gigabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in gigabytes. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l --tera --si','NL Queries':['How much free memory do I have on my disk in terabytes? Show detailed low and high memory statistics. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics  in terabytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details  in terabytes. Use powers of 1000 not 1024.',
'Display free RAM memory  in terabytes. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -h --si','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics in human readable format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics in human readable format. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details in human readable format. Use powers of 1000 not 1024.',
'Display free RAM memory in human readable format. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -o --si','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -t --si','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics and total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics and total of RAM plus Swap. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details and total of RAM and Swap. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 --si','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details every 1 second. Use powers of 1000 not 1024.',
'Display free RAM memory every 1 second. Results should inlcude detailed low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second including low and high memory statistics for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory for the next 5 seconds. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o -b --si','NL Queries':['How much free memory do I have on my disk in bytes? Give the result in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in bytes, without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in bytes, without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Give the output in bytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o -k --si','NL Queries':['How much free memory do I have on my disk in kilobytes? Give the result in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in kilobytes, without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in kilobytes, without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Give the output in kilobytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o -m --si','NL Queries':['How much free memory do I have on my disk in megabytes? Give the result in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in megabytes, without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in megabytes, without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Give the output in megabytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o -g --si','NL Queries':['How much free memory do I have on my disk in gigabytes? Give the result in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in gigabytes, without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in gigabytes, without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Give the output in gigabytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o --tera --si','NL Queries':['How much free memory do I have on my disk in terabytes? Give the result in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in terabytes, without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in terabytes, without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Give the output in terabytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o -h --si','NL Queries':['How much free memory do I have on my disk? Give the result in old format with human readable numbers. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in human readable format, without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in human readable format, without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format with human readable numbers. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o -t --si','NL Queries':['How much free memory do I have on my disk? Show total of RAM and Swap in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with total of RAM plus Swap and without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap but excluding -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Also include total of RAM plus Swap. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o -s 1 --si','NL Queries':['Display usage of RAM in old format every 1 second. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM without -/+buffers/cache line every second? Divide by 1000 not 1024.',
'Get statistics of available memory without -/+buffers/cache line every 1 second. Use powers of 1000 not 1024.',
'Display free RAM memory every in old format 1 second. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -o -c 5 --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Output should be in old format. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM without -/+buffers/cache line, every second for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory without -/+buffers/cache line for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory for the next 5 seconds. The result should be in old format. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -t -b --si','NL Queries':['How much free memory, in bytes, do I have on my disk? Show total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with total of RAM plus Swap in bytes. Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap in bytes. Use powers of 1000 not 1024.',
'Display free RAM memory in bytes. Also include total of RAM plus Swap. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -t -k --si','NL Queries':['How much free memory, in kilobytes, do I have on my disk? Show total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with total of RAM plus Swap in kilobytes. Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap in kilobytes. Use powers of 1000 not 1024.',
'Display free RAM memory in KB. Also include total of RAM plus Swap. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -t -m --si','NL Queries':['How much free memory, in megabytes, do I have on my disk? Show total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with total of RAM plus Swap in megabytes. Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap in megabytes. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include total of RAM plus Swap in MB. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -t -g --si','NL Queries':['How much free memory, in gigabytes, do I have on my disk? Show total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with total of RAM plus Swap in gigabytes. Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap in gigabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in GB. Also include total of RAM plus Swap. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -t --tera --si','NL Queries':['How much free memory, in terabytes, do I have on my disk? Show total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with total of RAM plus Swap in terabytes. Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap in terabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in TB. Also include total of RAM plus Swap. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -t -h --si','NL Queries':['How much free memory do I have on my disk? Show total of RAM and Swap in human readable format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with total of RAM plus Swap in human readable format. Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap in human readable format. Use powers of 1000 not 1024.',
'Display free RAM memory in human readable format. Also include total of RAM plus Swap. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -t -s 1 --si','NL Queries':['Display usage of RAM every 1 second. Also show total of RAM and Swap. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM including total of RAM plus Swap every second? Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap every 1 second. Use powers of 1000 not 1024.',
'Display free RAM memory including total of RAM plus Swap every 1 second. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -t -c 5 --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Also show total of RAM and Swap. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM including total of RAM plus Swap every second for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory including total of RAM and Swap for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory including total of RAM plus Swap for the next 5 seconds. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -s 1 -b --si','NL Queries':['Display usage of RAM every 1 second in bytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second in bytes? Divide by 1000 not 1024.',
'Get statistics of available memory in bytes every 1 second. Use powers of 1000 not 1024.',
'Display free RAM memory in bytes every 1 second. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -s 1 -k --si','NL Queries':['Display usage of RAM every 1 second in kilobytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second in kilobytes? Divide by 1000 not 1024.',
'Get statistics of available memory in kilobytes every 1 second. Use powers of 1000 not 1024.',
'Display free RAM memory in kilobytes every 1 second. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -s 1 -m --si','NL Queries':['Display usage of RAM every 1 second in megabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second in megabytes? Divide by 1000 not 1024.',
'Get statistics of available memory in megabytes every 1 second. Use powers of 1000 not 1024.',
'Display free RAM memory in megabytes every 1 second. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -s 1 -g --si','NL Queries':['Display usage of RAM every 1 second in gigabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second in gigabytes? Divide by 1000 not 1024.',
'Get statistics of available memory in gigabytes every 1 second. Use powers of 1000 not 1024.',
'Display free RAM memory in gigabytes every 1 second. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -s 1 --tera --si','NL Queries':['Display usage of RAM every 1 second in terabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second in terabytes? Divide by 1000 not 1024.',
'Get statistics of available memory in terabytes every 1 second. Use powers of 1000 not 1024.',
'Display free RAM memory in terabytes every 1 second. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -s 1 -h --si','NL Queries':['Display usage of RAM every 1 second in human readable format. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second in human readable format? Divide by 1000 not 1024.',
'Get statistics of available memory every 1 second in human readable format. Use powers of 1000 not 1024.',
'Display free RAM memory every 1 second in human readable format. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -c 5 -b --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds in bytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second for 5 seconds in bytes? Divide by 1000 not 1024.',
'Get statistics of available memory in bytes for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in bytes for the next 5 seconds. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -c 5 -k --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds in kilobytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second for 5 seconds in kilobytes? Divide by 1000 not 1024.',
'Get statistics of available memory in kilobytes for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in kilobytes for the next 5 seconds. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -c 5 -m --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds in megabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second for 5 seconds in megabytes? Divide by 1000 not 1024.',
'Get statistics of available memory in megabytes for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in megabytes for the next 5 seconds. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -c 5 -g --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds in gigabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second for 5 seconds in gigabytes? Divide by 1000 not 1024.',
'Get statistics of available memory in gigabytes for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in gigabytes for the next 5 seconds. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -c 5 --tera --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds in terabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second for 5 seconds in terabytes? Divide by 1000 not 1024.',
'Get statistics of available memory in terabytes for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in terabytes for the next 5 seconds. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -c 5 -h --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds in human readable format. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM in human readable format every second for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory for the next 5 seconds in human readable format. Use powers of 1000 not 1024.',
'Display free RAM memory in human readable format for the next 5 seconds. Divide by 1000 not 1024.']},ignore_index=True)

#### 
free = free.append({'Command':'free -l -o -b','NL Queries':['How much free memory do I have on my disk in bytes? Show detailed low and high memory statistics in old format.',
'Show the amount of free memory in bytes on my computer with detailed low and high memory statistics without -/+buffers/cache line.',
'Get statistics of available memory in bytes including low and high memory details without -/+buffers/cache line.',
'Display free RAM memory in old format. Also include low and high memory statistics in bytes.']},ignore_index=True)

free = free.append({'Command':'free -l -t -b','NL Queries':['How much free memory do I have on my disk in bytes? Show detailed low and high memory statistics and total of RAM and Swap.',
'Show the amount of free memory in bytes on my computer with detailed low and high memory statistics and total of RAM plus Swap.',
'Get statistics of available memory in bytes including low and high memory details and total of RAM and Swap.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in bytes.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -b','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in bytes.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in bytes.',
'Get statistics of available memory including low and high memory details every 1 second in bytes.',
'Display free RAM memory in bytes every 1 second. Results should inlcude detailed low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -b','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in bytes.',
'How do I check the usage of my RAM in bytes every second including low and high memory statistics for 5 seconds?',
'Get statistics of available memory in bytes including low and high memory details for the next 5 seconds.',
'Display free RAM memory in bytes for the next 5 seconds. Also include low and high memory statistics.']},ignore_index=True)

#### 
free = free.append({'Command':'free -l -o -k','NL Queries':['How much free memory do I have on my disk in kilobytes? Show detailed low and high memory statistics in old format.',
'Show the amount of free memory in kilobytes on my computer with detailed low and high memory statistics without -/+buffers/cache line.',
'Get statistics of available memory in kilobytes including low and high memory details without -/+buffers/cache line.',
'Display free RAM memory in old format. Also include low and high memory statistics in kilobytes.']},ignore_index=True)

free = free.append({'Command':'free -l -t -k','NL Queries':['How much free memory do I have on my disk in kilobytes? Show detailed low and high memory statistics and total of RAM and Swap.',
'Show the amount of free memory in kilobytes on my computer with detailed low and high memory statistics and total of RAM plus Swap.',
'Get statistics of available memory in kilobytes including low and high memory details and total of RAM and Swap.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in kilobytes.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -k','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in kilobytes.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in kilobytes.',
'Get statistics of available memory including low and high memory details every 1 second in kilobytes.',
'Display free RAM memory in kilobytes every 1 second. Results should include detailed low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -k','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in kilobytes.',
'How do I check the usage of my RAM in kilobytes every second including low and high memory statistics for 5 seconds?',
'Get statistics of available memory in kilobytes including low and high memory details for the next 5 seconds.',
'Display free RAM memory in kilobytes for the next 5 seconds. Also include low and high memory statistics.']},ignore_index=True)

### 
free = free.append({'Command':'free -l -o -m','NL Queries':['How much free memory do I have on my disk in megabytes? Show detailed low and high memory statistics in old format.',
'Show the amount of free memory in megabytes on my computer with detailed low and high memory statistics without -/+buffers/cache line.',
'Get statistics of available memory in megabytes including low and high memory details without -/+buffers/cache line.',
'Display free RAM memory in old format. Also include low and high memory statistics in megabytes.']},ignore_index=True)

free = free.append({'Command':'free -l -t -m','NL Queries':['How much free memory do I have on my disk in megabytes? Show detailed low and high memory statistics and total of RAM and Swap.',
'Show the amount of free memory in megabytes on my computer with detailed low and high memory statistics and total of RAM plus Swap.',
'Get statistics of available memory in megabytes including low and high memory details and total of RAM and Swap.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in megabytes.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -m','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in megabytes.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in megabytes.',
'Get statistics of available memory including low and high memory details every 1 second in megabytes.',
'Display free RAM memory in megabytes every 1 second. Results should include detailed low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -m','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in megabytes.',
'How do I check the usage of my RAM in megabytes every second including low and high memory statistics for 5 seconds?',
'Get statistics of available memory in megabytes including low and high memory details for the next 5 seconds.',
'Display free RAM memory in megabytes for the next 5 seconds. Also include low and high memory statistics.']},ignore_index=True)

### 
free = free.append({'Command':'free -l -o -g','NL Queries':['How much free memory do I have on my disk in gigabytes? Show detailed low and high memory statistics in old format.',
'Show the amount of free memory in gigabytes on my computer with detailed low and high memory statistics without -/+buffers/cache line.',
'Get statistics of available memory in gigabytes including low and high memory details without -/+buffers/cache line.',
'Display free RAM memory in old format. Also include low and high memory statistics in gigabytes.']},ignore_index=True)

free = free.append({'Command':'free -l -t -g','NL Queries':['How much free memory do I have on my disk in gigabytes? Show detailed low and high memory statistics and total of RAM and Swap.',
'Show the amount of free memory in gigabytes on my computer with detailed low and high memory statistics and total of RAM plus Swap.',
'Get statistics of available memory in gigabytes including low and high memory details and total of RAM and Swap.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in gigabytes.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -g','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in gigabytes.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in gigabytes.',
'Get statistics of available memory including low and high memory details every 1 second in gigabytes.',
'Display free RAM memory in gigabytes every 1 second. Results should include detailed low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -g','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in gigabytes.',
'How do I check the usage of my RAM in gigabytes every second including low and high memory statistics for 5 seconds?',
'Get statistics of available memory in gigabytes including low and high memory details for the next 5 seconds.',
'Display free RAM memory in gigabytes for the next 5 seconds. Also include low and high memory statistics.']},ignore_index=True)

#### 
free = free.append({'Command':'free -l -o --tera','NL Queries':['How much free memory do I have on my disk in terabytes? Show detailed low and high memory statistics in old format.',
'Show the amount of free memory in terabytes on my computer with detailed low and high memory statistics without -/+buffers/cache line.',
'Get statistics of available memory in terabytes including low and high memory details without -/+buffers/cache line.',
'Display free RAM memory in old format. Also include low and high memory statistics in terabytes.']},ignore_index=True)

free = free.append({'Command':'free -l -t --tera','NL Queries':['How much free memory do I have on my disk in terabytes? Show detailed low and high memory statistics and total of RAM and Swap.',
'Show the amount of free memory in terabytes on my computer with detailed low and high memory statistics and total of RAM plus Swap.',
'Get statistics of available memory in terabytes including low and high memory details and total of RAM and Swap.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in terabytes.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 --tera','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in terabytes.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in terabytes.',
'Get statistics of available memory including low and high memory details every 1 second in terabytes.',
'Display free RAM memory in terabytes every 1 second. Results should include detailed low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 --tera','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in terabytes.',
'How do I check the usage of my RAM in terabytes every second including low and high memory statistics for 5 seconds?',
'Get statistics of available memory in terabytes including low and high memory details for the next 5 seconds.',
'Display free RAM memory in terabytes for the next 5 seconds. Also include low and high memory statistics.']},ignore_index=True)

#### 
free = free.append({'Command':'free -l -o -h','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics in old format with human readable numbers.',
'Show the amount of free memory on my computer in human redable format with detailed low and high memory statistics without -/+buffers/cache line.',
'Get statistics of available memory in human readable format including low and high memory details without -/+buffers/cache line.',
'Display free RAM memory in old format with human readable numbers. Also include low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -t -h','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics and total of RAM and Swap in human readable format.',
'Show the amount of free memory on my computer with detailed low and high memory statistics and total of RAM plus Swap in human readable format.',
'Get statistics of available memory including low and high memory details and total of RAM and Swap in human readable format.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in human readable format.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -h','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in human readable format.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in human readable format.',
'Get statistics of available memory including low and high memory details every 1 second in human readable format.',
'Display free RAM memory every 1 second in human readable format. Results should inlcude detailed low and high memory statistics.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -h','NL Queries':['Display usage of RAM every 1 second for 5 seconds in human readable format. Show detailed low and high memory statistics.',
'How do I check the usage of my RAM every second including low and high memory statistics for 5 seconds in human readable format?',
'Get statistics of available memory including low and high memory details for the next 5 seconds in human readable format.',
'Display free RAM memory for the next 5 seconds in human readable format. Also include low and high memory statistics.']},ignore_index=True)

####
free = free.append({'Command':'free -l -o -b --si','NL Queries':['How much free memory do I have on my disk in bytes? Show detailed low and high memory statistics in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory in bytes on my computer with detailed low and high memory statistics without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in bytes including low and high memory details without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Also include low and high memory statistics in bytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -t -b --si','NL Queries':['How much free memory do I have on my disk in bytes? Show detailed low and high memory statistics and total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory in bytes on my computer with detailed low and high memory statistics and total of RAM plus Swap. Divide by 1000 not 1024.',
'Get statistics of available memory in bytes including low and high memory details and total of RAM and Swap. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in bytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -b --si','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in bytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in bytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details every 1 second in bytes. Use powers of 1000 not 1024.',
'Display free RAM memory in bytes every 1 second. Results should include detailed low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -b --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in bytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM in bytes every second including low and high memory statistics for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory in bytes including low and high memory details for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in bytes for the next 5 seconds. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

#### 
free = free.append({'Command':'free -l -o -k --si','NL Queries':['How much free memory do I have on my disk in kilobytes? Show detailed low and high memory statistics in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory in kilobytes on my computer with detailed low and high memory statistics without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in kilobytes including low and high memory details without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Also include low and high memory statistics in kilobytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -t -k --si','NL Queries':['How much free memory do I have on my disk in kilobytes? Show detailed low and high memory statistics and total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory in kilobytes on my computer with detailed low and high memory statistics and total of RAM plus Swap. Divide by 1000 not 1024.',
'Get statistics of available memory in kilobytes including low and high memory details and total of RAM and Swap. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in kilobytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -k --si','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in kilobytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in kilobytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details every 1 second in kilobytes. Use powers of 1000 not 1024.',
'Display free RAM memory in kilobytes every 1 second. Results should include detailed low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -k --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in kilobytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM in kilobytes every second including low and high memory statistics for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory in kilobytes including low and high memory details for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in kilobytes for the next 5 seconds. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

### 
free = free.append({'Command':'free -l -o -m --si','NL Queries':['How much free memory do I have on my disk in megabytes? Show detailed low and high memory statistics in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory in megabytes on my computer with detailed low and high memory statistics without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in megabytes including low and high memory details without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Also include low and high memory statistics in megabytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -t -m --si','NL Queries':['How much free memory do I have on my disk in megabytes? Show detailed low and high memory statistics and total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory in megabytes on my computer with detailed low and high memory statistics and total of RAM plus Swap. Divide by 1000 not 1024.',
'Get statistics of available memory in megabytes including low and high memory details and total of RAM and Swap. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in megabytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -m --si','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in megabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in megabytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details every 1 second in megabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in megabytes every 1 second. Results should include detailed low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -m --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in megabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM in megabytes every second including low and high memory statistics for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory in megabytes including low and high memory details for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in megabytes for the next 5 seconds. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

### 
free = free.append({'Command':'free -l -o -g --si','NL Queries':['How much free memory do I have on my disk in gigabytes? Show detailed low and high memory statistics in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory in gigabytes on my computer with detailed low and high memory statistics without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in gigabytes including low and high memory details without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Also include low and high memory statistics in gigabytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -t -g --si','NL Queries':['How much free memory do I have on my disk in gigabytes? Show detailed low and high memory statistics and total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory in gigabytes on my computer with detailed low and high memory statistics and total of RAM plus Swap. Divide by 1000 not 1024.',
'Get statistics of available memory in gigabytes including low and high memory details and total of RAM and Swap. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in gigabytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -g --si','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in gigabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in gigabytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details every 1 second in gigabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in gigabytes every 1 second. Results should include detailed low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -g --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in gigabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM in gigabytes every second including low and high memory statistics for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory in gigabytes including low and high memory details for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in gigabytes for the next 5 seconds. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

#### 
free = free.append({'Command':'free -l -o --tera --si','NL Queries':['How much free memory do I have on my disk in terabytes? Show detailed low and high memory statistics in old format. Use powers of 1000 not 1024.',
'Show the amount of free memory in terabytes on my computer with detailed low and high memory statistics without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in terabytes including low and high memory details without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format. Also include low and high memory statistics in terabytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -t --tera --si','NL Queries':['How much free memory do I have on my disk in terabytes? Show detailed low and high memory statistics and total of RAM and Swap. Use powers of 1000 not 1024.',
'Show the amount of free memory in terabytes on my computer with detailed low and high memory statistics and total of RAM plus Swap. Divide by 1000 not 1024.',
'Get statistics of available memory in terabytes including low and high memory details and total of RAM and Swap. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in terabytes. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 --tera --si','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in terabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in terabytes. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details every 1 second in terabytes. Use powers of 1000 not 1024.',
'Display free RAM memory in terabytes every 1 second. Results should include detailed low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 --tera --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds. Show detailed low and high memory statistics in terabytes. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM in terabytes every second including low and high memory statistics for 5 seconds? Divide by 1000 not 1024.',
'Get statistics of available memory in terabytes including low and high memory details for the next 5 seconds. Use powers of 1000 not 1024.',
'Display free RAM memory in terabytes for the next 5 seconds. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

#### 
free = free.append({'Command':'free -l -o -h --si','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics in old format with human readable numbers. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer in human redable format with detailed low and high memory statistics without -/+buffers/cache line. Divide by 1000 not 1024.',
'Get statistics of available memory in human readable format including low and high memory details without -/+buffers/cache line. Use powers of 1000 not 1024.',
'Display free RAM memory in old format with human readable numbers. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -t -h --si','NL Queries':['How much free memory do I have on my disk? Show detailed low and high memory statistics and total of RAM and Swap in human readable format. Use powers of 1000 not 1024.',
'Show the amount of free memory on my computer with detailed low and high memory statistics and total of RAM plus Swap in human readable format. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details and total of RAM and Swap in human readable format. Use powers of 1000 not 1024.',
'Display free RAM memory. Also include low and high memory statistics and total of RAM plus Swap in human readable format. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -s 1 -h --si','NL Queries':['Display usage of RAM including detailed low and high memory statistics every 1 second in human readable format. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second? Output should include low and high memory statistics in human readable format. Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details every 1 second in human readable format. Use powers of 1000 not 1024.',
'Display free RAM memory every 1 second in human readable format. Results should inlcude detailed low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

free = free.append({'Command':'free -l -c 5 -h --si','NL Queries':['Display usage of RAM every 1 second for 5 seconds in human readable format. Show detailed low and high memory statistics. Use powers of 1000 not 1024.',
'How do I check the usage of my RAM every second including low and high memory statistics for 5 seconds in human readable format? Divide by 1000 not 1024.',
'Get statistics of available memory including low and high memory details for the next 5 seconds in human readable format. Use powers of 1000 not 1024.',
'Display free RAM memory for the next 5 seconds in human readable format. Also include low and high memory statistics. Divide by 1000 not 1024.']},ignore_index=True)

####

free = free.append({'Command':'free --help','NL Queries':['Show all options of free command.',
'What all can be done using free command?',
'What are the options available with free command?',
'Display all the additions that can be made to the free command.']},ignore_index=True)

free = free.append({'Command':'free --version','NL Queries':['Show version of free command.',
'Who wrote free command?',
'What is the version of free command?',
'Who is the author of free command?']},ignore_index=True)

print free.shape
