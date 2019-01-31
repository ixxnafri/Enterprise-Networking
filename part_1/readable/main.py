#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("q1_out.txt",delimiter="|",usecols=[2,5],names=['action','prefix'],dtype={'action':'str','prefix':'str'})

counted = data.groupby(['prefix'])['action'].count().reset_index(name='count').sort_values(['count'],ascending=True)
print counted
#counted.unstack().plot()

#plt.legend(ncol=14,loc='upper center',bbox_to_anchor=(0.5,1.15))

#plt.show()
