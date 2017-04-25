import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# load data
data = np.load('LFP_example_data.npy')
sampfreq = 1000 # Hz

# plot subset of data
plt.figure(figsize=(10, 3)) # create a figure
plt.plot(data[:200])
plt.title('LFP example data')

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
plt.figure(figsize=(10, 3)) # create a figure
P = P[::-1] # flip P array vertically for plotting
extent = t[0], t[-1], freqs[0], freqs[-1]
plt.imshow(P, extent=extent, cmap='jet') # plot power as an image
plt.axis('tight')
plt.xlabel('time (s)')
plt.ylabel('frequency (Hz)')
plt.title('LFP example spectrogram')
plt.tight_layout(pad=0.3) # crop figure to contents
