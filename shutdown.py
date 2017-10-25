import pandas as pd 

'''
   -c     Cancel a shutdown that is in progress.

   -f    Reboot fast, by suppressing the normal call to fsck
         when rebooting.
   -h    Halt the system when shutdown is complete.

   -k    Print the warning message, but suppress actual shutdown.

   -n    Perform shutdown without a call to init.

   -r    Reboot the system when shutdown is complete.

   -t sec 
         Ensure a sec-second delay between killing processes
         and changing the runlevel.
'''

shutdown = pd.DataFrame(columns = ['Command','NL Queries'])

shutdown = shutdown.append({'Command':'shutdown -h now','NL Queries':['Shuts the system down immediately.',
													                    'How can I immediately shut down the system?',
                                                                        'The system will shut down immediately.',
                                                                        'How can I make the system to shutdown immediately?']},ignore_index=True)

shutdown = shutdown.append({'Command':'shutdown -h 08:00','NL Queries':['Shuts the system down at 8:00 A.M.',
													                    'How can I shut down the system at 8:00 A.M?',
                                                                        'The system will shut down at 8:00 A.M.',
                                                                        'How can I make the system to shutdown at 8:00 A.M?']},ignore_index=True)

shutdown = shutdown.append({'Command':'shutdown -c','NL Queries':['Cancels a scheduled shutdown.',
													                    'How can I cancel a scheduled system shutdown?',
                                                                        'A scheduled shutdown will be cancelled.',
                                                                        'How do I cancel a shutdown that has been scheduled?']},ignore_index=True)

shutdown = shutdown.append({'Command':'shutdown -h +10','NL Queries':['Shuts the system down in 10 minutes.',
													                    'How can I shut down the system in 10 minutes?',
                                                                        'The system will shut down in 10 minutes.',
                                                                        'How can I make the system to shutdown 10 minutes?']},ignore_index=True)

shutdown = shutdown.append({'Command':'shutdown -r now','NL Queries':['Reboots the system after an immediate system shuts down.',
													                    'How can I reboot the system after immediately shutting down the system?',
                                                                        'The system reboots after shutting down immediately.',
                                                                        'How can I make the system to reboot after immediately shutting down the system?']},ignore_index=True)

shutdown = shutdown.append({'Command':'shutdown -r 08:00','NL Queries':['Reboots the system after a system shut down at 08:00 A.M.',
													                    'How can I reboot the system after shutting down the system at 08:00 A.M?',
                                                                        'The system reboots after shutting down at 08:00 A.M.',
                                                                        'How can I make the system to reboot after shutting down the system?']},ignore_index=True)

shutdown = shutdown.append({'Command':'shutdown -r +10','NL Queries':['Reboots the system after a system shut down after 10 minutes.',
													                    'How can I reboot the system after immediately shutting down the system after 10 minutes?',
                                                                        'The system reboots after shutting down after 10 minutes.',
                                                                        'How can I make the system to reboot after shutting down the system 10 minutes later?']},ignore_index=True)

shutdown = shutdown.append({'Command':'shutdown -f now','NL Queries':['Reboots the system immediately by not doing a file system consistency check.',
													                    'How can I reboot the system immediately and suppress a file system consistency check?',
                                                                        'The system reboots immediately by suppressing a file system consistency check.',
                                                                        'How can I make the system to reboot immediately by preventing a file system consistency check?']},ignore_index=True)

shutdown = shutdown.append({'Command':'shutdown -t 10','NL Queries':['Shuts down the system after a 10 second delay.',
													                    'How can I shutdown the system after a 10 second delay?',
                                                                        'The system shuts down after a delay of 10 seconds.',
                                                                        'How can I make the system to shutdown after 10 seconds delay?']},ignore_index=True)

print shutdown.shape