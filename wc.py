import pandas as pd 

wc = pd.DataFrame(columns = ['Command','NL Queries'])


#options [-l,-m,-c,-w,-L]


wc = wc.append({'Command':'wc general.py',
				'NL Queries':['Print number of lines , words and characters in the file.',
							'How do I know the number of lines , words and characters in general.py?',
							'Show total number of lines , words and characters in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc --version',
				'NL Queries':['Print version of wc.',
							'How do I know the version of wc?',
							'Display version of wc.']},ignore_index=True)

wc = wc.append({'Command':'wc --help',
				'NL Queries':['Print help of wc.',
							'How do I know the man of wc?',
							'Display help of wc.']},ignore_index=True)

wc = wc.append({'Command':'wc -l general.py',
				'NL Queries':['Print number of lines in the file.',
							'How do I know the number of lines in general.py?',
							'Show total number of lines in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -w general.py',
				'NL Queries':['Print number of words in the file.',
							'How do I know the number of words in general.py?',
							'Show total number of words in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -m general.py',
				'NL Queries':['Print number of characters in the file.',
							'How do I know the number of characters in general.py?',
							'Show total number of characters in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -c general.py',
				'NL Queries':['Print total number of bytes in the file.',
							'How do I know the total number of bytes in general.py?',
							'Show total number of bytes in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -L general.py',
				'NL Queries':['Print length of largest line in the file.',
							'How do I know the length of largest line in general.py?',
							'Show length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lw general.py',
				'NL Queries':['Print number of lines and number of words in the file.',
							'How do I know the number of lines and number of words in general.py?',
							'Show total number of lines and words in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lm general.py',
				'NL Queries':['Print number of lines and number of characters in the file.',
							'How do I know the number of lines and number of characters in general.py?',
							'Show total number of lines and characters in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lc general.py',
				'NL Queries':['Print number of lines and number of bytes in the file.',
							'How do I know the number of lines and number of bytes in general.py?',
							'Show total number of lines and total number of bytes in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lL general.py',
				'NL Queries':['Print number of lines and length of largest line in the file.',
							'How do I know the number of lines and length of largest line in general.py?',
							'Show total number of lines and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lwm general.py',
				'NL Queries':['Print number of lines , number of words and number of characters in the file.',
							'How do I know the number of lines , number of words and number of characters in general.py?',
							'Show total number of lines , words and characters in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lwc general.py',
				'NL Queries':['Print number of lines , number of words and number of bytes in the file.',
							'How do I know the number of lines , number of words and number of bytes in general.py?',
							'Show total number of lines , words and bytes in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lwL general.py',
				'NL Queries':['Print number of lines , number of words and length of largest line in the file.',
							'How do I know the number of lines , number of words and length of largest line in general.py?',
							'Show total number of lines , words and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lmc general.py',
				'NL Queries':['Print number of lines , number of characters and number of bytes in the file.',
							'How do I know the number of lines , number of characters and number of bytes in general.py?',
							'Show total number of lines , characters and total number of bytes in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lmL general.py',
				'NL Queries':['Print number of lines , number of characters and length of largest line in the file.',
							'How do I know the number of lines , number of characters and length of largest line in general.py?',
							'Show total number of lines , characters and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lcL general.py',
				'NL Queries':['Print number of lines , number of bytes and length of largest line in the file.',
							'How do I know the number of lines , number of bytes and length of largest line in general.py?',
							'Show total number of lines , total number of bytes and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -wm general.py',
				'NL Queries':['Print number of words and number of characters in the file.',
							'How do I know the number of words and number of characters in general.py?',
							'Show total number of words and characters in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -wc general.py',
				'NL Queries':['Print number of words and number of bytes in the file.',
							'How do I know the number of words and number of bytes in general.py?',
							'Show total number of words and total number of bytes in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -wL general.py',
				'NL Queries':['Print number of words and length of largest line in the file.',
							'How do I know the number of words and length of largest line in general.py?',
							'Show total number of words and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -cL general.py',
				'NL Queries':['Print total number of bytes and length of largest line in the file.',
							'How do I know the total number of bytes and and length of largest line in general.py?',
							'Show total number of bytes and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -wmc general.py',
				'NL Queries':['Print number of words , number of characters and total number of bytes in the file.',
							'How do I know the number of words , number of characters and total number of bytes in general.py?',
							'Show total number of words , characters and total number of bytes in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -wmL general.py',
				'NL Queries':['Print number of words , number of characters and length of largest line in the file.',
							'How do I know the number of words , number of characters and length of largest line in general.py?',
							'Show total number of words , characters and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -wcL general.py',
				'NL Queries':['Print total number of words , total number of bytes and length of largest line in the file.',
							'How do I know the total number of words , total number of bytes and and length of largest line in general.py?',
							'Show total number of words , total number of bytes and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -mc general.py',
				'NL Queries':['Print total number of bytes and characters in the file.',
							'How do I know the total number of bytes and characters in general.py?',
							'Show total number of bytes and characters in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -mL general.py',
				'NL Queries':['Print number of characters and length of largest line in the file.',
							'How do I know the number of characters and length of largest line in general.py?',
							'Show total number of characters and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -mcL general.py',
				'NL Queries':['Print total number of bytes , characters and length of largest line in the file.',
							'How do I know the total number of bytes , characters and length of largest line in general.py?',
							'Show total number of bytes , characters and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lwmc general.py',
				'NL Queries':['Print number of lines , number of words , number of characters and number of bytes in the file.',
							'How do I know the number of lines , number of words , number of characters and number of bytes in general.py?',
							'Show total number of lines , words , characters and total number of bytes in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lwmL general.py',
				'NL Queries':['Print number of lines , number of words , number of characters and length of largest line in the file.',
							'How do I know the number of lines , number of words , number of characters and length of largest line in general.py?',
							'Show total number of lines , words , characters and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lwcL general.py',
				'NL Queries':['Print number of lines , number of words , number of bytes and length of largest line in the file.',
							'How do I know the number of lines , number of words , number of bytes and length of largest line in general.py?',
							'Show total number of lines , words , bytes and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lmcL general.py',
				'NL Queries':['Print number of lines , number of characters , number of bytes and length of largest line in the file.',
							'How do I know the number of lines , number of characters , number of bytes and length of largest line in general.py?',
							'Show total number of lines , characters , total number of bytes and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -wmcL general.py',
				'NL Queries':['Print number of words , number of characters , total number of bytes and length of largest line in the file.',
							'How do I know the number of words , number of characters , total number of bytes and length of largest line in general.py?',
							'Show total number of words , characters , total number of bytes and length of largest line in the file general.py.']},ignore_index=True)

wc = wc.append({'Command':'wc -lwmcL general.py',
				'NL Queries':['Print number of lines , number of words , number of characters , total number of bytes and length of largest line in the file.',
							'How do I know the number of lines , number of words , number of characters , total number of bytes and length of largest line in general.py?',
							'Show total number of lines , number of words , characters , total number of bytes and length of largest line in the file general.py.']},ignore_index=True)



print wc.shape


