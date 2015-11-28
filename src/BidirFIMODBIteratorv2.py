__author__ = 'Jonathan Rubin'

import os
import Functions
import numpy as np
import math
import scipy.stats
from operator import itemgetter

def run(bidirfile, fimodir):
    
    distances = dict()
    directorylist = [fimodir + '/' + item for item in os.listdir(fimodir) if 'fimo_out' in item]
    for item in directorylist:
        print item
        TF = item.split('/')[5].split('_')[0]
        x = Functions.get_distances_pad_v3(bidirfile, item + "/fimo.cut.txt", True, 1500)
        if len(x) != 0:
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
    

##This file is used to submit jobs to calculate distances for all HOCOMOCO TFs for each bidirectional file in a directory 
if __name__ == "__main__":
   
    #Submits a job for each bidirectional file that finds motif distances to bidir sites for each TF in HOCOMOCO database
    fimodir = '/scratch/Users/joru1876/HOCOMOCODatabaseFIMO/FIMO_OUT'
    bidirDir = '/scratch/Shares/dowell/TFIT/Danko2013'
    
    #for exp in os.listdir(bidirDir):
    #    print exp
    #    if exp != 'genome_files':
    #        if os.path.exists(bidirDir + '/' + exp + '/EMG_out_files'):
    #            bidirfileDir = bidirDir + '/' + exp + '/EMG_out_files'
    #            bidirfiles = [bidirfileDir + '/' + bidir for bidir in os.listdir(bidirfileDir) if 'bidirectional_hits' in bidir]
    #        else:
    #            bidirfileDir = bidirDir + '/' + exp
    #            bidirfiles = [bidirfileDir + '/' + bidir for bidir in os.listdir(bidirfileDir) if 'bidirectional_hits' in bidir]
    #
    #        for bidirfile in bidirfiles:
    #            print bidirfile
    #            if 'EMG_out_files' in bidirfile:
    #                outfiledir = Functions.parent_dir(Functions.parent_dir(bidirfile))
    #            else:
    #                outfiledir = Functions.parent_dir(bidirfile)
    #            if not os.path.exists(outfiledir + '/FIMO_OUT'):
    #                os.mkdir(outfiledir + '/FIMO_OUT')
                    
    for exp in os.listdir(bidirDir):
        if 'bidirectional_hits_intervals' in exp:
            bidirfile = bidirDir + '/' + exp
            print bidirfile
            outfiledir = bidirDir
            #os.system("qsub -v arg1='" + bidirfile + "',arg2='" + fimodir + "',arg3='" + outfiledir + "' /scratch/Users/joru1876/JDRScripts/runBidirHOCOMOCOTemplate.sh")
                    
            
            