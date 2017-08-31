import pandas as pd 

ssh = pd.DataFrame(columns = ['Command','NL Queries'])

ssh = ssh.append({'Command':'ssh jhawkins@collie.stanford.edu','NL Queries':['Login to collie.stanford.edu with username jhawkins.','Command to remote login. Username is jhawkins. Remote host is collie.stanford.edu.']},ignore_index = True)
ssh = ssh.append({'Command':'ssh -l uname gatech','NL Queries':['Login to server gatech with uname.','How do I login to a remote server with username uname and server name gatech.']},ignore_index=True)
ssh = ssh.append({'Command':'ssh 192.168.0.103 -p 1234','NL Queries':['Connect to address 192.168.0.03 to port 1234.','How do I connect to server 192.168.0.103 and port 1234']},ignore_index=True)



#1
ssh = ssh.append({'Command':  'ssh -1 pratik.jain@web.iiit.ac.in',
                  'NL Queries':  ['Log in to web.iiit.ac.in using username pratik.jain and protocol version 1 only.',
                                 'How do I login to remote server web.iiit.ac.in using username pratik.jain using protocol v1 ?',
                                 'Connect me to web.iiit.ac.in server using username pratik.jain using protocol v1 .',
                                 'Log in as pratik.jain@web.iiit.ac.in using v1 protocol.']}, ignore_index = True)

#2
ssh = ssh.append({'Command':  'ssh -2 pratik.jain@web.iiit.ac.in',
                  'NL Queries':  ['Log in to web.iiit.ac.in using username pratik.jain and protocol version 2 only.',
                                 'How do I login to remote server web.iiit.ac.in using username pratik.jain using protocol v2 ?',
                                 'Connect me to web.iiit.ac.in server using username pratik.jain using protocol v2 .',
                                 'Log in as pratik.jain@web.iiit.ac.in using v2 protocol.']}, ignore_index = True)

#3
ssh = ssh.append({'Command':  'ssh -4 pratik.jain@web.iiit.ac.in',
                  'NL Queries':  ['Log in to web.iiit.ac.in using username pratik.jain and use IPv4 only.',
                                 'Connect to pratik.jain@web.iiit.ac.in using IPv4 .',
                                 'Login to remote system web.iiit.ac.in using username pratik.jain using IPv4 .',
                                 'How do I log in to remote computer with server name web.iiit.ac.in and id pratik.jain using IPv4 ?']}, ignore_index = True)

#4
ssh = ssh.append({'Command':  'ssh -6 pratik.jain@web.iiit.ac.in',
                  'NL Queries':  ['Log in to web.iiit.ac.in using username pratik.jain and use IPv6 only.',
                                 'Connect to pratik.jain@web.iiit.ac.in using IPv6 .',
                                 'Login to remote system web.iiit.ac.in using username pratik.jain using IPv6 .',
                                 'How do I log in to remote computer with server name web.iiit.ac.in and id pratik.jain using IPv6 ?']}, ignore_index = True)

#5
ssh = ssh.append({'Command':  'ssh -C pratik.jain@web.iiit.ac.in',
                  'NL Queries':  ['Log in to web.iiit.ac.in using username pratik.jain and request compression of data.',
                                 'Requesting compression of data, connect to web.iiit.ac.in as pratik.jain .',
                                 'How do I log in to web.iiit.ac.in as pratik.jain and use compressed data for communication?']}, ignore_index = True)

#6
ssh = ssh.append({'Command':  'ssh -q pratik.jain@web.iiit.ac.in',
                  'NL Queries':  ['Log in to web.iiit.ac.in using username pratik.jain and show only important messages.',
                                 'Connect to web.iiit.ac.in using pratik.jain as id. Suppress warning messages.',
                                 'How do I log in as pratik.jain@web.iiit.ac.in without seeing unnecessary messages?']}, ignore_index = True)

#7
ssh = ssh.append({'Command':  'ssh -T root@10.42.0.34',
                  'NL Queries':  ['Log in to 10.42.0.34 using username root and disable pseudo terminal allocation.',
                                 'Login as root@10.42.0.34 disabling pty allocation.',
                                 'Connect to IP 10.42.0.34 as root . Do not allocate pseudo terminal by default.']}, ignore_index = True)

#8
ssh = ssh.append({'Command':  'ssh -x root@10.42.0.34',
                  'NL Queries':  ['Login into 10.42.0.34 using username root and disable X11 forwarding.',
                                 'Disabling X11 forwarding connect to IP 10.42.0.34 using root as username.',
                                 'Connect to root@10.42.0.34 without enabling X11 forwarding.']}, ignore_index = True)

#9
ssh = ssh.append({'Command':  'ssh -Y root@10.42.0.34',
                  'NL Queries':  ['Login into 10.42.0.34 using username root and enable X11 forwarding.',
                                 'Enabling X11 forwarding, connect to IP 10.42.0.34 using root as username.',
                                 'Connect to root@10.42.0.34 enabling X11 forwarding.']}, ignore_index = True)

#10
ssh = ssh.append({'Command':  'ssh -l root 10.42.0.34',
                  'NL Queries':  ['Login into 10.42.0.34 using username root.',
                                 'Using username root log in to 10.42.0.34 .',
                                 'Using ID as root connect to ssh server at 10.42.0.34 .']}, ignore_index = True)

#11
ssh = ssh.append({'Command':  'ssh user@remote-host \"ls test\"',
                  'NL Queries':  ['Login to remote-host as user and execute the command \"ls test\" after it and exit the remote shell.',
                                 'Run the command \"ls test\" on remote-host server as user and return to the current shell.',
                                 'Display the details in test directory of the user@remote-host and exit from remote-host shell.']}, ignore_index = True)

#12
ssh = ssh.append({'Command':  'ssh -v user@remote-host',
                  'NL Queries':  ['Login to remote-host as user and display debug log.',
                                 'Show the debug log of ssh while loggin in to remote-host as user .',
                                 'Using user as ID log in to remote-host and show the progress of the connection establishment.']}, ignore_index = True)

#13
ssh = ssh.append({'Command':  'ssh -E log_file user@remote-host',
                  'NL Queries':  ['Log in to remote-host as user and append debug logs to log_file instead of standard error.',
                                 'Connect to user@remote-host and append the debug messages to log_file .',
                                 'Log into remote-host using user as userid and add the debug messages to log_file file.']}, ignore_index = True)

#14
ssh = ssh.append({'Command':  'ssh -o Port=222 user@172.23.23.203',
                  'NL Queries':  ['Log in as user@172.23.23.203 using port 222 .',
                                 'Using port 222 for communication, log in to 172.23.23.203 as user .',
                                 'Connect to 172.23.23.203 as user via port 222 .']}, ignore_index = True)

#15
ssh = ssh.append({'Command':  'ssh -o BatchMode=yes user@172.23.23.203 \"who\"',
                  'NL Queries':  ['Log in as user@172.23.23.203 in batch mode and execute the command \"who\" and return.',
                                 'Execute the command \"who\" in remote server 172.23.23.203 as user if password-less login is enabled and exit the remote shell.',
                                 'Run the who command as user@172.23.23.203 if password-less login is permitted by the server.']}, ignore_index = True)

#16
ssh = ssh.append({'Command':  'ssh -t user@172.23.23.203',
                  'NL Queries':  ['Log in as user@172.23.23.203 and force pseudo-terminal allocation.',
                                 'Allocate pty when logged into 172.23.23.203 as user .',
                                 'Logging in as user@172.23.23.203 allocate pseudo terminal.']}, ignore_index = True)

#17
ssh = ssh.append({'Command':  'ssh -F user_ssh_config user@172.23.23.203',
                  'NL Queries':  ['Log in as user@172.23.23.203 using configuration from file user_ssh_config .',
                                 'Login as user@172.23.23.203 . Use user_ssh_config file for configuring login.',
                                 'Connect to user@172.23.23.203 using user_ssh_config for configuration.']}, ignore_index = True)

#18
ssh = ssh.append({'Command':  'ssh -N user@google.com',
                  'NL Queries':  ['Log in as user@google.com and do not execute remote command.',
                                 'Without executing remote command, login as user@google.com .',
                                 'Connect to user in server google.com without running remote commands.']}, ignore_index = True)

#19
ssh = ssh.append({'Command':  'ssh -f user@google.com',
                  'NL Queries':  ['Log in as user@google.com and put it in background.',
                                 'Connect to user@google.com . Do it in background.',
                                 'Log on to google.com as user and put the process in background.']}, ignore_index = True)

#20
ssh = ssh.append({'Command':  'ssh -V',
                  'NL Queries':  ['Show ssh version.',
                                 'Which version of ssh am I using?',
                                 'What is version number of ssh command?']}, ignore_index = True)

#21
ssh = ssh.append({'Command':  'ssh -o CheckHostIP=yes user@google.com',
                  'NL Queries':  ['Log in as user@google.com after checking host IP address.',
                                 'Check host IP address and then connect to google.com as user.',
                                 'Verify host IP and then log in as user@google.com .']}, ignore_index = True)

#22
ssh = ssh.append({'Command':  'ssh -o Cipher=blowfish user@manga.com',
                  'NL Queries':  ['Log in as user@manga.com using cipher blowfish .',
                                 'Using blowfish cipher, connect to manga.com as username user .',
                                 'Using ID user login to manga.com . Use blowfish cipher for encryption.']}, ignore_index = True)

#23
ssh = ssh.append({'Command':  'ssh -o CompressionLevel=1 user@manga.com',
                  'NL Queries':  ['Log in as user@manga.com using compression level 1 .',
                                 'Use compression level 1 and connect to manga.com as user .',
                                 'Login as user@manga.com and use 1st level compression.']}, ignore_index = True)

#24
ssh = ssh.append({'Command':  'ssh -b 192.168.0.200 leni@192.168.0.103',
                  'NL Queries':  ['Log in as leni@192.168.0.103 using 192.168.0.200 as IP address.',
                                 'Use 192.168.0.200 local IP to connect to 192.168.0.103 as leni .',
                                 'Use bind address 192.168.0.200 as source address for leni@192.168.0.103 and connect.']}, ignore_index = True)

#25
ssh = ssh.append({'Command':  'ssh -o StrictHostKeyChecking=no user@172.23.23.203',
                  'NL Queries':  ['Log in as user@172.23.23.203 without strict host key checking.',
                                 'Connect to 172.23.23.203 as user . Disable strict host checking.',
                                 'Disabling strict host checking, log in as user@172.23.23.203 .']}, ignore_index = True)


print ssh.shape

