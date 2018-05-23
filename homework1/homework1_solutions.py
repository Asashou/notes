def vowelcount(s):
    """Count vowels in s"""
    s = s.lower()
    nv = 0
    for v in 'aeiou':
        nv += s.count(v)
    return nv

def metric(x, y):
    """Calculate difference over sum"""
    d = x - y
    s = x + y
    print('difference is %g, sum is %g' % (d, s))
    if s == 0:
        return 0
    return d / s

def multtable(n):
    """Print multiplication table from 1 to n"""
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i * j, end=' ')
        print()
