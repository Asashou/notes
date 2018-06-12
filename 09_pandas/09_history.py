mspacek@Godel:~/SciPyCourse2018/notes/08_images$ cd ../09_pandas/
mspacek@Godel:~/SciPyCourse2018/notes/09_pandas$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pandas as pd

In [2]: fl = np.random.random(20)

In [3]: t = np.arange(0, 400, 20)

In [4]: fl
Out[4]:
array([0.0557962 , 0.19412326, 0.12507681, 0.79687463, 0.8320148 ,
       0.54804825, 0.90550127, 0.92827888, 0.09549871, 0.31605641,
       0.11960358, 0.89042223, 0.33928041, 0.30200408, 0.21936923,
       0.23765269, 0.7613507 , 0.23597446, 0.09160979, 0.19303976])

In [5]: t
Out[5]:
array([  0,  20,  40,  60,  80, 100, 120, 140, 160, 180, 200, 220, 240,
       260, 280, 300, 320, 340, 360, 380])

In [6]: fl[:5]
Out[6]: array([0.0557962 , 0.19412326, 0.12507681, 0.79687463, 0.8320148 ])

In [7]: t[:5]
Out[7]: array([ 0, 20, 40, 60, 80])

In [8]: fl[t == 60]
Out[8]: array([0.79687463])

In [9]: t == 60
Out[9]:
array([False, False, False,  True, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False])

In [10]: fl[t == 60]
Out[10]: array([0.79687463])

In [11]: fl[t == 60][0]
Out[11]: 0.7968746312612851

In [12]: s = pd.Series(data=fl, index=t)

In [13]: s
Out[13]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [14]: len(s)
Out[14]: 20

In [15]: s.iloc[4]
Out[15]: 0.8320147965846488

In [16]: s.iloc[:5]
Out[16]:
0     0.055796
20    0.194123
40    0.125077
60    0.796875
80    0.832015
dtype: float64

In [17]: s
Out[17]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [18]: s.head()
Out[18]:
0     0.055796
20    0.194123
40    0.125077
60    0.796875
80    0.832015
dtype: float64

In [19]: s.tail()
Out[19]:
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [20]: s.head(3)
Out[20]:
0     0.055796
20    0.194123
40    0.125077
dtype: float64

In [21]: s.tail(3)
Out[21]:
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [22]: s.iloc[3:7]
Out[22]:
60     0.796875
80     0.832015
100    0.548048
120    0.905501
dtype: float64

In [23]: s.iloc[7]
Out[23]: 0.92827888051704

In [24]: s
Out[24]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [25]: s.iloc[7]
Out[25]: 0.92827888051704

In [26]: s.iloc[3:7]
Out[26]:
60     0.796875
80     0.832015
100    0.548048
120    0.905501
dtype: float64

In [27]: s.loc[60]
Out[27]: 0.7968746312612851

In [28]: s
Out[28]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [29]: s.loc[60]
Out[29]: 0.7968746312612851

In [30]: s.loc[:60]
Out[30]:
0     0.055796
20    0.194123
40    0.125077
60    0.796875
dtype: float64

In [31]: s.loc[30:70]
Out[31]:
40    0.125077
60    0.796875
dtype: float64

In [32]: s.loc[60]
Out[32]: 0.7968746312612851

In [33]: s.loc[30:70]
Out[33]:
40    0.125077
60    0.796875
dtype: float64

In [34]: s.loc[30:70].values
Out[34]: array([0.12507681, 0.79687463])

In [35]: s.sort_values?

In [36]: s.sort_values()
Out[36]:
0      0.055796
360    0.091610
160    0.095499
200    0.119604
40     0.125077
380    0.193040
20     0.194123
280    0.219369
340    0.235974
300    0.237653
260    0.302004
180    0.316056
240    0.339280
100    0.548048
320    0.761351
60     0.796875
80     0.832015
220    0.890422
120    0.905501
140    0.928279
dtype: float64

In [37]: s.sort_index()
Out[37]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [38]: s
Out[38]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [39]: s.iloc
Out[39]: <pandas.core.indexing._iLocIndexer at 0x7fd6f8f34598>

In [40]: s.loc
Out[40]: <pandas.core.indexing._LocIndexer at 0x7fd6f9ac3f98>

In [41]: s[60]
Out[41]: 0.7968746312612851

In [42]: s.loc[60]
Out[42]: 0.7968746312612851

In [43]: s.loc[30:70]
Out[43]:
40    0.125077
60    0.796875
dtype: float64

In [44]: s[30:70]
Out[44]: Series([], dtype: float64)

In [45]: s.iloc[30:70]
Out[45]: Series([], dtype: float64)

In [46]: s.iloc[5:10]
Out[46]:
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
dtype: float64

In [47]: s[5:10]
Out[47]:
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
dtype: float64

In [48]: s.loc[30:70]
Out[48]:
40    0.125077
60    0.796875
dtype: float64

In [49]: s[30:70]
Out[49]: Series([], dtype: float64)

In [50]: s.loc
Out[50]: <pandas.core.indexing._LocIndexer at 0x7fd70e338138>

In [51]: s.iloc
Out[51]: <pandas.core.indexing._iLocIndexer at 0x7fd6f8f52ea8>

In [52]: s[60]
Out[52]: 0.7968746312612851

In [53]: s
Out[53]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [54]: tfloat = np.arange(0, 2, 0.1)

In [55]: tfloat
Out[55]:
array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2,
       1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])

In [56]: sfloat = pd.Series(data=fl, index=tfloat)

In [57]: sfloat
Out[57]:
0.0    0.055796
0.1    0.194123
0.2    0.125077
0.3    0.796875
0.4    0.832015
0.5    0.548048
0.6    0.905501
0.7    0.928279
0.8    0.095499
0.9    0.316056
1.0    0.119604
1.1    0.890422
1.2    0.339280
1.3    0.302004
1.4    0.219369
1.5    0.237653
1.6    0.761351
1.7    0.235974
1.8    0.091610
1.9    0.193040
dtype: float64

In [58]: s.loc[0.0]
Out[58]: 0.055796203580043446

In [59]: s.loc[0.1]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-59-80009a55734b> in <module>()
----> 1 s.loc[0.1]

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in __getitem__(self, key)
   1476
   1477             maybe_callable = com._apply_if_callable(key, self.obj)
-> 1478             return self._getitem_axis(maybe_callable, axis=axis)
   1479
   1480     def _is_scalar_access(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _getitem_axis(self, key, axis)
   1909
   1910         # fall thru to straight lookup
-> 1911         self._validate_key(key, axis)
   1912         return self._get_label(key, axis=axis)
   1913

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
   1786
   1787             try:
-> 1788                 key = self._convert_scalar_indexer(key, axis)
   1789                 if not ax.contains(key):
   1790                     error()

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _convert_scalar_indexer(self, key, axis)
    259         ax = self.obj._get_axis(min(axis, self.ndim - 1))
    260         # a scalar
--> 261         return ax._convert_scalar_indexer(key, kind=self.name)
    262
    263     def _convert_slice_indexer(self, key, axis):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/numeric.py in _convert_scalar_indexer(self, key, kind)
    185             key = self._maybe_cast_indexer(key)
    186         return (super(Int64Index, self)
--> 187                 ._convert_scalar_indexer(key, kind=kind))
    188
    189     def _wrap_joined_index(self, joined, other):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _convert_scalar_indexer(self, key, kind)
   1658                                               'unicode',
   1659                                               'mixed']:
-> 1660                     return self._invalid_indexer('label', key)
   1661
   1662             elif kind in ['loc'] and is_integer(key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _invalid_indexer(self, form, key)
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

TypeError: cannot do label indexing on <class 'pandas.core.indexes.numeric.Int64Index'> with these indexers [0.1] of <class 'float'>
> /usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py(1848)_invalid_indexer()
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

ipdb> c

In [60]: s.loc[0.2]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-60-3bc1108fa41e> in <module>()
----> 1 s.loc[0.2]

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in __getitem__(self, key)
   1476
   1477             maybe_callable = com._apply_if_callable(key, self.obj)
-> 1478             return self._getitem_axis(maybe_callable, axis=axis)
   1479
   1480     def _is_scalar_access(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _getitem_axis(self, key, axis)
   1909
   1910         # fall thru to straight lookup
-> 1911         self._validate_key(key, axis)
   1912         return self._get_label(key, axis=axis)
   1913

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
   1786
   1787             try:
-> 1788                 key = self._convert_scalar_indexer(key, axis)
   1789                 if not ax.contains(key):
   1790                     error()

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _convert_scalar_indexer(self, key, axis)
    259         ax = self.obj._get_axis(min(axis, self.ndim - 1))
    260         # a scalar
--> 261         return ax._convert_scalar_indexer(key, kind=self.name)
    262
    263     def _convert_slice_indexer(self, key, axis):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/numeric.py in _convert_scalar_indexer(self, key, kind)
    185             key = self._maybe_cast_indexer(key)
    186         return (super(Int64Index, self)
--> 187                 ._convert_scalar_indexer(key, kind=kind))
    188
    189     def _wrap_joined_index(self, joined, other):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _convert_scalar_indexer(self, key, kind)
   1658                                               'unicode',
   1659                                               'mixed']:
-> 1660                     return self._invalid_indexer('label', key)
   1661
   1662             elif kind in ['loc'] and is_integer(key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _invalid_indexer(self, form, key)
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

TypeError: cannot do label indexing on <class 'pandas.core.indexes.numeric.Int64Index'> with these indexers [0.2] of <class 'float'>
> /usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py(1848)_invalid_indexer()
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

ipdb> c

In [61]: s.loc[0.2]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-61-3bc1108fa41e> in <module>()
----> 1 s.loc[0.2]

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in __getitem__(self, key)
   1476
   1477             maybe_callable = com._apply_if_callable(key, self.obj)
-> 1478             return self._getitem_axis(maybe_callable, axis=axis)
   1479
   1480     def _is_scalar_access(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _getitem_axis(self, key, axis)
   1909
   1910         # fall thru to straight lookup
-> 1911         self._validate_key(key, axis)
   1912         return self._get_label(key, axis=axis)
   1913

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
   1786
   1787             try:
-> 1788                 key = self._convert_scalar_indexer(key, axis)
   1789                 if not ax.contains(key):
   1790                     error()

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _convert_scalar_indexer(self, key, axis)
    259         ax = self.obj._get_axis(min(axis, self.ndim - 1))
    260         # a scalar
--> 261         return ax._convert_scalar_indexer(key, kind=self.name)
    262
    263     def _convert_slice_indexer(self, key, axis):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/numeric.py in _convert_scalar_indexer(self, key, kind)
    185             key = self._maybe_cast_indexer(key)
    186         return (super(Int64Index, self)
--> 187                 ._convert_scalar_indexer(key, kind=kind))
    188
    189     def _wrap_joined_index(self, joined, other):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _convert_scalar_indexer(self, key, kind)
   1658                                               'unicode',
   1659                                               'mixed']:
-> 1660                     return self._invalid_indexer('label', key)
   1661
   1662             elif kind in ['loc'] and is_integer(key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _invalid_indexer(self, form, key)
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

TypeError: cannot do label indexing on <class 'pandas.core.indexes.numeric.Int64Index'> with these indexers [0.2] of <class 'float'>
> /usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py(1848)_invalid_indexer()
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

ipdb> c

In [62]: s.loc[0.3]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-62-4ce8b1031696> in <module>()
----> 1 s.loc[0.3]

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in __getitem__(self, key)
   1476
   1477             maybe_callable = com._apply_if_callable(key, self.obj)
-> 1478             return self._getitem_axis(maybe_callable, axis=axis)
   1479
   1480     def _is_scalar_access(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _getitem_axis(self, key, axis)
   1909
   1910         # fall thru to straight lookup
-> 1911         self._validate_key(key, axis)
   1912         return self._get_label(key, axis=axis)
   1913

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
   1786
   1787             try:
-> 1788                 key = self._convert_scalar_indexer(key, axis)
   1789                 if not ax.contains(key):
   1790                     error()

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _convert_scalar_indexer(self, key, axis)
    259         ax = self.obj._get_axis(min(axis, self.ndim - 1))
    260         # a scalar
--> 261         return ax._convert_scalar_indexer(key, kind=self.name)
    262
    263     def _convert_slice_indexer(self, key, axis):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/numeric.py in _convert_scalar_indexer(self, key, kind)
    185             key = self._maybe_cast_indexer(key)
    186         return (super(Int64Index, self)
--> 187                 ._convert_scalar_indexer(key, kind=kind))
    188
    189     def _wrap_joined_index(self, joined, other):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _convert_scalar_indexer(self, key, kind)
   1658                                               'unicode',
   1659                                               'mixed']:
-> 1660                     return self._invalid_indexer('label', key)
   1661
   1662             elif kind in ['loc'] and is_integer(key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _invalid_indexer(self, form, key)
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

TypeError: cannot do label indexing on <class 'pandas.core.indexes.numeric.Int64Index'> with these indexers [0.3] of <class 'float'>
> /usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py(1848)_invalid_indexer()
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

ipdb> c

In [63]: s.loc[0.4]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-63-80a56cb3732b> in <module>()
----> 1 s.loc[0.4]

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in __getitem__(self, key)
   1476
   1477             maybe_callable = com._apply_if_callable(key, self.obj)
-> 1478             return self._getitem_axis(maybe_callable, axis=axis)
   1479
   1480     def _is_scalar_access(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _getitem_axis(self, key, axis)
   1909
   1910         # fall thru to straight lookup
-> 1911         self._validate_key(key, axis)
   1912         return self._get_label(key, axis=axis)
   1913

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
   1786
   1787             try:
-> 1788                 key = self._convert_scalar_indexer(key, axis)
   1789                 if not ax.contains(key):
   1790                     error()

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _convert_scalar_indexer(self, key, axis)
    259         ax = self.obj._get_axis(min(axis, self.ndim - 1))
    260         # a scalar
--> 261         return ax._convert_scalar_indexer(key, kind=self.name)
    262
    263     def _convert_slice_indexer(self, key, axis):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/numeric.py in _convert_scalar_indexer(self, key, kind)
    185             key = self._maybe_cast_indexer(key)
    186         return (super(Int64Index, self)
--> 187                 ._convert_scalar_indexer(key, kind=kind))
    188
    189     def _wrap_joined_index(self, joined, other):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _convert_scalar_indexer(self, key, kind)
   1658                                               'unicode',
   1659                                               'mixed']:
-> 1660                     return self._invalid_indexer('label', key)
   1661
   1662             elif kind in ['loc'] and is_integer(key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in _invalid_indexer(self, form, key)
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

TypeError: cannot do label indexing on <class 'pandas.core.indexes.numeric.Int64Index'> with these indexers [0.4] of <class 'float'>
> /usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py(1848)_invalid_indexer()
   1846                         "indexers [{key}] of {kind}".format(
   1847                             form=form, klass=type(self), key=key,
-> 1848                             kind=type(key)))
   1849
   1850     def get_duplicates(self):

ipdb> c

In [64]: s
Out[64]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [65]: sfloat.loc[0.0]
Out[65]: 0.055796203580043446

In [66]: sfloat.loc[0.1]
Out[66]: 0.19412325524898488

In [67]: sfloat.loc[0.2]
Out[67]: 0.12507681436164864

In [68]: sfloat.loc[0.]
Out[68]: 0.055796203580043446

In [69]: sfloat.loc[0.3]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
   1789                 if not ax.contains(key):
-> 1790                     error()
   1791             except TypeError as e:

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in error()
   1784                                .format(key=key,
-> 1785                                        axis=self.obj._get_axis_name(axis)))
   1786

KeyError: 'the label [0.3] is not in the [index]'

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-69-54a69c1be8be> in <module>()
----> 1 sfloat.loc[0.3]

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in __getitem__(self, key)
   1476
   1477             maybe_callable = com._apply_if_callable(key, self.obj)
-> 1478             return self._getitem_axis(maybe_callable, axis=axis)
   1479
   1480     def _is_scalar_access(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _getitem_axis(self, key, axis)
   1909
   1910         # fall thru to straight lookup
-> 1911         self._validate_key(key, axis)
   1912         return self._get_label(key, axis=axis)
   1913

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
   1796                 raise
   1797             except:
-> 1798                 error()
   1799
   1800     def _is_scalar_access(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in error()
   1783                 raise KeyError(u"the label [{key}] is not in the [{axis}]"
   1784                                .format(key=key,
-> 1785                                        axis=self.obj._get_axis_name(axis)))
   1786
   1787             try:

KeyError: 'the label [0.3] is not in the [index]'
> /usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py(1785)error()
   1783                 raise KeyError(u"the label [{key}] is not in the [{axis}]"
   1784                                .format(key=key,
-> 1785                                        axis=self.obj._get_axis_name(axis)))
   1786
   1787             try:

ipdb> c

In [70]: sfloat
Out[70]:
0.0    0.055796
0.1    0.194123
0.2    0.125077
0.3    0.796875
0.4    0.832015
0.5    0.548048
0.6    0.905501
0.7    0.928279
0.8    0.095499
0.9    0.316056
1.0    0.119604
1.1    0.890422
1.2    0.339280
1.3    0.302004
1.4    0.219369
1.5    0.237653
1.6    0.761351
1.7    0.235974
1.8    0.091610
1.9    0.193040
dtype: float64

In [71]: sfloat.loc[0.3]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
   1789                 if not ax.contains(key):
-> 1790                     error()
   1791             except TypeError as e:

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in error()
   1784                                .format(key=key,
-> 1785                                        axis=self.obj._get_axis_name(axis)))
   1786

KeyError: 'the label [0.3] is not in the [index]'

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-71-54a69c1be8be> in <module>()
----> 1 sfloat.loc[0.3]

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in __getitem__(self, key)
   1476
   1477             maybe_callable = com._apply_if_callable(key, self.obj)
-> 1478             return self._getitem_axis(maybe_callable, axis=axis)
   1479
   1480     def _is_scalar_access(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _getitem_axis(self, key, axis)
   1909
   1910         # fall thru to straight lookup
-> 1911         self._validate_key(key, axis)
   1912         return self._get_label(key, axis=axis)
   1913

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in _validate_key(self, key, axis)
   1796                 raise
   1797             except:
-> 1798                 error()
   1799
   1800     def _is_scalar_access(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py in error()
   1783                 raise KeyError(u"the label [{key}] is not in the [{axis}]"
   1784                                .format(key=key,
-> 1785                                        axis=self.obj._get_axis_name(axis)))
   1786
   1787             try:

KeyError: 'the label [0.3] is not in the [index]'
> /usr/local/lib/python3.5/dist-packages/pandas/core/indexing.py(1785)error()
   1783                 raise KeyError(u"the label [{key}] is not in the [{axis}]"
   1784                                .format(key=key,
-> 1785                                        axis=self.obj._get_axis_name(axis)))
   1786
   1787             try:

ipdb> c

In [72]: sfloat
Out[72]:
0.0    0.055796
0.1    0.194123
0.2    0.125077
0.3    0.796875
0.4    0.832015
0.5    0.548048
0.6    0.905501
0.7    0.928279
0.8    0.095499
0.9    0.316056
1.0    0.119604
1.1    0.890422
1.2    0.339280
1.3    0.302004
1.4    0.219369
1.5    0.237653
1.6    0.761351
1.7    0.235974
1.8    0.091610
1.9    0.193040
dtype: float64

In [73]: sfloat.index
Out[73]:
Float64Index([                0.0,                 0.1,                 0.2,
              0.30000000000000004,                 0.4,                 0.5,
               0.6000000000000001,  0.7000000000000001,                 0.8,
                              0.9,                 1.0,                 1.1,
               1.2000000000000002,                 1.3,  1.4000000000000001,
                              1.5,                 1.6,  1.7000000000000002,
                              1.8,  1.9000000000000001],
             dtype='float64')

In [74]: sfloat[0.3]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   3062             try:
-> 3063                 return self._engine.get_loc(key)
   3064             except KeyError:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

KeyError: 0.3

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-74-feb3d725fcf0> in <module>()
----> 1 sfloat[0.3]

/usr/local/lib/python3.5/dist-packages/pandas/core/series.py in __getitem__(self, key)
    764         key = com._apply_if_callable(key, self)
    765         try:
--> 766             result = self.index.get_value(self, key)
    767
    768             if not is_scalar(result):

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/numeric.py in get_value(self, series, key)
    356
    357         k = com._values_from_object(key)
--> 358         loc = self.get_loc(k)
    359         new_values = com._values_from_object(series)[loc]
    360

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/numeric.py in get_loc(self, key, method, tolerance)
    417             pass
    418         return super(Float64Index, self).get_loc(key, method=method,
--> 419                                                  tolerance=tolerance)
    420
    421     @cache_readonly

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   3063                 return self._engine.get_loc(key)
   3064             except KeyError:
-> 3065                 return self._engine.get_loc(self._maybe_cast_indexer(key))
   3066
   3067         indexer = self.get_indexer([key], method=method, tolerance=tolerance)

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Float64HashTable.get_item()

KeyError: 0.3
> /home/mspacek/SciPyCourse2018/notes/09_pandas/pandas/_libs/hashtable_class_helper.pxi(385)pandas._libs.hashtable.Float64HashTable.get_item()

ipdb> c

In [75]: sfloat.index
Out[75]:
Float64Index([                0.0,                 0.1,                 0.2,
              0.30000000000000004,                 0.4,                 0.5,
               0.6000000000000001,  0.7000000000000001,                 0.8,
                              0.9,                 1.0,                 1.1,
               1.2000000000000002,                 1.3,  1.4000000000000001,
                              1.5,                 1.6,  1.7000000000000002,
                              1.8,  1.9000000000000001],
             dtype='float64')

In [76]: sfloat
Out[76]:
0.0    0.055796
0.1    0.194123
0.2    0.125077
0.3    0.796875
0.4    0.832015
0.5    0.548048
0.6    0.905501
0.7    0.928279
0.8    0.095499
0.9    0.316056
1.0    0.119604
1.1    0.890422
1.2    0.339280
1.3    0.302004
1.4    0.219369
1.5    0.237653
1.6    0.761351
1.7    0.235974
1.8    0.091610
1.9    0.193040
dtype: float64

In [77]: s - 5
Out[77]:
0     -4.944204
20    -4.805877
40    -4.874923
60    -4.203125
80    -4.167985
100   -4.451952
120   -4.094499
140   -4.071721
160   -4.904501
180   -4.683944
200   -4.880396
220   -4.109578
240   -4.660720
260   -4.697996
280   -4.780631
300   -4.762347
320   -4.238649
340   -4.764026
360   -4.908390
380   -4.806960
dtype: float64

In [78]: s + 2
Out[78]:
0      2.055796
20     2.194123
40     2.125077
60     2.796875
80     2.832015
100    2.548048
120    2.905501
140    2.928279
160    2.095499
180    2.316056
200    2.119604
220    2.890422
240    2.339280
260    2.302004
280    2.219369
300    2.237653
320    2.761351
340    2.235974
360    2.091610
380    2.193040
dtype: float64

In [79]: s < 0.5
Out[79]:
0       True
20      True
40      True
60     False
80     False
100    False
120    False
140    False
160     True
180     True
200     True
220    False
240     True
260     True
280     True
300     True
320    False
340     True
360     True
380     True
dtype: bool

In [80]: (s < 0.5).values
Out[80]:
array([ True,  True,  True, False, False, False, False, False,  True,
        True,  True, False,  True,  True,  True,  True, False,  True,
        True,  True])

In [81]: s.plot()
Out[81]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd70dd80f60>

In [82]: s.plot.hist()
Out[82]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd70dd80f60>

In [83]: s.plot.hist()
Out[83]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd70dd80e80>

In [84]: ax = s.plot.hist()

In [85]: ax.set_ylabel('fluorescence')
Out[85]: Text(37.5,0.5,'fluorescence')

In [86]: s.min()
Out[86]: 0.055796203580043446

In [87]: s
Out[87]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [88]: s.max()
Out[88]: 0.92827888051704

In [89]: s.mean()
Out[89]: 0.4093788069161325

In [90]: s.std()
Out[90]: 0.3180494251463849

In [91]: s.median()
Out[91]: 0.2698283838666723

In [92]: s
Out[92]:
0      0.055796
20     0.194123
40     0.125077
60     0.796875
80     0.832015
100    0.548048
120    0.905501
140    0.928279
160    0.095499
180    0.316056
200    0.119604
220    0.890422
240    0.339280
260    0.302004
280    0.219369
300    0.237653
320    0.761351
340    0.235974
360    0.091610
380    0.193040
dtype: float64

In [93]: pd.date_range('2018-06-01', periods=10, freq='D')
Out[93]:
DatetimeIndex(['2018-06-01', '2018-06-02', '2018-06-03', '2018-06-04',
               '2018-06-05', '2018-06-06', '2018-06-07', '2018-06-08',
               '2018-06-09', '2018-06-10'],
              dtype='datetime64[ns]', freq='D')

In [94]: pd.date_range('2018-06-01', periods=10, freq='D').values
Out[94]:
array(['2018-06-01T00:00:00.000000000', '2018-06-02T00:00:00.000000000',
       '2018-06-03T00:00:00.000000000', '2018-06-04T00:00:00.000000000',
       '2018-06-05T00:00:00.000000000', '2018-06-06T00:00:00.000000000',
       '2018-06-07T00:00:00.000000000', '2018-06-08T00:00:00.000000000',
       '2018-06-09T00:00:00.000000000', '2018-06-10T00:00:00.000000000'],
      dtype='datetime64[ns]')

In [95]: pd.date_range('2018-06-01', periods=10, freq='D')
Out[95]:
DatetimeIndex(['2018-06-01', '2018-06-02', '2018-06-03', '2018-06-04',
               '2018-06-05', '2018-06-06', '2018-06-07', '2018-06-08',
               '2018-06-09', '2018-06-10'],
              dtype='datetime64[ns]', freq='D')

In [96]: dr = pd.date_range('2018-06-01', periods=10, freq='D')

In [97]: s3 = pd.Series(data=fl, index=dr)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-97-d38d739a1dc3> in <module>()
----> 1 s3 = pd.Series(data=fl, index=dr)

/usr/local/lib/python3.5/dist-packages/pandas/core/series.py in __init__(self, data, index, dtype, name, copy, fastpath)
    259                             'Length of passed values is {val}, '
    260                             'index implies {ind}'
--> 261                             .format(val=len(data), ind=len(index)))
    262                 except TypeError:
    263                     pass

ValueError: Length of passed values is 20, index implies 10
> /usr/local/lib/python3.5/dist-packages/pandas/core/series.py(263)__init__()
    261                             .format(val=len(data), ind=len(index)))
    262                 except TypeError:
--> 263                     pass
    264
    265             # create/copy the manager

ipdb> c

In [98]: dr = pd.date_range('2018-06-01', periods=20, freq='D')

In [99]: dr = pd.date_range('2018-06-01', periods=20, freq='D')

In [100]: s3 = pd.Series(data=fl, index=dr)

In [101]: s3
Out[101]:
2018-06-01    0.055796
2018-06-02    0.194123
2018-06-03    0.125077
2018-06-04    0.796875
2018-06-05    0.832015
2018-06-06    0.548048
2018-06-07    0.905501
2018-06-08    0.928279
2018-06-09    0.095499
2018-06-10    0.316056
2018-06-11    0.119604
2018-06-12    0.890422
2018-06-13    0.339280
2018-06-14    0.302004
2018-06-15    0.219369
2018-06-16    0.237653
2018-06-17    0.761351
2018-06-18    0.235974
2018-06-19    0.091610
2018-06-20    0.193040
Freq: D, dtype: float64

In [102]: t2 = np.array([50, 70, 40, 20 , 10, 80, 90, 30, 0, 60])

In [103]: t2
Out[103]: array([50, 70, 40, 20, 10, 80, 90, 30,  0, 60])

In [104]: s2 = pd.Series(data=fl[:10], index=t2)

In [105]: s2
Out[105]:
50    0.055796
70    0.194123
40    0.125077
20    0.796875
10    0.832015
80    0.548048
90    0.905501
30    0.928279
0     0.095499
60    0.316056
dtype: float64

In [106]: s2.loc[40:80]
Out[106]:
40    0.125077
20    0.796875
10    0.832015
80    0.548048
dtype: float64

In [107]: s2.index
Out[107]: Int64Index([50, 70, 40, 20, 10, 80, 90, 30, 0, 60], dtype='int64')

In [108]: s2.index.values
Out[108]: array([50, 70, 40, 20, 10, 80, 90, 30,  0, 60])

In [109]: type(s2.index)
Out[109]: pandas.core.indexes.numeric.Int64Index

In [110]: s2.index.values
Out[110]: array([50, 70, 40, 20, 10, 80, 90, 30,  0, 60])

In [111]: ls
09_pandas.md   exp1.csv  exp.xlsx    Pandas_Cheat_Sheet.pdf          spikes.png       t.npy
09_pandas.pdf  exp2.csv  Galton.csv  PandasPythonForDataScience.pdf  spike_times.npy  V.npy

In [112]: t = np.load('t.npy')

In [113]: V = np.load('V.npy')

In [114]: t
Out[114]:
array([0.  , 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1 ,
       0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2 , 0.21,
       0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3 , 0.31, 0.32,
       0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4 , 0.41, 0.42, 0.43,
       0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5 , 0.51, 0.52, 0.53, 0.54,
       0.55, 0.56, 0.57, 0.58, 0.59, 0.6 , 0.61, 0.62, 0.63, 0.64, 0.65,
       0.66, 0.67, 0.68, 0.69, 0.7 , 0.71, 0.72, 0.73, 0.74, 0.75, 0.76,
       0.77, 0.78, 0.79, 0.8 , 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87,
       0.88, 0.89, 0.9 , 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98,
       0.99])

In [115]: V
Out[115]:
array([8.24777758e+01, 6.02342590e+01, 3.08380753e+01, 8.64603373e+01,
       3.56536647e+00, 2.00348496e+01, 5.91368637e+01, 4.15162129e+01,
       5.06776828e+01, 1.00000000e+03, 7.54405999e+01, 6.86314204e+01,
       2.61417936e+01, 3.51484713e+01, 2.58092387e+01, 1.04773450e+01,
       1.32408917e+01, 3.18672503e+01, 5.94482817e+01, 2.66580904e+01,
       5.91594717e+01, 6.53570651e+00, 8.58836573e+00, 1.00000000e+03,
       1.00000000e+03, 8.38927097e+01, 2.21202156e+01, 4.25819646e+01,
       3.83306221e+01, 2.09746967e+01, 7.53824835e+01, 4.45993633e+01,
       2.80853871e+01, 4.17249415e+01, 1.00000000e+03, 7.02201328e+01,
       3.63630564e+01, 5.22943367e+01, 1.00000000e+03, 6.16236716e+01,
       3.81947390e+01, 4.38238019e+01, 6.11110182e+01, 5.44227315e+01,
       2.45454038e+01, 4.02545425e+01, 2.14279017e+01, 6.62861764e+01,
       2.82545726e+01, 1.68717858e+01, 7.61757221e+01, 9.97308451e+00,
       4.37940989e+01, 8.95652919e+01, 3.18723823e+00, 8.79707384e+01,
       4.75663828e+01, 5.34237421e+01, 7.42926799e+01, 1.82295787e+01,
       5.64432797e+01, 5.74893311e+01, 1.00000000e+03, 7.39651359e+01,
       2.21320752e+01, 1.00000000e+03, 1.09191910e+01, 2.26514960e+01,
       1.69261930e+01, 4.44302184e+00, 8.89804525e+01, 8.77941436e+01,
       1.32775860e+01, 8.02132297e+01, 4.58869800e+01, 1.54311492e+01,
       7.52881650e+01, 3.07195208e+01, 3.12770187e+01, 3.49414948e+01,
       8.72803186e+01, 4.22898083e+01, 6.60830128e+01, 7.20574664e+01,
       1.00000000e+03, 5.18257219e+00, 6.97242785e+01, 4.99391302e+01,
       7.90815702e+01, 7.60846665e+01, 2.80442394e+01, 1.00118143e+01,
       5.65604354e+01, 8.32990442e+01, 4.40094004e+01, 5.55926930e+01,
       7.09025454e+01, 2.90419840e+01, 3.45839593e+01, 7.90880387e-01])

In [116]: V[0]
Out[116]: 82.47777579414692

In [117]: s = pd.Series(data=V, index=t)

In [118]: s
Out[118]:
0.00      82.477776
0.01      60.234259
0.02      30.838075
0.03      86.460337
0.04       3.565366
0.05      20.034850
0.06      59.136864
0.07      41.516213
0.08      50.677683
0.09    1000.000000
0.10      75.440600
0.11      68.631420
0.12      26.141794
0.13      35.148471
0.14      25.809239
0.15      10.477345
0.16      13.240892
0.17      31.867250
0.18      59.448282
0.19      26.658090
0.20      59.159472
0.21       6.535707
0.22       8.588366
0.23    1000.000000
0.24    1000.000000
0.25      83.892710
0.26      22.120216
0.27      42.581965
0.28      38.330622
0.29      20.974697
           ...
0.70      88.980452
0.71      87.794144
0.72      13.277586
0.73      80.213230
0.74      45.886980
0.75      15.431149
0.76      75.288165
0.77      30.719521
0.78      31.277019
0.79      34.941495
0.80      87.280319
0.81      42.289808
0.82      66.083013
0.83      72.057466
0.84    1000.000000
0.85       5.182572
0.86      69.724278
0.87      49.939130
0.88      79.081570
0.89      76.084666
0.90      28.044239
0.91      10.011814
0.92      56.560435
0.93      83.299044
0.94      44.009400
0.95      55.592693
0.96      70.902545
0.97      29.041984
0.98      34.583959
0.99       0.790880
Length: 100, dtype: float64

In [119]: s.shape
Out[119]: (100,)

In [120]: s.plot()
Out[120]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd6f0e300b8>

In [121]: s.plot()
Out[121]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd719fda710>

In [122]: s > 200
Out[122]:
0.00    False
0.01    False
0.02    False
0.03    False
0.04    False
0.05    False
0.06    False
0.07    False
0.08    False
0.09     True
0.10    False
0.11    False
0.12    False
0.13    False
0.14    False
0.15    False
0.16    False
0.17    False
0.18    False
0.19    False
0.20    False
0.21    False
0.22    False
0.23     True
0.24     True
0.25    False
0.26    False
0.27    False
0.28    False
0.29    False
        ...
0.70    False
0.71    False
0.72    False
0.73    False
0.74    False
0.75    False
0.76    False
0.77    False
0.78    False
0.79    False
0.80    False
0.81    False
0.82    False
0.83    False
0.84     True
0.85    False
0.86    False
0.87    False
0.88    False
0.89    False
0.90    False
0.91    False
0.92    False
0.93    False
0.94    False
0.95    False
0.96    False
0.97    False
0.98    False
0.99    False
Length: 100, dtype: bool

In [123]: s[s > 200]
Out[123]:
0.09    1000.0
0.23    1000.0
0.24    1000.0
0.34    1000.0
0.38    1000.0
0.62    1000.0
0.65    1000.0
0.84    1000.0
dtype: float64

In [124]: s[0.38]
Out[124]: 1000.0

In [125]: s.loc[0.38]
Out[125]: 1000.0

In [126]: s[s > 200]
Out[126]:
0.09    1000.0
0.23    1000.0
0.24    1000.0
0.34    1000.0
0.38    1000.0
0.62    1000.0
0.65    1000.0
0.84    1000.0
dtype: float64

In [127]: s + 1
Out[127]:
0.00      83.477776
0.01      61.234259
0.02      31.838075
0.03      87.460337
0.04       4.565366
0.05      21.034850
0.06      60.136864
0.07      42.516213
0.08      51.677683
0.09    1001.000000
0.10      76.440600
0.11      69.631420
0.12      27.141794
0.13      36.148471
0.14      26.809239
0.15      11.477345
0.16      14.240892
0.17      32.867250
0.18      60.448282
0.19      27.658090
0.20      60.159472
0.21       7.535707
0.22       9.588366
0.23    1001.000000
0.24    1001.000000
0.25      84.892710
0.26      23.120216
0.27      43.581965
0.28      39.330622
0.29      21.974697
           ...
0.70      89.980452
0.71      88.794144
0.72      14.277586
0.73      81.213230
0.74      46.886980
0.75      16.431149
0.76      76.288165
0.77      31.719521
0.78      32.277019
0.79      35.941495
0.80      88.280319
0.81      43.289808
0.82      67.083013
0.83      73.057466
0.84    1001.000000
0.85       6.182572
0.86      70.724278
0.87      50.939130
0.88      80.081570
0.89      77.084666
0.90      29.044239
0.91      11.011814
0.92      57.560435
0.93      84.299044
0.94      45.009400
0.95      56.592693
0.96      71.902545
0.97      30.041984
0.98      35.583959
0.99       1.790880
Length: 100, dtype: float64

In [128]: s[s > 200]
Out[128]:
0.09    1000.0
0.23    1000.0
0.24    1000.0
0.34    1000.0
0.38    1000.0
0.62    1000.0
0.65    1000.0
0.84    1000.0
dtype: float64

In [129]: t[s > 200]
Out[129]: array([0.09, 0.23, 0.24, 0.34, 0.38, 0.62, 0.65, 0.84])

In [130]: s[s > 200]
Out[130]:
0.09    1000.0
0.23    1000.0
0.24    1000.0
0.34    1000.0
0.38    1000.0
0.62    1000.0
0.65    1000.0
0.84    1000.0
dtype: float64

In [131]: s[s > 200].index
Out[131]: Float64Index([0.09, 0.23, 0.24, 0.34, 0.38, 0.62, 0.65, 0.84], dtype='float64')

In [132]: st = s[s > 200].index

In [133]: np.save('spike_times.npy', st)

In [134]: ls
09_pandas.md   exp1.csv  exp.xlsx    Pandas_Cheat_Sheet.pdf          spikes.png       t.npy
09_pandas.pdf  exp2.csv  Galton.csv  PandasPythonForDataScience.pdf  spike_times.npy  V.npy

In [135]: np.load('spike_times.npy')
Out[135]: array([0.09, 0.23, 0.24, 0.34, 0.38, 0.62, 0.65, 0.84])

In [136]: np.save('spike times.npy', st)

In [137]: ls
09_pandas.md   exp1.csv  exp.xlsx    Pandas_Cheat_Sheet.pdf          spikes.png       spike_times.npy  V.npy
09_pandas.pdf  exp2.csv  Galton.csv  PandasPythonForDataScience.pdf  spike times.npy  t.npy

In [138]: rm spike\ times.npy

In [139]: ls
09_pandas.md   exp1.csv  exp.xlsx    Pandas_Cheat_Sheet.pdf          spikes.png       t.npy
09_pandas.pdf  exp2.csv  Galton.csv  PandasPythonForDataScience.pdf  spike_times.npy  V.npy

In [140]: s[s > 200]
Out[140]:
0.09    1000.0
0.23    1000.0
0.24    1000.0
0.34    1000.0
0.38    1000.0
0.62    1000.0
0.65    1000.0
0.84    1000.0
dtype: float64

In [141]: s[s > 200].plot(ls='', marker='.')
Out[141]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd719fda710>

In [142]: s[s > 200].plot(linestyle='', marker='.')
Out[142]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd719fda710>

In [143]: s > 20
Out[143]:
0.00     True
0.01     True
0.02     True
0.03     True
0.04    False
0.05     True
0.06     True
0.07     True
0.08     True
0.09     True
0.10     True
0.11     True
0.12     True
0.13     True
0.14     True
0.15    False
0.16    False
0.17     True
0.18     True
0.19     True
0.20     True
0.21    False
0.22    False
0.23     True
0.24     True
0.25     True
0.26     True
0.27     True
0.28     True
0.29     True
        ...
0.70     True
0.71     True
0.72    False
0.73     True
0.74     True
0.75    False
0.76     True
0.77     True
0.78     True
0.79     True
0.80     True
0.81     True
0.82     True
0.83     True
0.84     True
0.85    False
0.86     True
0.87     True
0.88     True
0.89     True
0.90     True
0.91    False
0.92     True
0.93     True
0.94     True
0.95     True
0.96     True
0.97     True
0.98     True
0.99    False
Length: 100, dtype: bool

In [144]: s > 200
Out[144]:
0.00    False
0.01    False
0.02    False
0.03    False
0.04    False
0.05    False
0.06    False
0.07    False
0.08    False
0.09     True
0.10    False
0.11    False
0.12    False
0.13    False
0.14    False
0.15    False
0.16    False
0.17    False
0.18    False
0.19    False
0.20    False
0.21    False
0.22    False
0.23     True
0.24     True
0.25    False
0.26    False
0.27    False
0.28    False
0.29    False
        ...
0.70    False
0.71    False
0.72    False
0.73    False
0.74    False
0.75    False
0.76    False
0.77    False
0.78    False
0.79    False
0.80    False
0.81    False
0.82    False
0.83    False
0.84     True
0.85    False
0.86    False
0.87    False
0.88    False
0.89    False
0.90    False
0.91    False
0.92    False
0.93    False
0.94    False
0.95    False
0.96    False
0.97    False
0.98    False
0.99    False
Length: 100, dtype: bool

In [145]: eeg = np.random.random((20, 3))

In [146]: eeg
Out[146]:
array([[0.42655957, 0.26800355, 0.49069561],
       [0.89906914, 0.16803068, 0.00780771],
       [0.41787305, 0.80623626, 0.9666413 ],
       [0.28713752, 0.52892988, 0.6649552 ],
       [0.38094201, 0.1961847 , 0.13923259],
       [0.69353605, 0.1205256 , 0.2631022 ],
       [0.65990344, 0.23853481, 0.09517654],
       [0.48953366, 0.37795881, 0.58130989],
       [0.19343588, 0.40157794, 0.39175034],
       [0.18644337, 0.21934481, 0.77337814],
       [0.32918384, 0.40232268, 0.13593377],
       [0.67914706, 0.91032274, 0.17130591],
       [0.8409699 , 0.99422823, 0.88409431],
       [0.55601736, 0.44692312, 0.16384185],
       [0.39328943, 0.68021396, 0.75831263],
       [0.50003446, 0.79439173, 0.59832539],
       [0.46703166, 0.32322887, 0.52195299],
       [0.04650353, 0.12575051, 0.10571073],
       [0.41226214, 0.55118165, 0.48893002],
       [0.49815035, 0.70073484, 0.24645154]])

In [147]: t = np.arange(0, 20*50, 50)

In [148]: t
Out[148]:
array([  0,  50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600,
       650, 700, 750, 800, 850, 900, 950])

In [149]: len(t)
Out[149]: 20

In [150]: chans = ['Fz', 'Cz', 'Pz']

In [151]: eeg
Out[151]:
array([[0.42655957, 0.26800355, 0.49069561],
       [0.89906914, 0.16803068, 0.00780771],
       [0.41787305, 0.80623626, 0.9666413 ],
       [0.28713752, 0.52892988, 0.6649552 ],
       [0.38094201, 0.1961847 , 0.13923259],
       [0.69353605, 0.1205256 , 0.2631022 ],
       [0.65990344, 0.23853481, 0.09517654],
       [0.48953366, 0.37795881, 0.58130989],
       [0.19343588, 0.40157794, 0.39175034],
       [0.18644337, 0.21934481, 0.77337814],
       [0.32918384, 0.40232268, 0.13593377],
       [0.67914706, 0.91032274, 0.17130591],
       [0.8409699 , 0.99422823, 0.88409431],
       [0.55601736, 0.44692312, 0.16384185],
       [0.39328943, 0.68021396, 0.75831263],
       [0.50003446, 0.79439173, 0.59832539],
       [0.46703166, 0.32322887, 0.52195299],
       [0.04650353, 0.12575051, 0.10571073],
       [0.41226214, 0.55118165, 0.48893002],
       [0.49815035, 0.70073484, 0.24645154]])

In [152]: t
Out[152]:
array([  0,  50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600,
       650, 700, 750, 800, 850, 900, 950])

In [153]: chans
Out[153]: ['Fz', 'Cz', 'Pz']

In [154]: df = pd.DataFrame(data=eeg, index=t, columns=chans)

In [155]: df
Out[155]:
           Fz        Cz        Pz
0    0.426560  0.268004  0.490696
50   0.899069  0.168031  0.007808
100  0.417873  0.806236  0.966641
150  0.287138  0.528930  0.664955
200  0.380942  0.196185  0.139233
250  0.693536  0.120526  0.263102
300  0.659903  0.238535  0.095177
350  0.489534  0.377959  0.581310
400  0.193436  0.401578  0.391750
450  0.186443  0.219345  0.773378
500  0.329184  0.402323  0.135934
550  0.679147  0.910323  0.171306
600  0.840970  0.994228  0.884094
650  0.556017  0.446923  0.163842
700  0.393289  0.680214  0.758313
750  0.500034  0.794392  0.598325
800  0.467032  0.323229  0.521953
850  0.046504  0.125751  0.105711
900  0.412262  0.551182  0.488930
950  0.498150  0.700735  0.246452

In [156]: df.iloc[0, 0]
Out[156]: 0.4265595742097732

In [157]: df.iloc[-1, -1]
Out[157]: 0.24645153551504706

In [158]: df.iloc[:5]
Out[158]:
           Fz        Cz        Pz
0    0.426560  0.268004  0.490696
50   0.899069  0.168031  0.007808
100  0.417873  0.806236  0.966641
150  0.287138  0.528930  0.664955
200  0.380942  0.196185  0.139233

In [159]: df['Fz']
Out[159]:
0      0.426560
50     0.899069
100    0.417873
150    0.287138
200    0.380942
250    0.693536
300    0.659903
350    0.489534
400    0.193436
450    0.186443
500    0.329184
550    0.679147
600    0.840970
650    0.556017
700    0.393289
750    0.500034
800    0.467032
850    0.046504
900    0.412262
950    0.498150
Name: Fz, dtype: float64

In [160]: df.iloc
Out[160]: <pandas.core.indexing._iLocIndexer at 0x7fd719bcfef8>

In [161]: df['Fz']
Out[161]:
0      0.426560
50     0.899069
100    0.417873
150    0.287138
200    0.380942
250    0.693536
300    0.659903
350    0.489534
400    0.193436
450    0.186443
500    0.329184
550    0.679147
600    0.840970
650    0.556017
700    0.393289
750    0.500034
800    0.467032
850    0.046504
900    0.412262
950    0.498150
Name: Fz, dtype: float64

In [162]: df['Fz'][550]
Out[162]: 0.6791470577414486

In [163]: df['Fz'][550]
Out[163]: 0.6791470577414486

In [164]: df.loc
Out[164]: <pandas.core.indexing._LocIndexer at 0x7fd719b89d68>

In [165]: df.loc[550]
Out[165]:
Fz    0.679147
Cz    0.910323
Pz    0.171306
Name: 550, dtype: float64

In [166]: df.loc[550]['Fz']
Out[166]: 0.6791470577414486

In [167]: df.loc[550]['Fz']
Out[167]: 0.6791470577414486

In [168]: df['Fz'][550]
Out[168]: 0.6791470577414486

In [169]: exp1 = pd.read_csv('exp1.csv')

In [170]: exp1
Out[170]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [171]: exp1['stimulus']
Out[171]:
0    L
1    R
2    R
3    R
4    L
5    L
6    R
7    L
Name: stimulus, dtype: object

In [172]: exp1['stimulus'].dtype
Out[172]: dtype('O')

In [173]: exp1['stimulus'][0]
Out[173]: 'L'

In [174]: type(exp1['stimulus'][0])
Out[174]: str

In [175]: exp1.plot()
Out[175]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd719bb3668>

In [176]: ax = exp1.plot()

In [177]: ax.set_ylabel('time (s)')
Out[177]: Text(13.9444,0.5,'time (s)')

In [178]: exp1.plot.hist()
Out[178]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd7198ce3c8>

In [179]: exp1.hist()
Out[179]:
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7fd71989ada0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x7fd71984cfd0>]],
      dtype=object)

In [180]: exp2 = pd.read_csv('exp2.csv')

In [181]: exp2
Out[181]:
   subject  start_time  end_time stimulus outcome
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [182]: exp1
Out[182]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [183]: exp1
Out[183]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [184]: exp2
Out[184]:
   subject  start_time  end_time stimulus outcome
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [185]: pd.concat?

In [186]: pd.concat([exp1, exp2])
Out[186]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [187]: exps = pd.concat([exp1, exp2])

In [188]: exps
Out[188]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [189]: pd.concat([exp1, exp2], axis=1)
Out[189]:
   subject  start_time  end_time stimulus outcome subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass     A02         2.7       5.6        L    pass
1      A01         1.6       2.1        R    pass     A02         1.2       4.3        L    pass
2      A01         2.3       5.6        R    pass     A02         4.0      10.4        R    fail
3      A01         4.0      10.2        R    fail     A02         2.3       5.6        R    pass
4      A01         2.8       4.5        L    pass     A02         4.1      10.0        R    fail
5      A01         0.7       6.1        L    pass     A02         3.9      12.1        R    fail
6      A01         3.5      11.2        R    fail     A02         2.8       4.5        L    pass
7      A01         2.7       5.6        L    pass     A02         1.3       3.1        R    pass
8      NaN         NaN       NaN      NaN     NaN     A02         0.8       4.1        L    pass
9      NaN         NaN       NaN      NaN     NaN     A02         3.6      12.4        R    fail
10     NaN         NaN       NaN      NaN     NaN     A02         5.5      13.3        R    fail

In [190]: pd.concat([exp1, exp2], axis=1)['subject']
Out[190]:
   subject subject
0      A01     A02
1      A01     A02
2      A01     A02
3      A01     A02
4      A01     A02
5      A01     A02
6      A01     A02
7      A01     A02
8      NaN     A02
9      NaN     A02
10     NaN     A02

In [191]: exps.corr()
Out[191]:
            start_time  end_time
start_time    1.000000  0.841829
end_time      0.841829  1.000000

In [192]: exps
Out[192]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [193]: exps.corr()
Out[193]:
            start_time  end_time
start_time    1.000000  0.841829
end_time      0.841829  1.000000

In [194]: exps.corr()
Out[194]:
            start_time  end_time
start_time    1.000000  0.841829
end_time      0.841829  1.000000

In [195]: type(exps.corr())
Out[195]: pandas.core.frame.DataFrame

In [196]: exps.corr().to_csv('corr.csv')

In [197]: ls
09_pandas.md   corr.csv  exp2.csv  Galton.csv              PandasPythonForDataScience.pdf  spike_times.npy  V.npy
09_pandas.pdf  exp1.csv  exp.xlsx  Pandas_Cheat_Sheet.pdf  spikes.png                      t.npy

In [198]: pd.read_excel?

In [199]: exps = pd.read_excel('exp.xlsx')

In [200]: exps
Out[200]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [201]: exp1 = pd.read_excel('exp.xlsx', sheet='exp1')

In [202]: exp2 = pd.read_excel('exp.xlsx', sheet='exp2')

In [203]: exp1
Out[203]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [204]: exp2
Out[204]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [205]: exps.to_excel?

In [206]: exps
Out[206]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [207]: exps = pd.concat([exp1, exp2])

In [208]: exps
Out[208]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [209]: exps
Out[209]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [210]: exps.max()
Out[210]:
subject        A01
start_time       4
end_time      11.2
stimulus         R
outcome       pass
dtype: object

In [211]: exps
Out[211]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [212]: exp1 = pd.read_excel('exp.xlsx', sheet='exp1')

In [213]: exp2 = pd.read_excel('exp.xlsx', sheet='exp2')

In [214]: exps = pd.concat([exp1, exp2])

In [215]: exps
Out[215]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [216]: exp2 = pd.read_excel('exp.xlsx', sheetname='exp2')
/usr/local/lib/python3.5/dist-packages/pandas/io/excel.py:329: FutureWarning: The `sheetname` keyword is deprecated, use `sheet_name` instead
  **kwds)

In [217]: exp2 = pd.read_excel('exp.xlsx', sheet_name='exp2')

In [218]: exp1 = pd.read_excel('exp.xlsx', sheet_name='exp1')

In [219]: exps = pd.concat([exp1, exp2])

In [220]: exps
Out[220]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [221]: exps.max()
Out[221]:
subject        A02
start_time     5.5
end_time      13.3
stimulus         R
outcome       pass
dtype: object

In [222]: type(exps.max())
Out[222]: pandas.core.series.Series

In [223]: exps.min()
Out[223]:
subject        A01
start_time     0.7
end_time       2.1
stimulus         L
outcome       fail
dtype: object

In [224]: exps.mean()
Out[224]:
start_time    2.742105
end_time      7.173684
dtype: float64

In [225]: exps.median()
Out[225]:
start_time    2.7
end_time      5.6
dtype: float64

In [226]: exps.std()
Out[226]:
start_time    1.281629
end_time      3.502038
dtype: float64

In [227]: exps.describe()
Out[227]:
       start_time   end_time
count   19.000000  19.000000
mean     2.742105   7.173684
std      1.281629   3.502038
min      0.700000   2.100000
25%      1.950000   4.500000
50%      2.700000   5.600000
75%      3.750000  10.300000
max      5.500000  13.300000

In [228]: type(exps.describe())
Out[228]: pandas.core.frame.DataFrame

In [229]: exps.describe()['start_time']
Out[229]:
count    19.000000
mean      2.742105
std       1.281629
min       0.700000
25%       1.950000
50%       2.700000
75%       3.750000
max       5.500000
Name: start_time, dtype: float64

In [230]: exps.describe()['end_time']
Out[230]:
count    19.000000
mean      7.173684
std       3.502038
min       2.100000
25%       4.500000
50%       5.600000
75%      10.300000
max      13.300000
Name: end_time, dtype: float64

In [231]: exps.describe()['end_time']['mean']
Out[231]: 7.173684210526316

In [232]: exps
Out[232]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [233]: exps['subject']
Out[233]:
0     A01
1     A01
2     A01
3     A01
4     A01
5     A01
6     A01
7     A01
0     A02
1     A02
2     A02
3     A02
4     A02
5     A02
6     A02
7     A02
8     A02
9     A02
10    A02
Name: subject, dtype: object

In [234]: exps['subject'].nunique()
Out[234]: 2

In [235]: exps['start_time'].nunique()
Out[235]: 14

In [236]: exps['start_time'].shape
Out[236]: (19,)

In [237]: exps['start_time'].nunique()
Out[237]: 14

In [238]: exps
Out[238]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [239]: exps.groupby('outcome')
Out[239]: <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x7fd6ee23be48>

In [240]: exps.groupby('outcome').mean()
Out[240]:
         start_time   end_time
outcome
fail       4.085714  11.371429
pass       1.958333   4.725000

In [241]: exps.groupby('outcome').max()
Out[241]:
        subject  start_time  end_time stimulus
outcome
fail        A02         5.5      13.3        R
pass        A02         2.8       6.1        R

In [242]: exps.groupby('outcome').describe()
Out[242]:
        end_time                                                 ...  start_time
           count       mean       std   min    25%    50%    75% ...        mean       std  min    25%  50%   75%  max
outcome                                                          ...
fail         7.0  11.371429  1.260574  10.0  10.30  11.20  12.25 ...    4.085714  0.661888  3.5  3.750  4.0  4.05  5.5
pass        12.0   4.725000  1.203121   2.1   4.25   5.05   5.60 ...    1.958333  0.793678  0.7  1.275  2.3  2.70  2.8

[2 rows x 16 columns]

In [243]: exps
Out[243]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [244]: d = {}

In [245]: d
Out[245]: {}

In [246]: d['mike'] = 8

In [247]: d
Out[247]: {'mike': 8}

In [248]: exps
Out[248]:
   subject  start_time  end_time stimulus outcome
0      A01         2.3       5.6        L    pass
1      A01         1.6       2.1        R    pass
2      A01         2.3       5.6        R    pass
3      A01         4.0      10.2        R    fail
4      A01         2.8       4.5        L    pass
5      A01         0.7       6.1        L    pass
6      A01         3.5      11.2        R    fail
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
1      A02         1.2       4.3        L    pass
2      A02         4.0      10.4        R    fail
3      A02         2.3       5.6        R    pass
4      A02         4.1      10.0        R    fail
5      A02         3.9      12.1        R    fail
6      A02         2.8       4.5        L    pass
7      A02         1.3       3.1        R    pass
8      A02         0.8       4.1        L    pass
9      A02         3.6      12.4        R    fail
10     A02         5.5      13.3        R    fail

In [249]: exps['duration'] = exps['end_time'] - exps['start_time']

In [250]: exps
Out[250]:
   subject  start_time  end_time stimulus outcome  duration
0      A01         2.3       5.6        L    pass       3.3
1      A01         1.6       2.1        R    pass       0.5
2      A01         2.3       5.6        R    pass       3.3
3      A01         4.0      10.2        R    fail       6.2
4      A01         2.8       4.5        L    pass       1.7
5      A01         0.7       6.1        L    pass       5.4
6      A01         3.5      11.2        R    fail       7.7
7      A01         2.7       5.6        L    pass       2.9
0      A02         2.7       5.6        L    pass       2.9
1      A02         1.2       4.3        L    pass       3.1
2      A02         4.0      10.4        R    fail       6.4
3      A02         2.3       5.6        R    pass       3.3
4      A02         4.1      10.0        R    fail       5.9
5      A02         3.9      12.1        R    fail       8.2
6      A02         2.8       4.5        L    pass       1.7
7      A02         1.3       3.1        R    pass       1.8
8      A02         0.8       4.1        L    pass       3.3
9      A02         3.6      12.4        R    fail       8.8
10     A02         5.5      13.3        R    fail       7.8

In [251]: exps.groupby('outcome').mean()
Out[251]:
         start_time   end_time  duration
outcome
fail       4.085714  11.371429  7.285714
pass       1.958333   4.725000  2.766667

In [252]: missd = [[1, 2, 3],
     ...:          [4, 5],
     ...:          [7, 8, 9]]
     ...:

In [253]: missd
Out[253]: [[1, 2, 3], [4, 5], [7, 8, 9]]

In [254]: type(missd)
Out[254]: list

In [255]: np.array(missd)
Out[255]: array([list([1, 2, 3]), list([4, 5]), list([7, 8, 9])], dtype=object)

In [256]: a = np.array(missd)

In [257]: a.ndim
Out[257]: 1

In [258]: a.shape
Out[258]: (3,)

In [259]: a[0, 1]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-259-4446d87ab35e> in <module>()
----> 1 a[0, 1]

IndexError: too many indices for array
> <ipython-input-259-4446d87ab35e>(1)<module>()
----> 1 a[0, 1]

ipdb> c

In [260]: missd = [[1, 2, 3],
     ...:          [4, 5, np.nan],
     ...:          [7, 8, 9]]
     ...:

In [261]:

In [261]: np.array(missd)
Out[261]:
array([[ 1.,  2.,  3.],
       [ 4.,  5., nan],
       [ 7.,  8.,  9.]])

In [262]: missd = [[1, 2, 3],
     ...:          [4, 5],
     ...:          [7, 8, 9]]
     ...:

In [263]: pd.DataFrame(missd)
Out[263]:
   0  1    2
0  1  2  3.0
1  4  5  NaN
2  7  8  9.0

In [264]: df = pd.DataFrame(missd)

In [265]: df.mean()
Out[265]:
0    4.0
1    5.0
2    6.0
dtype: float64

In [266]: exps.groupby('outcome').mean()
Out[266]:
         start_time   end_time  duration
outcome
fail       4.085714  11.371429  7.285714
pass       1.958333   4.725000  2.766667

In [267]: exps.groupby('outcome').mean()
Out[267]:
         start_time   end_time  duration
outcome
fail       4.085714  11.371429  7.285714
pass       1.958333   4.725000  2.766667

In [268]: exps.groupby('outcome').mean()['start_time']
Out[268]:
outcome
fail    4.085714
pass    1.958333
Name: start_time, dtype: float64

In [269]: exps.groupby('outcome').mean()['start_time']['fail']
Out[269]: 4.085714285714286

In [270]: exps.groupby('outcome').mean()
Out[270]:
         start_time   end_time  duration
outcome
fail       4.085714  11.371429  7.285714
pass       1.958333   4.725000  2.766667

In [271]: exps.groupby('outcome').mean()['start_time']
Out[271]:
outcome
fail    4.085714
pass    1.958333
Name: start_time, dtype: float64

In [272]: gdf = pd.read_csv('Galton.csv')

In [273]: gdf
Out[273]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [274]: gdf.groupby('Family')
Out[274]: <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x7fd6ed0d4be0>

In [275]: gdf.groupby('Family').mean()
Out[275]:
        Father  Mother     Height  Kids
Family
1         78.5    67.0  70.100000     4
10        74.0    65.5  65.500000     1
100       69.0    66.0  70.733333     3
101       69.0    66.7  70.416667     6
102       69.0    66.0  66.166667     6
103       69.0    66.5  69.200000     5
104       69.5    66.5  66.625000     4
105       69.0    66.5  66.500000     6
106       69.5    66.0  68.500000     7
107       69.0    66.0  67.722222     9
108       69.0    65.0  65.571429     7
109       69.5    64.5  64.442857     7
11        74.0    62.0  67.312500     8
110       69.2    64.0  66.675000     4
112       69.0    63.0  66.666667     3
113       69.0    63.0  72.000000     1
114       69.0    63.0  67.500000     6
115       69.0    63.5  64.928571     7
116       69.0    63.5  65.733333     3
117       69.7    62.0  62.500000     1
118       69.5    62.0  71.333333     3
119       69.0    62.0  69.400000     5
12        74.0    61.0  65.000000     1
121       69.0    62.5  66.312500     8
122       69.0    62.0  68.000000     4
123       69.5    61.0  66.700000     5
124       69.0    61.0  64.555556     9
125       69.0    60.0  67.000000     3
126       69.0    60.0  64.300000     4
127       69.0    60.5  69.500000     1
...        ...     ...        ...   ...
71        70.0    65.0  66.666667     6
72        70.0    65.0  69.814286     7
73        70.0    65.0  70.166667     3
74        70.0    65.0  69.000000     2
75        70.0    64.7  67.414286     7
76        70.0    64.0  67.671429     7
77        70.0    64.0  67.550000     4
78        70.0    64.2  65.160000     5
79        70.5    64.0  68.375000     8
8         74.0    66.5  68.166667     3
80        70.5    64.5  60.000000     1
81        70.0    64.0  64.750000     4
82        70.0    64.0  68.555556     9
83        70.0    63.7  64.387500     8
85        70.5    63.0  67.400000     5
86        70.0    63.5  67.375000     4
87        70.0    63.0  65.175000     4
88        70.0    63.0  64.875000     4
89        70.5    62.0  67.625000     8
9         74.5    66.0  66.000000     1
90        70.3    62.7  66.500000     7
91        70.5    62.0  68.000000     3
92        70.0    61.0  69.100000     2
93        70.0    60.0  64.875000     4
94        70.0    60.0  65.000000     2
95        70.0    58.5  66.333333     3
96        70.0    58.0  66.400000     5
97        69.0    68.5  67.150000    10
98        69.0    67.0  64.000000     1
99        69.0    66.0  67.987500     8

[197 rows x 4 columns]

In [276]: 67/12
Out[276]: 5.583333333333333

In [277]: gdf = pd.read_csv('Galton.csv')

In [278]: gdf
Out[278]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [279]: gdf.shape
Out[279]: (898, 6)

In [280]: len(gdf)
Out[280]: 898

In [281]: gdf
Out[281]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [282]: gdf.columns
Out[282]: Index(['Family', 'Father', 'Mother', 'Gender', 'Height', 'Kids'], dtype='object')

In [283]: gdf.mean()
Out[283]:
Father    69.232851
Mother    64.084410
Height    66.760690
Kids       6.135857
dtype: float64

In [284]: gdf['Height']
Out[284]:
0      73.2
1      69.2
2      69.0
3      69.0
4      73.5
5      72.5
6      65.5
7      65.5
8      71.0
9      68.0
10     70.5
11     68.5
12     67.0
13     64.5
14     63.0
15     72.0
16     69.0
17     68.0
18     66.5
19     62.5
20     62.5
21     69.5
22     76.5
23     74.0
24     73.0
25     73.0
26     70.5
27     64.0
28     70.5
29     68.0
       ...
868    71.5
869    68.0
870    65.5
871    64.0
872    62.0
873    62.0
874    61.0
875    70.5
876    68.0
877    67.0
878    65.0
879    64.0
880    64.0
881    60.0
882    64.5
883    66.0
884    60.0
885    64.0
886    62.0
887    61.0
888    66.5
889    57.0
890    72.0
891    70.5
892    68.7
893    68.5
894    67.7
895    64.0
896    63.5
897    63.0
Name: Height, Length: 898, dtype: float64

In [285]: gdf['Height'].mean()
Out[285]: 66.76069042316259

In [286]: gdf.mean()
Out[286]:
Father    69.232851
Mother    64.084410
Height    66.760690
Kids       6.135857
dtype: float64

In [287]: gdf.mean()['Height']
Out[287]: 66.76069042316252

In [288]: gdf.hist(column='Height')
Out[288]:
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7fd6ed0d3f98>]],
      dtype=object)

In [289]: gdf['Height']
Out[289]:
0      73.2
1      69.2
2      69.0
3      69.0
4      73.5
5      72.5
6      65.5
7      65.5
8      71.0
9      68.0
10     70.5
11     68.5
12     67.0
13     64.5
14     63.0
15     72.0
16     69.0
17     68.0
18     66.5
19     62.5
20     62.5
21     69.5
22     76.5
23     74.0
24     73.0
25     73.0
26     70.5
27     64.0
28     70.5
29     68.0
       ...
868    71.5
869    68.0
870    65.5
871    64.0
872    62.0
873    62.0
874    61.0
875    70.5
876    68.0
877    67.0
878    65.0
879    64.0
880    64.0
881    60.0
882    64.5
883    66.0
884    60.0
885    64.0
886    62.0
887    61.0
888    66.5
889    57.0
890    72.0
891    70.5
892    68.7
893    68.5
894    67.7
895    64.0
896    63.5
897    63.0
Name: Height, Length: 898, dtype: float64

In [290]: gdf['Height'].plot.hist()
Out[290]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd6ed0b0710>

In [291]: gdf.hist(column='Height')
Out[291]:
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7fd6ece054a8>]],
      dtype=object)

In [292]: gdf['Height']
Out[292]:
0      73.2
1      69.2
2      69.0
3      69.0
4      73.5
5      72.5
6      65.5
7      65.5
8      71.0
9      68.0
10     70.5
11     68.5
12     67.0
13     64.5
14     63.0
15     72.0
16     69.0
17     68.0
18     66.5
19     62.5
20     62.5
21     69.5
22     76.5
23     74.0
24     73.0
25     73.0
26     70.5
27     64.0
28     70.5
29     68.0
       ...
868    71.5
869    68.0
870    65.5
871    64.0
872    62.0
873    62.0
874    61.0
875    70.5
876    68.0
877    67.0
878    65.0
879    64.0
880    64.0
881    60.0
882    64.5
883    66.0
884    60.0
885    64.0
886    62.0
887    61.0
888    66.5
889    57.0
890    72.0
891    70.5
892    68.7
893    68.5
894    67.7
895    64.0
896    63.5
897    63.0
Name: Height, Length: 898, dtype: float64

In [293]: gdf['Height'].plot.hist()
Out[293]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd6ece054a8>

In [294]: gdf['Height'].plot.hist()
Out[294]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd6ecbc0b00>

In [295]: gdf['Height'].hist()
Out[295]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd6ecbc0b00>

In [296]: gdf['Height'].plot.hist()
Out[296]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd6ecb932b0>

In [297]: gdf['Height'].hist()
Out[297]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd6ecaf2e80>

In [298]: gdf['Family'].nunique
Out[298]:
<bound method IndexOpsMixin.nunique of 0         1
1         1
2         1
3         1
4         2
5         2
6         2
7         2
8         3
9         3
10        4
11        4
12        4
13        4
14        4
15        5
16        5
17        5
18        5
19        5
20        5
21        6
22        7
23        7
24        7
25        7
26        7
27        7
28        8
29        8
       ...
868     198
869     198
870     198
871     198
872     198
873     198
874     198
875     199
876     199
877     199
878     199
879     199
880     199
881     199
882     200
883     201
884     201
885     203
886     203
887     203
888     204
889     204
890    136A
891    136A
892    136A
893    136A
894    136A
895    136A
896    136A
897    136A
Name: Family, Length: 898, dtype: object>

In [299]: gdf['Family'].nunique()
Out[299]: 197

In [300]: np.unique(gdf['Family'])
Out[300]:
array(['1', '10', '100', '101', '102', '103', '104', '105', '106', '107',
       '108', '109', '11', '110', '112', '113', '114', '115', '116',
       '117', '118', '119', '12', '121', '122', '123', '124', '125',
       '126', '127', '128', '129', '130', '131', '132', '133', '134',
       '135', '136', '136A', '137', '138', '139', '14', '140', '141',
       '142', '143', '144', '145', '146', '147', '148', '149', '15',
       '150', '151', '152', '153', '154', '155', '156', '157', '158',
       '159', '16', '160', '162', '163', '164', '165', '166', '167',
       '168', '169', '17', '170', '171', '172', '173', '174', '175',
       '176', '177', '178', '179', '18', '180', '181', '182', '183',
       '184', '185', '186', '187', '188', '19', '190', '191', '192',
       '193', '194', '195', '196', '197', '198', '199', '2', '20', '200',
       '201', '203', '204', '21', '22', '23', '24', '25', '26', '27',
       '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37',
       '38', '39', '4', '40', '41', '42', '43', '44', '45', '46', '47',
       '48', '49', '5', '51', '52', '53', '54', '55', '56', '57', '58',
       '59', '6', '60', '61', '62', '63', '64', '65', '66', '67', '68',
       '69', '7', '70', '71', '72', '73', '74', '75', '76', '77', '78',
       '79', '8', '80', '81', '82', '83', '85', '86', '87', '88', '89',
       '9', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99'],
      dtype=object)

In [301]: len(np.unique(gdf['Family']))
Out[301]: 197

In [302]: gdf
Out[302]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [303]: gdf['Family'] != '136A'
Out[303]:
0       True
1       True
2       True
3       True
4       True
5       True
6       True
7       True
8       True
9       True
10      True
11      True
12      True
13      True
14      True
15      True
16      True
17      True
18      True
19      True
20      True
21      True
22      True
23      True
24      True
25      True
26      True
27      True
28      True
29      True
       ...
868     True
869     True
870     True
871     True
872     True
873     True
874     True
875     True
876     True
877     True
878     True
879     True
880     True
881     True
882     True
883     True
884     True
885     True
886     True
887     True
888     True
889     True
890    False
891    False
892    False
893    False
894    False
895    False
896    False
897    False
Name: Family, Length: 898, dtype: bool

In [304]: gdf[gdf['Family'] != '136A']
Out[304]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
860    196    65.5    63.0      M    71.0     4
861    196    65.5    63.0      M    69.0     4
862    196    65.5    63.0      F    63.5     4
863    197    65.5    60.0      M    68.0     5
864    197    65.5    60.0      M    68.0     5
865    197    65.5    60.0      M    67.0     5
866    197    65.5    60.0      M    67.0     5
867    197    65.5    60.0      F    62.0     5
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2

[890 rows x 6 columns]

In [305]: gdf[gdf['Family'] != '136A']
Out[305]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
860    196    65.5    63.0      M    71.0     4
861    196    65.5    63.0      M    69.0     4
862    196    65.5    63.0      F    63.5     4
863    197    65.5    60.0      M    68.0     5
864    197    65.5    60.0      M    68.0     5
865    197    65.5    60.0      M    67.0     5
866    197    65.5    60.0      M    67.0     5
867    197    65.5    60.0      F    62.0     5
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2

[890 rows x 6 columns]

In [306]: gdf['Family'] != '136A'
Out[306]:
0       True
1       True
2       True
3       True
4       True
5       True
6       True
7       True
8       True
9       True
10      True
11      True
12      True
13      True
14      True
15      True
16      True
17      True
18      True
19      True
20      True
21      True
22      True
23      True
24      True
25      True
26      True
27      True
28      True
29      True
       ...
868     True
869     True
870     True
871     True
872     True
873     True
874     True
875     True
876     True
877     True
878     True
879     True
880     True
881     True
882     True
883     True
884     True
885     True
886     True
887     True
888     True
889     True
890    False
891    False
892    False
893    False
894    False
895    False
896    False
897    False
Name: Family, Length: 898, dtype: bool

In [307]: gdf[gdf['Family'] != '136A']
Out[307]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
860    196    65.5    63.0      M    71.0     4
861    196    65.5    63.0      M    69.0     4
862    196    65.5    63.0      F    63.5     4
863    197    65.5    60.0      M    68.0     5
864    197    65.5    60.0      M    68.0     5
865    197    65.5    60.0      M    67.0     5
866    197    65.5    60.0      M    67.0     5
867    197    65.5    60.0      F    62.0     5
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2

[890 rows x 6 columns]

In [308]: gdf.loc[gdf['Family'] != '136A']
Out[308]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
860    196    65.5    63.0      M    71.0     4
861    196    65.5    63.0      M    69.0     4
862    196    65.5    63.0      F    63.5     4
863    197    65.5    60.0      M    68.0     5
864    197    65.5    60.0      M    68.0     5
865    197    65.5    60.0      M    67.0     5
866    197    65.5    60.0      M    67.0     5
867    197    65.5    60.0      F    62.0     5
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2

[890 rows x 6 columns]

In [309]: gdf[gdf['Family'] != '136A']
Out[309]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
860    196    65.5    63.0      M    71.0     4
861    196    65.5    63.0      M    69.0     4
862    196    65.5    63.0      F    63.5     4
863    197    65.5    60.0      M    68.0     5
864    197    65.5    60.0      M    68.0     5
865    197    65.5    60.0      M    67.0     5
866    197    65.5    60.0      M    67.0     5
867    197    65.5    60.0      F    62.0     5
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2

[890 rows x 6 columns]

In [310]: gdf['Family']
Out[310]:
0         1
1         1
2         1
3         1
4         2
5         2
6         2
7         2
8         3
9         3
10        4
11        4
12        4
13        4
14        4
15        5
16        5
17        5
18        5
19        5
20        5
21        6
22        7
23        7
24        7
25        7
26        7
27        7
28        8
29        8
       ...
868     198
869     198
870     198
871     198
872     198
873     198
874     198
875     199
876     199
877     199
878     199
879     199
880     199
881     199
882     200
883     201
884     201
885     203
886     203
887     203
888     204
889     204
890    136A
891    136A
892    136A
893    136A
894    136A
895    136A
896    136A
897    136A
Name: Family, Length: 898, dtype: object

In [311]: gdf[gdf['Family'] != '136A']
Out[311]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
860    196    65.5    63.0      M    71.0     4
861    196    65.5    63.0      M    69.0     4
862    196    65.5    63.0      F    63.5     4
863    197    65.5    60.0      M    68.0     5
864    197    65.5    60.0      M    68.0     5
865    197    65.5    60.0      M    67.0     5
866    197    65.5    60.0      M    67.0     5
867    197    65.5    60.0      F    62.0     5
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2

[890 rows x 6 columns]

In [312]: gdf['Family']
Out[312]:
0         1
1         1
2         1
3         1
4         2
5         2
6         2
7         2
8         3
9         3
10        4
11        4
12        4
13        4
14        4
15        5
16        5
17        5
18        5
19        5
20        5
21        6
22        7
23        7
24        7
25        7
26        7
27        7
28        8
29        8
       ...
868     198
869     198
870     198
871     198
872     198
873     198
874     198
875     199
876     199
877     199
878     199
879     199
880     199
881     199
882     200
883     201
884     201
885     203
886     203
887     203
888     204
889     204
890    136A
891    136A
892    136A
893    136A
894    136A
895    136A
896    136A
897    136A
Name: Family, Length: 898, dtype: object

In [313]: gdf['Father'].mean()
Out[313]: 69.23285077951002

In [314]: gdf.groupby('Family')
Out[314]: <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x7fd6ecbc65c0>

In [315]: gdf.groupby('Family').mean()
Out[315]:
        Father  Mother     Height  Kids
Family
1         78.5    67.0  70.100000     4
10        74.0    65.5  65.500000     1
100       69.0    66.0  70.733333     3
101       69.0    66.7  70.416667     6
102       69.0    66.0  66.166667     6
103       69.0    66.5  69.200000     5
104       69.5    66.5  66.625000     4
105       69.0    66.5  66.500000     6
106       69.5    66.0  68.500000     7
107       69.0    66.0  67.722222     9
108       69.0    65.0  65.571429     7
109       69.5    64.5  64.442857     7
11        74.0    62.0  67.312500     8
110       69.2    64.0  66.675000     4
112       69.0    63.0  66.666667     3
113       69.0    63.0  72.000000     1
114       69.0    63.0  67.500000     6
115       69.0    63.5  64.928571     7
116       69.0    63.5  65.733333     3
117       69.7    62.0  62.500000     1
118       69.5    62.0  71.333333     3
119       69.0    62.0  69.400000     5
12        74.0    61.0  65.000000     1
121       69.0    62.5  66.312500     8
122       69.0    62.0  68.000000     4
123       69.5    61.0  66.700000     5
124       69.0    61.0  64.555556     9
125       69.0    60.0  67.000000     3
126       69.0    60.0  64.300000     4
127       69.0    60.5  69.500000     1
...        ...     ...        ...   ...
71        70.0    65.0  66.666667     6
72        70.0    65.0  69.814286     7
73        70.0    65.0  70.166667     3
74        70.0    65.0  69.000000     2
75        70.0    64.7  67.414286     7
76        70.0    64.0  67.671429     7
77        70.0    64.0  67.550000     4
78        70.0    64.2  65.160000     5
79        70.5    64.0  68.375000     8
8         74.0    66.5  68.166667     3
80        70.5    64.5  60.000000     1
81        70.0    64.0  64.750000     4
82        70.0    64.0  68.555556     9
83        70.0    63.7  64.387500     8
85        70.5    63.0  67.400000     5
86        70.0    63.5  67.375000     4
87        70.0    63.0  65.175000     4
88        70.0    63.0  64.875000     4
89        70.5    62.0  67.625000     8
9         74.5    66.0  66.000000     1
90        70.3    62.7  66.500000     7
91        70.5    62.0  68.000000     3
92        70.0    61.0  69.100000     2
93        70.0    60.0  64.875000     4
94        70.0    60.0  65.000000     2
95        70.0    58.5  66.333333     3
96        70.0    58.0  66.400000     5
97        69.0    68.5  67.150000    10
98        69.0    67.0  64.000000     1
99        69.0    66.0  67.987500     8

[197 rows x 4 columns]

In [316]: gdf.groupby('Family').mean().mean()
Out[316]:
Father    69.349239
Mother    63.984264
Height    66.878310
Kids       4.563452
dtype: float64

In [317]: gdf.groupby('Family').mean().mean()['Father']
Out[317]: 69.34923857868021

In [318]: gdf.groupby('Family').mean()
Out[318]:
        Father  Mother     Height  Kids
Family
1         78.5    67.0  70.100000     4
10        74.0    65.5  65.500000     1
100       69.0    66.0  70.733333     3
101       69.0    66.7  70.416667     6
102       69.0    66.0  66.166667     6
103       69.0    66.5  69.200000     5
104       69.5    66.5  66.625000     4
105       69.0    66.5  66.500000     6
106       69.5    66.0  68.500000     7
107       69.0    66.0  67.722222     9
108       69.0    65.0  65.571429     7
109       69.5    64.5  64.442857     7
11        74.0    62.0  67.312500     8
110       69.2    64.0  66.675000     4
112       69.0    63.0  66.666667     3
113       69.0    63.0  72.000000     1
114       69.0    63.0  67.500000     6
115       69.0    63.5  64.928571     7
116       69.0    63.5  65.733333     3
117       69.7    62.0  62.500000     1
118       69.5    62.0  71.333333     3
119       69.0    62.0  69.400000     5
12        74.0    61.0  65.000000     1
121       69.0    62.5  66.312500     8
122       69.0    62.0  68.000000     4
123       69.5    61.0  66.700000     5
124       69.0    61.0  64.555556     9
125       69.0    60.0  67.000000     3
126       69.0    60.0  64.300000     4
127       69.0    60.5  69.500000     1
...        ...     ...        ...   ...
71        70.0    65.0  66.666667     6
72        70.0    65.0  69.814286     7
73        70.0    65.0  70.166667     3
74        70.0    65.0  69.000000     2
75        70.0    64.7  67.414286     7
76        70.0    64.0  67.671429     7
77        70.0    64.0  67.550000     4
78        70.0    64.2  65.160000     5
79        70.5    64.0  68.375000     8
8         74.0    66.5  68.166667     3
80        70.5    64.5  60.000000     1
81        70.0    64.0  64.750000     4
82        70.0    64.0  68.555556     9
83        70.0    63.7  64.387500     8
85        70.5    63.0  67.400000     5
86        70.0    63.5  67.375000     4
87        70.0    63.0  65.175000     4
88        70.0    63.0  64.875000     4
89        70.5    62.0  67.625000     8
9         74.5    66.0  66.000000     1
90        70.3    62.7  66.500000     7
91        70.5    62.0  68.000000     3
92        70.0    61.0  69.100000     2
93        70.0    60.0  64.875000     4
94        70.0    60.0  65.000000     2
95        70.0    58.5  66.333333     3
96        70.0    58.0  66.400000     5
97        69.0    68.5  67.150000    10
98        69.0    67.0  64.000000     1
99        69.0    66.0  67.987500     8

[197 rows x 4 columns]

In [319]: gdf.groupby('Family').mean()['Father']
Out[319]:
Family
1      78.5
10     74.0
100    69.0
101    69.0
102    69.0
103    69.0
104    69.5
105    69.0
106    69.5
107    69.0
108    69.0
109    69.5
11     74.0
110    69.2
112    69.0
113    69.0
114    69.0
115    69.0
116    69.0
117    69.7
118    69.5
119    69.0
12     74.0
121    69.0
122    69.0
123    69.5
124    69.0
125    69.0
126    69.0
127    69.0
       ...
71     70.0
72     70.0
73     70.0
74     70.0
75     70.0
76     70.0
77     70.0
78     70.0
79     70.5
8      74.0
80     70.5
81     70.0
82     70.0
83     70.0
85     70.5
86     70.0
87     70.0
88     70.0
89     70.5
9      74.5
90     70.3
91     70.5
92     70.0
93     70.0
94     70.0
95     70.0
96     70.0
97     69.0
98     69.0
99     69.0
Name: Father, Length: 197, dtype: float64

In [320]: gdf.groupby('Family').mean()['Father'].mean()
Out[320]: 69.3492385786802

In [321]: gdf.groupby('Family').mean().mean()['Father']
Out[321]: 69.34923857868021

In [322]: gdf.groupby('Family').mean()['Mother'].mean()
Out[322]: 63.98426395939087

In [323]: gdf.groupby('Family').mean()
Out[323]:
        Father  Mother     Height  Kids
Family
1         78.5    67.0  70.100000     4
10        74.0    65.5  65.500000     1
100       69.0    66.0  70.733333     3
101       69.0    66.7  70.416667     6
102       69.0    66.0  66.166667     6
103       69.0    66.5  69.200000     5
104       69.5    66.5  66.625000     4
105       69.0    66.5  66.500000     6
106       69.5    66.0  68.500000     7
107       69.0    66.0  67.722222     9
108       69.0    65.0  65.571429     7
109       69.5    64.5  64.442857     7
11        74.0    62.0  67.312500     8
110       69.2    64.0  66.675000     4
112       69.0    63.0  66.666667     3
113       69.0    63.0  72.000000     1
114       69.0    63.0  67.500000     6
115       69.0    63.5  64.928571     7
116       69.0    63.5  65.733333     3
117       69.7    62.0  62.500000     1
118       69.5    62.0  71.333333     3
119       69.0    62.0  69.400000     5
12        74.0    61.0  65.000000     1
121       69.0    62.5  66.312500     8
122       69.0    62.0  68.000000     4
123       69.5    61.0  66.700000     5
124       69.0    61.0  64.555556     9
125       69.0    60.0  67.000000     3
126       69.0    60.0  64.300000     4
127       69.0    60.5  69.500000     1
...        ...     ...        ...   ...
71        70.0    65.0  66.666667     6
72        70.0    65.0  69.814286     7
73        70.0    65.0  70.166667     3
74        70.0    65.0  69.000000     2
75        70.0    64.7  67.414286     7
76        70.0    64.0  67.671429     7
77        70.0    64.0  67.550000     4
78        70.0    64.2  65.160000     5
79        70.5    64.0  68.375000     8
8         74.0    66.5  68.166667     3
80        70.5    64.5  60.000000     1
81        70.0    64.0  64.750000     4
82        70.0    64.0  68.555556     9
83        70.0    63.7  64.387500     8
85        70.5    63.0  67.400000     5
86        70.0    63.5  67.375000     4
87        70.0    63.0  65.175000     4
88        70.0    63.0  64.875000     4
89        70.5    62.0  67.625000     8
9         74.5    66.0  66.000000     1
90        70.3    62.7  66.500000     7
91        70.5    62.0  68.000000     3
92        70.0    61.0  69.100000     2
93        70.0    60.0  64.875000     4
94        70.0    60.0  65.000000     2
95        70.0    58.5  66.333333     3
96        70.0    58.0  66.400000     5
97        69.0    68.5  67.150000    10
98        69.0    67.0  64.000000     1
99        69.0    66.0  67.987500     8

[197 rows x 4 columns]

In [324]: gdf.groupby('Family').mean().plot.scatter?
Object `plot.scatter` not found.

In [325]: gdf.plot.scatter?

In [326]: gdf.groupby('Family').mean().plot.scatter(x='Father', y='Mother')
Out[326]: <matplotlib.axes._subplots.AxesSubplot at 0x7fd6ecaa85f8>

In [327]: gdf.groupby('Family').mean().corr
Out[327]:
<bound method DataFrame.corr of         Father  Mother     Height  Kids
Family
1         78.5    67.0  70.100000     4
10        74.0    65.5  65.500000     1
100       69.0    66.0  70.733333     3
101       69.0    66.7  70.416667     6
102       69.0    66.0  66.166667     6
103       69.0    66.5  69.200000     5
104       69.5    66.5  66.625000     4
105       69.0    66.5  66.500000     6
106       69.5    66.0  68.500000     7
107       69.0    66.0  67.722222     9
108       69.0    65.0  65.571429     7
109       69.5    64.5  64.442857     7
11        74.0    62.0  67.312500     8
110       69.2    64.0  66.675000     4
112       69.0    63.0  66.666667     3
113       69.0    63.0  72.000000     1
114       69.0    63.0  67.500000     6
115       69.0    63.5  64.928571     7
116       69.0    63.5  65.733333     3
117       69.7    62.0  62.500000     1
118       69.5    62.0  71.333333     3
119       69.0    62.0  69.400000     5
12        74.0    61.0  65.000000     1
121       69.0    62.5  66.312500     8
122       69.0    62.0  68.000000     4
123       69.5    61.0  66.700000     5
124       69.0    61.0  64.555556     9
125       69.0    60.0  67.000000     3
126       69.0    60.0  64.300000     4
127       69.0    60.5  69.500000     1
...        ...     ...        ...   ...
71        70.0    65.0  66.666667     6
72        70.0    65.0  69.814286     7
73        70.0    65.0  70.166667     3
74        70.0    65.0  69.000000     2
75        70.0    64.7  67.414286     7
76        70.0    64.0  67.671429     7
77        70.0    64.0  67.550000     4
78        70.0    64.2  65.160000     5
79        70.5    64.0  68.375000     8
8         74.0    66.5  68.166667     3
80        70.5    64.5  60.000000     1
81        70.0    64.0  64.750000     4
82        70.0    64.0  68.555556     9
83        70.0    63.7  64.387500     8
85        70.5    63.0  67.400000     5
86        70.0    63.5  67.375000     4
87        70.0    63.0  65.175000     4
88        70.0    63.0  64.875000     4
89        70.5    62.0  67.625000     8
9         74.5    66.0  66.000000     1
90        70.3    62.7  66.500000     7
91        70.5    62.0  68.000000     3
92        70.0    61.0  69.100000     2
93        70.0    60.0  64.875000     4
94        70.0    60.0  65.000000     2
95        70.0    58.5  66.333333     3
96        70.0    58.0  66.400000     5
97        69.0    68.5  67.150000    10
98        69.0    67.0  64.000000     1
99        69.0    66.0  67.987500     8

[197 rows x 4 columns]>

In [328]: gdf.groupby('Family').mean().corr()
Out[328]:
          Father    Mother    Height      Kids
Father  1.000000  0.100606  0.334510 -0.076212
Mother  0.100606  1.000000  0.261300  0.074431
Height  0.334510  0.261300  1.000000 -0.082782
Kids   -0.076212  0.074431 -0.082782  1.000000

In [329]: gdf.groupby('Family').mean().corr()
Out[329]:
          Father    Mother    Height      Kids
Father  1.000000  0.100606  0.334510 -0.076212
Mother  0.100606  1.000000  0.261300  0.074431
Height  0.334510  0.261300  1.000000 -0.082782
Kids   -0.076212  0.074431 -0.082782  1.000000

In [330]: gdf.shape
Out[330]: (898, 6)

In [331]: gdf
Out[331]:
    Family  Father  Mother Gender  Height  Kids
0        1    78.5    67.0      M    73.2     4
1        1    78.5    67.0      F    69.2     4
2        1    78.5    67.0      F    69.0     4
3        1    78.5    67.0      F    69.0     4
4        2    75.5    66.5      M    73.5     4
5        2    75.5    66.5      M    72.5     4
6        2    75.5    66.5      F    65.5     4
7        2    75.5    66.5      F    65.5     4
8        3    75.0    64.0      M    71.0     2
9        3    75.0    64.0      F    68.0     2
10       4    75.0    64.0      M    70.5     5
11       4    75.0    64.0      M    68.5     5
12       4    75.0    64.0      F    67.0     5
13       4    75.0    64.0      F    64.5     5
14       4    75.0    64.0      F    63.0     5
15       5    75.0    58.5      M    72.0     6
16       5    75.0    58.5      M    69.0     6
17       5    75.0    58.5      M    68.0     6
18       5    75.0    58.5      F    66.5     6
19       5    75.0    58.5      F    62.5     6
20       5    75.0    58.5      F    62.5     6
21       6    74.0    68.0      F    69.5     1
22       7    74.0    68.0      M    76.5     6
23       7    74.0    68.0      M    74.0     6
24       7    74.0    68.0      M    73.0     6
25       7    74.0    68.0      M    73.0     6
26       7    74.0    68.0      F    70.5     6
27       7    74.0    68.0      F    64.0     6
28       8    74.0    66.5      F    70.5     3
29       8    74.0    66.5      F    68.0     3
..     ...     ...     ...    ...     ...   ...
868    198    64.0    64.0      M    71.5     7
869    198    64.0    64.0      M    68.0     7
870    198    64.0    64.0      F    65.5     7
871    198    64.0    64.0      F    64.0     7
872    198    64.0    64.0      F    62.0     7
873    198    64.0    64.0      F    62.0     7
874    198    64.0    64.0      F    61.0     7
875    199    64.0    64.0      M    70.5     7
876    199    64.0    64.0      M    68.0     7
877    199    64.0    64.0      F    67.0     7
878    199    64.0    64.0      F    65.0     7
879    199    64.0    64.0      F    64.0     7
880    199    64.0    64.0      F    64.0     7
881    199    64.0    64.0      F    60.0     7
882    200    64.0    63.0      M    64.5     1
883    201    64.0    60.0      M    66.0     2
884    201    64.0    60.0      F    60.0     2
885    203    62.0    66.0      M    64.0     3
886    203    62.0    66.0      F    62.0     3
887    203    62.0    66.0      F    61.0     3
888    204    62.5    63.0      M    66.5     2
889    204    62.5    63.0      F    57.0     2
890   136A    68.5    65.0      M    72.0     8
891   136A    68.5    65.0      M    70.5     8
892   136A    68.5    65.0      M    68.7     8
893   136A    68.5    65.0      M    68.5     8
894   136A    68.5    65.0      M    67.7     8
895   136A    68.5    65.0      F    64.0     8
896   136A    68.5    65.0      F    63.5     8
897   136A    68.5    65.0      F    63.0     8

[898 rows x 6 columns]

In [332]: df['Family']
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

TypeError: an integer is required

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   3062             try:
-> 3063                 return self._engine.get_loc(key)
   3064             except KeyError:

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

KeyError: 'Family'

During handling of the above exception, another exception occurred:

TypeError                                 Traceback (most recent call last)
pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.Int64HashTable.get_item()

TypeError: an integer is required

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-332-e8c24f265bfb> in <module>()
----> 1 df['Family']

/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py in __getitem__(self, key)
   2683             return self._getitem_multilevel(key)
   2684         else:
-> 2685             return self._getitem_column(key)
   2686
   2687     def _getitem_column(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py in _getitem_column(self, key)
   2690         # get column
   2691         if self.columns.is_unique:
-> 2692             return self._get_item_cache(key)
   2693
   2694         # duplicate columns & possible reduce dimensionality

/usr/local/lib/python3.5/dist-packages/pandas/core/generic.py in _get_item_cache(self, item)
   2484         res = cache.get(item)
   2485         if res is None:
-> 2486             values = self._data.get(item)
   2487             res = self._box_item_values(item, values)
   2488             cache[item] = res

/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py in get(self, item, fastpath)
   4113
   4114             if not isna(item):
-> 4115                 loc = self.items.get_loc(item)
   4116             else:
   4117                 indexer = np.arange(len(self.items))[isna(self.items)]

/usr/local/lib/python3.5/dist-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
   3063                 return self._engine.get_loc(key)
   3064             except KeyError:
-> 3065                 return self._engine.get_loc(self._maybe_cast_indexer(key))
   3066
   3067         indexer = self.get_indexer([key], method=method, tolerance=tolerance)

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()

KeyError: 'Family'
> /home/mspacek/SciPyCourse2018/notes/09_pandas/pandas/_libs/index.pyx(164)pandas._libs.index.IndexEngine.get_loc()

ipdb> c

In [333]: gdf['Family']
Out[333]:
0         1
1         1
2         1
3         1
4         2
5         2
6         2
7         2
8         3
9         3
10        4
11        4
12        4
13        4
14        4
15        5
16        5
17        5
18        5
19        5
20        5
21        6
22        7
23        7
24        7
25        7
26        7
27        7
28        8
29        8
       ...
868     198
869     198
870     198
871     198
872     198
873     198
874     198
875     199
876     199
877     199
878     199
879     199
880     199
881     199
882     200
883     201
884     201
885     203
886     203
887     203
888     204
889     204
890    136A
891    136A
892    136A
893    136A
894    136A
895    136A
896    136A
897    136A
Name: Family, Length: 898, dtype: object

In [334]: gdf.groupby('Family')
Out[334]: <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x7fd6eb37fbe0>

In [335]: gdf.groupby('Family').count()
Out[335]:
        Father  Mother  Gender  Height  Kids
Family
1            4       4       4       4     4
10           1       1       1       1     1
100          3       3       3       3     3
101          6       6       6       6     6
102          6       6       6       6     6
103          5       5       5       5     5
104          4       4       4       4     4
105          6       6       6       6     6
106          7       7       7       7     7
107          9       9       9       9     9
108          7       7       7       7     7
109          7       7       7       7     7
11           8       8       8       8     8
110          4       4       4       4     4
112          3       3       3       3     3
113          1       1       1       1     1
114          6       6       6       6     6
115          7       7       7       7     7
116          3       3       3       3     3
117          1       1       1       1     1
118          3       3       3       3     3
119          5       5       5       5     5
12           1       1       1       1     1
121          8       8       8       8     8
122          4       4       4       4     4
123          5       5       5       5     5
124          9       9       9       9     9
125          3       3       3       3     3
126          4       4       4       4     4
127          1       1       1       1     1
...        ...     ...     ...     ...   ...
71           6       6       6       6     6
72           7       7       7       7     7
73           3       3       3       3     3
74           2       2       2       2     2
75           7       7       7       7     7
76           7       7       7       7     7
77           4       4       4       4     4
78           5       5       5       5     5
79           8       8       8       8     8
8            3       3       3       3     3
80           1       1       1       1     1
81           4       4       4       4     4
82           9       9       9       9     9
83           8       8       8       8     8
85           5       5       5       5     5
86           4       4       4       4     4
87           4       4       4       4     4
88           4       4       4       4     4
89           8       8       8       8     8
9            1       1       1       1     1
90           7       7       7       7     7
91           3       3       3       3     3
92           2       2       2       2     2
93           4       4       4       4     4
94           2       2       2       2     2
95           3       3       3       3     3
96           5       5       5       5     5
97          10      10      10      10    10
98           1       1       1       1     1
99           8       8       8       8     8

[197 rows x 5 columns]

In [336]: gdf.groupby('Family').mean().count()
Out[336]:
Father    197
Mother    197
Height    197
Kids      197
dtype: int64

In [337]: gdf.groupby('Family').mean()
Out[337]:
        Father  Mother     Height  Kids
Family
1         78.5    67.0  70.100000     4
10        74.0    65.5  65.500000     1
100       69.0    66.0  70.733333     3
101       69.0    66.7  70.416667     6
102       69.0    66.0  66.166667     6
103       69.0    66.5  69.200000     5
104       69.5    66.5  66.625000     4
105       69.0    66.5  66.500000     6
106       69.5    66.0  68.500000     7
107       69.0    66.0  67.722222     9
108       69.0    65.0  65.571429     7
109       69.5    64.5  64.442857     7
11        74.0    62.0  67.312500     8
110       69.2    64.0  66.675000     4
112       69.0    63.0  66.666667     3
113       69.0    63.0  72.000000     1
114       69.0    63.0  67.500000     6
115       69.0    63.5  64.928571     7
116       69.0    63.5  65.733333     3
117       69.7    62.0  62.500000     1
118       69.5    62.0  71.333333     3
119       69.0    62.0  69.400000     5
12        74.0    61.0  65.000000     1
121       69.0    62.5  66.312500     8
122       69.0    62.0  68.000000     4
123       69.5    61.0  66.700000     5
124       69.0    61.0  64.555556     9
125       69.0    60.0  67.000000     3
126       69.0    60.0  64.300000     4
127       69.0    60.5  69.500000     1
...        ...     ...        ...   ...
71        70.0    65.0  66.666667     6
72        70.0    65.0  69.814286     7
73        70.0    65.0  70.166667     3
74        70.0    65.0  69.000000     2
75        70.0    64.7  67.414286     7
76        70.0    64.0  67.671429     7
77        70.0    64.0  67.550000     4
78        70.0    64.2  65.160000     5
79        70.5    64.0  68.375000     8
8         74.0    66.5  68.166667     3
80        70.5    64.5  60.000000     1
81        70.0    64.0  64.750000     4
82        70.0    64.0  68.555556     9
83        70.0    63.7  64.387500     8
85        70.5    63.0  67.400000     5
86        70.0    63.5  67.375000     4
87        70.0    63.0  65.175000     4
88        70.0    63.0  64.875000     4
89        70.5    62.0  67.625000     8
9         74.5    66.0  66.000000     1
90        70.3    62.7  66.500000     7
91        70.5    62.0  68.000000     3
92        70.0    61.0  69.100000     2
93        70.0    60.0  64.875000     4
94        70.0    60.0  65.000000     2
95        70.0    58.5  66.333333     3
96        70.0    58.0  66.400000     5
97        69.0    68.5  67.150000    10
98        69.0    67.0  64.000000     1
99        69.0    66.0  67.987500     8

[197 rows x 4 columns]

In [338]:
