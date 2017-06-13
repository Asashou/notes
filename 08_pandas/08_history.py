In [1]: import numpy as np

In [2]: import pandas as pd

In [3]: pd.Series?
Init signature: pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
Docstring:
One-dimensional ndarray with axis labels (including time series).

Labels need not be unique but must be any hashable type. The object
supports both integer- and label-based indexing and provides a host of
methods for performing operations involving the index. Statistical
methods from ndarray have been overridden to automatically exclude
missing data (currently represented as NaN)

Operations between Series (+, -, /, *, **) align values based on their
associated index values-- they need not be the same length. The result
index will be the sorted union of the two indexes.

Parameters
----------
data : array-like, dict, or scalar value
    Contains data stored in Series
index : array-like or Index (1d)
    Values must be unique and hashable, same length as data. Index
    object (or other iterable of same length as data) Will default to
    RangeIndex(len(data)) if not provided. If both a dict and index
    sequence are used, the index will override the keys found in the
    dict.
dtype : numpy.dtype or None
    If None, dtype will be inferred
copy : boolean, default False
    Copy input data
File:           /usr/local/lib/python3.5/dist-packages/pandas/core/series.py
Type:           type

In [4]: a = np.arange(10)

In [5]: a
Out[5]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [6]: a  = np.random.random(10)

In [7]: a
Out[7]:
array([ 0.79160646,  0.5110092 ,  0.00864628,  0.18793665,  0.37210977,
        0.83444054,  0.67052261,  0.64343563,  0.65243364,  0.40341656])

In [8]: a[0]
Out[8]: 0.79160645551955022

In [9]: a[1]
Out[9]: 0.51100920004138073

In [10]: fl = np.array(np.random.random(10))

In [11]: fl
Out[11]:
array([ 0.74228662,  0.78732836,  0.10613978,  0.1604254 ,  0.45066009,
        0.81383792,  0.79652715,  0.34367488,  0.39570216,  0.12279305])

In [12]: t = np.arange(0, 1, 0.1)

In [13]: t
Out[13]: array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])

In [14]: fl
Out[14]:
array([ 0.74228662,  0.78732836,  0.10613978,  0.1604254 ,  0.45066009,
        0.81383792,  0.79652715,  0.34367488,  0.39570216,  0.12279305])

In [15]: t
Out[15]: array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])

In [16]: fl[:5]
Out[16]: array([ 0.74228662,  0.78732836,  0.10613978,  0.1604254 ,  0.45066009])

In [17]: t[:5]
Out[17]: array([ 0. ,  0.1,  0.2,  0.3,  0.4])

In [18]: t == 0.2
Out[18]: array([False, False,  True, False, False, False, False, False, False, False], dtype=bool)

In [19]: idx = t == 0.2

In [20]: idx
Out[20]: array([False, False,  True, False, False, False, False, False, False, False], dtype=bool)

In [21]: fl[idx]
Out[21]: array([ 0.10613978])

In [22]: fl[idx][0]
Out[22]: 0.10613978148811931

In [23]: s = pd.Series(data=fl, index=t)

In [24]: s
Out[24]:
0.0    0.742287
0.1    0.787328
0.2    0.106140
0.3    0.160425
0.4    0.450660
0.5    0.813838
0.6    0.796527
0.7    0.343675
0.8    0.395702
0.9    0.122793
dtype: float64

In [25]: s.iloc[:5]
Out[25]:
0.0    0.742287
0.1    0.787328
0.2    0.106140
0.3    0.160425
0.4    0.450660
dtype: float64

In [26]: s[0.2]
Out[26]: 0.10613978148811931

In [27]: s_no_time = pd.Series(data=fl)

In [28]: s_no_time
Out[28]:
0    0.742287
1    0.787328
2    0.106140
3    0.160425
4    0.450660
5    0.813838
6    0.796527
7    0.343675
8    0.395702
9    0.122793
dtype: float64

In [29]: s[2]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.5/dist-packages/pandas/indexes/base.py in get_loc(self, key, method, tolerance)
   2133             try:
-> 2134                 return self._engine.get_loc(key)
   2135             except KeyError:

pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:4433)()

pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:4279)()

pandas/src/hashtable_class_helper.pxi in pandas.hashtable.Float64HashTable.get_item (pandas/hashtable.c:5131)()

pandas/src/hashtable_class_helper.pxi in pandas.hashtable.Float64HashTable.get_item (pandas/hashtable.c:5075)()

KeyError: 2.0

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-29-e6073c75a3db> in <module>()
----> 1 s[2]

/usr/local/lib/python3.5/dist-packages/pandas/core/series.py in __getitem__(self, key)
    601         key = com._apply_if_callable(key, self)
    602         try:
--> 603             result = self.index.get_value(self, key)
    604
    605             if not is_scalar(result):

/usr/local/lib/python3.5/dist-packages/pandas/indexes/numeric.py in get_value(self, series, key)
    283
    284         k = _values_from_object(key)
--> 285         loc = self.get_loc(k)
    286         new_values = _values_from_object(series)[loc]
    287

/usr/local/lib/python3.5/dist-packages/pandas/indexes/numeric.py in get_loc(self, key, method, tolerance)
    339             pass
    340         return super(Float64Index, self).get_loc(key, method=method,
--> 341                                                  tolerance=tolerance)
    342
    343     @property

/usr/local/lib/python3.5/dist-packages/pandas/indexes/base.py in get_loc(self, key, method, tolerance)
   2134                 return self._engine.get_loc(key)
   2135             except KeyError:
-> 2136                 return self._engine.get_loc(self._maybe_cast_indexer(key))
   2137
   2138         indexer = self.get_indexer([key], method=method, tolerance=tolerance)

pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:4433)()

pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:4279)()

pandas/src/hashtable_class_helper.pxi in pandas.hashtable.Float64HashTable.get_item (pandas/hashtable.c:5131)()

pandas/src/hashtable_class_helper.pxi in pandas.hashtable.Float64HashTable.get_item (pandas/hashtable.c:5075)()

KeyError: 2.0
> /home/mspacek/SciPyCourse2017/notes/08_pandas/pandas/src/hashtable_class_helper.pxi(193)pandas.hashtable.Float64HashTable.get_item (pandas/hashtable.c:5075)()

ipdb> c

In [30]: s.iloc[2]
Out[30]: 0.10613978148811931

In [31]: s
Out[31]:
0.0    0.742287
0.1    0.787328
0.2    0.106140
0.3    0.160425
0.4    0.450660
0.5    0.813838
0.6    0.796527
0.7    0.343675
0.8    0.395702
0.9    0.122793
dtype: float64

In [32]: s[0.3:0.7]
Out[32]:
0.3    0.160425
0.4    0.450660
0.5    0.813838
0.6    0.796527
dtype: float64

In [33]: s_no_time[0]
Out[33]: 0.7422866161653503

In [34]: s_no_time[2]
Out[34]: 0.10613978148811931

In [35]: s_no_time
Out[35]:
0    0.742287
1    0.787328
2    0.106140
3    0.160425
4    0.450660
5    0.813838
6    0.796527
7    0.343675
8    0.395702
9    0.122793
dtype: float64

In [36]: s[0.3:0.7]
Out[36]:
0.3    0.160425
0.4    0.450660
0.5    0.813838
0.6    0.796527
dtype: float64

In [37]: s[0.3:0.7].values
Out[37]: array([ 0.1604254 ,  0.45066009,  0.81383792,  0.79652715])

In [38]: s - 5
Out[38]:
0.0   -4.257713
0.1   -4.212672
0.2   -4.893860
0.3   -4.839575
0.4   -4.549340
0.5   -4.186162
0.6   -4.203473
0.7   -4.656325
0.8   -4.604298
0.9   -4.877207
dtype: float64

In [39]: s
Out[39]:
0.0    0.742287
0.1    0.787328
0.2    0.106140
0.3    0.160425
0.4    0.450660
0.5    0.813838
0.6    0.796527
0.7    0.343675
0.8    0.395702
0.9    0.122793
dtype: float64

In [40]: s - 5
Out[40]:
0.0   -4.257713
0.1   -4.212672
0.2   -4.893860
0.3   -4.839575
0.4   -4.549340
0.5   -4.186162
0.6   -4.203473
0.7   -4.656325
0.8   -4.604298
0.9   -4.877207
dtype: float64

In [41]: s.plot()
Out[41]: <matplotlib.axes._subplots.AxesSubplot at 0x7fb5d80c5390>

In [42]: s.plot.hist()
Out[42]: <matplotlib.axes._subplots.AxesSubplot at 0x7fb5d80c5390>

In [43]: s.plot.hist()
Out[43]: <matplotlib.axes._subplots.AxesSubplot at 0x7fb5d8040e48>

In [44]: s.plot.bar()
Out[44]: <matplotlib.axes._subplots.AxesSubplot at 0x7fb5d013bc50>

In [45]: s.plot.area()
Out[45]: <matplotlib.axes._subplots.AxesSubplot at 0x7fb5cff4f0b8>

In [46]: s.min()
Out[46]: 0.10613978148811931

In [47]: s
Out[47]:
0.0    0.742287
0.1    0.787328
0.2    0.106140
0.3    0.160425
0.4    0.450660
0.5    0.813838
0.6    0.796527
0.7    0.343675
0.8    0.395702
0.9    0.122793
dtype: float64

In [48]: s.max()
Out[48]: 0.81383791641456238

In [49]: s.sum()
Out[49]: 4.7193754037443627

In [50]: s.mean()
Out[50]: 0.47193754037443625

In [51]: s.median()
Out[51]: 0.42318112251408824

In [52]: s.std()
Out[52]: 0.29255195812519658

In [53]: s.describe()
Out[53]:
count    10.000000
mean      0.471938
std       0.292552
min       0.106140
25%       0.206238
50%       0.423181
75%       0.776068
max       0.813838
dtype: float64

In [54]: pd.date_range('2017-06-01', periods=10, freq='D')
Out[54]:
DatetimeIndex(['2017-06-01', '2017-06-02', '2017-06-03', '2017-06-04',
               '2017-06-05', '2017-06-06', '2017-06-07', '2017-06-08',
               '2017-06-09', '2017-06-10'],
              dtype='datetime64[ns]', freq='D')

In [55]: dr = pd.date_range('2017-06-01', periods=10, freq='D')

In [56]: s3 = pd.Series(data=fl, index=dr)

In [57]: s3
Out[57]:
2017-06-01    0.742287
2017-06-02    0.787328
2017-06-03    0.106140
2017-06-04    0.160425
2017-06-05    0.450660
2017-06-06    0.813838
2017-06-07    0.796527
2017-06-08    0.343675
2017-06-09    0.395702
2017-06-10    0.122793
Freq: D, dtype: float64

In [58]: t
Out[58]: array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])

In [59]: np.random.shuffle(t)

In [60]: t
Out[60]: array([ 0.2,  0.1,  0.4,  0.5,  0.6,  0.9,  0. ,  0.3,  0.7,  0.8])

In [61]: s4 = pd.Series(data=fl, index=t)

In [62]: s4
Out[62]:
0.2    0.742287
0.1    0.787328
0.4    0.106140
0.5    0.160425
0.6    0.450660
0.9    0.813838
0.0    0.796527
0.3    0.343675
0.7    0.395702
0.8    0.122793
dtype: float64

In [63]: s[0.2]
Out[63]: 0.10613978148811931

In [64]: s4[0.2]
Out[64]: 0.7422866161653503

In [65]: v = np.random.random((20, 3))

In [66]: v
Out[66]:
array([[ 0.49730577,  0.20314052,  0.02023168],
       [ 0.6958954 ,  0.10218326,  0.66885912],
       [ 0.22918995,  0.58923751,  0.53505365],
       [ 0.69013121,  0.2833932 ,  0.27418386],
       [ 0.22763881,  0.61396539,  0.68282642],
       [ 0.74121676,  0.70399633,  0.5757964 ],
       [ 0.6040567 ,  0.95569952,  0.68046772],
       [ 0.91150306,  0.62880385,  0.94177272],
       [ 0.44363229,  0.62957569,  0.95524697],
       [ 0.9717374 ,  0.7367783 ,  0.04466697],
       [ 0.11414409,  0.44985727,  0.41100664],
       [ 0.93464333,  0.74979538,  0.19108267],
       [ 0.54378179,  0.30825271,  0.72152318],
       [ 0.64874587,  0.4629518 ,  0.53414826],
       [ 0.65629762,  0.97637862,  0.01762579],
       [ 0.79421718,  0.4035798 ,  0.8247677 ],
       [ 0.43077003,  0.90816422,  0.97243312],
       [ 0.47501269,  0.45933676,  0.95493255],
       [ 0.11889175,  0.96818505,  0.57250044],
       [ 0.90205941,  0.47080667,  0.20803031]])

In [67]: t = np.arange(0, 20*50, 50)

In [68]: t
Out[68]:
array([  0,  50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600,
       650, 700, 750, 800, 850, 900, 950])

In [69]: v
Out[69]:
array([[ 0.49730577,  0.20314052,  0.02023168],
       [ 0.6958954 ,  0.10218326,  0.66885912],
       [ 0.22918995,  0.58923751,  0.53505365],
       [ 0.69013121,  0.2833932 ,  0.27418386],
       [ 0.22763881,  0.61396539,  0.68282642],
       [ 0.74121676,  0.70399633,  0.5757964 ],
       [ 0.6040567 ,  0.95569952,  0.68046772],
       [ 0.91150306,  0.62880385,  0.94177272],
       [ 0.44363229,  0.62957569,  0.95524697],
       [ 0.9717374 ,  0.7367783 ,  0.04466697],
       [ 0.11414409,  0.44985727,  0.41100664],
       [ 0.93464333,  0.74979538,  0.19108267],
       [ 0.54378179,  0.30825271,  0.72152318],
       [ 0.64874587,  0.4629518 ,  0.53414826],
       [ 0.65629762,  0.97637862,  0.01762579],
       [ 0.79421718,  0.4035798 ,  0.8247677 ],
       [ 0.43077003,  0.90816422,  0.97243312],
       [ 0.47501269,  0.45933676,  0.95493255],
       [ 0.11889175,  0.96818505,  0.57250044],
       [ 0.90205941,  0.47080667,  0.20803031]])

In [70]: t
Out[70]:
array([  0,  50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600,
       650, 700, 750, 800, 850, 900, 950])

In [71]: chans = ['Fz', 'Cz', 'Pz']

In [72]: df = pd.DataFrame(data=v, index=t, columns=chans)

In [73]: df
Out[73]:
           Fz        Cz        Pz
0    0.497306  0.203141  0.020232
50   0.695895  0.102183  0.668859
100  0.229190  0.589238  0.535054
150  0.690131  0.283393  0.274184
200  0.227639  0.613965  0.682826
250  0.741217  0.703996  0.575796
300  0.604057  0.955700  0.680468
350  0.911503  0.628804  0.941773
400  0.443632  0.629576  0.955247
450  0.971737  0.736778  0.044667
500  0.114144  0.449857  0.411007
550  0.934643  0.749795  0.191083
600  0.543782  0.308253  0.721523
650  0.648746  0.462952  0.534148
700  0.656298  0.976379  0.017626
750  0.794217  0.403580  0.824768
800  0.430770  0.908164  0.972433
850  0.475013  0.459337  0.954933
900  0.118892  0.968185  0.572500
950  0.902059  0.470807  0.208030

In [74]: v
Out[74]:
array([[ 0.49730577,  0.20314052,  0.02023168],
       [ 0.6958954 ,  0.10218326,  0.66885912],
       [ 0.22918995,  0.58923751,  0.53505365],
       [ 0.69013121,  0.2833932 ,  0.27418386],
       [ 0.22763881,  0.61396539,  0.68282642],
       [ 0.74121676,  0.70399633,  0.5757964 ],
       [ 0.6040567 ,  0.95569952,  0.68046772],
       [ 0.91150306,  0.62880385,  0.94177272],
       [ 0.44363229,  0.62957569,  0.95524697],
       [ 0.9717374 ,  0.7367783 ,  0.04466697],
       [ 0.11414409,  0.44985727,  0.41100664],
       [ 0.93464333,  0.74979538,  0.19108267],
       [ 0.54378179,  0.30825271,  0.72152318],
       [ 0.64874587,  0.4629518 ,  0.53414826],
       [ 0.65629762,  0.97637862,  0.01762579],
       [ 0.79421718,  0.4035798 ,  0.8247677 ],
       [ 0.43077003,  0.90816422,  0.97243312],
       [ 0.47501269,  0.45933676,  0.95493255],
       [ 0.11889175,  0.96818505,  0.57250044],
       [ 0.90205941,  0.47080667,  0.20803031]])

In [75]: df.iloc[:5]
Out[75]:
           Fz        Cz        Pz
0    0.497306  0.203141  0.020232
50   0.695895  0.102183  0.668859
100  0.229190  0.589238  0.535054
150  0.690131  0.283393  0.274184
200  0.227639  0.613965  0.682826

In [76]: df.iloc[0, 0]
Out[76]: 0.4973057684037856

In [77]: df.iloc[-1, -1]
Out[77]: 0.2080303134286382

In [78]: df
Out[78]:
           Fz        Cz        Pz
0    0.497306  0.203141  0.020232
50   0.695895  0.102183  0.668859
100  0.229190  0.589238  0.535054
150  0.690131  0.283393  0.274184
200  0.227639  0.613965  0.682826
250  0.741217  0.703996  0.575796
300  0.604057  0.955700  0.680468
350  0.911503  0.628804  0.941773
400  0.443632  0.629576  0.955247
450  0.971737  0.736778  0.044667
500  0.114144  0.449857  0.411007
550  0.934643  0.749795  0.191083
600  0.543782  0.308253  0.721523
650  0.648746  0.462952  0.534148
700  0.656298  0.976379  0.017626
750  0.794217  0.403580  0.824768
800  0.430770  0.908164  0.972433
850  0.475013  0.459337  0.954933
900  0.118892  0.968185  0.572500
950  0.902059  0.470807  0.208030

In [79]: df['Fz']
Out[79]:
0      0.497306
50     0.695895
100    0.229190
150    0.690131
200    0.227639
250    0.741217
300    0.604057
350    0.911503
400    0.443632
450    0.971737
500    0.114144
550    0.934643
600    0.543782
650    0.648746
700    0.656298
750    0.794217
800    0.430770
850    0.475013
900    0.118892
950    0.902059
Name: Fz, dtype: float64

In [80]: type(df['Fz'])
Out[80]: pandas.core.series.Series

In [81]: df['Fz']
Out[81]:
0      0.497306
50     0.695895
100    0.229190
150    0.690131
200    0.227639
250    0.741217
300    0.604057
350    0.911503
400    0.443632
450    0.971737
500    0.114144
550    0.934643
600    0.543782
650    0.648746
700    0.656298
750    0.794217
800    0.430770
850    0.475013
900    0.118892
950    0.902059
Name: Fz, dtype: float64

In [82]: df.Fz
Out[82]:
0      0.497306
50     0.695895
100    0.229190
150    0.690131
200    0.227639
250    0.741217
300    0.604057
350    0.911503
400    0.443632
450    0.971737
500    0.114144
550    0.934643
600    0.543782
650    0.648746
700    0.656298
750    0.794217
800    0.430770
850    0.475013
900    0.118892
950    0.902059
Name: Fz, dtype: float64

In [83]: df
Out[83]:
           Fz        Cz        Pz
0    0.497306  0.203141  0.020232
50   0.695895  0.102183  0.668859
100  0.229190  0.589238  0.535054
150  0.690131  0.283393  0.274184
200  0.227639  0.613965  0.682826
250  0.741217  0.703996  0.575796
300  0.604057  0.955700  0.680468
350  0.911503  0.628804  0.941773
400  0.443632  0.629576  0.955247
450  0.971737  0.736778  0.044667
500  0.114144  0.449857  0.411007
550  0.934643  0.749795  0.191083
600  0.543782  0.308253  0.721523
650  0.648746  0.462952  0.534148
700  0.656298  0.976379  0.017626
750  0.794217  0.403580  0.824768
800  0.430770  0.908164  0.972433
850  0.475013  0.459337  0.954933
900  0.118892  0.968185  0.572500
950  0.902059  0.470807  0.208030

In [84]: df.loc[450]
Out[84]:
Fz    0.971737
Cz    0.736778
Pz    0.044667
Name: 450, dtype: float64

In [85]: df['Fz']
Out[85]:
0      0.497306
50     0.695895
100    0.229190
150    0.690131
200    0.227639
250    0.741217
300    0.604057
350    0.911503
400    0.443632
450    0.971737
500    0.114144
550    0.934643
600    0.543782
650    0.648746
700    0.656298
750    0.794217
800    0.430770
850    0.475013
900    0.118892
950    0.902059
Name: Fz, dtype: float64

In [86]: df.loc[450]
Out[86]:
Fz    0.971737
Cz    0.736778
Pz    0.044667
Name: 450, dtype: float64

In [87]: df['Fz'][450]
Out[87]: 0.97173740304799272

In [88]: df
Out[88]:
           Fz        Cz        Pz
0    0.497306  0.203141  0.020232
50   0.695895  0.102183  0.668859
100  0.229190  0.589238  0.535054
150  0.690131  0.283393  0.274184
200  0.227639  0.613965  0.682826
250  0.741217  0.703996  0.575796
300  0.604057  0.955700  0.680468
350  0.911503  0.628804  0.941773
400  0.443632  0.629576  0.955247
450  0.971737  0.736778  0.044667
500  0.114144  0.449857  0.411007
550  0.934643  0.749795  0.191083
600  0.543782  0.308253  0.721523
650  0.648746  0.462952  0.534148
700  0.656298  0.976379  0.017626
750  0.794217  0.403580  0.824768
800  0.430770  0.908164  0.972433
850  0.475013  0.459337  0.954933
900  0.118892  0.968185  0.572500
950  0.902059  0.470807  0.208030

In [89]: df.loc[450]['Fz']
Out[89]: 0.97173740304799272

In [90]: a = np.random.random(10)

In [91]: v = np.random.random(20, 3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-91-a0e983186e06> in <module>()
----> 1 v = np.random.random(20, 3)

mtrand.pyx in mtrand.RandomState.random_sample (numpy/random/mtrand/mtrand.c:15497)()

TypeError: random_sample() takes at most 1 positional argument (2 given)
> /home/mspacek/SciPyCourse2017/notes/08_pandas/mtrand.pyx(814)mtrand.RandomState.random_sample (numpy/random/mtrand/mtrand.c:15497)()

ipdb> c

In [92]: np.random.random?

In [93]: df
Out[93]:
           Fz        Cz        Pz
0    0.497306  0.203141  0.020232
50   0.695895  0.102183  0.668859
100  0.229190  0.589238  0.535054
150  0.690131  0.283393  0.274184
200  0.227639  0.613965  0.682826
250  0.741217  0.703996  0.575796
300  0.604057  0.955700  0.680468
350  0.911503  0.628804  0.941773
400  0.443632  0.629576  0.955247
450  0.971737  0.736778  0.044667
500  0.114144  0.449857  0.411007
550  0.934643  0.749795  0.191083
600  0.543782  0.308253  0.721523
650  0.648746  0.462952  0.534148
700  0.656298  0.976379  0.017626
750  0.794217  0.403580  0.824768
800  0.430770  0.908164  0.972433
850  0.475013  0.459337  0.954933
900  0.118892  0.968185  0.572500
950  0.902059  0.470807  0.208030

In [94]: exp1 = pd.read_csv('exp1.csv')

In [95]: exp1
Out[95]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [96]: exp1.subject
Out[96]:
0    A01
1    A01
2    A01
3    A01
4    A01
5    A01
6    A01
7    A01
Name: subject, dtype: object

In [97]: exp1.subject[0]
Out[97]: 'A01'

In [98]: type(exp1.subject[0])
Out[98]: str

In [99]: exp1
Out[99]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [100]: exp1.plot()
Out[100]: <matplotlib.axes._subplots.AxesSubplot at 0x7fb5f6b6f0f0>

In [101]: exp.plot.hist()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-101-4609877227d9> in <module>()
----> 1 exp.plot.hist()

NameError: name 'exp' is not defined
> <ipython-input-101-4609877227d9>(1)<module>()
----> 1 exp.plot.hist()

ipdb> c

In [102]: exp1.plot.hist()
Out[102]: <matplotlib.axes._subplots.AxesSubplot at 0x7fb5f6aec940>

In [103]: exp1.hist()
Out[103]:
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7fb5f68c6470>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x7fb5f6731940>]], dtype=object)

In [104]: exp1 = pd.read_csv('exp1.csv')

In [105]: exp2 = pd.read_csv('exp2.csv')

In [106]: exp2
Out[106]:
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

In [107]: pd.concat([exp1, exp2])
Out[107]:
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

In [108]: exps = pd.concat([exp1, exp2])

In [109]: exps
Out[109]:
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

In [110]: exps[0]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/usr/local/lib/python3.5/dist-packages/pandas/indexes/base.py in get_loc(self, key, method, tolerance)
   2133             try:
-> 2134                 return self._engine.get_loc(key)
   2135             except KeyError:

pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:4433)()

pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:4279)()

pandas/src/hashtable_class_helper.pxi in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13742)()

pandas/src/hashtable_class_helper.pxi in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13696)()

KeyError: 0

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-110-71bd84907e37> in <module>()
----> 1 exps[0]

/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py in __getitem__(self, key)
   2057             return self._getitem_multilevel(key)
   2058         else:
-> 2059             return self._getitem_column(key)
   2060
   2061     def _getitem_column(self, key):

/usr/local/lib/python3.5/dist-packages/pandas/core/frame.py in _getitem_column(self, key)
   2064         # get column
   2065         if self.columns.is_unique:
-> 2066             return self._get_item_cache(key)
   2067
   2068         # duplicate columns & possible reduce dimensionality

/usr/local/lib/python3.5/dist-packages/pandas/core/generic.py in _get_item_cache(self, item)
   1384         res = cache.get(item)
   1385         if res is None:
-> 1386             values = self._data.get(item)
   1387             res = self._box_item_values(item, values)
   1388             cache[item] = res

/usr/local/lib/python3.5/dist-packages/pandas/core/internals.py in get(self, item, fastpath)
   3541
   3542             if not isnull(item):
-> 3543                 loc = self.items.get_loc(item)
   3544             else:
   3545                 indexer = np.arange(len(self.items))[isnull(self.items)]

/usr/local/lib/python3.5/dist-packages/pandas/indexes/base.py in get_loc(self, key, method, tolerance)
   2134                 return self._engine.get_loc(key)
   2135             except KeyError:
-> 2136                 return self._engine.get_loc(self._maybe_cast_indexer(key))
   2137
   2138         indexer = self.get_indexer([key], method=method, tolerance=tolerance)

pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:4433)()

pandas/index.pyx in pandas.index.IndexEngine.get_loc (pandas/index.c:4279)()

pandas/src/hashtable_class_helper.pxi in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13742)()

pandas/src/hashtable_class_helper.pxi in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13696)()

KeyError: 0
> /home/mspacek/SciPyCourse2017/notes/08_pandas/pandas/src/hashtable_class_helper.pxi(740)pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13696)()

ipdb> c

In [111]: exps
Out[111]:
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

In [112]: exps.loc[0]
Out[112]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
0     A02         2.7       5.6        L    pass

In [113]: exps.plot.scatter('start_time', 'end_time')
Out[113]: <matplotlib.axes._subplots.AxesSubplot at 0x7fb5ceb00898>

In [114]: exps.corr()
Out[114]:
            start_time  end_time
start_time    1.000000  0.841829
end_time      0.841829  1.000000

In [115]: exps
Out[115]:
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

In [116]: exps.sort_values('start_time')
Out[116]:
   subject  start_time  end_time stimulus outcome
5      A01         0.7       6.1        L    pass
8      A02         0.8       4.1        L    pass
1      A02         1.2       4.3        L    pass
7      A02         1.3       3.1        R    pass
1      A01         1.6       2.1        R    pass
3      A02         2.3       5.6        R    pass
0      A01         2.3       5.6        L    pass
2      A01         2.3       5.6        R    pass
7      A01         2.7       5.6        L    pass
0      A02         2.7       5.6        L    pass
4      A01         2.8       4.5        L    pass
6      A02         2.8       4.5        L    pass
6      A01         3.5      11.2        R    fail
9      A02         3.6      12.4        R    fail
5      A02         3.9      12.1        R    fail
2      A02         4.0      10.4        R    fail
3      A01         4.0      10.2        R    fail
4      A02         4.1      10.0        R    fail
10     A02         5.5      13.3        R    fail

In [117]: exps[['stimulus', 'outcome']]
Out[117]:
   stimulus outcome
0         L    pass
1         R    pass
2         R    pass
3         R    fail
4         L    pass
5         L    pass
6         R    fail
7         L    pass
0         L    pass
1         L    pass
2         R    fail
3         R    pass
4         R    fail
5         R    fail
6         L    pass
7         R    pass
8         L    pass
9         R    fail
10        R    fail

In [118]: exps.loc[[8, 10]]
Out[118]:
   subject  start_time  end_time stimulus outcome
8      A02         0.8       4.1        L    pass
10     A02         5.5      13.3        R    fail

In [119]: pd.read_excel('exp.xlsx', sheetname='exp1')
Out[119]:
  subject  start_time  end_time stimulus outcome
0     A01         2.3       5.6        L    pass
1     A01         1.6       2.1        R    pass
2     A01         2.3       5.6        R    pass
3     A01         4.0      10.2        R    fail
4     A01         2.8       4.5        L    pass
5     A01         0.7       6.1        L    pass
6     A01         3.5      11.2        R    fail
7     A01         2.7       5.6        L    pass

In [120]: import xlrd

In [121]: xlrd
Out[121]: <module 'xlrd' from '/usr/local/lib/python3.5/dist-packages/xlrd/__init__.py'>

In [122]: exp1 = pd.read_excel('exp.xlsx', sheetname='exp1')

In [123]: exp2 = pd.read_excel('exp.xlsx', sheetname='exp2')

In [124]: exp2
Out[124]:
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

In [125]: exp2.to_csv?

In [126]: exp2.to_excel?

In [127]: exps
Out[127]:
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

In [128]: exps.min()
Out[128]:
subject        A01
start_time     0.7
end_time       2.1
stimulus         L
outcome       fail
dtype: object

In [129]: exps.max()
Out[129]:
subject        A02
start_time     5.5
end_time      13.3
stimulus         R
outcome       pass
dtype: object

In [130]: exps.mean()
Out[130]:
start_time    2.742105
end_time      7.173684
dtype: float64

In [131]: exps.describe()
Out[131]:
       start_time   end_time
count   19.000000  19.000000
mean     2.742105   7.173684
std      1.281629   3.502038
min      0.700000   2.100000
25%      1.950000   4.500000
50%      2.700000   5.600000
75%      3.750000  10.300000
max      5.500000  13.300000

In [132]: type(exps.describe())
Out[132]: pandas.core.frame.DataFrame

In [133]: exps
Out[133]:
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

In [134]: exps.start_time
Out[134]:
0     2.3
1     1.6
2     2.3
3     4.0
4     2.8
5     0.7
6     3.5
7     2.7
0     2.7
1     1.2
2     4.0
3     2.3
4     4.1
5     3.9
6     2.8
7     1.3
8     0.8
9     3.6
10    5.5
Name: start_time, dtype: float64

In [135]: exps.subject
Out[135]:
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

In [136]: exps.subject.nunique()
Out[136]: 2

In [137]: exps.stimulus.nunique()
Out[137]: 2

In [138]: exps.outcome.nunique()
Out[138]: 2

In [139]: exps
Out[139]:
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

In [140]: exps.groupby
Out[140]:
<bound method NDFrame.groupby of    subject  start_time  end_time stimulus outcome
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
10     A02         5.5      13.3        R    fail>

In [141]: exps.groupby?

In [142]: exps.groupby('subject')
Out[142]: <pandas.core.groupby.DataFrameGroupBy object at 0x7fb5ce865630>

In [143]: exps.groupby('subject').mean()
Out[143]:
         start_time  end_time
subject
A01        2.487500  6.362500
A02        2.927273  7.763636

In [144]: exps.groupby('outcome').mean()
Out[144]:
         start_time   end_time
outcome
fail       4.085714  11.371429
pass       1.958333   4.725000

In [145]: exps.groupby('outcome').max()
Out[145]:
        subject  start_time  end_time stimulus
outcome
fail        A02         5.5      13.3        R
pass        A02         2.8       6.1        R

In [146]: exps.groupby('outcome').describe()
Out[146]:
                end_time  start_time
outcome
fail    count   7.000000    7.000000
        mean   11.371429    4.085714
        std     1.260574    0.661888
        min    10.000000    3.500000
        25%    10.300000    3.750000
        50%    11.200000    4.000000
        75%    12.250000    4.050000
        max    13.300000    5.500000
pass    count  12.000000   12.000000
        mean    4.725000    1.958333
        std     1.203121    0.793678
        min     2.100000    0.700000
        25%     4.250000    1.275000
        50%     5.050000    2.300000
        75%     5.600000    2.700000
        max     6.100000    2.800000

In [147]: exps.groupby('subject').describe()
Out[147]:
                end_time  start_time
subject
A01     count   8.000000    8.000000
        mean    6.362500    2.487500
        std     2.965968    1.035702
        min     2.100000    0.700000
        25%     5.325000    2.125000
        50%     5.600000    2.500000
        75%     7.125000    2.975000
        max    11.200000    4.000000
A02     count  11.000000   11.000000
        mean    7.763636    2.927273
        std     3.874086    1.454710
        min     3.100000    0.800000
        25%     4.400000    1.800000
        50%     5.600000    2.800000
        75%    11.250000    3.950000
        max    13.300000    5.500000

In [148]: exps.groupby('start_time').mean()
Out[148]:
            end_time
start_time
0.7              6.1
0.8              4.1
1.2              4.3
1.3              3.1
1.6              2.1
2.3              5.6
2.7              5.6
2.8              4.5
3.5             11.2
3.6             12.4
3.9             12.1
4.0             10.3
4.1             10.0
5.5             13.3

In [149]: exps.groupby?

In [150]: exps.groupby(['subject', 'outcome'])
Out[150]: <pandas.core.groupby.DataFrameGroupBy object at 0x7fb5ce886ba8>

In [151]: exps.groupby(['subject', 'outcome']).mean()
Out[151]:
                 start_time   end_time
subject outcome
A01     fail       3.750000  10.700000
        pass       2.066667   4.916667
A02     fail       4.220000  11.640000
        pass       1.850000   4.533333

In [152]: exps
Out[152]:
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

In [153]: s
Out[153]:
0.2    0.742287
0.1    0.787328
0.4    0.106140
0.5    0.160425
0.6    0.450660
0.9    0.813838
0.0    0.796527
0.3    0.343675
0.7    0.395702
0.8    0.122793
dtype: float64

In [154]: s.values
Out[154]:
array([ 0.74228662,  0.78732836,  0.10613978,  0.1604254 ,  0.45066009,
        0.81383792,  0.79652715,  0.34367488,  0.39570216,  0.12279305])

In [155]: exps.values
Out[155]:
array([['A01', 2.3, 5.6, 'L', 'pass'],
       ['A01', 1.6, 2.1, 'R', 'pass'],
       ['A01', 2.3, 5.6, 'R', 'pass'],
       ['A01', 4.0, 10.2, 'R', 'fail'],
       ['A01', 2.8, 4.5, 'L', 'pass'],
       ['A01', 0.7, 6.1, 'L', 'pass'],
       ['A01', 3.5, 11.2, 'R', 'fail'],
       ['A01', 2.7, 5.6, 'L', 'pass'],
       ['A02', 2.7, 5.6, 'L', 'pass'],
       ['A02', 1.2, 4.3, 'L', 'pass'],
       ['A02', 4.0, 10.4, 'R', 'fail'],
       ['A02', 2.3, 5.6, 'R', 'pass'],
       ['A02', 4.1, 10.0, 'R', 'fail'],
       ['A02', 3.9, 12.1, 'R', 'fail'],
       ['A02', 2.8, 4.5, 'L', 'pass'],
       ['A02', 1.3, 3.1, 'R', 'pass'],
       ['A02', 0.8, 4.1, 'L', 'pass'],
       ['A02', 3.6, 12.4, 'R', 'fail'],
       ['A02', 5.5, 13.3, 'R', 'fail']], dtype=object)

In [156]: exps
Out[156]:
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

In [157]: exps['start_time']
Out[157]:
0     2.3
1     1.6
2     2.3
3     4.0
4     2.8
5     0.7
6     3.5
7     2.7
0     2.7
1     1.2
2     4.0
3     2.3
4     4.1
5     3.9
6     2.8
7     1.3
8     0.8
9     3.6
10    5.5
Name: start_time, dtype: float64

In [158]: exps['start_time'].values
Out[158]:
array([ 2.3,  1.6,  2.3,  4. ,  2.8,  0.7,  3.5,  2.7,  2.7,  1.2,  4. ,
        2.3,  4.1,  3.9,  2.8,  1.3,  0.8,  3.6,  5.5])

In [159]: exps['start_time'].values
Out[159]:
array([ 2.3,  1.6,  2.3,  4. ,  2.8,  0.7,  3.5,  2.7,  2.7,  1.2,  4. ,
        2.3,  4.1,  3.9,  2.8,  1.3,  0.8,  3.6,  5.5])

In [160]: exps['start_time']
Out[160]:
0     2.3
1     1.6
2     2.3
3     4.0
4     2.8
5     0.7
6     3.5
7     2.7
0     2.7
1     1.2
2     4.0
3     2.3
4     4.1
5     3.9
6     2.8
7     1.3
8     0.8
9     3.6
10    5.5
Name: start_time, dtype: float64

In [161]: exps['start_time'].values
Out[161]:
array([ 2.3,  1.6,  2.3,  4. ,  2.8,  0.7,  3.5,  2.7,  2.7,  1.2,  4. ,
        2.3,  4.1,  3.9,  2.8,  1.3,  0.8,  3.6,  5.5])

In [162]:

In [162]:

In [162]:

In [162]:

In [162]:

In [162]:

In [162]: [[1, 2, 3],
     ...:  [4, 6],
     ...:  [7, 8, 9]]
Out[162]: [[1, 2, 3], [4, 6], [7, 8, 9]]

In [163]: missd = [[1, 2, 3],
     ...:  [4, 6],
     ...:  [7, 8, 9]]

In [164]: missd
Out[164]: [[1, 2, 3], [4, 6], [7, 8, 9]]

In [165]: len(missd)
Out[165]: 3

In [166]: np.array(missd)
Out[166]: array([[1, 2, 3], [4, 6], [7, 8, 9]], dtype=object)

In [167]: np.array(missd).ndim
Out[167]: 1

In [168]: np.array(missd).shape
Out[168]: (3,)

In [169]: [[1, 2, 3],
     ...:  [4, np.nan, 6],
     ...:  [7, 8, 9]]
Out[169]: [[1, 2, 3], [4, nan, 6], [7, 8, 9]]

In [170]: nand = [[1, 2, 3],
     ...:  [4, np.nan, 6],
     ...:  [7, 8, 9]]

In [171]: np.array(nand)
Out[171]:
array([[  1.,   2.,   3.],
       [  4.,  nan,   6.],
       [  7.,   8.,   9.]])

In [172]: np.array(nand).dtype
Out[172]: dtype('float64')

In [173]: nand
Out[173]: [[1, 2, 3], [4, nan, 6], [7, 8, 9]]

In [174]: 5.6
Out[174]: 5.6

In [175]: missd
Out[175]: [[1, 2, 3], [4, 6], [7, 8, 9]]

In [176]: pd.DataFrame(missd)
Out[176]:
   0  1    2
0  1  2  3.0
1  4  6  NaN
2  7  8  9.0

In [177]: pd.DataFrame(missd).iloc[0, 0]
Out[177]: 1.0

In [178]: nand
Out[178]: [[1, 2, 3], [4, nan, 6], [7, 8, 9]]

In [179]: pd.DataFrame(nand)
Out[179]:
   0    1  2
0  1  2.0  3
1  4  NaN  6
2  7  8.0  9

In [180]: pd.DataFrame(nand)[1]
Out[180]:
0    2.0
1    NaN
2    8.0
Name: 1, dtype: float64

In [181]: pd.DataFrame(nand)[1].mean()
Out[181]: 5.0

In [182]:
