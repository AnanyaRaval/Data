import pandas as pd 

wget = pd.DataFrame(columns = ['Command','NL Queries'])

wget = wget.append({'Command':'wget pes.edu/logo.png','NL Queries':['Download the logo.png file from the website pes.edu.',
						                   'How can I fetch the file logo.png from the pes.edu website?',
                                                                        'Fetch the logo.png resource from the pes.edu website.',
                                                                        'How do I download the logo.png resource from the pes.edu website?']},ignore_index=True)


wget = wget.append({'Command':'wget pes.edu/logo.png -o output.txt','NL Queries':['Download the logo.png file from the website pes.edu, create a log file named output.txt.',
									'How can I fetch the file logo.png from the pes.edu website, copy the log details to output.txt?',
                                                                        'Fetch the logo.png resource from the pes.edu website, create a log file output.txt.',
                                                                        'How do I download the logo.png resource from the pes.edu website, make a log file output.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget -q pes.edu/logo.png','NL Queries':['Download the logo.png file from the website pes.edu, show no details on the terminal screen.',
									'How can I fetch the file logo.png from the pes.edu website, prevent messages from being shown on the terminal screen?',
                                                                        'Fetch the logo.png resource from the pes.edu website, prevent messages from being shown on the terminal screen.',
                                                                        'How do I download the logo.png resource from the pes.edu website, make sure no details are shown on the terminal?']},ignore_index=True)

wget = wget.append({'Command':'wget pes.edu/logo.png --report-speed=bits','NL Queries':['Downloads the logo.png file from the website pes.edu, show the current speed in bits.',
												                        'How can I fetch the file logo.png from the pes.edu website, show the current speed in bits?',
                                                                        'Fetch the logo.png resource from the pes.edu website, show the current speed in bits.',
                                                                        'How do I download the logo.png resource from the pes.edu website, show the current speed in bits?']},ignore_index=True)
#bits is not in the query because whatever may be the parameter, It'll show only in bits

wget = wget.append({'Command':'wget --input-file=url.txt','NL Queries':['Downloads the contents from the urls present in url.txt.',
												                        'How can I fetch the contents from the urls provided in the url.txt file?',
                                                                        'Fetch the contents from the urls given in the url.txt file.',
                                                                        'How do I download from the urls present in the url.txt file?']},ignore_index=True)

wget = wget.append({'Command':'wget --base=pes.edu --input-file=url.txt','NL Queries':['Downloads the contents from the urls present in url.txt with the base url as pes.edu.',
												                        'How can I fetch the contents from the urls provided in the url.txt file with the base url as pes.edu?',
                                                                        'Fetch the contents from the urls given in the url.txt file with the base url as pes.edu.',
                                                                        'How do I download from the urls present in the url.txt file with the base url as pes.edu?']},ignore_index=True)

wget = wget.append({'Command':'wget pes.edu/logo.png --tries=3','NL Queries':['Tries to download the logo.png file from the website pes.edu 3 times.',
												                        'How can I try to fetch the file logo.png from the pes.edu website 3 times?',
                                                                        'Try to fetch the logo.png resource from the pes.edu website 3 times.',
                                                                        'How do I try to download the logo.png resource from the pes.edu website 3 times?']},ignore_index=True)

wget = wget.append({'Command':'wget pes.edu/instructions.txt --output-document=new_inst.txt','NL Queries':['Downloads the instructions.txt file from the website pes.edu, copy the contents of the file to new_inst.txt.',
												                        'How can I fetch the file instructions.txt from the pes.edu website, dump the contents of the file to new_inst.txt?',
                                                                        'Fetch the instructions.txt resource from the pes.edu website, put the contents of the file into new_inst.txt.',
                                                                        'How do I download the instructions.txt resource from the pes.edu website, paste the contents of the file into new_inst.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget -c pes.edu/Handbook.pdf','NL Queries':['Downloads the Handbook.pdf file from the website pes.edu, resumes it if it has been partially downloaded.',
												                        'How can I fetch the file Handbook.pdf from the pes.edu website, resume it if it has been partially downloaded?',
                                                                        'Fetch the Handbook.pdf resource from the pes.edu website, resume it if it has been partially downloaded.',
                                                                        'How do I download the logo.png resource from the pes.edu website, continue downloading it if it has been partially downloaded?']},ignore_index=True)

wget = wget.append({'Command':'wget pes.edu/logo.png --timeout=20','NL Queries':['Downloads the logo.png file from the website pes.edu with a 20 second timeout if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website, set a timeout for 20 seconds?',
                                                                        'Fetch the logo.png resource from the pes.edu website, a timeout of 20 seconds if the server isn\'t responding.',
                                                                        'How do I download the logo.png resource from the pes.edu website, set a timeout of 20 seconds?']},ignore_index=True)

wget = wget.append({'Command':'wget pes.edu/logo.png --wait=20','NL Queries':['Downloads the logo.png file from the website pes.edu, tries downloading with an interval of 20 seconds if the server hasn\'t responded.',
												                        'How can I fetch the file logo.png from the pes.edu website, try downloading in an interval of 20 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding.',
                                                                        'How do I download the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding?']},ignore_index=True)

wget = wget.append({'Command':'wget -r pes.edu/wp-content/','NL Queries':['Downloads the contents of the folder wp-content of the website pes.edu recursively.',
												                        'How can I fetch the contents of the directory wp-contents of the website pes.edu recursively?',
                                                                        'Fetch the contents of the directory wp-contents of the website pes.edu recursively.',
                                                                        'How do I download the contents of the folder wp-contents of the website pes.edu recursively?']},ignore_index=True)

#Vanilla
wget = wget.append({'Command':'wget --output=out.txt -q pes.edu/logo.png','NL Queries':['Downloads the logo.png file from the website pes.edu, shows no details on the terminal screen and create a log file named out.txt.',
												                        'How can I fetch the file logo.png from the pes.edu website, prevent messages from being shown on the terminal screen and create a log file named out.txt?',
                                                                        'Fetch the logo.png resource from the pes.edu website, prevent messages from being shown on the terminal screen and create a log file named out.txt.',
                                                                        'How do I download the logo.png resource from the pes.edu website, make sure no details are shown on the terminal and create a log file named out.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget --output=out.txt pes.edu/logo.png --report-speed=bits','NL Queries':['Downloads the logo.png file from the website pes.edu, show the current speed in bits and create a log file named out.txt.',
												                        'How can I fetch the file logo.png from the pes.edu website, show the current speed in bits and create a log file named out.txt?',
                                                                        'Fetch the logo.png resource from the pes.edu website, show the current speed in bits and create a log file named out.txt.',
                                                                        'How do I download the logo.png resource from the pes.edu website, show the current speed in bits and create a log file named out.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget --output=out.txt --input-file=url.txt','NL Queries':['Downloads the contents from the urls present in url.txt and create a log file named out.txt.',
												                        'How can I fetch the contents from the urls provided in the url.txt file and create a log file named out.txt?',
                                                                        'Fetch the contents from the urls given in the url.txt file and create a log file named out.txt.',
                                                                        'How do I download from the urls present in the url.txt file and create a log file named out.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget --output=out.txt --base=pes.edu --input-file=url.txt','NL Queries':['Downloads the contents from the urls present in url.txt with the base url as pes.edu, create a log file named out.txt.',
												                        'How can I fetch the contents from the urls provided in the url.txt file with the base url as pes.edu, create a log file named out.txt?',
                                                                        'Fetch the contents from the urls given in the url.txt file with the base url as pes.edu, create a log file named out.txt.',
                                                                        'How do I download from the urls present in the url.txt file with the base url as pes.edu, create a log file named out.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget --output=out.txt pes.edu/logo.png --tries=3','NL Queries':['Tries to download the logo.png file from the website pes.edu 3 times and create a log file named out.txt.',
												                        'How can I try to fetch the file logo.png from the pes.edu website 3 times and create a log file named out.txt?',
                                                                        'Try to fetch the logo.png resource from the pes.edu website 3 times and create a log file named out.txt.',
                                                                        'How do I try to download the logo.png resource from the pes.edu website 3 times and create a log file named out.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget --output=out.txt pes.edu/instructions.txt --output-document=new_inst.txt','NL Queries':['Downloads the instructions.txt file from the website pes.edu, copy the contents of the file to new_inst.txt and create a log file named out.txt.',
												                        'How can I fetch the file instructions.txt from the pes.edu website, dump the contents of the file to new_inst.txt and create a log file named out.txt?',
                                                                        'Fetch the instructions.txt resource from the pes.edu website, put the contents of the file into new_inst.txt and create a log file named out.txt.',
                                                                        'How do I download the instructions.txt resource from the pes.edu website, paste the contents of the file into new_inst.txt and create a log file named out.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget --output=out.txt -c pes.edu/Handbook.pdf','NL Queries':['Downloads the Handbook.pdf file from the website pes.edu, resumes it if it has been partially downloaded and create a log file named out.txt.',
												                        'How can I fetch the file Handbook.pdf from the pes.edu website, resume it if it has been partially downloaded and create a log file named out.txt?',
                                                                        'Fetch the Handbook.pdf resource from the pes.edu website, resume it if it has been partially downloaded and create a log file named out.txt.',
                                                                        'How do I download the logo.png resource from the pes.edu website, continue downloading it if it has been partially downloaded and create a log file named out.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget --output=out.txt pes.edu/logo.png --timeout=20','NL Queries':['Downloads the logo.png file from the website pes.edu with a 20 second timeout if the request isn\'t complete and create a log file named out.txt.',
												                        'How can I fetch the file logo.png from the pes.edu website, set a timeout for 20 seconds and create a log file named out.txt?',
                                                                        'Fetch the logo.png resource from the pes.edu website, a timeout of 20 seconds if the server isn\'t responding and create a log file named out.txt.',
                                                                        'How do I download the logo.png resource from the pes.edu website, set a timeout of 20 seconds and create a log file named out.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget --output=out.txt pes.edu/logo.png --wait=20','NL Queries':['Downloads the logo.png file from the website pes.edu, tries downloading with an interval of 20 seconds if the server hasn\'t responded and create a log file named out.txt.',
												                        'How can I fetch the file logo.png from the pes.edu website, try downloading in an interval of 20 seconds if the request isn\'t complete and create a log file named out.txt?',
                                                                        'Fetch the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and create a log file named out.txt.',
                                                                        'How do I download the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and create a log file named out.txt?']},ignore_index=True)

wget = wget.append({'Command':'wget -r --output=out.txt pes.edu/wp-content/','NL Queries':['Downloads the contents of the folder wp-content of the website pes.edu recursively and create a log file named out.txt.',
												                        'How can I fetch the contents of the directory wp-contents of the website pes.edu recursively and create a log file named out.txt?',
                                                                        'Fetch the contents of the directory wp-contents of the website pes.edu recursively and create a log file named out.txt.',
                                                                        'How do I download the contents of the folder wp-contents of the website pes.edu recursively and create a log file named out.txt?']},ignore_index=True)

#output

wget = wget.append({'Command':'wget -q pes.edu/logo.png --report-speed=bits','NL Queries':['Downloads the logo.png file from the website pes.edu, show the current speed in bits and prevent messages from being shown on the terminal screen.',
												                        'How can I fetch the file logo.png from the pes.edu website, show the current speed in bits and prevent messages from being shown on the terminal screen?',
                                                                        'Fetch the logo.png resource from the pes.edu website, show the current speed in bits and prevent messages from being shown on the terminal screen.',
                                                                        'How do I download the logo.png resource from the pes.edu website, show the current speed in bits and prevent messages from being shown on the terminal screen?']},ignore_index=True)

wget = wget.append({'Command':'wget -q --input-file=url.txt','NL Queries':['Downloads the contents from the urls present in url.txt and prevent messages from being shown on the terminal screen.',
												                        'How can I fetch the contents from the urls provided in the url.txt file and prevent messages from being shown on the terminal screen?',
                                                                        'Fetch the contents from the urls given in the url.txt file and prevent messages from being shown on the terminal screen.',
                                                                        'How do I download from the urls present in the url.txt file and prevent messages from being shown on the terminal screen?']},ignore_index=True)

wget = wget.append({'Command':'wget -q --base=pes.edu --input-file=url.txt','NL Queries':['Downloads the contents from the urls present in url.txt with the base url as pes.edu, prevent messages from being shown on the terminal screen.',
												                        'How can I fetch the contents from the urls provided in the url.txt file with the base url as pes.edu, prevent messages from being shown on the terminal screen?',
                                                                        'Fetch the contents from the urls given in the url.txt file with the base url as pes.edu, prevent messages from being shown on the terminal screen.',
                                                                        'How do I download from the urls present in the url.txt file with the base url as pes.edu, prevent messages from being shown on the terminal screen?']},ignore_index=True)

wget = wget.append({'Command':'wget -q pes.edu/logo.png --tries=3','NL Queries':['Tries to download the logo.png file from the website pes.edu 3 times and prevent messages from being shown on the terminal screen.',
												                        'How can I try to fetch the file logo.png from the pes.edu website 3 times and prevent messages from being shown on the terminal screen?',
                                                                        'Try to fetch the logo.png resource from the pes.edu website 3 times and prevent messages from being shown on the terminal screen.',
                                                                        'How do I try to download the logo.png resource from the pes.edu website 3 times and prevent messages from being shown on the terminal screen?']},ignore_index=True)

wget = wget.append({'Command':'wget -q pes.edu/instructions.txt --output-document=new_inst.txt','NL Queries':['Downloads the instructions.txt file from the website pes.edu, copy the contents of the file to new_inst.txt and prevent messages from being shown on the terminal screen.',
												                        'How can I fetch the file instructions.txt from the pes.edu website, dump the contents of the file to new_inst.txt and prevent messages from being shown on the terminal screen?',
                                                                        'Fetch the instructions.txt resource from the pes.edu website, put the contents of the file into new_inst.txt and prevent messages from being shown on the terminal screen.',
                                                                        'How do I download the instructions.txt resource from the pes.edu website, paste the contents of the file into new_inst.txt and prevent messages from being shown on the terminal screen?']},ignore_index=True)

wget = wget.append({'Command':'wget -q -c pes.edu/Handbook.pdf','NL Queries':['Downloads the Handbook.pdf file from the website pes.edu, resumes it if it has been partially downloaded and prevent messages from being shown on the terminal screen.',
												                        'How can I fetch the file Handbook.pdf from the pes.edu website, resume it if it has been partially downloaded and prevent messages from being shown on the terminal screen?',
                                                                        'Fetch the Handbook.pdf resource from the pes.edu website, resume it if it has been partially downloaded and prevent messages from being shown on the terminal screen.',
                                                                        'How do I download the logo.png resource from the pes.edu website, continue downloading it if it has been partially downloaded and prevent messages from being shown on the terminal screen?']},ignore_index=True)

wget = wget.append({'Command':'wget -q pes.edu/logo.png --timeout=20','NL Queries':['Downloads the logo.png file from the website pes.edu with a 20 second timeout if the request isn\'t complete and prevent messages from being shown on the terminal screen.',
												                        'How can I fetch the file logo.png from the pes.edu website, set a timeout for 20 seconds and prevent messages from being shown on the terminal screen?',
                                                                        'Fetch the logo.png resource from the pes.edu website, a timeout of 20 seconds if the server isn\'t responding and prevent messages from being shown on the terminal screen.',
                                                                        'How do I download the logo.png resource from the pes.edu website, set a timeout of 20 seconds and prevent messages from being shown on the terminal screen?']},ignore_index=True)

wget = wget.append({'Command':'wget -q pes.edu/logo.png --wait=20','NL Queries':['Downloads the logo.png file from the website pes.edu, tries downloading with an interval of 20 seconds if the server hasn\'t responded and prevent messages from being shown on the terminal screen.',
												                        'How can I fetch the file logo.png from the pes.edu website, try downloading in an interval of 20 seconds if the request isn\'t complete and prevent messages from being shown on the terminal screen?',
                                                                        'Fetch the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and prevent messages from being shown on the terminal screen.',
                                                                        'How do I download the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and prevent messages from being shown on the terminal screen?']},ignore_index=True)

wget = wget.append({'Command':'wget -q -r pes.edu/wp-content/','NL Queries':['Downloads the contents of the folder wp-content of the website pes.edu recursively and prevent messages from being shown on the terminal screen.',
												                        'How can I fetch the contents of the directory wp-contents of the website pes.edu recursively and prevent messages from being shown on the terminal screen?',
                                                                        'Fetch the contents of the directory wp-contents of the website pes.edu recursively and prevent messages from being shown on the terminal screen.',
                                                                        'How do I download the contents of the folder wp-contents of the website pes.edu recursively and prevent messages from being shown on the terminal screen?']},ignore_index=True)

#no errors 

wget = wget.append({'Command':'wget --report-speed=bits --input-file=url.txt','NL Queries':['Downloads the contents from the urls present in url.txt and show the current speed in bits.',
												                        'How can I fetch the contents from the urls provided in the url.txt file and show the current speed in bits?',
                                                                        'Fetch the contents from the urls given in the url.txt file and show the current speed in bits.',
                                                                        'How do I download from the urls present in the url.txt file and show the current speed in bits?']},ignore_index=True)

wget = wget.append({'Command':'wget --report-speed=bits --base=pes.edu --input-file=url.txt','NL Queries':['Downloads the contents from the urls present in url.txt with the base url as pes.edu, show the current speed in bits.',
												                        'How can I fetch the contents from the urls provided in the url.txt file with the base url as pes.edu, show the current speed in bits?',
                                                                        'Fetch the contents from the urls given in the url.txt file with the base url as pes.edu, show the current speed in bits.',
                                                                        'How do I download from the urls present in the url.txt file with the base url as pes.edu, show the current speed in bits?']},ignore_index=True)

wget = wget.append({'Command':'wget --report-speed=bits pes.edu/logo.png --tries=3','NL Queries':['Tries to download the logo.png file from the website pes.edu 3 times and show the current speed in bits.',
												                        'How can I try to fetch the file logo.png from the pes.edu website 3 times and show the current speed in bits?',
                                                                        'Try to fetch the logo.png resource from the pes.edu website 3 times and show the current speed in bits.',
                                                                        'How do I try to download the logo.png resource from the pes.edu website 3 times and show the current speed in bits?']},ignore_index=True)

wget = wget.append({'Command':'wget --report-speed=bits pes.edu/instructions.txt --output-document=new_inst.txt','NL Queries':['Downloads the instructions.txt file from the website pes.edu, copy the contents of the file to new_inst.txt and show the current speed in bits.',
												                        'How can I fetch the file instructions.txt from the pes.edu website, dump the contents of the file to new_inst.txt and show the current speed in bits?',
                                                                        'Fetch the instructions.txt resource from the pes.edu website, put the contents of the file into new_inst.txt and show the current speed in bits.',
                                                                        'How do I download the instructions.txt resource from the pes.edu website, paste the contents of the file into new_inst.txt and show the current speed in bits?']},ignore_index=True)

wget = wget.append({'Command':'wget --report-speed=bits -c pes.edu/Handbook.pdf','NL Queries':['Downloads the Handbook.pdf file from the website pes.edu, resumes it if it has been partially downloaded and show the current speed in bits.',
												                        'How can I fetch the file Handbook.pdf from the pes.edu website, resume it if it has been partially downloaded and show the current speed in bits?',
                                                                        'Fetch the Handbook.pdf resource from the pes.edu website, resume it if it has been partially downloaded and show the current speed in bits.',
                                                                        'How do I download the logo.png resource from the pes.edu website, continue downloading it if it has been partially downloaded and show the current speed in bits?']},ignore_index=True)

wget = wget.append({'Command':'wget --report-speed=bits pes.edu/logo.png --timeout=20','NL Queries':['Downloads the logo.png file from the website pes.edu with a 20 second timeout if the request isn\'t complete and show the current speed in bits.',
												                        'How can I fetch the file logo.png from the pes.edu website, set a timeout for 20 seconds and show the current speed in bits?',
                                                                        'Fetch the logo.png resource from the pes.edu website, a timeout of 20 seconds if the server isn\'t responding and show the current speed in bits.',
                                                                        'How do I download the logo.png resource from the pes.edu website, set a timeout of 20 seconds and show the current speed in bits?']},ignore_index=True)

wget = wget.append({'Command':'wget --report-speed=bits pes.edu/logo.png --wait=20','NL Queries':['Downloads the logo.png file from the website pes.edu, tries downloading with an interval of 20 seconds if the server hasn\'t responded and show the current speed in bits.',
												                        'How can I fetch the file logo.png from the pes.edu website, try downloading in an interval of 20 seconds if the request isn\'t complete and show the current speed in bits?',
                                                                        'Fetch the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and show the current speed in bits.',
                                                                        'How do I download the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and show the current speed in bits?']},ignore_index=True)

wget = wget.append({'Command':'wget --report-speed=bits -r pes.edu/wp-content/','NL Queries':['Downloads the contents of the folder wp-content of the website pes.edu recursively and show the current speed in bits.',
												                        'How can I fetch the contents of the directory wp-contents of the website pes.edu recursively and show the current speed in bits?',
                                                                        'Fetch the contents of the directory wp-contents of the website pes.edu recursively and show the current speed in bits.',
                                                                        'How do I download the contents of the folder wp-contents of the website pes.edu recursively and show the current speed in bits?']},ignore_index=True)

#report speed

wget = wget.append({'Command':'wget --tries=3 pes.edu/logo.png','NL Queries':['Downloads the logo.png file from the website pes.edu, try downloading 3 times if an error has occured.',
												                        'How can I fetch the file logo.png from the pes.edu website, try downloading 3 times if an error has occured?',
                                                                        'Fetch the logo.png resource from the pes.edu website, try downloading 3 times if an error has occured.',
                                                                        'How do I download the logo.png resource from the pes.edu website, try downloading 3 times if an error has occured?']},ignore_index=True)


wget = wget.append({'Command':'wget --tries=3 pes.edu/logo.png -o output.txt','NL Queries':['Downloads the logo.png file from the website pes.edu, create a log file named output.txt and try downloading 3 times if an error has occured.',
												                        'How can I fetch the file logo.png from the pes.edu website, copy the log details to output.txt and try downloading 3 times if an error has occured?',
                                                                        'Fetch the logo.png resource from the pes.edu website, create a log file output.txt and try downloading 3 times if an error has occured.',
                                                                        'How do I download the logo.png resource from the pes.edu website, make a log file output.txt and try downloading 3 times if an error has occured?']},ignore_index=True)

wget = wget.append({'Command':'wget --tries=3 -q pes.edu/logo.png','NL Queries':['Downloads the logo.png file from the website pes.edu, shows no details on the terminal screen and try downloading 3 times if an error has occured.',
												                        'How can I fetch the file logo.png from the pes.edu website, prevent messages from being shown on the terminal screen and try downloading 3 times if an error has occured?',
                                                                        'Fetch the logo.png resource from the pes.edu website, prevent messages from being shown on the terminal screen and try downloading 3 times if an error has occured.',
                                                                        'How do I download the logo.png resource from the pes.edu website, make sure no details are shown on the terminal and try downloading 3 times if an error has occured?']},ignore_index=True)

wget = wget.append({'Command':'wget --tries=3 pes.edu/logo.png --report-speed=bits','NL Queries':['Downloads the logo.png file from the website pes.edu, show the current speed in bits and try downloading 3 times if an error has occured.',
												                        'How can I fetch the file logo.png from the pes.edu website, show the current speed in bits and try downloading 3 times if an error has occured?',
                                                                        'Fetch the logo.png resource from the pes.edu website, show the current speed in bits and try downloading 3 times if an error has occured.',
                                                                        'How do I download the logo.png resource from the pes.edu website, show the current speed in bits and try downloading 3 times if an error has occured?']},ignore_index=True)

wget = wget.append({'Command':'wget --tries=3 pes.edu/instructions.txt --output-document=new_inst.txt','NL Queries':['Downloads the instructions.txt file from the website pes.edu, copy the contents of the file to new_inst.txt and try downloading 3 times if an error has occured.',
												                        'How can I fetch the file instructions.txt from the pes.edu website, dump the contents of the file to new_inst.txt and try downloading 3 times if an error has occured?',
                                                                        'Fetch the instructions.txt resource from the pes.edu website, put the contents of the file into new_inst.txt and try downloading 3 times if an error has occured.',
                                                                        'How do I download the instructions.txt resource from the pes.edu website, paste the contents of the file into new_inst.txt and try downloading 3 times if an error has occured?']},ignore_index=True)

wget = wget.append({'Command':'wget --tries=3 -c pes.edu/Handbook.pdf','NL Queries':['Downloads the Handbook.pdf file from the website pes.edu, resumes it if it has been partially downloaded and try downloading 3 times if an error has occured.',
												                        'How can I fetch the file Handbook.pdf from the pes.edu website, resume it if it has been partially downloaded and try downloading 3 times if an error has occured?',
                                                                        'Fetch the Handbook.pdf resource from the pes.edu website, resume it if it has been partially downloaded and try downloading 3 times if an error has occured.',
                                                                        'How do I download the logo.png resource from the pes.edu website, continue downloading it if it has been partially downloaded and try downloading 3 times if an error has occured?']},ignore_index=True)

wget = wget.append({'Command':'wget --tries=3 pes.edu/logo.png --timeout=20','NL Queries':['Downloads the logo.png file from the website pes.edu with a 20 second timeout if the request isn\'t complete and try downloading 3 times if an error has occured.',
												                        'How can I fetch the file logo.png from the pes.edu website, set a timeout for 20 seconds and try downloading 3 times if an error has occured?',
                                                                        'Fetch the logo.png resource from the pes.edu website, a timeout of 20 seconds if the server isn\'t responding and try downloading 3 times if an error has occured.',
                                                                        'How do I download the logo.png resource from the pes.edu website, set a timeout of 20 seconds and try downloading 3 times if an error has occured?']},ignore_index=True)

wget = wget.append({'Command':'wget --tries=3 pes.edu/logo.png --wait=20','NL Queries':['Downloads the logo.png file from the website pes.edu, tries downloading with an interval of 20 seconds if the server hasn\'t responded and try downloading 3 times if an error has occured.',
												                        'How can I fetch the file logo.png from the pes.edu website, try downloading in an interval of 20 seconds if the request isn\'t complete and try downloading 3 times if an error has occured?',
                                                                        'Fetch the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and try downloading 3 times if an error has occured.',
                                                                        'How do I download the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and try downloading 3 times if an error has occured?']},ignore_index=True)

wget = wget.append({'Command':'wget --tries=3 -r pes.edu/wp-content/','NL Queries':['Downloads the contents of the folder wp-content of the website pes.edu recursively and show the current speed in bits.',
												                        'How can I fetch the contents of the directory wp-contents of the website pes.edu recursively and show the current speed in bits?',
                                                                        'Fetch the contents of the directory wp-contents of the website pes.edu recursively and show the current speed in bits.',
                                                                        'How do I download the contents of the folder wp-contents of the website pes.edu recursively and show the current speed in bits?']},ignore_index=True)

#try

wget = wget.append({'Command':'wget -c pes.edu/logo.png','NL Queries':['Downloads the logo.png file from the website pes.edu, resumes it if it has been partially downloaded.',
												                        'How can I fetch the file logo.png from the pes.edu website, resume it if it has been partially downloaded?',
                                                                        'Fetch the logo.png resource from the pes.edu website, resumes it if it has been partially downloaded.',
                                                                        'How do I download the logo.png resource from the pes.edu website, resume it if it has been partially downloaded?']},ignore_index=True)


wget = wget.append({'Command':'wget -c pes.edu/logo.png -o output.txt','NL Queries':['Downloads the logo.png file from the website pes.edu, create a log file named output.txt and resumes it if it has been partially downloaded.',
												                        'How can I fetch the file logo.png from the pes.edu website, copy the log details to output.txt and resume it if it has been partially downloaded?',
                                                                        'Fetch the logo.png resource from the pes.edu website, create a log file output.txt and resumes it if it has been partially downloaded.',
                                                                        'How do I download the logo.png resource from the pes.edu website, make a log file output.txt and resume it if it has been partially downloaded?']},ignore_index=True)

wget = wget.append({'Command':'wget -c -q pes.edu/logo.png','NL Queries':['Downloads the logo.png file from the website pes.edu, shows no details on the terminal screen and resumes it if it has been partially downloaded.',
												                        'How can I fetch the file logo.png from the pes.edu website, prevent messages from being shown on the terminal screen and resume it if it has been partially downloaded?',
                                                                        'Fetch the logo.png resource from the pes.edu website, prevent messages from being shown on the terminal screen and resumes it if it has been partially downloaded.',
                                                                        'How do I download the logo.png resource from the pes.edu website, make sure no details are shown on the terminal and resume it if it has been partially downloaded?']},ignore_index=True)

wget = wget.append({'Command':'wget -c pes.edu/logo.png --report-speed=bits','NL Queries':['Downloads the logo.png file from the website pes.edu, show the current speed in bits and resumes it if it has been partially downloaded.',
												                        'How can I fetch the file logo.png from the pes.edu website, show the current speed in bits and resume it if it has been partially downloaded?',
                                                                        'Fetch the logo.png resource from the pes.edu website, show the current speed in bits and resumes it if it has been partially downloaded.',
                                                                        'How do I download the logo.png resource from the pes.edu website, show the current speed in bits and resume it if it has been partially downloaded?']},ignore_index=True)

wget = wget.append({'Command':'wget -c pes.edu/instructions.txt --output-document=new_inst.txt','NL Queries':['Downloads the instructions.txt file from the website pes.edu, copy the contents of the file to new_inst.txt and resumes it if it has been partially downloaded.',
												                        'How can I fetch the file instructions.txt from the pes.edu website, dump the contents of the file to new_inst.txt and resume it if it has been partially downloaded?',
                                                                        'Fetch the instructions.txt resource from the pes.edu website, put the contents of the file into new_inst.txt and resumes it if it has been partially downloaded.',
                                                                        'How do I download the instructions.txt resource from the pes.edu website, paste the contents of the file into new_inst.txt and resume it if it has been partially downloaded?']},ignore_index=True)

wget = wget.append({'Command':'wget -c pes.edu/logo.png --timeout=20','NL Queries':['Downloads the logo.png file from the website pes.edu with a 20 second timeout if the request isn\'t complete and resumes it if it has been partially downloaded.',
												                        'How can I fetch the file logo.png from the pes.edu website, set a timeout for 20 seconds and resume it if it has been partially downloaded?',
                                                                        'Fetch the logo.png resource from the pes.edu website, a timeout of 20 seconds if the server isn\'t responding and resumes it if it has been partially downloaded.',
                                                                        'How do I download the logo.png resource from the pes.edu website, set a timeout of 20 seconds and resume it if it has been partially downloaded?']},ignore_index=True)

wget = wget.append({'Command':'wget -c pes.edu/logo.png --wait=20','NL Queries':['Downloads the logo.png file from the website pes.edu, tries downloading with an interval of 20 seconds if the server hasn\'t responded and resumes it if it has been partially downloaded.',
												                        'How can I fetch the file logo.png from the pes.edu website, try downloading in an interval of 20 seconds if the request isn\'t complete and resume it if it has been partially downloaded?',
                                                                        'Fetch the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and resumes it if it has been partially downloaded.',
                                                                        'How do I download the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and resume it if it has been partially downloaded?']},ignore_index=True)

wget = wget.append({'Command':'wget -c -r pes.edu/wp-content/','NL Queries':['Downloads the contents of the folder wp-content of the website pes.edu recursively and resumes it if it has been partially downloaded.',
												                        'How can I fetch the contents of the directory wp-contents of the website pes.edu recursively and resume it if it has been partially downloaded?',
                                                                        'Fetch the contents of the directory wp-contents of the website pes.edu recursively and resumes it if it has been partially downloaded.',
                                                                        'How do I download the contents of the folder wp-contents of the website pes.edu recursively and resume it if it has been partially downloaded?']},ignore_index=True)

#continue

wget = wget.append({'Command':'wget --timeout=30 pes.edu/logo.png','NL Queries':['Downloads the logo.png file from the website pes.edu, set a timeout of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website and set a timeout of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website and set a timeout of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the logo.png resource from the pes.edu website and set a timeout of 30 seconds if the request isn\'t complete?']},ignore_index=True)


wget = wget.append({'Command':'wget --timeout=30 pes.edu/logo.png -o output.txt','NL Queries':['Downloads the logo.png file from the website pes.edu, create a log file named output.txt and set a timeout of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website and copy the log details to output.txt and set a timeout of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website and create a log file output.txt and set a timeout of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the logo.png resource from the pes.edu website and make a log file output.txt and set a timeout of 30 seconds if the request isn\'t complete?']},ignore_index=True)

wget = wget.append({'Command':'wget --timeout=30 -q pes.edu/logo.png','NL Queries':['Downloads the logo.png file from the website pes.edu, shows no details on the terminal screen and set a timeout of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website and prevent messages from being shown on the terminal screen and set a timeout of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website and prevent messages from being shown on the terminal screen and set a timeout of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the logo.png resource from the pes.edu website and make sure no details are shown on the terminal and set a timeout of 30 seconds if the request isn\'t complete?']},ignore_index=True)

wget = wget.append({'Command':'wget --timeout=30 pes.edu/logo.png --report-speed=bits','NL Queries':['Downloads the logo.png file from the website pes.edu, show the current speed in bits and set a timeout of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website and show the current speed in bits and set a timeout of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website and show the current speed in bits and set a timeout of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the logo.png resource from the pes.edu website and show the current speed in bits and set a timeout of 30 seconds if the request isn\'t complete?']},ignore_index=True)

wget = wget.append({'Command':'wget --timeout=30 pes.edu/instructions.txt --output-document=new_inst.txt','NL Queries':['Downloads the instructions.txt file from the website pes.edu, copy the contents of the file to new_inst.txt and set a timeout of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file instructions.txt from the pes.edu website and dump the contents of the file to new_inst.txt and set a timeout of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the instructions.txt resource from the pes.edu website and put the contents of the file into new_inst.txt and set a timeout of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the instructions.txt resource from the pes.edu website and paste the contents of the file into new_inst.txt and set a timeout of 30 seconds if the request isn\'t complete?']},ignore_index=True)

wget = wget.append({'Command':'wget --timeout=30 pes.edu/logo.png --wait=20','NL Queries':['Downloads the logo.png file from the website pes.edu, tries downloading with an interval of 20 seconds if the server hasn\'t responded and set a timeout of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website and try downloading in an interval of 20 seconds if the request isn\'t complete and set a timeout of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website and try downloading at an interval of 20 seconds if the server isn\'t responding and set a timeout of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the logo.png resource from the pes.edu website, try downloading at an interval of 20 seconds if the server isn\'t responding and set a timeout of 30 seconds if the request isn\'t complete?']},ignore_index=True)

wget = wget.append({'Command':'wget --timeout=30 -r pes.edu/wp-content/','NL Queries':['Downloads the contents of the folder wp-content of the website pes.edu recursively and set a timeout of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the contents of the directory wp-contents of the website pes.edu recursively and set a timeout of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the contents of the directory wp-contents of the website pes.edu recursively and set a timeout of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the contents of the folder wp-contents of the website pes.edu recursively and set a timeout of 30 seconds if the request isn\'t complete?']},ignore_index=True)

#timeout

wget = wget.append({'Command':'wget --wait=30 pes.edu/logo.png','NL Queries':['Downloads the logo.png file from the website pes.edu and try downloading at an interval of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website and try downloading at an interval of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website and try downloading at an interval of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the logo.png resource from the pes.edu website and try downloading at an interval of 30 seconds if the request isn\'t complete?']},ignore_index=True)


wget = wget.append({'Command':'wget --wait=30 pes.edu/logo.png -o output.txt','NL Queries':['Downloads the logo.png file from the website pes.edu and create a log file named output.txt and try downloading at an interval of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website and copy the log details to output.txt and try downloading at an interval of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website and create a log file output.txt and try downloading at an interval of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the logo.png resource from the pes.edu website and make a log file output.txt and try downloading at an interval of 30 seconds if the request isn\'t complete?']},ignore_index=True)

wget = wget.append({'Command':'wget --wait=30 -q pes.edu/logo.png','NL Queries':['Downloads the logo.png file from the website pes.edu and shows no details on the terminal screen and try downloading at an interval of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website and prevent messages from being shown on the terminal screen and try downloading at an interval of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website and prevent messages from being shown on the terminal screen and try downloading at an interval of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the logo.png resource from the pes.edu website and make sure no details are shown on the terminal and try downloading at an interval of 30 seconds if the request isn\'t complete?']},ignore_index=True)

wget = wget.append({'Command':'wget --wait=30 pes.edu/logo.png --report-speed=bits','NL Queries':['Downloads the logo.png file from the website pes.edu and show the current speed in bits and try downloading at an interval of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file logo.png from the pes.edu website and show the current speed in bits and try downloading at an interval of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the logo.png resource from the pes.edu website and show the current speed in bits and try downloading at an interval of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the logo.png resource from the pes.edu website and show the current speed in bits and try downloading at an interval of 30 seconds if the request isn\'t complete?']},ignore_index=True)

wget = wget.append({'Command':'wget --wait=30 pes.edu/instructions.txt --output-document=new_inst.txt','NL Queries':['Downloads the instructions.txt file from the website pes.edu and copy the contents of the file to new_inst.txt and try downloading at an interval of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the file instructions.txt from the pes.edu website and dump the contents of the file to new_inst.txt and try downloading at an interval of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the instructions.txt resource from the pes.edu website and put the contents of the file into new_inst.txt and try downloading at an interval of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the instructions.txt resource from the pes.edu website and paste the contents of the file into new_inst.txt and try downloading at an interval of 30 seconds if the request isn\'t complete?']},ignore_index=True)

wget = wget.append({'Command':'wget --wait=30 -r pes.edu/wp-content/','NL Queries':['Downloads the contents of the folder wp-content of the website pes.edu recursively and try downloading at an interval of 30 seconds if the request isn\'t complete.',
												                        'How can I fetch the contents of the directory wp-contents of the website pes.edu recursively and try downloading at an interval of 30 seconds if the request isn\'t complete?',
                                                                        'Fetch the contents of the directory wp-contents of the website pes.edu recursively and try downloading at an interval of 30 seconds if the request isn\'t complete.',
                                                                        'How do I download the contents of the folder wp-contents of the website pes.edu recursively and try downloading at an interval of 30 seconds if the request isn\'t complete?']},ignore_index=True)

#wait


print(wget.shape)