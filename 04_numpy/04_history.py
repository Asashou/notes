mspacek@Godel:~/SciPyCourse2018/notes/04_numpy$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: a = [1,2,3]

In [2]: out = ([1, 2, 3])

In [3]: out
Out[3]: [1, 2, 3]

In [4]: type(out)
Out[4]: list

In [5]: out = ([1, 2, 3],)

In [6]: out
Out[6]: ([1, 2, 3],)

In [7]: type(out)
Out[7]: tuple

In [8]: out
Out[8]: ([1, 2, 3],)

In [9]: out[0]
Out[9]: [1, 2, 3]

In [10]: out[1]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-10-bc2a673b3295> in <module>()
----> 1 out[1]

IndexError: tuple index out of range
> <ipython-input-10-bc2a673b3295>(1)<module>()
----> 1 out[1]

ipdb> c

In [11]: len(out)
Out[11]: 1

In [12]: out[0][0]
Out[12]: 1

In [13]: sum = 0

In [14]: sum([1,2,3])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-56b33b39430a> in <module>()
----> 1 sum([1,2,3])

TypeError: 'int' object is not callable
> <ipython-input-14-56b33b39430a>(1)<module>()
----> 1 sum([1,2,3])

ipdb> c

In [15]: sum
Out[15]: 0

In [16]: del sum

In [17]: sum
Out[17]: <function sum(iterable, start=0, /)>

In [18]: normalized_values = []
    ...: def norm(list):
    ...:      """that accepts a list of values of arbitrary length N, and returns a list of the nor
    ...: malized values"""
    ...:      normalized_values.append(float(i)/sum(list) for i in list)
    ...:      return normalized_values
    ...:
    ...:

In [19]: norm([1,2,3])
Out[19]: [<generator object norm.<locals>.<genexpr> at 0x7f873ace3e60>]

In [20]: norm([1,2,3])
Out[20]:
[<generator object norm.<locals>.<genexpr> at 0x7f873ace3e60>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc2b0f8>]

In [21]: norm([1,2,3])
Out[21]:
[<generator object norm.<locals>.<genexpr> at 0x7f873ace3e60>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc2b0f8>,
 <generator object norm.<locals>.<genexpr> at 0x7f873c2ed258>]

In [22]: norm([1,2,3])
Out[22]:
[<generator object norm.<locals>.<genexpr> at 0x7f873ace3e60>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc2b0f8>,
 <generator object norm.<locals>.<genexpr> at 0x7f873c2ed258>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc61518>]

In [23]: norm([1,2,3])
Out[23]:
[<generator object norm.<locals>.<genexpr> at 0x7f873ace3e60>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc2b0f8>,
 <generator object norm.<locals>.<genexpr> at 0x7f873c2ed258>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc61518>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc612b0>]

In [24]: norm([1,2,3])
Out[24]:
[<generator object norm.<locals>.<genexpr> at 0x7f873ace3e60>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc2b0f8>,
 <generator object norm.<locals>.<genexpr> at 0x7f873c2ed258>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc61518>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc612b0>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc61620>]

In [25]: norm([1,2,3])
Out[25]:
[<generator object norm.<locals>.<genexpr> at 0x7f873ace3e60>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc2b0f8>,
 <generator object norm.<locals>.<genexpr> at 0x7f873c2ed258>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc61518>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc612b0>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc61620>,
 <generator object norm.<locals>.<genexpr> at 0x7f872cc616d0>]

In [26]: data = [[9.1, 2.1, 0.9, 1.5, 1.1],
    ...: [4.4, 2.2, 3.3, 5.5, 6.6],
    ...: [0.1, 0.2, 0.3, 0.4, 0.5]]

In [27]:

In [27]: type(data)
Out[27]: list

In [28]: len(data)
Out[28]: 3

In [29]: for blah in data:
    ...:     print(blah)
    ...:
[9.1, 2.1, 0.9, 1.5, 1.1]
[4.4, 2.2, 3.3, 5.5, 6.6]
[0.1, 0.2, 0.3, 0.4, 0.5]

In [30]: def norm(vals):
    ...:     """Return values normalized by the sum of the values"""
    ...:     s = sum(vals)
    ...:     return [ val/s for val in vals ]
    ...:
    ...:

In [31]: normdata = [ norm(row) for row in data ]

In [32]:

In [32]: [ sum(row) for row in normdata ]
Out[32]: [1.0, 1.0, 1.0]

In [33]: d = {'a': 1, 'b':2, 'c':3}

In [34]: for blah in d:
    ...:     print(blah)
    ...:
c
b
a

In [35]: d.values()
Out[35]: dict_values([3, 2, 1])

In [36]: range(10)
Out[36]: range(0, 10)

In [37]: d.values
Out[37]: <function dict.values>

In [38]: d
Out[38]: {'a': 1, 'b': 2, 'c': 3}

In [39]: sum(d)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-39-3b8b3f92adcf> in <module>()
----> 1 sum(d)

TypeError: unsupported operand type(s) for +: 'int' and 'str'
> <ipython-input-39-3b8b3f92adcf>(1)<module>()
----> 1 sum(d)

ipdb> c

In [40]: import numpy as np

In [41]: np.array([1, 2, 3])
Out[41]: array([1, 2, 3])

In [42]: a = np.array([1, 2, 3])

In [43]: type(a)
Out[43]: numpy.ndarray

In [44]: len(a)
Out[44]: 3

In [45]: list(range(10))
Out[45]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [46]: np.arange(10)
Out[46]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [47]: np.arange?

In [48]: np.arange(5, 10)
Out[48]: array([5, 6, 7, 8, 9])

In [49]: np.arange(0, 10, 2)
Out[49]: array([0, 2, 4, 6, 8])

In [50]: a = np.zeros(10)

In [51]: a
Out[51]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

In [52]: np.zeros?

In [53]: np.zeros(10, dtype=int)
Out[53]: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

In [54]: np.ones(10)
Out[54]: array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

In [55]: np.random.random()
Out[55]: 0.6933926661268643

In [56]: np.random.random(10)
Out[56]:
array([0.92832641, 0.54520633, 0.32089939, 0.7502674 , 0.76521327,
       0.12184333, 0.71188846, 0.81876743, 0.49383334, 0.93380366])

In [57]: np.random.random(10)
Out[57]:
array([0.62092071, 0.91471678, 0.01708538, 0.71346464, 0.75259576,
       0.36003441, 0.03886495, 0.37476866, 0.29590562, 0.29222271])

In [58]: np.random.random(10)
Out[58]:
array([0.72365784, 0.7904832 , 0.11321651, 0.10460852, 0.04090354,
       0.36700808, 0.37862027, 0.0629504 , 0.52255285, 0.76814799])

In [59]: np.random.random(10)
Out[59]:
array([0.93545075, 0.78369415, 0.35498173, 0.3808017 , 0.10508283,
       0.89968913, 0.9759162 , 0.59270249, 0.70722926, 0.99197756])

In [60]: np.random.random(10)
Out[60]:
array([0.47633676, 0.09597018, 0.61361619, 0.09872256, 0.34417759,
       0.85735885, 0.811615  , 0.86779086, 0.56265595, 0.43576761])

In [61]: np.random.random(10)
Out[61]:
array([0.06307054, 0.99229968, 0.21011   , 0.46315025, 0.46104423,
       0.5549749 , 0.58090636, 0.92564639, 0.61632985, 0.1596553 ])

In [62]: np.random.random(10)
Out[62]:
array([0.53764548, 0.54009523, 0.97425611, 0.04813426, 0.86381816,
       0.0220876 , 0.2572609 , 0.30792534, 0.97062869, 0.54061391])

In [63]: np.random.random(10)
Out[63]:
array([0.37714014, 0.11030685, 0.83016746, 0.77362355, 0.43025869,
       0.36249539, 0.36915069, 0.52375035, 0.90301258, 0.72779409])

In [64]: np.random.random(10)
Out[64]:
array([0.57406261, 0.27078683, 0.52111471, 0.47161363, 0.96583367,
       0.0775885 , 0.56066856, 0.22679126, 0.72036536, 0.24519929])

In [65]: a = np.tile([1, 2], 5)

In [66]: a
Out[66]: array([1, 2, 1, 2, 1, 2, 1, 2, 1, 2])

In [67]: a = np.zeros(10)

In [68]: a
Out[68]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

In [69]: a.fill(7)

In [70]: a
Out[70]: array([7., 7., 7., 7., 7., 7., 7., 7., 7., 7.])

In [71]: a
Out[71]: array([7., 7., 7., 7., 7., 7., 7., 7., 7., 7.])

In [72]: a = np.random.random(10)

In [73]: a
Out[73]:
array([0.00725926, 0.15087952, 0.75850931, 0.28192286, 0.11269132,
       0.63402425, 0.16261415, 0.21486441, 0.57475184, 0.65762235])

In [74]: a.max()
Out[74]: 0.7585093117608965

In [75]: np.max(a)
Out[75]: 0.7585093117608965

In [76]: a.fill?
Docstring:
a.fill(value)

Fill the array with a scalar value.

Parameters
----------
value : scalar
    All elements of `a` will be assigned this value.

Examples
--------
>>> a = np.array([1, 2])
>>> a.fill(0)
>>> a
array([0, 0])
>>> a = np.empty(2)
>>> a.fill(1)
>>> a
array([ 1.,  1.])
Type:      builtin_function_or_method

In [77]: a[0]
Out[77]: 0.007259260418730373

In [78]: a[1]
Out[78]: 0.1508795201429055

In [79]: a[-1]
Out[79]: 0.6576223477170077

In [80]: a[-2]
Out[80]: 0.5747518425582401

In [81]: a
Out[81]:
array([0.00725926, 0.15087952, 0.75850931, 0.28192286, 0.11269132,
       0.63402425, 0.16261415, 0.21486441, 0.57475184, 0.65762235])

In [82]: a[0] = 2342342

In [83]: a
Out[83]:
array([2.34234200e+06, 1.50879520e-01, 7.58509312e-01, 2.81922859e-01,
       1.12691315e-01, 6.34024248e-01, 1.62614154e-01, 2.14864405e-01,
       5.74751843e-01, 6.57622348e-01])

In [84]: a[:] = 7

In [85]: a[:] = np.random.random(10)

In [86]: a
Out[86]:
array([0.26928622, 0.42447639, 0.73288087, 0.22799728, 0.66563259,
       0.21730009, 0.12965631, 0.41110079, 0.51321832, 0.77216661])

In [87]: a[:] = np.random.random(len(10))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-87-1877ef05ebb7> in <module>()
----> 1 a[:] = np.random.random(len(10))

TypeError: object of type 'int' has no len()
> <ipython-input-87-1877ef05ebb7>(1)<module>()
----> 1 a[:] = np.random.random(len(10))

ipdb> c

In [88]: a[:] = np.random.random(len(a))

In [89]: a[:5] = 453

In [90]: a
Out[90]:
array([4.53000000e+02, 4.53000000e+02, 4.53000000e+02, 4.53000000e+02,
       4.53000000e+02, 9.27263594e-02, 5.16953940e-01, 3.46144280e-01,
       4.48089737e-02, 4.78367557e-01])

In [91]: a = 453

In [92]: a
Out[92]: 453

In [93]: a = np.random.random(10)

In [94]: a
Out[94]:
array([0.52632586, 0.59361555, 0.94303106, 0.29582494, 0.19002054,
       0.06335352, 0.28476905, 0.31435305, 0.08336591, 0.10792136])

In [95]: a[:] = np.random.random(len(a))

In [96]: a
Out[96]:
array([0.84837705, 0.83441609, 0.48379602, 0.86901683, 0.43329609,
       0.23921007, 0.0669839 , 0.21671215, 0.887067  , 0.99714408])

In [97]: a[:] = np.random.random(len(a))

In [98]: a
Out[98]:
array([0.85024312, 0.87932086, 0.11248969, 0.054427  , 0.06007943,
       0.43282916, 0.2498028 , 0.12607751, 0.29624769, 0.74477733])

In [99]: a[:] = np.random.random(len(a))

In [100]: a
Out[100]:
array([0.57024489, 0.90269929, 0.59213985, 0.231844  , 0.95254352,
       0.91552841, 0.48249847, 0.30210503, 0.74906922, 0.73103586])

In [101]: np.random.random?

In [102]: def normd(d):
     ...:    "Normalise values of each key of dictionary d"
     ...:    d_sum = sum(d.values())
     ...:    for key, val in d.items():
     ...:        d[key]=val/d_sum
     ...:    return d
     ...:
     ...:

In [103]: normd?
Signature: normd(d)
Docstring: Normalise values of each key of dictionary d
File:      ~/SciPyCourse2018/notes/04_numpy/<ipython-input-102-290507438436>
Type:      function

In [104]: a = np.random.random(5)

In [105]: a
Out[105]: array([0.93738312, 0.93412268, 0.86453757, 0.55468707, 0.36503948])

In [106]: b = a.copy()

In [107]: a.copy()
Out[107]: array([0.93738312, 0.93412268, 0.86453757, 0.55468707, 0.36503948])

In [108]: a
Out[108]: array([0.93738312, 0.93412268, 0.86453757, 0.55468707, 0.36503948])

In [109]: b
Out[109]: array([0.93738312, 0.93412268, 0.86453757, 0.55468707, 0.36503948])

In [110]: c = np.copy(b)

In [111]: a == b
Out[111]: array([ True,  True,  True,  True,  True])

In [112]: a == c
Out[112]: array([ True,  True,  True,  True,  True])

In [113]: a is b
Out[113]: False

In [114]: a is c
Out[114]: False

In [115]: b is c
Out[115]: False

In [116]: d = a

In [117]: d
Out[117]: array([0.93738312, 0.93412268, 0.86453757, 0.55468707, 0.36503948])

In [118]: d == a
Out[118]: array([ True,  True,  True,  True,  True])

In [119]: d is a
Out[119]: True

In [120]: del d

In [121]: a
Out[121]: array([0.93738312, 0.93412268, 0.86453757, 0.55468707, 0.36503948])

In [122]: d = a

In [123]: d.sort()

In [124]: d
Out[124]: array([0.36503948, 0.55468707, 0.86453757, 0.93412268, 0.93738312])

In [125]: a
Out[125]: array([0.36503948, 0.55468707, 0.86453757, 0.93412268, 0.93738312])

In [126]: d is a
Out[126]: True

In [127]: d == a
Out[127]: array([ True,  True,  True,  True,  True])

In [128]: b == a
Out[128]: array([False, False,  True, False, False])

In [129]: a = np.random.random(5)

In [130]: a
Out[130]: array([0.90063362, 0.63074645, 0.20416973, 0.03845636, 0.60056531])

In [131]: len(a)
Out[131]: 5

In [132]: a.shape
Out[132]: (5,)

In [133]: a.ndim
Out[133]: 1

In [134]: a[0]
Out[134]: 0.9006336214669415

In [135]: a[:2]
Out[135]: array([0.90063362, 0.63074645])

In [136]: a
Out[136]: array([0.90063362, 0.63074645, 0.20416973, 0.03845636, 0.60056531])

In [137]: a = np.random.random(10)

In [138]: a
Out[138]:
array([0.05905415, 0.09015096, 0.80256404, 0.47067378, 0.15206401,
       0.18353202, 0.73042719, 0.34466832, 0.54610601, 0.56930401])

In [139]: i = [3, 7, 5, 2, 7]

In [140]: a[i]
Out[140]: array([0.47067378, 0.34466832, 0.18353202, 0.80256404, 0.34466832])

In [141]: a = np.arange(10)

In [142]: a[i]
Out[142]: array([3, 7, 5, 2, 7])

In [143]: a
Out[143]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In [144]: a[i]
Out[144]: array([3, 7, 5, 2, 7])

In [145]: a = np.random.random(10)

In [146]: a[i]
Out[146]: array([0.51404049, 0.74331624, 0.68632351, 0.51904487, 0.74331624])

In [147]: a[i] = -1

In [148]: a
Out[148]:
array([ 0.62345697,  0.40625338, -1.        , -1.        ,  0.67894066,
       -1.        ,  0.04840348, -1.        ,  0.33904749,  0.21132023])

In [149]: l = list(range(10))

In [150]: l
Out[150]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [151]: l[i]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-151-021c72463b38> in <module>()
----> 1 l[i]

TypeError: list indices must be integers or slices, not list
> <ipython-input-151-021c72463b38>(1)<module>()
----> 1 l[i]

ipdb> c

In [152]: a
Out[152]:
array([ 0.62345697,  0.40625338, -1.        , -1.        ,  0.67894066,
       -1.        ,  0.04840348, -1.        ,  0.33904749,  0.21132023])

In [153]: a = np.random.random(10)

In [154]: a
Out[154]:
array([0.89355442, 0.33720005, 0.09607528, 0.52180477, 0.490364  ,
       0.76004755, 0.63037843, 0.65590122, 0.55949636, 0.77334468])

In [155]: a + 2
Out[155]:
array([2.89355442, 2.33720005, 2.09607528, 2.52180477, 2.490364  ,
       2.76004755, 2.63037843, 2.65590122, 2.55949636, 2.77334468])

In [156]: a - 2
Out[156]:
array([-1.10644558, -1.66279995, -1.90392472, -1.47819523, -1.509636  ,
       -1.23995245, -1.36962157, -1.34409878, -1.44050364, -1.22665532])

In [157]: a * 2
Out[157]:
array([1.78710884, 0.6744001 , 0.19215056, 1.04360954, 0.980728  ,
       1.5200951 , 1.26075685, 1.31180244, 1.11899272, 1.54668936])

In [158]: a / 2
Out[158]:
array([0.44677721, 0.16860003, 0.04803764, 0.26090239, 0.245182  ,
       0.38002378, 0.31518921, 0.32795061, 0.27974818, 0.38667234])

In [159]: a == 1
Out[159]:
array([False, False, False, False, False, False, False, False, False,
       False])

In [160]: i
Out[160]: [3, 7, 5, 2, 7]

In [161]: a[i]
Out[161]: array([0.52180477, 0.65590122, 0.76004755, 0.09607528, 0.65590122])

In [162]: a[i] + 1
Out[162]: array([1.52180477, 1.65590122, 1.76004755, 1.09607528, 1.65590122])

In [163]: i
Out[163]: [3, 7, 5, 2, 7]

In [164]: i + 1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-164-0d38202312c5> in <module>()
----> 1 i + 1

TypeError: can only concatenate list (not "int") to list
> <ipython-input-164-0d38202312c5>(1)<module>()
----> 1 i + 1

ipdb> c

In [165]: i
Out[165]: [3, 7, 5, 2, 7]

In [166]: np.array(i)
Out[166]: array([3, 7, 5, 2, 7])

In [167]: ai = np.array(i)

In [168]: a[ai]
Out[168]: array([0.52180477, 0.65590122, 0.76004755, 0.09607528, 0.65590122])

In [169]: a[i]
Out[169]: array([0.52180477, 0.65590122, 0.76004755, 0.09607528, 0.65590122])

In [170]: a[ai+1]
Out[170]: array([0.490364  , 0.55949636, 0.63037843, 0.52180477, 0.55949636])

In [171]: ai
Out[171]: array([3, 7, 5, 2, 7])

In [172]: ai + 1
Out[172]: array([4, 8, 6, 3, 8])

In [173]: a
Out[173]:
array([0.89355442, 0.33720005, 0.09607528, 0.52180477, 0.490364  ,
       0.76004755, 0.63037843, 0.65590122, 0.55949636, 0.77334468])

In [174]: a == 1
Out[174]:
array([False, False, False, False, False, False, False, False, False,
       False])

In [175]: a > 0.5
Out[175]:
array([ True, False, False,  True, False,  True,  True,  True,  True,
        True])

In [176]: bi = a > 0.5

In [177]: bi
Out[177]:
array([ True, False, False,  True, False,  True,  True,  True,  True,
        True])

In [178]: a[bi]
Out[178]:
array([0.89355442, 0.52180477, 0.76004755, 0.63037843, 0.65590122,
       0.55949636, 0.77334468])

In [179]: a[a > 0.5]
Out[179]:
array([0.89355442, 0.52180477, 0.76004755, 0.63037843, 0.65590122,
       0.55949636, 0.77334468])

In [180]: np.where([a > 0.5])
Out[180]: (array([0, 0, 0, 0, 0, 0, 0]), array([0, 3, 5, 6, 7, 8, 9]))

In [181]:

In [181]:

In [181]:

In [181]:

In [181]:

In [181]:

In [181]:

In [181]:

In [181]:

In [181]:

In [181]:

In [181]:

In [181]:

In [181]: a < 0.5
Out[181]:
array([False,  True,  True, False,  True, False, False, False, False,
       False])

In [182]: a[a < 0.5]
Out[182]: array([0.33720005, 0.09607528, 0.490364  ])

In [183]: a = np.array([1, 2, 3])

In [184]: b = np.array([4, 5, 6])

In [185]: a
Out[185]: array([1, 2, 3])

In [186]: b
Out[186]: array([4, 5, 6])

In [187]: [a, b]
Out[187]: [array([1, 2, 3]), array([4, 5, 6])]

In [188]: l = [a,b]

In [189]: type(l)
Out[189]: list

In [190]: l[0]
Out[190]: array([1, 2, 3])

In [191]: l[1]
Out[191]: array([4, 5, 6])

In [192]: [a, b]
Out[192]: [array([1, 2, 3]), array([4, 5, 6])]

In [193]: np.concatenate([a, b])
Out[193]: array([1, 2, 3, 4, 5, 6])

In [194]: a + 1
Out[194]: array([2, 3, 4])

In [195]: 'sdfsdf' + 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-195-02f5350b304b> in <module>()
----> 1 'sdfsdf' + 2

TypeError: Can't convert 'int' object to str implicitly
> <ipython-input-195-02f5350b304b>(1)<module>()
----> 1 'sdfsdf' + 2

ipdb> c

In [196]: 'sdfsdf' * 2
Out[196]: 'sdfsdfsdfsdf'

In [197]: 'sdfsdf' + 'werwerw'
Out[197]: 'sdfsdfwerwerw'

In [198]: l
Out[198]: [array([1, 2, 3]), array([4, 5, 6])]

In [199]: l[0] + l[1]
Out[199]: array([5, 7, 9])

In [200]: np.array([1,2,3]) + np.array([4,5,6])
Out[200]: array([5, 7, 9])

In [201]: np.array([1,2,3]) - np.array([4,5,6])
Out[201]: array([-3, -3, -3])

In [202]: np.array([1,2,3]) * np.array([4,5,6])
Out[202]: array([ 4, 10, 18])

In [203]: np.array([1,2,3]) ** np.array([4,5,6])
Out[203]: array([  1,  32, 729])

In [204]: a
Out[204]: array([1, 2, 3])

In [205]: a + 1
Out[205]: array([2, 3, 4])

In [206]: c = 5

In [207]: c += 1

In [208]: c
Out[208]: 6

In [209]: a + 1
Out[209]: array([2, 3, 4])

In [210]: a
Out[210]: array([1, 2, 3])

In [211]: a += 1

In [212]: a
Out[212]: array([2, 3, 4])

In [213]: a += 1

In [214]: a += 1

In [215]: a += 1

In [216]: a += 1

In [217]: a += 1

In [218]: a
Out[218]: array([7, 8, 9])

In [219]: a -= 1

In [220]: a -= 1

In [221]: a -= 1

In [222]: a -= 1

In [223]: a -= 1

In [224]: a -= 1

In [225]: a -= 1

In [226]: a -= 1

In [227]: a
Out[227]: array([-1,  0,  1])

In [228]: np.sqrt()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-228-136fd2b92199> in <module>()
----> 1 np.sqrt()

ValueError: invalid number of arguments
> <ipython-input-228-136fd2b92199>(1)<module>()
----> 1 np.sqrt()

ipdb> c

In [229]: np.sqrt
Out[229]: <ufunc 'sqrt'>

In [230]: np.mean
Out[230]: <function numpy.core.fromnumeric.mean(a, axis=None, dtype=None, out=None, keepdims=<class 'numpy._globals._NoValue'>)>

In [231]: a
Out[231]: array([-1,  0,  1])

In [232]: a.mean()
Out[232]: 0.0

In [233]: np.average?

In [234]: a.mean()
Out[234]: 0.0

In [235]: np.zeros
Out[235]: <function numpy.core.multiarray.zeros>

In [236]: np.zeros(5)
Out[236]: array([0., 0., 0., 0., 0.])

In [237]: [ np.zeros(5), np.zeros(5), np.zeros(5) ]
Out[237]:
[array([0., 0., 0., 0., 0.]),
 array([0., 0., 0., 0., 0.]),
 array([0., 0., 0., 0., 0.])]

In [238]: np.tile(np.zeros(5), 3)
Out[238]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

In [239]: l = []

In [240]: for i in range(3);
  File "<ipython-input-240-5b00b1aba38a>", line 1
    for i in range(3);
                     ^
SyntaxError: invalid syntax


In [241]: for i in range(3):
     ...:     l.append(np.zeros(5))
     ...:

In [242]: l
Out[242]:
[array([0., 0., 0., 0., 0.]),
 array([0., 0., 0., 0., 0.]),
 array([0., 0., 0., 0., 0.])]

In [243]: a = np.array([10, 20, 30,
     ...: 40, 50])

In [244]: b = np.array([5, 10, 15, 20, 25])

In [245]: a - b
Out[245]: array([ 5, 10, 15, 20, 25])

In [246]: np.mean(a - b)
Out[246]: 15.0

In [247]: a - b
Out[247]: array([ 5, 10, 15, 20, 25])

In [248]: c = a - b

In [249]: c.mean()
Out[249]: 15.0

In [250]: (a - b).mean()
Out[250]: 15.0

In [251]: a.mean() - b.mean()
Out[251]: 15.0

In [252]:

In [252]: a
Out[252]: array([10, 20, 30, 40, 50])

In [253]: b
Out[253]: array([ 5, 10, 15, 20, 25])

In [254]: c = np.array([1,2,3])

In [255]: c
Out[255]: array([1, 2, 3])

In [256]: a
Out[256]: array([10, 20, 30, 40, 50])

In [257]: a + c
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-257-e81e582b6fa9> in <module>()
----> 1 a + c

ValueError: operands could not be broadcast together with shapes (5,) (3,)
> <ipython-input-257-e81e582b6fa9>(1)<module>()
----> 1 a + c

ipdb> c

In [258]: x = np.random.random(10)

In [259]: x
Out[259]:
array([0.63242915, 0.30956196, 0.8158855 , 0.80591226, 0.93027787,
       0.72828754, 0.81700785, 0.10470338, 0.2478481 , 0.45255019])

In [260]: np.sqrt(x)
Out[260]:
array([0.79525414, 0.55638293, 0.9032638 , 0.89772616, 0.96450913,
       0.85339764, 0.90388486, 0.32357901, 0.49784344, 0.67271851])

In [261]: def rms(x):
     ...:     return np.sqrt(np.mean(x**2))
     ...:
     ...:

In [262]: rms(x)
Out[262]: 0.6443192973240945

In [263]: rms([234,2,4,1])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-263-ad83bdee9fde> in <module>()
----> 1 rms([234,2,4,1])

<ipython-input-261-532123607e2e> in rms(x)
      1 def rms(x):
----> 2     return np.sqrt(np.mean(x**2))

TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
> <ipython-input-261-532123607e2e>(2)rms()
      1 def rms(x):
----> 2     return np.sqrt(np.mean(x**2))

ipdb> c

In [264]: def rms(x):
     ...:     x = np.array(x)
     ...:     return np.sqrt(np.mean(x**2))
     ...:
     ...:
     ...:

In [265]:

In [265]: rms([234,2,4,1])
Out[265]: 117.02243374669662

In [266]: a - b
Out[266]: array([ 5, 10, 15, 20, 25])

In [267]: rms(a - b)
Out[267]: 16.583123951777

In [268]:
