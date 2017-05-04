### organizing code, data, results

- code reuse
    - take a long script with repeating code patterns, replace with function
    - take a script with several functions, move those functions into their own modules,
      import them
    - "refactoring"
- DRY principle - don't repeat yourself
    - make variables out of numbers or strings that show up multiple times in your code,
    don't hard-code them every time
        - as a variable, defined once, it's easier to change it later
        - more abstract, but also more descriptive if you choose reasonable variable
        names: similar to difference between arithmetic and algebra
    - globals are usually defined at the top of the module, and CAPITALIZED, to make it
    clear they're global within that module
- multiple modules
    - naming convention: lowercase, no spaces, underscores if need-be
    - importing
    - circular imports
- if name == main
    - control behaviour of module when run as a script
    - difference between running a script and importing a module
- typical files to include for public projects, good habit for private ones too:
    - README(.md), TODO, LICENSE
- data and results:
    - folder naming schemes and hierarchies
        - consistent naming is important for programmatic analysis
        - datetime naming, _ separator, filenames without spaces
    - separating data from code
        - mount data as read-only for safety?
    - relative vs absolute paths
    - raw data vs intermediate data vs final results
    - making folders read-only to protect raw data?
    - where to store results/figures?
    - VC only works well for text, such as code, so you can see the diff
- backups!
    - `rsync`, or use Grsync for GUI and as a place to store backup commands

- exercises:
    - refactoring: take existing messy code, clean it up
        - replace repetitive code with a function

