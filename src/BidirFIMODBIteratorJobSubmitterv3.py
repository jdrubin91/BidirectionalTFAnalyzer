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
                start2,stop2,info = item
                i = (start+stop)/2
                x = (start2+stop2)/2
                intervalsearch.append((i-x,info))
            bidirsites[key].append((TF,intervalsearch))

        
    return bidirsites
    
    
if __name__ == "__main__":
    bidirfile = sys.argv[1]
    fimodir = sys.argv[2]
    outfiledir = sys.argv[3]
    
    bidirsites = run(bidirfile, fimodir)
    outfile = open(outfiledir + '/FIMO_OUT/' + bidirfile.split('/')[6][0:bidirfile.split('/')[6].index('.')] + '.txt', 'w')
    outfile.write("chrom\tstart\tstop\tTF:distance,(motif,pval,qval,strand)\n")
    for key in bidirsites:
        start,stop,chrom = key
        outfile.wirte(chrom + "\t" + str(start) + "\t" + str(stop) + "\t")
        for TF in bidirsites[key]:
            outfile.write(TF + ":")
            for distance in TF[1]:
                outfile.write(str(distance) + ",")
        outfile.write("\n")