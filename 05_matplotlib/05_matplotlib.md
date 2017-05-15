### plotting with matplotlib

- review numpy 1D arrays:


- loading and saving binary files:
    - `np.load()` - from a binary `.npy` file, or a `.zip` file containing multiple `.npy` files
    - `np.save()` - to a binary `.npy` file
    - `np.savez()` & `np.savez_compressed()` - save multiple arrays to an uncompressed or compressed `.zip` file
    - for loading/saving raw binary representation of array data from/to files, for use with other systems:
        - `np.fromfile()`
        - `a.tofile()`



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
