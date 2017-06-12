### data analysis with Pandas

- not all experimental data can fit seamlessly into a normal numpy array
    - missing data
    - different number of data points for different subjects/trials
    - heterogenous data types
    - lots of other little annoyances when it comes to doing analysis on real-world data
    - Pandas is a library built on top of numpy that deals with these annoyances, designed to make it easier to store data
    - Pandas also has the ability to load/save data directly from/to Excel files, as well as databases
    - why the name pandas?

- numpy has one basic object type: array, can be 1, 2, 3 or more dimensions
- pandas has two basic object types: Series & DataFrame, 1 and 2 dimensions respectively

- customary name for pandas import is `pd`: `import pandas as pd`

- Series: like a 1D numpy array, but with indices don't have to be integers
    - indices can be floats, strings
    - if indices are numeric, they need not be in numerical order
    - e.g. time series data of fluorescence intensity vs. time
        - with numpy, you'd need two arrays of the same length to properly describe this data: one for fluorescence, and another to store the corresponding timestamps of each measurement
        ```python
        fl = np.array(np.random.random(10))
        t = np.arange(0, 1, 0.1) # in seconds, say
        ````
        - a little bit awkward: one data set represented by two separate arrays, with two different names
        - if you want to manipulate this data set, you have to remember to do the manipulation on both arrays, not just one of them!
        - e.g. trim the data down to just the first 5 data points:
            ```python
            fl = fl[:5]
            t = t[:5]
            ````
    - `s = pd.Series(data=fl, index=t)`

- missing data:
    - say you have 2D data, and one data point is missing
    - if you simply leave it out, like this:
    ```python
    data = [[1, 2, 3],
            [4, 6],
            [7, 8, 9]]
    ````
    - what kind of object is this?
    - what happens if you try to convert this list of variable length lists to an array?
        - `a = np.array(data)`
        - because not all the rows are the same length, converting to an array doesn't have any benefit
        - the hint is that something is wrong is that `dtype=object`
        - `a.shape` is `(3,)`, i.e. this is just a one dimensional list
        - `a.ndim` is `1`
        - this is no different from a list of lists, i.e. can't index into columns, even though it looks almost like a 2D array
        - `a[:, 0]` gives an IndexError
    - so, missing data can't simply be left out when loading numpy arrays
    - to represent missing data in numpy, can use a placeholder called `np.nan`
    - nan = "not a number"

- DataFrame: like a 2D numpy array, but both row and column indices can be non-integers
    - both row and column indices are more like labels, can be ints, floats, or strings
    - so flexible that labels don't even have to be unique! but that's weird
    - looks and feels a lot like a spreadsheet
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
    - `.mean()`, `.median()`, `df.std()`
- `df.groupby()`
    - groupby object, various methods: mean(), std(), hist()
- `df.to_records()`

- see both pandas cheat sheets
