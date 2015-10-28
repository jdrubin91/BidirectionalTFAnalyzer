__author__ = 'Jonathan Rubin'

import os
import sys
import Functions
import numpy as np
import math
import scipy.stats
from operator import itemgetter
import node

#This code will be used by BidirFIMODBIteratorv2 to submit jobs to pando

def run(bidirfile, fimodir):
    
    distances = dict()
    directorylist = [fimodir + '/' + item for item in os.listdir(fimodir) if 'fimo_out' in item]
    bidirsites = Functions.create_site_bidir(bidirfile)
    for item in directorylist:
        print item
        TF = item.split('/')[5].split('_')[0]
        fimodict = Functions.create_tup_fimo(item + "/fimo.cut.txt", True)
        for key in bidirsites:
            start,stop,chrom = key
            fimotree = fimodict[chrom]
            fimotree = node.tree(fimotree)
            intervalsearch = []
            for item in fimotree.searchInterval(key):
                start2,stop2,pval = item
                i = (start+stop)/2
                x = (start2+stop2)/2
                intervalsearch.append((i-x,pval))
            bidirsites[key].append((TF,intervalsearch))

        x = Functions.get_distances_pad_v3(bidirfile, item + "/fimo.cut.txt", True, 1500)
        if len(x) != 0:
            start = min(x)
            stop = max(x)
            sigma = np.std(x)
            mu = np.mean(x)
            N = len(x)
            #y = np.random.uniform(start, stop, N)
            y = np.linspace(start,stop,N)
            z = mu/(sigma/math.sqrt(N))
            p = 1 - scipy.special.ndtr(z)
            k = scipy.stats.ks_2samp(x,y)
            m = scipy.stats.mode(x)[0][0]
            if -0.25 < m < 0.25:
                m = 0
            else:
                m = 1
            distances[TF] = [k[1],p,m]
        
    return distances,bidirsites
    
    
if __name__ == "__main__":
    bidirfile = sys.argv[1]
    fimodir = sys.argv[2]
    outfiledir = sys.argv[3]
    
    distances,bidirsites = run(bidirfile, fimodir)
    print bidirsites
    sorted_distances = sorted(distances.items(), key=itemgetter(1))
    outfile = open(outfiledir + '/FIMO_OUT/' + bidirfile.split('/')[6][0:bidirfile.split('/')[6].index('.')] + '.txt', 'w')
    outfile.write("TF\tUniform p-val\tCentered(0) p-val\tBimodality (1=True)\tDistance List\n")
    for item in sorted_distances:
        outfile.write(str(item[0]))
        outfile.write("\t")
        outfile.write(str(item[1][0]))
        outfile.write("\t")
        outfile.write(str(item[1][1]))
        outfile.write("\t")
        outfile.write(str(item[1][2]))
        outfile.write("\t")
        for val in item[1][3]:
            outfile.write(str(val))
            outfile.write(",")
        outfile.write("\n")
    
    outfile.write("#########################################################################\n")
    outfile.write("#Bidirectional Sites#\n")
    outfile.write("chrom\tstart\tstop\tTF:distance,p-val\n")
    for key in bidirsites:
        start,stop,chrom = key
        outfile.wirte(chrom + "\t" + str(start) + "\t" + str(stop) + "\t")
        for TF in bidirsites[key]:
            outfile.write(TF + ":")
            for distance in TF[1]:
                outfile.write(str(distance) + ",")
        outfile.write("\n")