__author__ = 'Jonathan Rubin'

import numpy as np
import Depletion_Simulatorv2 as ds
import matplotlib.pyplot as plt

filedir = 'C:/Users/Jonathan/Google Drive/Colorado University/Taatjes-Dowell Lab/BidirectionalTFAnalyzer/Danko2013_E2_25-1_bidirectional_hits_intervals.EM.txt'
TF = 'FOXA1'

with open(filedir) as file1:
    for line in file1:
        if TF in line:
            y = line.strip().split()[5].split(',')[:-1]

x = list()
for item in y:
    x.append(float(item))

bins = 200
#F = plt.figure()
#ax1 = F.add_subplot(1,2,1)
#ax2 = F.add_subplot(1,2,2)
#ax1.hist(x,bins=bins)
#
#counts,edges 	= np.histogram(x, bins=bins)
#X 	= np.zeros((bins,2))
#X[:,0] 	= edges[1:]
#X[:,1] 	= counts

counts,edges 	= np.histogram(x, bins=200)
edges 			= edges[1:]
X 				= np.zeros((len(counts), 2))
X[:,0] 			= edges
X[:,1] 			= counts

print ds.get_w(X)