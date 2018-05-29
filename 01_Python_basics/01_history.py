mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md
mspacek@Godel:~/SciPyCourse2018/notes$ pwd
/home/mspacek/SciPyCourse2018/notes
mspacek@Godel:~/SciPyCourse2018/notes$ pwd
/home/mspacek/SciPyCourse2018/notes
mspacek@Godel:~/SciPyCourse2018/notes$ cd
mspacek@Godel:~$ cd -
/home/mspacek/SciPyCourse2018/notes
mspacek@Godel:~/SciPyCourse2018/notes$ pwd
/home/mspacek/SciPyCourse2018/notes
mspacek@Godel:~/SciPyCourse2018/notes$ cd 01_Python_basics/
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ cd ..
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md
mspacek@Godel:~/SciPyCourse2018/notes$ ls -l
total 16
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:17 00_intro
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:28 01_Python_basics
drwxrwxr-x 14 mspacek mspacek 4096 Apr 10 00:26 old_notes
-rw-rw-r--  1 mspacek mspacek   20 Mar 28  2017 README.md
mspacek@Godel:~/SciPyCourse2018/notes$ cd /
mspacek@Godel:/$ ls
bin  boot  dev  etc  home  initrd.img  initrd.img.old  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  snap  srv  sys  tmp  usr  var  vmlinuz  vmlinuz.old
mspacek@Godel:/$ cd -
/home/mspacek/SciPyCourse2018/notes
mspacek@Godel:~/SciPyCourse2018/notes$ cd -
/
mspacek@Godel:/$ cd -
/home/mspacek/SciPyCourse2018/notes
mspacek@Godel:~/SciPyCourse2018/notes$ cd -
/
mspacek@Godel:/$ cd -
/home/mspacek/SciPyCourse2018/notes
mspacek@Godel:~/SciPyCourse2018/notes$ cd ~
mspacek@Godel:~$ cd -
/home/mspacek/SciPyCourse2018/notes
mspacek@Godel:~/SciPyCourse2018/notes$ cd .
mspacek@Godel:~/SciPyCourse2018/notes$ mv
mv: missing file operand
Try 'mv --help' for more information.
mspacek@Godel:~/SciPyCourse2018/notes$ mv --help
Usage: mv [OPTION]... [-T] SOURCE DEST
  or:  mv [OPTION]... SOURCE... DIRECTORY
  or:  mv [OPTION]... -t DIRECTORY SOURCE...
Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

Mandatory arguments to long options are mandatory for short options too.
      --backup[=CONTROL]       make a backup of each existing destination file
  -b                           like --backup but does not accept an argument
  -f, --force                  do not prompt before overwriting
  -i, --interactive            prompt before overwrite
  -n, --no-clobber             do not overwrite an existing file
If you specify more than one of -i, -f, -n, only the final one takes effect.
      --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                 argument
  -S, --suffix=SUFFIX          override the usual backup suffix
  -t, --target-directory=DIRECTORY  move all SOURCE arguments into DIRECTORY
  -T, --no-target-directory    treat DEST as a normal file
  -u, --update                 move only when the SOURCE file is newer
                                 than the destination file or when the
                                 destination file is missing
  -v, --verbose                explain what is being done
  -Z, --context                set SELinux security context of destination
                                 file to default type
      --help     display this help and exit
      --version  output version information and exit

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       never make backups (even if --backup is given)
  numbered, t     make numbered backups
  existing, nil   numbered if numbered backups exist, simple otherwise
  simple, never   always make simple backups

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/mv>
or available locally via: info '(coreutils) mv invocation'
mspacek@Godel:~/SciPyCourse2018/notes$ man mv
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md
mspacek@Godel:~/SciPyCourse2018/notes$ mkdir tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ cd tmp
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ touch test.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls
test.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls -al
total 8
drwxrwxr-x 2 mspacek mspacek 4096 Apr 10 13:57 .
drwxrwxr-x 7 mspacek mspacek 4096 Apr 10 13:56 ..
-rw-rw-r-- 1 mspacek mspacek    0 Apr 10 13:57 test.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls -al
total 8
drwxrwxr-x 2 mspacek mspacek 4096 Apr 10 13:57 .
drwxrwxr-x 7 mspacek mspacek 4096 Apr 10 13:56 ..
-rw-rw-r-- 1 mspacek mspacek    0 Apr 10 13:57 test.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ mv test.txt test2.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls -al
total 8
drwxrwxr-x 2 mspacek mspacek 4096 Apr 10 13:57 .
drwxrwxr-x 7 mspacek mspacek 4096 Apr 10 13:56 ..
-rw-rw-r-- 1 mspacek mspacek    0 Apr 10 13:57 test2.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ mv test2.txt ..
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls -al
total 8
drwxrwxr-x 2 mspacek mspacek 4096 Apr 10 13:58 .
drwxrwxr-x 7 mspacek mspacek 4096 Apr 10 13:58 ..
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls ..
00_intro  01_Python_basics  old_notes  README.md  test2.txt  tmp
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ cd ..
mspacek@Godel:~/SciPyCourse2018/notes$
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md  test2.txt  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ mv --help
Usage: mv [OPTION]... [-T] SOURCE DEST
  or:  mv [OPTION]... SOURCE... DIRECTORY
  or:  mv [OPTION]... -t DIRECTORY SOURCE...
Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

Mandatory arguments to long options are mandatory for short options too.
      --backup[=CONTROL]       make a backup of each existing destination file
  -b                           like --backup but does not accept an argument
  -f, --force                  do not prompt before overwriting
  -i, --interactive            prompt before overwrite
  -n, --no-clobber             do not overwrite an existing file
If you specify more than one of -i, -f, -n, only the final one takes effect.
      --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                 argument
  -S, --suffix=SUFFIX          override the usual backup suffix
  -t, --target-directory=DIRECTORY  move all SOURCE arguments into DIRECTORY
  -T, --no-target-directory    treat DEST as a normal file
  -u, --update                 move only when the SOURCE file is newer
                                 than the destination file or when the
                                 destination file is missing
  -v, --verbose                explain what is being done
  -Z, --context                set SELinux security context of destination
                                 file to default type
      --help     display this help and exit
      --version  output version information and exit

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       never make backups (even if --backup is given)
  numbered, t     make numbered backups
  existing, nil   numbered if numbered backups exist, simple otherwise
  simple, never   always make simple backups

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/mv>
or available locally via: info '(coreutils) mv invocation'
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md  test2.txt  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ cp test2.txt tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md  test2.txt  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ cd tmp
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls
test2.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ cd ..
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md  test2.txt  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ mv test2.txt tmp
mspacek@Godel:~/SciPyCourse2018/notes$ cd tmp
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls
test2.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls -al
total 8
drwxrwxr-x 2 mspacek mspacek 4096 Apr 10 14:00 .
drwxrwxr-x 7 mspacek mspacek 4096 Apr 10 14:00 ..
-rw-rw-r-- 1 mspacek mspacek    0 Apr 10 13:57 test2.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ cd ..
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ cd tmp
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls
test2.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ mv test2.txt ..
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ cd ..
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  old_notes  README.md  test2.txt  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ mv test2.txt tmp
mspacek@Godel:~/SciPyCourse2018/notes$ cd tmp
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls
test2.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ cat > test2.txt
sdlkjfsldkfjlds
sdlkfjsldkfjsldjf
sldjflskdfj
sjdlfksjdlfksjdf
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ cat test2.txt
sdlkjfsldkfjlds
sdlkfjsldkfjsldjf
sldjflskdfj
sjdlfksjdlfksjdf
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls
test2.txt
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ mv -v test2.txt
mv: missing destination file operand after 'test2.txt'
Try 'mv --help' for more information.
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ mv --help
Usage: mv [OPTION]... [-T] SOURCE DEST
  or:  mv [OPTION]... SOURCE... DIRECTORY
  or:  mv [OPTION]... -t DIRECTORY SOURCE...
Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

Mandatory arguments to long options are mandatory for short options too.
      --backup[=CONTROL]       make a backup of each existing destination file
  -b                           like --backup but does not accept an argument
  -f, --force                  do not prompt before overwriting
  -i, --interactive            prompt before overwrite
  -n, --no-clobber             do not overwrite an existing file
If you specify more than one of -i, -f, -n, only the final one takes effect.
      --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                 argument
  -S, --suffix=SUFFIX          override the usual backup suffix
  -t, --target-directory=DIRECTORY  move all SOURCE arguments into DIRECTORY
  -T, --no-target-directory    treat DEST as a normal file
  -u, --update                 move only when the SOURCE file is newer
                                 than the destination file or when the
                                 destination file is missing
  -v, --verbose                explain what is being done
  -Z, --context                set SELinux security context of destination
                                 file to default type
      --help     display this help and exit
      --version  output version information and exit

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       never make backups (even if --backup is given)
  numbered, t     make numbered backups
  existing, nil   numbered if numbered backups exist, simple otherwise
  simple, never   always make simple backups

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/mv>
or available locally via: info '(coreutils) mv invocation'
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ mv -v test2.txt ..
'test2.txt' -> '../test2.txt'
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ mv --help
Usage: mv [OPTION]... [-T] SOURCE DEST
  or:  mv [OPTION]... SOURCE... DIRECTORY
  or:  mv [OPTION]... -t DIRECTORY SOURCE...
Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

Mandatory arguments to long options are mandatory for short options too.
      --backup[=CONTROL]       make a backup of each existing destination file
  -b                           like --backup but does not accept an argument
  -f, --force                  do not prompt before overwriting
  -i, --interactive            prompt before overwrite
  -n, --no-clobber             do not overwrite an existing file
If you specify more than one of -i, -f, -n, only the final one takes effect.
      --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                 argument
  -S, --suffix=SUFFIX          override the usual backup suffix
  -t, --target-directory=DIRECTORY  move all SOURCE arguments into DIRECTORY
  -T, --no-target-directory    treat DEST as a normal file
  -u, --update                 move only when the SOURCE file is newer
                                 than the destination file or when the
                                 destination file is missing
  -v, --verbose                explain what is being done
  -Z, --context                set SELinux security context of destination
                                 file to default type
      --help     display this help and exit
      --version  output version information and exit

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       never make backups (even if --backup is given)
  numbered, t     make numbered backups
  existing, nil   numbered if numbered backups exist, simple otherwise
  simple, never   always make simple backups

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/mv>
or available locally via: info '(coreutils) mv invocation'
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ man mv
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ ls -al
total 8
drwxrwxr-x 2 mspacek mspacek 4096 Apr 10 14:20 .
drwxrwxr-x 7 mspacek mspacek 4096 Apr 10 14:20 ..
mspacek@Godel:~/SciPyCourse2018/notes/tmp$ cd ..
mspacek@Godel:~/SciPyCourse2018/notes$ ls -al
total 40
drwxrwxr-x  7 mspacek mspacek 4096 Apr 10 14:20 .
drwxrwxr-x  5 mspacek mspacek 4096 Apr  9 17:42 ..
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:17 00_intro
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:28 01_Python_basics
drwxrwxr-x  8 mspacek mspacek 4096 Apr 10 11:29 .git
-rw-rw-r--  1 mspacek mspacek   85 Apr 10 01:58 .gitignore
drwxrwxr-x 14 mspacek mspacek 4096 Apr 10 00:26 old_notes
-rw-rw-r--  1 mspacek mspacek   20 Mar 28  2017 README.md
-rw-rw-r--  1 mspacek mspacek   63 Apr 10 14:04 test2.txt
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 14:20 tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls -al > mylisting.txt
mspacek@Godel:~/SciPyCourse2018/notes$ cat mylisting.txt
total 40
drwxrwxr-x  7 mspacek mspacek 4096 Apr 10 14:27 .
drwxrwxr-x  5 mspacek mspacek 4096 Apr  9 17:42 ..
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:17 00_intro
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:28 01_Python_basics
drwxrwxr-x  8 mspacek mspacek 4096 Apr 10 11:29 .git
-rw-rw-r--  1 mspacek mspacek   85 Apr 10 01:58 .gitignore
-rw-rw-r--  1 mspacek mspacek    0 Apr 10 14:27 mylisting.txt
drwxrwxr-x 14 mspacek mspacek 4096 Apr 10 00:26 old_notes
-rw-rw-r--  1 mspacek mspacek   20 Mar 28  2017 README.md
-rw-rw-r--  1 mspacek mspacek   63 Apr 10 14:04 test2.txt
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 14:20 tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls -al
total 44
drwxrwxr-x  7 mspacek mspacek 4096 Apr 10 14:27 .
drwxrwxr-x  5 mspacek mspacek 4096 Apr  9 17:42 ..
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:17 00_intro
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:28 01_Python_basics
drwxrwxr-x  8 mspacek mspacek 4096 Apr 10 11:29 .git
-rw-rw-r--  1 mspacek mspacek   85 Apr 10 01:58 .gitignore
-rw-rw-r--  1 mspacek mspacek  632 Apr 10 14:27 mylisting.txt
drwxrwxr-x 14 mspacek mspacek 4096 Apr 10 00:26 old_notes
-rw-rw-r--  1 mspacek mspacek   20 Mar 28  2017 README.md
-rw-rw-r--  1 mspacek mspacek   63 Apr 10 14:04 test2.txt
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 14:20 tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls -l
total 28
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:17 00_intro
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:28 01_Python_basics
-rw-rw-r--  1 mspacek mspacek  632 Apr 10 14:27 mylisting.txt
drwxrwxr-x 14 mspacek mspacek 4096 Apr 10 00:26 old_notes
-rw-rw-r--  1 mspacek mspacek   20 Mar 28  2017 README.md
-rw-rw-r--  1 mspacek mspacek   63 Apr 10 14:04 test2.txt
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 14:20 tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls -l > anotherlisting.txt
mspacek@Godel:~/SciPyCourse2018/notes$ cat anotherlisting.txt
total 28
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:17 00_intro
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:28 01_Python_basics
-rw-rw-r--  1 mspacek mspacek    0 Apr 10 14:28 anotherlisting.txt
-rw-rw-r--  1 mspacek mspacek  632 Apr 10 14:27 mylisting.txt
drwxrwxr-x 14 mspacek mspacek 4096 Apr 10 00:26 old_notes
-rw-rw-r--  1 mspacek mspacek   20 Mar 28  2017 README.md
-rw-rw-r--  1 mspacek mspacek   63 Apr 10 14:04 test2.txt
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 14:20 tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic characters
      --block-size=SIZE      scale sizes by SIZE before printing them; e.g.,
                               '--block-size=M' prints sizes in units of
                               1,048,576 bytes; see SIZE format below
  -B, --ignore-backups       do not list implied entries ending with ~
  -c                         with -lt: sort by, and show, ctime (time of last
                               modification of file status information);
                               with -l: show ctime and sort by name;
                               otherwise: sort by ctime, newest first
  -C                         list entries by columns
      --color[=WHEN]         colorize the output; WHEN can be 'always' (default
                               if omitted), 'auto', or 'never'; more info below
  -d, --directory            list directories themselves, not their contents
  -D, --dired                generate output designed for Emacs' dired mode
  -f                         do not sort, enable -aU, disable -ls --color
  -F, --classify             append indicator (one of */=>@|) to entries
      --file-type            likewise, except do not append '*'
      --format=WORD          across -x, commas -m, horizontal -x, long -l,
                               single-column -1, verbose -l, vertical -C
      --full-time            like -l --time-style=full-iso
  -g                         like -l, but do not list owner
      --group-directories-first
                             group directories before files;
                               can be augmented with a --sort option, but any
                               use of --sort=none (-U) disables grouping
  -G, --no-group             in a long listing, don't print group names
  -h, --human-readable       with -l and/or -s, print human readable sizes
                               (e.g., 1K 234M 2G)
      --si                   likewise, but use powers of 1000 not 1024
  -H, --dereference-command-line
                             follow symbolic links listed on the command line
      --dereference-command-line-symlink-to-dir
                             follow each command line symbolic link
                               that points to a directory
      --hide=PATTERN         do not list implied entries matching shell PATTERN
                               (overridden by -a or -A)
      --indicator-style=WORD  append indicator with style WORD to entry names:
                               none (default), slash (-p),
                               file-type (--file-type), classify (-F)
  -i, --inode                print the index number of each file
  -I, --ignore=PATTERN       do not list implied entries matching shell PATTERN
  -k, --kibibytes            default to 1024-byte blocks for disk usage
  -l                         use a long listing format
  -L, --dereference          when showing file information for a symbolic
                               link, show information for the file the link
                               references rather than for the link itself
  -m                         fill width with a comma separated list of entries
  -n, --numeric-uid-gid      like -l, but list numeric user and group IDs
  -N, --litreal              print raw entry names (don't treat e.g. control
                               characters specially)
  -o                         like -l, but do not list group information
  -p, --indicator-style=slash
                             append / indicator to directories
  -q, --hide-control-chars   print ? instead of nongraphic characters
      --show-control-chars   show nongraphic characters as-is (the default,
                               unless program is 'ls' and output is a terminal)
  -Q, --quote-name           enclose entry names in double quotes
      --quoting-style=WORD   use quoting style WORD for entry names:
                               literal, locale, shell, shell-always,
                               shell-escape, shell-escape-always, c, escape
  -r, --reverse              reverse order while sorting
  -R, --recursive            list subdirectories recursively
  -s, --size                 print the allocated size of each file, in blocks
  -S                         sort by file size, largest first
      --sort=WORD            sort by WORD instead of name: none (-U), size (-S),
                               time (-t), version (-v), extension (-X)
      --time=WORD            with -l, show time as WORD instead of default
                               modification time: atime or access or use (-u);
                               ctime or status (-c); also use specified time
                               as sort key if --sort=time (newest first)
      --time-style=STYLE     with -l, show times using style STYLE:
                               full-iso, long-iso, iso, locale, or +FORMAT;
                               FORMAT is interpreted like in 'date'; if FORMAT
                               is FORMAT1<newline>FORMAT2, then FORMAT1 applies
                               to non-recent files and FORMAT2 to recent files;
                               if STYLE is prefixed with 'posix-', STYLE
                               takes effect only outside the POSIX locale
  -t                         sort by modification time, newest first
  -T, --tabsize=COLS         assume tab stops at each COLS instead of 8
  -u                         with -lt: sort by, and show, access time;
                               with -l: show access time and sort by name;
                               otherwise: sort by access time, newest first
  -U                         do not sort; list entries in directory order
  -v                         natural sort of (version) numbers within text
  -w, --width=COLS           set output width to COLS.  0 means no limit
  -x                         list entries by lines instead of by columns
  -X                         sort alphabetically by entry extension
  -Z, --context              print any security context of each file
  -1                         list one file per line.  Avoid '\n' with -q or -b
      --help     display this help and exit
      --version  output version information and exit

The SIZE argument is an integer and optional unit (example: 10K is 10*1024).
Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,... (powers of 1000).

Using color to distinguish file types is disabled both by default and
with --color=never.  With --color=auto, ls emits color codes only when
standard output is connected to a terminal.  The LS_COLORS environment
variable can change the settings.  Use the dircolors command to set it.

Exit status:
 0  if OK,
 1  if minor problems (e.g., cannot access subdirectory),
 2  if serious trouble (e.g., cannot access command-line argument).

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/ls>
or available locally via: info '(coreutils) ls invocation'
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  anotherlisting.txt  mylisting.txt  old_notes  README.md  test2.txt  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  anotherlisting.txt  mylisting.txt  old_notes  README.md  test2.txt  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  anotherlisting.txt  mylisting.txt  old_notes  README.md  test2.txt  tmp
mspacek@Godel:~/SciPyCourse2018/notes$ cp tmp tmp2
cp: omitting directory 'tmp'
mspacek@Godel:~/SciPyCourse2018/notes$ cp --help
Usage: cp [OPTION]... [-T] SOURCE DEST
  or:  cp [OPTION]... SOURCE... DIRECTORY
  or:  cp [OPTION]... -t DIRECTORY SOURCE...
Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.

Mandatory arguments to long options are mandatory for short options too.
  -a, --archive                same as -dR --preserve=all
      --attributes-only        don't copy the file data, just the attributes
      --backup[=CONTROL]       make a backup of each existing destination file
  -b                           like --backup but does not accept an argument
      --copy-contents          copy contents of special files when recursive
  -d                           same as --no-dereference --preserve=links
  -f, --force                  if an existing destination file cannot be
                                 opened, remove it and try again (this option
                                 is ignored when the -n option is also used)
  -i, --interactive            prompt before overwrite (overrides a previous -n
                                  option)
  -H                           follow command-line symbolic links in SOURCE
  -l, --link                   hard link files instead of copying
  -L, --dereference            always follow symbolic links in SOURCE
  -n, --no-clobber             do not overwrite an existing file (overrides
                                 a previous -i option)
  -P, --no-dereference         never follow symbolic links in SOURCE
  -p                           same as --preserve=mode,ownership,timestamps
      --preserve[=ATTR_LIST]   preserve the specified attributes (default:
                                 mode,ownership,timestamps), if possible
                                 additional attributes: context, links, xattr,
                                 all
      --no-preserve=ATTR_LIST  don't preserve the specified attributes
      --parents                use full source file name under DIRECTORY
  -R, -r, --recursive          copy directories recursively
      --reflink[=WHEN]         control clone/CoW copies. See below
      --remove-destination     remove each existing destination file before
                                 attempting to open it (contrast with --force)
      --sparse=WHEN            control creation of sparse files. See below
      --strip-trailing-slashes  remove any trailing slashes from each SOURCE
                                 argument
  -s, --symbolic-link          make symbolic links instead of copying
  -S, --suffix=SUFFIX          override the usual backup suffix
  -t, --target-directory=DIRECTORY  copy all SOURCE arguments into DIRECTORY
  -T, --no-target-directory    treat DEST as a normal file
  -u, --update                 copy only when the SOURCE file is newer
                                 than the destination file or when the
                                 destination file is missing
  -v, --verbose                explain what is being done
  -x, --one-file-system        stay on this file system
  -Z                           set SELinux security context of destination
                                 file to default type
      --context[=CTX]          like -Z, or if CTX is specified then set the
                                 SELinux or SMACK security context to CTX
      --help     display this help and exit
      --version  output version information and exit

By default, sparse SOURCE files are detected by a crude heuristic and the
corresponding DEST file is made sparse as well.  That is the behavior
selected by --sparse=auto.  Specify --sparse=always to create a sparse DEST
file whenever the SOURCE file contains a long enough sequence of zero bytes.
Use --sparse=never to inhibit creation of sparse files.

When --reflink[=always] is specified, perform a lightweight copy, where the
data blocks are copied only when modified.  If this is not possible the copy
fails, or if --reflink=auto is specified, fall back to a standard copy.

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       never make backups (even if --backup is given)
  numbered, t     make numbered backups
  existing, nil   numbered if numbered backups exist, simple otherwise
  simple, never   always make simple backups

As a special case, cp makes a backup of SOURCE when the force and backup
options are given and SOURCE and DEST are the same name for an existing,
regular file.

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/cp>
or available locally via: info '(coreutils) cp invocation'
mspacek@Godel:~/SciPyCourse2018/notes$ cp -r tmp tmp2
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  anotherlisting.txt  mylisting.txt  old_notes  README.md  test2.txt  tmp  tmp2
mspacek@Godel:~/SciPyCourse2018/notes$ cd tmp2
mspacek@Godel:~/SciPyCourse2018/notes/tmp2$ ls
mspacek@Godel:~/SciPyCourse2018/notes/tmp2$ ls -al
total 8
drwxrwxr-x 2 mspacek mspacek 4096 Apr 10 14:33 .
drwxrwxr-x 8 mspacek mspacek 4096 Apr 10 14:33 ..
mspacek@Godel:~/SciPyCourse2018/notes/tmp2$ cd ..
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  anotherlisting.txt  mylisting.txt  old_notes  README.md  test2.txt  tmp  tmp2
mspacek@Godel:~/SciPyCourse2018/notes$ rm tmp
rm: cannot remove 'tmp': Is a directory
mspacek@Godel:~/SciPyCourse2018/notes$ rm -r tmp
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  anotherlisting.txt  mylisting.txt  old_notes  README.md  test2.txt  tmp2
mspacek@Godel:~/SciPyCourse2018/notes$ mv tmp2 tmp1
mspacek@Godel:~/SciPyCourse2018/notes$ ls -al
total 48
drwxrwxr-x  7 mspacek mspacek 4096 Apr 10 14:35 .
drwxrwxr-x  5 mspacek mspacek 4096 Apr  9 17:42 ..
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:17 00_intro
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 11:28 01_Python_basics
-rw-rw-r--  1 mspacek mspacek  486 Apr 10 14:28 anotherlisting.txt
drwxrwxr-x  8 mspacek mspacek 4096 Apr 10 11:29 .git
-rw-rw-r--  1 mspacek mspacek   85 Apr 10 01:58 .gitignore
-rw-rw-r--  1 mspacek mspacek  632 Apr 10 14:27 mylisting.txt
drwxrwxr-x 14 mspacek mspacek 4096 Apr 10 00:26 old_notes
-rw-rw-r--  1 mspacek mspacek   20 Mar 28  2017 README.md
-rw-rw-r--  1 mspacek mspacek   63 Apr 10 14:04 test2.txt
drwxrwxr-x  2 mspacek mspacek 4096 Apr 10 14:33 tmp1
mspacek@Godel:~/SciPyCourse2018/notes$ python
Python 2.7.12 (default, Dec  4 2017, 14:50:18)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
mspacek@Godel:~/SciPyCourse2018/notes$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+1
2
>>> 2*2
4
>>> 4/2
2.0
>>> 5-3
2
>>> print()

>>> 'this is a string'
'this is a string'
>>> print('this is a string')
this is a string
>>> 1
1
>>> 2
2
>>> 3
3
>>> 4
4
>>> 5
5
>>> 6
6
>>> 7
7
>>> 8
8
>>> -5
-5
>>> 5
5
>>> 2.5
2.5
>>> 1/2
0.5
>>> 5/2
2.5
>>> type
<class 'type'>
>>> type(1)
<class 'int'>
>>> type(2.5)
<class 'float'>
>>> type('hello')
<class 'str'>
>>> a = 1
>>> a
1
>>> type(a)
<class 'int'>
>>> a = 2.5
>>> s = 'hello world'
>>> s
'hello world'
>>> a
2.5
>>> a = 1
>>> a
1
>>> a + 1
2
>>> a * 10
10
>>> a += 1
>>> a
2
>>> a += 1
>>> a += 1
>>> a += 1
>>> a += 1
>>> a += 1
>>> a += 1
>>> a
8
>>> b =
  File "<stdin>", line 1
    b =
       ^
SyntaxError: invalid syntax
>>> b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> b = 5
>>> a = 0
>>> b = 'hello'
>>> b += 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
>>> a = 1
>>> 'hello' * 2
'hellohello'
>>> 'hello' * 10
'hellohellohellohellohellohellohellohellohellohello'
>>> 'hello' + 'bye'
'hellobye'
>>> 'hello' + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
>>> '1'
'1'
>>> type('1')
<class 'str'>
>>> 'hello' + '1'
'hello1'
>>> al2k3jld = 5
>>> 2342kdfsljk = 5
  File "<stdin>", line 1
    2342kdfsljk = 5
              ^
SyntaxError: invalid syntax
>>> _dlfkjlskd = 1
>>> import math
>>> math.sqrt(4)
2.0
>>> import math
>>> math
<module 'math' (built-in)>
>>> from math import sqrt
>>> sqrt
<built-in function sqrt>
>>> sqrt(4)
2.0
>>> True
True
>>> False
False
>>> type(True)
<class 'bool'>
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> None
>>> type(None)
<class 'NoneType'>
>>> 5 / 2
2.5
>>> 5 % 2
1
>>> 4 % 2
0
>>> 5 / 2
2.5
>>> 5 // 2
2
>>> a
1
>>> a == 1
True
>>> a == 2
False
>>> a = 2
>>> a == 2
True
>>> a
2
>>> print(a)
2
>>> a != 2
False
>>>
>>> a
2
>>> a > 5
False
>>> a >= 2
True
>>> a <= -5
False
>>> a < 5 and a > 10
False
>>> a
2
>>> a < 5 and a == 2
True
>>> a < -55 and a == 2
False
>>> a < -5 and a == 2
False
>>> a < 5 and a == 2
True
>>> a < -5 or a == 2
True
>>> a < -5 or not a == 2
False
>>> 1 | 2
3
>>> if
  File "<stdin>", line 1
    if
     ^
SyntaxError: invalid syntax
>>> a
2
>>> if a == 2:
...     print('hi')
...
hi
>>> if a == 3:
...     print('hi')
...     print('hello')
...
>>> if a == 3: print('hi')
...
>>> if a == 3:
...     print('a is 3')
... else:
...     print('a is not 3')
...
a is not 3
>>> if a == 3:
...     print('a is 3')
... elif a == 2:
...     print('a is 2')
... else:
...     print('a is something else')
...
a is 2
>>> for i in range(10):
...     print(i)
...
0
1
2
3
4
5
6
7
8
9
>>> range(10)
range(0, 10)
>>> type(range(10))
<class 'range'>
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> help(range)

>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(1, 11):
...     print(i)
...
1
2
3
4
5
6
7
8
9
10
>>> i
10
>>> for i in range(10):
...     if i == 5:
...         print('i is 5!')
...     else:
...         print(i)
...
0
1
2
3
4
i is 5!
6
7
8
9
>>> for i in range(10):
... c
  File "<stdin>", line 2
    c
    ^
IndentationError: expected an indented block
>>>
>>>
>>> a
2
>>> a = 0
>>> for i in range(10):
...     a += 1
...
>>> a
10
>>>
mspacek@Godel:~/SciPyCourse2018/notes$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
mspacek@Godel:~/SciPyCourse2018/notes$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
mspacek@Godel:~/SciPyCourse2018/notes$ ls
00_intro  01_Python_basics  anotherlisting.txt  mylisting.txt  old_notes  README.md  test2.txt  tmp1
mspacek@Godel:~/SciPyCourse2018/notes$ cd 01_Python_basics/
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ ls
01_Python_basics.md  01_Python_basics.pdf  hello.py
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ python hello.py
hello world
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ python hello.py
hello world
goodbye world
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ python --help
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-B     : don't write .py[co] files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser; also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-m mod : run library module as a script (terminates option list)
-O     : optimize generated bytecode slightly; also PYTHONOPTIMIZE=x
-OO    : remove doc-strings in addition to the -O optimizations
-R     : use a pseudo-random salt to make hash() values of various types be
         unpredictable between separate invocations of the interpreter, as
         a defense against denial-of-service attacks
-Q arg : division options: -Qold (default), -Qwarn, -Qwarnall, -Qnew
-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : don't imply 'import site' on initialization
-t     : issue warnings about inconsistent tab usage (-tt: issue errors)
-u     : unbuffered binary stdout and stderr; also PYTHONUNBUFFERED=x
         see man page for details on internal buffering relating to '-u'
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-3     : warn about Python 3.x incompatibilities that 2to3 cannot trivially fix
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]

Other environment variables:
PYTHONSTARTUP: file executed on interactive startup (no default)
PYTHONPATH   : ':'-separated list of directories prefixed to the
               default module search path.  The result is sys.path.
PYTHONHOME   : alternate <prefix> directory (or <prefix>:<exec_prefix>).
               The default module search path uses <prefix>/pythonX.X.
PYTHONCASEOK : ignore case in 'import' statements (Windows).
PYTHONIOENCODING: Encoding[:errors] used for stdin/stdout/stderr.
PYTHONHASHSEED: if this variable is set to 'random', the effect is the same
   as specifying the -R option: a random value is used to seed the hashes of
   str, bytes and datetime objects.  It can also be set to an integer
   in the range [0,4294967295] to get hash values with a predictable seed.
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ python -i hello.py
hello world
goodbye world
>>>
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ python -i hello.py
hello world
goodbye world
>>> a
1
>>> run
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'run' is not defined
>>>
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ mv hello.py hello.txt
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ python -i hello.txt
hello world
goodbye world
>>>
mspacek@Godel:~/SciPyCourse2018/notes/01_Python_basics$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: run hello.txt
hello world
goodbye world

In [2]:
