"""Analyze all behavioural data"""

import os
import pandas as pd
from common import plot_rt, plot_rt_outcome, DATAPATH, RESULTSPATH

subjfnames = os.listdir(DATAPATH) # each subject should be a folder name

# plot reaction times separately for all experiments in all subjects:
dfs = []
for subjfname in subjfnames:
    subjectpath = os.path.join(DATAPATH, subjfname) # full path for this subject
    expfnames = os.listdir(subjectpath) # list all exp file names in this subj folder
    for expfname in expfnames:
        exppath = os.path.join(subjectpath, expfname) # full path for this experimenet
        print(exppath)
        df = pd.read_excel(exppath) # pandas DataFrame
        f, ax = plot_rt(df)
        expbasename, ext = os.path.splitext(expfname) # remove .xlsx extension
        ax.set_title(expbasename) # set axes title
        f.canvas.set_window_title(expbasename) # set figure window title
        f.savefig(os.path.join(RESULTSPATH, expbasename + '_rt.pdf'), format='pdf')
        dfs.append(df) # collect all experiment DataFrames

# plot average reaction time as a function of outcome, for all experiments in all subjects:
alldf = pd.concat(dfs)
f, ax = plot_rt_outcome(alldf)
ax.set_title('All Data') # set axes title
f.canvas.set_window_title('All Data') # set figure window title
f.savefig(os.path.join(RESULTSPATH, 'all_rt_outcome.pdf'), format='pdf')
