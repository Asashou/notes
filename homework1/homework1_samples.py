"""Sample solutions from various students"""

# Exercise 1

def vowelcount (s):
    #  function vowelcount takes a string as an argument and returns the number of vowels in the string.

    s = s.lower()
    vowels = s.count('a') + s.count('o') + s.count('e') + s.count('u') + s.count('i')

    return vowels


def vowelcount(str):
    """Count number of vowels in a string"""
    vowels = 'aeiouAEIOU'
    count = 0
    for i in str:
        if i in vowels:
            count += 1
    return count

# Martin's solution:
def vowelcount(s):
    """Count vowels in s"""
    s = s.lower()
    nv = 0
    for v in 'aeiou':
        nv += s.count(v)
    return nv

# Exercise 2

def metric(x, y):
    """Calculate the difference and sum of two numbers x and y and the quotient
        of the difference and sum"""

    d = x - y
    s = x + y

    if s == 0:
        print ('the sum is 0 and you can not divide by 0! Ever tried to divide cake by 0 people?')
        return None
    q = d / s
    return q


# Martin's solution:
def metric(x, y):
    """Calculate difference over sum"""
    d = x - y
    s = x + y
    print('difference is %g, sum is %g' % (d, s))
    if s == 0:
        return 0
    return d / s



# Exercise 3

def multtable(n):
    "Integers table of 1 to n multiplication"

    for x in range(1,n+1):
            #print(x)
            for y in range(1,n+1):
                result=x*y
                #print(y)

                if y<n:
                    #pass
                    print(str(result) + ' ', end='')
                else:
                    print(result,end='\n')


#martin's solution:

def multtable(n):
    """Print multiplication table from 1 to n"""
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i * j, end=' ')
        print()
