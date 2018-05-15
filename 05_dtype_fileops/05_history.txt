mspacek@Godel:~/SciPyCourse2018/notes/05_dtype_fileops$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   05_dtypes_fileops.md
    modified:   05_dtypes_fileops.pdf

Untracked files:
  (use "git add <file>..." to include in what will be committed)

    ../06_matplotlib/

no changes added to commit (use "git add" and/or "git commit -a")
mspacek@Godel:~/SciPyCourse2018/notes/05_dtype_fileops$ gc
mspacek@Godel:~/SciPyCourse2018/notes/05_dtype_fileops$ git push
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 19.74 KiB | 0 bytes/s, done.
Total 5 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To git@github.com:SciPyCourse2018/notes.git
   aaf7fd3..2ef62f4  master -> master
mspacek@Godel:~/SciPyCourse2018/notes/05_dtype_fileops$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import numpy as np

In [2]: np.array([1, 2, 3])
Out[2]: array([1, 2, 3])

In [3]: np.arange(10)
Out[3]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [4]: np.zeros(5)
Out[4]: array([0., 0., 0., 0., 0.])

In [5]: np.ones(5)
Out[5]: array([1., 1., 1., 1., 1.])

In [6]: np.random.random(5)
Out[6]: array([0.7769928 , 0.21411377, 0.36502575, 0.23591421, 0.85258807])

In [7]: a = np.array([1,2,3])

In [8]: b = np.array([4,5,6])

In [9]: np.concatenate([a, b])
Out[9]: array([1, 2, 3, 4, 5, 6])

In [10]: a[0]
Out[10]: 1

In [11]: a[[0, 3, 4]]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-11-995449552aa8> in <module>()
----> 1 a[[0, 3, 4]]

IndexError: index 3 is out of bounds for axis 1 with size 3
> <ipython-input-11-995449552aa8>(1)<module>()
----> 1 a[[0, 3, 4]]

ipdb> c

In [12]: a[[0, 3, 2]]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-12-897507720e86> in <module>()
----> 1 a[[0, 3, 2]]

IndexError: index 3 is out of bounds for axis 1 with size 3
> <ipython-input-12-897507720e86>(1)<module>()
----> 1 a[[0, 3, 2]]

ipdb> c

In [13]: a
Out[13]: array([1, 2, 3])

In [14]: a = np.arange(10)

In [15]: a[[0, 3, 2]]
Out[15]: array([0, 3, 2])

In [16]: a = np.array([1,2,3])

In [17]: a
Out[17]: array([1, 2, 3])

In [18]: a[[False, True, True]]
Out[18]: array([2, 3])

In [19]: a[(False, True, True)]
Out[19]: array([], shape=(0, 3), dtype=int64)

In [20]: a[(0, 1, 2)]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-20-aba6884e6f08> in <module>()
----> 1 a[(0, 1, 2)]

IndexError: too many indices for array
> <ipython-input-20-aba6884e6f08>(1)<module>()
----> 1 a[(0, 1, 2)]

ipdb> c

In [21]: a[[False, True, True]]
Out[21]: array([2, 3])

In [22]: a > 1
Out[22]: array([False,  True,  True])

In [23]: a[a > 1]
Out[23]: array([2, 3])

In [24]: a > 1
Out[24]: array([False,  True,  True])

In [25]: np.where(a > 1)
Out[25]: (array([1, 2]),)

In [26]: np.where(a > 1)[0]
Out[26]: array([1, 2])

In [27]: np.where(a > 1)
Out[27]: (array([1, 2]),)

In [28]: np.where(a > 1)[0]
Out[28]: array([1, 2])

In [29]: np.where(a > 1)[0]
Out[29]: array([1, 2])

In [30]: a
Out[30]: array([1, 2, 3])

In [31]: a
Out[31]: array([1, 2, 3])

In [32]: b
Out[32]: array([4, 5, 6])

In [33]: a + b
Out[33]: array([5, 7, 9])

In [34]: a * b
Out[34]: array([ 4, 10, 18])

In [35]: a == b
Out[35]: array([False, False, False])

In [36]: a = np.array([True, False, False])

In [37]: b = np.array([True, True, False])

In [38]: a
Out[38]: array([ True, False, False])

In [39]: b
Out[39]: array([ True,  True, False])

In [40]: a and b
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-40-61df3bd186ad> in <module>()
----> 1 a and b

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
> <ipython-input-40-61df3bd186ad>(1)<module>()
----> 1 a and b

ipdb> c

In [41]: a & b
Out[41]: array([ True, False, False])

In [42]: np.array([1, 2, 3]) & np.array([2, 3, 4])
Out[42]: array([0, 2, 0])

In [43]: a & b
Out[43]: array([ True, False, False])

In [44]: a | b
Out[44]: array([ True,  True, False])

In [45]: a
Out[45]: array([ True, False, False])

In [46]: b
Out[46]: array([ True,  True, False])

In [47]: a | b
Out[47]: array([ True,  True, False])

In [48]: ~a
Out[48]: array([False,  True,  True])

In [49]: not a
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-49-666acecd4e9c> in <module>()
----> 1 not a

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
> <ipython-input-49-666acecd4e9c>(1)<module>()
----> 1 not a

ipdb> c

In [50]: not False
Out[50]: True

In [51]: not True
Out[51]: False

In [52]: a
Out[52]: array([ True, False, False])

In [53]: a
Out[53]: array([ True, False, False])

In [54]: a.all()
Out[54]: False

In [55]: a.any()
Out[55]: True

In [56]: np.all(a)
Out[56]: False

In [57]: f = np.array([False, False, False])

In [58]: f.all()
Out[58]: False

In [59]: f == False
Out[59]: array([ True,  True,  True])

In [60]: (f == False).all()
Out[60]: True

In [61]: a.max()
Out[61]: True

In [62]: a = np.array([1,2,3])

In [63]: a
Out[63]: array([1, 2, 3])

In [64]: a.max()
Out[64]: 3

In [65]: a.min()
Out[65]: 1

In [66]: a.mean()
Out[66]: 2.0

In [67]: a.sum()
Out[67]: 6

In [68]: a.ptp()
Out[68]: 2

In [69]: a.std()
Out[69]: 0.816496580927726

In [70]: a = np.arange(10)

In [71]: a
Out[71]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [72]: a -= a.mean()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-72-0edd4ebf7ae7> in <module>()
----> 1 a -= a.mean()

TypeError: Cannot cast ufunc subtract output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
> <ipython-input-72-0edd4ebf7ae7>(1)<module>()
----> 1 a -= a.mean()

ipdb> c

In [73]: a
Out[73]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [74]: a = a - a.mean()

In [75]: a
Out[75]: array([-4.5, -3.5, -2.5, -1.5, -0.5,  0.5,  1.5,  2.5,  3.5,  4.5])

In [76]: a.std()
Out[76]: 2.8722813232690143

In [77]: a = a / a.std()

In [78]: a
Out[78]:
array([-1.5666989 , -1.21854359, -0.87038828, -0.52223297, -0.17407766,
        0.17407766,  0.52223297,  0.87038828,  1.21854359,  1.5666989 ])

In [79]: a.std()
Out[79]: 1.0

In [80]: a.mean()
Out[80]: -6.661338147750939e-17

In [81]: a
Out[81]:
array([-1.5666989 , -1.21854359, -0.87038828, -0.52223297, -0.17407766,
        0.17407766,  0.52223297,  0.87038828,  1.21854359,  1.5666989 ])

In [82]: a = np.random.random(10)

In [83]: a
Out[83]:
array([0.09955295, 0.89036162, 0.10880796, 0.22626407, 0.09015402,
       0.02069752, 0.51345743, 0.66080201, 0.5720114 , 0.54555957])

In [84]: a.sort()

In [85]: a
Out[85]:
array([0.02069752, 0.09015402, 0.09955295, 0.10880796, 0.22626407,
       0.51345743, 0.54555957, 0.5720114 , 0.66080201, 0.89036162])

In [86]: np.sort(a)
Out[86]:
array([0.02069752, 0.09015402, 0.09955295, 0.10880796, 0.22626407,
       0.51345743, 0.54555957, 0.5720114 , 0.66080201, 0.89036162])

In [87]: np.diff?

In [88]: a
Out[88]:
array([0.02069752, 0.09015402, 0.09955295, 0.10880796, 0.22626407,
       0.51345743, 0.54555957, 0.5720114 , 0.66080201, 0.89036162])

In [89]: np.diff(a)
Out[89]:
array([0.06945649, 0.00939893, 0.00925501, 0.11745611, 0.28719336,
       0.03210214, 0.02645183, 0.08879061, 0.22955962])

In [90]: c = np.random.random(10)

In [91]: c
Out[91]:
array([0.32793355, 0.96456499, 0.30996069, 0.71583173, 0.71489704,
       0.71115823, 0.88940566, 0.3402144 , 0.9199117 , 0.64808675])

In [92]: c = np.random.random(10)*10

In [93]: c
Out[93]:
array([1.85060378, 0.78743231, 9.48751661, 2.28088003, 6.87335134,
       8.75942919, 2.69822152, 9.54837969, 9.55495683, 6.76592484])

In [94]: d = c[[2, 5, 8]]

In [95]: d = c[[1, 4, 7]]

In [96]: d
Out[96]: array([0.78743231, 6.87335134, 9.54837969])

In [97]: c > 5
Out[97]:
array([False, False,  True, False,  True,  True, False,  True,  True,
        True])

In [98]: c[c > 5]
Out[98]:
array([9.48751661, 6.87335134, 8.75942919, 9.54837969, 9.55495683,
       6.76592484])

In [99]: e = c[c > 5]

In [100]: c > 5
Out[100]:
array([False, False,  True, False,  True,  True, False,  True,  True,
        True])

In [101]: np.where(c > 5)
Out[101]: (array([2, 4, 5, 7, 8, 9]),)

In [102]: np.where(c > 5)[0]
Out[102]: array([2, 4, 5, 7, 8, 9])

In [103]: e.all() > 5
Out[103]: False

In [104]: np.all(e > 5)
Out[104]: True

In [105]: e > 5
Out[105]: array([ True,  True,  True,  True,  True,  True])

In [106]: (e > 5).all()
Out[106]: True

In [107]: f = np.random.random(10)

In [108]: f
Out[108]:
array([0.62775109, 0.49357233, 0.1542015 , 0.66093214, 0.33290038,
       0.1394076 , 0.12453399, 0.67340666, 0.88125575, 0.39493266])

In [109]: f * 2
Out[109]:
array([1.25550218, 0.98714466, 0.308403  , 1.32186429, 0.66580077,
       0.2788152 , 0.24906798, 1.34681331, 1.76251151, 0.78986532])

In [110]: f * 2 - 1
Out[110]:
array([ 0.25550218, -0.01285534, -0.691597  ,  0.32186429, -0.33419923,
       -0.7211848 , -0.75093202,  0.34681331,  0.76251151, -0.21013468])

In [111]: (f - 0.5)*2
Out[111]:
array([ 0.25550218, -0.01285534, -0.691597  ,  0.32186429, -0.33419923,
       -0.7211848 , -0.75093202,  0.34681331,  0.76251151, -0.21013468])

In [112]: np.random.random(10) *2 - 1
Out[112]:
array([-0.36437985, -0.13764721, -0.72491059, -0.72635391,  0.85512729,
       -0.74899159,  0.89717918, -0.89513827, -0.82508071,  0.3863081 ])

In [113]: np.random.random?

In [114]: f = (f - 0.5)*2

In [115]: f
Out[115]:
array([ 0.25550218, -0.01285534, -0.691597  ,  0.32186429, -0.33419923,
       -0.7211848 , -0.75093202,  0.34681331,  0.76251151, -0.21013468])

In [116]: -0.5 < f
Out[116]:
array([ True,  True, False,  True,  True, False, False,  True,  True,
        True])

In [117]: f < 0.5
Out[117]:
array([ True,  True,  True,  True,  True,  True,  True,  True, False,
        True])

In [118]: -0.5 < f & f < 0.5
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-118-0a50e6dce0f7> in <module>()
----> 1 -0.5 < f & f < 0.5

TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
> <ipython-input-118-0a50e6dce0f7>(1)<module>()
----> 1 -0.5 < f & f < 0.5

ipdb> c

In [119]: (-0.5 < f) & (f < 0.5)
Out[119]:
array([ True,  True, False,  True,  True, False, False,  True, False,
        True])

In [120]: -0.5 < f < 0.5
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-120-1e727fb71eaf> in <module>()
----> 1 -0.5 < f < 0.5

ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
> <ipython-input-120-1e727fb71eaf>(1)<module>()
----> 1 -0.5 < f < 0.5

ipdb> c

In [121]: -0.5 < 0 < 0.5
Out[121]: True

In [122]: (-0.5 < f) & (f < 0.5)
Out[122]:
array([ True,  True, False,  True,  True, False, False,  True, False,
        True])

In [123]: g = f[(-0.5 < f) & (f < 0.5)]

In [124]: g
Out[124]:
array([ 0.25550218, -0.01285534,  0.32186429, -0.33419923,  0.34681331,
       -0.21013468])

In [125]: ((-0.5 < g) & (g < 0.5)).all()
Out[125]: True

In [126]: np.all((-0.5 < g) & (g < 0.5))
Out[126]: True

In [127]: h = np.concatenate([c, f])

In [128]: h
Out[128]:
array([ 1.85060378,  0.78743231,  9.48751661,  2.28088003,  6.87335134,
        8.75942919,  2.69822152,  9.54837969,  9.55495683,  6.76592484,
        0.25550218, -0.01285534, -0.691597  ,  0.32186429, -0.33419923,
       -0.7211848 , -0.75093202,  0.34681331,  0.76251151, -0.21013468])

In [129]: c
Out[129]:
array([1.85060378, 0.78743231, 9.48751661, 2.28088003, 6.87335134,
       8.75942919, 2.69822152, 9.54837969, 9.55495683, 6.76592484])

In [130]: f
Out[130]:
array([ 0.25550218, -0.01285534, -0.691597  ,  0.32186429, -0.33419923,
       -0.7211848 , -0.75093202,  0.34681331,  0.76251151, -0.21013468])

In [131]: h
Out[131]:
array([ 1.85060378,  0.78743231,  9.48751661,  2.28088003,  6.87335134,
        8.75942919,  2.69822152,  9.54837969,  9.55495683,  6.76592484,
        0.25550218, -0.01285534, -0.691597  ,  0.32186429, -0.33419923,
       -0.7211848 , -0.75093202,  0.34681331,  0.76251151, -0.21013468])

In [132]: h.sort()

In [133]: h
Out[133]:
array([-0.75093202, -0.7211848 , -0.691597  , -0.33419923, -0.21013468,
       -0.01285534,  0.25550218,  0.32186429,  0.34681331,  0.76251151,
        0.78743231,  1.85060378,  2.28088003,  2.69822152,  6.76592484,
        6.87335134,  8.75942919,  9.48751661,  9.54837969,  9.55495683])

In [134]: np.diff(h)
Out[134]:
array([0.02974723, 0.0295878 , 0.35739777, 0.12406455, 0.19727934,
       0.26835752, 0.0663621 , 0.02494902, 0.4156982 , 0.0249208 ,
       1.06317147, 0.43027625, 0.4173415 , 4.06770331, 0.1074265 ,
       1.88607784, 0.72808742, 0.06086308, 0.00657714])

In [135]: np.diff(h) > 0
Out[135]:
array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True])

In [136]: (np.diff(h) > 0).all()
Out[136]: True

In [137]: a
Out[137]:
array([0.02069752, 0.09015402, 0.09955295, 0.10880796, 0.22626407,
       0.51345743, 0.54555957, 0.5720114 , 0.66080201, 0.89036162])

In [138]: len(a)
Out[138]: 10

In [139]: a.nbytes
Out[139]: 80

In [140]: len(a) * a.dtype.itemsize
Out[140]: 80

In [141]: a.dtype
Out[141]: dtype('float64')

In [142]: a = 5

In [143]: type(a)
Out[143]: int

In [144]: a = np.zeros(5)

In [145]: a
Out[145]: array([0., 0., 0., 0., 0.])

In [146]: a.dtype
Out[146]: dtype('float64')

In [147]: a = np.arange(10)

In [148]: a
Out[148]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [149]: a.dtype
Out[149]: dtype('int64')

In [150]: np.arange?

In [151]: np.arange(10, dtype=np.uint64)
Out[151]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint64)

In [152]: a = np.arange(10, dtype=np.uint64)

In [153]: a[0] = -1

In [154]: a
Out[154]:
array([18446744073709551615,                    1,                    2,
                          3,                    4,                    5,
                          6,                    7,                    8,
                          9], dtype=uint64)

In [155]: 2**63 -1
Out[155]: 9223372036854775807

In [156]: 2**64 -1
Out[156]: 18446744073709551615

In [157]: np.iinfo
Out[157]: numpy.core.getlimits.iinfo

In [158]: np.int8
Out[158]: numpy.int8

In [159]: np.uint8
Out[159]: numpy.uint8

In [160]: np.int64
Out[160]: numpy.int64

In [161]: np.uint64
Out[161]: numpy.uint64

In [162]: np.iinfo(np.uint8)
Out[162]: iinfo(min=0, max=255, dtype=uint8)

In [163]: np.iinfo(np.int8)
Out[163]: iinfo(min=-128, max=127, dtype=int8)

In [164]: np.iinfo(np.int16)
Out[164]: iinfo(min=-32768, max=32767, dtype=int16)

In [165]: np.iinfo(np.uint16)
Out[165]: iinfo(min=0, max=65535, dtype=uint16)

In [166]: np.iinfo(np.int32)
Out[166]: iinfo(min=-2147483648, max=2147483647, dtype=int32)

In [167]: np.iinfo(np.uint32)
Out[167]: iinfo(min=0, max=4294967295, dtype=uint32)

In [168]: np.iinfo(np.int64)
Out[168]: iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)

In [169]: np.iinfo(np.uint64)
Out[169]: iinfo(min=0, max=18446744073709551615, dtype=uint64)

In [170]: 2**63-1
Out[170]: 9223372036854775807

In [171]: 2**64-1
Out[171]: 18446744073709551615

In [172]: a = np.zeros(5, dtype=np.uint8)

In [173]: b = np.zeros(5, dtype=np.int8)

In [174]: a.dtype
Out[174]: dtype('uint8')

In [175]: b.dtype
Out[175]: dtype('int8')

In [176]: a
Out[176]: array([0, 0, 0, 0, 0], dtype=uint8)

In [177]: a[:] = 255

In [178]: a
Out[178]: array([255, 255, 255, 255, 255], dtype=uint8)

In [179]: a[:] = 256

In [180]: a
Out[180]: array([0, 0, 0, 0, 0], dtype=uint8)

In [181]: a = np.zeros(5, dtype=np.uint8)

In [182]: a
Out[182]: array([0, 0, 0, 0, 0], dtype=uint8)

In [183]: a[:] -1
Out[183]: array([255, 255, 255, 255, 255], dtype=uint8)

In [184]: b
Out[184]: array([0, 0, 0, 0, 0], dtype=int8)

In [185]: b.dtype
Out[185]: dtype('int8')

In [186]: b[:] = 127

In [187]: b
Out[187]: array([127, 127, 127, 127, 127], dtype=int8)

In [188]: b[:] = 128

In [189]: b
Out[189]: array([-128, -128, -128, -128, -128], dtype=int8)

In [190]: b[:] = -128

In [191]: b
Out[191]: array([-128, -128, -128, -128, -128], dtype=int8)

In [192]: b[:] = -129

In [193]: b
Out[193]: array([127, 127, 127, 127, 127], dtype=int8)

In [194]: a
Out[194]: array([0, 0, 0, 0, 0], dtype=uint8)

In [195]: a[:] = 200

In [196]: b[:] = 100

In [197]: a
Out[197]: array([200, 200, 200, 200, 200], dtype=uint8)

In [198]: b
Out[198]: array([100, 100, 100, 100, 100], dtype=int8)

In [199]: a + b
Out[199]: array([300, 300, 300, 300, 300], dtype=int16)

In [200]: a + b
Out[200]: array([300, 300, 300, 300, 300], dtype=int16)

In [201]: np.int16(a) + np.int16(b)
Out[201]: array([300, 300, 300, 300, 300], dtype=int16)

In [202]: a = np.zeros(20000000000, dtype=np.int8)
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)
<ipython-input-202-ee45ca3b244d> in <module>()
----> 1 a = np.zeros(20000000000, dtype=np.int8)

MemoryError:
> <ipython-input-202-ee45ca3b244d>(1)<module>()
----> 1 a = np.zeros(20000000000, dtype=np.int8)

ipdb> c

In [203]: whos
Variable   Type       Data/Info
-------------------------------
a          ndarray    5: 5 elems, type `uint8`, 5 bytes
b          ndarray    5: 5 elems, type `int8`, 5 bytes
c          ndarray    10: 10 elems, type `float64`, 80 bytes
d          ndarray    3: 3 elems, type `float64`, 24 bytes
e          ndarray    6: 6 elems, type `float64`, 48 bytes
f          ndarray    10: 10 elems, type `float64`, 80 bytes
g          ndarray    6: 6 elems, type `float64`, 48 bytes
h          ndarray    20: 20 elems, type `float64`, 160 bytes
np         module     <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
odict      type       <class 'collections.OrderedDict'>
plt        module     <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>

In [204]: del a

In [205]: whos
Variable   Type       Data/Info
-------------------------------
b          ndarray    5: 5 elems, type `int8`, 5 bytes
c          ndarray    10: 10 elems, type `float64`, 80 bytes
d          ndarray    3: 3 elems, type `float64`, 24 bytes
e          ndarray    6: 6 elems, type `float64`, 48 bytes
f          ndarray    10: 10 elems, type `float64`, 80 bytes
g          ndarray    6: 6 elems, type `float64`, 48 bytes
h          ndarray    20: 20 elems, type `float64`, 160 bytes
np         module     <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
odict      type       <class 'collections.OrderedDict'>
plt        module     <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>

In [206]: np.float64
Out[206]: numpy.float64

In [207]: np.float32
Out[207]: numpy.float32

In [208]: np.float16
Out[208]: numpy.float16

In [209]: a = np.zeros(5)

In [210]: a
Out[210]: array([0., 0., 0., 0., 0.])

In [211]: a.dtype
Out[211]: dtype('float64')

In [212]: a[:] = -1

In [213]: a
Out[213]: array([-1., -1., -1., -1., -1.])

In [214]: np.finfo(np.float16)
Out[214]: finfo(resolution=0.001, min=-6.55040e+04, max=6.55040e+04, dtype=float16)

In [215]: np.float16(1.234567e4)
Out[215]: 12344.0

In [216]: np.finfo(np.float32)
Out[216]: finfo(resolution=1e-06, min=-3.4028235e+38, max=3.4028235e+38, dtype=float32)

In [217]: np.float32(1.234567e4)
Out[217]: 12345.67

In [218]: np.float32(0)
Out[218]: 0.0

In [219]: np.finfo(np.float16).tiny
Out[219]: 6.104e-05

In [220]: np.inf
Out[220]: inf

In [221]: np.nan
Out[221]: nan

In [222]: np.float16(200000)
Out[222]: inf

In [223]: np.float16(-200000)
Out[223]: -inf

In [224]: np.zeros(5)
Out[224]: array([0., 0., 0., 0., 0.])

In [225]: 1 / np.zeros(5)
/usr/local/bin/ipython:1: RuntimeWarning: divide by zero encountered in true_divide
  #!/usr/bin/python3
Out[225]: array([inf, inf, inf, inf, inf])

In [226]: 1/0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-226-9e1622b385b6> in <module>()
----> 1 1/0

ZeroDivisionError: division by zero
> <ipython-input-226-9e1622b385b6>(1)<module>()
----> 1 1/0

ipdb> c

In [227]: np.sqrt(-1)
/usr/local/bin/ipython:1: RuntimeWarning: invalid value encountered in sqrt
  #!/usr/bin/python3
Out[227]: nan

In [228]: np.sqrt(np.array([-1]))
/usr/local/bin/ipython:1: RuntimeWarning: invalid value encountered in sqrt
  #!/usr/bin/python3
Out[228]: array([nan])

In [229]: np.sqrt(-1)
/usr/local/bin/ipython:1: RuntimeWarning: invalid value encountered in sqrt
  #!/usr/bin/python3
Out[229]: nan

In [230]: np.nan != np.inf
Out[230]: True

In [231]: np.nan != 0
Out[231]: True

In [232]: np.nan == np.inf
Out[232]: False

In [233]: np.nan == 0
Out[233]: False

In [234]: np.nan == np.nan
Out[234]: False

In [235]: None

In [236]: np.isnan(0)
Out[236]: False

In [237]: np.isnan(np.nan)
Out[237]: True

In [238]: b = np.array([True, True, False])

In [239]: len(3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-239-6b3b01eb5e19> in <module>()
----> 1 len(3)

TypeError: object of type 'int' has no len()
> <ipython-input-239-6b3b01eb5e19>(1)<module>()
----> 1 len(3)

ipdb> c

In [240]: len(b)
Out[240]: 3

In [241]: b.dtype
Out[241]: dtype('bool')

In [242]: b.nbytes
Out[242]: 3

In [243]: a = np.zeros(5)

In [244]: a
Out[244]: array([0., 0., 0., 0., 0.])

In [245]: a.dtype
Out[245]: dtype('float64')

In [246]: np.float32(a)
Out[246]: array([0., 0., 0., 0., 0.], dtype=float32)

In [247]: a
Out[247]: array([0., 0., 0., 0., 0.])

In [248]: np.int64(a)
Out[248]: array([0, 0, 0, 0, 0])

In [249]: np.int64(a).dtype
Out[249]: dtype('int64')

In [250]: a = np.random.random(5)

In [251]: a
Out[251]: array([0.8388389 , 0.48228068, 0.45827689, 0.9747822 , 0.74090766])

In [252]: np.int64(a)
Out[252]: array([0, 0, 0, 0, 0])

In [253]: np.intround(a)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-253-e967778cf880> in <module>()
----> 1 np.intround(a)

AttributeError: module 'numpy' has no attribute 'intround'
> <ipython-input-253-e967778cf880>(1)<module>()
----> 1 np.intround(a)

ipdb> c

In [254]: np.round(a)
Out[254]: array([1., 0., 0., 1., 1.])

In [255]: a
Out[255]: array([0.8388389 , 0.48228068, 0.45827689, 0.9747822 , 0.74090766])

In [256]: np.round(a)
Out[256]: array([1., 0., 0., 1., 1.])

In [257]: np.int64(np.round(a))
Out[257]: array([1, 0, 0, 1, 1])

In [258]: print('%.3f' % a[0])
0.839

In [259]: [3, 5, 1.7, -2.7, 1e2, -50]
Out[259]: [3, 5, 1.7, -2.7, 100.0, -50]

In [260]: a = np.array([3, 5, 1.7, -2.7, 1e2, -50])

In [261]: a
Out[261]: array([  3. ,   5. ,   1.7,  -2.7, 100. , -50. ])

In [262]: d.type
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-262-82019b232166> in <module>()
----> 1 d.type

AttributeError: 'numpy.ndarray' object has no attribute 'type'
> <ipython-input-262-82019b232166>(1)<module>()
----> 1 d.type

ipdb> c

In [263]: a.dtype
Out[263]: dtype('float64')

In [264]: a.nbytes
Out[264]: 48

In [265]: 1.5*8
Out[265]: 12.0

In [266]:
