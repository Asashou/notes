### clustering

- say you're doing a controlled experiment to test a specific hypothesis
    - you have treatment and control data, and you know which is which, i.e. if you plot your data, you know which colour to assign to each point
    - in that case, the question is "are my treatment data significantly different from control", and you use a stats test to answer that
    - there's no clustering required, because your data already come with built-in labels!

- sometimes you have a bunch of data, with no specific hypothesis that you're testing, no treatment vs. control
    - your data points come without labels, i.e. they're unclustered, all coloured the same
    - you might wonder if your data naturally fall into various clusters/categories, or if they're just one big continuous cloud of smoothly varying data points
    - if they **do** form clusters, then you should probably analyze each cluster separately instead of lumping all your data together
    - clustering is a type of exploratory data analysis

- first step is to plot your data
    - if it's low enough dimensionality (1 or 2 or maybe 3D), then you can inspect it visually and look for clusters
    - if it's very high-dimensional data (e.g. the activity of many simultaneously Ca-imaged neurons), then you'll have to do some dimension reduction before you can visually inspect your data
    - if you see clusters in your data, then one way to label each data point is to manually draw boundaries between clusters, but this can be tedious

- let's look at two example automated clustering methods, and test them on 2D data:

#### k-means algorithm:

- probably the most commonly used clustering algorithm

0. Randomly initialize a set of cluster centers (i.e. means)
1. Assign each data point to the nearest cluster
2. Update the position of each cluster center by taking the mean of the positions of all its member points. Go to 1.

- After enough iterations, cluster centers will stop moving, and cluster membership of each point will become stable.
- Simple, fast, but it has some limitations:
    - need to specify how many clusters you want it to find
        - that's what the 'k' in k-means refers to
    - because it uses only distance to assign points to clusters, it performs poorly for elongated clusters

- k-means demo and exercise

#### DBSCAN algorithm:

- density-based instead of just distance based
- does much better than k-means with clusters of different sizes and shapes
- it figures out the number of clusters automatically!


### dimension reduction

datasets.make_classification for generating high-D data with low-D embedded structure
