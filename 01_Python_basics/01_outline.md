- Python basics
    - motivation:
        - example: load data, analyze, plot, save
    - command line basics, assume git bash or mingw installed on windows
        - cd, ls, mv, cp, rm, touch, cat
        - man and --help for help
        - save text output of a command to file using redirection:
            - `ls > file_list.txt`
            - `cat > shopping_list.txt`
                - Ctrl+D to finish entering
            - redirection overwrites any existing file!
            - view a file using cat filename.txt
    - py interpreter
        - interpreted vs compiled languages?
        - calculator, math operators
        - `print('hello world')`
            - intro to functions: take input, generate output
        - `input()`
    - make hello world script, run from command line
    - variable assignment
        - tuple expansion
    - help
        - in py interp
        - online
    - basic Python data types
        - `int, float, str, bool`
            - types also are functions that convert input to that type
            - literals: `1, 1.0, '1', True`
        - `None`
        - division always gives float, unless `//` (div)
            - find remainder using %
        - using `type()`
    - control flow:
        - `if` statements
        - `for` loops
            - tabs vs spaces, check your editor
            - `range()`
            - `break`, `continue`
        - `while` loops
    - a few tips from coding style guide
        - PEP 8: https://www.python.org/dev/peps/pep-0008/
        - why does coding style matter - easier to read, understand, debug
            - like trying to read a book without paragraphs