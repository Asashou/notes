def add(x, y):
    """Add two numbers x and y"""
    result = x + y
    return result

def subtract(x, y):
    """Subtract y from x"""
    result = x - y
    return result

def add3(x, y, z=0):
    """Add two numbers x and y, and optionally z"""
    result = x + y + z
    return result

def addsubtract(x, y):
    """Return the sum and the difference of two numbers x and y"""
    s = x + y
    d = x - y
    if s > 5:
        print(s)
    return s, d
