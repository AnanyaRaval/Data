import pandas as pd 

cat = pd.DataFrame(columns = ['Command','NL Queries'])



#options [-nbeEsvtTu]
#options n and b are similar , e=-vE and t=-vT
 
cat = cat.append({'Command':'cat >foo.txt',
				'NL Queries':['Create new file foo.txt. Open it in command line.',
							'How do I start a file foo.txt so that I can add lines to it?',
							'Start a file foo.txt in command line.']},ignore_index = True)

cat = cat.append({'Command':'cat instructions.txt',
				'NL Queries':['Open file instructions.txt',
							'Show contents of file instructions.txt.',
							'Display data in file instructions.txt.',
							'How do I see what is in the file instructions.txt?']},ignore_index = True)

cat = cat.append({'Command':'cat -- -*',
				'NL Queries':['Display contents of all files starting with \'-\'.',
							'How can I see data in all files starting with \'-\'?',
							'Show me contents of all files starting with \'-\'.',
							'In terminal how do I see content of all files starting with \'-\'?']},ignore_index = True)

cat = cat.append({'Command':'cat instructions.txt file.txt',
				'NL Queries':['Open files instructions.txt and file.txt',
							'Show contents of files instructions.txt and file.txt.',
							'Display data in files instructions.txt and file.txt.',
							'How do I see what is in the files instructions.txt and file.txt?']},ignore_index = True)

cat = cat.append({'Command':'cat -n instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers.',
							'Show contents of file instructions.txt with line numbers.',
							'How do I get content of file instructions.txt with line numbers?',
							'I want to see content of file instructions.txt with line numbers.']},ignore_index = True)

cat = cat.append({'Command':'cat -b instructions.txt',
				'NL Queries':['Open file instructions.txt. Do not show line number for blank lines.',
							'Display file instructions.txt with line numbers only for non-blank lines.',
							'How do I see contents of instructions.txt along with line numbering only for non-blank lines?',
							'Show file instructions.txt with line numbers only for non-blank lines.']},ignore_index = True)

cat = cat.append({'Command':'cat -e instructions.txt',
				'NL Queries':['Open file instructions.txt. Show $ for end of each line and display non-printing characters.',
							'How do I see contents of instructions.txt along with non-printing characters and $ at end of each line?',
							'Display file instructions.txt with non-printing characters and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -E instructions.txt',
				'NL Queries':['Open file instructions.txt. Show $ for end of each line.',
							'Display file instructions.txt with $ at end of each line.',
							'How do I see contents of instructions.txt with $ at end of each line?',
							'I want to see content of instructions.txt with $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -s instructions.txt',
				'NL Queries':['Open file instructions.txt. Squeeze multiple adjacent empty lines.',
							'Display file instructions.txt, squeeze multiple adjacent empty lines.',
							'How do I see contents removing adjacent multiple empty lines?']},ignore_index = True)

cat = cat.append({'Command':'cat -v instructions.txt',
				'NL Queries':['Open file instructions.txt with non-printing characters.',
							'Display file instructions.txt with non-printing characters.',
							'How do I see contents of instructions.txt with non-printing characters?',
							'Show me the content of instructions.txt with non-printing characters.']},ignore_index = True)

cat = cat.append({'Command':'cat -t instructions.txt',
				'NL Queries':['Open file instructions.txt. Display non-printing characters as well as TAB character as ^I.',
							'Display file instructions.txt with non-printing characters and TAB character as ^I.',
							'How do I see contents of instructions.txt with non-printing characters and TAB character as ^I?',
							'In the command line how do I see contents of instructions.txt with non-printing characters and TAB character as ^I?']},ignore_index = True)

cat = cat.append({'Command':'cat -T instructions.txt',
				'NL Queries':['Open file instructions.txt. Display TAB character as ^I.',
							'Display file instructions.txt with TAB character as ^I.',
							'How do I see contents of instructions.txt with TAB character as ^I?',
							'Show the content of instructions.txt with TAB character as ^I']},ignore_index = True)

cat = cat.append({'Command':'cat -u instructions.txt',
				'NL Queries':['Open file instructions.txt with output buffering disabled.',
							'Display file instructions.txt with output buffering disabled.',
							'How do I see contents of instructions.txt with output buffering disabled?']},ignore_index = True)



cat = cat.append({'Command':'cat -tn instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters and TAB character as ^I.',
							'How do I see the content of file instructions.txt with line numbers, non-printing characters and TAB character as ^I?',
							'Open file instructions.txt. Show line numbers for each line. Show non-printing characters and TAB character as ^I.',
							'Show the content of instructions.txt with numbering of each line, non-printing characters and TAB character as ^I.',
							'In the command line ,how do I see contents of file instructions.txt with line numbers, non-printing characters and TAB character as ^I?']},ignore_index = True)

cat = cat.append({'Command':'cat -tb instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines, non-printing characters and TAB character as ^I.',
							'How do I see the content of file instructions.txt with line numbers for non-blank lines, non-printing characters and TAB character as ^I?',
							'Open file instructions.txt. Show line numbers for non-blank lines. Show non-printing characters and TAB character as ^I.',
							'Show the content of instructions.txt with numbering of each non-blank line, non-printing characters and TAB character as ^I.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for non-blank lines only, non-printing characters and TAB character as ^I?']},ignore_index = True)

cat = cat.append({'Command':'cat -te instructions.txt',
				'NL Queries':['Display file instructions.txt with $ at end of each line, non-printing characters and TAB character as ^I.',
							'How do I see the content of file instructions.txt with $ at end of each line, non-printing characters and TAB character as ^I?',
							'Open file instructions.txt. Show $ symbol at end of each line. Show non-printing characters and TAB character as ^I.',
							'In the command line, how do I see contents of file instructions.txt with $ at end of each line, non-printing characters and TAB character as ^I?',
							'Show the content of instructions.txt with $ at end of each line, non-printing characters and TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -ts instructions.txt',
				'NL Queries':['Display file instructions.txt with squeezing multiple adjacent empty lines, non-printing characters and TAB character as ^I.',
							'How do I see the content of file instructions.txt with squeezing multiple adjacent empty lines, non-printing characters and TAB character as ^I?',
							'Open file instructions.txt. Squeeze multiple adjacent empty lines. Show non-printing characters and TAB character as ^I.',
							'In the command line, how do I see contents of file instructions.txt with squeezing multiple adjacent empty lines, non-printing characters and TAB character as ^I?',
							'Show the content of instructions.txt with squeezing multiple adjacent empty lines, non-printing characters and TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -tu instructions.txt',
				'NL Queries':['Display file instructions.txt with output buffering disabled, non-printing characters and TAB character as ^I.',
							'How do I see the content of file instructions.txt with output buffering disabled, non-printing characters and TAB character as ^I?',
							'Open file instructions.txt. Set output buffering disabled. Show non-printing characters and TAB character as ^I.',
							'In the command line, how do I see contents of file instructions.txt with output buffering disabled, non-printing characters and TAB character as ^I?',
							'Show the content of instructions.txt with output buffering disabled, non-printing characters and TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -Tn instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers and TAB character as ^I.',
							'How do I see the content of file instructions.txt with line numbers and TAB character as ^I?',
							'Open file instructions.txt. Show line numbers for each line. Show TAB character as ^I.',
							'Show the content of instructions.txt with numbering of each line and TAB character as ^I.',
							'In the command line, how do I see contents of file instructions.txt with line numbers and TAB character as ^I?']},ignore_index = True)

cat = cat.append({'Command':'cat -Tb instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines and TAB character as ^I.',
							'How do I see the content of file instructions.txt with line numbers for non-blank lines and TAB character as ^I?',
							'Open file instructions.txt. Show line numbers for non-blank lines. Show TAB character as ^I.',
							'Show the content of instructions.txt with numbering of each non-blank line and TAB character as ^I.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for non-blank lines only and TAB character as ^I?']},ignore_index = True)

cat = cat.append({'Command':'cat -TE instructions.txt',
				'NL Queries':['Display file instructions.txt with $ at end of each line and TAB character as ^I.',
							'How do I see the content of file instructions.txt with $ at end of each line and TAB character as ^I?',
							'Open file instructions.txt. Show $ symbol at end of each line. Show TAB character as ^I.',
							'In the command line how do I see contents of file instructions.txt with $ at end of each line and TAB character as ^I.',
							'Show the content of instructions.txt with $ at end of each line and TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -Ts instructions.txt',
				'NL Queries':['Display file instructions.txt after squeezing multiple adjacent empty lines and show TAB character as ^I.',
							'How do I see the content of file instructions.txt after squeezing multiple adjacent empty lines and show TAB character as ^I?',
							'Open file instructions.txt. Squeeze multiple adjacent empty lines. Show TAB character as ^I.',
							'In the command line, how do I see contents of file instructions.txt with squeezing multiple adjacent empty lines and TAB character as ^I.',
							'Show the content of instructions.txt with squeezing multiple adjacent empty lines and TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -Tu instructions.txt',
				'NL Queries':['Display file instructions.txt with output buffering disabled and  show TAB character as ^I.',
							'How do I see the content of file instructions.txt with output buffering disabled and TAB character as ^I?',
							'Open file instructions.txt. Set output buffering disabled. Show TAB character as ^I.',
							'In the command line how do I see contents of file instructions.txt with output buffering disabled and TAB character as ^I.',
							'Show the content of instructions.txt with output buffering disabled and TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -vn instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers and non-printing characters.',
							'How do I see the content of file instructions.txt with line numbers and non-printing characters?',
							'Open file instructions.txt. Show line numbers for each line. Show non-printing characters.',
							'Show the content of instructions.txt with numbering of each line and non-printing characters.',
							'In the command line, how do I see contents of file instructions.txt with line numbers and non-printing characters?']},ignore_index = True)

cat = cat.append({'Command':'cat -vb instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines and non-printing characters.',
							'How do I see the content of file instructions.txt with line numbers for non empty lines and non-printing characters?',
							'Open file instructions.txt. Show line numbers for each non empty line. Show non-printing characters.',
							'Show the content of instructions.txt with numbering of each non empty line and non-printing characters.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for non-blank lines and non-printing characters?']},ignore_index = True)

cat = cat.append({'Command':'cat -vs instructions.txt',
				'NL Queries':['Display file instructions.txt with squeezing multiple adjacent blank lines and non-printing characters.',
							'How do I see the content of file instructions.txt with squeezing multiple adjacent empty lines and non-printing characters?',
							'Open file instructions.txt. Squeeze multiple adjacent empty lines. Show non-printing characters.',
							'Show the content of instructions.txt with squeezing multiple adjacent blank lines and non-printing characters.',
							'In the command line, how do I see contents of file instructions.txt with squeezing multiple adjacent empty lines and non-printing characters?']},ignore_index = True)

cat = cat.append({'Command':'cat -vu instructions.txt',
				'NL Queries':['Display file instructions.txt with output buffering disabled and non-printing characters.',
							'How do I see the content of file instructions.txt with output buffering disabled and non-printing characters?',
							'Open file instructions.txt. Set output buffering disabled. Show non-printing characters.',
							'Show the content of instructions.txt with output buffering disabled and non-printing characters.',
							'In the command line, how do I see contents of file instructions.txt with output buffering disabled and non-printing characters?']},ignore_index = True)

cat = cat.append({'Command':'cat -un instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers and output buffering disabled.',
							'How do I see the content of file instructions.txt with line numbers and output buffering disabled?',
							'Open file instructions.txt. Show line numbers for each line. Set output buffering disabled.',
							'Show the content of instructions.txt with numbering of each line and output buffering disabled.',
							'In the command line, how do I see contents of file instructions.txt with line numbers and output buffering disabled?']},ignore_index = True)

cat = cat.append({'Command':'cat -ub instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines and output buffering cancelled.',
							'How do I see the content of file instructions.txt with line numbers for non empty lines and output buffering cancelled?',
							'Open file instructions.txt. Show line numbers for each non empty line. Set output buffering cancelled.',
							'Show the content of instructions.txt with numbering of each non empty line and output buffering off.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for non-blank lines and output buffering off?']},ignore_index = True)

cat = cat.append({'Command':'cat -us instructions.txt',
				'NL Queries':['Display file instructions.txt after squeezing multiple adjacent blank lines and output buffering off.',
							'How do I see the content of file instructions.txt after squeezing multiple adjacent empty lines and output buffering off?',
							'Open file instructions.txt. Squeeze multiple adjacent empty lines. Set output buffering off.',
							'Show the content of instructions.txt after squeezing multiple adjacent blank lines and output buffering disabled.',
							'In the command line, how do I see contents of file instructions.txt after squeezing multiple adjacent empty lines and output buffering cancelled?']},ignore_index = True)

cat = cat.append({'Command':'cat -ue instructions.txt',
				'NL Queries':['Display file instructions.txt with $ at end of each line, non-printing characters and output buffering disabled.',
							'How do I see the content of file instructions.txt with $ at end of each line, non-printing characters and output buffering off?',
							'Open file instructions.txt. Show $ symbol at end of each line. Show non-printing characters and output buffering cancelled.',
							'In the command line how do I see contents of file instructions.txt with $ at end of each line, non-printing characters and output buffering disabled.',
							'Show the content of instructions.txt with $ at end of each line, non-printing characters and output buffering disabled.']},ignore_index = True)

cat = cat.append({'Command':'cat -uE instructions.txt',
				'NL Queries':['Display file instructions.txt with $ at end of each line and output buffering disabled.',
							'How do I see the content of file instructions.txt with $ at end of each line and output buffering disabled.?',
							'Open file instructions.txt. Show $ symbol at end of each line. Set output buffering off.',
							'In the command line how do I see contents of file instructions.txt with $ at end of each line and output buffering cancelled.',
							'Show the content of instructions.txt with $ at end of each line and output buffering disabled.']},ignore_index = True)

cat = cat.append({'Command':'cat -En instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers and $ at end of each line.',
							'How do I see the content of file instructions.txt with line numbers and $ symbol at end of each line?',
							'Open file instructions.txt. Show line numbers for each line. Show $ symbol at end of each line.',
							'Show the content of instructions.txt with numbering of each line and $ at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -Eb instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines and $ symbol at end of each line.',
							'How do I see the content of file instructions.txt with line numbers for non empty lines and $ at end of each line?',
							'Open file instructions.txt. Show line numbers for each non empty line. Dsiplay $ at end of each line.',
							'Show the content of instructions.txt with numbering of each non empty line and $ at end of each line.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for non-blank lines and $ symbol at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -Es instructions.txt',
				'NL Queries':['Display file instructions.txt with squeezing multiple adjacent blank lines and $ symbol at end of each line.',
							'How do I see the content of file instructions.txt with squeezing multiple adjacent empty lines and $ at end of each line?',
							'Open file instructions.txt. Squeeze multiple adjacent empty lines. Display $ symbol at end of each line.',
							'Show the content of instructions.txt with squeezing multiple adjacent blank lines and $ at end of each line.',
							'In the command line how do I see contents of file instructions.txt with squeezing multiple adjacent empty lines and $ symbol at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -ne instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters and $ symbol at end of each line.',
							'How do I see the content of file instructions.txt with line numbers, non-printing characters and $ symbol at end of each line?',
							'Open file instructions.txt. Show line numbers for each line. Show non-printing characters and $ at end of each line.',
							'Show the content of instructions.txt with numbering of each line, non-printing characters and $ symbol at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers, non-printing characters and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -ns instructions.txt',
				'NL Queries':['Display file instructions.txt after squeezing multiple adjacent blank lines and output number of each line.',
							'How do I see the content of file instructions.txt after squeezing multiple adjacent empty lines and number of each line?',
							'Open file instructions.txt. Squeeze multiple adjacent empty lines. Show line numbers for each line.',
							'Show the content of instructions.txt with squeezing multiple adjacent blank lines and display numbering for each line.',
							'In the command line how do I see contents of file instructions.txt with squeezing multiple adjacent empty lines and show numbering for each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -bs instructions.txt',
				'NL Queries':['Display file instructions.txt with squeezing multiple adjacent blank lines and numbering for each non empty line.',
							'How do I see the content of file instructions.txt with squeezing multiple adjacent empty lines and numbering only for non empty lines?',
							'Open file instructions.txt. Squeeze multiple adjacent empty lines. Give numbering for each non-blank line.',
							'Show the content of instructions.txt with squeezing multiple adjacent blank lines and display numbering only for non-blank lines.',
							'In the command line how do I see contents of file instructions.txt with squeezing multiple adjacent empty lines and show numbering only for non empty lines.']},ignore_index = True)

cat = cat.append({'Command':'cat -be instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non empty lines, non-printing characters and $ symbol at end of each line.',
							'How do I see the content of file instructions.txt with line numbers for non-blank lines, non-printing characters and $ symbol at end of each line?',
							'Open file instructions.txt. Show line numbers only for non empty lines. Show non-printing characters and $ at end of each line.',
							'Show the content of instructions.txt with numbering of each non-blank line, non-printing characters and $ symbol at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers for only non-blank lines, non-printing characters and $ at end of each line.']},ignore_index = True)



cat = cat.append({'Command':'cat -nes instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters and $ at end of each line, squeeze multiple empty lines.',
							'Open file instructions.txt. Display line numbers. Print non-printing characters. Squeeze multiple adjacent empty lines. Show $ at end of each line.',
							'How do I open a file instructions.txt with line numbers, non-printing characters for each line and $ at end of each line? Squeeze blank lines.'
							'Show the content of instructions.txt with line numbers, non-printing characters, and show $ at end of each line. Squeeze multiple adjacent empty lines.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each line, non-printing characters and $ at end of each line, squeeze multiple adjacent empty lines.']},ignore_index = True)

cat = cat.append({'Command':'cat -neT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters, $ at end of each line and TAB character as ^I.',
							'Open file instructions.txt. Display line numbers. Print non-printing characters. Print TAB character as ^I. Show $ at end of each line.',
							'How do i open a file instructions.txt with line numbers for each line, non-printing characters, TAB character as ^I and $ at end of each line?',
							'Show the content of instructions.txt with line numbers, non-printing characters, TAB character as ^I and $ at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters, TAB character as ^I and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -neu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters, $ at end of each line and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Print non-printing characters. Set output buffering off. Show $ at end of each line.',
							'How do I open a file instructions.txt with line numbers for each line, non-printing characters, output buffering cancelled and $ at end of each line?',
							'Show the content of instructions.txt with line numbers, non-printing characters and $ at end of each line, along with disabled output buffering.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters, output buffering off and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -nEs instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, squeeze multiple adjacent empty lines and show $ at end of each line.',
							'Open file instructions.txt. Display line numbers. Squeeze multiple adjacent empty lines. Show $ at end of each line.',
							'How do i open a file instructions.txt with line numbers for each line, squeeze multiple adjacent empty lines and display $ at end of each line?',
							'Show the content of instructions.txt with line numbers and $ at end of each line and squeeze multiple adjacent empty lines.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, squeeze multiple adjacent empty lines and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -nET instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, $ at end of each line and TAB character as ^I.',
							'Open file instructions.txt. Display line numbers. Print TAB character as ^I. Show $ at end of each line.',
							'How do I open a file instructions.txt with line numbers for each line, TAB character as ^I and $ at end of each line?',
							'Show the content of instructions.txt with line numbers, TAB character as ^I and $ at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, TAB character as ^I and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -nEu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, $ at end of each line and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Set output buffering off. Add $ at end of each line.',
							'How do I open a file instructions.txt with line numbers for each line, output buffering cancelled and add $ at end of each line?',
							'Show the content of instructions.txt with line numbers, output buffering off and add $ at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, output buffering off and add $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -nsv instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters and squeeze multiple adjacent empty lines.',
							'Open file instructions.txt. Display line numbers. Print non-printing characters. Squeeze multiple adjacent empty lines',
							'How do I open a file instructions.txt with line numbers for each line, non-printing characters and squeeze multiple adjacent empty lines?',
							'Show the content of instructions.txt with line numbers, non-printing characters and squeeze multiple adjacent empty lines.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters and squeeze multiple adjacent empty lines.']},ignore_index = True)

cat = cat.append({'Command':'cat -nsT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, squeeze multiple adjacent empty lines and TAB character as ^I.',
							'Open file instructions.txt. Display line numbers. Squeeze multiple adjacent empty lines. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers for each line, squeeze multiple adjacent empty lines and TAB character as ^I?',
							'Show the content of instructions.txt with line numbers, squeeze multiple adjacent empty lines and TAB character as ^I.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line and TAB character as ^I. Also,squeeze multiple adjacent empty lines .']},ignore_index = True)

cat = cat.append({'Command':'cat -nst instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters and TAB character as ^I, squeeze multiple adjacent empty lines .',
							'Open file instructions.txt. Display line numbers. Print non-printing characters. Squeeze multiple adjacent empty lines. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers for each line, non-printing characters and TAB character as ^I after squeezing multiple adjacent empty lines ?',
							'Show the content of instructions.txt with line numbers, non-printing characters, squeeze multiple adjacent empty lines and TAB character as ^I.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters and TAB character as ^I along with squeezed multiple adjacent empty lines']},ignore_index = True)

cat = cat.append({'Command':'cat -nsu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, squeeze multiple adjacent empty lines and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Squeeze multiple adjacent empty lines. Set output buffering offed.',
							'How do I open a file instructions.txt with line numbers for each line, squeeze multiple adjacent empty lines and output buffering cancelled?',
							'Show the content of instructions.txt with line numbers, squeeze multiple adjacent empty lines and output buffering offed.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, squeeze multiple adjacent empty lines and output buffering disabled.']},ignore_index = True)

cat = cat.append({'Command':'cat -nvu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Print non-printing characters. Set output buffering off.',
							'How do I open a file instructions.txt with line numbers for each line, non-printing characters and output buffering cancelled?',
							'Show the content of instructions.txt with line numbers and non-printing characters with output buffering off.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -nut instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters, TAB character as ^I and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Print non-printing characters. Set output buffering off. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers for each line, non-printing characters and TAB character as ^I, with output buffering disba;ed?',
							'Show the content of instructions.txt with line numbers, non-printing characters and TAB character as ^I. Set output buffering off.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters and TAB character as ^I? Output buffering should be off .']},ignore_index = True)

cat = cat.append({'Command':'cat -nuT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, TAB character as ^I and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Set output buffering off. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers for each line and TAB character as ^I, with disabled output buffering?',
							'Show the content of instructions.txt with line numbers and TAB character as ^I. Keep output buffering off.', 
							'In the command line, how do I see contents of file instructions.txt with line numbers for each line and TAB character as ^I? Turn off output buffering.']},ignore_index = True)
#print cat.shape
cat = cat.append({'Command':'cat -bes instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers only for non empty lines, non-printing characters, squeeze multiple adjacent empty lines and show $ at end of each line.',
							'Open file instructions.txt. Display line numbers for non-blank lines. Print non-printing characters. Squeeze multiple adjacent empty lines. Display $ at end of each line.',
							'How do i open a file instructions.txt with line numbers for each non empty line, non-printing characters and $ at end of each line after squeezing multiple adjacent empty lines?',
							'Show the content of instructions.txt with line numbers only for non-blank lines, non-printing characters and $ at end of each line,along with squeezing multiple adjacent empty lines.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each non-blank line, non-printing characters and $ at end of each line after squeezing multiple adjacent empty lines']},ignore_index = True)

cat = cat.append({'Command':'cat -beT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers only for non empty lines, non-printing characters, $ at end of each line and TAB character as ^I.',
							'Open file instructions.txt. Display line numbers for non-blank lines only. Print non-printing characters. Print TAB character as ^I. $ at end of each line.',
							'How do I open a file instructions.txt with line numbers for each non empty line, non-printing characters, TAB character as ^I and $ at end of each line?',
							'Show the content of instructions.txt with line numbers for non-blank lines, non-printing characters, TAB character as ^I and $ at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each non-blank line, non-printing characters, TAB character as ^I and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -beu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers only for non-blank lines, non-printing characters, $ at end of each line and output buffering disabled.',
							'Open file instructions.txt. Display line numbers only for non-blank lines. Print non-printing characters. Set output buffering off. $ at end of each line.',
							'How do i open a file instructions.txt with line numbers for each non empty line, non-printing characters, output buffering cancelled and $ at end of each line?',
							'Show the content of instructions.txt with line numbers for each non-blank line, non-printing characters, output buffering off and $ at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each non empty line only, non-printing characters, output buffering off and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -bEs instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines after squeezing multiple adjacent empty lines and show $ at end of each line.',
							'Open file instructions.txt. Display line numbers for non empty lines. Squeeze multiple adjacent empty lines. Display $ at end of each line.',
							'How do I open a file instructions.txt with line numbers for each non-blank line, squeeze multiple adjacent empty lines and show $ at end of each line?',
							'Show the content of instructions.txt with line numbers for each non empty line, squeeze multiple adjacent empty lines and show $ at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line which is not empty, squeeze multiple adjacent empty lines and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -bET instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for lines which are not empty, $ at end of each line and TAB character as ^I.',
							'Open file instructions.txt. Display line numbers for non-blank lines. Print TAB character as ^I. $ at end of each line.',
							'How do I open a file instructions.txt with line numbers for each line which is not blank, TAB character as ^I and $ at end of each line?',
							'Show the content of instructions.txt with line numbers for each line which is not empty, TAB character as ^I and $ at end of each line.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line which is not blank, TAB character as ^I and $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -bEu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for lines which are not empty, $ at end of each line and output buffering disabled.',
							'Open file instructions.txt. Display line numbers for lines which are not blank. Set output buffering off. Add $ at end of each line.',
							'How do I open a file instructions.txt with line numbers for each non empty line, output buffering cancelled and add $ at end of each line?',
							'Show the content of instructions.txt with line numbers for each non-blank line, output buffering off and add $ at end of each line.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each line which is not blank, output buffering off and add $ at end of each line.']},ignore_index = True)

cat = cat.append({'Command':'cat -bsv instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for lines which are not blank, non-printing characters and squeeze multiple adjacent empty lines.',
							'Open file instructions.txt. Display line numbers for lines which are not empty. Print non-printing characters. Squeeze multiple adjacent empty lines',
							'How do i open a file instructions.txt with line numbers for each non-blank line, non-printing characters and squeeze multiple adjacent empty lines?',
							'Show the content of instructions.txt with line numbers for each non empty line, non-printing characters and squeeze multiple adjacent empty lines.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each non empty line, non-printing characters and squeeze multiple adjacent empty lines.']},ignore_index = True)

cat = cat.append({'Command':'cat -bsT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines, squeeze multiple adjacent empty lines and show TAB character as ^I.',
							'Open file instructions.txt. Display line numbers for non empty lines only. Squeeze multiple adjacent empty lines. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers for each non empty line, squeeze multiple adjacent empty lines and display TAB character as ^I?',
							'Show the content of instructions.txt with line numbers for lines which are not blank, squeeze multiple adjacent empty lines and display TAB character as ^I.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line for lines which is not empty, squeeze multiple adjacent empty lines and show TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -bst instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for lines which are not empty, non-printing characters and TAB character as ^I after squeezing multiple adjacent empty lines .',
							'Open file instructions.txt. Display line numbers for lines which are not blank. Print non-printing characters. Squeeze multiple adjacent empty lines. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers for each non empty line, non-printing characters and TAB character as ^I? Squeeze multiple adjacent empty lines',
							'Show the content of instructions.txt with line numbers for each non-blank line, non-printing characters, squeeze multiple adjacent empty lines and TAB character as ^I.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each non empty line, non-printing characters, squeeze multiple adjacent empty lines and TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -bsu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non empty lines, squeeze multiple adjacent empty lines and disabled output buffering.',
							'Open file instructions.txt. Display line numbers for non-blank lines. Squeeze multiple adjacent empty lines. Set output buffering off.',
							'How do I open a file instructions.txt with line numbers for each line non empty line, squeeze multiple adjacent empty lines and cancel output buffering?',
							'Show the content of instructions.txt with line numbers for lines which are not blank, squeeze multiple adjacent empty lines and output buffering offed.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each line which is not empty, squeeze multiple adjacent empty lines and output buffering disabled.']},ignore_index = True)

cat = cat.append({'Command':'cat -bvu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines, show non-printing characters and disable output buffering.',
							'Open file instructions.txt. Display line numbers for non empty lines. Print non-printing characters. Set output buffering off.',
							'How do I open a file instructions.txt with line numbers and non-printing characters for each non-blank line and output buffering cancelled?',
							'Show the content of instructions.txt with line numbers for each non-empty line,show non-printing characters and cancel output buffering.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each non empty or non-blank line, along with non-printing characters and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -but instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for lines which are non empty or non-blank, non-printing characters, TAB character as ^I and output buffering disabled.',
							'Open file instructions.txt. Display line numbers for lines which are non empty or non-blank. Print non-printing characters. Set output buffering off. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers for each non empty or non-blank line, non-printing characters and TAB character as ^I with output buffering cancelled?',
							'Show the content of instructions.txt with line numbers for lines which are non empty or non-blank, non-printing characters and TAB character as ^I, along with output buffering off.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each non empty or non-blank line, non-printing characters and TAB character as ^I with output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -buT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for lines which are either non empty or non-blank and TAB character as ^I with output buffering disabled.',
							'Open file instructions.txt. Display line numbers for lines which are either non empty or non-blank. Set output buffering off. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers for each non empty or non-blank line, cancel output buffering and  show TAB character as ^I?',
							'Show the content of instructions.txt with line numbers for lines which are either non empty or non-blank and TAB character as ^I. Turn output buffering off.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each non empty or non-blank line and TAB character as ^I, along with output buffering off.']},ignore_index = True)



cat = cat.append({'Command':'cat -nesT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters, $ at end of each line and TAB character as ^I after squeezing adjacent multiple empty lines.',
							'Open file instructions.txt. Display line numbers. Add $ at end of each line. Print non-printing characters. Squeeze adjacent multiple empty lines. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers, $ at end of each line, non-printing characters, TAB character as ^I and squeeze adjacent multiple empty lines?',
							'Show the content of instructions.txt with line numbers each line, non-printing characters, $ at end of each line and TAB character as ^I, along with squeezing adjacent multiple empty lines .',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters, $ at end of each line and TAB character as ^I. Squeeze adjacent multiple empty lines.']},ignore_index = True)

cat = cat.append({'Command':'cat -nesu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters and $ at end of each line. Squeeze adjacent multiple empty lines and disable output buffering.',
							'Open file instructions.txt. Display line numbers. Add $ at end of each line. Print non-printing characters. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do I open a file instructions.txt with line numbers, $ at end of each line and non-printing characters, squeeze adjacent multiple empty lines and turn output buffering off?',
							'Show the content of instructions.txt with line numbers each line, non-printing characters, $ at end of each line, squeeze adjacent multiple empty lines and cancel output buffering.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters, and $ at end of each line, squeeze adjacent multiple empty lines and turn output buffering off.']},ignore_index = True)
cat = cat.append({'Command':'cat -nEsT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, $ at end of each line and TAB character as ^I after squeezing adjacent multiple empty lines.',
							'Open file instructions.txt. Display line numbers. Add $ at end of each line. Squeeze adjacent multiple empty lines. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers, $ at end of each line and TAB character as ^I? Squeeze adjacent multiple empty lines',
							'Show the content of instructions.txt with line numbers each line, $ at end of each line and TAB character as ^I, along with squeezed adjacent multiple empty lines.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line and $ at end of each line, squeeze adjacent multiple empty lines and show TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -nEsu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, $ at end of each line, squeeze adjacent multiple empty lines and disble output buffering.',
							'Open file instructions.txt. Display line numbers. Add $ at end of each line. Squeeze adjacent multiple empty lines. Set output buffering off.',
							'How do I open a file instructions.txt with line numbers, $ at end of each line, squeeze adjacent multiple empty lines and turn output buffering off?',
							'Show the content of instructions.txt with line numbers each line, $ at end of each line, squeeze adjacent multiple empty lines cancel and output buffering.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each line, $ at end of each line, squeeze adjacent multiple empty lines and set output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -nsvu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters, squeeze adjacent multiple empty lines and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Print non-printing characters. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do i open a file instructions.txt with line numbers, non-printing characters, squeeze adjacent multiple empty lines and output buffering off?',
							'Show the content of instructions.txt with line numbers each line, non-printing characters, squeeze adjacent multiple empty lines and output buffering cancelled.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters, squeeze adjacent multiple empty lines and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -nsTu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Print TAB character as ^I. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do i open a file instructions.txt with line numbers, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering off?',
							'Show the content of instructions.txt with line numbers each line, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering cancelled.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -nstu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, non-printing characters, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Print TAB character as ^I. Print non-printing characters. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do I open a file instructions.txt with line numbers, TAB character as ^I, non-printing characters, squeeze adjacent multiple empty lines and output buffering off?',
							'Show the content of instructions.txt with line numbers each line, non-printing characters, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering cancelled.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, non-printing characters, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -besT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines, non-printing characters, $ at end of each line and TAB character as ^I after squeezing adjacent multiple empty lines.',
							'Open file instructions.txt. Display line numbers for non empty lines. Add $ at end of each line. Print non-printing characters. Squeeze adjacent multiple empty lines. Print TAB character as ^I.',
							'How do I open a file instructions.txt with line numbers for non empty lines, $ at end of each line, non-printing characters and TAB character as ^I after squeezing adjacent multiple empty lines ?',
							'Show the content of instructions.txt with line numbers for each non empty line, non-printing characters, $ at end of each line,TAB character as ^I and squeeze adjacent multiple empty lines.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each non-blank line, non-printing characters, $ at end of each line and TAB character as ^I, squeeze adjacent multiple empty lines.']},ignore_index = True)

cat = cat.append({'Command':'cat -besu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for lines which are not empty, non-printing characters, $ at end of each line, squeeze adjacent multiple empty lines and output buffering disabled.',
							'Open file instructions.txt. Display line numbers for non-blank lines. Add $ at end of each line. Print non-printing characters. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do i open a file instructions.txt with line numbers for non empty lines, $ at end of each line, non-printing characters, squeeze adjacent multiple empty lines and output buffering off?',
							'Show the content of instructions.txt with line numbers each line which is not empty, non-printing characters, $ at end of each line, squeeze adjacent multiple empty lines and output buffering cancelled.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each non-blank line, non-printing characters, $ at end of each line, squeeze adjacent multiple empty lines and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -bEsT instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for lines which are not blank, $ at end of each line, squeeze adjacent multiple empty lines and TAB character as ^I.',
							'Open file instructions.txt. Display line numbers for non-blank lines. Add $ at end of each line. Squeeze adjacent multiple empty lines. Print TAB character as ^I.',
							'How do i open a file instructions.txt with line numbers for non empty lines, $ at end of each line, squeeze adjacent multiple empty lines and TAB character as ^I?',
							'Show the content of instructions.txt with line numbers each line which is not empty, $ at end of each line, squeeze adjacent multiple empty lines and TAB character as ^I.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each non empty or non-blank line, $ at end of each line, squeeze adjacent multiple empty lines and TAB character as ^I.']},ignore_index = True)

cat = cat.append({'Command':'cat -nEsu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non empty lines, $ at end of each line, squeeze adjacent multiple empty lines and disable output buffering.',
							'Open file instructions.txt. Display line numbers for non-blank lines. Add $ at end of each line. Squeeze adjacent multiple empty lines. Set output buffering to be disabled.',
							'How do I open a file instructions.txt with line numbers for non empty lines and $ at end of each line, squeeze adjacent multiple empty lines and set output buffering off?',
							'Show the content of instructions.txt with line numbers each line which is not blank and $ at end of each line, squeeze adjacent multiple empty lines and cancel output buffering.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each non-blank line and $ at end of each line, squeeze adjacent multiple empty lines and turn output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -bsvu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers and non-printing characters for non empty lines, squeeze adjacent multiple empty lines and output buffering disabled.',
							'Open file instructions.txt. Display line numbers for non empty lines. Print non-printing characters. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do I open a file instructions.txt with line numbers for non empty lines, show non-printing characters, squeeze adjacent multiple empty lines and turn output buffering off?',
							'Show the content of instructions.txt with line numbers each non empty line, non-printing characters, squeeze adjacent multiple empty lines and output buffering cancelled.',
							'In the command line, how do I see contents of file instructions.txt with line numbers and non-printing characters for each non empty line, squeeze adjacent multiple empty lines and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -bsTu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines and TAB character as ^I, squeeze adjacent multiple empty lines and disable output buffering.',
							'Open file instructions.txt. Display line numbers for non-blank lines. Print TAB character as ^I. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do i open a file instructions.txt with line numbers for non-blank lines and TAB character as ^I, squeeze adjacent multiple empty lines and set output buffering off?',
							'Show the content of instructions.txt with line numbers each non-blank line and TAB character as ^I, squeeze adjacent multiple empty lines and cancel output buffering cancelled.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each non-blank line, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -bstu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers and non-printing characters for lines which are not empty and TAB character as ^I, squeeze adjacent multiple empty lines and disable output buffering.',
							'Open file instructions.txt. Display line numbers for lines which are non-empty. Print TAB character as ^I. Print non-printing characters. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do I open a file instructions.txt with line numbers for lines which are neither empty nor blank, show TAB character as ^I and non-printing characters, squeeze adjacent multiple empty lines and set output buffering off?',
							'Show the content of instructions.txt with line numbers each line which is neither empty nor blank, display non-printing characters, show TAB character as ^I, squeeze adjacent multiple empty lines and cancel output buffering.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each line which is neither empty nor blank. Show all non-printing characters with TAB character as ^I, squeeze adjacent multiple empty lines and turn output buffering off.']},ignore_index = True)



cat = cat.append({'Command':'cat -nETsu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, $ at end of each line, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Print TAB character as ^I. Add $ at end of each line. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do i open a file instructions.txt with line numbers, TAB character as ^I, $ at end of each line, squeeze adjacent multiple empty lines and output buffering off?',
							'Show the content of instructions.txt with line numbers each line, $ at end of each line, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering cancelled.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, $ at end of each line, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -bETsu instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines, $ at end of each line, TAB character as ^I, squeeze adjacent multiple empty lines and disable output buffering.'
							'Open file instructions.txt. Display line numbers for lines which are neither empty not blank. Add $ at end of each line. Print TAB character as ^I. Squeeze adjacent multiple empty lines. Set output buffering off.',
							'How do I open a file instructions.txt with line numbers for non-blank lines with $ at end of each line and TAB character as ^I. Squeeze adjacent multiple empty lines and turn output buffering off?',
							'Show the content of instructions.txt with line numbers each non-blank line along with $ at end of each line and TAB character as ^I and squeeze adjacent multiple empty lines and cancel output buffering.',
							'In the command line, how do I see contents of file instructions.txt with line numbers for each non-blank line, $ at end of each line, TAB character as ^I, squeeze adjacent multiple empty lines and set output buffering off.']},ignore_index = True)



cat = cat.append({'Command':'cat -nETsuv instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers, $ at end of each line, TAB character as ^I, non-printing characters, squeeze adjacent multiple empty lines and output buffering disabled.',
							'Open file instructions.txt. Display line numbers. Print TAB character as ^I. Add $ at end of each line. Print non-printing characters. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do i open a file instructions.txt with line numbers, TAB character as ^I, $ at end of each line, non-printing characters, squeeze adjacent multiple empty lines and output buffering off?',
							'Show the content of instructions.txt with line numbers each line, $ at end of each line, non-printing characters, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering cancelled.',
							'In the command line how do I see contents of file instructions.txt with line numbers for each line, $ at end of each line, non-printing characters, TAB character as ^I, squeeze adjacent multiple empty lines and output buffering off.']},ignore_index = True)

cat = cat.append({'Command':'cat -bETsuv instructions.txt',
				'NL Queries':['Display file instructions.txt with line numbers for non-blank lines with $ at end of each line, TAB character as ^I, non-printing characters, squeeze adjacent multiple empty lines and disable output buffering.'
							'Open file instructions.txt. Display line numbers for lines which are neither empty not blank. Print non-printing characters. Add $ at end of each line. Print TAB character as ^I. Squeeze adjacent multiple empty lines. Set output buffering disabled.',
							'How do I open a file instructions.txt with line numbers for non-blank lines and show $ at end of each line, TAB character as ^I and non-printing characters. Squeeze adjacent multiple empty lines and turn output buffering off?',
							'Show the content of instructions.txt with line numbers of each non-blank line along with $ at end of each line, TAB character as ^I and non-printing characters after squeezing adjacent multiple empty lines and cancelling output buffering.',
							'In the command line, how do I see contents and non-printing characters of file instructions.txt with line numbers for each non-blank line, $ at end of each line and TAB character as ^I, squeeze adjacent multiple empty lines and turn output buffering off.']},ignore_index = True)


#tac is used for bottom to top displaying of lines but not actual reversing of lines
#cat = cat.append({'Command':'tac instructions.txt',
#				'NL Queries':['Open file instructions.txt in reverse order',
#							'Show contents of file instructions.txt in reverse order.',
#							'Display data in file instructions.txt in reverse order.',
#							'How do I see what is in the file instructions.txt in reverse order?']},ignore_index = True)

#cat = cat.append({'Command':'cat instructions.txt | wc -l',
#				'NL Queries':['Number of lines in instructions.txt.',
#							'Count number of lines in instructions.txt.',
#							'How do I know the number of lines in instructions.txt.?',
#							'How do I count the number of lines in instructions.txt.?',
#							'Display the number of lines in instructions.txt']},ignore_index = True)

cat = cat.append({'Command':'cat *',
				'NL Queries':['Display contents of all files.',
							'How can I see data in all files?',
							'Show me contents of all files.',
							'In terminal how do I see content of all files?']},ignore_index = True)

cat = cat.append({'Command':'cat <<EOF',
				'NL Queries':['Read content for command line until a specific pattern.',
							'How do I read content from command line until a specific pattern']},ignore_index = True)



print (cat.shape)
