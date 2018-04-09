import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# load data
data = np.load('LFP_example_data.npy')
npoints = len(data)
sampfreq = 1000 # Hz
t = np.arange(npoints) / sampfreq

# plot subset of data
f, a = plt.subplots(figsize=(10, 3)) # create a figure and axes
a.plot(t[:200], data[:200], '-')
a.set_title('LFP example data')
a.set_xlabel('Time (s)')
a.set_ylabel('Volage (mV)')

# calculate spectrogram using Welch's periodogram method
winwidth = 5 # window width, seconds
winwidthsamples = int(winwidth * sampfreq)
P, freqs, t = mpl.mlab.specgram(data, winwidthsamples, sampfreq)

# set frequency limits
fmin, fmax = 0, 50 # set frequency limits, in Hz
lo, hi = freqs.searchsorted([fmin, fmax])
P, freqs = P[lo:hi], freqs[lo:hi]

# convert power to dB and set power limits
P = 10 * np.log10(P)
pmax = 200 # dB
P[P > pmax] = pmax

# plot the spectrogram
f, a = plt.subplots(figsize=(10, 3)) # create a figure and axes
P = P[::-1] # flip P array vertically for plotting
extent = t[0], t[-1], freqs[0], freqs[-1]
a.imshow(P, extent=extent, cmap='hot') # plot power as an image
a.axis('tight')
a.set_xlabel('Time (s)')
a.set_ylabel('Frequency (Hz)')
a.set_title('LFP example spectrogram')
f.tight_layout(pad=0.3) # crop figure to contents
