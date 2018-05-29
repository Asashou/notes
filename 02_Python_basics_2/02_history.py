
mspacek@Godel:~/SciPyCourse2018/notes$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
mspacek@Godel:~/SciPyCourse2018/notes$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
mspacek@Godel:~/SciPyCourse2018/notes$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
mspacek@Godel:~/SciPyCourse2018/notes$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]:

In [1]:

In [1]:

In [1]:

In [1]: a = 2

In [2]: print(a)
2

In [3]: 1 + 1
Out[3]: 2

In [4]: 2 * 23423 / 2
Out[4]: 23423.0

In [5]: _4
Out[5]: 23423.0

In [6]: b = _4

In [7]: b
Out[7]: 23423.0

In [8]: ?

In [9]: ?

In [10]: s = 'hello'

In [11]: s?
Type:        str
String form: hello
Length:      5
Docstring:
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.

In [12]: type(s)
Out[12]: str

In [13]: s?
Type:        str
String form: hello
Length:      5
Docstring:
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.

In [14]: something = 'ssldkjfsldkfj'

In [15]: something
Out[15]: 'ssldkjfsldkfj'

In [16]: s
Out[16]: 'hello'

In [17]: whos
Variable    Type      Data/Info
-------------------------------
a           int       2
b           float     23423.0
np          module    <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
odict       type      <class 'collections.OrderedDict'>
plt         module    <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
s           str       hello
something   str       ssldkjfsldkfj

In [18]: del s

In [19]: whos
Variable    Type      Data/Info
-------------------------------
a           int       2
b           float     23423.0
np          module    <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
odict       type      <class 'collections.OrderedDict'>
plt         module    <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
something   str       ssldkjfsldkfj

In [20]: reset
Once deleted, variables cannot be recovered. Proceed (y/[n])? y

In [21]: whos
Interactive namespace is empty.

In [22]: # print a greeting 10 times
    ...: nhellos = 10
    ...: for i in range(nhellos):
    ...:     print('hello world')
    ...:
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world

In [23]: pwd
Out[23]: '/home/mspacek/SciPyCourse2018/notes'

In [24]: ls
00_intro/  01_Python_basics/  02_Python_basics_2/  homework1.md  homework1.pdf  homework1_solutions.py  old_notes/  README.md

In [25]: ls -al
total 96
drwxrwxr-x  7 mspacek mspacek  4096 Apr 17 02:29 ./
drwxrwxr-x  5 mspacek mspacek  4096 Apr 13 16:50 ../
drwxrwxr-x  2 mspacek mspacek  4096 Apr 10 11:17 00_intro/
drwxrwxr-x  2 mspacek mspacek  4096 Apr 16 11:15 01_Python_basics/
drwxrwxr-x  2 mspacek mspacek  4096 Apr 17 11:33 02_Python_basics_2/
drwxrwxr-x  8 mspacek mspacek  4096 Apr 17 12:29 .git/
-rw-rw-r--  1 mspacek mspacek    85 Apr 10 01:58 .gitignore
-rw-rw-r--  1 mspacek mspacek  1066 Apr 17 02:26 homework1.md
-rw-------  1 mspacek mspacek 49274 Apr 17 02:26 homework1.pdf
-rw-rw-r--  1 mspacek mspacek   501 Apr 17 02:20 homework1_solutions.py
drwxrwxr-x 13 mspacek mspacek  4096 Apr 17 01:38 old_notes/
-rw-rw-r--  1 mspacek mspacek    20 Mar 28  2017 README.md

In [26]: cd 02_Python_basics_2/
/home/mspacek/SciPyCourse2018/notes/02_Python_basics_2

In [27]: ls
02_Python_basics_2.md  02_Python_basics_2.pdf  example_functions.py  hellos.py

In [28]: pwd
Out[28]: '/home/mspacek/SciPyCourse2018/notes/02_Python_basics_2'

In [29]: ls
02_Python_basics_2.md  02_Python_basics_2.pdf  example_functions.py  hellos.py

In [30]: run hellos.py
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world

In [31]: whos
Variable   Type    Data/Info
----------------------------
i          int     9
nhellos    int     10

In [32]:
mspacek@Godel:~/SciPyCourse2018/notes$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: exit
mspacek@Godel:~/SciPyCourse2018/notes$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: quit
mspacek@Godel:~/SciPyCourse2018/notes$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: for i in range(1, 6, 1):
   ...:     print(i)
   ...:
1
2
3
4
5

In [2]: for i in range(10, 0, -1):
   ...:     print(i)
   ...:
10
9
8
7
6
5
4
3
2
1

In [3]: for i in range(10, 0, -2):
   ...:     print(i)
   ...:
10
8
6
4
2

In [4]: for i in range(10):
   ...:     if i == 5:
   ...:         continue
   ...:     print(i)
   ...:
0
1
2
3
4
6
7
8
9

In [5]: for i in range(10):
   ...:     if i == 5:
   ...:         break
   ...:     print(i)
   ...:
0
1
2
3
4

In [6]: i = 0

In [7]: while i < 5:
   ...:     i = i + 1
   ...:     print(i)
   ...:
1
2
3
4
5

In [8]: i
Out[8]: 5

In [9]: i = 0

In [10]: while i < 5:
    ...:     print(i)
    ...:
    ...:
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
^C0
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-10-c83e20cc8bda> in <module>()
      1 while i < 5:
----> 2     print(i)
      3
      4

KeyboardInterrupt:
> <ipython-input-10-c83e20cc8bda>(2)<module>()
      1 while i < 5:
----> 2     print(i)
      3
      4

ipdb> c

In [11]: a = 1

In [12]: b = 1.11

In [13]: a + b
Out[13]: 2.1100000000000003

In [14]: i = 2 + 2

In [15]: print(i)
4

In [16]: for i in range(10):
    ...:     print(i)
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

In [17]: ls
00_intro/  01_Python_basics/  02_Python_basics_2/  homework1.md  homework1.pdf  homework1_solutions.py  old_notes/  README.md

In [18]: cd 02_Python_basics_2/
/home/mspacek/SciPyCourse2018/notes/02_Python_basics_2

In [19]: ls
02_Python_basics_2.md  02_Python_basics_2.pdf  basics.py  example_functions.py  hellos.py

In [20]: run basics.py
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

In [21]: run basics.py
0
1
4
9
16
25
36
49
64
81

In [22]: run basics.py
0
0
1
1
4
3
9
6
16
10
25
15
36
21
49
28
64
36
81
45

In [23]: run basics.py
square: 0
running sum 0
square: 1
running sum 1
square: 4
running sum 3
square: 9
running sum 6
square: 16
running sum 10
square: 25
running sum 15
square: 36
running sum 21
square: 49
running sum 28
square: 64
running sum 36
square: 81
running sum 45

In [24]: run basics.py

In [25]: run basics.py
0.0
1.0
1.4142135623730951
1.7320508075688772
2.0
2.23606797749979
2.449489742783178
2.6457513110645907
2.8284271247461903
3.0

In [26]: run basics.py
0.0
1.0
1.4142135623730951
1.7320508075688772
2.0
2.23606797749979
2.449489742783178
2.6457513110645907
2.8284271247461903
3.0

In [27]: import math

In [28]: run basics.py
0
1
2
3
4
5
6
7
seven
8
9

In [29]: run basics.py
0
1
2
3
three
4
5
6
7
seven
8
9

In [30]: run basics.py
0
1
2
three
4
5
6
seven
8
9

In [31]: run basics.py
0 is even
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
7 is odd
8 is even
9 is odd

In [32]: run basics.py
0 is even
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
8 is even
9 is odd

In [33]: run basics.py
0 is even
1 is odd
2 is even
3 is odd
4 is even
5 is odd
6 is even
8 is even
9 is odd

In [34]: run basics.py
9 is odd
8 is even
6 is even
5 is odd
4 is even
3 is odd
2 is even
1 is odd
0 is even

In [35]: s = 'sdfsdfs'

In [36]: s = "sdfsdfs"

In [37]: s = """sdfsfdsdfds"""

In [38]: s
Out[38]: 'sdfsfdsdfds'

In [39]: s = '''sdfsfdsdfds'''

In [40]: type('''sdfsfdsdfds''')
Out[40]: str

In [41]: s = ''

In [42]: s
Out[42]: ''

In [43]: len?
Signature: len(obj, /)
Docstring: Return the number of items in a container.
Type:      builtin_function_or_method

In [44]: len(s)
Out[44]: 0

In [45]: s = 'abc'

In [46]: len(3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-46-6b3b01eb5e19> in <module>()
----> 1 len(3)

TypeError: object of type 'int' has no len()
> <ipython-input-46-6b3b01eb5e19>(1)<module>()
----> 1 len(3)

ipdb> c

In [47]: len(s)
Out[47]: 3

In [48]: s = 'hello' + 'world'

In [49]: s
Out[49]: 'helloworld'

In [50]: 'hello' + ' world'
Out[50]: 'hello world'

In [51]: 'hello ' + 'world'
Out[51]: 'hello world'

In [52]: 'hello' + ' ' + 'world'
Out[52]: 'hello world'

In [53]: cat
^C
Program interrupted. (Use 'cont' to resume).
--Call--
> /usr/lib/python3.5/signal.py(45)signal()
     43
     44
---> 45 @_wraps(_signal.signal)
     46 def signal(signalnum, handler):
     47     handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))

ipdb> c

In [54]: cat?
Repr: <alias cat for 'cat'>

In [55]: help(cat)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-55-a5a4a8576882> in <module>()
----> 1 help(cat)

NameError: name 'cat' is not defined
> <ipython-input-55-a5a4a8576882>(1)<module>()
----> 1 help(cat)

ipdb> c

In [56]: ls
02_Python_basics_2.md  02_Python_basics_2.pdf  basics.py  example_functions.py  hellos.py

In [57]: pwd
Out[57]: '/home/mspacek/SciPyCourse2018/notes/02_Python_basics_2'

In [58]: s
Out[58]: 'helloworld'

In [59]: s += '!'

In [60]: s
Out[60]: 'helloworld!'

In [61]: ss = s * 2

In [62]: ss
Out[62]: 'helloworld!helloworld!'

In [63]: s * s
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-63-e2649a84434e> in <module>()
----> 1 s * s

TypeError: can't multiply sequence by non-int of type 'str'
> <ipython-input-63-e2649a84434e>(1)<module>()
----> 1 s * s

ipdb> c

In [64]: ss = s * 2

In [65]: ss
Out[65]: 'helloworld!helloworld!'

In [66]: '\n'
Out[66]: '\n'

In [67]: print('hello\nworld')
hello
world

In [68]: print('hello\tworld')
hello   world

In [69]: print('hello\nworld')
hello
world

In [70]: print('hello\\nworld')
hello\nworld

In [71]: print('hello\\\nworld')
hello\
world

In [72]: print('hello\\\\nworld')
hello\\nworld

In [73]: print(r'hello\nworld')
hello\nworld

In [74]: name = 'Bob'

In [75]: print('hello %s' % name)
hello Bob

In [76]: print('hello', name)
hello Bob

In [77]: print('hello %s!' % name)
hello Bob!

In [78]: print('hello', name, '!')
hello Bob !

In [79]: 'The date is %s %d, %d' % ('April', 17, 2018)
Out[79]: 'The date is April 17, 2018'

In [80]: f = 3.14159

In [81]: f
Out[81]: 3.14159

In [82]: print('pi is %f' % f)
pi is 3.141590

In [83]: print('pi is %.2f' % f)
pi is 3.14

In [84]: print('number is %g' % f)
number is 3.14159

In [85]: print('number is %g' % 10)
number is 10

In [86]: print('number is %f' % 10)
number is 10.000000

In [87]: 'The date is %g %g, %g' % ('April', 17, 2018)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-87-7027813e6a8f> in <module>()
----> 1 'The date is %g %g, %g' % ('April', 17, 2018)

TypeError: a float is required
> <ipython-input-87-7027813e6a8f>(1)<module>()
----> 1 'The date is %g %g, %g' % ('April', 17, 2018)

ipdb> c

In [88]: 'The date is %s %g, %g' % ('April', 17, 2018)
Out[88]: 'The date is April 17, 2018'

In [89]: 'The date is %s %s, %s' % ('April', 17, 2018)
Out[89]: 'The date is April 17, 2018'

In [90]: 'The date is %s %s, %s' % ('April', 17, 2018.23)
Out[90]: 'The date is April 17, 2018.23'

In [91]: 1 % 2
Out[91]: 1

In [92]: s = 'abcdefg'

In [93]: len(s)
Out[93]: 7

In [94]: 'a' in s
Out[94]: True

In [95]: 'h' in s
Out[95]: False

In [96]: 'abc' in s
Out[96]: True

In [97]: for c in s:
    ...:     print(c)
    ...:
a
b
c
d
e
f
g

In [98]: s
Out[98]: 'abcdefg'

In [99]: s[0]
Out[99]: 'a'

In [100]: s[0]
Out[100]: 'a'

In [101]: s[1]
Out[101]: 'b'

In [102]: s[2]
Out[102]: 'c'

In [103]: s[6]
Out[103]: 'g'

In [104]: s[7]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-104-b035325af127> in <module>()
----> 1 s[7]

IndexError: string index out of range
> <ipython-input-104-b035325af127>(1)<module>()
----> 1 s[7]

ipdb> c

In [105]: len(s)
Out[105]: 7

In [106]: s[7-1]
Out[106]: 'g'

In [107]: s[-1]
Out[107]: 'g'

In [108]: -0 == 0
Out[108]: True

In [109]: s[0:2]
Out[109]: 'ab'

In [110]: s[0]
Out[110]: 'a'

In [111]: s[1]
Out[111]: 'b'

In [112]: s[1,3]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-112-503bc1b3bfb0> in <module>()
----> 1 s[1,3]

TypeError: string indices must be integers
> <ipython-input-112-503bc1b3bfb0>(1)<module>()
----> 1 s[1,3]

ipdb> c

In [113]: s[0:2]
Out[113]: 'ab'

In [114]: s[0:3]
Out[114]: 'abc'

In [115]: s[0 and 1]
Out[115]: 'a'

In [116]: 0 and 1
Out[116]: 0

In [117]: s[0]
Out[117]: 'a'

In [118]: 1 and 2
Out[118]: 2

In [119]: s[1:3]
Out[119]: 'bc'

In [120]: s[0:7:2]
Out[120]: 'aceg'

In [121]: s[0:7:3]
Out[121]: 'adg'

In [122]: s[:7:3]
Out[122]: 'adg'

In [123]: s[0::2]
Out[123]: 'aceg'

In [124]: s[::2]
Out[124]: 'aceg'

In [125]: s[::-1]
Out[125]: 'gfedcba'

In [126]: class Dog(object): pass

In [127]: fido = Dog()

In [128]: type(fido)
Out[128]: __main__.Dog

In [129]: fido.color = 'brown'

In [130]: fido.color
Out[130]: 'brown'

In [131]: fido.weight = 15

In [132]: type(5)
Out[132]: int

In [133]: fido
Out[133]: <__main__.Dog at 0x7f91d0634d30>

In [134]: 5
Out[134]: 5

In [135]: type(5)
Out[135]: int

In [136]: fido
Out[136]: <__main__.Dog at 0x7f91d0634d30>

In [137]: george = Dog()

In [138]: george.color = 'purple'

In [139]: george.color
Out[139]: 'purple'

In [140]: fido.color
Out[140]: 'brown'

In [141]: s
Out[141]: 'abcdefg'

In [142]: del fido

In [143]: fido.color = 'black'
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-143-494e432a4b4e> in <module>()
----> 1 fido.color = 'black'

NameError: name 'fido' is not defined
> <ipython-input-143-494e432a4b4e>(1)<module>()
----> 1 fido.color = 'black'

ipdb> c

In [144]: Dog
Out[144]: __main__.Dog

In [145]: fido = Dog()

In [146]: fido.color = 'dddsfsdf'

In [147]: whos
Variable   Type                          Data/Info
--------------------------------------------------
Dog        type                          <class '__main__.Dog'>
a          int                           1
b          float                         1.11
c          str                           g
f          float                         3.14159
fido       Dog                           <__main__.Dog object at 0x7f91d15ae7b8>
george     Dog                           <__main__.Dog object at 0x7f91deee68d0>
i          int                           0
math       module                        <module 'math' (built-in)>
name       str                           Bob
np         module                        <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
odict      type                          <class 'collections.OrderedDict'>
plt        module                        <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
s          str                           abcdefg
sqrt       builtin_function_or_method    <built-in function sqrt>
ss         str                           helloworld!helloworld!

In [148]: s
Out[148]: 'abcdefg'

In [149]: s.count
Out[149]: <function str.count>

In [150]: s.count?
Docstring:
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are
interpreted as in slice notation.
Type:      builtin_function_or_method

In [151]: s.count('a')
Out[151]: 1

In [152]: s.count('abc')
Out[152]: 1

In [153]: s.count('h')
Out[153]: 0

In [154]: s.index?
Docstring:
S.index(sub[, start[, end]]) -> int

Like S.find() but raise ValueError when the substring is not found.
Type:      builtin_function_or_method

In [155]: s.index('a')
Out[155]: 0

In [156]: 'asdlkfjsldkfjla'.index('a')
Out[156]: 0

In [157]: s
Out[157]: 'abcdefg'

In [158]: s.index('cde')
Out[158]: 2

In [159]: s.index('ced')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-159-fc9c70a73725> in <module>()
----> 1 s.index('ced')

ValueError: substring not found
> <ipython-input-159-fc9c70a73725>(1)<module>()
----> 1 s.index('ced')

ipdb> c

In [160]: s.index('z')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-160-3d8ee9b57202> in <module>()
----> 1 s.index('z')

ValueError: substring not found
> <ipython-input-160-3d8ee9b57202>(1)<module>()
----> 1 s.index('z')

ipdb> c

In [161]: s.count('ced')
Out[161]: 0

In [162]: s.split?
Docstring:
S.split(sep=None, maxsplit=-1) -> list of strings

Return a list of the words in S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are
removed from the result.
Type:      builtin_function_or_method

In [163]: s
Out[163]: 'abcdefg'

In [164]: s.split('d')
Out[164]: ['abc', 'efg']

In [165]: 'data1value,data2value'.split(',')
Out[165]: ['data1value', 'data2value']

In [166]: s.replace('abc', 'hello')
Out[166]: 'hellodefg'

In [167]: s.replace?
Docstring:
S.replace(old, new[, count]) -> str

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
Type:      builtin_function_or_method

In [168]: 'abcabc123'.replace('abc', 'hello')
Out[168]: 'hellohello123'

In [169]: s
Out[169]: 'abcdefg'

In [170]: s.replace('abc', 'hello')
Out[170]: 'hellodefg'

In [171]: s = s.replace('abc', 'hello')

In [172]: s
Out[172]: 'hellodefg'

In [173]: s = 'abcdefg'

In [174]: type(s)
Out[174]: str

In [175]: s.upper?
Docstring:
S.upper() -> str

Return a copy of S converted to uppercase.
Type:      builtin_function_or_method

In [176]: s.upper()
Out[176]: 'ABCDEFG'

In [177]: a = 1

In [178]: a.upper()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-178-b9d8f89049c4> in <module>()
----> 1 a.upper()

AttributeError: 'int' object has no attribute 'upper'
> <ipython-input-178-b9d8f89049c4>(1)<module>()
----> 1 a.upper()

ipdb> c

In [179]: 'ABC123'.lower()
Out[179]: 'abc123'

In [180]: s
Out[180]: 'abcdefg'

In [181]: s.upper()
Out[181]: 'ABCDEFG'

In [182]: s.upper().lower()
Out[182]: 'abcdefg'

In [183]: s.upper().lower().upper()
Out[183]: 'ABCDEFG'

In [184]: s.title?
Docstring:
S.title() -> str

Return a titlecased version of S, i.e. words start with title case
characters, all remaining cased characters have lower case.
Type:      builtin_function_or_method

In [185]: s.title()
Out[185]: 'Abcdefg'

In [186]: s = 'abcdefghijklmnopqrstuvwxyz'

In [187]: s
Out[187]: 'abcdefghijklmnopqrstuvwxyz'

In [188]: len(s)
Out[188]: 26

In [189]: for i in range(len(s)-1, -1, -1):
     ...:     print(s[i])
     ...:
z
y
x
w
v
u
t
s
r
q
p
o
n
m
l
k
j
i
h
g
f
e
d
c
b
a

In [190]: for i in range(-1, -1, -1):
     ...:     print(s[i])
     ...:

In [191]:

In [191]: for i in range(len(s)-1, -1, -1):
     ...:     print(s[i])
     ...:
z
y
x
w
v
u
t
s
r
q
p
o
n
m
l
k
j
i
h
g
f
e
d
c
b
a

In [192]: for x in s[::-1]:
     ...:     print(x)
     ...:
     ...:
z
y
x
w
v
u
t
s
r
q
p
o
n
m
l
k
j
i
h
g
f
e
d
c
b
a

In [193]: s[::-1]
Out[193]: 'zyxwvutsrqponmlkjihgfedcba'

In [194]: s[::2]
Out[194]: 'acegikmoqsuwy'

In [195]: every2 = s[::2]

In [196]: s
Out[196]: 'abcdefghijklmnopqrstuvwxyz'

In [197]: every2
Out[197]: 'acegikmoqsuwy'

In [198]: every2.replace('a', '4').replace('e', '3').replace('i', '1')
Out[198]: '4c3g1kmoqsuwy'

In [199]: s = s[::-1]

In [200]: s
Out[200]: 'zyxwvutsrqponmlkjihgfedcba'

In [201]: s = s[::-1]

In [202]: s
Out[202]: 'abcdefghijklmnopqrstuvwxyz'

In [203]: def add(x, y):
     ...:     result = x + y
     ...:     return result
     ...:

In [204]: whos
Variable   Type                          Data/Info
--------------------------------------------------
Dog        type                          <class '__main__.Dog'>
a          int                           1
add        function                      <function add at 0x7f91dee9d620>
b          float                         1.11
c          str                           g
every2     str                           acegikmoqsuwy
f          float                         3.14159
fido       Dog                           <__main__.Dog object at 0x7f91d15ae7b8>
george     Dog                           <__main__.Dog object at 0x7f91deee68d0>
i          int                           0
math       module                        <module 'math' (built-in)>
name       str                           Bob
np         module                        <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
odict      type                          <class 'collections.OrderedDict'>
plt        module                        <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
s          str                           abcdefghijklmnopqrstuvwxyz
sqrt       builtin_function_or_method    <built-in function sqrt>
ss         str                           helloworld!helloworld!
x          str                           a

In [205]: add?
Signature: add(x, y)
Docstring: <no docstring>
File:      ~/SciPyCourse2018/notes/02_Python_basics_2/<ipython-input-203-92adc0ed9402>
Type:      function

In [206]: add(1, 2)
Out[206]: 3

In [207]: def add(x, y):
     ...:     """Adds two numbers x and y"""
     ...:     result = x + y
     ...:     return result
     ...:

In [208]: add?
Signature: add(x, y)
Docstring: Adds two numbers x and y
File:      ~/SciPyCourse2018/notes/02_Python_basics_2/<ipython-input-207-21e1905a415a>
Type:      function

In [209]: def add(x, y):
     ...:     '''Adds two numbers x and y'''
     ...:     result = x + y
     ...:     return result
     ...:

In [210]: add?
Signature: add(x, y)
Docstring: Adds two numbers x and y
File:      ~/SciPyCourse2018/notes/02_Python_basics_2/<ipython-input-209-11bfc550a1e5>
Type:      function

In [211]: def add(x, y):
     ...:     'Adds two numbers x and y'
     ...:     result = x + y
     ...:     return result
     ...:

In [212]: add?
Signature: add(x, y)
Docstring: Adds two numbers x and y
File:      ~/SciPyCourse2018/notes/02_Python_basics_2/<ipython-input-211-050597f8a87c>
Type:      function

In [213]: def add(x, y):
     ...:     """Adds two numbers x and y"""
     ...:     result = x + y
     ...:     return result
     ...:
     ...: a = 12345
     ...:

In [214]: a
Out[214]: 12345

In [215]: add(4,5)
Out[215]: 9

In [216]: a = 12345

In [217]: pwd
Out[217]: '/home/mspacek/SciPyCourse2018/notes/02_Python_basics_2'

In [218]: ls
02_Python_basics_2.md  02_Python_basics_2.pdf  basics.py  example_functions.py  hellos.py

In [219]: run example_functions.py

In [220]: add
Out[220]: <function __main__.add>

In [221]: subtract?
Signature: subtract(x, y)
Docstring: Subtracts y from x
File:      ~/SciPyCourse2018/notes/02_Python_basics_2/example_functions.py
Type:      function

In [222]: subtract(5, 2)
Out[222]: 3

In [223]: add(5, 2)
Out[223]: 7

In [224]: add(2, 5)
Out[224]: 7

In [225]: subtract(5, 2)
Out[225]: 3

In [226]: subtract(2, 5)
Out[226]: -3

In [227]: run example_functions.py

In [228]: add3?
Signature: add3(x, y, z=0)
Docstring: <no docstring>
File:      ~/SciPyCourse2018/notes/02_Python_basics_2/example_functions.py
Type:      function

In [229]: run example_functions.py

In [230]: add3?
Signature: add3(x, y, z=0)
Docstring: Adds two numbers x and y, and optionally z
File:      ~/SciPyCourse2018/notes/02_Python_basics_2/example_functions.py
Type:      function

In [231]: add(1, 2)
Out[231]: 3

In [232]: add(1, 2, 10)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-232-5d3f2e4fa87f> in <module>()
----> 1 add(1, 2, 10)

TypeError: add() takes 2 positional arguments but 3 were given
> <ipython-input-232-5d3f2e4fa87f>(1)<module>()
----> 1 add(1, 2, 10)

ipdb> c

In [233]: add(1, 2, z=10)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-233-473759ae2367> in <module>()
----> 1 add(1, 2, z=10)

TypeError: add() got an unexpected keyword argument 'z'
> <ipython-input-233-473759ae2367>(1)<module>()
----> 1 add(1, 2, z=10)

ipdb> c

In [234]: add3(1, 2, 10)
Out[234]: 13

In [235]: add3(1, 2, z=10)
Out[235]: 13

In [236]: add3(z=10, x=1, y=2)
Out[236]: 13

In [237]: run example_functions.py

In [238]: add3(z=10, x=1, y=2)
1 2 10
Out[238]: 13

In [239]: len
Out[239]: <function len>

In [240]: def print(x):
     ...:     pass
     ...:

In [241]: print?
Signature: print(x)
Docstring: <no docstring>
File:      ~/SciPyCourse2018/notes/02_Python_basics_2/<ipython-input-240-58d3b65af875>
Type:      function

In [242]: del print

In [243]: print('sdfs')
sdfs

In [244]: keywords
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-244-1eb9771c7f0a> in <module>()
----> 1 keywords

NameError: name 'keywords' is not defined
> <ipython-input-244-1eb9771c7f0a>(1)<module>()
----> 1 keywords

ipdb> c

In [245]: help
Out[245]: Type help() for interactive help, or help(object) for help about object.

In [246]: help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not
class               from                or
continue            global              pass


In [247]: help('builtins')


In [248]: run example_functions.py

In [249]: add3(z=10, x=1, y=2)
1 2 10
Out[249]: 13

In [250]: whos
Variable   Type                          Data/Info
--------------------------------------------------
Dog        type                          <class '__main__.Dog'>
a          int                           12345
add        function                      <function add at 0x7f91dee39b70>
add3       function                      <function add3 at 0x7f91dee392f0>
b          float                         1.11
c          str                           g
every2     str                           acegikmoqsuwy
f          float                         3.14159
fido       Dog                           <__main__.Dog object at 0x7f91d15ae7b8>
george     Dog                           <__main__.Dog object at 0x7f91deee68d0>
i          int                           0
math       module                        <module 'math' (built-in)>
name       str                           Bob
np         module                        <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
odict      type                          <class 'collections.OrderedDict'>
plt        module                        <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>
s          str                           abcdefghijklmnopqrstuvwxyz
sqrt       builtin_function_or_method    <built-in function sqrt>
ss         str                           helloworld!helloworld!
subtract   function                      <function subtract at 0x7f91dee39e18>
x          str                           a

In [251]: myresult = add3(z=10, x=1, y=2)
1 2 10

In [252]: run example_functions.py

In [253]:
mspacek@Godel:~/SciPyCourse2018/notes$ ipython
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: whos
Variable   Type      Data/Info
------------------------------
np         module    <module 'numpy' from '/us<...>kages/numpy/__init__.py'>
odict      type      <class 'collections.OrderedDict'>
plt        module    <module 'matplotlib.pyplo<...>es/matplotlib/pyplot.py'>

In [2]: reset
Once deleted, variables cannot be recovered. Proceed (y/[n])? y

In [3]: run example_functions.py
ERROR:root:File `'example_functions.py'` not found.

In [4]: pwd
Out[4]: '/home/mspacek/SciPyCourse2018/notes'

In [5]: cd 02_Python_basics_2/
/home/mspacek/SciPyCourse2018/notes/02_Python_basics_2

In [6]: run example_functions.py

In [7]: addsubtract(10, 2)
Out[7]: (12, 8)

In [8]: type(addsubtract(10, 2))
Out[8]: tuple

In [9]: result = addsubtract(10, 2)

In [10]: type(result)
Out[10]: tuple

In [11]: s, d = addsubtract(10, 2)

In [12]: s
Out[12]: 12

In [13]: d
Out[13]: 8

In [14]: run example_functions.py

In [15]: addsubtract(10, 2)
12
Out[15]: (12, 8)

In [16]:
