import pandas as pd 

more = pd.DataFrame(columns = ['Command','NL Queries'])

more = more.append({'Command':'more instructions.txt',
				'NL Queries':['Show content of instructions.txt enough to fit the command line.',
							'How do I see a part of the file instructions.txt which fits the command line?',
							'Show as much content of instructions.txt on the terminal.']},ignore_index=True)

more = more.append({'Command':'more -V myfile.txt',
				'NL Queries':['Display version of \'more\' command and exit.',
							'Show the version of \'more command\'.',
							'How do i know the version of \'more command\'.']},ignore_index=True)

more = more.append({'Command':'more --help myfile.txt',
				'NL Queries':['Display \'more\' command help.',
							'How do i know the man of \'more\' command?',
							'Show the help of \'more\' command.']},ignore_index=True)

more = more.append({'Command':'more +/"hope" myfile.txt',
				'NL Queries':['Display the contents of file myfile.txt enough to fit the command line, from beginning and check if file contains the string "hope".',
							'How do i see the contents of file myfile.txt enough to fit the command line and check if the file contains the word "hope"?',
							'Show the contents of file myfile.txt enough to fit the command line. Check if the file contains the word "hope".']},ignore_index=True)

more = more.append({'Command':'more +3 myfile.txt',
				'NL Queries':['Show contents of myfile.txt starting from line \'3\', enough to fit the command line.',
							'Display contents of myfile.txt enough to fit the command line. Skip first 2 lines. Show only as much content as it fits the terminal.',
							'How do i see contents of myfile.txt from 3rd line and enough to fit the command line?',
							'Jump to 3rd line then display contents of myfile.txt']},ignore_index=True)

more = more.append({'Command':'more -3 myfile.txt',
				'NL Queries':['Show contents of myfile.txt with \'3\' lines per screenful.',
							'Display contents of myfile.txt. Show only as much content as it fits for \'3\' lines.',
							'How do i see the contents in file myfile.txt with screen lines to use set as \'3\'?']},ignore_index=True)



more = more.append({'Command':'more -p myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line.',
							'Display contents of myfile.txt from next page of command line.',
							'How to see the contents of myfile.txt? Display from next page of command line.']},ignore_index=True)

more = more.append({'Command':'more -u myfile.txt',
				'NL Queries':['Show contents of myfile.txt enough to fit the command line. Suppress underlining.',
							'Display contents of myfile.txt enough to fit the command line. Do not show underlines.',
							'How do i see the contents of myfile.txt suppressing underlining?']},ignore_index=True)

more = more.append({'Command':'more -d -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\' and with prompting help instead of ringing the bell when an illegal key is pressed?']},ignore_index=True)

more = more.append({'Command':'more -f myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Count logical lines rather than screen lines.',
							'Display contents of myfile.txt. Count logical lines and not screen lines.',
							'How do i see contents of myfile.txt with counting logical lines instead of screen lines?']},ignore_index=True)

more = more.append({'Command':'more -s myfile.txt',
				'NL Queries':['Show contents of myfile.txt enough to fit the command line. Squeeze multiple blank lines into one.',
							'Display contents of myfile.txt and squeeze multiple blank lines into one.',
							'How do i see contents of myfile.txt enough to fit the command line and squeezing multiple empty lines?']},ignore_index=True)

more = more.append({'Command':'more -c myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line.',
							'Display contents of myfile.txt enough to fit the command line. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt?',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line.']},ignore_index=True)

more = more.append({'Command':'more -l myfile.txt',
				'NL Queries':['Show contents of myfile.txt enough to fit the command line. Do not pause after form feed.',
							'Display output of myfile.txt without pausing after any occurence of form feed.',
							'How to get contents of myfile.txt enough to fit the command line? Do not pause after any form feed.']},ignore_index=True)



#-p option combinations
more = more.append({'Command':'more -pd -10 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Set screen lines to use as \'10\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed and set number of display lines to \'10\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed and screen size set as \'10\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Set screen lines to use as \'10\'.']},ignore_index=True)

more = more.append({'Command':'more -pl myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Do not pause after any form feed.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line without pausing after any occurence of form feed.',
							'How to display contents of myfile.txt from next page of command line? Do not pause after any form feed.',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -pf +5 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Start from \'5\'th line in myfile.txt. Count logical lines instead of screen lines.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line without folding long lines. Skip first \'4\' lines.',
							'How to display contents of myfile.txt from \'5\'th line in next page of command line enough to fit the command line without folding long lines?',
							'Move to next page of command line. Show the contents of myfile.txt starting from \'5\'th line. Do not fold long lines.']},ignore_index=True)

more = more.append({'Command':'more -ps myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Squeeze multiple blank lines into one.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line, squeezing multiple blank lines into one.',
							'How to display contents of myfile.txt from next page of command line enough to fit the command line with squeeze multiple blank lines into one?',
							'Move to next page of command line. Show the contents of myfile.txt . Squeeze multiple empty lines into one.']},ignore_index=True)

more = more.append({'Command':'more -pu myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Suppress underlining.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line, suppressing underlines.',
							'How to display contents of myfile.txt from next page of command line enough to fit the command line? Do not show underlines.',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Suppress underlines.']},ignore_index=True)

more = more.append({'Command':'more -pdl -20 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Set number of display lines to \'20\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, do not pause for any form feed and set number of display lines to \'20\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, without pausing after any occurence of form feed and screen size set as \'20\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Set number of lines for display as \'20\'.']},ignore_index=True)

more = more.append({'Command':'more -pdf -5 +8 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines instead of screen lines. Set screen lines to use as \'5\'. Skip first \'7\' lines.',
							'Display the contents of myfile.txt from next page of command line  without folding long lines, with prompting help instead of ringing the bell when an illegal key is pressed and set number of display lines to \'5\'. Start from \'8\'th line.',
							'How to display contents of myfile.txt from \'8\'th line in next page of command line with prompt instead of ringing bell when an illegal key is pressed, without folding long lines and screen size set as \'5\'?',
							'Move to next page of command line. Show the contents of myfile.txt starting from \'8\'th line. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines. Set screen lines to use as \'5\'.']},ignore_index=True)

more = more.append({'Command':'more -pds -7 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines into one. Set screen lines to use as \'7\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed and squeeze multiple blank lines into one and set number of display lines to \'7\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed and squeezeing multiple blank lines into one and screen size set as \'7\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines into one. Set number of lines for display as \'7\'.']},ignore_index=True)

more = more.append({'Command':'more -pdu -12 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Set number of display lines to \'12\'',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, with suppressing underlines and screen size set to \'12\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed and with suppressing underlines and set screen size as \'12\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not show underlines. Set number of lines for display as \'12\'']},ignore_index=True)

more = more.append({'Command':'more -pfl myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Count logical lines instead of screen lines. Do not pause after any form feed.',
							'Display the contents of myfile.txt from next page of command line without folding long lines and do not pause after any form feed.',
							'How to display contents of myfile.txt from next page of command line enough to fit the command line, without folding long lines and do not pause after any form feed.?',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -pls myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line without pausing after any occurence of form feed and squeezing multiple empty lines.',
							'How to display contents of myfile.txt from next page of command line? Do not pause after any form feed and squeeze multiple empty lines.',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines into one.']},ignore_index=True)

more = more.append({'Command':'more -plu myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Do not pause after any form feed. Suppress underlining.',
							'Display the contents of myfile.txt from next page of command line without pausing after any occurence of form feed and do not show underlines.',
							'How to display contents of myfile.txt from next page of command line without underlines? Do not pause after any form feed.',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Suppress underlining.']},ignore_index=True)

more = more.append({'Command':'more -pfs myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Count logical lines instead of screen lines. Squeeze multiple blank lines.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line without folding long lines and squeezing multiple blank lines.',
							'How to display contents of myfile.txt from next page of command line enough to fit the command line without folding long lines and squeeze multiple empty lines into one?',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Squeeze multiple empty lines.']},ignore_index=True)

more = more.append({'Command':'more -pfu myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Count logical lines instead of screen lines. Suppress underlining.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line without folding long lines and suppessing underlines.',
							'How to display contents of myfile.txt from next page of command line without folding long lines and not showing underlines?',
							'Move to next page of command line. Show the contents of myfile.txt. Do not fold long lines. Suppress underlines.']},ignore_index=True)

more = more.append({'Command':'more -psu myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Suppress underlining. Squeeze multiple blank lines.',
							'Display the contents of myfile.txt from next page of command line suppressing underlines and squeezing multiple empty lines into one.',
							'How to display contents of myfile.txt from next page of command line enough to fit the command line? Do not show underlines and squeeze mutliple empty lines.',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Suppress underlines. Squeeze multiple empty lines into one.']},ignore_index=True)

more = more.append({'Command':'more -pdlf -25 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Use count logical lines instead of screen lines. Set number of display lines to \'25\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, without folding long lines, do not pause for any form feed and set number of display lines to \'25\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, without folding long lines, without pausing after any occurence of form feed and screen size set as \'25\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Do logical lines count instead of screen lines. Set number of lines for display as \'25\'.']},ignore_index=True)

more = more.append({'Command':'more -pdls -20 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Set number of display lines to \'20\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, squeeze multiple blank lines, do not pause for any form feed and set number of display lines to \'20\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, squeeze multiple blank lines, without pausing after any occurence of form feed and screen size set as \'20\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines into one. Do not pause after any form feed. Set number of lines for display as \'20\'.']},ignore_index=True)

more = more.append({'Command':'more -pdlu -10 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Set number of display lines to \'10\'. Suppress underlines.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, suppress underlines, do not pause for any form feed and set number of display lines to \'10\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, suppress underlining ,without pausing after any occurence of form feed and screen size set as \'10\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Set number of lines for display as \'10\'. Suppress underlines.']},ignore_index=True)

more = more.append({'Command':'more -pdfs -5 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines instead of screen lines. Squeeze multiple blank lines. Set screen lines to use as \'5\'.',
							'Display the contents of myfile.txt from next page of command line  without folding long lines, squeezing multiple blank lines into one. with prompting help instead of ringing the bell when an illegal key is pressed and set number of display lines to \'5\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, squeeze multiple empty lines into one. without folding long lines and screen size set as \'5\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines. Set screen lines to use as \'5\'. Squeeze multiple blank lines.']},ignore_index=True)

more = more.append({'Command':'more -pdfu -5 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlines. Count logical lines instead of screen lines. Set screen lines to use as \'5\'.',
							'Display the contents of myfile.txt from next page of command line  without folding long lines, with prompting help instead of ringing the bell when an illegal key is pressed, suppress underlining, and set number of display lines to \'5\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, without folding long lines, suppress underlining and screen size set as \'5\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlines. Count logical lines. Set screen lines to use as \'5\'.']},ignore_index=True)

more = more.append({'Command':'more -pfls myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Squeeze multiple blank lines into one. Count logical lines instead of screen lines. Do not pause after any form feed.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line without folding long lines, squeezing multiple blank lines and do not pause after any form feed.',
							'How to display contents of myfile.txt from next page of command line enough to fit the command line without folding long lines, squeezing multiple empty lines and do not pause after any form feed.?',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Squeeze multiple blank lines into one. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -pflu myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Count logical lines instead of screen lines. Suppress underlines. Do not pause after any form feed.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line without folding long lines, suppress underlining and do not pause after any form feed.',
							'How to display contents of myfile.txt from next page of command line without folding long lines, suppressing underlining. and do not pause after any form feed.?',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Suppress underlining. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -pdsu -7 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Squeeze multiple blank lines into one. Set screen lines to use as \'7\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, suppressing underlining and squeeze multiple blank lines into one and set number of display lines to \'7\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, suppressing underlining and squeezeing multiple blank lines into one and screen size set as \'7\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Squeeze multiple blank lines into one. Set number of lines for display as \'7\'.']},ignore_index=True)

more = more.append({'Command':'more -plsu myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines. Suppress underlines.',
							'Display the contents of myfile.txt from next page of command line without pausing after any occurence of form feed and squeezing multiple empty lines and suppressing underlining.',
							'How to display contents of myfile.txt from next page of command line enough to fit the command line? Do not pause after any form feed and squeeze multiple empty lines.',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines into one. Suppress underlining.']},ignore_index=True)

more = more.append({'Command':'more -pfsu myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Count logical lines instead of screen lines. Squeeze multiple blank lines. Suppress underlining.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line without folding long lines, suppressing underlining and squeezing multiple blank lines.',
							'How to display contents of myfile.txt from next page of command line enough to fit the command line without folding long lines, suppressing underlining and squeeze multiple empty lines into one?',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Squeeze multiple empty lines. Suppress underlining.']},ignore_index=True)

more = more.append({'Command':'more -pdlsu -20 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Suppress underlining. Set number of display lines to \'20\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, squeeze multiple blank lines, suppressing underlining, do not pause for any form feed and set number of display lines to \'20\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, squeeze multiple blank lines, suppressing underlining, without pausing after any occurence of form feed and screen size set as \'20\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines into one. Suppress underlining. Do not pause after any form feed. Set number of lines for display as \'20\'.']},ignore_index=True)

more = more.append({'Command':'more -pdlfs -25 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Use count logical lines instead of screen lines. Set number of display lines to \'25\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, squeeze multiple blank lines, without folding long lines, do not pause for any form feed and set number of display lines to \'25\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, squeezing multiple blank lines, without folding long lines, without pausing after any occurence of form feed and screen size set as \'25\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Do logical lines count instead of screen lines. Set number of lines for display as \'25\'.']},ignore_index=True)

more = more.append({'Command':'more -pdlfu -25 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Use count logical lines instead of screen lines. Suppress underlining. Set number of display lines to \'25\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, without folding long lines, suppressing underlining, do not pause for any form feed and set number of display lines to \'25\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, without folding long lines, suppressing underlines, without pausing after any occurence of form feed and screen size set as \'25\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Do logical lines count instead of screen lines. Suppress underlining. Set number of lines for display as \'25\'.']},ignore_index=True)

more = more.append({'Command':'more -pflsu myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line enough to fit the command line. Squeeze multiple blank lines into one. Count logical lines instead of screen lines. Suppress underlining. Do not pause after any form feed.',
							'Display the contents of myfile.txt from next page of command line enough to fit the command line without folding long lines, squeezing multiple blank lines, suppressing underlining and do not pause after any form feed.',
							'How to display contents of myfile.txt from next page of command line without folding long lines, squeezing multiple empty lines, suppressing underlining and do not pause after any form feed.?',
							'Move to next page of command line. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Squeeze multiple blank lines into one. Suppress underlining. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -pdfsu -5 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines instead of screen lines. Suppress underlining. Squeeze multiple blank lines. Set screen lines to use as \'5\'.',
							'Display the contents of myfile.txt from next page of command line  without folding long lines, squeezing multiple blank lines into one. with prompting help instead of ringing the bell when an illegal key is pressed, suppressing underlining and set number of display lines to \'5\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, suppress underlining, squeeze multiple empty lines into one. without folding long lines and screen size set as \'5\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines. Suppress underlining. Set screen lines to use as \'5\'. Squeeze multiple blank lines.']},ignore_index=True)

more = more.append({'Command':'more -pdlfsu -25 myfile.txt',
				'NL Queries':['Show output of myfile.txt from next page of command line. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Suppress underlining. Use count logical lines instead of screen lines. Set number of display lines to \'25\'.',
							'Display the contents of myfile.txt from next page of command line with prompting help instead of ringing the bell when an illegal key is pressed, squeeze multiple blank lines, without folding long lines, suppressing underlining, do not pause for any form feed and set number of display lines to \'25\'.',
							'How to display contents of myfile.txt from next page of command line with prompt instead of ringing bell when an illegal key is pressed, squeezing multiple blank lines, without folding long lines, suppressing underlining, without pausing after any occurence of form feed and screen size set as \'25\'?',
							'Move to next page of command line. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Suppress underlining. Do logical lines count instead of screen lines. Set number of lines for display as \'25\'.']},ignore_index=True)



#-c option combinations
more = more.append({'Command':'more -cd -10 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Set screen lines to use as \'10\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed and set number of display lines to \'10\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed and screen size set as \'10\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Set screen lines to use as \'10\'.']},ignore_index=True)

more = more.append({'Command':'more -cl +10 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt starting from \'10\'th line, enough to fit the command line. Do not pause after any form feed.',
							'Display contents of myfile.txt enough to fit the command line without pausing after any occurence of form feed. Clear the current screen before displaying content. Start displaying from \'10\'th line.',
							'How to clear the current screen and display contents of myfile.txt from \'10\'th line? Do not pause after any form feed.',
							'Clear current screen. Jump to \'10\'th line. Show the contents of myfile.txt enough to fit the command line. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -cf myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Count logical lines instead of screen lines.',
							'Display contents of myfile.txt enough to fit the command line without folding long lines. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt enough to fit the command line without folding long lines?',
							'Clear current screen. Show the contents of myfile.txt. Do not fold long lines.']},ignore_index=True)

more = more.append({'Command':'more -cs myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Squeeze multiple blank lines into one.',
							'Display contents of myfile.txt enough to fit the command line, squeezing multiple blank lines into one. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt enough to fit the command line with squeeze multiple blank lines into one?',
							'Clear current screen. Show the contents of myfile.txt . Squeeze multiple empty lines into one.']},ignore_index=True)

more = more.append({'Command':'more -cu myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Suppress underlining.',
							'Display contents of myfile.txt enough to fit the command line, suppressing underlines. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt enough to fit the command line? Do not show underlines.',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Suppress underlines.']},ignore_index=True)

more = more.append({'Command':'more -cdl -20 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Set number of display lines to \'20\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, do not pause for any form feed and set number of display lines to \'20\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, without pausing after any occurence of form feed and screen size set as \'20\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Set number of lines for display as \'20\'.']},ignore_index=True)

more = more.append({'Command':'more -cdf -5 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines instead of screen lines. Set screen lines to use as \'5\'.',
							'Display contents of myfile.txt  without folding long lines, with prompting help instead of ringing the bell when an illegal key is pressed and set number of display lines to \'5\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, without folding long lines and screen size set as \'5\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines. Set screen lines to use as \'5\'.']},ignore_index=True)

more = more.append({'Command':'more -cds -7 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines into one. Set screen lines to use as \'7\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed and squeeze multiple blank lines into one and set number of display lines to \'7\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed and squeezeing multiple blank lines into one and screen size set as \'7\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines into one. Set number of lines for display as \'7\'.']},ignore_index=True)

more = more.append({'Command':'more -cdu -12 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Set number of display lines to \'12\'',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, with suppressing underlines and screen size set to \'12\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed and with suppressing underlines and set screen size as \'12\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not show underlines. Set number of lines for display as \'12\'']},ignore_index=True)

more = more.append({'Command':'more -cfl myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Count logical lines instead of screen lines. Do not pause after any form feed.',
							'Display contents of myfile.txt without folding long lines and do not pause after any form feed. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt enough to fit the command line, without folding long lines and do not pause after any form feed.?',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -cls myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines.',
							'Display contents of myfile.txt enough to fit the command line without pausing after any occurence of form feed and squeezing multiple empty lines. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt? Do not pause after any form feed and squeeze multiple empty lines.',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines into one.']},ignore_index=True)

more = more.append({'Command':'more -clu myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Do not pause after any form feed. Suppress underlining.',
							'Display contents of myfile.txt without pausing after any occurence of form feed and do not show underlines. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt without underlines? Do not pause after any form feed.',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Suppress underlining.']},ignore_index=True)

more = more.append({'Command':'more -cfs myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Count logical lines instead of screen lines. Squeeze multiple blank lines.',
							'Display contents of myfile.txt enough to fit the command line without folding long lines and squeezing multiple blank lines. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt enough to fit the command line without folding long lines and squeeze multiple empty lines into one?',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Squeeze multiple empty lines.']},ignore_index=True)

more = more.append({'Command':'more -cfu myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Count logical lines instead of screen lines. Suppress underlining.',
							'Display contents of myfile.txt enough to fit the command line without folding long lines and suppessing underlines. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt without folding long lines and not showing underlines?',
							'Clear current screen. Show the contents of myfile.txt. Do not fold long lines. Suppress underlines.']},ignore_index=True)

more = more.append({'Command':'more -csu myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Suppress underlining. Squeeze multiple blank lines.',
							'Display contents of myfile.txt suppressing underlines and squeezing multiple empty lines into one. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt enough to fit the command line? Do not show underlines and squeeze mutliple empty lines.',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Suppress underlines. Squeeze multiple empty lines into one.']},ignore_index=True)

more = more.append({'Command':'more -cdlf -25 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Use count logical lines instead of screen lines. Set number of display lines to \'25\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, without folding long lines, do not pause for any form feed and set number of display lines to \'25\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, without folding long lines, without pausing after any occurence of form feed and screen size set as \'25\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Do logical lines count instead of screen lines. Set number of lines for display as \'25\'.']},ignore_index=True)

more = more.append({'Command':'more -cdls -20 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Set number of display lines to \'20\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, squeeze multiple blank lines, do not pause for any form feed and set number of display lines to \'20\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, squeeze multiple blank lines, without pausing after any occurence of form feed and screen size set as \'20\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines into one. Do not pause after any form feed. Set number of lines for display as \'20\'.']},ignore_index=True)

more = more.append({'Command':'more -cdlu -10 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Set number of display lines to \'10\'. Suppress underlines.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, suppress underlines, do not pause for any form feed and set number of display lines to \'10\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, suppress underlining ,without pausing after any occurence of form feed and screen size set as \'10\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Set number of lines for display as \'10\'. Suppress underlines.']},ignore_index=True)

more = more.append({'Command':'more -cdfs -5 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines instead of screen lines. Squeeze multiple blank lines. Set screen lines to use as \'5\'.',
							'Display contents of myfile.txt  without folding long lines, squeezing multiple blank lines into one. with prompting help instead of ringing the bell when an illegal key is pressed and set number of display lines to \'5\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, squeeze multiple empty lines into one. without folding long lines and screen size set as \'5\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines. Set screen lines to use as \'5\'. Squeeze multiple blank lines.']},ignore_index=True)

more = more.append({'Command':'more -cdfu -5 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlines. Count logical lines instead of screen lines. Set screen lines to use as \'5\'.',
							'Display contents of myfile.txt  without folding long lines, with prompting help instead of ringing the bell when an illegal key is pressed, suppress underlining, and set number of display lines to \'5\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, without folding long lines, suppress underlining and screen size set as \'5\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlines. Count logical lines. Set screen lines to use as \'5\'.']},ignore_index=True)

more = more.append({'Command':'more -cfls myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Squeeze multiple blank lines into one. Count logical lines instead of screen lines. Do not pause after any form feed.',
							'Display contents of myfile.txt enough to fit the command line without folding long lines, squeezing multiple blank lines and do not pause after any form feed. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt enough to fit the command line without folding long lines, squeezing multiple empty lines and do not pause after any form feed.?',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Squeeze multiple blank lines into one. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -cflu myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Count logical lines instead of screen lines. Suppress underlines. Do not pause after any form feed.',
							'Display contents of myfile.txt enough to fit the command line without folding long lines, suppress underlining and do not pause after any form feed. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt without folding long lines, suppressing underlining. and do not pause after any form feed.?',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Suppress underlining. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -cdsu -7 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Squeeze multiple blank lines into one. Set screen lines to use as \'7\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, suppressing underlining and squeeze multiple blank lines into one and set number of display lines to \'7\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, suppressing underlining and squeezeing multiple blank lines into one and screen size set as \'7\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Squeeze multiple blank lines into one. Set number of lines for display as \'7\'.']},ignore_index=True)

more = more.append({'Command':'more -clsu myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines. Suppress underlines.',
							'Display contents of myfile.txt without pausing after any occurence of form feed and squeezing multiple empty lines and suppressing underlining. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt enough to fit the command line? Do not pause after any form feed and squeeze multiple empty lines.',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines into one. Suppress underlining.']},ignore_index=True)

more = more.append({'Command':'more -cfsu myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Count logical lines instead of screen lines. Squeeze multiple blank lines. Suppress underlining.',
							'Display contents of myfile.txt enough to fit the command line without folding long lines, suppressing underlining and squeezing multiple blank lines. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt enough to fit the command line without folding long lines, suppressing underlining and squeeze multiple empty lines into one?',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Squeeze multiple empty lines. Suppress underlining.']},ignore_index=True)

more = more.append({'Command':'more -cdlsu -20 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Suppress underlining. Set number of display lines to \'20\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, squeeze multiple blank lines, suppressing underlining, do not pause for any form feed and set number of display lines to \'20\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, squeeze multiple blank lines, suppressing underlining, without pausing after any occurence of form feed and screen size set as \'20\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines into one. Suppress underlining. Do not pause after any form feed. Set number of lines for display as \'20\'.']},ignore_index=True)

more = more.append({'Command':'more -cdlfs -25 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Use count logical lines instead of screen lines. Set number of display lines to \'25\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, squeeze multiple blank lines, without folding long lines, do not pause for any form feed and set number of display lines to \'25\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, squeezing multiple blank lines, without folding long lines, without pausing after any occurence of form feed and screen size set as \'25\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Do logical lines count instead of screen lines. Set number of lines for display as \'25\'.']},ignore_index=True)

more = more.append({'Command':'more -cdlfu -25 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Use count logical lines instead of screen lines. Suppress underlining. Set number of display lines to \'25\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, without folding long lines, suppressing underlining, do not pause for any form feed and set number of display lines to \'25\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, without folding long lines, suppressing underlines, without pausing after any occurence of form feed and screen size set as \'25\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Do logical lines count instead of screen lines. Suppress underlining. Set number of lines for display as \'25\'.']},ignore_index=True)

more = more.append({'Command':'more -cflsu myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt enough to fit the command line. Squeeze multiple blank lines into one. Count logical lines instead of screen lines. Suppress underlining. Do not pause after any form feed.',
							'Display contents of myfile.txt enough to fit the command line without folding long lines, squeezing multiple blank lines, suppressing underlining and do not pause after any form feed. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt without folding long lines, squeezing multiple empty lines, suppressing underlining and do not pause after any form feed.?',
							'Clear current screen. Show the contents of myfile.txt enough to fit the command line. Do not fold long lines. Squeeze multiple blank lines into one. Suppress underlining. Do not pause after any form feed.']},ignore_index=True)

more = more.append({'Command':'more -cdfsu -5 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines instead of screen lines. Suppress underlining. Squeeze multiple blank lines. Set screen lines to use as \'5\'.',
							'Display contents of myfile.txt  without folding long lines, squeezing multiple blank lines into one. with prompting help instead of ringing the bell when an illegal key is pressed, suppressing underlining and set number of display lines to \'5\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, suppress underlining, squeeze multiple empty lines into one. without folding long lines and screen size set as \'5\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines. Suppress underlining. Set screen lines to use as \'5\'. Squeeze multiple blank lines.']},ignore_index=True)

more = more.append({'Command':'more -cdlfsu -25 myfile.txt',
				'NL Queries':['Clear current screen and show output of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Suppress underlining. Use count logical lines instead of screen lines. Set number of display lines to \'25\'.',
							'Display contents of myfile.txt with prompting help instead of ringing the bell when an illegal key is pressed, squeeze multiple blank lines, without folding long lines, suppressing underlining, do not pause for any form feed and set number of display lines to \'25\'. Clear the current screen before displaying content.',
							'How to clear the current screen and display contents of myfile.txt with prompt instead of ringing bell when an illegal key is pressed, squeezing multiple blank lines, without folding long lines, suppressing underlining, without pausing after any occurence of form feed and screen size set as \'25\'?',
							'Clear current screen. Show the contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines. Do not pause after any form feed. Suppress underlining. Do logical lines count instead of screen lines. Set number of lines for display as \'25\'.']},ignore_index=True)









#other options combinations
more = more.append({'Command':'more -dl -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Do not pause after any form feed. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, do not pause after any form feed, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', with prompting help instead of ringing the bell when an illegal key is pressed and not pausing after any form feed?']},ignore_index=True)

more = more.append({'Command':'more -df -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines rather than screen lines. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, count logical lines rather than screen lines, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\' and with prompting help instead of ringing the bell when an illegal key is pressed? Count logical lines rather than screen lines.']},ignore_index=True)

more = more.append({'Command':'more -ds -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Squeeze multiple blank lines into one. Display prompt instead of ringing bell when an illegal key is pressed. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, squeezing multiple blank lines into one, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\' and with prompting help instead of ringing the bell when an illegal key is pressed and squeezing multiple blank lines into one?']},ignore_index=True)

more = more.append({'Command':'more -du -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, suppressing underlining, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\' and with prompting help instead of ringing the bell when an illegal key is pressed and suppress underlining?']},ignore_index=True)

more = more.append({'Command':'more -fs myfile.txt',
				'NL Queries':['Show contents of myfile.txt enough to fit the command line. Count logical lines rather than screen lines. Squeeze multiple blank lines into one.',
							'Display contents of myfile.txt with squeezing multiple blank lines into one. Count logical lines and not screen lines.',
							'How do i see contents of myfile.txt enough to fit the command line with counting logical lines instead of screen lines and squeezing multiple empty lines into one?']},ignore_index=True)

more = more.append({'Command':'more -fu myfile.txt',
				'NL Queries':['Show contents of myfile.txt enough to fit the command line. Suppress underlining. Count logical lines rather than screen lines.',
							'Display contents of myfile.txt enough to fit the command line with suppressing underlines. Count logical lines and not screen lines.',
							'How do i see contents of myfile.txt enough to fit the command line with counting logical lines instead of screen lines and suppressing underlines?']},ignore_index=True)

more = more.append({'Command':'more -su myfile.txt',
				'NL Queries':['Show output of myfile.txt enough to fit the command line. Suppress underlining. Squeeze multiple blank lines.',
							'Display contents of myfile.txt enough to fit the command line suppressing underlines and squeezing multiple empty lines into one.',
							'How to display contents of myfile.txt enough to fit the command line? Do not show underlines and squeeze mutliple empty lines.',
							'Show the contents of myfile.txt enough to fit the command line. Suppress underlines. Squeeze multiple empty lines into one.']},ignore_index=True)

more = more.append({'Command':'more -lf myfile.txt',
				'NL Queries':['Show contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Count logical lines rather than screen lines.',
							'Display contents of myfile.txt without pausing after any form feed. Count logical lines and not screen lines.',
							'How do i see contents of myfile.txt enough to fit the command line with counting logical lines instead of screen lines and not pausing after any form feed?']},ignore_index=True)

more = more.append({'Command':'more -ls myfile.txt',
				'NL Queries':['Show output of myfile.txt. Do not pause after any form feed. Squeeze multiple blank lines.',
							'Display contents of myfile.txt without pausing after any occurence of form feed and squeezing multiple empty lines.',
							'How to display contents of myfile.txt enough to fit the command line? Do not pause after any form feed and squeeze multiple empty lines.',
							'Show the contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines into one.']},ignore_index=True)

more = more.append({'Command':'more -lu myfile.txt',
				'NL Queries':['Show output of myfile.txt enough to fit the command line. Do not pause after any form feed. Suppress underlining.',
							'Display contents of myfile.txt without pausing after any occurence of form feed and do not show underlines.',
							'How to display contents of myfile.txt without underlines? Do not pause after any form feed.',
							'Show the contents of myfile.txt. Do not pause after any form feed. Suppress underlining.']},ignore_index=True)

more = more.append({'Command':'more -dfl -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Do not pause after any form feed. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines rather than screen lines. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, do not pause after any form feed, count logical lines rather than screen lines, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', not pausing after any form feed and with prompting help instead of ringing the bell when an illegal key is pressed? Count logical lines rather than screen lines.']},ignore_index=True)

more = more.append({'Command':'more -dls -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple empty lines. Do not pause after any form feed. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, squeezing multiple empty lines, do not pause after any form feed, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', with prompting help instead of ringing the bell when an illegal key is pressed and not pausing after any form feed and squeezing multiple empty lines?']},ignore_index=True)

more = more.append({'Command':'more -dlu -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Do not pause after any form feed. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, suppress underlining, do not pause after any form feed, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', suppressing underlining, with prompting help instead of ringing the bell when an illegal key is pressed and not pausing after any form feed?']},ignore_index=True)

more = more.append({'Command':'more -lfs myfile.txt',
				'NL Queries':['Show contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Count logical lines rather than screen lines. Squeeze multiple empty lines.',
							'Display contents of myfile.txt enough to fit the command line without pausing after any form feed and squeezing multiple empty lines. Count logical lines and not screen lines.',
							'How do i see contents of myfile.txt enough to fit the command line with counting logical lines instead of screen lines, squeezing multiple blank lines into one and not pausing after any form feed?']},ignore_index=True)

more = more.append({'Command':'more -lfu myfile.txt',
				'NL Queries':['Show contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Suppress underlining. Count logical lines rather than screen lines.',
							'Display contents of myfile.txt enough to fit the command line without pausing after any form feed and suppressing underlining. Count logical lines and not screen lines.',
							'How do i see contents of myfile.txt enough to fit the command line with counting logical lines instead of screen lines, suppressing underlining and not pausing after any form feed?']},ignore_index=True)

more = more.append({'Command':'more -fsu myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Count logical lines rather than screen lines. Suppress underlining. Squeeze multiple blank lines into one',
							'Display contents of myfile.txt with squeezing multiple blank lines into one and suppressing underlining. Count logical lines and not screen lines.',
							'How do i see contents of myfile.txt with counting logical lines instead of screen lines, suppressing underlining and squeezing multiple empty lines into one?']},ignore_index=True)

more = more.append({'Command':'more -dsu -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Squeeze multiple blank lines into one. Suppress underlines. Display prompt instead of ringing bell when an illegal key is pressed. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, suppressing underlines, squeezing multiple blank lines into one, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', suppressing underlines and with prompting help instead of ringing the bell when an illegal key is pressed and squeezing multiple blank lines into one?']},ignore_index=True)

more = more.append({'Command':'more -dfs -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Squeeze multiple blank lines into one. Count logical lines rather than screen lines. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, squeezing multiple blank lines into one, count logical lines rather than screen lines, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', squeezing multiple blank lines into one and with prompting help instead of ringing the bell when an illegal key is pressed? Count logical lines rather than screen lines.']},ignore_index=True)

more = more.append({'Command':'more -dfu -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Count logical lines rather than screen lines. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, suppressing underlining, count logical lines rather than screen lines, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', suppressing underlining, and with prompting help instead of ringing the bell when an illegal key is pressed? Count logical lines rather than screen lines.']},ignore_index=True)

more = more.append({'Command':'more -lsu myfile.txt',
				'NL Queries':['Show output of myfile.txt enough to fit the command line. Do not pause after any form feed. Squeeze multiple blank lines. Suppress underlines.',
							'Display contents of myfile.txt enough to fit the command line without pausing after any occurence of form feed and squeezing multiple empty lines and suppressing underlining.',
							'How to display contents of myfile.txt enough to fit the command line? Do not pause after any form feed and squeeze multiple empty lines.',
							'Show the contents of myfile.txt . Do not pause after any form feed. Squeeze multiple blank lines into one. Suppress underlines.']},ignore_index=True)

more = more.append({'Command':'more -dfls -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Do not pause after any form feed. Squeeze multiple blank lines into one. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines rather than screen lines. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, do not pause after any form feed, squeezing multiple blank lines into one, count logical lines rather than screen lines, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', squeezing multiple blank lines into one, not pausing after any form feed and with prompting help instead of ringing the bell when an illegal key is pressed? Count logical lines rather than screen lines.']},ignore_index=True)

more = more.append({'Command':'more -dflu -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Do not pause after any form feed. Suppress underlining. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines rather than screen lines. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, suppressing underlining, do not pause after any form feed, count logical lines rather than screen lines, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', suppressing underlining, not pausing after any form feed and with prompting help instead of ringing the bell when an illegal key is pressed? Count logical lines rather than screen lines.']},ignore_index=True)

more = more.append({'Command':'more -dfsu -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Squeeze multiple blank lines into one. Count logical lines rather than screen lines. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, suppressing underlining, squeezing multiple blank lines into one, count logical lines rather than screen lines, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', suppressing underlining, squeezing multiple blank lines into one and with prompting help instead of ringing the bell when an illegal key is pressed? Count logical lines rather than screen lines.']},ignore_index=True)

more = more.append({'Command':'more -dlsu -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Display prompt instead of ringing bell when an illegal key is pressed. Suppress underlining. Squeeze multiple empty lines. Do not pause after any form feed. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, squeezing multiple empty lines, suppressing underlining, do not pause after any form feed, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', suppressing underlining, with prompting help instead of ringing the bell when an illegal key is pressed and not pausing after any form feed and squeezing multiple empty lines?']},ignore_index=True)

more = more.append({'Command':'more -lfsu myfile.txt',
				'NL Queries':['Show contents of myfile.txt enough to fit the command line. Do not pause after any form feed. Count logical lines rather than screen lines. Suppress underlining. Squeeze multiple empty lines.',
							'Display contents of myfile.txt without pausing after any form feed and squeezing multiple empty lines and suppress underlining. Count logical lines and not screen lines.',
							'How do i see contents of myfile.txt enough to fit the command line with counting logical lines instead of screen lines, suppressing underlining, squeezing multiple blank lines into one and not pausing after any form feed?']},ignore_index=True)

more = more.append({'Command':'more -dflsu -4 myfile.txt',
				'NL Queries':['Show contents of myfile.txt. Do not pause after any form feed. Suppress underlining. Squeeze multiple blank lines into one. Display prompt instead of ringing bell when an illegal key is pressed. Count logical lines rather than screen lines. Set screen lines to use as \'4\'.',
							'Display contents of myfile.txt with \'4\' lines per screenful, suppressing underlining, do not pause after any form feed, squeezing multiple blank lines into one, count logical lines rather than screen lines, prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal key is pressed.',
							'How do i see contents of myfile.txt with screen lines set to use as \'4\', suppressing underlining, squeezing multiple blank lines into one, not pausing after any form feed and with prompting help instead of ringing the bell when an illegal key is pressed? Count logical lines rather than screen lines.']},ignore_index=True)




print more.shape


