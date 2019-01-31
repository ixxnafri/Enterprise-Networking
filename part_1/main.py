#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("merged_updates.txt",
                   delimiter="|",
                   usecols=[2,3,4,5],
                   names=['AW','src_ip','AS','prefix'],
                   dtype={'AW':'str','src_ip':'str','AS':'int','prefix':'str'})

## Q1 ##
#counted = data[data['src_ip'] == "12.0.1.63"]
#print counted.groupby(['prefix'])['prefix']
#             .count()
#             .reset_index(name='count')
#             .sort_values(['count'],ascending=False)

## Q2 ##
#counted = data.groupby(['AS'])['AS'].count().reset_index(name='count').sort_values(['count'],ascending=True)
#counted.unstack().plot()
#plt.legend(ncol=14,loc='upper center',bbox_to_anchor=(0.5,1.15))
#plt.show()

## Q3 ##
#counted_vp_1 = data[data['src_ip'] == "208.51.134.246"].drop_duplicates(subset='prefix')
#
#counted_vp_2 = data[data['src_ip'] == "67.17.82.114"].drop_duplicates(subset='prefix')
#print counted_vp_1
#print counted_vp_2
#diff = pd.concat([counted_vp_1,counted_vp_2]).drop_duplicates(subset='prefix',keep=False).sort_values(['prefix'])
#print diff
#diff.to_csv('diff_AS3549',index=False)

## Q4 ## get rank of prefixes
#counted = data[data['AW'] == "A"].drop_duplicates(subset=['src_ip','prefix'])
#print counted
#counted = counted.groupby(['AS'])['AS'].count().reset_index(name='prefixes_announced').sort_values(['prefixes_announced'],ascending=False)
#counted.to_csv('count_prefix_announced.csv',index=False)
#print counted

## Q4 ## get sorted list of prefixes from top ranked AS
#counted = data[(data['AS'] == 3130) & (data['AW'] == "A")].drop_duplicates(subset=['prefix']).sort_values(['prefix'],ascending=False)
#counted.to_csv('sorted_prefixes_AS3130',index=False)
#print counted

## Q5 ## look for bogons "10.0.0.0/8","172.16.0.0/12","192.168.0.0/16"
#counted = data[(data['prefix'].str.contains('^10\.')) | (data['prefix'].str.contains('^172\.16\.')) | (data['prefix'].str.contains('^192\.168\.'))]
#print counted

# Count AS with most withdrawals
#counted = data[data['AW'] == 'W'].groupby(['AS'])['AS'].count().reset_index(name='count').sort_values(['count'],ascending=False)
#counted.to_csv('least_withdrawals.csv',index=False)

