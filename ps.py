import pandas as pd 

ps = pd.DataFrame(columns = ['Command','NL Queries'])

ps = ps.append({'Command':'ps -ef',
				'NL Queries':['Show all processes.',
							'Display the state of all process currently being executed on the system.',
							'Display all processes currently running on this system.']},ignore_index=True)

ps = ps.append({'Command':'ps -f -U www-data',
				'NL Queries':['Show all processes run by user www-data.',
							'How do I see the state of all processes run by www-data?']},ignore_index=True)

ps = ps.append({'Command':'ps -f -U 1234',
				'NL Queries':['Show processes run by user id 1234.',
							'How do I see the state of all processes run by user id 1234?']},ignore_index=True)

ps = ps.append({'Command':'ps -f -G 1234',
				'NL Queries':['Show processes run by group id 1234.',
							'How do I see the state of all processes run by group id 1234?']},ignore_index=True)

ps = ps.append({'Command':'ps -f -p 3150,7298,6544',
				'NL Queries':['Show state of process of the following ids:3150,7298,654.',
							'How do I check the status of processes 3150,6544 and 7298?']},ignore_index=True)

ps = ps.append({'Command':'ps -f --ppid 3150,7298,6544',
				'NL Queries':['Show state of process of the following parent id\'s:3150,7298,654.',
							'How do I check the status of processes with parent id\'s 3150,6544 and 7298?']},ignore_index=True)

ps = ps.append({'Command':'ps -u root -U root',
				'NL Queries':['Show all processes running by root.',
							'Display the state of all process currently being executed by root.',
							'Display all processes currently running by root.']},ignore_index=True)

ps = ps.append({'Command':'ps -t',
				'NL Queries':['Show all processes by tty.',
							'Display the state of all process currently being executed by terminal.',
							'Display all processes currently running by tty.']},ignore_index=True)

ps = ps.append({'Command':'ps -fL',
				'NL Queries':['Show all light weight processes.',
							'Display all light weight processes and number of light weight processes.',
							'How do I see the light weight processes and number of light weight processes?']},ignore_index=True)

ps = ps.append({'Command':'ps -p 1234 -o pid,etime ',
				'NL Queries':['Show elapsed time of process with id 1234.',
							'How do I see the elapsed time of process with id 1234?',
							'How do I know the amount time the process with id 1234 is alive?']},ignore_index=True)

ps = ps.append({'Command':'ps -e --forest',
				'NL Queries':['Show processes with it\'s process hierarchy.',
							'Display the state of all process currently being executed on the system with it\'s hierarchy.',
							'Display all processes currently running on this system with hierarchy.']},ignore_index=True)

ps = ps.append({'Command':'ps -f -C testing.sh',
				'NL Queries':['Show current processes with name testing.sh .',
							'How do I see the if any current processes with name testing.sh ?',
							'Display any current processes with name testing.sh .']},ignore_index=True)





print ps


