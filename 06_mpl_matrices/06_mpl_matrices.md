### more matplotlib, numpy matrices and ndarrays

#### more matplotlib

- create a new empty figure with `plt.figure()`

- subplots: multiple axes in a single figure
    - `plt.subplot()`

- many different kinds of plots:
    - scatterplots
    - histograms
    - bar charts
    - 3d plots

- `.matplotlibrc` file for changing defaults
    - builtin styles?
    - matplotlib.style.available

#### matrices and ndarrays

- multidimensional arrays, indexing, slicing, axis arg
    - rows vs. columns vs. hypercolumns
    - `-1`, `:`, `...`, `::2`, `::-1`
    - `a.reshape()`, or assign to `a.shape`
    - another useful array property: `a.size` - total number of elements in array, across all dimensions
        - same as flattening the array and asking for the length of the result
        - `len(a.ravel())`
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

- np.stack, np.hstack, np.vstack

- record arrays?
    - a numpy array with a custom dtype made of basic dtypes
- object arrays?
