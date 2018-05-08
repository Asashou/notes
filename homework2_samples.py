"""Sample solutions from various students"""

# Exercise 1

def norm(l):
    """ takes a list or tuple and normalises each value to the sum of the values """
    if type(l) is tuple:
        list(l)

    return tuple([val/sum(l) for val in l])

def norm(l):
    """returns a list with the normalized values of a previous list"""
    N = sum(l)
    lnorm = []
    j = 0
    for i in l:
        lnorm.append(j)
        lnorm [j] = i/N
        j = j + 1
    return lnorm

def norm(l):
    """gives a list with the normalized values of a list l"""
    return [i/sum(l) for i in l]

def norm(x):
    """a function that return normalized values of list"""
    sum = 0
    for var in x:
        sum += var
    return [var/sum for var in x]

normalized_values = []
def norm(list):
     """that accepts a list of values of arbitrary length N, and returns a list of the normalized values"""
     normalized_values.append(float(i)/sum(list) for i in list)
     return normalized_values

# Exercise 2

def normdata(data):
    """Returns normalized values for given sublist within a list"""
    return [[j/sum(i) for j in i] for i in data]


def norm3(data):
    """Returns the normalised values for each list"""
    x = sum(data[0])
    y = sum(data[1])
    z = sum(data[2])
    normdata = [[val/x for val in data[0]], [val/y for val in data[1]], [val/z for val in data[2]]]
    print(normdata)


def multiNorm(inListOfLists):
    """Returns 'normArray' normalised to the max value of 'inArray'
       inListOfLists must be a list of lists and values must be numeric"""

    normArray = [[nVal/sum(sum(val,[])) for nVal in sum(val,[])] for val in zip(inListOfLists)]

    # Print a check of sums of individual lists
    for index, val in enumerate(normArray):
        print('Exp. No. %d, sum = %.1f' % (index+1, sum(val)))
    return normArray


def norm(x):
    """Takes a list of 3 lists and returns a normalized list of the 3 lists"""
    normdata = [[val/sum(x[0]) for val in x[0]], [val/sum(x[1]) for val in x[1]], [val/sum(x[2]) for val in x[2]]]
    return normdata

# Exercise 3

def vectorsum(x,y):
    """a function that sum of elements of two lists"""
    return [x[i]+y[i] for i in range(len(x))]

def vectorsum(x,y):
    """Returns the vector sum of 2 lists"""
    return [sum(z) for z in zip(x,y)]

def vectorsum(x,y):
    """Returns the vector sum of 2 lists"""
    return([sum(z) for z in zip(x,y)])

# Exercise 4

def normd(x):
    result = {key:val/sum(d) for (key, val) in d.items()}
    return result

def normd(d):
    """Returns normalized values for given list"""
    return {key:val/sum(d.values()) for (key, val) in d.items()}

def normd(d):
    #   takes a dictionary with an arbitrary number of key:value pairs, and returns a dictionary with the same keys,
    #   but with normalized values.

    d = dict(zip(d.keys(), norm(d.values())))
    return d

def normd(d):
   "Normalise values of each key of dictionary d"
   d_sum = sum(d.values())
   for key, val in d.items():
       d[key]=val/d_sum
   return d

def normd(my_dict):
    """This function takes a dictionary and return normalized values"""
    total = 0
    for i in my_dict:
        total = total + my_dict[i]
    for j in my_dict:
        my_dict[j] = (float)(my_dict[j])/total
    return my_dict
