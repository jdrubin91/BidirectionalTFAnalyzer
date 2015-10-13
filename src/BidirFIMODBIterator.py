__author__ = 'Jonathan Rubin'

import os
import Functions
import numpy as np
import math
import scipy
from operator import itemgetter

def run(bidirfile, fimodir):
    
    distances = dict()
    directorylist = [fimodir + item for item in os.listdir(fimodir) if 'fimo_out' in item]
    for item in directorylist:
        print item
        TF = item.split('/')[5].split('_')[0]
        os.chdir(item)
        TF = item.split('/')[5].split('_')[0]
        x = Functions.get_distances_pad_v3(bidirfile, "fimo.cut.txt", True, 1500)
        start = min(x)
        stop = max(x)
        sigma = np.std(x)
        mu = np.mean(x)
        N = len(x)
        y = np.random.uniform(start, stop, N)
        z = mu/(sigma/math.sqrt(N))
        p = 1 - scipy.special.ndtr(z)
        k = scipy.stats.ks_2samp(x,y)
        m = scipy.stats.mode(x)[0][0]
        if -0.25 < m < 0.25:
            m = 0
        else:
            m = 1
        distances[TF] = [k[1],p,m,x]
        
        return distances
        
if __name__ == "__main__":
    fimodir = '/Users/joru1876/HOCOMOCODatabaseFIMO/FIMO_OUT'
    bidirDir = '/projects/dowellLab/TFIT'
    
    for exp in os.listdir(bidirDir):
        if exp != 'genome_files':
            bidirfileDir = bidirDir + '/' + exp + '/EMG_out_files'
            bidirfiles = [bidirfileDir + '/' + bidir for bidir in os.listdir(bidirfileDir) if 'bidirectional_hits' in bidir]
    
    for bidirfile in bidirfiles:
        if 'bidirectional_hits' in bidirfile:
            outfiledir = Functions.get_parent_dir(Functions.get_parent_dir(bidirfile))
            if not os.path.exists(outfiledir + '/FIMO_OUT'):
                os.makedir(outfiledir + '/FIMO_OUT')
            distances = run(bidirfile, fimodir)
            sorted_distances = sorted(distances.items(), key=itemgetter(1))
            outfile = open(outfiledir + '/FIMO_OUT/TFDatabaseAnalysis.txt', 'w')
            outfile.write("TF\tUniform p-val\tCentered(0) p-val\tBimodality (1=True)\tDistance List")
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
                    
            
            