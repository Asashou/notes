### statistics


- we've already done some stats using the numpy library:
    - `import numpy as np`
    - `x = np.random.random(n)` - what does this do?
    - returns `n` *continuous* (float) values evenly distributed over the interval `[0, 1)`
    - this is called a continuous uniform random distribution
    - `y = np.random.randint(minval, maxval, n)` - what does this do?
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
        x = np.random.normal(mu, sigma, 1000)
        f, ax = plt.subplots()
        ax.hist(x, bins=30)````
    - what if your data are bimodally distributed (having 2 peaks) like this?:
        ```python
        x1 = np.random.normal(0, 1, 1000)
        x2 = np.random.normal(5, 0.5, 1000)
        # confirm we got what we asked for:
        x1.mean()
        x1.std()
        x2.mean()
        x2.std()
        x = np.concatenate([x1, x2])
        f, ax = plt.subplots()
        ax.hist(x, bins=40)
        ````
        - are `x.mean()` and `x.std()` meaningful? no! they're poor descriptors of this bimodal distribution, but the only way to tell is to plot and inspect it.

- mpl hist vs np hist
- AJ had stats talk, gleaned from scipy.stats tutorial
- create distribution object, sample it to get data
    - plot pdf and cdf of sampled data, maybe add noise to it, or give it a slight offset?
    - then do some stats to test if it's significantly different from 0 (due to offset), or significantly different from some other distrib
    - various different stats tests, parametric vs non-parametric?
- next run a fitting algorithm to extract the estimated distribution parameters (say mean and std of Gaussian) from the noisy data
    - scipy.optimize?
