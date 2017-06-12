### data analysis with Pandas

- so far, we've seen a few different ways of storing data in Python
    - collections
        - sequences: tuples `()` and lists `[]`
        - mappings: dictionaries `{}`
        - numpy arrays: `np.array()` - best for handling large multidimensional datasets, fast, memory efficient, vectorized math, matrix math, lots of builtin analyses

- not all experimental data can fit seamlessly into a normal numpy array
    - indexing with integers isn't always ideal
        - sometimes it's nicer to use more meaningful labels, like strings, such as in a dictionary
    - missing data isn't necessarily handled automatically in numpy
    - different number of data points for different subjects/trials, which requires multiple arrays, each of different length
    - heterogenous data types that you want to keep together in the same data object
        - possible with `numpy.recarray()`, but not all that convenient
    - Pandas is a library built on top of numpy that deals with these annoyances, designed to make it easier to handle real-world data
    - quickly calculate and plot simple analyses
    - Pandas also has the ability to load/save data directly from/to text files, Excel files, as well as databases
    - why the name pandas? comes from "panel data", economics term?

- numpy has one basic object type: array, can be 1, 2, 3 or more dimensions
- pandas has two basic object types: Series & DataFrame, 1 and 2 dimensions respectively

- customary name for pandas import is `pd`: `import pandas as pd`

- `pd.Series`
    - like a 1D numpy array, but more flexible in that indices don't have to be integers
    - indices can be ints, floats, strings, others
    - e.g. time series data of fluorescence intensity of some ROI vs. time
        - with numpy, you'd need two arrays of the same length to properly describe this data: one for fluorescence, and another to store the corresponding timestamps of each measurement
        ```python
        fl = np.array(np.random.random(10))
        t = np.arange(0, 1, 0.1) # in seconds, say
        ````
        - a bit awkward: one data set represented by two separate arrays, with two different names
        - if you want to manipulate this data set, you have to remember to do the manipulation on both arrays, not just one of them!
        - e.g. trim the data down to just the first 5 data points:
            ```python
            trim_fl = fl[:5]
            trim_t = t[:5]
            ````
        - another annoyance: say you want to get fluorescence value at a specific timepoint, like t=0.2 seconds
        - 2 step process:
        ```python
        idx = t == 0.2 # find where t is 0.2, get a boolean array idx
        v = fl[idx] # use idx as index into fl, get a float array with one entry
        # or in one line:
        v = fl[t == 0.2] # also a float array with one entry
        v[0] # to get the actual float value out of it, tedious!
        ````
    - combine fluorescence data and timestamps into a single pandas data series:
    - `s = pd.Series(data=fl, index=t)`
    - now if you want to trim the Series, it's a single command:
    - `s.iloc[:5]` for the 1st 5 data points - `.iloc` stand for "integer location"

    - if indices are numeric, they need not be in numerical order
    - indices don't even have to be unique! but that's weird


- missing data:
    - say you have 2D data, and one data point is missing
    - if you simply leave it out, like this:
    ```python
    missd = [[1, 2, 3],
             [4, 6],
             [7, 8, 9]]
    ````
    - what kind of object is this? try `type(missd)`
    - what happens if you try to convert this list of variable length lists to an array?
        - `a = np.array(missd)`
        - not all the rows are the same length, converting to an array doesn't have any benefit
        - the hint that something is wrong is that `dtype=object` instead of say `dtype=int`
        - `a.shape` is `(3,)`, i.e. this is just a one dimensional list
        - `a.ndim` is `1`
        - `a[:, 0]` gives an IndexError
        - this is no different from a list of lists, i.e. can't index into columns, even though it looks almost like a 2D array
    - so, missing data can't simply be left out when creating numpy arrays
    - to represent missing data in numpy, can use a placeholder called `np.nan`
    - nan = "not a number"
    ```python
    nand = [[1, 2, 3],
            [4, np.nan, 6],
            [7, 8, 9]]
    ````
    - now converting to an array is useful again:
        - `a = np.array(nand)`
        - `a.shape` is `(3, 3)` and `a.ndim` is `2`
        - can index into columns: `a[:, 0]` works
        - but notice that the dtype isn't integer, it's float:
            - `a.dtype` gives `dtype('float64')`
            - this is because `np.nan` is itself a special float value
            - a single `np.nan` forces the whole array to become float, even though all the real values it was given were integers
    - pandas DataFrame deals better with missing data

- `pd.DataFrame`
    - looks and feels a lot like a spreadsheet
    - like a 2D numpy array, but both row and column indices can be non-integers
    - both row and column indices are more like labels, can be ints, floats, or strings
    - so flexible that labels don't even have to be unique! but that's weird
    - indexing and slicing columns and rows
        - `df.column_name` - can use tab completion to complete the column name
    - sorting by column
    - renaming columns
    - concatenating DataFrames:
        - very similar to `np.concatenate` in numpy, but called `pd.concat` instead
        - vertically (default): `pd.concat([df1, df2])`
        - horizontally: `pd.concat([df1, df2], axis=1)`

    - index with `df.loc` and `df.iloc`
        - don't use `df.ix`, an older deprecated way of indexing that can still be found in tutorials

- loading data from a .csv text file:
    - csv = comma separated values
    - each line of text is a row, commas separate the columns
    - in a pandas DataFrame, a row is called an "observation", each column a "variable"
    - `df = pd.read_csv('exp1.csv')`
    - pandas automatically parses the first row as a "header" and uses that to label each column

- built-in plotting!

- pd.date_range

- ragged arrays in pandas?

- loading and saving
    - excel and csv files
    - compare with loading csv files in numpy
- selecting columns and rows, getting values as np arrays
- ask questions of your data, answer them with...
- useful series and dataframe methods:
    - `.head()`, `.tail()`
    - `.min()`, `.max()`
    - `.mean()`, `.median()`, `.std()`
- `df.groupby()`
    - groupby object, various methods: mean(), std(), hist()
- `df.to_records()`

- see both pandas cheat sheets
