#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

def apply_mask16(string):
    arr = string.split('.')
    return str(arr[0]+'.'+arr[1]+'.0.0')

data = pd.read_csv("netflowOutput.txt",delimiter=",",header=0,dtype={'srcport':'int','dstport':'int'})

# Q2 #
#data_bt = data[((data['srcport'] >= 6881) & (data['srcport'] <= 6999)) |
#               ((data['dstport'] >= 6881) & (data['dstport'] <= 6999))]

#data_web = data[(data['srcport'] == 80) | (data['dstport'] == 80)]

# Q3 #
doctets_sum = data['doctets'].sum()
doctets = data['doctets'].apply(lambda x: float(x)/doctets_sum)
plt.plot(doctets.sort_values(ascending=False).reset_index(drop=True).cumsum())
plt.title('CDF of DOCTETS(BYTES)')
plt.show()

dpkts_sum = data['dpkts'].sum()
dpkts = data['dpkts'].apply(lambda x: float(x)/dpkts_sum)
plt.plot(dpkts.sort_values(ascending=False).reset_index(drop=True).cumsum())
plt.title('CDF of DPKTS(NUMBER OF PACKETS)')
plt.show()

# Q4 #
#top_pre = data[(data['src_as'] == 680) & (data['dst_mask'] == 16)]
## apply /16 masks
#top_pre['dstaddr'] = top_pre['dstaddr'].apply(lambda x: apply_mask16(x))
#print top_pre
## sort by occurances
#top_pre = top_pre.groupby(['dstaddr'])['dstaddr'].count().sort_values(ascending=False)
#print top_pre

# Q5 #
#top_AS = data[(data['dst_as'] == 680) & (data['src_mask'] == 16)]
## apply /16 masks
#top_AS['srcaddr'] = top_AS['srcaddr'].apply(lambda x: apply_mask16(x))
## sort by occurances
#top_AS = top_AS.groupby(['srcaddr'])['srcaddr'].count().sort_values(ascending=False)
#print top_AS
