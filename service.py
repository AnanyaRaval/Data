import pandas as pd 

service = pd.DataFrame(columns = ['Command','NL Queries'])

service = service.append({'Command':'service start httpd','NL Queries':['Start the httpd service.',
									'How can I start the httpd service?',
                                                                        'Command to start the httpd background service immediately.',
                                                                        'How can I make the system to start the httpd service?']},ignore_index=True)

service = service.append({'Command':'service stop httpd','NL Queries':['Stop the httpd service.',
									'How can I stop the httpd service?',
                                                                        'The httpd background service will be stopped immediately.',
                                                                        'How can I make the system to stop the httpd service?']},ignore_index=True)

service = service.append({'Command':'service restart httpd','NL Queries':['Restart the httpd service if already running in the background.',
									'How can I restart the httpd service?',
                                                                        'Command to restart the httpd background service immediately.',
                                                                        'How can I make the system to restart the running httpd service?']},ignore_index=True)

service = service.append({'Command':'service reload httpd','NL Queries':['Reload the configuration files of the httpd service.',
									'How can I reload the configuration files of the httpd service?',
                                                                        'Command to reload the configuration files of the httpd background service.',
                                                                        'How can I make the system to reload the configuration files of the running httpd service?']},ignore_index=True)

service = service.append({'Command':'service --status-all','NL Queries':['Show the status of all the services started.',
									'How can I see the statuses of all the services that have started?',
                                                                        'Command to show the status of all the services that have started.',
                                                                        'How can I make the status of all the services to be shown?']},ignore_index=True)

service = service.append({'Command':'service --full-restart','NL Queries':['Restart all the running services in the system.',
									'How can I restart all the services that are currently running?',
                                                                        'Command to restart the services running at the moment on the system.',
                                                                        'How can I make all the services in the system to restart?']},ignore_index=True)