### more numpy 1D arrays, plotting with matplotlib


- array methods
    - `a.max()`, `a.min()`, `a.ptp()`, `a.sum()`, `a.mean()`, `a.std()`
    - `a.sort()` - sorts in place! same as for a list
    - `a.tolist()` returns list equivalent of `a`, same as `list(a)` if `a` is 1D
    - many have an equivalent numpy function, e.g. `np.max()`, `np.min()`, etc.

- dtypes:
    - what's a bit? bit = binary digit, takes two values, 0 or 1
    - what's a byte? 8 bits: 00000000, 00000001, 00000010, 00000011 ... == 0, 1, 2, 3, ...
    - 8 bit integer takes up 1 byte of memory
    - 16 bit takes up 2 bytes
    - 32 bit takes up 4 bytes
    - 64 bit takes up 8 bytes

- exercise: create a 1D array of length 1 million that's suitable for storing integer values ranging from -1000 to 1000, while using as little memory as possible
    - how many bytes of memory do you predict it will use? how many does it actually use?
    - is it safe to add/subtract two such arrays to/from each other?
    - unless you absolutely need the extra double max value, it's safer to use signed integers, in case of subtraction

- deciding between lists and arrays:
    - use a list when:
        - have heterogenous data types you want to store together in a sequence
        - want to easily add and remove items to/from it
        - don't have to store a very large number of items, memory use isn't an issue
        - don't have to do vectorized operations on the sequence, e.g. adding two of them together
    - otherwise, use an array!

- loading/saving arrays from/to files:
    - text vs. binary files?
        - text files are easier to view in a text editor
        - binary files require a "hex" editor, harder to view and edit, but are much more space efficient and faster
            - same amount of data can be stored using less disk space
        - which one to use depends on your application, how your data are saved
        - for large data sets, like images or electrophysiology, binary files are critical, text files aren't appropriate

- loading/saving text files
    - `np.loadtxt(fname)` - recommended way to load from a text file
        - use the `delimiter=','` kwarg to handle e.g. comma separated values, see `test.csv`
    - `np.savetxt(fname, a)` - recommended way to save to a text file
        - again, use the `delimiter=','` kwarg to create comma separated values
        - notice that dtype information can be lost using the above, `fmt=%g'` kwarg helps
        - saving to and loading from binary files is handles metadata better, covered later

- loading/saving binary files:
    - to see hex representation of bytes in memory for array `a` : `a.tobytes()`
    - `np.load()` - from a binary `.npy` file, or a `.zip` file containing multiple `.npy` files
    - `np.save()` - to a binary `.npy` file
    - `np.savez()` & `np.savez_compressed()` - save multiple arrays to an uncompressed or compressed `.zip` file
    - for loading/saving raw binary representation of array data from/to files, for use with other systems:
        - `np.fromfile()`
        - `a.tofile()`
    - inspect binary files with hex editor
        - hex = hexadecimal = base 16 representation of numbers, 0 to 9 plus 6 more: abcdef instead of just 0 to 9
        - hex editor is a good way to learn about different data types
            - same set of bytes on the disk/in memory can be interpreted in different ways
        - windows: [HexEdit](http://www.catch22.net/software/hexedit)
        - mac: [Hex Fiend](http://ridiculousfish.com/hexfiend/)
        - linux: ghex, bless


- create some moderately interesting arrays using `np.sin` or `np.cos`

- line plots
- scatterplots
- histograms
- bar charts?
- 3d plots?
- anatomy of a MPL figure
    - http://matplotlib.org/examples/showcase/anatomy.html
    - axes, markers, lines, labels, titles, legends, ticks, grids, spines
- subplots
- matplotlibrc for changing defaults
    - builtin styles?
    - matplotlib.style.available


- exercise:
    - create 1D array, plot it to see what it looks like, save the plot to disk, save the array to both a text file (using `np.savetxt()`) and a binary file (using `np.save()`) to disk, compare their file sizes. Now exit ipython, restart ipython, load array from the both the text file and the binary file, plot both arrays, compare them to each other, and to the saved plot to make sure they look the same
