### more matplotlib, numpy matrices and ndarrays

#### more matplotlib

- plotting issues:
    ```python
    import matplotlib.pyplot as plt
    plt.plot() # should pop up a figure window with axes
    ````
    - figures not popping up in **ipython**?
        - turn on interactive mode by calling `plt.ion()`
        - permanently enable interactive mode in matplotlib settings file:
            - linux: `~/.config/matplotlib/matplotlibrc`
            - mac + windows: `~/.matplotlib/matplotlibrc`
            - uncomment `#interactive: False` line and set to `True` instead
    - figures in **jupyter** not automatically displaying inline?
        - type `%matplotlib inline` in a cell, all cells that follow will do inline plots
        - make this setting permanent in `~/.ipython/ipython_config.py` file
        - uncomment `#c.InteractiveShellApp.matplotlib = None` line and set to `'inline'`
        - for interactive plotting in jupyter, type `%matplotlib notebook`
        - make this setting permanent with `c.InteractiveShellApp.matplotlib = 'notebook'` in `ipython_config.py` file
            - NOTE: this only works in more recent versions of matplotlib/jupyter?
            - quite a bit slower than interactive plots in ipython
    - missing toolbar?
        - set `toolbar : toolbar2` in `matplotlibrc` file
    - the button for "edit axes/curve/image params" in figure window might be missing

- MATLAB style vs. OOP style:
    - last week we learned the MATLAB "procedural" style of plotting:
    ```python
    import matplotlib.pyplot as plt
    t = np.linspace(0, 4*np.pi, 100) # 100 evenly spaced timepoints, 2 cycles
    s = np.sin(t) # calculate sine as a function of t
    c = np.cos(t) # calculate cosine as a function of t
    plt.plot(t, s) # plot points in t on x-axis vs. points in s on y-axis
    ````
    - MPL also has an alternative, more Pythonic, object-oriented (OOP) style, with very similar commands
    - first, you explicitly create a figure and an axes
    - `f, a = plt.subplots()` - by default creates a new figure with one set of x-y axes, and returns objects representing them
        - notice the `s` in `plt.subplots()`, `plt.subplot()` is a slightly different MATLAB-style procedural command
    - now, we can do most of our plot commands as methods of this particular axes `a`:
        - `a.plot(t, s)`
        - common formatting commands in OOP style:
            - `a.set_xlim()`, `a.set_ylim()`, `a.set_xlabel()`, `a.set_ylabel()`, `a.set_title()`
        - compare with MATLAB style:
            - `plt.xlim()`, `plt.ylim()`, `plt.xlabel()`, `plt.ylabel`, `plt.title()`
        - one more useful figure property worth formatting is `spines`, only easily accessible through the OOP interface:
            - `a.spines['top'].set_visible(False)`
            - `a.spines['right'].set_visible(False)`
        - OOP style is slightly more wordy, but much more explicit, gives better control over multiple figures
    - with multiple figures and axes open, we can refer to them directly by name, no longer have to worry about which is the "current" figure:
    - `f2, a2 = plt.subplots()`
    - `a2.hist(s)` - do a histogram this time
    - to clear a particular axes: `a2.clear()`

- subplots: create multiple axes in a single figure
    - `f, axs = plt.subplots(nrows=2, ncols=2)`
    - `axs` is now a 2D array, you choose your axes by indexing into it with row and col indicies:
        - `axs[0, 1].plot(t, s) # plot s vs. t in axes in 1st row 2nd column`
        - `axs[1, 0].plot(t, c, color='r') # plot c vs. t in red in axes in 2nd row 1st column`
    - optional kwargs `sharex`, `sharey`
        ```python
        plt.close('all')
        f1, a1 = plt.subplots(2, 1, sharex=True, sharey=False) # a1 is 1D array
        a1[0].plot(t, s) # plot s vs. t
        a1[1].plot(t, c, color='r') # plot c vs. t in red, shared x axis as above
        f2, a2 = plt.subplots(2, 1, sharex=True, sharey=False) # a2 is 1D array
        a2[0].hist(s) # plot hist of s
        a2[1].hist(c, color='r') # plot hist of c in red, shared x axis as above
        ````
    - change the name of a figure, i.e. its titlebar and its default filename in the save dialog box:
        ```python
        f1.canvas.set_window_title('time series')
        f2.canvas.set_window_title('histograms')
        ````
- some other kinds of plots:
    - scatterplots:
        - `a.scatter(x, y)` - very similar to `a.plot()`
            - allows each point to be formatted differently (colour, marker, size)
            - defaults to not drawing a line between points
    - errorbar plot
        - `a.errorbar(x, y, yerr=5, xerr=2)` - again similar to `a.plot()`, but with errorbars
    - bar charts
        - `a.bar(left, height)` - vertical bars, left and height are sequences
        - `a.bar(bottom, width)` - horizontal bars

#### matrices, ndarrays, ndimage

- so far, we've dealt with only 1D arrays, a.k.a vectors
- numpy allows for N dimensional arrays, but most common are 2D arrays, a.k.a matrices
- matrix is like an image: each entry has a (pixel) value stored at a row and column index
- plotting matrices as images is a great way to visualize them

- initializing a 2D array
    - explicitly, using a list of lists, or a tuple of tuples, convert to array:
    - `a = np.array([[1, 2, 3], [4, 5, 6]])` or `a = np.array(((1, 2, 3), (4, 5, 6)))``
    - `a = np.arange(10).reshape((5, 2))`
        - creates a 1D array, but then reshapes it to 2D
        - 2D array shape tuples are always `(nrows, ncolums)`
        - nrows x ncols of the reshaped array have to equal the number of elements in the 1D array
        - what happens if you do `a = np.arange(10).reshape((6, 2))`
        - can also change the shape of an existing array by assigning to `a.shape = 6, 2`
    - `a = np.zeros((5, 2))`
    - `a = np.ones((5, 2))`
    - `a = np.random.random((5, 2))`
    - `a = np.tile([1, 2], 5)`
    - `a.fill(7)` fills the array with the number 7, but maintains its shape
    - array methods often operate on the array in-place, while numpy functions often return a new array, but there are lots of exceptions

- `np.eye(5)` - create 5x5 identity matrix

- to get number of rows: `a.shape[0]`
- to get number of columns: `a.shape[1]`
    - for 1D arrays, `len()` gave number of elements in the array
    - for 2D arrays, `len()` gives is a shortcut for `a.shape[0]`, i.e. number of *rows* in `a`
- to convert 2D array down to a 1D array, flatten it using `a.ravel()`
    - `np.arange(10).reshape((5, 2)).ravel()` gives the same as `np.arange(10)`
- `a.size` gives the total number of elements in `a`, across all dimensions
    - same as flattening the array and asking for the length of the result: `len(a.ravel())`

- multidimensional indexing, slicing, axis arg
    - `-1`, `:`, `...`, `::2`, `::-1`
    - `a.reshape()`, or assign to `a.shape`
    - `scipy.ndimage`
        - loading different image types
        - `plt.imshow` to display matrices and images
        - increase contrast of an image
            - `np.percentile`
            - denoising/smoothing
                - convolution, say box filter
        - array/image rotation, flipping (lots of different ways, indexing, np.flip, skimage, multiply by transformation matrix), rescaling:
        - thresholding, masking an image
    - choose colormaps in `matplotlib.cm`

- array broadcasting

- various array methods and numpy functions:
    - `a.reshape()`, `a.ravel()`
    - `a.transpose()` or its shortcut property: `a.T`
    - `np.diff()`
    - `np.searchsorted()` & `a.searchsorted()`
    - `np.sort` & `a.sort()`, `np.argsort()` & `a.argsort()`
    - `np.random.shuffle`
    - `np.corrcoeff()`, `np.cov()`

- 2D array layout in memory, C-order vs F-order
    - use `timeit` to show difference in mean along columns vs rows of square array

- introduce 3D and higher dim arrays
    - movie is easy 3D array to understand

- when to use numpy or not
    - compare to for loops, list comprehensions
    - use `timeit` to compare them, maybe also builtin `sum()` on list vs numpy `a.sum()`
    - what's happening under the hood?
        - multiple python ops vs single python op w/ multiple C ops
    - don't worry too much about optimizing for speed until it becomes an issue

- ragged arrays vs full arrays:
    - ragged: when e.g. each row has a different number of columns
        - each row is an experimental session, each session has a different number of trials
        - if you don't have too many sessions, use a sequence as the outer container, and make each entry a 1D array to efficiently hold trial data for each session
            - so, a tuple or list or dict, indexed by session name or number, whose contents is a 1D array of trial data:
            - ```python
                 s = {}
                 for sessioni in range(nsessions):
                    trialdata = np.asarray(gettrialdata(sessioni))
                    s.append(trialdata)
              ````
        - alternative: if you have a **lot** of rows, and you want to store everything in a single array, and you know the maximum number of columns for a given row ahead of time, declare your array to have as many columns as your longest row, pad shorter rows with some placeholder, like np.nan if it's a float, or some special integer if it's an int array, like -1, or `np.iinfo(a).min` or `np.iinfo(a).max` or `np.iinfo(dtype).min`

- higher dim arrays
    - rows, columns, hypercolumns


- np.stack, np.hstack, np.vstack

- record arrays?
    - a numpy array with a custom dtype made of basic dtypes
- object arrays?
