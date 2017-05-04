### collections, files

- review:
    - different ways of running code/scripts
        - in terminal/command line: type `python myscript.py`
            - exits immediately back to terminal when done, can't inspect variables or plots
            - add `input()` to last line of script to prevent exiting
        - run `ipython`, type `run myscript.py`, then you can inspect variables when it's done
        - run `python` or `ipython` interpreter, copy and paste code from editor to interpreter
            - IPython handles pasted code better than plain Python
        - Jupyter: like IPython, but in a web browser
    - IPython tips:
        - tab completion, saves time, mistakes, frustration - use it!
            ```
            verylong<TAB> -> verylongvariablename
            import math
            math.<TAB>
                .acos .acosh, .asin, .asinh, etc.
            math.fac<TAB> -> math.factorial
            cd lon<TAB> -> cd long\ pathname\ with\ spaces
            ````
        - `obj?` - get help about obj (variable, function, etc.)
        - separately numbered input and output lines
        - `_`, `__`, `___` - return last/2nd last/3rd last output
        - `_5` - return output of output line 5
        - `ipython_config.py` file in your hidden `~/.ipython` directory for changing defaults

- ways of installing python libraries/packages/modules, just for familiarity's sake:
    - `conda install`
    - `pip install`
    - less recommended: binaries (.exe, .zip), especially in windows, .dmg on Mac
    - ubuntu/deb repositories
    - advanced: from original source code, might require compiling

- collections
    - sequences
        - tuples
            - declare with `t = (value, value...)` or `t = value, value...`
                - often the parentheses are optional
            - tuple expansion allows for multiple assignment:
                - `a, b, c = (1, 2, 3)` or simply `a, b, c = 1, 2, 3`
            - methods: `.count()`, `.index()`
            - tuples can be used to `return` multiple values from a function
        - lists
            - init with `[]` or `list()`
            - extra methods: `.append(value)`, `.clear()`,
            - delete entries with `del`
            - convert to a list with `list()`
            - `del` an entry
        - indexing
            - 0-based
            - negative indices denote distance from end
        - slicing
            - `a[start:stop:step]`
            - fencepost analogy, slicing from one fencepost to another, not from one slot to
            another
            - negative indices also work for slices
            - colon `:` can be used as placeholder for start or stop if you don't want to specify them
        - iterating over sequences
            - for loops: `for val in sequence:`
                - `enumerate()`
                    - `for index, val in enumerate(sequence):`
            - list comprehension, good for doing repetitive things in a single line
                - `doubledlist = [ 2*val for val in sequence ]`
        - functions: `min(), max(), mean(), sorted(), tuple(), list()`
    - dictionaries, aka "mappings"
        - init with `{}` or `dict()`
        - add new key:value pairs with `d[key] = value`
            - what happens if key already exists?
        - various methods
        - iterating over dicts:
            - dict comprehension:
                - `doubleddict = { key:2*val for (key, val) in d.items() }`
            - dict vs. OrderedDict
                - NOTE: order of keys in dict is not preserved! dict is a key:val mapping, not a sequence of keys
                - OrderedDict is a hybrid of mapping and a sequence, preserves key order
                - `from collections import OrderedDict as odict`
    - combining tuples, lists, dicts, any combination is possible, can be nested
        - common ones:
            - list of tuples
            - dict of lists
    - memory, value vs reference, mutability
        - `a = [1, 2, 3]; b = a` vs `a = [1, 2, 3]; b = a.copy()`
        - `is` and `is not` operators check for identity instead of value
            - `a = 1`
            - `a == True` returns `True`, `a is True` returns `False`
