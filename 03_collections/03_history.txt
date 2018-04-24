mspacek@Godel:~/SciPyCourse2018/notes/03_collections$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.3.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: def test():
   ...:     print('hi')
   ...:

In [2]: test()
hi

In [3]: a = test()
hi

In [4]: a

In [5]: type(a)
Out[5]: NoneType

In [6]: None

In [7]: a == None
Out[7]: True

In [8]:





In [8]:

In [8]: def test():
   ...:     print('hi')
   ...:     return
   ...:
   ...:

In [9]: a = test()
hi

In [10]: a

In [11]: type(a)
Out[11]: NoneType

In [12]: a == None
Out[12]: True

In [13]: type(return)
  File "<ipython-input-13-00945b484227>", line 1
    type(return)
              ^
SyntaxError: invalid syntax


In [14]: help('return')

Related help topics: FUNCTIONS


In [15]: return(5)
  File "<ipython-input-15-865680d9eefb>", line 1
    return(5)
             ^
SyntaxError: 'return' outside function


In [16]: def test():
    ...:     print('hi')
    ...:     return(5)
    ...:
    ...:
    ...:
    ...:

In [17]: a = test()
hi

In [18]: a
Out[18]: 5

In [19]: def test():
    ...:     print('hi')
    ...:     return 5
    ...:
    ...:
    ...:

In [20]: a = test()
hi

In [21]: a
Out[21]: 5

In [22]: print?
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method

In [23]: type(print)
Out[23]: builtin_function_or_method

In [24]: type(return)
  File "<ipython-input-24-00945b484227>", line 1
    type(return)
              ^
SyntaxError: invalid syntax


In [25]: def test(x):
    ...:     if x > 0:
    ...:         return 1
    ...:     return -1
    ...:
    ...:
    ...:
    ...:
    ...:

In [26]: test(5)
Out[26]: 1

In [27]: test(-2)
Out[27]: -1

In [28]: def test(x):
    ...:     return x
    ...:
    ...:

In [29]: test(5)
Out[29]: 5

In [30]: def test(x):
    ...:     a = 5;
    ...:     return a
    ...:
    ...:

In [31]: a = 5

In [32]: b = 6

In [33]: 'dlfkjsl some really long string sldjflsk lskjdlfkjsdlf lkjldkfj'
Out[33]: 'dlfkjsl some really long string sldjflsk lskjdlfkjsdlf lkjldkfj'

In [34]: ('dlfkjsl some really long string sldjflsklskjdlfkjsdlf lkjldkfj')
Out[34]: 'dlfkjsl some really long string sldjflsklskjdlfkjsdlf lkjldkfj'

In [35]: ('dlfkjsl some really long stringsldjflsklskjdlfkjsdlf lkjldkfj')
Out[35]: 'dlfkjsl some really long stringsldjflsklskjdlfkjsdlf lkjldkfj'

In [36]: ('dlfkjsl some really long stringsldjflsklskjdlfkjsdlf lkjldkfj')
Out[36]: 'dlfkjsl some really long stringsldjflsklskjdlfkjsdlf lkjldkfj'

In [37]: ('dlfkjsl some really long stringsldjflsklskjdlfkjsdlf lkjldkfj')
Out[37]: 'dlfkjsl some really long stringsldjflsklskjdlfkjsdlf lkjldkfj'

In [38]:

In [38]:

In [38]: s = 'hi'

In [39]: s.lower?
Docstring:
S.lower() -> str

Return a copy of the string S converted to lowercase.
Type:      builtin_function_or_method

In [40]: s = 'HI'

In [41]: s.lower()
Out[41]: 'hi'

In [42]: s
Out[42]: 'HI'

In [43]: nv
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-43-a94cf9656c24> in <module>()
----> 1 nv

NameError: name 'nv' is not defined
> <ipython-input-43-a94cf9656c24>(1)<module>()
----> 1 nv

ipdb> c

In [44]: nv += 1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-44-545e99e37f55> in <module>()
----> 1 nv += 1

NameError: name 'nv' is not defined
> <ipython-input-44-545e99e37f55>(1)<module>()
----> 1 nv += 1

ipdb> c

In [45]: 1 / 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-45-bc757c3fda29> in <module>()
----> 1 1 / 0

ZeroDivisionError: division by zero
> <ipython-input-45-bc757c3fda29>(1)<module>()
----> 1 1 / 0

ipdb> c

In [46]: for i in range(1, 10):
    ...:     print(i)
    ...:
1
2
3
4
5
6
7
8
9

In [47]: for i in range(1, 11):
    ...:     print(i)
    ...:
1
2
3
4
5
6
7
8
9
10

In [48]: help?
Signature:   help(*args, **kwds)
Type:        _Helper
String form: Type help() for interactive help, or help(object) for help about object.
Namespace:   Python builtin
File:        /usr/lib/python3.5/_sitebuiltins.py
Docstring:
Define the builtin 'help'.

This is a wrapper around pydoc.help that provides a helpful message
when 'help' is typed at the Python interactive prompt.

Calling help() at the Python prompt starts an interactive help session.
Calling help(thing) prints help for the python object 'thing'.

In [49]: print?
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method

In [50]:

In [50]:

In [50]:

In [50]:

In [50]:

In [50]:


In [50]:

In [50]:

In [50]:

In [50]:

In [50]:
^[[26;1R
In [50]:

In [50]:
^[[26;1R^[[26;1R
In [50]:

In [50]:

In [50]:

In [50]: print?
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method

In [51]: print('hi')
hi

In [52]: print('hi', end=' ')
hi
In [53]: print('hi', end='sldkjf')
hisldkjf
In [54]: print('hi', end='')
hi
In [55]: print(5)
5

In [56]: print(str(5))
5

In [57]: print()


In [58]: (1, 2)
Out[58]: (1, 2)

In [59]: (1, 2, 3)
Out[59]: (1, 2, 3)

In [60]: t = (1, 2, 3)

In [61]: type(t)
Out[61]: tuple

In [62]: t = 1, 2, 3

In [63]: type(t)
Out[63]: tuple

In [64]: t
Out[64]: (1, 2, 3)

In [65]: t = 4, 5, 6

In [66]: t
Out[66]: (4, 5, 6)

In [67]: t = 'a', True, 4.5

In [68]: t
Out[68]: ('a', True, 4.5)

In [69]:

In [69]: def mult123(x):
    ...:     return x, 2*x, 3*x
    ...:
    ...:

In [70]: mult123(2)
Out[70]: (2, 4, 6)

In [71]: t = mult123(2)

In [72]: type(t)
Out[72]: tuple

In [73]: t
Out[73]: (2, 4, 6)

In [74]: t
Out[74]: (2, 4, 6)

In [75]: t * 2
Out[75]: (2, 4, 6, 2, 4, 6)

In [76]: t * 2
Out[76]: (2, 4, 6, 2, 4, 6)

In [77]: t + 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-77-3753f0400dec> in <module>()
----> 1 t + 2

TypeError: can only concatenate tuple (not "int") to tuple
> <ipython-input-77-3753f0400dec>(1)<module>()
----> 1 t + 2

ipdb> c

In [78]: t + t
Out[78]: (2, 4, 6, 2, 4, 6)

In [79]: len(t)
Out[79]: 3

In [80]: t
Out[80]: (2, 4, 6)

In [81]: t[0]
Out[81]: 2

In [82]: t[0]
Out[82]: 2

In [83]: type(t[0])
Out[83]: int

In [84]: t[-1]
Out[84]: 6

In [85]: t = 1, 2, 3, 4, 5

In [86]: t[::2]
Out[86]: (1, 3, 5)

In [87]: t[::2]
Out[87]: (1, 3, 5)

In [88]: t
Out[88]: (1, 2, 3, 4, 5)

In [89]: t.count?
Docstring: T.count(value) -> integer -- return number of occurrences of value
Type:      builtin_function_or_method

In [90]: t.count(3)
Out[90]: 1

In [91]: t.count(10)
Out[91]: 0

In [92]: t.index(3)
Out[92]: 2

In [93]: s = 'hello'

In [94]: s[1] = '3'
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-94-71f91e291bb8> in <module>()
----> 1 s[1] = '3'

TypeError: 'str' object does not support item assignment
> <ipython-input-94-71f91e291bb8>(1)<module>()
----> 1 s[1] = '3'

ipdb> c

In [95]: t[0] = 5
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-95-6dd06f73cec4> in <module>()
----> 1 t[0] = 5

TypeError: 'tuple' object does not support item assignment
> <ipython-input-95-6dd06f73cec4>(1)<module>()
----> 1 t[0] = 5

ipdb> c

In [96]: t
Out[96]: (1, 2, 3, 4, 5)

In [97]: t = 1, 2, 3

In [98]: t
Out[98]: (1, 2, 3)

In [99]: a = t[0]

In [100]: b = t[1]

In [101]: c = t[2]

In [102]: a
Out[102]: 1

In [103]:

In [103]: b
Out[103]: 2

In [104]: c
Out[104]: 3

In [105]: a, b, c = t

In [106]: a
Out[106]: 1

In [107]: b
Out[107]: 2

In [108]: c
Out[108]: 3

In [109]: a, b, c, d = t
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-109-717d2ab55525> in <module>()
----> 1 a, b, c, d = t

ValueError: not enough values to unpack (expected 4, got 3)
> <ipython-input-109-717d2ab55525>(1)<module>()
----> 1 a, b, c, d = t

ipdb> c

In [110]: a, b = t
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-110-b0af552e832d> in <module>()
----> 1 a, b = t

ValueError: too many values to unpack (expected 2)
> <ipython-input-110-b0af552e832d>(1)<module>()
----> 1 a, b = t

ipdb> c

In [111]: len(t)
Out[111]: 3

In [112]: l = [1, 2, 3]

In [113]: l
Out[113]: [1, 2, 3]

In [114]: type(l)
Out[114]: list

In [115]: l = [True, 'sdf', 5.2]

In [116]: l
Out[116]: [True, 'sdf', 5.2]

In [117]: l[0] = False

In [118]: l
Out[118]: [False, 'sdf', 5.2]

In [119]: l = []

In [120]: l
Out[120]: []

In [121]: len(l)
Out[121]: 0

In [122]: l.append(2)

In [123]: l
Out[123]: [2]

In [124]: len(l)
Out[124]: 1

In [125]: l.append(4)

In [126]: l.append(6)

In [127]: l.append(8)

In [128]: l.append(10)

In [129]: l
Out[129]: [2, 4, 6, 8, 10]

In [130]: l = [2, 4, 6, 8, 10]

In [131]: range(2, 11, 2)
Out[131]: range(2, 11, 2)

In [132]: list(range(2, 11, 2))
Out[132]: [2, 4, 6, 8, 10]

In [133]: list()
Out[133]: []

In [134]: l = list()

In [135]: l = []

In [136]: list(range(2, 11, 2))
Out[136]: [2, 4, 6, 8, 10]

In [137]: range(2, 11, 2)
Out[137]: range(2, 11, 2)

In [138]: t
Out[138]: (1, 2, 3)

In [139]: list(t)
Out[139]: [1, 2, 3]

In [140]: l
Out[140]: []

In [141]: l = list(range(10))

In [142]: l
Out[142]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [143]: l[::3]
Out[143]: [0, 3, 6, 9]

In [144]: l[::-3]
Out[144]: [9, 6, 3, 0]

In [145]: l[::-1]
Out[145]: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

In [146]: l[-1]
Out[146]: 9

In [147]: for val in l:
     ...:     print(val)
     ...:
0
1
2
3
4
5
6
7
8
9

In [148]: s = 'stuff'

In [149]: for c in s:
     ...:     print(c)
     ...:
s
t
u
f
f

In [150]: for i in range(len(s));
  File "<ipython-input-150-371032dbf822>", line 1
    for i in range(len(s));
                          ^
SyntaxError: invalid syntax


In [151]: for i in range(len(s)):
     ...:     c = s[i]
     ...:     print(c)
     ...:
s
t
u
f
f

In [152]: for val in l:
     ...:     print(val)
     ...:
0
1
2
3
4
5
6
7
8
9

In [153]: l
Out[153]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [154]: 11 in l
Out[154]: False

In [155]: 5 in l
Out[155]: True

In [156]: l.extend([11, 12, 13])

In [157]: l
Out[157]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]

In [158]: l = 4, 6, 2, 7, 8, 3, 2

In [159]: l = list(l)

In [160]: l
Out[160]: [4, 6, 2, 7, 8, 3, 2]

In [161]: l.sort?
Docstring: L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
Type:      builtin_function_or_method

In [162]: l = [4, 6, 2, 7, 8, 3, 2]

In [163]: l.sort?
Docstring: L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
Type:      builtin_function_or_method

In [164]: l.sort()

In [165]: l
Out[165]: [2, 2, 3, 4, 6, 7, 8]

In [166]: l
Out[166]: [2, 2, 3, 4, 6, 7, 8]

In [167]: del l[0]

In [168]: l
Out[168]: [2, 3, 4, 6, 7, 8]

In [169]: del l[-1]

In [170]: l
Out[170]: [2, 3, 4, 6, 7]

In [171]: l.clear()

In [172]: l
Out[172]: []

In [173]: l = []

In [174]: l.reverse?
Docstring: L.reverse() -- reverse *IN PLACE*
Type:      builtin_function_or_method

In [175]: l
Out[175]: []

In [176]: l = [4, 6, 2, 7, 8, 3, 2]

In [177]: l.reverse()

In [178]: l
Out[178]: [2, 3, 8, 7, 2, 6, 4]

In [179]: l[::-1]
Out[179]: [4, 6, 2, 7, 8, 3, 2]

In [180]: l.reverse()

In [181]: l
Out[181]: [4, 6, 2, 7, 8, 3, 2]

In [182]: l
Out[182]: [4, 6, 2, 7, 8, 3, 2]

In [183]: tuple(l)
Out[183]: (4, 6, 2, 7, 8, 3, 2)

In [184]: list(tuple(l))
Out[184]: [4, 6, 2, 7, 8, 3, 2]

In [185]: l
Out[185]: [4, 6, 2, 7, 8, 3, 2]

In [186]: sorted(l)
Out[186]: [2, 2, 3, 4, 6, 7, 8]

In [187]: l
Out[187]: [4, 6, 2, 7, 8, 3, 2]

In [188]: l.sort()

In [189]: l
Out[189]: [2, 2, 3, 4, 6, 7, 8]

In [190]: max?
Docstring:
max(iterable, *[, default=obj, key=func]) -> value
max(arg1, arg2, *args, *[, key=func]) -> value

With a single iterable argument, return its biggest item. The
default keyword-only argument specifies an object to return if
the provided iterable is empty.
With two or more arguments, return the largest argument.
Type:      builtin_function_or_method

In [191]: l.insert?
Docstring: L.insert(index, object) -- insert object before index
Type:      builtin_function_or_method

In [192]: l
Out[192]: [2, 2, 3, 4, 6, 7, 8]

In [193]: l.insert(3, 'three')

In [194]: l
Out[194]: [2, 2, 3, 'three', 4, 6, 7, 8]

In [195]: 1e2
Out[195]: 100.0

In [196]: t = 3, 5, 1.7, -2.7, 1e2, -50

In [197]: t
Out[197]: (3, 5, 1.7, -2.7, 100.0, -50)

In [198]: t[::2]
Out[198]: (3, 1.7, 100.0)

In [199]: l = list(t)

In [200]: l
Out[200]: [3, 5, 1.7, -2.7, 100.0, -50]

In [201]: l.sort()

In [202]: l.sort
Out[202]: <function list.sort>

In [203]: l
Out[203]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [204]: l.sort()

In [205]: l
Out[205]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [206]: sorted(l)
Out[206]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [207]: l
Out[207]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [208]: l.append('blah')

In [209]: l
Out[209]: [-50, -2.7, 1.7, 3, 5, 100.0, 'blah']

In [210]: l.sort()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-210-fb07ac7c73ab> in <module>()
----> 1 l.sort()

TypeError: unorderable types: str() < float()
> <ipython-input-210-fb07ac7c73ab>(1)<module>()
----> 1 l.sort()

ipdb> c

In [211]: del l[-1]

In [212]: l
Out[212]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [213]: l.remove?
Docstring:
L.remove(value) -> None -- remove first occurrence of value.
Raises ValueError if the value is not present.
Type:      builtin_function_or_method

In [214]: l.remove(-2.7)

In [215]: l
Out[215]: [-50, 1.7, 3, 5, 100.0]

In [216]: l.pop?
Docstring:
L.pop([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.
Type:      builtin_function_or_method

In [217]: l.pop[0]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-217-61a379b73811> in <module>()
----> 1 l.pop[0]

TypeError: 'builtin_function_or_method' object is not subscriptable
> <ipython-input-217-61a379b73811>(1)<module>()
----> 1 l.pop[0]

ipdb> c

In [218]: l.pop(0)
Out[218]: -50

In [219]: l
Out[219]: [1.7, 3, 5, 100.0]

In [220]: l = [3, 5, 1.7, -2.7, 1e2, -50]

In [221]: l.sort()

In [222]: l
Out[222]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [223]: l
Out[223]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [224]: l.reverse?
Docstring: L.reverse() -- reverse *IN PLACE*
Type:      builtin_function_or_method

In [225]: l.reverse()

In [226]: l
Out[226]: [100.0, 5, 3, 1.7, -2.7, -50]

In [227]: l.reverse()

In [228]: l
Out[228]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [229]: l.sort?
Docstring: L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
Type:      builtin_function_or_method

In [230]: l.sort(reverse=True)

In [231]: l
Out[231]: [100.0, 5, 3, 1.7, -2.7, -50]

In [232]: l.sort(reverse=True)

In [233]: l
Out[233]: [100.0, 5, 3, 1.7, -2.7, -50]

In [234]: l.sort()

In [235]: l
Out[235]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [236]: l[::-1]
Out[236]: [100.0, 5, 3, 1.7, -2.7, -50]

In [237]: t = 3, 5, 1.7, -2.7, 1e2, -50

In [238]: t
Out[238]: (3, 5, 1.7, -2.7, 100.0, -50)

In [239]: out = []

In [240]: for i in l:
     ...:     out.append(2*i)
     ...:

In [241]: out
Out[241]: [-100, -5.4, 3.4, 6, 10, 200.0]

In [242]: l
Out[242]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [243]: out
Out[243]: [-100, -5.4, 3.4, 6, 10, 200.0]

In [244]: [ 2*i for i in l ]
Out[244]: [-100, -5.4, 3.4, 6, 10, 200.0]

In [245]: out = [ 2*i for i in l ]

In [246]: out
Out[246]: [-100, -5.4, 3.4, 6, 10, 200.0]

In [247]: [ 2*val for val in l ]
Out[247]: [-100, -5.4, 3.4, 6, 10, 200.0]

In [248]: [ 2*val for val in l ]
Out[248]: [-100, -5.4, 3.4, 6, 10, 200.0]

In [249]: def multlist(seq, x):
     ...:     out = []
     ...:     for val in seq:
     ...:         out.append(val * x)
     ...:

In [250]:

In [250]: multlist(l, 5)

In [251]: def multlist(seq, x):
     ...:     out = []
     ...:     for val in seq:
     ...:         out.append(val * x)
     ...:     return out
     ...:
     ...:

In [252]: multlist(l, 5)
Out[252]: [-250, -13.5, 8.5, 15, 25, 500.0]

In [253]: l
Out[253]: [-50, -2.7, 1.7, 3, 5, 100.0]

In [254]: multlist(l, 10)
Out[254]: [-500, -27.0, 17.0, 30, 50, 1000.0]

In [255]: def multlist2(seq, x):
     ...:     return [ val*x for val in seq ]
     ...:
     ...:

In [256]: multlist2(l, 5)
Out[256]: [-250, -13.5, 8.5, 15, 25, 500.0]

In [257]: {}
Out[257]: {}

In [258]: type({})
Out[258]: dict

In [259]: d = {}

In [260]: d = dict()

In [261]: d
Out[261]: {}

In [262]: d = {'a':1, 'b':2}

In [263]: len(d)
Out[263]: 2

In [264]: names2ages = {'Alice':25, 'Bob':20, 'Carol':32}

In [265]: names2ages = {'Alice':25, 'Bob':20, 'Carol':32}

In [266]: ages2names = {25:'Alice', 20:'Bob', 32:'Carol'}

In [267]: ages2names = {25:'Alice', 20:'Bob', 32:'Carol', 25:'George'}

In [268]: ages2names
Out[268]: {20: 'Bob', 25: 'George', 32: 'Carol'}

In [269]: ages2names = {25:'Alice', 20:'Bob', 32:'Carol'}

In [270]: ages2names
Out[270]: {20: 'Bob', 25: 'Alice', 32: 'Carol'}

In [271]: names2ages
Out[271]: {'Alice': 25, 'Bob': 20, 'Carol': 32}

In [272]: names2ages['Alice']
Out[272]: 25

In [273]: names2ages['Bob']
Out[273]: 20

In [274]: names2ages[20]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-274-6e8c698035b6> in <module>()
----> 1 names2ages[20]

KeyError: 20
> <ipython-input-274-6e8c698035b6>(1)<module>()
----> 1 names2ages[20]

ipdb> c

In [275]: ages2names
Out[275]: {20: 'Bob', 25: 'Alice', 32: 'Carol'}

In [276]: names2ages
Out[276]: {'Alice': 25, 'Bob': 20, 'Carol': 32}

In [277]: names2ages['Alice'] = 5

In [278]: names2ages
Out[278]: {'Alice': 5, 'Bob': 20, 'Carol': 32}

In [279]: names2ages['George'] = 15

In [280]: names2ages
Out[280]: {'Alice': 5, 'Bob': 20, 'Carol': 32, 'George': 15}

In [281]: del names2ages['George']

In [282]: names2ages
Out[282]: {'Alice': 5, 'Bob': 20, 'Carol': 32}

In [283]: del names2ages['Matilda']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-283-eeece7fce9ff> in <module>()
----> 1 del names2ages['Matilda']

KeyError: 'Matilda'
> <ipython-input-283-eeece7fce9ff>(1)<module>()
----> 1 del names2ages['Matilda']

ipdb> c

In [284]: names2ages
Out[284]: {'Alice': 5, 'Bob': 20, 'Carol': 32}

In [285]: d = names2ages

In [286]: d
Out[286]: {'Alice': 5, 'Bob': 20, 'Carol': 32}

In [287]: d.keys()
Out[287]: dict_keys(['Alice', 'Bob', 'Carol'])

In [288]: d.keys?
Docstring: D.keys() -> a set-like object providing a view on D's keys
Type:      builtin_function_or_method

In [289]: d.keys()
Out[289]: dict_keys(['Alice', 'Bob', 'Carol'])

In [290]: type(d.keys())
Out[290]: dict_keys

In [291]: d.keys()
Out[291]: dict_keys(['Alice', 'Bob', 'Carol'])

In [292]: list(d.keys())
Out[292]: ['Alice', 'Bob', 'Carol']

In [293]: tuple(d.keys())
Out[293]: ('Alice', 'Bob', 'Carol')

In [294]: keys = tuple(d.keys())

In [295]: keys
Out[295]: ('Alice', 'Bob', 'Carol')

In [296]: values = 10, 20, 30

In [297]: d.fromkeys?
Signature: d.fromkeys(iterable, value=None, /)
Docstring: Returns a new dict with keys from iterable and values equal to value.
Type:      builtin_function_or_method

In [298]: dict?
Init signature: dict(self, /, *args, **kwargs)
Docstring:
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
Type:           type

In [299]: dict(keys, values)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-299-6d6764120acd> in <module>()
----> 1 dict(keys, values)

TypeError: dict expected at most 1 arguments, got 2
> <ipython-input-299-6d6764120acd>(1)<module>()
----> 1 dict(keys, values)

ipdb> c

In [300]: dict((keys, values))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-300-2fd08f5030fb> in <module>()
----> 1 dict((keys, values))

ValueError: dictionary update sequence element #0 has length 3; 2 is required
> <ipython-input-300-2fd08f5030fb>(1)<module>()
----> 1 dict((keys, values))

ipdb> c

In [301]: {}.fromkeys(keys)
Out[301]: {'Alice': None, 'Bob': None, 'Carol': None}

In [302]: {}.fromkeys(keys, values)
Out[302]: {'Alice': (10, 20, 30), 'Bob': (10, 20, 30), 'Carol': (10, 20, 30)}

In [303]: {}.fromkeys?
Object `fromkeys` not found.

In [304]: dict.fromkeys?
Signature: dict.fromkeys(iterable, value=None, /)
Docstring: Returns a new dict with keys from iterable and values equal to value.
Type:      builtin_function_or_method

In [305]: {}.fromkeys(keys, values)
Out[305]: {'Alice': (10, 20, 30), 'Bob': (10, 20, 30), 'Carol': (10, 20, 30)}

In [306]: {}.fromkeys(keys, *values)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-306-3f0b1c3b8a0f> in <module>()
----> 1 {}.fromkeys(keys, *values)

TypeError: fromkeys expected at most 2 arguments, got 4
> <ipython-input-306-3f0b1c3b8a0f>(1)<module>()
----> 1 {}.fromkeys(keys, *values)

ipdb> c

In [307]: d
Out[307]: {'Alice': 5, 'Bob': 20, 'Carol': 32}

In [308]: list(d.values())
Out[308]: [5, 20, 32]

In [309]: d.items()
Out[309]: dict_items([('Alice', 5), ('Bob', 20), ('Carol', 32)])

In [310]: list(d.items())
Out[310]: [('Alice', 5), ('Bob', 20), ('Carol', 32)]

In [311]: for key, val in d.items():
     ...:     print(key, val)
     ...:
Alice 5
Bob 20
Carol 32

In [312]: d2 = {}

In [313]: for key, val in d.items():
     ...:     d2[key] = val * 2
     ...:
     ...:

In [314]: d2
Out[314]: {'Alice': 10, 'Bob': 40, 'Carol': 64}

In [315]: d
Out[315]: {'Alice': 5, 'Bob': 20, 'Carol': 32}

In [316]: { key:val*2 for key, val in d.items() }
Out[316]: {'Alice': 10, 'Bob': 40, 'Carol': 64}

In [317]: for something in d:
     ...:     print(something)
     ...:
Alice
Bob
Carol

In [318]: for val in d.values():
     ...:     print(val)
     ...:
5
20
32

In [319]:

In [319]:

In [319]:

In [319]:

In [319]:

In [319]:

In [319]: [(1, 2), (2, 3), (4, 5)]
Out[319]: [(1, 2), (2, 3), (4, 5)]

In [320]: l = [(1, 2), (2, 3), (4, 5)]

In [321]: len(l)
Out[321]: 3

In [322]: l[0]
Out[322]: (1, 2)

In [323]: l[0][-1]
Out[323]: 2

In [324]: l[0,-1]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-324-c80ae3eb0798> in <module>()
----> 1 l[0,-1]

TypeError: list indices must be integers or slices, not tuple
> <ipython-input-324-c80ae3eb0798>(1)<module>()
----> 1 l[0,-1]

ipdb> c

In [325]: {'Alice':[20, 170], 'Bob':[30, 180]}
Out[325]: {'Alice': [20, 170], 'Bob': [30, 180]}

In [326]: d = {'Alice':[20, 170], 'Bob':[30, 180]}

In [327]: dl = {'Alice':[20, 170], 'Bob':[30, 180]}

In [328]: dl['Carol'] = 'stuff'

In [329]: dl
Out[329]: {'Alice': [20, 170], 'Bob': [30, 180], 'Carol': 'stuff'}

In [330]: {'Alice': {'height': 170, 'age':20}}
Out[330]: {'Alice': {'age': 20, 'height': 170}}

In [331]: {'Alice': {'height': 170, 'age':20}}
Out[331]: {'Alice': {'age': 20, 'height': 170}}

In [332]: d = [{'a':1, 'b':2}, {'c':3, 'd':4}]

In [333]: l = [{'a':1, 'b':2}, {'c':3, 'd':4}]

In [334]: l
Out[334]: [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]

In [335]: type(l)
Out[335]: list

In [336]: l[1]
Out[336]: {'c': 3, 'd': 4}

In [337]: l[1]
Out[337]: {'c': 3, 'd': 4}

In [338]: l[1]['e'] = 5

In [339]: l
Out[339]: [{'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

In [340]: l[0]
Out[340]: {'a': 1, 'b': 2}

In [341]: l[0]['e'] = 5

In [342]: l[0]
Out[342]: {'a': 1, 'b': 2, 'e': 5}

In [343]: d2 = l[0]

In [344]: d2
Out[344]: {'a': 1, 'b': 2, 'e': 5}

In [345]: l = [{'a':1, 'b':2}, {'c':3, 'd':4}]

In [346]: l[1]
Out[346]: {'c': 3, 'd': 4}

In [347]: d2 = l[1]

In [348]: d2['e'] = 5

In [349]: d2
Out[349]: {'c': 3, 'd': 4, 'e': 5}

In [350]: l
Out[350]: [{'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

In [351]: l
Out[351]: [{'a': 1, 'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

In [352]: l[0]
Out[352]: {'a': 1, 'b': 2}

In [353]: del l[0]['a']

In [354]: l
Out[354]: [{'b': 2}, {'c': 3, 'd': 4, 'e': 5}]

In [355]: a = [1, 2, 3]

In [356]: b = a

In [357]: b
Out[357]: [1, 2, 3]

In [358]: a
Out[358]: [1, 2, 3]

In [359]: b[2] = 666

In [360]: b
Out[360]: [1, 2, 666]

In [361]: a
Out[361]: [1, 2, 666]

In [362]: a.copy?
Docstring: L.copy() -> list -- a shallow copy of L
Type:      builtin_function_or_method

In [363]: a = [1,2,3]

In [364]: b = a.copy()

In [365]: b
Out[365]: [1, 2, 3]

In [366]: b[2] = 666

In [367]: b
Out[367]: [1, 2, 666]

In [368]: a
Out[368]: [1, 2, 3]

In [369]: b = a

In [370]: b
Out[370]: [1, 2, 3]

In [371]: a
Out[371]: [1, 2, 3]

In [372]: a[0] = 'fun'

In [373]: a
Out[373]: ['fun', 2, 3]

In [374]: b
Out[374]: ['fun', 2, 3]

In [375]: a = [1,2,3]

In [376]: b = a

In [377]: a = 10

In [378]: b = a

In [379]: b = 5

In [380]: a
Out[380]: 10

In [381]:
