### plotting with matplotlib

- review numpy 1D arrays:


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

- loading and saving binary files:
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

- exercise:
    - create 1D array, plot it to see what it looks like, save the plot to disk, save the array to both a text file (using `np.savetxt()`) and a binary file (using `np.save()`) to disk, compare their file sizes. Now exit ipython, restart ipython, load array from the both the text file and the binary file, plot both arrays, compare them to each other, and to the saved plot to make sure they look the same
