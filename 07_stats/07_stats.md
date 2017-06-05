### statistics


- we've already done some stats using the numpy library:
    - `import numpy as np`
    - `x = np.random.random(n)` - what does this do?
    - returns `n` *continuous* (float) values evenly distributed over the interval `[0, 1)`
    - this is called a continuous uniform random distribution
    - `x = np.random.randint(minval, maxval, n)` - what does this do?
    - returns `n` *discrete* (integer) values evenly distributed over the interval `[minval, maxval)`
    - this is called a discrete uniform random distribution
    - we also already know how to check if the values get from these functions really are uniformly distributed - how can we visualize this?
        ```python
        import matplotlib.pyplot as plt`
        f, ax = plt.subplots()
        ax.hist(x, bins=nbins)
        ````
        - how to choose `nbins`?
            - if `nbins` is too low, you can't capture enough of the variability of your data in the plotted distribution
            - if `nbins` is too high, you capture too much of the variability, get a very noisy distribution
            - guess and test, but a rule of thumb for continuous variables is `nbins = np.sqrt(n)`
    - plotting the distribution of your data (with a reasonable choice of `nbins`) is really important!
        - can reveal outliers, and maybe sources of error in the data collection
        - many stats tests make assumptions about how your data are distributed, and if your data don't satisfy those assumptions, you should use a different stats test!
        - good to get into the habit of plotting distribs
    - in addition to uniform distrib, the other very common continuous distribution is the normal (Gaussian) distrib
        ```python
        mu, sigma = 0, 1
        s = np.random.normal(loc=mu, scale=sigma, size=1000) # call it s for "sample"
        f, ax = plt.subplots()
        ax.hist(x, bins=30)````
    - what if your data are bimodally distributed (having 2 peaks) like this?:
        ```python
        s1 = np.random.normal(loc=0, scale=1, size=1000)
        s2 = np.random.normal(5, 0.5, 1000) # can use positional args instead of kwargs
        # confirm we got what we asked for:
        s1.mean()
        s1.std()
        s2.mean()
        s2.std()
        s = np.concatenate([s1, s2])
        f, ax = plt.subplots()
        ax.hist(s, bins=40)
        ````
        - are `s.mean()` and `s.std()` meaningful in this case? no! they're poor descriptors of this bimodal distribution, but the only way to tell is to plot and inspect the disctribution

    - can also plot the distribution of discrete valued data, but to get ideal bin locations and widths, need to be a bit more explicit and specify the edges of each bin:
        ```python
        s = np.random.randint(0, 10, 1000)
        s.min() # check that we got what we asked for
        s.max()
        f, ax = plt.subplots()
        edges = np.arange(0, 11) # bin edges, 0 to 10, inclusive, steps of 1
        ax.hist(s, bins=edges)
        ````
        - for discrete values, best to use no more than one bin per possible value, as above, otherwise you'll end up with artificial gaps between discrete values:
        ```python
        f, ax = plt.subplots()
        edges = np.arange(0, 10.5, 0.5) # bin edges, 0 to 10, inclusive, steps of 0.5
        ax.hist(s, bins=edges) # notice the artificial gaps
        ````


- numpy can generate some random samples from distributions, but `scipy.stats` has a lot more stats functionality
    - `import scipy.stats as stats`
    - `stats?` shows a big list of all the stats related objects and functions in `scipy.stats`
    - numpy functions for generating random numbers are actually just shortcuts to the functionality implemented in `scipy.stats`
    - instead of just asking for a random sample of numbers from a particular kind of distribution, `scipy.stats` provides "random variables" as objects, which you can then not only sample, but also call their methods:
        ```python
        rv = stats.norm() # create a continuous normal random variable object
        rv.mean() # returns exactly 0.0
        rv.std() # returns exactly 1.0
        rv = stats.norm(loc=5, scale=0.5)
        rv.mean() # returns exactly 5
        rv.std() # returns exactly 0.5
        s = rv.rvs(1000) # get 1000 random samples from rv
        f, ax = plt.subplots()
        ax.hist(s, bins=30) # looks like what we got earlier from np.random.normal()
        ````
    - the benefit of using a random variable object is that it provides an exact representation of a particular type of distribution
    - to access it analytically as a function of x, call the `.pdf` method
        - `rv.pdf(x)` - PDF = probability density function, or more typically, just "distribution"
        - probability always has to sum to 1, so area under the curve == 1
        - let's overplot the exact representation of the normal distribution over top of the normalized histogram of our 1000 samples from that distribution:
        ```python
        f, ax = plt.subplots()
        ax.hist(s, bins=30, normed=True) # plot a normalized distrib, ie area == 1
        x = np.arange(3, 7, 0.01) # evenly spaced x values
        y = rv.pdf(x)
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('probability')
        ax.set_title('mu=5, sigma=0.5, n=1000 samples')
        f.canvas.set_window_title('sampled vs. exact distribution')
        ````

- now the question is, if we've collected a bunch of data, presumably sampled from some natural process, and we suspect the process that generated our data is distributed according to some distribution, such as the normal distribution, how can we check how likely it is to really have come from a normal distrib, and what optimal values of the normal distribution (mean and std) would allow it to best fit the data?


- mpl hist vs np hist
- AJ had stats talk, gleaned from scipy.stats tutorial
- create distribution object, sample it to get data
    - plot pdf and cdf of sampled data, maybe add noise to it, or give it a slight offset?
    - then do some stats to test if it's significantly different from 0 (due to offset), or significantly different from some other distrib
    - various different stats tests, parametric vs non-parametric?
- next run a fitting algorithm to extract the estimated distribution parameters (say mean and std of Gaussian) from the noisy data
    - scipy.optimize?
