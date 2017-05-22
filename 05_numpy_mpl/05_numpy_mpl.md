### more numpy 1D arrays, numpy file operations, plotting with matplotlib

#### more numpy 1D arrays

- `import numpy as np` to gain convenient access to numpy functions/modules/objects with `np.something`

- array methods
    - `a = np.random.random(10)` of random float values between 0 and 1
    - `a.max()`, `a.min()`, `a.ptp()`, `a.sum()`, `a.mean()`, `a.std()`
    - how can we shift all these values to have zero mean and a standard deviation of 1?
        - ```python
          a -= a.mean() # now mean is very close to 0
          a /= a.std() # now std is also very close to 0
          ````
        - note that e.g. `-3.3306690738754695e-17` is shorthand for `-3.33... x 10^-17`
        - what if you now want the sum of the values to be 1?
    - `a.sort()` - sorts in place! same as for a list
    - `a.tolist()` returns list equivalent of `a`, same as `list(a)` if `a` is 1D
    - many array methods have an equivalent numpy function, e.g. `np.max()`, `np.min()`, etc., which you can use directly on lists or tuples

- review integer dtypes:
    - what's a digit? numeric symbol used to represent numbers
    - "digiti": Latin for "fingers", decimal digits are numeric symbols for counting in base 10, values 0 to 9
    - what's a bit? bit = binary digit, bits are numeric symbols for counting in base 2, values 0 and 1
    - what's a byte? 8 bits: 00000000, 00000001, 00000010, 00000011 ... == 0, 1, 2, 3, ...
    - 8 bit integer takes up 1 byte of memory
    - 16 bit takes up 2 bytes
    - 32 bit takes up 4 bytes
    - 64 bit takes up 8 bytes
    - total number of values expressable by an int: `2**nbits`
    - max value for unsigned int: `2**nbits - 1`
    - min/max val for signed int: `-(2**nbits)/2, (2**nbits)/2 - 1`
        - or, use `np.iinfo()`
        - unless you absolutely need the extra double max value, it's usually safer to use signed integers, especially for subtraction
    - what's overflow? it's what happens when you
    - when converting between dtypes, numpy *warns* about overflow but doesn't stop execution:
        - what's the max value expressable by int8?
        - `np.int8(120) + np.int8(10)` warns
        - get numpy error settings using `np.geterr()`
        - set numpy error setting using e.g. `np.seterr(over='raise')` to "raise" an *error* on overflow, which stops execution of your code, more strict than a *warning*
            - `np.seterr()` returns old settings before setting new ones

- exercise: create a 1D array of length 1 million that's suitable for storing integer values ranging from -1000 to 1000, while using as little memory as possible
    - how many bytes of memory do you predict it will use?
    - check `a.nbytes` to see if you got it right
    - is it safe to add/subtract two such arrays to/from each other?

- deciding between lists and arrays:
    - use a list when:
        - have heterogenous data types you want to store together in a sequence
        - want to easily add and remove items to/from it
        - don't have to store a very large number of items, memory use isn't an issue
        - don't have to do vectorized operations on the sequence, e.g. adding two of them together
    - otherwise, use an array!

#### numpy file operations

- so far we've been using mostly made up values to fill arrays, generated in code
- in reality you have to load data from disk, and save results (and figures) back to disk
- loading/saving arrays from/to files:
- two broad types of files: **text** and **binary**
    - **text files** are familiar, easy to view in a plain text editor, just a bunch of printable characters
        - what's a printable char? basically any available on your keyboard, plus maybe some old ones from the early days when computers didn't have screens
        - these characters are stored by bytes in memory, and on disk
        - computers have to agree on which bytes represent which chars
            - encoding: mapping of byte values to characters
            - most common encoding is ASCII: American Standard Code for Information Interchange
            - ASCII uses 1 byte per character, but only uses the first 128 integer values (0 to 127) to represent various characters, plus outdated "characters" that controlled direct output to printers and communications with old modems
            - see `ASCII-Conversion-Chart.pdf`
            - a newer increasingly common one is UTF-8, an extension of ASCII that can encode many more characters from more languages
        - in a text file, if you want to save the number `100`, you need to save 3 characters to disk (one `1`, two `0`s), so this takes up 3 bytes of space.
        - what's the smallest integer data type that can represent `100`? How many bytes does it take up?
    - **binary files** are much more space efficient for storing numbers, and are therefore also faster, but require a "hex" editor
        - if you try and open a binary file using a plain text editor, it will either show you a bunch of garbled characters, or it will refuse to open it at all
        - binaries are harder to view and edit than a simple plain text file, but mostly you load/save them programmatically anyway
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
        - open-source hex editors:
            - windows: [HexEdit](http://www.catch22.net/software/hexedit)
            - mac: [Hex Fiend](http://ridiculousfish.com/hexfiend/)
            - linux: [ghex](https://github.com/GNOME/ghex), [bless](http://home.gna.org/bless/)

#### plotting with matplotlib (MPL)

- main plotting library for python, others exist, but often based on MPL
- typical usage: `import matplotlib.pyplot as plt`
    - now all the common plotting functions are available as `plt.something`

- line plots:
    - let's create a data array using `np.linspace()` to get a set of evenly spaced time points, and then `np.sin()` or `np.cos()` to create a nice sinusoid as a function of time
        ```python
        t = np.linspace(0, 4*np.pi, 100) # 100 evenly spaced timepoints
        s = np.sin(t) # calculate sine as a function of t
        plt.plot(t, s) # plot points in t on x-axis vs. points in s on y-axis
        ````
        - compare `np.linspace(start, stop, npoints)` with `np.arange(start, stop, step)`
            - `np.linspace()`
                - lets you specify the number of points you want to get out
                - is end-inclusive (`stop` value is included in the output)
            - `np.arange()`
                - lets you specify the step size between points
                - is end-exclusive (`stop` value is excluded in the output)
        - `np.logspace()` is the logarithmic equivalent of `np.linspace`, but creates requested number of points equally spaced on a logarithmic scale instead of linear scale

    - if no existing plot window ("figure") exists, a new one will pop up, or will be embedded in your jupyter notebook
    - figure toolbar:
        - pan tool:
            - left button drag: pan horizontally and vertically
            - right button drag: zoom horizontally and vertically
            - back and forward buttons skip between recent views
            - home button returns to default view
            - magnifying glass: zoom to rectangle
                - left button drag to zoom to rectangle
                - right button drag to zoom view out to fit rectangle
        - configure subplots: change borders, spacing between subplots (if any)
            - tight layout button minimizes borders and maximizes data, good for saving to file
        - edit plot params: titles, labels, limits, scales, line and marker formatting
        - save: save figure to disk, typically `.pdf` or `.png`
    - everything you can do interactively with the toolbar, you can also do programmatically in python code
    - add another line to the same plot:
        ```python
        c = np.cin(t) # calculate cosine as a function of the same timebase t
        plt.plot(t, c) # plot points in t on x-axis vs. points in c on y-axis
        ````
    - by default, MPL adds the new line plot to the existing one

- exercise:
    - create 1D array using `np.sin()` or `np.cos()`
    - plot it with `plt.plot()` to see what it looks like
    - give it some labels, save the plot to disk
    - save the array to a text file with `np.savetxt()`
    - examine the text file in your text editor, make sure it's saved the way you want
    - now save the same array to binary file using `np.save()`
    - compare the size of the text and binary file
    - exit ipython/jupyter, restart ipython/jupyter
    - load array twice: from the text file & form the binary file, save to two different names
    - plot both arrays, compare them to each other, compare to saved plot to make sure they look the same

- anatomy of a MPL figure
    - http://matplotlib.org/examples/showcase/anatomy.html
    - axes, markers, lines, labels, titles, legends, ticks, grids, spines
    - annotate, text, circle

- many different kinds of plots:

    - scatterplots
    - histograms
    - bar charts
    - 3d plots
