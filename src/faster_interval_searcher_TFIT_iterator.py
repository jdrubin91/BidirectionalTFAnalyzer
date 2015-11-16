__author__ = 'Jonathan Rubin'

import os

if __name__ == "__main__":
    #Submits a job for each bidirectional file that finds motif distances to bidir sites for each TF in HOCOMOCO database
    fimodir = '/scratch/Users/joru1876/HOCOMOCODatabaseFIMO/FIMO_OUT'
    bidirDir = '/scratch/Shares/dowell/TFIT'
    
    for exp in os.listdir(bidirDir):
        print exp
        if exp != 'genome_files':
            if os.path.exists(bidirDir + '/' + exp + '/EMG_out_files'):
                bidirfileDir = bidirDir + '/' + exp + '/EMG_out_files'
                bidirfiles = [bidirfileDir + '/' + bidir for bidir in os.listdir(bidirfileDir) if 'bidirectional_hits' in bidir]
            else:
                bidirfileDir = bidirDir + '/' + exp
                bidirfiles = [bidirfileDir + '/' + bidir for bidir in os.listdir(bidirfileDir) if 'bidirectional_hits' in bidir]
    
            for bidirfile in bidirfiles:
                print bidirfile
                    
                os.system("qsub -v arg1='" + bidirfile + "',arg2='" + exp + "' /scratch/Users/joru1876/JDRScripts/faster_interval_searcher.sh")