"""Sample solutions from various students"""

# no need to manually unzip the .npz
a = np.load('x.npy')
b = np.load('y.npy')
t = np.load('t.npy')


# no need to rename
a = d['x']
b = d['y']
t = d['t']



# will this absdiff() work for all types of sequences?
a = np.array([1, 2, 3])
b = np.array([10, 0 , -10])
def absdiff(a, b) :
    return np.abs(a - b)


# don't be afraid to overwrite existing variable names
def absdiff(a, b):
    """Take two sequencies of values a,b of identical lengths and returns an array
    of the absolute difference of each number"""
    A = np.array(a)
    B = np.array(b)
    return abs(A-B)


# nice list comprehension practice, but no need with arrays
def absdiff(x, y):
    """Calculate the absolute difference of x and y"""
    diff = [xx - yy for xx, yy in zip(x, y)]
    absd = [abs(number) for number in diff]
    return np.asarray(absd)


# what does this do?
plt.hist(x, bins=30)
plt.hist(y, bins=30)
plt.hist(absd, bins=30)


# how could this be improved?
fBin = 0 # Value of the first bin
lBin = 8 # Value of the last bin
rBin = 0.1 # Resolution of each bin
plt.hist(a, bins=np.arange(fBin, lBin, rBin), label = 'Series a')
plt.hist(b, bins=np.arange(fBin, lBin, rBin), label = 'Series b')
plt.hist(absd, bins=np.arange(fBin, lBin, rBin), label = 'abs(b - a)')


# changes location and shape of the legend, to prevent overlap
plt.legend(loc=2, ncol=2)

# lots of people forgot to actually plot a legend!

# what does this do?
np.savez('t_absd.npz', t = 't', absd = 'absd')


# what does this do?
np.savez('t_absd.npz', t, absd)


# this is nice code, but squinting your eyes, how could it be improved?
import numpy as np
import matplotlib.pyplot as plt
def absdiff(a, b):
    """returns the absolute value of the difference between a and b"""
    return np.array([np.abs(aa - bb) for aa, bb in zip(a, b)])
d = np.load('homework3.npz')
list(d.keys())
t, a, b = d['t'], d['x'], d['y']
plt.plot(t, a, label = 'a')
plt.plot(t, b, label = 'b')
absd = absdiff(a, b)
plt.plot(t, absd, label = 'absd')
plt.xlabel('Time(s)')
plt.ylabel('Position(cm)')
plt.title('Time series')
plt.legend()
plt.savefig('time_series.png')
plt.figure()
plt.hist(a, bins = 30, label = 'a')
plt.hist(b, bins = 30, label = 'b')
plt.hist(absd, bins = 30, label = 'absd')
plt.xlabel('Position (cm)')
plt.title('Distributions')
plt.legend()
plt.savefig('distributions.png')
np.savez('t_absd', t, absd)
