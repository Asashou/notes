### statistics

- mpl hist vs np hist
- AJ had stats talk, gleaned from scipy.stats tutorial
- create distribution object, sample it to get data
    - plot pdf and cdf of sampled data, maybe add noise to it, or give it a slight offset?

    - then do some stats to test if it's significantly different from 0 (due to offset), or significantly different from some other distrib
    - various different stats tests, parametric vs non-parametric?
- next run a fitting algorithm to extract the estimated distribution parameters (say mean and std of Gaussian) from the noisy data
    - scipy.optimize?
