- various simple tasks, maybe in a worksheet. Do first x steps, then pause and discuss results
& issues, pose questions
- windows users should have mingw or git bash installed, for access to basic unix command line
tools

- navigating terminal:
    - what path does your terminal start at? where is home?
    - pwd and ls to get your bearings
        - `ls` options: -a, -l, combine them to -al
    - save output of ls to a file: `ls -al > file_list.txt`
    - create temp dir
    - create some files and subdirs within that temp dir
        - create files using only the command line:
            - empty ones with touch
            - use
    - open up one of the files in editor, add some text, save close, now list its contents at
    command line using cat
        - now append some more text to it using cat, careful not to overwrite it!
    - cd between various dirs, list contents of current dir, list contents of all subdirs,
    show how tedious it is to have to cd between different dirs just to list them
    - using `ls --help`, figure out how to list dir contents without cd'ing to that path,
    although --help doesn't help much in this case: ls path/to/dir
    - copy a file
    - copy a folder, what happens?
        - `cp` on its own only works on files, `cp -r` copies folder and all its contents
    - remove a file
    - remove a subdir, what happens?
        - `rm -r`, but better to use `rm -rv` for verbosity

- run a couple of simple python scripts, edit to make specific simple changes in behaviour
- predict and test logic value of various different data types:
    - what will "`if True`" do?
    - `if False, if None, if 0, if 0.0, if '', if '0', if '1'`
- write a Python program that asks user for various data, name, email, birth day month year,
and then uses a for loop to print out a report of the data entered
    - what if values are left blank, what happens?
    - add check to see if any values are blank, keep querying user for non-blank entry
    - report if birth year is an even number
        - what do you have to do first to year input before you can test it numerically?
    - add a for loop to print out all years from 1950 until year of birth, one year per line
    - do it again using a while loop
- take some poorly formatted (though syntactically correct) code, in groups discuss and
predict what it will do, then individually test it to see if it works as predicted, clean it
up to make it ~ PEP8 compliant, test again to make sure it still works, compare rewrites
within the group, have a couple of them present to full class?

- `turtle`?
