__author__ = 'Jonathan Rubin'

import os
import sys
import Functions
import numpy as np
import math
import scipy.stats
from operator import itemgetter
import EM_algorithm as em
import Depletion_Simulator as ds
import Depletion_Simulatorv2 as ds2

#This code will be used by BidirFIMODBIteratorv2 to submit jobs to pando

def run(bidirfile, fimodir):
    
    distances = dict()
    directorylist = [fimodir + '/' + item for item in os.listdir(fimodir) if 'fimo_out' in item]
    for item in directorylist:
        print item
        TF = item.split('/')[6].split('_')[0]
        x = Functions.get_distances_pad_v3(bidirfile, item + "/fimo.cut.txt", True, 1500)
        for i in range(len(x)):
            x[i] = x[i]*1500
            
        if len(x) != 0:
            counts,edges 	= np.histogram(x, bins=200)
            edges 			= edges[1:]
            X 				= np.zeros((len(counts), 2))
            X[:,0] 			= edges
            X[:,1] 			= counts
            w = em.fit(X)
            w2 = ds2.get_w(X)
            ks = list()
            for a in range(1000):
                d = ds.simulate
                ks.append(scipy.stats.ks_2samp(x,d))
            d = np.mean(ks)
            start = min(x)
            stop = max(x)
            sigma = np.std(x)
            mu = np.mean(x)
            N = len(x)
            y = np.random.uniform(start, stop, N)
            y = np.linspace(start,stop,N)
            z = mu/(sigma/math.sqrt(N))
            p = 1 - scipy.special.ndtr(z)
            k = scipy.stats.ks_2samp(x,y)
            m = scipy.stats.mode(x)[0][0]
            if -0.25 < m < 0.25:
                m = 0
            else:
                m = 1
            distances[TF] = [w,w2,k[1],d,p,m,x]
        
    return distances
    
    
if __name__ == "__main__":
    bidirfile = sys.argv[1]
    fimodir = sys.argv[2]
    outfiledir = sys.argv[3]
    
    distances = run(bidirfile, fimodir)
    
    sorted_distances = sorted(distances.items(), key=itemgetter(1))
    outfile = open(outfiledir + '/FIMO_OUT/' + bidirfile.split('/')[7][0:bidirfile.split('/')[7].index('.')] + '.EM.txt', 'w')
    outfile.write("TF\tSignal/Noise Normal\tSignal/Noise Depletion\tUniform p-val\tDepletion p-val\tCentered(0) p-val\tBimodality (1=True)\tDistance List")
    outfile.write("\n")
    for item in sorted_distances:
        outfile.write(str(item[0]))
        outfile.write("\t")
        outfile.write(str(item[1][0]))
        outfile.write("\t")
        outfile.write(str(item[1][1]))
        outfile.write("\t")
        outfile.write(str(item[1][2]))
        outfile.write("\t")
        outfile.write(str(item[1][3]))
        outfile.write("\t")
        outfile.write(str(item[1][4]))
        outfile.write("\t")
        for val in item[1][5]:
            outfile.write(str(val))
            outfile.write(",")
        outfile.write("\n")