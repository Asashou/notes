In [2]: import matplotlib.pyplot as plt

In [3]: plt.plot()
Out[3]: []

In [4]: plt.ion()

In [5]: import matplotlib.pyplot as plt

In [6]: t = linspace(0, 4*np.pi, 100)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-5ffa27f728e5> in <module>()
----> 1 t = linspace(0, 4*np.pi, 100)

NameError: name 'linspace' is not defined
> <ipython-input-6-5ffa27f728e5>(1)<module>()
----> 1 t = linspace(0, 4*np.pi, 100)

ipdb> c

In [7]: t = np.linspace(0, 4*np.pi, 100)

In [8]: t
Out[8]:
array([  0.        ,   0.12693304,   0.25386607,   0.38079911,
         0.50773215,   0.63466518,   0.76159822,   0.88853126,
         1.01546429,   1.14239733,   1.26933037,   1.3962634 ,
         1.52319644,   1.65012947,   1.77706251,   1.90399555,
         2.03092858,   2.15786162,   2.28479466,   2.41172769,
         2.53866073,   2.66559377,   2.7925268 ,   2.91945984,
         3.04639288,   3.17332591,   3.30025895,   3.42719199,
         3.55412502,   3.68105806,   3.8079911 ,   3.93492413,
         4.06185717,   4.1887902 ,   4.31572324,   4.44265628,
         4.56958931,   4.69652235,   4.82345539,   4.95038842,
         5.07732146,   5.2042545 ,   5.33118753,   5.45812057,
         5.58505361,   5.71198664,   5.83891968,   5.96585272,
         6.09278575,   6.21971879,   6.34665183,   6.47358486,
         6.6005179 ,   6.72745093,   6.85438397,   6.98131701,
         7.10825004,   7.23518308,   7.36211612,   7.48904915,
         7.61598219,   7.74291523,   7.86984826,   7.9967813 ,
         8.12371434,   8.25064737,   8.37758041,   8.50451345,
         8.63144648,   8.75837952,   8.88531256,   9.01224559,
         9.13917863,   9.26611167,   9.3930447 ,   9.51997774,
         9.64691077,   9.77384381,   9.90077685,  10.02770988,
        10.15464292,  10.28157596,  10.40850899,  10.53544203,
        10.66237507,  10.7893081 ,  10.91624114,  11.04317418,
        11.17010721,  11.29704025,  11.42397329,  11.55090632,
        11.67783936,  11.8047724 ,  11.93170543,  12.05863847,
        12.1855715 ,  12.31250454,  12.43943758,  12.56637061])

In [9]: s = np.sin(t)

In [10]: c = np.cost(t)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-10-e5bee056b802> in <module>()
----> 1 c = np.cost(t)

AttributeError: module 'numpy' has no attribute 'cost'
> <ipython-input-10-e5bee056b802>(1)<module>()
----> 1 c = np.cost(t)

ipdb> c

In [11]: c = np.cos(t)

In [12]: plt.plot(t, s)
Out[12]: [<matplotlib.lines.Line2D at 0x7fc880c1cb00>]

In [13]: plt.plot(t, s)
Out[13]: [<matplotlib.lines.Line2D at 0x7fc880b75e48>]

In [14]: plt.plot(t, c)
Out[14]: [<matplotlib.lines.Line2D at 0x7fc880b98f60>]

In [15]: plt.subplots?

In [16]: f, ax = plt.subplots()

In [17]: f
Out[17]: <matplotlib.figure.Figure at 0x7fc880b578d0>

In [18]: ax
Out[18]: <matplotlib.axes._subplots.AxesSubplot at 0x7fc880b5e240>

In [19]: ax.plot(t, s)
Out[19]: [<matplotlib.lines.Line2D at 0x7fc896641ef0>]

In [20]: ax.set_xlim(-2, 5)
Out[20]: (-2, 5)

In [21]: ax.set_ylim(-2, 2)
Out[21]: (-2, 2)

In [22]: ax.legend()
/usr/local/lib/python3.5/dist-packages/matplotlib/axes/_axes.py:545: UserWarning: No labelled objects found. Use label='...' kwarg on individual plots.
  warnings.warn("No labelled objects found. "

In [23]: f, ax = plt.subplots()

In [24]: ax.spines
Out[24]:
OrderedDict([('left', <matplotlib.spines.Spine at 0x7fc8964b0c18>),
             ('right', <matplotlib.spines.Spine at 0x7fc896457080>),
             ('bottom', <matplotlib.spines.Spine at 0x7fc896457208>),
             ('top', <matplotlib.spines.Spine at 0x7fc896457390>)])

In [25]: ax.spines['right']
Out[25]: <matplotlib.spines.Spine at 0x7fc896457080>

In [26]: ax.spines['right'].set_visible(False)

In [27]: ax.spines['top'].set_visible(False)

In [28]: ax.plot(t, s)
Out[28]: [<matplotlib.lines.Line2D at 0x7fc8965f6908>]

In [29]: f, axs = plt.subplots(nrows=2, ncols=2)

In [30]: axs
Out[30]:
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7fc8965b09b0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x7fc896573278>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x7fc8966738d0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x7fc89657f4a8>]], dtype=object)

In [31]: axs[0, 0]
Out[31]: <matplotlib.axes._subplots.AxesSubplot at 0x7fc8965b09b0>

In [32]: axs[0, 1].plot(t, s)
Out[32]: [<matplotlib.lines.Line2D at 0x7fc8960f4ba8>]

In [33]: axs[1, 0].plot(t, c, color='r')
Out[33]: [<matplotlib.lines.Line2D at 0x7fc896109a90>]

In [34]: f, axs = plt.subplots(2, 1, sharex=True, sharey=False)

In [35]: axs[0]
Out[35]: <matplotlib.axes._subplots.AxesSubplot at 0x7fc895f57b70>

In [36]: axs[0].plot(t, s)
Out[36]: [<matplotlib.lines.Line2D at 0x7fc895f03518>]

In [37]: axs[1].plot(t, c, color='red')
Out[37]: [<matplotlib.lines.Line2D at 0x7fc88142a710>]

In [38]: f
Out[38]: <matplotlib.figure.Figure at 0x7fc895f571d0>

In [39]: f.canvas.set_window_title('2 axes subplot example')

In [40]: ax.errorbar(x, y, yerr=5, xerr=3)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-40-72e7b5e77bd6> in <module>()
----> 1 ax.errorbar(x, y, yerr=5, xerr=3)

NameError: name 'x' is not defined
> <ipython-input-40-72e7b5e77bd6>(1)<module>()
----> 1 ax.errorbar(x, y, yerr=5, xerr=3)

ipdb> c

In [41]: x = np.random.random(10)

In [42]: ax.bar(x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-42-35273c45b882> in <module>()
----> 1 ax.bar(x)

/usr/local/lib/python3.5/dist-packages/matplotlib/__init__.py in inner(ax, *args, **kwargs)
   1890                     warnings.warn(msg % (label_namer, func.__name__),
   1891                                   RuntimeWarning, stacklevel=2)
-> 1892             return func(ax, *args, **kwargs)
   1893         pre_doc = inner.__doc__
   1894         if pre_doc is None:

TypeError: bar() missing 1 required positional argument: 'height'
> /usr/local/lib/python3.5/dist-packages/matplotlib/__init__.py(1892)inner()
   1890                     warnings.warn(msg % (label_namer, func.__name__),
   1891                                   RuntimeWarning, stacklevel=2)
-> 1892             return func(ax, *args, **kwargs)
   1893         pre_doc = inner.__doc__
   1894         if pre_doc is None:

ipdb> c

In [43]: left = np.arange(10)

In [44]: height = np.random.random(10)

In [45]: f, ax = plt.subplots()

In [46]: ax.bar(left, height)
Out[46]: <Container object of 10 artists>

In [47]: ax.bar?

In [48]: np.array([1, 2, 3])
Out[48]: array([1, 2, 3])

In [49]: np.array([[1, 2, 3], [4, 5, 6]))
  File "<ipython-input-49-868172d9ecf7>", line 1
    np.array([[1, 2, 3], [4, 5, 6]))
                                  ^
SyntaxError: invalid syntax


In [50]: np.array([[1, 2, 3], [4, 5, 6]])
Out[50]:
array([[1, 2, 3],
       [4, 5, 6]])

In [51]: np.array([[1, 2, 3], [4, 5, 6, 7]])
Out[51]: array([[1, 2, 3], [4, 5, 6, 7]], dtype=object)

In [52]: np.array([[1, 2, 3], [4, 5, 6]])
Out[52]:
array([[1, 2, 3],
       [4, 5, 6]])

In [53]: np.array(((1, 2, 3), [4, 5, 6)))
  File "<ipython-input-53-33a3d33842a8>", line 1
    np.array(((1, 2, 3), [4, 5, 6)))
                                 ^
SyntaxError: invalid syntax


In [54]: np.array(((1, 2, 3), [4, 5, 6))))
  File "<ipython-input-54-6bb35a4a465c>", line 1
    np.array(((1, 2, 3), [4, 5, 6))))
                                 ^
SyntaxError: invalid syntax


In [55]: np.array(((1, 2, 3), (4, 5, 6)))
Out[55]:
array([[1, 2, 3],
       [4, 5, 6]])

In [56]: np.arange(16)
Out[56]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

In [57]: np.arange(16).reshape((8, 2))
Out[57]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [58]: a = np.arange(16).reshape((8, 2))

In [59]: a.shape
Out[59]: (8, 2)

In [60]: a.size
Out[60]: 16

In [61]:

In [61]: a
Out[61]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [62]: a.reshape((4, 4))
Out[62]:
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])

In [63]: a.reshape((8, 2))
Out[63]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [64]: a.reshape((8, 3))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-64-39b9a48ee80c> in <module>()
----> 1 a.reshape((8, 3))

ValueError: cannot reshape array of size 16 into shape (8,3)
> <ipython-input-64-39b9a48ee80c>(1)<module>()
----> 1 a.reshape((8, 3))

ipdb> c

In [65]: np.zeros(10)
Out[65]: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])

In [66]: np.zeros((8, 2))
Out[66]:
array([[ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.]])

In [67]: np.ones((8, 2))
Out[67]:
array([[ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.]])

In [68]: np.random.random((8, 2))
Out[68]:
array([[ 0.86110482,  0.55658592],
       [ 0.66417215,  0.34862305],
       [ 0.99042453,  0.00442762],
       [ 0.19696781,  0.59112595],
       [ 0.13248685,  0.83770621],
       [ 0.04571792,  0.43502959],
       [ 0.21036904,  0.8319733 ],
       [ 0.39049463,  0.12653993]])

In [69]: np.tile(7, 8)
Out[69]: array([7, 7, 7, 7, 7, 7, 7, 7])

In [70]: np.tile(7, 15)
Out[70]: array([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])

In [71]: np.tile([1, 2], 8)
Out[71]: array([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])

In [72]: np.tile(8, [1,2])
Out[72]: array([[8, 8]])

In [73]: np.tile?

In [74]: np.tile([[1, 2]], 8)
Out[74]: array([[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]])

In [75]: np.tile(8, (1, 2))
Out[75]: array([[8, 8]])

In [76]: np.tile([1, 2], [8, 1])
Out[76]:
array([[1, 2],
       [1, 2],
       [1, 2],
       [1, 2],
       [1, 2],
       [1, 2],
       [1, 2],
       [1, 2]])

In [77]: a = np.zeros((8, 2))

In [78]: a
Out[78]:
array([[ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.],
       [ 0.,  0.]])

In [79]: a.fill(7)

In [80]: a
Out[80]:
array([[ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.]])

In [81]: np.eye(5)
Out[81]:
array([[ 1.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.]])

In [82]: a
Out[82]:
array([[ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.],
       [ 7.,  7.]])

In [83]: a = np.arange(16).reshape((8, 2))

In [84]: a
Out[84]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [85]: a.ravel()
Out[85]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

In [86]: f, ax = plt.subplots(figsize=(3, 3))

In [87]: ax
Out[87]: <matplotlib.axes._subplots.AxesSubplot at 0x7fc87b8ac780>

In [88]: a
Out[88]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [89]: im = ax.imshow(a)

In [90]: f.canvas.set_window_title('imshow')

In [91]: f.colorbar(im)
Out[91]: <matplotlib.colorbar.Colorbar at 0x7fc87b80f7b8>

In [92]: f.set_tight_layout(True)

In [93]: ax.set_xticks([])
Out[93]: []

In [94]: ax.set_yticks([])
Out[94]: []

In [95]: im.set_cmap('jet')

In [96]: plt.colormaps()
Out[96]:
['Accent',
 'Accent_r',
 'Blues',
 'Blues_r',
 'BrBG',
 'BrBG_r',
 'BuGn',
 'BuGn_r',
 'BuPu',
 'BuPu_r',
 'CMRmap',
 'CMRmap_r',
 'Dark2',
 'Dark2_r',
 'GnBu',
 'GnBu_r',
 'Greens',
 'Greens_r',
 'Greys',
 'Greys_r',
 'OrRd',
 'OrRd_r',
 'Oranges',
 'Oranges_r',
 'PRGn',
 'PRGn_r',
 'Paired',
 'Paired_r',
 'Pastel1',
 'Pastel1_r',
 'Pastel2',
 'Pastel2_r',
 'PiYG',
 'PiYG_r',
 'PuBu',
 'PuBuGn',
 'PuBuGn_r',
 'PuBu_r',
 'PuOr',
 'PuOr_r',
 'PuRd',
 'PuRd_r',
 'Purples',
 'Purples_r',
 'RdBu',
 'RdBu_r',
 'RdGy',
 'RdGy_r',
 'RdPu',
 'RdPu_r',
 'RdYlBu',
 'RdYlBu_r',
 'RdYlGn',
 'RdYlGn_r',
 'Reds',
 'Reds_r',
 'Set1',
 'Set1_r',
 'Set2',
 'Set2_r',
 'Set3',
 'Set3_r',
 'Spectral',
 'Spectral_r',
 'Vega10',
 'Vega10_r',
 'Vega20',
 'Vega20_r',
 'Vega20b',
 'Vega20b_r',
 'Vega20c',
 'Vega20c_r',
 'Wistia',
 'Wistia_r',
 'YlGn',
 'YlGnBu',
 'YlGnBu_r',
 'YlGn_r',
 'YlOrBr',
 'YlOrBr_r',
 'YlOrRd',
 'YlOrRd_r',
 'afmhot',
 'afmhot_r',
 'autumn',
 'autumn_r',
 'binary',
 'binary_r',
 'bone',
 'bone_r',
 'brg',
 'brg_r',
 'bwr',
 'bwr_r',
 'cool',
 'cool_r',
 'coolwarm',
 'coolwarm_r',
 'copper',
 'copper_r',
 'cubehelix',
 'cubehelix_r',
 'flag',
 'flag_r',
 'gist_earth',
 'gist_earth_r',
 'gist_gray',
 'gist_gray_r',
 'gist_heat',
 'gist_heat_r',
 'gist_ncar',
 'gist_ncar_r',
 'gist_rainbow',
 'gist_rainbow_r',
 'gist_stern',
 'gist_stern_r',
 'gist_yarg',
 'gist_yarg_r',
 'gnuplot',
 'gnuplot2',
 'gnuplot2_r',
 'gnuplot_r',
 'gray',
 'gray_r',
 'hot',
 'hot_r',
 'hsv',
 'hsv_r',
 'inferno',
 'inferno_r',
 'jet',
 'jet_r',
 'magma',
 'magma_r',
 'nipy_spectral',
 'nipy_spectral_r',
 'ocean',
 'ocean_r',
 'pink',
 'pink_r',
 'plasma',
 'plasma_r',
 'prism',
 'prism_r',
 'rainbow',
 'rainbow_r',
 'seismic',
 'seismic_r',
 'spectral',
 'spectral_r',
 'spring',
 'spring_r',
 'summer',
 'summer_r',
 'terrain',
 'terrain_r',
 'viridis',
 'viridis_r',
 'winter',
 'winter_r']

In [97]: plt.colormaps()
Out[97]:
['Accent',
 'Accent_r',
 'Blues',
 'Blues_r',
 'BrBG',
 'BrBG_r',
 'BuGn',
 'BuGn_r',
 'BuPu',
 'BuPu_r',
 'CMRmap',
 'CMRmap_r',
 'Dark2',
 'Dark2_r',
 'GnBu',
 'GnBu_r',
 'Greens',
 'Greens_r',
 'Greys',
 'Greys_r',
 'OrRd',
 'OrRd_r',
 'Oranges',
 'Oranges_r',
 'PRGn',
 'PRGn_r',
 'Paired',
 'Paired_r',
 'Pastel1',
 'Pastel1_r',
 'Pastel2',
 'Pastel2_r',
 'PiYG',
 'PiYG_r',
 'PuBu',
 'PuBuGn',
 'PuBuGn_r',
 'PuBu_r',
 'PuOr',
 'PuOr_r',
 'PuRd',
 'PuRd_r',
 'Purples',
 'Purples_r',
 'RdBu',
 'RdBu_r',
 'RdGy',
 'RdGy_r',
 'RdPu',
 'RdPu_r',
 'RdYlBu',
 'RdYlBu_r',
 'RdYlGn',
 'RdYlGn_r',
 'Reds',
 'Reds_r',
 'Set1',
 'Set1_r',
 'Set2',
 'Set2_r',
 'Set3',
 'Set3_r',
 'Spectral',
 'Spectral_r',
 'Vega10',
 'Vega10_r',
 'Vega20',
 'Vega20_r',
 'Vega20b',
 'Vega20b_r',
 'Vega20c',
 'Vega20c_r',
 'Wistia',
 'Wistia_r',
 'YlGn',
 'YlGnBu',
 'YlGnBu_r',
 'YlGn_r',
 'YlOrBr',
 'YlOrBr_r',
 'YlOrRd',
 'YlOrRd_r',
 'afmhot',
 'afmhot_r',
 'autumn',
 'autumn_r',
 'binary',
 'binary_r',
 'bone',
 'bone_r',
 'brg',
 'brg_r',
 'bwr',
 'bwr_r',
 'cool',
 'cool_r',
 'coolwarm',
 'coolwarm_r',
 'copper',
 'copper_r',
 'cubehelix',
 'cubehelix_r',
 'flag',
 'flag_r',
 'gist_earth',
 'gist_earth_r',
 'gist_gray',
 'gist_gray_r',
 'gist_heat',
 'gist_heat_r',
 'gist_ncar',
 'gist_ncar_r',
 'gist_rainbow',
 'gist_rainbow_r',
 'gist_stern',
 'gist_stern_r',
 'gist_yarg',
 'gist_yarg_r',
 'gnuplot',
 'gnuplot2',
 'gnuplot2_r',
 'gnuplot_r',
 'gray',
 'gray_r',
 'hot',
 'hot_r',
 'hsv',
 'hsv_r',
 'inferno',
 'inferno_r',
 'jet',
 'jet_r',
 'magma',
 'magma_r',
 'nipy_spectral',
 'nipy_spectral_r',
 'ocean',
 'ocean_r',
 'pink',
 'pink_r',
 'plasma',
 'plasma_r',
 'prism',
 'prism_r',
 'rainbow',
 'rainbow_r',
 'seismic',
 'seismic_r',
 'spectral',
 'spectral_r',
 'spring',
 'spring_r',
 'summer',
 'summer_r',
 'terrain',
 'terrain_r',
 'viridis',
 'viridis_r',
 'winter',
 'winter_r']

In [98]: scipy.ndimage
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-98-77f7494fdb50> in <module>()
----> 1 scipy.ndimage

NameError: name 'scipy' is not defined
> <ipython-input-98-77f7494fdb50>(1)<module>()
----> 1 scipy.ndimage

ipdb> c

In [99]: import scipy.ndimage

In [100]: import skimage

In [101]: a
Out[101]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [102]: a
Out[102]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [103]: a[0, 0]
Out[103]: 0

In [104]: a[2, 0]
Out[104]: 4

In [105]: a[-1, -1]
Out[105]: 15

In [106]: a[2, 2]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-106-b47b56fd5a74> in <module>()
----> 1 a[2, 2]

IndexError: index 2 is out of bounds for axis 1 with size 2
> <ipython-input-106-b47b56fd5a74>(1)<module>()
----> 1 a[2, 2]

ipdb> c

In [107]: a[0, :]
Out[107]: array([0, 1])

In [108]: a[0]
Out[108]: array([0, 1])

In [109]: a[:, 1]
Out[109]: array([ 1,  3,  5,  7,  9, 11, 13, 15])

In [110]:

In [110]: a
Out[110]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [111]: a[:3]
Out[111]:
array([[0, 1],
       [2, 3],
       [4, 5]])

In [112]: a[::2]
Out[112]:
array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]])

In [113]: x = np.arange(10)

In [114]: x
Out[114]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [115]: x[::-1]
Out[115]: array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

In [116]: a[::-1]
Out[116]:
array([[14, 15],
       [12, 13],
       [10, 11],
       [ 8,  9],
       [ 6,  7],
       [ 4,  5],
       [ 2,  3],
       [ 0,  1]])

In [117]: a[:, ::-1]
Out[117]:
array([[ 1,  0],
       [ 3,  2],
       [ 5,  4],
       [ 7,  6],
       [ 9,  8],
       [11, 10],
       [13, 12],
       [15, 14]])

In [118]: a
Out[118]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [119]: np.rot90(a)
Out[119]:
array([[ 1,  3,  5,  7,  9, 11, 13, 15],
       [ 0,  2,  4,  6,  8, 10, 12, 14]])

In [120]: np.rot90(a, -1)
Out[120]:
array([[14, 12, 10,  8,  6,  4,  2,  0],
       [15, 13, 11,  9,  7,  5,  3,  1]])

In [121]: a
Out[121]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [122]: a + 2
Out[122]:
array([[ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15],
       [16, 17]])

In [123]: a
Out[123]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [124]: a + 2
Out[124]:
array([[ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15],
       [16, 17]])

In [125]: a * 2
Out[125]:
array([[ 0,  2],
       [ 4,  6],
       [ 8, 10],
       [12, 14],
       [16, 18],
       [20, 22],
       [24, 26],
       [28, 30]])

In [126]: b = np.random.random(16).reshape((8, 2))

In [127]: a
Out[127]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [128]: b
Out[128]:
array([[ 0.08015195,  0.93534932],
       [ 0.4758314 ,  0.75844615],
       [ 0.25348448,  0.06686355],
       [ 0.32080073,  0.04669503],
       [ 0.36620918,  0.32856125],
       [ 0.34681433,  0.26401783],
       [ 0.93828584,  0.8098179 ],
       [ 0.69171322,  0.65358283]])

In [129]: a.shape
Out[129]: (8, 2)

In [130]: b.shape
Out[130]: (8, 2)

In [131]: a + b
Out[131]:
array([[  0.08015195,   1.93534932],
       [  2.4758314 ,   3.75844615],
       [  4.25348448,   5.06686355],
       [  6.32080073,   7.04669503],
       [  8.36620918,   9.32856125],
       [ 10.34681433,  11.26401783],
       [ 12.93828584,  13.8098179 ],
       [ 14.69171322,  15.65358283]])

In [132]: a * b
Out[132]:
array([[  0.        ,   0.93534932],
       [  0.9516628 ,   2.27533846],
       [  1.01393792,   0.33431774],
       [  1.92480436,   0.32686519],
       [  2.92967343,   2.95705129],
       [  3.46814328,   2.90419611],
       [ 11.25943008,  10.52763276],
       [  9.68398503,   9.80374248]])

In [133]: a - b
Out[133]:
array([[ -0.08015195,   0.06465068],
       [  1.5241686 ,   2.24155385],
       [  3.74651552,   4.93313645],
       [  5.67919927,   6.95330497],
       [  7.63379082,   8.67143875],
       [  9.65318567,  10.73598217],
       [ 11.06171416,  12.1901821 ],
       [ 13.30828678,  14.34641717]])

In [134]: a
Out[134]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [135]: a / b
Out[135]:
array([[   0.        ,    1.06911929],
       [   4.20316946,    3.95545548],
       [  15.78005874,   74.77916109],
       [  18.70319955,  149.90889666],
       [  21.84543828,   27.39215252],
       [  28.83387217,   41.66385313],
       [  12.78927965,   16.05299157],
       [  20.23960172,   22.95041924]])

In [136]: b / a
/usr/local/bin/ipython:1: RuntimeWarning: divide by zero encountered in true_divide
  #!/usr/bin/python3
Out[136]:
array([[        inf,  0.93534932],
       [ 0.2379157 ,  0.25281538],
       [ 0.06337112,  0.01337271],
       [ 0.05346679,  0.00667072],
       [ 0.04577615,  0.03650681],
       [ 0.03468143,  0.02400162],
       [ 0.07819049,  0.06229368],
       [ 0.04940809,  0.04357219]])

In [137]: 1 / 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-137-b710d87c980c> in <module>()
----> 1 1 / 0

ZeroDivisionError: division by zero
> <ipython-input-137-b710d87c980c>(1)<module>()
----> 1 1 / 0

ipdb> c

In [138]: b / a
/usr/local/bin/ipython:1: RuntimeWarning: divide by zero encountered in true_divide
  #!/usr/bin/python3
Out[138]:
array([[        inf,  0.93534932],
       [ 0.2379157 ,  0.25281538],
       [ 0.06337112,  0.01337271],
       [ 0.05346679,  0.00667072],
       [ 0.04577615,  0.03650681],
       [ 0.03468143,  0.02400162],
       [ 0.07819049,  0.06229368],
       [ 0.04940809,  0.04357219]])

In [139]: np.dot(a, b)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-139-579c274cec9b> in <module>()
----> 1 np.dot(a, b)

ValueError: shapes (8,2) and (8,2) not aligned: 2 (dim 1) != 8 (dim 0)
> <ipython-input-139-579c274cec9b>(1)<module>()
----> 1 np.dot(a, b)

ipdb> c

In [140]: a
Out[140]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [141]: b
Out[141]:
array([[ 0.08015195,  0.93534932],
       [ 0.4758314 ,  0.75844615],
       [ 0.25348448,  0.06686355],
       [ 0.32080073,  0.04669503],
       [ 0.36620918,  0.32856125],
       [ 0.34681433,  0.26401783],
       [ 0.93828584,  0.8098179 ],
       [ 0.69171322,  0.65358283]])

In [142]: a
Out[142]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [143]: a.T
Out[143]:
array([[ 0,  2,  4,  6,  8, 10, 12, 14],
       [ 1,  3,  5,  7,  9, 11, 13, 15]])

In [144]: np.dot(a, b.T)
Out[144]:
array([[  0.93534932,   0.75844615,   0.06686355,   0.04669503,
          0.32856125,   0.26401783,   0.8098179 ,   0.65358283],
       [  2.96635184,   3.22700126,   0.70755961,   0.78168653,
          1.71810212,   1.48568214,   4.30602539,   3.34417493],
       [  4.99735437,   5.69555636,   1.34825566,   1.51667804,
          3.10764299,   2.70734645,   7.80223288,   6.03476702],
       [  7.0283569 ,   8.16411147,   1.98895172,   2.25166955,
          4.49718385,   3.92901076,  11.29844037,   8.72535912],
       [  9.05935943,  10.63266657,   2.62964778,   2.98666105,
          5.88672472,   5.15067507,  14.79464786,  11.41595122],
       [ 11.09036195,  13.10122168,   3.27034383,   3.72165256,
          7.27626558,   6.37233939,  18.29085535,  14.10654331],
       [ 13.12136448,  15.56977678,   3.91103989,   4.45664407,
          8.66580645,   7.5940037 ,  21.78706284,  16.79713541],
       [ 15.15236701,  18.03833188,   4.55173595,   5.19163558,
         10.05534731,   8.81566801,  25.28327033,  19.48772751]])

In [145]: a.shape
Out[145]: (8, 2)

In [146]: b.T
Out[146]:
array([[ 0.08015195,  0.4758314 ,  0.25348448,  0.32080073,  0.36620918,
         0.34681433,  0.93828584,  0.69171322],
       [ 0.93534932,  0.75844615,  0.06686355,  0.04669503,  0.32856125,
         0.26401783,  0.8098179 ,  0.65358283]])

In [147]: b.T.shape
Out[147]: (2, 8)

In [148]: x
Out[148]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [149]: x.min()
Out[149]: 0

In [150]: x.max()
Out[150]: 9

In [151]: a
Out[151]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [152]: a.max()
Out[152]: 15

In [153]: a.max?
Docstring:
a.max(axis=None, out=None)

Return the maximum along a given axis.

Refer to `numpy.amax` for full documentation.

See Also
--------
numpy.amax : equivalent function
Type:      builtin_function_or_method

In [154]: a.max(axis=0)
Out[154]: array([14, 15])

In [155]: a.max(axis=1)
Out[155]: array([ 1,  3,  5,  7,  9, 11, 13, 15])

In [156]: a.sum()
Out[156]: 120

In [157]: a.sum(axis=0)
Out[157]: array([56, 64])

In [158]: a.sum(axis=1)
Out[158]: array([ 1,  5,  9, 13, 17, 21, 25, 29])

In [159]: a
Out[159]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [160]: a.sum(axis=1)
Out[160]: array([ 1,  5,  9, 13, 17, 21, 25, 29])

In [161]: a.sum(axis=0)
Out[161]: array([56, 64])

In [162]: np.concatenate
Out[162]: <function numpy.core.multiarray.concatenate>

In [163]: np.concatenate?

In [164]: a
Out[164]:
array([[ 0,  1],
       [ 2,  3],
       [ 4,  5],
       [ 6,  7],
       [ 8,  9],
       [10, 11],
       [12, 13],
       [14, 15]])

In [165]: b
Out[165]:
array([[ 0.08015195,  0.93534932],
       [ 0.4758314 ,  0.75844615],
       [ 0.25348448,  0.06686355],
       [ 0.32080073,  0.04669503],
       [ 0.36620918,  0.32856125],
       [ 0.34681433,  0.26401783],
       [ 0.93828584,  0.8098179 ],
       [ 0.69171322,  0.65358283]])

In [166]: np.concatenate([a, b], axis=0)
Out[166]:
array([[  0.        ,   1.        ],
       [  2.        ,   3.        ],
       [  4.        ,   5.        ],
       [  6.        ,   7.        ],
       [  8.        ,   9.        ],
       [ 10.        ,  11.        ],
       [ 12.        ,  13.        ],
       [ 14.        ,  15.        ],
       [  0.08015195,   0.93534932],
       [  0.4758314 ,   0.75844615],
       [  0.25348448,   0.06686355],
       [  0.32080073,   0.04669503],
       [  0.36620918,   0.32856125],
       [  0.34681433,   0.26401783],
       [  0.93828584,   0.8098179 ],
       [  0.69171322,   0.65358283]])

In [167]: np.concatenate([a, b], axis=1)
Out[167]:
array([[  0.        ,   1.        ,   0.08015195,   0.93534932],
       [  2.        ,   3.        ,   0.4758314 ,   0.75844615],
       [  4.        ,   5.        ,   0.25348448,   0.06686355],
       [  6.        ,   7.        ,   0.32080073,   0.04669503],
       [  8.        ,   9.        ,   0.36620918,   0.32856125],
       [ 10.        ,  11.        ,   0.34681433,   0.26401783],
       [ 12.        ,  13.        ,   0.93828584,   0.8098179 ],
       [ 14.        ,  15.        ,   0.69171322,   0.65358283]])

In [168]: c = np.zeros([4, 5])

In [169]: np.concatenate([a, c], axis=1)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-169-1e110519d495> in <module>()
----> 1 np.concatenate([a, c], axis=1)

ValueError: all the input array dimensions except for the concatenation axis must match exactly
> <ipython-input-169-1e110519d495>(1)<module>()
----> 1 np.concatenate([a, c], axis=1)

ipdb> c
