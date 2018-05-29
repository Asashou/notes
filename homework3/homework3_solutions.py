# code used to generate the data:

t = np.arange(0, 100, 0.1)
x = np.random.normal(loc=5, scale=0.5, size=1000)
y = np.random.normal(loc=3, scale=0.25, size=1000)
np.savez('homework3.npz', t=t, x=x, y=y)

# homework3 solution:

def absdiff(a, b):
    """Return the absolute difference between a and b"""
    a = np.asarray(a)
    b = np.asarray(b)
    return np.abs(a - b)

# load data:
d = np.load('homework3.npz')
print(d.keys()) # check keys
t, x, y = d['t'], d['x'], d['y'] # extract arrays

absd = absdiff(x, y)

# plot time series:
plt.figure()
plt.plot(t, x, marker='', label='x')
plt.plot(t, y, marker='', label='y')
plt.plot(t, absd, marker='', label='absd')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.title('Time series')
plt.legend()
plt.savefig('time_series.png')

# plot distributions:
plt.figure()
bins = np.arange(0, 7.5, 0.1)
plt.hist(x, bins=bins, label='x')
plt.hist(y, bins=bins, label='y')
plt.hist(absd, bins=bins, label='absd')
plt.xlabel('Position (cm)')
plt.title('Distributions')
plt.legend()
plt.savefig('distributions.png')

# save t and absd to disk:
np.savez('t_absd.npz', t=t, absd=absd)
