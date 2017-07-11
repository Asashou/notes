"""Defines functions and global variables commonly used by my scripts"""

import os
import matplotlib.pyplot as plt

# define some path names, use ALLCAPS to indicate that they're global variables
# whose values rarely change:
BASEPATH = '/home/mspacek/SciPyCourse2017/notes/11_organizing/separate'
DATAPATH = os.path.join(BASEPATH, 'data')
RESULTSPATH = os.path.join(BASEPATH, 'results')
FIGSIZE = (5, 3)

def plot_rt(df):
    """Plots reaction times across trials for each experiment DataFrame.
    Expects a pandas DataFrame as exp"""
    f, ax = plt.subplots(figsize=FIGSIZE)
    ax.plot(df['trial'], df['reaction_time'])
    f.set_tight_layout(True) # make figure automatically resize contents
    # disable top and right spines:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # set labels:
    ax.set_xlabel('Trial')
    ax.set_ylabel('Reaction Time (s)')
    return f, ax

def plot_rt_outcome(alldf):
    """Plots mean and stdev reaction times vs. trial outcome for all data in alldf"""
    f, ax = plt.subplots(figsize=FIGSIZE)
    mean = alldf.groupby('outcome')['reaction_time'].mean()
    std = alldf.groupby('outcome')['reaction_time'].std()
    mean.plot.bar(yerr=std)
    f.set_tight_layout(True) # make figure automatically resize contents
    # disable top and right spines:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # set labels:
    ax.set_xlabel('Outcome')
    ax.set_ylabel('Mean Reaction Time (s)')
    return f, ax
