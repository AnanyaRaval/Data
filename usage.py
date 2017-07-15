import pandas as pd

''' usage is a dataframe comtaining 3 columns: 
Command name: string
Description: string
Synopsis: list of synopsis from man page
Dict of options: dictionary of options with the commmand 
'''
usage = pd.DataFrame(columns = ['Command Name', 'Description', 'Synopsis','Dict of options'])
dictionary = {}

#Command: pwd
dictionary = {'-L': 'Use PWD from environment, even if it contains symlinks','-P': 'Avoid all symlinks'}
usage = usage.append({'Command Name':'pwd','Description':'Print the full filename of the current working directory.','Synopsis':['pwd [OPTION]...'],'Dict of options':dictionary},ignore_index = True)

#Command: ln
dictionary = {'--backup':'make a backup of each existing destination file','-b':'like --backup but does not accept an argument','-d':'allow the superuser to attempt to hard link directories','-f':'remove existing destination files','-i':'prompt whether to remove destinations','-L':'dereference TARGETs that are symbolic links','-n':'treat LINK_NAME as a normal file if it is a symbolic link to a directory','-P':'make hard links directly to symbolic links','-r':'create symbolic links relative to link location','-s':'make symbolic links instead of hard links','-S':'override the usual backup suffix','-t':'specify the DIRECTORY in which to create the links','-T':'treat LINK_NAME as a normal file always','-v':'print name of each linked file'}
usage = usage.append({'Description':'make links between files','Command Name':'ln', 'Synopsis':['ln [OPTION]... [-T] TARGET LINK_NAME','ln [OPTION]... TARGET','ln [OPTION]... TARGET... DIRECTORY','ln [OPTION]... -t DIRECTORY TARGET...'],'Dict of options':dictionary},ignore_index=True)

dictionary = {}
dictionary = {'-a':'do not ignore entries starting with .','-A':'do not list implied . and ..','--author':'with -l, print the author of each file','--all':'do not ignore entries starting with .','--almost-all':'do not list implied . and ..','-b':'print C-style escapes for nongraphic characters','--escape':'print C-style escapes for nongraphic characters','--block-size=SIZE':'scale sizes by SIZE before printing them.  E.g., \'--block-size=M \\' ' prints sizes in units of 1,048,576 bytes.','-B':'--ignore-back do not list implied entries ending with ~','-c':'with  -lt:  sort  by,  and show, ctime (time of last modification of file status information) with -l: show ctime and sort by name otherwise: sort by ctime, newest first'}
dictionary['-C'] = 'list entries by columns'
dictionary['--color[=WHEN]'] = 'colorize the output.  WHEN defaults to \'always\' or can be \'never\' or \'auto\'.'
dictionary['-d'] = 'list directory entries instead of contents, and do not dereference symbolic links'
dictionary['--directory'] = 'list directory entries instead of contents, and do not dereference symbolic links'
dictionary['-D'] = 'generate output designed for Emacs\' dired mode\''
dictionary['--dired'] = 'generate output designed for Emacs\' dired mode\''
dictionary['-f'] = 'do not sort, enable -aU, disable -ls --color'
dictionary['-F'] = 'append indicator (one of */=>@|) to entries'
dictionary['--classify'] = 'append indicator (one of */=>@|) to entries'
dictionary['--file-type'] = 'likewise, except do not append \'*\''
dictionary['--format=WORD'] = 'across -x, commas -m, horizontal -x, long -l, single-column -1, verbose -l, vertical -C'
dictionary['--full-time'] = 'like -l --time-style=full-iso'
dictionary['-g'] = 'like -l, but do not list owner'
dictionary['--group-directories-first'] = 'group directories before files. augment with a --sort option, but any use of --sort=none (-U) disables grouping'
dictionary['-G'] = 'in a long listing, don\'t print group names'
dictionary['--no-group'] = 'in a long listing, don\'t print group names'
dictionary['-h'] = 'with -l, print sizes in human readable format (e.g., 1K 234M 2G)'
dictionary['--human-readable'] = 'with -l, print sizes in human readable format (e.g., 1K 234M 2G)'
dictionary['--si'] = 'likewise, but use powers of 1000 not 1024'
dictionary['H'] = 'follow symbolic links listed on the command line'
dictionary['--dereference-command-line'] = 'follow symbolic links listed on the command line'
dictionary['--dereference-command-line-symlink-to-dir'] = 'follow each command line symbolic link that points to a directory'
dictionary['--hide=PATTERN'] = 'do not list implied entries matching shell PATTERN (overridden by -a or -A)'
dictionary['--indicator-style=WORD'] = 'append indicator with style WORD to entry names: none (default), slash (-p), file-type (--file-type), classify (-F)'
dictionary['-i'] = 'print the index number of each file'
dictionary['--inode'] = 'print the index number of each file'
dictionary['-I'] = 'do not list implied entries matching shell PATTERN'
dictionary['--ignore = PATTERN'] = 'do not list implied entries matching shell PATTERN'
dictionary['-k'] = 'use 1024-byte blocks'
dictionary['--kibibytes'] = 'use 1024-byte blocks'
dictionary['-l']  = 'use a long listing format'
dictionary['-L'] = 'when showing file information for a symbolic link, show information for the file the link references rather than for the link itself'
dictionary ['--dereference'] = 'when showing file information for a symbolic link, show information for the file the link references rather than for the link itself'
dictionary['-m'] = 'fill width with a comma separated list of entries'
dictionary['-n'] = 'like -l, but list numeric user and group IDs'
dictionary['--numeric-uid-gid'] = 'like -l, but list numeric user and group IDs'
dictionary['-N'] = 'print raw entry names (don\'t treat e.g. control characters specially)'
dictionary['--literal'] = 'print raw entry names (don\'t treat e.g. control characters specially)'
dictionary['-o'] = 'like -l, but do not list group information'
dictionary['-p'] = 'append / indicator to directories'
dictionary['--indicator-style= slash'] = 'append / indicator to directories'
dictionary['-q'] = 
dictionary['--hide-control-chars'] = 'print ? instead of non graphic characters'
dictionary['--show-control-chars'] = 'show non graphic characters as-is (default unless program is \'ls\' and output is a terminal)'
dictionary['-Q'] = 
dictionary['--quote-name'] = 'enclose entry names in double quotes'
dctionary['--quoting-style=WORD'] = 'use quoting style WORD for entry names: literal, locale, shell, shell-always, c, escape'
dictionary['-r'] = 
dictionary['--reverse'] = 'reverse order while sorting'
dictionary['-R'] = 'list subdirectories recursively'
dictionary['--recursive'] = 'list subdirectories recursively'

       -r, --reverse
              reverse order while sorting

       -R, --recursive
              list subdirectories recursively

       -s, --size
              print the allocated size of each file, in blocks

       -S     sort by file size

       --sort=WORD
              sort by WORD instead of name: none -U, extension -X, size -S, time -t, version -v

       --time=WORD
              with  -l,  show time as WORD instead of modification time: atime -u, access -u, use -u, ctime -c, or status -c; use specified
              time as sort key if --sort=time

       --time-style=STYLE
              with -l, show times using style STYLE: full-iso, long-iso, iso, locale, +FORMAT.  FORMAT is interpreted like 'date'; if  FOR‐
              MAT  is  FORMAT1<newline>FORMAT2,  FORMAT1 applies to non-recent files and FORMAT2 to recent files; if STYLE is prefixed with
              'posix-', STYLE takes effect only outside the POSIX locale

       -t     sort by modification time, newest first

       -T, --tabsize=COLS
              assume tab stops at each COLS instead of 8

       -u     with -lt: sort by, and show, access time with -l: show access time and sort by name otherwise: sort by access time

       -U     do not sort; list entries in directory order

       -v     natural sort of (version) numbers within text

       -w, --width=COLS
              assume screen width instead of current value

       -x     list entries by lines instead of by columns

       -X     sort alphabetically by entry extension

       -Z, --context
              print any SELinux security context of each file

       -1     list one file per line}
print dictionary.keys()

print usage
print dictionary
