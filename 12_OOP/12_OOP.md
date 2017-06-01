### object-oriented programming

- use datetime.datetime and datetime.timedelta objects, and ndarray object, as reminder of  attribs and methods
- another good example: procedural MPL vs. OOP MPL
- object == instance of a class, class == type more or less
- writing a class: __init__(self), other methods, attributes
- one nice thing about using an object with attributes and methods is that you don't have
to pass around lots and lots of arguments from one function to another - methods can work
on the attributes of self instead
    - convenient, but can be dangerous, because now the ouput of your methods depends on
    the state of your object, making your code harder to debug
    - compare with "functional programming", where all you have are inputs and outputs
- properties? getters and setters?
- class inheritance? maybe just mention it
- add some plot methods for engagement!
